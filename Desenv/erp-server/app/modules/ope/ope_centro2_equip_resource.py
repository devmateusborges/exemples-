from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ope.ope_centro2_equip_service import ope_centro2_equip_service

from app.modules.ope.base.ope_serealizer import OpeCentro2EquipSchema
from app.modules.ope.base.ope_model import OpeCentro2Equip
from app.generics.generic_resource import generic_resource


routes_ope_centro2_equip = Blueprint(
    "opecentro2equip", __name__, url_prefix="/api/ope/opecentro2equip"
)


# ==============================


@routes_ope_centro2_equip.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ope_centro2_equip_service,
        model=OpeCentro2Equip,
        schema=OpeCentro2EquipSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ope_centro2_equip.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ope_centro2_equip_service,
        model=OpeCentro2Equip,
        schema=OpeCentro2EquipSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ope_centro2_equip.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ope_centro2_equip_service,
        model=OpeCentro2Equip,
        schema=OpeCentro2EquipSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ope_centro2_equip.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ope_centro2_equip_service,
        model=OpeCentro2Equip,
        db_session=current_app.db.session,
    )
