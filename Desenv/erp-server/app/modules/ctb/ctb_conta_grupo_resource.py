from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ctb.ctb_conta_grupo_service import ctb_conta_grupo_service

from app.modules.ctb.base.ctb_serealizer import CtbContaGrupoSchema
from app.modules.ctb.base.ctb_model import CtbContaGrupo
from app.generics.generic_resource import generic_resource


routes_ctb_conta_grupo = Blueprint(
    "ctbcontagrupo", __name__, url_prefix="/api/ctb/ctbcontagrupo"
)


# ==============================


@routes_ctb_conta_grupo.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ctb_conta_grupo_service,
        model=CtbContaGrupo,
        schema=CtbContaGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ctb_conta_grupo.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ctb_conta_grupo_service,
        model=CtbContaGrupo,
        schema=CtbContaGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ctb_conta_grupo.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ctb_conta_grupo_service,
        model=CtbContaGrupo,
        schema=CtbContaGrupoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ctb_conta_grupo.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ctb_conta_grupo_service,
        model=CtbContaGrupo,
        db_session=current_app.db.session,
    )
