from app.generics.generic_service import generic_service

from app.utils.funcs_sql import funcs_sql
from app.modules.sys.base.sys_sql import (
    SQL_SYS_UNIT_BY_USER_LOGIN,
    SQL_SYS_UNIT_BY_USER_LOGIN_FIELD,
)


class sys_user_unit_service(generic_service):
    pass

    # ==============================
    def get_by_user_login(
        self,
        session,
        page=1,
        per_page=50,
        pfilters=None,
    ):

        result = funcs_sql.getResultSql(
            #TODO revisar hardcode pois a chamada web ja monta o filtro nao esta legal
            SQL_SYS_UNIT_BY_USER_LOGIN.format(
                pvuserlogin=funcs_sql.getFieldFilter(
                    pfilters, ["filter", "and", "login"]
                ),
                name=funcs_sql.getFieldFilter(pfilters, ["filter", "and", "name"]),
                id=funcs_sql.getFieldFilter(pfilters, ["filter", "or", "id"]),
            ),
            SQL_SYS_UNIT_BY_USER_LOGIN_FIELD,
            session,
            page=page,
            per_page=per_page,
        )

        return result
