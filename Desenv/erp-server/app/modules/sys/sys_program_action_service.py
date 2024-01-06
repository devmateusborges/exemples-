from app.generics.generic_service import generic_service
from app.modules.sys.base.sys_sql import (
    SQL_SYS_PROGRAM_ACTION_ACESSO,
    SQL_SYS_PROGRAM_ACTION_ACESSO_FIELD,
)

from app.utils.funcs_sql import funcs_sql


class sys_program_action_service(generic_service):

    # ==============================
    def get_by_user_login(self, session, pfilters=None):
        result = funcs_sql.getResultSql(
            SQL_SYS_PROGRAM_ACTION_ACESSO.format(
                pvuserlogin=funcs_sql.getFieldFilter(
                    pfilters, ["filter", "and", "login"]
                ),
                pvsysprogramid=pfilters["filter"]["and"]["pvsysprogramid"],
            ),
            SQL_SYS_PROGRAM_ACTION_ACESSO_FIELD,
            session,
        )

        return result
