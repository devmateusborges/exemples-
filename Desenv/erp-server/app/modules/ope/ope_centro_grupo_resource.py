from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ope.ope_centro_grupo_service import ope_centro_grupo_service

from app.modules.ope.base.ope_serealizer import OpeCentroGrupoSchema
from app.modules.ope.base.ope_model import OpeCentroGrupo
from app.generics.generic_resource import generic_resource


routes_ope_centro_grupo = Blueprint(
    "opecentrogrupo", __name__, url_prefix="/api/ope/opecentrogrupo"
)


# ==============================


@routes_ope_centro_grupo.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ope_centro_grupo_service,
        model=OpeCentroGrupo,
        schema=OpeCentroGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ope_centro_grupo.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ope_centro_grupo_service,
        model=OpeCentroGrupo,
        schema=OpeCentroGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ope_centro_grupo.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ope_centro_grupo_service,
        model=OpeCentroGrupo,
        schema=OpeCentroGrupoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ope_centro_grupo.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ope_centro_grupo_service,
        model=OpeCentroGrupo,
        db_session=current_app.db.session,
    )
