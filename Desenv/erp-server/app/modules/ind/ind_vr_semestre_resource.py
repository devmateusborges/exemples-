from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ind.ind_vr_semestre_service import ind_vr_semestre_service

from app.modules.ind.base.ind_serealizer import IndVrSemestreSchema
from app.modules.ind.base.ind_model import IndVrSemestre
from app.generics.generic_resource import generic_resource


routes_ind_vr_semestre = Blueprint(
    "indvrsemestre", __name__, url_prefix="/api/ind/indvrsemestre"
)


# ==============================


@routes_ind_vr_semestre.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ind_vr_semestre_service,
        model=IndVrSemestre,
        schema=IndVrSemestreSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ind_vr_semestre.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ind_vr_semestre_service,
        model=IndVrSemestre,
        schema=IndVrSemestreSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ind_vr_semestre.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ind_vr_semestre_service,
        model=IndVrSemestre,
        schema=IndVrSemestreSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ind_vr_semestre.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ind_vr_semestre_service,
        model=IndVrSemestre,
        db_session=current_app.db.session,
    )
