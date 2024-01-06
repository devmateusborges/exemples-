from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.mov.mov_percurso_service import mov_percurso_service

from app.modules.mov.base.mov_serealizer import MovPercursoSchema
from app.modules.mov.base.mov_model import MovPercurso
from app.generics.generic_resource import generic_resource


routes_mov_percurso = Blueprint(
    "movpercurso", __name__, url_prefix="/api/mov/movpercurso"
)


# ==============================


@routes_mov_percurso.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=mov_percurso_service,
        model=MovPercurso,
        schema=MovPercursoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_mov_percurso.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=mov_percurso_service,
        model=MovPercurso,
        schema=MovPercursoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_mov_percurso.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=mov_percurso_service,
        model=MovPercurso,
        schema=MovPercursoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_mov_percurso.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=mov_percurso_service,
        model=MovPercurso,
        db_session=current_app.db.session,
    )
