from app.exceptions.ApiException import ApiException
from app.generics.generic_service import generic_service
from app.modules.sys.base.sys_model import SysUserPreference
from app.modules.sys.base.sys_serealizer import SysUserPreferenceSchema


class sys_user_preference_service(generic_service):
    def save(self, obj: SysUserPreference):

        if obj.id is None:
            vPrefDefault = SysUserPreference.query.filter_by(
                isdefault="S",
                sys_user_id=obj.sys_user_id,
                object_type=obj.object_type,
                object_id=obj.object_id,
                object_sub_id=obj.object_sub_id,
            ).one_or_none()

            if vPrefDefault is not None and obj.isdefault == "S":
                raise ApiException(
                    message={"error": f"Only one record can be default"},
                    name="VALIDATION_ERROR",
                    status_code=400,
                )

        return super().save(obj)
