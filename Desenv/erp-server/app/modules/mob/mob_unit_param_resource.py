from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.mob.mob_unit_param_service import mob_unit_param_service

from app.modules.mob.base.mob_serealizer import MobUnitParamSchema
from app.modules.mob.base.mob_model import MobUnitParam
from app.generics.generic_resource import generic_resource


routes_mob_unit_param = Blueprint(
    "mobunitparam", __name__, url_prefix="/api/mob/mobunitparam"
)


# ==============================


@routes_mob_unit_param.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=mob_unit_param_service,
        model=MobUnitParam,
        schema=MobUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_mob_unit_param.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=mob_unit_param_service,
        model=MobUnitParam,
        schema=MobUnitParamSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_mob_unit_param.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=mob_unit_param_service,
        model=MobUnitParam,
        schema=MobUnitParamSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_mob_unit_param.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=mob_unit_param_service,
        model=MobUnitParam,
        db_session=current_app.db.session,
    )
