from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.sys.sys_program_favorite_service import sys_program_favorite_service

from app.modules.sys.base.sys_serealizer import SysProgramFavoriteSchema
from app.modules.sys.base.sys_model import SysProgramFavorite


routes_sys_program_favorite = Blueprint('sysprogramfavorite', __name__,url_prefix="/api/sysprogramfavorite")

 

#============================== 
@routes_sys_program_favorite.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = sys_program_favorite_service(SysProgramFavorite)
    result = srv.find_all()
    resultJson = SysProgramFavoriteSchema(many=True).jsonify(result)
    current_app.db.session.close()
    return  resultJson, 200

#==============================
@routes_sys_program_favorite.route('/<id>', methods=['GET'])
@jwt_required()
def find_by_id(id):
    srv = sys_program_favorite_service(SysProgramFavorite)
    result = srv.find_by_id(id)
    resultJson = SysProgramFavoriteSchema().jsonify(result)
    current_app.db.session.close()    
    return resultJson, 200

#==============================
@routes_sys_program_favorite.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = sys_program_favorite_service(SysProgramFavorite)    
    
    try:
        obj = SysProgramFavoriteSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)   
    current_app.db.session.commit()  
    resultJson = SysProgramFavoriteSchema().jsonify(result)
    
    current_app.db.session.close()
    return resultJson, 201

#==============================
@routes_sys_program_favorite.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = sys_program_favorite_service(SysProgramFavorite)
    result = srv.delete(id)
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 204

 