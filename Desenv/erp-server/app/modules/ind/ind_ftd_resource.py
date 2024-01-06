from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ind.ind_ftd_service import ind_ftd_service

from app.modules.ind.base.ind_serealizer import IndFtdSchema
from app.modules.ind.base.ind_model import IndFtd
from app.generics.generic_resource import generic_resource


routes_ind_ftd = Blueprint("indftd", __name__, url_prefix="/api/ind/indftd")


# ==============================


@routes_ind_ftd.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ind_ftd_service,
        model=IndFtd,
        schema=IndFtdSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ind_ftd.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ind_ftd_service,
        model=IndFtd,
        schema=IndFtdSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ind_ftd.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ind_ftd_service,
        model=IndFtd,
        schema=IndFtdSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ind_ftd.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id, service=ind_ftd_service, model=IndFtd, db_session=current_app.db.session
    )
