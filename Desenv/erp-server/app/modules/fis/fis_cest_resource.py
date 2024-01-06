from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fis.fis_cest_service import fis_cest_service

from app.modules.fis.base.fis_serealizer import FisCestSchema
from app.modules.fis.base.fis_model import FisCest
from app.generics.generic_resource import generic_resource


routes_fis_cest = Blueprint("fiscest", __name__, url_prefix="/api/fis/fiscest")


# ==============================


@routes_fis_cest.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fis_cest_service,
        model=FisCest,
        schema=FisCestSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fis_cest.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fis_cest_service,
        model=FisCest,
        schema=FisCestSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fis_cest.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fis_cest_service,
        model=FisCest,
        schema=FisCestSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fis_cest.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fis_cest_service,
        model=FisCest,
        db_session=current_app.db.session,
    )
