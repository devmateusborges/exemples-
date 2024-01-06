from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_restriction_licence_service import sys_restriction_licence_service

from app.modules.sys.base.sys_serealizer import SysRestrictionLicenceSchema
from app.modules.sys.base.sys_model import SysRestrictionLicence


routes_sys_restriction_licence = Blueprint('sysrestrictionlicence', __name__,url_prefix="/api/sysrestrictionlicence")



#==============================
@routes_sys_restriction_licence.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_restriction_licence_service(SysRestrictionLicence)
    result = srv.find_all()
    resultJson = SysRestrictionLicenceSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_restriction_licence.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_restriction_licence_service(SysRestrictionLicence)
    result = srv.find_by_id(id)
    resultJson = SysRestrictionLicenceSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_restriction_licence.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_restriction_licence_service(SysRestrictionLicence)    
    
    try:
        obj = SysRestrictionLicenceSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj) 
    current_app.db.session.commit()    
    resultJson = SysRestrictionLicenceSchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_restriction_licence.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_restriction_licence_service(SysRestrictionLicence)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

