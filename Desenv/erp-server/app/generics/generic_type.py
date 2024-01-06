from app.modules.sys.base.sys_model import SysTranslate, SysTypeDescription
from app.modules.sys.sys_translate_service import sys_translate_service
from ..exceptions.ApiException import ApiException
from flask import current_app


class generic_type:
    # ===============================
    @staticmethod
    def get_choices_obj(choices, value):
        for item in choices:
            if item[0] == value:
                return {"code": item[0], "description": item[1]}

    # ===============================
    @staticmethod
    def get_type_obj(obj, field_choice, type_choice):
        try:
            if type(obj) is dict:
                if obj[field_choice] is not None:
                    return generic_type.get_choices_obj(type_choice, obj[field_choice])
            else:
                if getattr(obj, field_choice) is not None:
                    return generic_type.get_choices_obj(
                        type_choice, getattr(obj, field_choice)
                    )
                else:
                    return {}
        except Exception as e:
            raise ApiException(
                message={
                    "error": f"Error get_type_obj: obj [{obj}] field_choice [{field_choice}] type_choice [{type_choice}] "
                },
                name="VALIDATION_ERROR",
                status_code=400,
            )

    # ===============================
    @staticmethod
    def get_type_obj_sql(
        obj,
        field_choice,
        table_name,
        field_name,
        session,
        load_default,
        lang,
    ):
        try:

            sysTranslateService = sys_translate_service(model=SysTranslate)

            value = None
            if type(obj) is dict:
                if field_choice in obj:
                    if obj[field_choice] is not None:
                        value = str(obj[field_choice])

                        cache_key = f"TYPE-OBJ-{table_name}-{field_name}"
                        cache_types = current_app.cache.get(cache_key)
                        if cache_types is None:
                            cache_types = SysTypeDescription.query.filter_by(
                                table_name=table_name,
                                field_name=field_name,
                                value_type=value,
                            ).first()
                            current_app.cache.set(cache_key, cache_types)

                        return {
                            "code": cache_types.value_type,
                            "description": sysTranslateService.get_term_translate(
                                lang, "DEFAULT", cache_types.description_type
                            ),
                        }
                else:
                    return load_default
            else:
                if getattr(obj, field_choice) is not None:
                    value = str(getattr(obj, field_choice))

                    cache_key = f"TYPE-OBJ-{table_name}-{field_name}"
                    cache_types = current_app.cache.get(cache_key)
                    if cache_types is None:
                        cache_types = SysTypeDescription.query.filter_by(
                            table_name=table_name,
                            field_name=field_name,
                            value_type=value,
                        ).first()
                        current_app.cache.set(cache_key, cache_types)
                    return {
                        "code": cache_types.value_type,
                        "description": sysTranslateService.get_term_translate(
                            lang, "DEFAULT", cache_types.description_type
                        ),
                    }
                else:
                    return load_default
        except Exception as e:
            raise ApiException(
                message={
                    "error": f"Error get_type_obj_sql: obj [{obj}] table_name [{table_name}] field_name [{field_name}] value [{value}] "
                },
                name="VALIDATION_ERROR",
                status_code=400,
                e_predecessor=e,
            )
