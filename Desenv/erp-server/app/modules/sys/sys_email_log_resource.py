from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_email_log_service import sys_email_log_service

from app.modules.sys.base.sys_serealizer import SysEmailLogSchema
from app.modules.sys.base.sys_model import SysEmailLog
from app.generics.generic_resource import generic_resource


routes_sys_email_log = Blueprint(
    "sysemaillog", __name__, url_prefix="/api/sys/sysemaillog"
)


# ==============================


@routes_sys_email_log.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_email_log_service,
        model=SysEmailLog,
        schema=SysEmailLogSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_email_log.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_email_log_service,
        model=SysEmailLog,
        schema=SysEmailLogSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_email_log.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_email_log_service,
        model=SysEmailLog,
        schema=SysEmailLogSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_email_log.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_email_log_service,
        model=SysEmailLog,
        db_session=current_app.db.session,
    )
