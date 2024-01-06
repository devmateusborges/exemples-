from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.mov.mov_unit_param_service import mov_unit_param_service

from app.modules.mov.base.mov_serealizer import MovUnitParamSchema
from app.modules.mov.base.mov_model import MovUnitParam
from app.generics.generic_resource import generic_resource


routes_mov_unit_param = Blueprint(
    "movunitparam", __name__, url_prefix="/api/mov/movunitparam"
)


# ==============================


@routes_mov_unit_param.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=mov_unit_param_service,
        model=MovUnitParam,
        schema=MovUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_mov_unit_param.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=mov_unit_param_service,
        model=MovUnitParam,
        schema=MovUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_mov_unit_param.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=mov_unit_param_service,
        model=MovUnitParam,
        schema=MovUnitParamSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_mov_unit_param.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=mov_unit_param_service,
        model=MovUnitParam,
        db_session=current_app.db.session,
    )
