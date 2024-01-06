from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_document_user_service import sys_document_user_service

from app.modules.sys.base.sys_serealizer import SysDocumentUserSchema
from app.modules.sys.base.sys_model import SysDocumentUser


routes_sys_document_user = Blueprint('sysdocumentuser', __name__,url_prefix="/api/sysdocumentuser")



#==============================
@routes_sys_document_user.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_document_user_service(SysDocumentUser)
    result = srv.find_all()
    resultJson = SysDocumentUserSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_document_user.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_document_user_service(SysDocumentUser)
    result = srv.find_by_id(id)
    resultJson = SysDocumentUserSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_document_user.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_document_user_service(SysDocumentUser)    
    
    try:
        obj = SysDocumentUserSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)     
    current_app.db.session.commit()
    resultJson = SysDocumentUserSchema().jsonify(result)
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_document_user.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_document_user_service(SysDocumentUser)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204