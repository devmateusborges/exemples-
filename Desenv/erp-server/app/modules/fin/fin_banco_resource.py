from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fin.fin_banco_service import fin_banco_service

from app.modules.fin.base.fin_serealizer import FinBancoSchema
from app.modules.fin.base.fin_model import FinBanco
from app.generics.generic_resource import generic_resource


routes_fin_banco = Blueprint("finbanco", __name__, url_prefix="/api/fin/finbanco")


# ==============================


@routes_fin_banco.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fin_banco_service,
        model=FinBanco,
        schema=FinBancoSchema,
        db_session=current_app.db.session,
        enabled_filter_fields=["id", "nome", "nr_banco"],
    )


# ==============================
@routes_fin_banco.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fin_banco_service,
        model=FinBanco,
        schema=FinBancoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fin_banco.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fin_banco_service,
        model=FinBanco,
        schema=FinBancoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fin_banco.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fin_banco_service,
        model=FinBanco,
        db_session=current_app.db.session,
    )
