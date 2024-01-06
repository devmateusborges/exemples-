from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_user_chat_grupo_service import sys_user_chat_grupo_service

from app.modules.sys.base.sys_serealizer import SysUserChatGrupoSchema
from app.modules.sys.base.sys_model import SysUserChatGrupo
from app.generics.generic_resource import generic_resource


routes_sys_user_chat_grupo = Blueprint(
    "sysuserchatgrupo", __name__, url_prefix="/api/sys/sysuserchatgrupo"
)


# ==============================


@routes_sys_user_chat_grupo.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_user_chat_grupo_service,
        model=SysUserChatGrupo,
        schema=SysUserChatGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_user_chat_grupo.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_user_chat_grupo_service,
        model=SysUserChatGrupo,
        schema=SysUserChatGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_user_chat_grupo.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_user_chat_grupo_service,
        model=SysUserChatGrupo,
        schema=SysUserChatGrupoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_user_chat_grupo.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_user_chat_grupo_service,
        model=SysUserChatGrupo,
        db_session=current_app.db.session,
    )
