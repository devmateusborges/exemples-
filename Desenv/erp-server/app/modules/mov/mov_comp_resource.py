from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.mov.mov_comp_service import mov_comp_service

from app.modules.mov.base.mov_serealizer import MovCompSchema
from app.modules.mov.base.mov_model import MovComp
from app.generics.generic_resource import generic_resource


routes_mov_comp = Blueprint("movcomp", __name__, url_prefix="/api/mov/movcomp")


# ==============================


@routes_mov_comp.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=mov_comp_service,
        model=MovComp,
        schema=MovCompSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_mov_comp.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=mov_comp_service,
        model=MovComp,
        schema=MovCompSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_mov_comp.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=mov_comp_service,
        model=MovComp,
        schema=MovCompSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_mov_comp.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=mov_comp_service,
        model=MovComp,
        db_session=current_app.db.session,
    )
