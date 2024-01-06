from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.bor.bor_unit_param_service import bor_unit_param_service

from app.modules.bor.base.bor_serealizer import BorUnitParamSchema
from app.modules.bor.base.bor_model import BorUnitParam
from app.generics.generic_resource import generic_resource


routes_bor_unit_param = Blueprint(
    "borunitparam", __name__, url_prefix="/api/bor/borunitparam"
)


# ==============================


@routes_bor_unit_param.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=bor_unit_param_service,
        model=BorUnitParam,
        schema=BorUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_bor_unit_param.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=bor_unit_param_service,
        model=BorUnitParam,
        schema=BorUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_bor_unit_param.route("/", methods=["POST"])
@jwt_required()
def save():

    return generic_resource.save(
        body=request.get_json(),
        service=bor_unit_param_service,
        model=BorUnitParam,
        schema=BorUnitParamSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_bor_unit_param.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=bor_unit_param_service,
        model=BorUnitParam,
        db_session=current_app.db.session,
    )
