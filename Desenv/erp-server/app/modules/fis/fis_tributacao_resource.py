from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fis.fis_tributacao_service import fis_tributacao_service

from app.modules.fis.base.fis_serealizer import FisTributacaoSchema
from app.modules.fis.base.fis_model import FisTributacao
from app.generics.generic_resource import generic_resource


routes_fis_tributacao = Blueprint(
    "fistributacao", __name__, url_prefix="/api/fis/fistributacao"
)


# ==============================


@routes_fis_tributacao.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fis_tributacao_service,
        model=FisTributacao,
        schema=FisTributacaoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fis_tributacao.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fis_tributacao_service,
        model=FisTributacao,
        schema=FisTributacaoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fis_tributacao.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fis_tributacao_service,
        model=FisTributacao,
        schema=FisTributacaoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fis_tributacao.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fis_tributacao_service,
        model=FisTributacao,
        db_session=current_app.db.session,
    )
