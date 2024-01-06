from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.bov.bov_unit_param_service import bov_unit_param_service

from app.modules.bov.base.bov_serealizer import BovUnitParamSchema
from app.modules.bov.base.bov_model import BovUnitParam
from app.generics.generic_resource import generic_resource

routes_bov_unit_param = Blueprint(
    "bovunitparam", __name__, url_prefix="/api/bov/bovunitparam"
)


# ==============================


@routes_bov_unit_param.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=bov_unit_param_service,
        model=BovUnitParam,
        schema=BovUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_bov_unit_param.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=bov_unit_param_service,
        model=BovUnitParam,
        schema=BovUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_bov_unit_param.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=bov_unit_param_service,
        model=BovUnitParam,
        schema=BovUnitParamSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_bov_unit_param.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=bov_unit_param_service,
        model=BovUnitParam,
        db_session=current_app.db.session,
    )
