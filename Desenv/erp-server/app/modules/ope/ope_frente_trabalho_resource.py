from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ope.ope_frente_trabalho_service import ope_frente_trabalho_service

from app.modules.ope.base.ope_serealizer import OpeFrenteTrabalhoSchema
from app.modules.ope.base.ope_model import OpeFrenteTrabalho
from app.generics.generic_resource import generic_resource


routes_ope_frente_trabalho = Blueprint(
    "opefrentetrabalho", __name__, url_prefix="/api/ope/opefrentetrabalho"
)


# ==============================


@routes_ope_frente_trabalho.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ope_frente_trabalho_service,
        model=OpeFrenteTrabalho,
        schema=OpeFrenteTrabalhoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ope_frente_trabalho.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ope_frente_trabalho_service,
        model=OpeFrenteTrabalho,
        schema=OpeFrenteTrabalhoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ope_frente_trabalho.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ope_frente_trabalho_service,
        model=OpeFrenteTrabalho,
        schema=OpeFrenteTrabalhoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ope_frente_trabalho.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ope_frente_trabalho_service,
        model=OpeFrenteTrabalho,
        db_session=current_app.db.session,
    )
