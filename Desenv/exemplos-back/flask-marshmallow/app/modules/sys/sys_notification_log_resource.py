from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_notification_log_service import sys_notification_log_service

from app.modules.sys.base.sys_serealizer import SysNotificationLogSchema
from app.modules.sys.base.sys_model import SysNotificationLog


routes_sys_notification_log = Blueprint('sysnotificationlog', __name__,url_prefix="/api/sysnotificationlog")



#==============================
@routes_sys_notification_log.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_notification_log_service(SysNotificationLog)
    result = srv.find_all()
    resultJson = SysNotificationLogSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_notification_log.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_notification_log_service(SysNotificationLog)
    result = srv.find_by_id(id)
    resultJson = SysNotificationLogSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_notification_log.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_notification_log_service(SysNotificationLog)    
    
    try:
        obj = SysNotificationLogSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)   
    current_app.db.session.commit()  
    resultJson = SysNotificationLogSchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_notification_log.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_notification_log_service(SysNotificationLog)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

 