from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_translate_service import sys_translate_service

from app.modules.sys.base.sys_serealizer import SysTranslateSchema
from app.modules.sys.base.sys_model import SysTranslate
from app.generics.generic_resource import generic_resource
from app.utils.funcs_util import funcs_util


routes_sys_translate = Blueprint(
    "systranslate", __name__, url_prefix="/api/sys/systranslate"
)


# ==============================


@routes_sys_translate.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_translate_service,
        model=SysTranslate,
        schema=SysTranslateSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_translate.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_translate_service,
        model=SysTranslate,
        schema=SysTranslateSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_translate.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_translate_service,
        model=SysTranslate,
        schema=SysTranslateSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_translate.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_translate_service,
        model=SysTranslate,
        db_session=current_app.db.session,
    )
