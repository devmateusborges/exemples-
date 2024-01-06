from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.mov.mov_status_service import mov_status_service

from app.modules.mov.base.mov_serealizer import MovStatusSchema
from app.modules.mov.base.mov_model import MovStatus
from app.generics.generic_resource import generic_resource


routes_mov_status = Blueprint("movstatus", __name__, url_prefix="/api/mov/movstatus")


# ==============================


@routes_mov_status.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=mov_status_service,
        model=MovStatus,
        schema=MovStatusSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_mov_status.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=mov_status_service,
        model=MovStatus,
        schema=MovStatusSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_mov_status.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=mov_status_service,
        model=MovStatus,
        schema=MovStatusSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_mov_status.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=mov_status_service,
        model=MovStatus,
        db_session=current_app.db.session,
    )
