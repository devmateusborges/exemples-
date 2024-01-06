from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ind.ind_grupo_service import ind_grupo_service

from app.modules.ind.base.ind_serealizer import IndGrupoSchema
from app.modules.ind.base.ind_model import IndGrupo
from app.generics.generic_resource import generic_resource


routes_ind_grupo = Blueprint("indgrupo", __name__, url_prefix="/api/ind/indgrupo")


# ==============================


@routes_ind_grupo.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ind_grupo_service,
        model=IndGrupo,
        schema=IndGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ind_grupo.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ind_grupo_service,
        model=IndGrupo,
        schema=IndGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ind_grupo.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ind_grupo_service,
        model=IndGrupo,
        schema=IndGrupoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ind_grupo.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ind_grupo_service,
        model=IndGrupo,
        db_session=current_app.db.session,
    )
