from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fin.fin_conta_service import fin_conta_service

from app.modules.fin.base.fin_serealizer import FinContaSchema
from app.modules.fin.base.fin_model import FinConta
from app.generics.generic_resource import generic_resource


routes_fin_conta = Blueprint("finconta", __name__, url_prefix="/api/fin/finconta")


# ==============================


@routes_fin_conta.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fin_conta_service,
        model=FinConta,
        schema=FinContaSchema,
        db_session=current_app.db.session,
        enabled_filter_fields=["nome", "id"],
    )


# ==============================
@routes_fin_conta.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fin_conta_service,
        model=FinConta,
        schema=FinContaSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fin_conta.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fin_conta_service,
        model=FinConta,
        schema=FinContaSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fin_conta.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fin_conta_service,
        model=FinConta,
        db_session=current_app.db.session,
    )
