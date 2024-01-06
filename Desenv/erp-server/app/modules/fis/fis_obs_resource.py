from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fis.fis_obs_service import fis_obs_service

from app.modules.fis.base.fis_serealizer import FisObsSchema
from app.modules.fis.base.fis_model import FisObs
from app.generics.generic_resource import generic_resource


routes_fis_obs = Blueprint("fisobs", __name__, url_prefix="/api/fis/fisobs")


# ==============================


@routes_fis_obs.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fis_obs_service,
        model=FisObs,
        schema=FisObsSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fis_obs.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fis_obs_service,
        model=FisObs,
        schema=FisObsSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fis_obs.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fis_obs_service,
        model=FisObs,
        schema=FisObsSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fis_obs.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id, service=fis_obs_service, model=FisObs, db_session=current_app.db.session
    )
