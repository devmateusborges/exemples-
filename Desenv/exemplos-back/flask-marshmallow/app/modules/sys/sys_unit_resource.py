from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_unit_service import sys_unit_service

from app.modules.sys.base.sys_serealizer import SysUnitSchema
from app.modules.sys.base.sys_model import SysUnit


routes_sys_unit = Blueprint('sysunit', __name__,url_prefix="/api/sysunit")

#==============================
@routes_sys_unit.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_unit_service(SysUnit)
    result = srv.find_all()
    resultJson = SysUnitSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_unit.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_unit_service(SysUnit)
    result = srv.find_by_id(id)
    resultJson = SysUnitSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_unit.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_unit_service(SysUnit)    
    
    try:
        obj = SysUnitSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)     
    current_app.db.session.commit()
    resultJson = SysUnitSchema().jsonify(result)
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_unit.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_unit_service(SysUnit)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204



