from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required
from app.modules.ope.ope_centro2_mapa_geometria_service import (
    ope_centro2_mapa_geometria_service,
)

from app.modules.ope.base.ope_serealizer import OpeCentro2MapaGeometriaSchema
from app.modules.ope.base.ope_model import OpeCentro2MapaGeometria
from app.generics.generic_resource import generic_resource


routes_ope_centro2_mapa_geometria = Blueprint(
    "opecentro2mapageometria", __name__, url_prefix="/api/ope/opecentro2mapageometria"
)


# ==============================


@routes_ope_centro2_mapa_geometria.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ope_centro2_mapa_geometria_service,
        model=OpeCentro2MapaGeometria,
        schema=OpeCentro2MapaGeometriaSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ope_centro2_mapa_geometria.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ope_centro2_mapa_geometria_service,
        model=OpeCentro2MapaGeometria,
        schema=OpeCentro2MapaGeometriaSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ope_centro2_mapa_geometria.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ope_centro2_mapa_geometria_service,
        model=OpeCentro2MapaGeometria,
        schema=OpeCentro2MapaGeometriaSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ope_centro2_mapa_geometria.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ope_centro2_mapa_geometria_service,
        model=OpeCentro2MapaGeometria,
        db_session=current_app.db.session,
    )
