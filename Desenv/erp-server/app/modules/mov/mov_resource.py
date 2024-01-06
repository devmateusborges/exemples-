from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.mov.mov_service import mov_service

from app.modules.mov.base.mov_serealizer import MovSchema
from app.modules.mov.base.mov_model import Mov
from app.generics.generic_resource import generic_resource


routes_mov = Blueprint("mov", __name__, url_prefix="/api/mov/mov")


# ==============================


@routes_mov.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=mov_service,
        model=Mov,
        schema=MovSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_mov.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=mov_service,
        model=Mov,
        schema=MovSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_mov.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=mov_service,
        model=Mov,
        schema=MovSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_mov.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id, service=mov_service, model=Mov, db_session=current_app.db.session
    )
