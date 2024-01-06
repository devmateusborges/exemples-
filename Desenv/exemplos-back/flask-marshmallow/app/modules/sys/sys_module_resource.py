from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_module_service import sys_module_service

from app.modules.sys.base.sys_serealizer import SysModuleSchema
from app.modules.sys.base.sys_model import SysModule


routes_sys_module = Blueprint('sysmodule', __name__,url_prefix="/api/sysmodule")


#==============================
@routes_sys_module.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_module_service(SysModule)
    result = srv.find_all()
    resultJson = SysModuleSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_module.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_module_service(SysModule)
    result = srv.find_by_id(id)
    
    current_app.db.session.commit()   
    resultJson = SysModuleSchema().jsonify(result) 
    current_app.db.session.close() 
    return resultJson, 200

#==============================
@routes_sys_module.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_module_service(SysModule)    
    
    try:
        obj = SysModuleSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj) 
    current_app.db.session.commit()   
    resultJson = SysModuleSchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_module.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_module_service(SysModule)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

