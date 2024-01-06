from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_email_log_service import sys_email_log_service

from app.modules.sys.base.sys_serealizer import SysEmailLogSchema
from app.modules.sys.base.sys_model import SysEmailLog


routes_sys_email_log = Blueprint('sysemaillog', __name__,url_prefix="/api/sysemaillog")



#==============================
@routes_sys_email_log.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_email_log_service(SysEmailLog)
    result = srv.find_all()
    resultJson = SysEmailLogSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_email_log.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_email_log_service(SysEmailLog)
    result = srv.find_by_id(id)
    resultJson = SysEmailLogSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_email_log.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_email_log_service(SysEmailLog)    
    
    try:
        obj = SysEmailLogSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)   
    current_app.db.session.commit()  
    resultJson = SysEmailLogSchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_email_log.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_email_log_service(SysEmailLog)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

 