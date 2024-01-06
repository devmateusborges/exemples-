from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_user_group_service import sys_user_group_service

from app.modules.sys.base.sys_serealizer import SysUserGroupSchema
from app.modules.sys.base.sys_model import SysUserGroup


routes_sys_user_group = Blueprint('sysusergroup', __name__,url_prefix="/api/sysusergroup")

#==============================
@routes_sys_user_group.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_user_group_service(SysUserGroup)
    result = srv.find_all()
    resultJson = SysUserGroupSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_user_group.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_user_group_service(SysUserGroup)
    result = srv.find_by_id(id)
    resultJson = SysUserGroupSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_user_group.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_user_group_service(SysUserGroup)    
    
    try:
        obj = SysUserGroupSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)     
    current_app.db.session.commit()
    resultJson = SysUserGroupSchema().jsonify(result)
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_user_group.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_user_group_service(SysUserGroup)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204
