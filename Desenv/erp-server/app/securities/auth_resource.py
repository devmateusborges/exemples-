import datetime
import logging
from datetime import timedelta
from app.env import APP_ERP_URL, PUBLIC_URL
from flask_jwt_extended import current_user
from passlib.hash import pbkdf2_sha256

from flask_jwt_extended import jwt_required
from app.generics.generic_resource import generic_resource
from app.exceptions.ApiException import ApiException
import json
from app.modules.sys.base.sys_model import (
    SysModule,
    SysProgram,
    SysProgramAction,
    SysTranslate,
    SysTranslateLang,
    SysTypeDescription,
    SysUnit,
    SysUser,
    SysUserUnit,
)
from app.modules.sys.base.sys_serealizer import (
    SysModuleSchema,
    SysProgramActionSchema,
    SysProgramSchema,
    SysTranslateLangSchema,
    SysTranslateSchema,
    SysTypeDescriptionSchema,
    SysUnitSchema,
    SysUserSchema,
    SysUserUnitSchema,
)
import uuid
from app.modules.sys.sys_module_service import sys_module_service
from app.modules.sys.sys_program_action_service import sys_program_action_service
from app.modules.sys.sys_program_service import sys_program_service
from app.modules.sys.sys_token_service import sys_token_service
from app.modules.sys.sys_translate_lang_service import sys_translate_lang_service
from app.modules.sys.sys_translate_service import sys_translate_service
from app.modules.sys.sys_type_description_service import sys_type_description_service
from app.modules.sys.sys_user_service import SysUser_service
from app.modules.sys.sys_user_unit_service import sys_user_unit_service
from app.modules.sys.sys_unit_service import sys_unit_service

from app.securities.auth_serializer import LoginSchema
from flask import (
    Blueprint,
    current_app,
    jsonify,
    request,
    url_for,
    make_response,
    redirect,
)
from flask_jwt_extended import create_access_token, create_refresh_token
from app.utils.funcs_util import funcs_util
from app.utils.resource_util import resource_util

routes_auth = Blueprint("auth", __name__, url_prefix="/api/auth")

# ==============================


@routes_auth.route("/login", methods=["POST"])
def login():
    logging.debug("Login")

    userLogin = LoginSchema().load(request.json)
    srv = SysUser_service(model=SysUser, schema=SysUserSchema)

    user = srv.find_all(
        enabled_filter_fields=["login"],
        filters={"filter": {"and": {"login": userLogin.get("login")}}},
    )

    unit = SysUnit.query.filter_by(id=userLogin.get("unit_id"), active="S").first()
    userUnitCount = (
        SysUserUnit.query.filter_by(sys_unit_id=userLogin.get("unit_id"))
        .join(SysUser)
        .filter_by(login=userLogin.get("login"))
        .count()
    )
    if user["total"] != 0:
        user = user["items"][0]

        if user["active"] == "N":
            if user["active_message"] == "INATIVO_POR_REDEF_SENHA":
                raise ApiException(
                    message=user["active_message_obj"]["description"],
                    name="ERROR_LOGIN_VALIDATE",
                    status_code=400,
                )
            else:
                raise ApiException(
                    message="Error invalid user",
                    name="ERROR_LOGIN_VALIDATE",
                    status_code=400,
                )

        if (
            pbkdf2_sha256.verify(request.json["password"], user["password"])
            and unit
            and userUnitCount > 0
        ):
            additional_claims = {"unit_id": userLogin.get("unit_id")}
            acess_token = create_access_token(
                identity=user["id"],
                expires_delta=timedelta(days=1),
                additional_claims=additional_claims,
            )
            refresh_token = create_refresh_token(identity=user["id"])

            userJson = SysUserSchema(exclude=["password"]).dump(user)
            unitJson = SysUnitSchema().dump(unit)
            return (
                jsonify(
                    {
                        "user": userJson,
                        "unit": unitJson,
                        "access_token": acess_token,
                        "refresh_token": refresh_token,
                    }
                ),
                200,
            )

    raise ApiException(message="Invalid credencial", name="AUTH_ERROR", status_code=401)


