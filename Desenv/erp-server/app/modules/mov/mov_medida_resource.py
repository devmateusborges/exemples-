from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.mov.mov_medida_service import mov_medida_service

from app.modules.mov.base.mov_serealizer import MovMedidaSchema
from app.modules.mov.base.mov_model import MovMedida
from app.generics.generic_resource import generic_resource


routes_mov_medida = Blueprint("movmedida", __name__, url_prefix="/api/mov/movmedida")


# ==============================


@routes_mov_medida.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=mov_medida_service,
        model=MovMedida,
        schema=MovMedidaSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_mov_medida.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=mov_medida_service,
        model=MovMedida,
        schema=MovMedidaSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_mov_medida.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=mov_medida_service,
        model=MovMedida,
        schema=MovMedidaSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_mov_medida.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=mov_medida_service,
        model=MovMedida,
        db_session=current_app.db.session,
    )
