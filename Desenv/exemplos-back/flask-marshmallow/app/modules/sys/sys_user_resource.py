from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_user_service import SysUser_service

from app.modules.sys.base.sys_serealizer import SysUserSchema
from app.modules.sys.base.sys_model import SysUser


routes_sys_user = Blueprint('sysuser', __name__,url_prefix="/api/sysuser")


@routes_sys_user.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = SysUser_service(SysUser)
    result = srv.find_all()
    resultJson = SysUserSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_user.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = SysUser_service(SysUser)
    result = srv.find_by_id(id)
    resultJson = SysUserSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_user.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = SysUser_service(SysUser)    
    
    try:
        obj = SysUserSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj) 
    current_app.db.session.commit()    
    resultJson = SysUserSchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_user.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = SysUser_service(SysUser)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

