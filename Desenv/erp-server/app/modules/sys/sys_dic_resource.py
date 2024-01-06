from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_dic_service import sys_dic_service

from app.modules.sys.base.sys_serealizer import SysDicSchema
from app.modules.sys.base.sys_model import SysDic
from app.generics.generic_resource import generic_resource


routes_sys_dic = Blueprint("sysdic", __name__, url_prefix="/api/sys/sysdic")


# ==============================


@routes_sys_dic.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_dic_service,
        model=SysDic,
        schema=SysDicSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_dic.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_dic_service,
        model=SysDic,
        schema=SysDicSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_dic.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_dic_service,
        model=SysDic,
        schema=SysDicSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_dic.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id, service=sys_dic_service, model=SysDic, db_session=current_app.db.session
    )
