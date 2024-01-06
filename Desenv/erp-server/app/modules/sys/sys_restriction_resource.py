from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_restriction_service import sys_restriction_service

from app.modules.sys.base.sys_serealizer import SysRestrictionSchema
from app.modules.sys.base.sys_model import SysRestriction
from app.generics.generic_resource import generic_resource


routes_sys_restriction = Blueprint(
    "sysrestriction", __name__, url_prefix="/api/sys/sysrestriction"
)


# ==============================


@routes_sys_restriction.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_restriction_service,
        model=SysRestriction,
        schema=SysRestrictionSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_restriction.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_restriction_service,
        model=SysRestriction,
        schema=SysRestrictionSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_restriction.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_restriction_service,
        model=SysRestriction,
        schema=SysRestrictionSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_restriction.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_restriction_service,
        model=SysRestriction,
        db_session=current_app.db.session,
    )
