import logging
from datetime import timedelta


from app.exceptions.ApiException import ApiException
from app.modules.sys.base.sys_model import SysUser
from app.modules.sys.base.sys_serealizer import LoginSchema, SysUserSchema
from app.modules.sys.sys_user_service import SysUser_service
from flask import Blueprint, current_app, jsonify, request, session
from flask_jwt_extended import create_access_token, create_refresh_token
from marshmallow import ValidationError

routes_auth = Blueprint('auth', __name__,url_prefix="/api/auth")


@routes_auth.route('/login', methods=['POST'])
def login():
    logging.debug("Login")   
    try:
        userLogin = LoginSchema().load(request.json)
    except ValidationError as err:
        return jsonify( err.messages), 401
    
    user = SysUser.query.filter_by(login=userLogin.get('login')).first()

    if user and user.verify_password(request.json['password']):
        additional_claims= {"unit_id": userLogin.get('unit_id')}
        acess_token = create_access_token(
            identity=user.id,
            expires_delta=timedelta(days=1),
            additional_claims=additional_claims
        )
        refresh_token = create_refresh_token(identity=user.id)

        return jsonify({
            'acess_token': acess_token,
            'refresh_token': refresh_token,
        }), 200

    raise ApiException("Invalid credencial", status_code=401)
   
    
    
@routes_auth.route('/register', methods=['POST'])
def register():
    logging.debug("Registr new user")    
    
    srv = SysUser_service(SysUser)  
    try:
        obj = SysUserSchema().load(request.json)
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj) 

    return SysUserSchema( exclude=['password']).dump(result), 201
    
