from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_unit_param_service import sys_unit_param_service

from app.modules.sys.base.sys_serealizer import SysUnitParamSchema
from app.modules.sys.base.sys_model import SysUnitParam
from app.generics.generic_resource import generic_resource


routes_sys_unit_param = Blueprint(
    "sysunitparam", __name__, url_prefix="/api/sys/sysunitparam"
)


# ==============================


@routes_sys_unit_param.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_unit_param_service,
        model=SysUnitParam,
        schema=SysUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_unit_param.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_unit_param_service,
        model=SysUnitParam,
        schema=SysUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_unit_param.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_unit_param_service,
        model=SysUnitParam,
        schema=SysUnitParamSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_unit_param.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_unit_param_service,
        model=SysUnitParam,
        db_session=current_app.db.session,
    )
