from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_plan_restriction_service import sys_plan_restriction_service

from app.modules.sys.base.sys_serealizer import SysPlanRestrictionSchema
from app.modules.sys.base.sys_model import SysPlanRestriction


routes_sys_plan_restriction = Blueprint('sysplanrestriction', __name__,url_prefix="/api/sysplanrestriction")


#==============================
@routes_sys_plan_restriction.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_plan_restriction_service(SysPlanRestriction)
    result = srv.find_all()
    resultJson = SysPlanRestrictionSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_plan_restriction.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_plan_restriction_service(SysPlanRestriction)
    result = srv.find_by_id(id)
    resultJson = SysPlanRestrictionSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_plan_restriction.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_plan_restriction_service(SysPlanRestriction)    
    
    try:
        obj = SysPlanRestrictionSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)  
    current_app.db.session.commit()   
    resultJson = SysPlanRestrictionSchema().jsonify(result)
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_plan_restriction.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_plan_restriction_service(SysPlanRestriction)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

