from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fis.fis_ncm_service import fis_ncm_service

from app.modules.fis.base.fis_serealizer import FisNcmSchema
from app.modules.fis.base.fis_model import FisNcm
from app.generics.generic_resource import generic_resource


routes_fis_ncm = Blueprint("fisncm", __name__, url_prefix="/api/fis/fisncm")


# ==============================


@routes_fis_ncm.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fis_ncm_service,
        model=FisNcm,
        schema=FisNcmSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fis_ncm.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fis_ncm_service,
        model=FisNcm,
        schema=FisNcmSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fis_ncm.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fis_ncm_service,
        model=FisNcm,
        schema=FisNcmSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fis_ncm.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id, service=fis_ncm_service, model=FisNcm, db_session=current_app.db.session
    )
