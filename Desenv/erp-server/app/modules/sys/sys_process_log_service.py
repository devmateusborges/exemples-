from app.generics.generic_service import generic_service
from app.modules.sys.base.sys_model import SysProcessLog
import uuid
from app.modules.sys.base.sys_serealizer import SysProcessLogSchema
from datetime import datetime
from flask import current_app


class sys_process_log_service(generic_service):
    def init(
        self, unitid, sysuserid, messageprocess, paramprocess, typeprocess, codeprocess
    ):
        data = SysProcessLog()

        data.id = str(uuid.uuid4())
        data.date_ini_process = datetime.now()
        data.unit_id = unitid
        data.type_process = typeprocess
        data.reversed = "N"
        data.param_process = paramprocess
        data.message_process = messageprocess
        data.sys_user_id = sysuserid
        data.code_process = codeprocess

        self.save(data)
        return data

    def finish(self, id, messageprocess, error):
        data = (
            current_app.db.session.query(SysProcessLog)
            .filter(SysProcessLog.id == id)
            .one_or_none()
        )

        data.date_fin_process = datetime.now()
        data.error = error
        data.message_process = messageprocess

        self.save(data)
        return data
