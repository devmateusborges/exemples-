from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ind.ind_pnl_service import ind_pnl_service

from app.modules.ind.base.ind_serealizer import IndPnlSchema
from app.modules.ind.base.ind_model import IndPnl
from app.generics.generic_resource import generic_resource


routes_ind_pnl = Blueprint("indpnl", __name__, url_prefix="/api/ind/indpnl")


# ==============================


@routes_ind_pnl.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ind_pnl_service,
        model=IndPnl,
        schema=IndPnlSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ind_pnl.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ind_pnl_service,
        model=IndPnl,
        schema=IndPnlSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ind_pnl.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ind_pnl_service,
        model=IndPnl,
        schema=IndPnlSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ind_pnl.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id, service=ind_pnl_service, model=IndPnl, db_session=current_app.db.session
    )
