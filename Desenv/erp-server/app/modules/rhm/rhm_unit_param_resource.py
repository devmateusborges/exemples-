from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.rhm.rhm_unit_param_service import rhm_unit_param_service

from app.modules.rhm.base.rhm_serealizer import RhmUnitParamSchema
from app.modules.rhm.base.rhm_model import RhmUnitParam
from app.generics.generic_resource import generic_resource


routes_rhm_unit_param = Blueprint(
    "rhmunitparam", __name__, url_prefix="/api/rhm/rhmunitparam"
)


# ==============================


@routes_rhm_unit_param.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=rhm_unit_param_service,
        model=RhmUnitParam,
        schema=RhmUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_rhm_unit_param.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=rhm_unit_param_service,
        model=RhmUnitParam,
        schema=RhmUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_rhm_unit_param.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=rhm_unit_param_service,
        model=RhmUnitParam,
        schema=RhmUnitParamSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_rhm_unit_param.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=rhm_unit_param_service,
        model=RhmUnitParam,
        db_session=current_app.db.session,
    )
