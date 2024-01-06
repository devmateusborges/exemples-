from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fis.fis_tributo_service import fis_tributo_service

from app.modules.fis.base.fis_serealizer import FisTributoSchema
from app.modules.fis.base.fis_model import FisTributo
from app.generics.generic_resource import generic_resource


routes_fis_tributo = Blueprint("fistributo", __name__, url_prefix="/api/fis/fistributo")


# ==============================


@routes_fis_tributo.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fis_tributo_service,
        model=FisTributo,
        schema=FisTributoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fis_tributo.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fis_tributo_service,
        model=FisTributo,
        schema=FisTributoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fis_tributo.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fis_tributo_service,
        model=FisTributo,
        schema=FisTributoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fis_tributo.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fis_tributo_service,
        model=FisTributo,
        db_session=current_app.db.session,
    )
