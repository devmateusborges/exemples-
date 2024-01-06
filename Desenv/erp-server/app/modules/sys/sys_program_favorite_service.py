# ====================================================================================
# Code Owner ..: EDUARDO JUNQUEIRA - ME - CNPJ: 12.138.668/0001-89
# Create_at ...: 01/01/2021
# History Update
# 30/09/2022 - EJ - Ajuste metodos retirando padrao deixando apenas customizados.
# ====================================================================================


from app.exceptions.ApiException import ApiException
from app.modules.sys.base.sys_model import SysProgram, SysProgramFavorite, SysUser

from app.modules.sys.base.sys_sql import (
    SQL_SYS_PROGRAM_BY_USER_LOGIN,
    SQL_SYS_PROGRAM_BY_USER_LOGIN_FIELD,
)
from app.utils.funcs_sql import funcs_sql


class sys_program_favorite_service:

    # ==============================
    def get_by_user_login(self, session, pfilters=None):

        result = funcs_sql.getResultSql(
            SQL_SYS_PROGRAM_BY_USER_LOGIN.format(
                pvuserlogin=funcs_sql.getFieldFilter(
                    pfilters, ["filter", "and", "login"]
                ),
                pvsysprogramadmin="%",
                pvsysprogrammenu="S",
                pvsysprogramfavorite="S",
                pvsysprogramid="%",
            ),
            SQL_SYS_PROGRAM_BY_USER_LOGIN_FIELD,
            session,
        )

        return result

    # ==============================
    def favotite(self, session, obj):

        user = SysUser.query.filter_by(id=obj["sys_user_id"]).one_or_none()
        if user is None:
            raise ApiException(message="User not exist", name="VALIDATION_ERROR")

        program = SysProgram.query.filter_by(id=obj["sys_program_id"]).one_or_none()
        if program is None:
            raise ApiException(message="Program not exist", name="VALIDATION_ERROR")

        if obj["favorite"] == "N":
            SysProgramFavorite.query.filter_by(
                sys_program_id=obj["sys_program_id"],
                sys_user_id=obj["sys_user_id"],
            ).delete()
            return {"code": "200", "msg": "Successfully unfavorited"}

        elif obj["favorite"] == "S":
            objSysProgramFavorite = SysProgramFavorite()
            objSysProgramFavorite.sys_program_id = obj["sys_program_id"]
            objSysProgramFavorite.sys_user_id = obj["sys_user_id"]
            session.add(objSysProgramFavorite)
            return {"code": "200", "msg": "Successfully favorited"}
