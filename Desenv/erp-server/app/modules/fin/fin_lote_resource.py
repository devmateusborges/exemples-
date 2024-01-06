from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fin.fin_lote_service import fin_lote_service

from app.modules.fin.base.fin_serealizer import FinLoteSchema
from app.modules.fin.base.fin_model import FinLote
from app.generics.generic_resource import generic_resource


routes_fin_lote = Blueprint("finlote", __name__, url_prefix="/api/fin/finlote")


# ==============================


@routes_fin_lote.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fin_lote_service,
        model=FinLote,
        schema=FinLoteSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fin_lote.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fin_lote_service,
        model=FinLote,
        schema=FinLoteSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fin_lote.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fin_lote_service,
        model=FinLote,
        schema=FinLoteSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fin_lote.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fin_lote_service,
        model=FinLote,
        db_session=current_app.db.session,
    )
