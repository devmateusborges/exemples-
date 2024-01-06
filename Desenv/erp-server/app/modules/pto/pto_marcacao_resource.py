from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.pto.pto_marcacao_service import pto_marcacao_service

from app.modules.pto.base.pto_serealizer import PtoMarcacaoSchema
from app.modules.pto.base.pto_model import PtoMarcacao
from app.generics.generic_resource import generic_resource


routes_pto_marcacao = Blueprint("ptomarcacao", __name__, url_prefix="/api/ptomarcacao")


# ==============================


@routes_pto_marcacao.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        pto_marcacao_service, PtoMarcacao, PtoMarcacaoSchema, current_app.db.session
    )


# ==============================
@routes_pto_marcacao.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=pto_marcacao_service,
        model=PtoMarcacao,
        schema=PtoMarcacaoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_pto_marcacao.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=pto_marcacao_service,
        model=PtoMarcacao,
        schema=PtoMarcacaoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_pto_marcacao.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=pto_marcacao_service,
        model=PtoMarcacao,
        db_session=current_app.db.session,
    )
