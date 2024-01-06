import datetime
import json
from app.exceptions.ApiException import ApiException
from app.generics.generic_model import gen_uuid

from app.modules.sys.base.sys_model import SysToken


class sys_token_service:
    # ==============================
    def get_token(self, token, session):
        token = session.query(SysToken).filter(SysToken.token == token).first()
        if token is None:
            raise ApiException(
                message="Token not exist", name="TOKEN_INVALID", status_code=400
            )
        if token.dt_validade < datetime.datetime.now():
            raise ApiException(
                message="Token expired", name="TOKEN_INVALID", status_code=400
            )

        if token.dt_used is not None:
            raise ApiException(
                message="Token used", name="TOKEN_INVALID", status_code=400
            )

        token.dt_used = datetime.datetime.now()
        session.merge(token)
        token.data_token = json.loads(token.data_token)
        return token

    # ==============================
    def generate_token(self, session, hours=24, data_token=None):
        if hours <= 0:
            raise ApiException(
                message="Hours negative", name="TOKEN_INVALID", status_code=400
            )

        try:
            data_token_aux = json.dumps(data_token)
        except Exception as e:
            raise ApiException(
                message="Data token invalid", name="TOKEN_INVALID", status_code=400
            )

        token = SysToken(
            token=gen_uuid(),
            dt_validade=datetime.datetime.now() + datetime.timedelta(hours=hours),
            data_token=data_token_aux,
        )
        session.add(token)

        return token.token
