from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.mov.mov_tomador_service import mov_tomador_service

from app.modules.mov.base.mov_serealizer import MovTomadorSchema
from app.modules.mov.base.mov_model import MovTomador
from app.generics.generic_resource import generic_resource


routes_mov_tomador = Blueprint("movtomador", __name__, url_prefix="/api/mov/movtomador")


# ==============================


@routes_mov_tomador.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=mov_tomador_service,
        model=MovTomador,
        schema=MovTomadorSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_mov_tomador.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=mov_tomador_service,
        model=MovTomador,
        schema=MovTomadorSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_mov_tomador.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=mov_tomador_service,
        model=MovTomador,
        schema=MovTomadorSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_mov_tomador.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=mov_tomador_service,
        model=MovTomador,
        db_session=current_app.db.session,
    )
