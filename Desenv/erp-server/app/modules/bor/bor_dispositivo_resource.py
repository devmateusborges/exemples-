from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.bor.bor_dispositivo_service import bor_dispositivo_service

from app.modules.bor.base.bor_serealizer import BorDispositivoSchema
from app.modules.bor.base.bor_model import BorDispositivo
from app.generics.generic_resource import generic_resource


routes_bor_dispositivo = Blueprint(
    "bordispositivo", __name__, url_prefix="/api/bor/bordispositivo"
)


# ==============================


@routes_bor_dispositivo.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=bor_dispositivo_service,
        model=BorDispositivo,
        schema=BorDispositivoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_bor_dispositivo.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=bor_dispositivo_service,
        model=BorDispositivo,
        schema=BorDispositivoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_bor_dispositivo.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=bor_dispositivo_service,
        model=BorDispositivo,
        schema=BorDispositivoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_bor_dispositivo.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=bor_dispositivo_service,
        model=BorDispositivo,
        db_session=current_app.db.session,
    )
