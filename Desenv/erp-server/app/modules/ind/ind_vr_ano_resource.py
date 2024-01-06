from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ind.ind_vr_ano_service import ind_vr_ano_service

from app.modules.ind.base.ind_serealizer import IndVrAnoSchema
from app.modules.ind.base.ind_model import IndVrAno
from app.generics.generic_resource import generic_resource


routes_ind_vr_ano = Blueprint("indvrano", __name__, url_prefix="/api/ind/indvrano")


# ==============================


@routes_ind_vr_ano.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ind_vr_ano_service,
        model=IndVrAno,
        schema=IndVrAnoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ind_vr_ano.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ind_vr_ano_service,
        model=IndVrAno,
        schema=IndVrAnoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ind_vr_ano.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ind_vr_ano_service,
        model=IndVrAno,
        schema=IndVrAnoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ind_vr_ano.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ind_vr_ano_service,
        model=IndVrAno,
        db_session=current_app.db.session,
    )
