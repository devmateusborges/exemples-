from app.modules.ind.base.ind_sql import (
    SQL_IND_GRUPO_SUBGRUPO,
    SQL_IND_GRUPO_SUBGRUPO_FIELD,
    SQL_IND_INDIC,
    SQL_IND_INDIC_FIELD,
    SQL_IND_PER,
    SQL_IND_PER_FIELD,
    SQL_IND_VALOR,
    SQL_IND_VALOR_FIELD,
)
from app.utils.funcs_util import funcs_util
from app.utils.funcs_sql import funcs_sql


class ind_dash_service:
    # ==============================
    def get_indics(self, session, punitid, pfilters=None):
        vuserlogin = funcs_sql.getFieldFilter(pfilters, ["filter", "and", "login"])
        funcs_util.ExceptionRequiredValue(vuserlogin, "User login")
        vindsubgrupoid = funcs_sql.getFieldFilter(
            pfilters, ["filter", "and", "pvindsubgrupoid"], "%"
        )

        result = funcs_sql.getResultSql(
            SQL_IND_INDIC.format(
                pvuserlogin=vuserlogin, pvunitid=punitid, pvindsubgrupoid=vindsubgrupoid
            ),
            SQL_IND_INDIC_FIELD,
            session,
        )

        return result

    # ==============================
    def get_pers(self, session, punitid, pfilters=None):
        vuserlogin = funcs_sql.getFieldFilter(pfilters, ["filter", "and", "login"])
        funcs_util.ExceptionRequiredValue(vuserlogin, "User login")

        vtipo = funcs_sql.getFieldFilter(pfilters, ["filter", "and", "pvtipo"], "DIA")

        vgerempresaids = funcs_sql.getFieldFilter(
            pfilters,
            ["filter", "and", "pvgerempresaids"],
            pDefault=None,
            pReplace=False,
        )
        funcs_util.ExceptionRequiredValue(vgerempresaids, "Empresas")

        vanos = funcs_sql.getFieldFilter(pfilters, ["filter", "and", "pvanos"])
        funcs_util.ExceptionRequiredValue(vanos, "Anos")

        result = funcs_sql.getResultSql(
            SQL_IND_PER.format(
                pvuserlogin=vuserlogin,
                pvunitid=punitid,
                pvtipo=vtipo,
                pvgerempresaids=vgerempresaids,
                pvanos=vanos,
            ),
            SQL_IND_PER_FIELD,
            session,
        )

        return result

    # ==============================
    def get_grupo_subgrupo(self, session, punitid, pfilters=None):
        vuserlogin = funcs_sql.getFieldFilter(pfilters, ["filter", "and", "login"])
        funcs_util.ExceptionRequiredValue(vuserlogin, "User login")

        result = funcs_sql.getResultSql(
            SQL_IND_GRUPO_SUBGRUPO.format(
                pvuserlogin=vuserlogin,
                pvunitid=punitid,
            ),
            SQL_IND_GRUPO_SUBGRUPO_FIELD,
            session,
        )

        return result

    # ==============================
    def get_valores(self, session, punitid, pfilters=None):
        vuserlogin = funcs_sql.getFieldFilter(pfilters, ["filter", "and", "login"])
        funcs_util.ExceptionRequiredValue(vuserlogin, "User login")

        vtipo = funcs_sql.getFieldFilter(pfilters, ["filter", "and", "pvtipo"], "DIA")

        vgerempresaids = funcs_sql.getFieldFilter(
            pfilters,
            ["filter", "and", "pvgerempresaids"],
            pDefault=None,
            pReplace=False,
        )
        funcs_util.ExceptionRequiredValue(vgerempresaids, "Empresas")

        vgerperids = funcs_sql.getFieldFilter(
            pfilters,
            ["filter", "and", "pvgerperids"],
            pDefault=None,
            pReplace=False,
        )
        funcs_util.ExceptionRequiredValue(vgerperids, "Período")

        vindindicid = funcs_sql.getFieldFilter(
            pfilters, ["filter", "and", "pvindindicid"], "%"
        )

        result = funcs_sql.getResultSql(
            SQL_IND_VALOR.format(
                pvuserlogin=vuserlogin,
                pvunitid=punitid,
                pvtipo=vtipo,
                pvgerempresaids=vgerempresaids,
                pvgerperids=vgerperids,
                pvindindicid=vindindicid,
            ),
            SQL_IND_VALOR_FIELD,
            session,
        )

        return result
