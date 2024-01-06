from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.mov.mov_condutor_service import mov_condutor_service

from app.modules.mov.base.mov_serealizer import MovCondutorSchema
from app.modules.mov.base.mov_model import MovCondutor
from app.generics.generic_resource import generic_resource


routes_mov_condutor = Blueprint(
    "movcondutor", __name__, url_prefix="/api/mov/movcondutor"
)


# ==============================


@routes_mov_condutor.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=mov_condutor_service,
        model=MovCondutor,
        schema=MovCondutorSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_mov_condutor.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=mov_condutor_service,
        model=MovCondutor,
        schema=MovCondutorSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_mov_condutor.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=mov_condutor_service,
        model=MovCondutor,
        schema=MovCondutorSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_mov_condutor.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=mov_condutor_service,
        model=MovCondutor,
        db_session=current_app.db.session,
    )
