from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.pto.pto_medidor_service import pto_medidor_service

from app.modules.pto.base.pto_serealizer import PtoMedidorSchema
from app.modules.pto.base.pto_model import PtoMedidor
from app.generics.generic_resource import generic_resource


routes_pto_medidor = Blueprint("ptomedidor", __name__, url_prefix="/api/pto/ptomedidor")


# ==============================


@routes_pto_medidor.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=pto_medidor_service,
        model=PtoMedidor,
        schema=PtoMedidorSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_pto_medidor.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=pto_medidor_service,
        model=PtoMedidor,
        schema=PtoMedidorSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_pto_medidor.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=pto_medidor_service,
        model=PtoMedidor,
        schema=PtoMedidorSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_pto_medidor.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=pto_medidor_service,
        model=PtoMedidor,
        db_session=current_app.db.session,
    )
