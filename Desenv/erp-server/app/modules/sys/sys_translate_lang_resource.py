from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_translate_lang_service import sys_translate_lang_service

from app.modules.sys.base.sys_serealizer import SysTranslateLangSchema
from app.modules.sys.base.sys_model import SysTranslateLang
from app.generics.generic_resource import generic_resource


routes_sys_translate_lang = Blueprint(
    "systranslatelang", __name__, url_prefix="/api/sys/systranslatelang"
)


# ==============================


@routes_sys_translate_lang.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_translate_lang_service,
        model=SysTranslateLang,
        schema=SysTranslateLangSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_translate_lang.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_translate_lang_service,
        model=SysTranslateLang,
        schema=SysTranslateLangSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_translate_lang.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_translate_lang_service,
        model=SysTranslateLang,
        schema=SysTranslateLangSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_translate_lang.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_translate_lang_service,
        model=SysTranslateLang,
        db_session=current_app.db.session,
    )
