from flask import current_app
from app.generics.generic_service import generic_service
from app.modules.sys.base.sys_model import SysNotificationToken


class sys_notification_token_service(generic_service):
    def save(self, obj: SysNotificationToken):
        if obj.token is not None:
            objOld = (
                current_app.db.session.query(SysNotificationToken)
                .filter(SysNotificationToken.token == obj.token)
                .first()
            )
            if objOld is not None:
                obj = objOld

        return super().save(obj)
