from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_group_program_action_service import (
    sys_group_program_action_service,
)

from app.modules.sys.base.sys_serealizer import SysGroupProgramActionSchema
from app.modules.sys.base.sys_model import SysGroupProgramAction
from app.generics.generic_resource import generic_resource


routes_sys_group_program_action = Blueprint(
    "sysgroupprogramaction", __name__, url_prefix="/api/sys/sysgroupprogramaction"
)


# ==============================


@routes_sys_group_program_action.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_group_program_action_service,
        model=SysGroupProgramAction,
        schema=SysGroupProgramActionSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_group_program_action.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_group_program_action_service,
        model=SysGroupProgramAction,
        schema=SysGroupProgramActionSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_group_program_action.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_group_program_action_service,
        model=SysGroupProgramAction,
        schema=SysGroupProgramActionSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_group_program_action.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_group_program_action_service,
        model=SysGroupProgramAction,
        db_session=current_app.db.session,
    )
