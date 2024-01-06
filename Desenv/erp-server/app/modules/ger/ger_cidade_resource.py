from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ger.ger_cidade_service import ger_cidade_service

from app.modules.ger.base.ger_serealizer import GerCidadeSchema
from app.modules.ger.base.ger_model import GerCidade
from app.generics.generic_resource import generic_resource


routes_ger_cidade = Blueprint("gercidade", __name__, url_prefix="/api/ger/gercidade")


# ==============================


@routes_ger_cidade.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ger_cidade_service,
        model=GerCidade,
        schema=GerCidadeSchema,
        db_session=current_app.db.session,
        enabled_filter_fields=["id", "nr_cidade", "nome"],
    )


# ==============================
@routes_ger_cidade.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ger_cidade_service,
        model=GerCidade,
        schema=GerCidadeSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ger_cidade.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ger_cidade_service,
        model=GerCidade,
        schema=GerCidadeSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ger_cidade.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ger_cidade_service,
        model=GerCidade,
        db_session=current_app.db.session,
    )
