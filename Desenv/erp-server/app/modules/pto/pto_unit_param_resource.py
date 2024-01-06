from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.pto.pto_unit_param_service import pto_unit_param_service

from app.modules.pto.base.pto_serealizer import PtoUnitParamSchema
from app.modules.pto.base.pto_model import PtoUnitParam
from app.generics.generic_resource import generic_resource


routes_pto_unit_param = Blueprint(
    "ptounitparam", __name__, url_prefix="/api/pto/ptounitparam"
)


# ==============================


@routes_pto_unit_param.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=pto_unit_param_service,
        model=PtoUnitParam,
        schema=PtoUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_pto_unit_param.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=pto_unit_param_service,
        model=PtoUnitParam,
        schema=PtoUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_pto_unit_param.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=pto_unit_param_service,
        model=PtoUnitParam,
        schema=PtoUnitParamSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_pto_unit_param.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=pto_unit_param_service,
        model=PtoUnitParam,
        db_session=current_app.db.session,
    )
