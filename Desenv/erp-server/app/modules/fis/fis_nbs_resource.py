from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fis.fis_nbs_service import fis_nbs_service

from app.modules.fis.base.fis_serealizer import FisNbsSchema
from app.modules.fis.base.fis_model import FisNbs
from app.generics.generic_resource import generic_resource


routes_fis_nbs = Blueprint("fisnbs", __name__, url_prefix="/api/fis/fisnbs")


# ==============================


@routes_fis_nbs.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fis_nbs_service,
        model=FisNbs,
        schema=FisNbsSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fis_nbs.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fis_nbs_service,
        model=FisNbs,
        schema=FisNbsSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fis_nbs.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fis_nbs_service,
        model=FisNbs,
        schema=FisNbsSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fis_nbs.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id, service=fis_nbs_service, model=FisNbs, db_session=current_app.db.session
    )
