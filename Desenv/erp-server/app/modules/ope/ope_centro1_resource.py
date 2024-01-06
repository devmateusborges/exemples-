from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required
from app.modules.ope.ope_centro1_service import ope_centro1_service

from app.modules.ope.base.ope_serealizer import OpeCentro1Schema
from app.modules.ope.base.ope_model import OpeCentro1
from app.generics.generic_resource import generic_resource


routes_ope_centro1 = Blueprint("opecentro1", __name__, url_prefix="/api/ope/opecentro1")


# ==============================


@routes_ope_centro1.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ope_centro1_service,
        model=OpeCentro1,
        schema=OpeCentro1Schema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ope_centro1.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ope_centro1_service,
        model=OpeCentro1,
        schema=OpeCentro1Schema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ope_centro1.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ope_centro1_service,
        model=OpeCentro1,
        schema=OpeCentro1Schema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ope_centro1.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ope_centro1_service,
        model=OpeCentro1,
        db_session=current_app.db.session,
    )