@routes_auth.route("/loginsocialgoogle", methods=["POST"])
def loginsocialgoogle():
    logging.debug("Login social google")

    userLogin = LoginSchema().load(request.json)
    unitSrv = sys_unit_service(model=SysUnit, schema=SysUnitSchema)
    userSrv = SysUser_service(model=SysUser, schema=SysUserSchema)

    user = userSrv.find_all(
        enabled_filter_fields=["login"],
        filters={"filter": {"and": {"login": userLogin.get("login")}}},
    )

    unit = unitSrv.find_all(
        enabled_filter_fields=["unit_id"],
        filters={"filter": {"and": {"unit_id": userLogin.get("unit_id")}}},
    )

    if user["total"] != 0:
        user = user["items"][0]

        if user["active"] == "N":

            raise ApiException(
                message="Error invalid user",
                name="ERROR_LOGIN_VALIDATE",
                status_code=400,
            )

        if unit["total"] == 1:
            additional_claims = {"unit_id": userLogin.get("unit_id")}
            acess_token = create_access_token(
                identity=user["id"],
                expires_delta=timedelta(days=1),
                additional_claims=additional_claims,
            )
            refresh_token = create_refresh_token(identity=user["id"])

            unitJson = SysUnitSchema().dump(unit)
            return (
                jsonify(
                    {
                        "user": user,
                        "unit": unitJson,
                        "access_token": acess_token,
                        "refresh_token": refresh_token,
                    }
                ),
                200,
            )

    raise ApiException(message="Invalid credencial", name="AUTH_ERROR", status_code=401)


# ==============================
@routes_auth.route("/register", methods=["POST"])
def register():
    logging.debug("Register new user")
    srv = SysUser_service(SysUser)
    body = request.json

    user = SysUser.query.filter_by(email=body["email"]).one_or_none()
    if user is not None:
        return (
            json.dumps({"success": False, "msg": "EMAIL_AREADY_EXISTS"}),
            200,
            {"ContentType": "application/json"},
        )

    sysTranslateLangObj = SysTranslateLang.query.filter_by(
        code=body["sys_tran_lang_id_default"]
    ).one_or_none()
    body["sys_tran_lang_id_default"] = sysTranslateLangObj.id
    body["active"] = "N"
    body["active_message"] = "NOVO_USUARIO"

    obj = SysUserSchema().load(body)
    result = srv.save(obj)
    srv.sendActivationEmail(obj)
    current_app.db.session.commit()
    return SysUserSchema(exclude=["password"]).jsonify(result), 201


# ==============================
@routes_auth.route("/registersocialgoogle", methods=["POST"])
def registersocialgoogle():
    logging.debug("Register new google user")
    userSrv = SysUser_service(model=SysUser, schema=SysUserSchema)
    translateLangSrv = sys_translate_lang_service(
        model=SysTranslateLang, schema=SysTranslateLangSchema
    )
    body = request.json

    user = userSrv.find_all(
        enabled_filter_fields=["email"],
        filters={"filter": {"and": {"email": body["user"]["email"]}}},
    )

    if user["total"] != 0:
        return (
            json.dumps({"success": False, "msg": "EMAIL_AREADY_EXISTS"}),
            200,
            {"ContentType": "application/json"},
        )

    sysTranslateLangObj = translateLangSrv.find_all(
        enabled_filter_fields=["code"],
        filters={"filter": {"and": {"code": body["sys_tran_lang_id_default"]}}},
    )

    newSysUser = SysUser()
    newSysUser.name = body["user"]["displayName"]
    newSysUser.login = body["user"]["email"]
    newSysUser.email = body["user"]["email"]
    newSysUser.password = ""
    newSysUser.active = "S"
    newSysUser.active_message = None
    newSysUser.phone = None
    newSysUser.document = None
    newSysUser.admin = "N"
    newSysUser.login_ext = "N"
    newSysUser.origem = "2"
    newSysUser.chat = "N"
    newSysUser.image_url = body["user"]["photoURL"]
    newSysUser.email_verified = "S"
    newSysUser.provider = "GOOGLE"
    newSysUser.provider_code = None
    newSysUser.gtm_default = body["gtm_default"]
    newSysUser.sys_tran_lang_id_default = sysTranslateLangObj["items"][0]["id"]

    sysUnitDemo = SysUnit()
    sysUnitDemo.id = str(uuid.uuid4())
    sysUnitDemo.sys_unit_manager_id = "f7be1548-73d3-44c0-9c8e-a499794f36ea"
    sysUnitDemo.name = "demo"
    sysUnitDemo.code_unit = "0001"
    sysUnitDemo.active = "S"

    current_app.db.session.add(newSysUser)
    current_app.db.session.add(sysUnitDemo)
    current_app.db.session.commit()

    sysUserUnit = SysUserUnit()
    sysUserUnit.owner = "S"
    sysUserUnit.sys_unit_id = sysUnitDemo.id
    sysUserUnit.sys_user_id = newSysUser.id

    current_app.db.session.add(sysUserUnit)

    # userSrv.save(obj)

    current_app.db.session.commit()
    return json.dumps({"success": True}), 201, {"ContentType": "application/json"}


