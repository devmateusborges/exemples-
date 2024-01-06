from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_licence_service import sys_licence_service

from app.modules.sys.base.sys_serealizer import SysLicenceSchema
from app.modules.sys.base.sys_model import SysLicence


routes_sys_licence = Blueprint('syslicence', __name__,url_prefix="/api/syslicence")


#==============================
@routes_sys_licence.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_licence_service(SysLicence)
    result = srv.find_all()
    resultJson = SysLicenceSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_licence.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_licence_service(SysLicence)
    result = srv.find_by_id(id)
    resultJson = SysLicenceSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_licence.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_licence_service(SysLicence)    
    
    try:
        obj = SysLicenceSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)
    current_app.db.session.commit()     
    resultJson = SysLicenceSchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_licence.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_licence_service(SysLicence)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

