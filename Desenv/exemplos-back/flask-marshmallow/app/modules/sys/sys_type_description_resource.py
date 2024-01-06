from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_type_description_service import sys_type_description_service

from app.modules.sys.base.sys_serealizer import SysTypeDescriptionSchema
from app.modules.sys.base.sys_model import SysTypeDescription


routes_sys_type_description = Blueprint('systypedescription', __name__,url_prefix="/api/systypedescription")



#==============================
@routes_sys_type_description.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_type_description_service(SysTypeDescription)
    result = srv.find_all()
    resultJson = SysTypeDescriptionSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_type_description.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_type_description_service(SysTypeDescription)
    result = srv.find_by_id(id)
    resultJson = SysTypeDescriptionSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_type_description.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_type_description_service(SysTypeDescription)    
    
    try:
        obj = SysTypeDescriptionSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)   
    current_app.db.session.commit()  
    resultJson = SysTypeDescriptionSchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_type_description.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_type_description_service(SysTypeDescription)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

 