@routes_auth.route("/sendredefinepasswordemail", methods=["POST"])
@jwt_required()
def sendredefinepasswordemail():
    body = request.json

    srv = SysUser_service(model=SysUser, schema=SysUserSchema)
    user = srv.find_all(
        enabled_filter_fields=["login", "provider"],
        filters={
            "filter": {
                "and": {"login": current_user[0].login, "and": {"provider": "LOCAL"}}
            }
        },
    )

    if user["total"] == 0:
        raise ApiException(
            message="Error invalid user",
            name="ERROR_REDEFINE_PASSWORD_VALIDATE",
            status_code=400,
        )

    verifyPasswd = pbkdf2_sha256.verify(body["password"], user["items"][0]["password"])

    if verifyPasswd is False:
        raise ApiException(
            message="Error invalid user",
            name="ERROR_REDEFINE_PASSWORD_VALIDATE",
            status_code=400,
        )

    srv.sendRedefinePasswordEmail(user["items"][0], body)
    current_app.db.session.commit()
    return json.dumps({"success": True}), 200, {"ContentType": "application/json"}


@routes_auth.route("/sendresetpasswordemail", methods=["POST"])
def sendresetpasswordemail():
    body = request.json
    user = SysUser.query.filter_by(email=body["email"], active="S").one_or_none()
    srv = SysUser_service(SysUser)

    if user is None:
        raise ApiException(
            message="Error invalid user",
            name="ERROR_RESET_PASSWORD_VALIDATE",
            status_code=400,
        )

    srv.sendResetPasswordEmail(user)
    current_app.db.session.commit()
    return json.dumps({"success": True}), 200, {"ContentType": "application/json"}


@routes_auth.route("/passwordresetvalidate", methods=["GET"])
def passwordresetvalidate():
    req_param_token = request.args.get("token", default="", type=str)
    srvToken = sys_token_service()
    srv = SysUser_service(model=SysUser, schema=SysUserSchema)

    token = srvToken.get_token(session=current_app.db.session, token=req_param_token)

    if token is None:
        raise ApiException(
            message="Error invalid token",
            name="ERROR_PASSWORD_VALIDATE",
            status_code=400,
        )

    login = token.data_token["login"]
    user = srv.find_all(
        enabled_filter_fields=["login"],
        filters={"filter": {"and": {"login": login}}},
    )

    if user is None:
        raise ApiException(
            message="Error invalid user",
            name="ERROR_PASSWORD_VALIDATE",
            status_code=400,
        )

    srv.resetPassword(user["items"][0])

    current_app.db.session.commit()

    return make_response(redirect(APP_ERP_URL + "/#/signin?passwordreseted=true"))


