from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_plan_service import sys_plan_service

from app.modules.sys.base.sys_serealizer import SysPlanSchema
from app.modules.sys.base.sys_model import SysPlan


routes_sys_plan = Blueprint('sysplan', __name__,url_prefix="/api/sysplan")



#==============================
@routes_sys_plan.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_plan_service(SysPlan)
    result = srv.find_all()
    resultJson = SysPlanSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_plan.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_plan_service(SysPlan)
    result = srv.find_by_id(id)
    resultJson = SysPlanSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_plan.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_plan_service(SysPlan)    
    
    try:
        obj = SysPlanSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)   
    current_app.db.session.commit()  
    resultJson = SysPlanSchema().jsonify(result)
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_plan.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_plan_service(SysPlan)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

