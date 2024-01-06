from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_group_program_service import sys_group_program_service

from app.modules.sys.base.sys_serealizer import SysGroupProgramSchema
from app.modules.sys.base.sys_model import SysGroupProgram


routes_sys_group_program = Blueprint('sysgroupprogram', __name__,url_prefix="/api/sysgroupprogram")



#==============================
@routes_sys_group_program.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_group_program_service(SysGroupProgram)
    result = srv.find_all()
    resultJson = SysGroupProgramSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_group_program.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_group_program_service(SysGroupProgram)
    result = srv.find_by_id(id)
    resultJson = SysGroupProgramSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_group_program.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_group_program_service(SysGroupProgram)    
    
    try:
        obj = SysGroupProgramSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj) 
    current_app.db.session.commit()    
    resultJson = SysGroupProgramSchema().jsonify(result)
    current_app.db.session.commit()
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_group_program.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_group_program_service(SysGroupProgram)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204
