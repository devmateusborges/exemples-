from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.mov.mov_pedagio_service import mov_pedagio_service

from app.modules.mov.base.mov_serealizer import MovPedagioSchema
from app.modules.mov.base.mov_model import MovPedagio
from app.generics.generic_resource import generic_resource


routes_mov_pedagio = Blueprint("movpedagio", __name__, url_prefix="/api/mov/movpedagio")


# ==============================


@routes_mov_pedagio.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=mov_pedagio_service,
        model=MovPedagio,
        schema=MovPedagioSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_mov_pedagio.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=mov_pedagio_service,
        model=MovPedagio,
        schema=MovPedagioSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_mov_pedagio.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=mov_pedagio_service,
        model=MovPedagio,
        schema=MovPedagioSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_mov_pedagio.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=mov_pedagio_service,
        model=MovPedagio,
        db_session=current_app.db.session,
    )
