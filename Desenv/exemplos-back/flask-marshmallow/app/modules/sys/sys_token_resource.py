from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_token_service import sys_token_service

from app.modules.sys.base.sys_serealizer import SysTokenSchema
from app.modules.sys.base.sys_model import SysToken


routes_sys_token = Blueprint('systoken', __name__,url_prefix="/api/systoken")



#==============================
@routes_sys_token.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_token_service(SysToken)
    result = srv.find_all()
    resultJson = SysTokenSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_token.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_token_service(SysToken)
    result = srv.find_by_id(id)
    resultJson = SysTokenSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_token.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_token_service(SysToken)    
    
    try:
        obj = SysTokenSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)   
    current_app.db.session.commit()  
    resultJson = SysTokenSchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_token.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_token_service(SysToken)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

 