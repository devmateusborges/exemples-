from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ctb.ctb_lote_service import ctb_lote_service

from app.modules.ctb.base.ctb_serealizer import CtbLoteSchema
from app.modules.ctb.base.ctb_model import CtbLote
from app.generics.generic_resource import generic_resource


routes_ctb_lote = Blueprint("ctblote", __name__, url_prefix="/api/ctb/ctblote")


# ==============================


@routes_ctb_lote.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ctb_lote_service,
        model=CtbLote,
        schema=CtbLoteSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ctb_lote.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ctb_lote_service,
        model=CtbLote,
        schema=CtbLoteSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ctb_lote.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ctb_lote_service,
        model=CtbLote,
        schema=CtbLoteSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ctb_lote.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ctb_lote_service,
        model=CtbLote,
        db_session=current_app.db.session,
    )
