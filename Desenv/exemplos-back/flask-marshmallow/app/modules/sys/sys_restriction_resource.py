from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_restriction_service import sys_restriction_service

from app.modules.sys.base.sys_serealizer import SysRestrictionSchema
from app.modules.sys.base.sys_model import SysRestriction


routes_sys_restriction = Blueprint('sysrestriction', __name__,url_prefix="/api/sysrestriction")


#==============================
@routes_sys_restriction.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_restriction_service(SysRestriction)
    result = srv.find_all()
    resultJson = SysRestrictionSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_restriction.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_restriction_service(SysRestriction)
    result = srv.find_by_id(id)
    resultJson = SysRestrictionSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_restriction.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_restriction_service(SysRestriction)    
    
    try:
        obj = SysRestrictionSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)     
    current_app.db.session.commit()
    resultJson = SysRestrictionSchema().jsonify(result)
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_restriction.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_restriction_service(SysRestriction)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

