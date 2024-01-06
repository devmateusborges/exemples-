from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_program_service import sys_program_service

from app.modules.sys.base.sys_serealizer import SysProgramSchema
from app.modules.sys.base.sys_model import SysProgram
from app.generics.generic_resource import generic_resource


routes_sys_program = Blueprint("sysprogram", __name__, url_prefix="/api/sys/sysprogram")


# ==============================


@routes_sys_program.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_program_service,
        model=SysProgram,
        schema=SysProgramSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_program.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_program_service,
        model=SysProgram,
        schema=SysProgramSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_program.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_program_service,
        model=SysProgram,
        schema=SysProgramSchema,
        db_session=current_app.db.session,
        unique_fields=["controller"],
    )


# ==============================


@routes_sys_program.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_program_service,
        model=SysProgram,
        db_session=current_app.db.session,
    )
