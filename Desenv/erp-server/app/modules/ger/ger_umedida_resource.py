from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ger.ger_umedida_service import ger_umedida_service

from app.modules.ger.base.ger_serealizer import GerUmedidaSchema
from app.modules.ger.base.ger_model import GerUmedida
from app.generics.generic_resource import generic_resource


routes_ger_umedida = Blueprint("gerumedida", __name__, url_prefix="/api/ger/gerumedida")


# ==============================


@routes_ger_umedida.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ger_umedida_service,
        model=GerUmedida,
        schema=GerUmedidaSchema,
        db_session=current_app.db.session,
        enabled_filter_fields=["nome", "id", "sigla_umedida"],
    )


# ==============================
@routes_ger_umedida.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ger_umedida_service,
        model=GerUmedida,
        schema=GerUmedidaSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ger_umedida.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ger_umedida_service,
        model=GerUmedida,
        schema=GerUmedidaSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ger_umedida.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ger_umedida_service,
        model=GerUmedida,
        db_session=current_app.db.session,
    )
