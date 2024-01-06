from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_action_service import sys_action_service

from app.modules.sys.base.sys_serealizer import SysActionSchema
from app.modules.sys.base.sys_model import SysAction
from app.generics.generic_resource import generic_resource


routes_sys_action = Blueprint("sysaction", __name__, url_prefix="/api/sys/sysaction")


# ==============================


@routes_sys_action.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_action_service,
        model=SysAction,
        schema=SysActionSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_action.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_action_service,
        model=SysAction,
        schema=SysActionSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_action.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_action_service,
        model=SysAction,
        schema=SysActionSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_action.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_action_service,
        model=SysAction,
        db_session=current_app.db.session,
    )
