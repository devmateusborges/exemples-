import json
from app.generics.generic_service import generic_service
from app.utils.funcs_sql import funcs_sql
from app.modules.sys.sys_process_log_service import sys_process_log_service


class ger_per_service(generic_service):
    def generatePer(
        session, punitid, pgerpertipo, pgerempresaid, pano, psysuserid, pcodeprocess
    ):
        srvSysLog = sys_process_log_service(generic_service)

        sysLogObj = srvSysLog.init(
            unitid=punitid,
            sysuserid=psysuserid,
            messageprocess="Processing",
            paramprocess="",
            typeprocess="GER_PER_GENERATE",
            codeprocess=pcodeprocess,
        )

        session.commit()

        result = funcs_sql.execProcSql(
            sqlfunction="fnger_per_gerar(:pvunitid,:pvgerempresaid,:pvgerpertipo,:pvano,:pvsysuserid,:pvsysprocesslogid)",
            session=session,
            commit=True,
            pvunitid=punitid,
            pvgerpertipo=pgerpertipo,
            pvgerempresaid=pgerempresaid,
            pvano=pano,
            pvsysuserid=psysuserid,
            pvsysprocesslogid=sysLogObj.id,
        )

        resultLoad = json.loads(result)

        error = "N"
        messageprocess = resultLoad["msg"]

        if resultLoad["code"] != 200:
            error = "S"

        srvSysLog.finish(
            id=sysLogObj.id,
            error=error,
            messageprocess=messageprocess,
        )

        session.commit()

        return resultLoad
