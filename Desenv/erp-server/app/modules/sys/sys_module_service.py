from app.generics.generic_service import generic_service
from app.modules.sys.base.sys_sql import (
    SQL_SYS_MODULE_BY_USER_LOGIN,
    SQL_SYS_MODULE_BY_USER_LOGIN_FIELD,
)
from app.utils.funcs_sql import funcs_sql


class sys_module_service(generic_service):
    pass

    # ==============================
    def get_by_user_login(self, session, pfilters=None):
        result = funcs_sql.getResultSql(
            SQL_SYS_MODULE_BY_USER_LOGIN.format(
                pvuserlogin=funcs_sql.getFieldFilter(
                    pfilters, ["filter", "and", "login"]
                ),
                pvsysprogramadmin="N",
                pvsysprogrammenu="S",
                pvsysprogramfavorite="N",
                pvsysprogramid="%",
            ),
            SQL_SYS_MODULE_BY_USER_LOGIN_FIELD,
            session,
        )

        return result
