from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_change_log_service import sys_change_log_service

from app.modules.sys.base.sys_serealizer import SysChangeLogSchema
from app.modules.sys.base.sys_model import SysChangeLog


routes_sys_change_log = Blueprint('syschangelog', __name__,url_prefix="/api/syschangelog")



#==============================
@routes_sys_change_log.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_change_log_service(SysChangeLog)
    result = srv.find_all()
    resultJson = SysChangeLogSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_change_log.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_change_log_service(SysChangeLog)
    result = srv.find_by_id(id)
    resultJson = SysChangeLogSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_change_log.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_change_log_service(SysChangeLog)    
    
    try:
        obj = SysChangeLogSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)   
    current_app.db.session.commit()  
    resultJson = SysChangeLogSchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_change_log.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_change_log_service(SysChangeLog)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

 