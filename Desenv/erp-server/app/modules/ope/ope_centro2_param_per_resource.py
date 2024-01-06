from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required
from app.modules.ope.ope_centro2_param_per_service import ope_centro2_param_per_service

from app.modules.ope.base.ope_serealizer import OpeCentro2ParamPerSchema
from app.modules.ope.base.ope_model import OpeCentro2ParamPer
from app.generics.generic_resource import generic_resource


routes_ope_centro2_param_per = Blueprint(
    "opecentro2paramper", __name__, url_prefix="/api/ope/opecentro2paramper"
)


# ==============================


@routes_ope_centro2_param_per.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ope_centro2_param_per_service,
        model=OpeCentro2ParamPer,
        schema=OpeCentro2ParamPerSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ope_centro2_param_per.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ope_centro2_param_per_service,
        model=OpeCentro2ParamPer,
        schema=OpeCentro2ParamPerSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ope_centro2_param_per.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ope_centro2_param_per_service,
        model=OpeCentro2ParamPer,
        schema=OpeCentro2ParamPerSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ope_centro2_param_per.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ope_centro2_param_per_service,
        model=OpeCentro2ParamPer,
        db_session=current_app.db.session,
    )
