from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_document_category_service import sys_document_category_service

from app.modules.sys.base.sys_serealizer import SysDocumentCategorySchema
from app.modules.sys.base.sys_model import SysDocumentCategory


routes_sys_document_category = Blueprint('sysdocumentcategory', __name__,url_prefix="/api/sysdocumentcategory")



#==============================
@routes_sys_document_category.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_document_category_service(SysDocumentCategory)
    result = srv.find_all()
    resultJson = SysDocumentCategorySchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_document_category.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_document_category_service(SysDocumentCategory)

    result = srv.find_by_id(id)
    resultJson = SysDocumentCategorySchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_document_category.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_document_category_service(SysDocumentCategory)    
    
    try:
        obj = SysDocumentCategorySchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)   
    current_app.db.session.commit()  
    resultJson = SysDocumentCategorySchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_document_category.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_document_category_service(SysDocumentCategory)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

 