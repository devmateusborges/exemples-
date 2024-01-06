from datetime import datetime
import uuid
from sqlalchemy import TIMESTAMP, Column, String
from flask_jwt_extended import get_current_user


def gen_uuid():
    return str(uuid.uuid4())


def get_login():
    try:
        user = get_current_user()
        return user[0].login
    except Exception as e:
        return "anonymus"


def get_now():
    return datetime.now()


class generic_model(object):
    id = Column(String(36), name="id", primary_key=True, default=gen_uuid)
    log_user_ins = Column(String(100), default=get_login)
    log_date_ins = Column(
        TIMESTAMP,
        default=get_now,
    )
    log_user_upd = Column(String(100), onupdate=get_login)
    log_date_upd = Column(TIMESTAMP, onupdate=get_now)
