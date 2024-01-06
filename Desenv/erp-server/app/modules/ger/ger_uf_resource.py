from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ger.ger_uf_service import ger_uf_service

from app.modules.ger.base.ger_serealizer import GerUfSchema
from app.modules.ger.base.ger_model import GerUf
from app.generics.generic_resource import generic_resource


routes_ger_uf = Blueprint("geruf", __name__, url_prefix="/api/ger/geruf")


# ==============================


@routes_ger_uf.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ger_uf_service,
        model=GerUf,
        schema=GerUfSchema,
        db_session=current_app.db.session,
        enabled_filter_fields=["id", "sigla_uf", "nome"],
    )


# ==============================
@routes_ger_uf.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ger_uf_service,
        model=GerUf,
        schema=GerUfSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ger_uf.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ger_uf_service,
        model=GerUf,
        schema=GerUfSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ger_uf.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ger_uf_service,
        model=GerUf,
        db_session=current_app.db.session,
    )
