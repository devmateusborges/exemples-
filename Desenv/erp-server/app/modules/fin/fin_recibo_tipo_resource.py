from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fin.fin_recibo_tipo_service import fin_recibo_tipo_service

from app.modules.fin.base.fin_serealizer import FinReciboTipoSchema
from app.modules.fin.base.fin_model import FinReciboTipo
from app.generics.generic_resource import generic_resource


routes_fin_recibo_tipo = Blueprint(
    "finrecibotipo", __name__, url_prefix="/api/fin/finrecibotipo"
)


# ==============================


@routes_fin_recibo_tipo.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fin_recibo_tipo_service,
        model=FinReciboTipo,
        schema=FinReciboTipoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fin_recibo_tipo.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fin_recibo_tipo_service,
        model=FinReciboTipo,
        schema=FinReciboTipoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fin_recibo_tipo.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fin_recibo_tipo_service,
        model=FinReciboTipo,
        schema=FinReciboTipoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fin_recibo_tipo.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fin_recibo_tipo_service,
        model=FinReciboTipo,
        db_session=current_app.db.session,
    )