@routes_auth.route("/passwordredefinevalidate", methods=["GET"])
def passwordredefinevalidate():
    req_param_token = request.args.get("token", default="", type=str)
    srvToken = sys_token_service()
    srv = SysUser_service(model=SysUser, schema=SysUserSchema)

    # TODO fazer metodo no service tokem para validar usuario
    token = srvToken.get_token(session=current_app.db.session, token=req_param_token)

    if token is None:
        raise ApiException(
            message="Error invalid token",
            name="ERROR_PASSWORD_VALIDATE",
            status_code=400,
        )

    login = token.data_token["login"]
    user = srv.find_all(
        enabled_filter_fields=["login"],
        filters={"filter": {"and": {"login": login}}},
    )

    if user is None:
        raise ApiException(
            message="Error invalid user",
            name="ERROR_PASSWORD_VALIDATE",
            status_code=400,
        )

    body = json.loads(token.data_token["body"])
    verifyPassword = pbkdf2_sha256.verify(
        body["password"], user["items"][0]["password"]
    )

    if verifyPassword is False:
        raise ApiException(
            message="Error invalid credentials",
            name="ERROR_PASSWORD_VALIDATE",
            status_code=400,
        )

    srv.redefinePassword(user["items"][0], body)

    current_app.db.session.commit()

    return make_response(
        redirect(APP_ERP_URL + "/#/private/sys/redefinepassword?passwordredefined=true")
    )


@routes_auth.route("/deactivateuser", methods=["GET"])
def deactivateuser():
    req_param_token = request.args.get("token", default="", type=str)
    srvToken = sys_token_service()
    srv = SysUser_service(model=SysUser, schema=SysUserSchema)

    token = srvToken.get_token(session=current_app.db.session, token=req_param_token)

    if token is None:
        raise ApiException(
            message="Error invalid token",
            name="ERROR_PASSWORD_VALIDATE",
            status_code=400,
        )

    login = token.data_token["login"]
    user = srv.find_all(
        enabled_filter_fields=["login"],
        filters={"filter": {"and": {"login": login}}},
    )

    srv.deactivateuser(user["items"][0])
    current_app.db.session.commit()

    return make_response(redirect(APP_ERP_URL + "/#/signin?userdeactivated=true"))


# ==============================
@routes_auth.route("/registervalidate", methods=["GET"])
def registervalidate():
    req_param_token = request.args.get("token", default="", type=str)
    srv = sys_token_service()
    token = srv.get_token(session=current_app.db.session, token=req_param_token)

    if token is None:
        raise ApiException(
            message="Error invalid token",
            name="ERROR_REGISTER_VALIDATE",
            status_code=400,
        )

    login = token.data_token["login"]
    user = SysUser.query.filter_by(login=login, active="N").first()
    if user is None:
        raise ApiException(
            message="Error invalid user",
            name="ERROR_REGISTER_VALIDATE",
            status_code=400,
        )

    user.email_verified = "S"
    user.active = "S"
    user.active_message = "Not message"

    sysUnitDemo = SysUnit()
    sysUnitDemo.id = str(uuid.uuid4())
    sysUnitDemo.sys_unit_manager_id = "f7be1548-73d3-44c0-9c8e-a499794f36ea"
    sysUnitDemo.name = "demo"
    sysUnitDemo.code_unit = "0001"
    sysUnitDemo.active = "S"

    current_app.db.session.merge(sysUnitDemo)
    current_app.db.session.commit()

    sysUserUnit = SysUserUnit()
    sysUserUnit.owner = "S"
    sysUserUnit.sys_unit_id = sysUnitDemo.id
    sysUserUnit.sys_user_id = user.id

    current_app.db.session.merge(user)
    current_app.db.session.merge(sysUserUnit)
    current_app.db.session.commit()
    current_app.db.session.close()
    return make_response(redirect(APP_ERP_URL + "/signin"))


# ==============================
@routes_auth.route("/logingoogle", methods=["GET"])
def logingoogle():
    redirect_uri = url_for("auth.callbackgoogle", _external=True)
    redirect_uri = redirect_uri.replace("/api/", PUBLIC_URL + "/api/")

    # return current_app.auth_client_google.authorize_redirect(redirect_uri)

    auth_location = current_app.auth_client_google.authorize_redirect(
        redirect_uri
    ).location

    return make_response(redirect(auth_location, 302))

    # return (
    #    jsonify(
    #        {
    #            "datetime": datetime.datetime.now().strftime("%d/%m/%YT%H:%M:%S.%f"),
    #            "code": "200",
    #            "name": "LOGIN_SOCIAL",
    #            "msg": "Login social successlly",
    #            "data": {"url_auth": auth_location},
    #        }
    #    ),
    #    200,
    # )


