from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ctb.ctb_centro_service import ctb_centro_service

from app.modules.ctb.base.ctb_serealizer import CtbCentroSchema
from app.modules.ctb.base.ctb_model import CtbCentro
from app.generics.generic_resource import generic_resource


routes_ctb_centro = Blueprint("ctbcentro", __name__, url_prefix="/api/ctb/ctbcentro")


# ==============================


@routes_ctb_centro.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ctb_centro_service,
        model=CtbCentro,
        schema=CtbCentroSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ctb_centro.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ctb_centro_service,
        model=CtbCentro,
        schema=CtbCentroSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ctb_centro.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ctb_centro_service,
        model=CtbCentro,
        schema=CtbCentroSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ctb_centro.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ctb_centro_service,
        model=CtbCentro,
        db_session=current_app.db.session,
    )
