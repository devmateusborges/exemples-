from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_module_service import sys_module_service

from app.modules.sys.base.sys_serealizer import SysModuleSchema
from app.modules.sys.base.sys_model import SysModule
from app.generics.generic_resource import generic_resource


routes_sys_module = Blueprint("sysmodule", __name__, url_prefix="/api/sys/sysmodule")


# ==============================


@routes_sys_module.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_module_service,
        model=SysModule,
        schema=SysModuleSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_module.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id,
        service=sys_module_service,
        model=SysModule,
        schema=SysModuleSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_module.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_module_service,
        model=SysModule,
        schema=SysModuleSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_module.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_module_service,
        model=SysModule,
        db_session=current_app.db.session,
    )
