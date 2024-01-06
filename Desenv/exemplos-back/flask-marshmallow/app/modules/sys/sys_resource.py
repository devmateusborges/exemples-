from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_service import sys_service

from app.modules.sys.base.sys_serealizer import SysSchema
from app.modules.sys.base.sys_model import Sys

 
routes_sys = Blueprint('sys', __name__,url_prefix="/api/sys")


@routes_sys.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_service(Sys)
    result = srv.find_all()
    resultJson = SysSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_service(Sys)
    result = srv.find_by_id(id)
    resultJson = SysSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_service(Sys)    
    
    try:
        obj = SysSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj) 
    current_app.db.session.commit()    
    resultJson = SysSchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_service(Sys)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

