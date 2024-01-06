from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ope.ope_centro2_area_service import ope_centro2_area_service

from app.modules.ope.base.ope_serealizer import OpeCentro2AreaSchema
from app.modules.ope.base.ope_model import OpeCentro2Area
from app.generics.generic_resource import generic_resource


routes_ope_centro2_area = Blueprint(
    "opecentro2area", __name__, url_prefix="/api/ope/opecentro2area"
)


# ==============================


@routes_ope_centro2_area.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ope_centro2_area_service,
        model=OpeCentro2Area,
        schema=OpeCentro2AreaSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ope_centro2_area.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ope_centro2_area_service,
        model=OpeCentro2Area,
        schema=OpeCentro2AreaSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ope_centro2_area.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ope_centro2_area_service,
        model=OpeCentro2Area,
        schema=OpeCentro2AreaSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ope_centro2_area.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ope_centro2_area_service,
        model=OpeCentro2Area,
        db_session=current_app.db.session,
    )
