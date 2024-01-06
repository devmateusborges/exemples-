from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_notification_token_service import (
    sys_notification_token_service,
)

from app.modules.sys.base.sys_serealizer import SysNotificationTokenSchema
from app.modules.sys.base.sys_model import SysNotificationToken
from app.generics.generic_resource import generic_resource


routes_sys_notification_token = Blueprint(
    "sysnotificationtoken", __name__, url_prefix="/api/sys/sysnotificationtoken"
)


# ==============================


@routes_sys_notification_token.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_notification_token_service,
        model=SysNotificationToken,
        schema=SysNotificationTokenSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_notification_token.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_notification_token_service,
        model=SysNotificationToken,
        schema=SysNotificationTokenSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_notification_token.route("/", methods=["POST"])
##Criar um usuario custom com senha dinamica, token basic ok
##@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_notification_token_service,
        model=SysNotificationToken,
        schema=SysNotificationTokenSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_notification_token.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_notification_token_service,
        model=SysNotificationToken,
        db_session=current_app.db.session,
    )