# ==============================
@routes_auth.route("/callbackgoogle")
def callbackgoogle():
    req = request
    token = current_app.auth_client_google.authorize_access_token()
    user = token.get("userinfo")
    return jsonify(user), 200


# ==============================
@routes_auth.route("/getunitbyuserlogin/", methods=["GET"])
def get_by_user_login():
    req_param = resource_util.req_param_default()
    srv = sys_user_unit_service(model=SysUserUnit, schema=SysUserUnitSchema)
    result = srv.get_by_user_login(
        session=current_app.db.session,
        page=req_param["ppage"],
        per_page=req_param["pper_page"],
        pfilters=req_param["pfilters"],
    )

    response = funcs_util.getResponseJsonList(result)
    current_app.db.session.close()
    return response


# ==============================
@routes_auth.route("/getprogrambyuserlogin/", methods=["GET"])
@jwt_required()
def get_program_by_user_login():
    req_param = resource_util.req_param_default()
    srv = sys_program_service(model=SysProgram, schema=SysProgramSchema)
    result = srv.get_by_user_login(
        session=current_app.db.session, pfilters=req_param["pfilters"]
    )

    response = funcs_util.getResponseJsonList(result)

    current_app.db.session.close()
    return response


# ==============================
@routes_auth.route("/getprogramactionbyuserlogin/", methods=["GET"])
@jwt_required()
def get_program_action_by_user_login():
    req_param = resource_util.req_param_default()

    srv = sys_program_action_service(
        model=SysProgramAction, schema=SysProgramActionSchema
    )
    result = srv.get_by_user_login(
        session=current_app.db.session, pfilters=req_param["pfilters"]
    )

    response = funcs_util.getResponseJsonList(result)

    current_app.db.session.close()
    return response


# ==============================
@routes_auth.route("/getmodulebyuserlogin/", methods=["GET"])
@jwt_required()
def get_module_by_user_login():
    req_param = resource_util.req_param_default()
    srv = sys_module_service(model=SysModule, schema=SysModuleSchema)
    result = srv.get_by_user_login(
        session=current_app.db.session, pfilters=req_param["pfilters"]
    )

    response = funcs_util.getResponseJsonList(result)

    current_app.db.session.close()
    return response


@routes_auth.route("/i18ngmt", methods=["get"])
def i18n_gmt():
    sysTypeDescriptionService = sys_type_description_service(
        model=SysTypeDescription, schema=SysTypeDescriptionSchema
    )
    i18nGmt = sysTypeDescriptionService.find_all(
        filters={"filter": {"and": {"table_name": "i18n_gmt"}}},
        enabled_filter_fields=["table_name"],
    )
    return i18nGmt


@routes_auth.route("/i18ntranslate/<systranalateid>", methods=["GET"])
def find_i18n_translate(systranalateid):

    sysTranslateService = sys_translate_service(
        model=SysTranslate, schema=SysTranslateSchema
    )
    translate = sysTranslateService.find_all(
        page=1,
        per_page=999999,
        filters={"filter": {"and": {"sys_translate_lang_id": systranalateid}}},
        enabled_filter_fields=["sys_translate_lang_id"],
    )
    ret_trans = {}
    for t in translate["items"]:
        key = t["term_orig"]
        if t["term_group"] is not None:
            key += t["term_group"]

        ret_trans[key] = t["term_translate"]

    return ret_trans


@routes_auth.route("/i18nlang", methods=["get"])
def i18n_lang():
    sysTypeDescriptionService = sys_translate_lang_service(
        model=SysTranslateLang, schema=SysTranslateLangSchema
    )
    i18nLang = sysTypeDescriptionService.find_all(
        page=1,
        per_page=999999,
        filters={"filter": {"and": {"code": {"not_equal_to": "TST1"}}}},
        enabled_filter_fields=["code"],
    )
    return i18nLang
