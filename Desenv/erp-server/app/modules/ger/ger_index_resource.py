from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ger.ger_index_service import ger_index_service

from app.modules.ger.base.ger_serealizer import GerIndexSchema
from app.modules.ger.base.ger_model import GerIndex
from app.generics.generic_resource import generic_resource


routes_ger_index = Blueprint("gerindex", __name__, url_prefix="/api/ger/gerindex")


# ==============================


@routes_ger_index.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ger_index_service,
        model=GerIndex,
        schema=GerIndexSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ger_index.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ger_index_service,
        model=GerIndex,
        schema=GerIndexSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ger_index.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ger_index_service,
        model=GerIndex,
        schema=GerIndexSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ger_index.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ger_index_service,
        model=GerIndex,
        db_session=current_app.db.session,
    )
