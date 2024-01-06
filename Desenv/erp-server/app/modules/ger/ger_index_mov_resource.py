from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ger.ger_index_mov_service import ger_index_mov_service

from app.modules.ger.base.ger_serealizer import GerIndexMovSchema
from app.modules.ger.base.ger_model import GerIndexMov
from app.generics.generic_resource import generic_resource


routes_ger_index_mov = Blueprint(
    "gerindexmov", __name__, url_prefix="/api/ger/gerindexmov"
)


# ==============================


@routes_ger_index_mov.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ger_index_mov_service,
        model=GerIndexMov,
        schema=GerIndexMovSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ger_index_mov.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ger_index_mov_service,
        model=GerIndexMov,
        schema=GerIndexMovSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ger_index_mov.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ger_index_mov_service,
        model=GerIndexMov,
        schema=GerIndexMovSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ger_index_mov.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ger_index_mov_service,
        model=GerIndexMov,
        db_session=current_app.db.session,
    )
