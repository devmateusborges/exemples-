from datetime import datetime
import uuid
from sqlalchemy import TIMESTAMP, Column, String
from flask_jwt_extended import current_user
from flask_jwt_extended import verify_jwt_in_request

def gen_uuid():
    return str(uuid.uuid4())

def get_login():
    try:
        if verify_jwt_in_request():
            return current_user.user.login
    except Exception as e:
        return "anonymus"    

    return "anonymus"

def get_now():
    return datetime.now()

class generic_model(object):
    id =  Column(String(36), name='id', primary_key=True, default=gen_uuid, comment='ID')
    log_user_ins = Column(String(100), default=get_login, comment='Log - Usuário de Inserção')
    log_date_ins = Column(TIMESTAMP, default=get_now, comment='Log - Data de Inserção')
    log_user_upd = Column(String(100), onupdate=get_login, comment='Log - Usuário de Alteração')
    log_date_upd = Column(TIMESTAMP,  onupdate=get_now, comment='Log - Data de Alteração')  