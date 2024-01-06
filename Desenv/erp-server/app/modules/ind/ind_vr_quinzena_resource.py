from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ind.ind_vr_quinzena_service import ind_vr_quinzena_service

from app.modules.ind.base.ind_serealizer import IndVrQuinzenaSchema
from app.modules.ind.base.ind_model import IndVrQuinzena
from app.generics.generic_resource import generic_resource


routes_ind_vr_quinzena = Blueprint(
    "indvrquinzena", __name__, url_prefix="/api/ind/indvrquinzena"
)


# ==============================


@routes_ind_vr_quinzena.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ind_vr_quinzena_service,
        model=IndVrQuinzena,
        schema=IndVrQuinzenaSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ind_vr_quinzena.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ind_vr_quinzena_service,
        model=IndVrQuinzena,
        schema=IndVrQuinzenaSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ind_vr_quinzena.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ind_vr_quinzena_service,
        model=IndVrQuinzena,
        schema=IndVrQuinzenaSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ind_vr_quinzena.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ind_vr_quinzena_service,
        model=IndVrQuinzena,
        db_session=current_app.db.session,
    )
