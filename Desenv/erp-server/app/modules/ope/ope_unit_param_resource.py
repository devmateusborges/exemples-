from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ope.ope_unit_param_service import ope_unit_param_service

from app.modules.ope.base.ope_serealizer import OpeUnitParamSchema
from app.modules.ope.base.ope_model import OpeUnitParam
from app.generics.generic_resource import generic_resource


routes_ope_unit_param = Blueprint(
    "opeunitparam", __name__, url_prefix="/api/ope/opeunitparam"
)


# ==============================


@routes_ope_unit_param.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ope_unit_param_service,
        model=OpeUnitParam,
        schema=OpeUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ope_unit_param.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ope_unit_param_service,
        model=OpeUnitParam,
        schema=OpeUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ope_unit_param.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ope_unit_param_service,
        model=OpeUnitParam,
        schema=OpeUnitParamSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ope_unit_param.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ope_unit_param_service,
        model=OpeUnitParam,
        db_session=current_app.db.session,
    )
