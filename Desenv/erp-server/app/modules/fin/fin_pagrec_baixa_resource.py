from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fin.fin_pagrec_baixa_service import fin_pagrec_baixa_service

from app.modules.fin.base.fin_serealizer import FinPagrecBaixaSchema
from app.modules.fin.base.fin_model import FinPagrecBaixa
from app.generics.generic_resource import generic_resource


routes_fin_pagrec_baixa = Blueprint(
    "finpagrecbaixa", __name__, url_prefix="/api/fin/finpagrecbaixa"
)


# ==============================


@routes_fin_pagrec_baixa.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fin_pagrec_baixa_service,
        model=FinPagrecBaixa,
        schema=FinPagrecBaixaSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fin_pagrec_baixa.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fin_pagrec_baixa_service,
        model=FinPagrecBaixa,
        schema=FinPagrecBaixaSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fin_pagrec_baixa.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fin_pagrec_baixa_service,
        model=FinPagrecBaixa,
        schema=FinPagrecBaixaSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fin_pagrec_baixa.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fin_pagrec_baixa_service,
        model=FinPagrecBaixa,
        db_session=current_app.db.session,
    )
