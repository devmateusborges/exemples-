from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_param_service import sys_param_service

from app.modules.sys.base.sys_serealizer import SysParamSchema
from app.modules.sys.base.sys_model import SysParam
from app.generics.generic_resource import generic_resource


routes_sys_param = Blueprint("sysparam", __name__, url_prefix="/api/sys/sysparam")


# ==============================


@routes_sys_param.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_param_service,
        model=SysParam,
        schema=SysParamSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_param.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_param_service,
        model=SysParam,
        schema=SysParamSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_param.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_param_service,
        model=SysParam,
        schema=SysParamSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_param.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_param_service,
        model=SysParam,
        db_session=current_app.db.session,
    )
