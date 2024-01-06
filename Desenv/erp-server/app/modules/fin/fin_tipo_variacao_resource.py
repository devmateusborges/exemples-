from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fin.fin_tipo_variacao_service import fin_tipo_variacao_service

from app.modules.fin.base.fin_serealizer import FinTipoVariacaoSchema
from app.modules.fin.base.fin_model import FinTipoVariacao
from app.generics.generic_resource import generic_resource


routes_fin_tipo_variacao = Blueprint(
    "fintipovariacao", __name__, url_prefix="/api/fin/fintipovariacao"
)


# ==============================


@routes_fin_tipo_variacao.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fin_tipo_variacao_service,
        model=FinTipoVariacao,
        schema=FinTipoVariacaoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fin_tipo_variacao.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fin_tipo_variacao_service,
        model=FinTipoVariacao,
        schema=FinTipoVariacaoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fin_tipo_variacao.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fin_tipo_variacao_service,
        model=FinTipoVariacao,
        schema=FinTipoVariacaoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fin_tipo_variacao.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fin_tipo_variacao_service,
        model=FinTipoVariacao,
        db_session=current_app.db.session,
    )
