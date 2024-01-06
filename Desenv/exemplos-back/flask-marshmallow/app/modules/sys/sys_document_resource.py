from base64 import decode, encode
import base64
import os
from pickletools import uint8
from flask import Blueprint, current_app, request, jsonify, send_from_directory
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from sqlalchemy import update
from app.exceptions.ApiException import ApiException
from app.modules.sys.sys_document_service import sys_document_service

from app.modules.sys.base.sys_serealizer import SysDocumentSchema
from app.modules.sys.base.sys_model import SysDocument


routes_sys_document = Blueprint('sysdocument', __name__,url_prefix="/api/sysdocument")


#==============================
@routes_sys_document.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_document_service(SysDocument)
    result = srv.find_all()
    resultJson = SysDocumentSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_document.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_document_service(SysDocument)
    result = srv.find_by_id(id)
    resultJson = SysDocumentSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_document.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_document_service(SysDocument)    
    
    try:
        obj = SysDocumentSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.active(obj)
    
    current_app.db.session.commit()     
    resultJson = SysDocumentSchema().jsonify(result)
    current_app.db.session.close()
    return resultJson, 201
 
#==============================
@routes_sys_document.route('/<id>', methods=['DELETE'])
@jwt_required() 
def delete(id):
    srv = sys_document_service(SysDocument)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204
#==============================

@routes_sys_document.route("/upload/<id>", methods=["POST"])
@jwt_required() 
def post_file(id):
    srv = sys_document_service(SysDocument)

    data = request.get_json()

    if data.get('filename') is None:
        raise ApiException('File name required')

    if data.get('file_64') is None:
        raise ApiException('File 64 required')
    
    if data.get('file_content_type') is None:
        raise ApiException('File ContentType required')

    #todo storage_type
    result = srv.uploadfile(id,data.get('file_64'),data.get('filename'),data.get('file_content_type'),1)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 201

#==============================
@routes_sys_document.route('/download/<id>', methods=["GET"])
#@jwt_required() TODO analisar autenticação
def get_file(id):
    
     srv = sys_document_service(SysDocument) 

     return  srv.download(id,1)
     

#==============================
@routes_sys_document.route('/downloadopen/<path:filename>', methods=["GET"])
def get_file_open(filename):
     srv = sys_document_service(SysDocument)
     
     return srv.download_open(filename)
     