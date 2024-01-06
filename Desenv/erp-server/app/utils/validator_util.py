from marshmallow.validate import Validator, _T
from sqlalchemy.orm import class_mapper
from app.exceptions.ApiException import ApiException
from flask import current_app
from app.modules.sys.base.sys_model import SysTypeDescription

# ==============================


class validator_util:
    @staticmethod
    def valid_unique_fields(obj, model, unique_fields, db_session):
        filters = []
        filters_msg = ""
        # Busca colunas para serem incluidas como filtro unique
        for col in unique_fields:
            col_mapper = class_mapper(model)
            if not hasattr(col_mapper.columns, col):
                continue
            filters.append(col_mapper.columns[col].__eq__(getattr(obj, col)))
            filters_msg += (
                col_mapper.columns[col].name + "=" + str(getattr(obj, col)) + ","
            )

        filters_msg = filters_msg[0 : (len(filters_msg) - 1)]

        # Busca registro com ID diferente para validar unique
        filters.append(col_mapper.columns["id"].__ne__(getattr(obj, "id")))

        objUnique = db_session.query(model).filter(*filters).first()

        if objUnique is not None:
            return {"unique": True, "msg": filters_msg}
        else:
            return {"unique": False, "msg": None}


# ==============================


class valid_type_choice(Validator):

    default_message = """Value [{input}] valid is {values}."""

    def __init__(self, type_choice, *, error: str = ""):
        self.type_choice = type_choice
        self.error = error or self.default_message

    def _repr_args(self) -> str:
        return f"type_choice={self.type_choice!r}"

    def _format_error(self, value: _T) -> str:
        return self.error.format(input=value, values=self.type_choice)

    def __call__(self, value: _T) -> _T:
        valid_error = True
        for item in self.type_choice:
            if item[0] == value:
                valid_error = False
        if valid_error:
            raise ApiException(
                message={"error": self._format_error(value)},
                name="VALIDATION_ERROR",
                status_code=400,
            )
        return value


# ==============================


class valid_type_choice_sql(Validator):

    default_message = """Value [{input}] valid is {values}."""

    def __init__(self, table_name, field_name, session, *, error: str = ""):
        self.table_name = table_name
        self.field_name = field_name
        self.session = session
        self.error = error or self.default_message

    def _repr_args(self) -> str:
        return f"table_name={self.table_name!r}"

    def _format_error(self, value: _T) -> str:
        cache_key = f"VALIDATOR-{self.table_name}-{self.field_name}"
        cache_types = current_app.cache.get(cache_key)
        if cache_types is None:
            typeValues = (
                self.session.query(SysTypeDescription.value_type)
                .filter(
                    SysTypeDescription.table_name == self.table_name,
                    SysTypeDescription.field_name == self.field_name,
                )
                .all()
            )
            cache_types = [value for (value,) in typeValues]
            current_app.cache.set(cache_key, cache_types)

        return self.error.format(input=value, values=cache_types)

    def __call__(self, value: _T) -> _T:
        valid_error = True

        cache_key = f"VALIDATOR-COUNT-{self.table_name}-{self.field_name}"
        cache_types = current_app.cache.get(cache_key)
        if cache_types is None:
            cache_types = SysTypeDescription.query.filter_by(
                table_name=self.table_name,
                field_name=self.field_name,
                value_type=str(value),
            ).count()
            current_app.cache.set(cache_key, cache_types)

        if cache_types > 0:
            valid_error = False

        if valid_error:
            raise ApiException(
                message={"error": self._format_error(value)},
                name="VALIDATION_ERROR",
                status_code=400,
            )
        return value
