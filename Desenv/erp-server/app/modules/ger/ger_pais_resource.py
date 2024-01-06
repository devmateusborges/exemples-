from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ger.ger_pais_service import ger_pais_service

from app.modules.ger.base.ger_serealizer import GerPaisSchema
from app.modules.ger.base.ger_model import GerPais
from app.generics.generic_resource import generic_resource


routes_ger_pais = Blueprint("gerpais", __name__, url_prefix="/api/ger/gerpais")


# ==============================


@routes_ger_pais.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ger_pais_service,
        model=GerPais,
        schema=GerPaisSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ger_pais.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ger_pais_service,
        model=GerPais,
        schema=GerPaisSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ger_pais.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ger_pais_service,
        model=GerPais,
        schema=GerPaisSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ger_pais.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ger_pais_service,
        model=GerPais,
        db_session=current_app.db.session,
    )