from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.crm.crm_etapa_service import crm_etapa_service

from app.modules.crm.base.crm_serealizer import CrmEtapaSchema
from app.modules.crm.base.crm_model import CrmEtapa
from app.generics.generic_resource import generic_resource


routes_crm_etapa = Blueprint("crmetapa", __name__, url_prefix="/api/crm/crmetapa")


# ==============================


@routes_crm_etapa.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=crm_etapa_service,
        model=CrmEtapa,
        schema=CrmEtapaSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_crm_etapa.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=crm_etapa_service,
        model=CrmEtapa,
        schema=CrmEtapaSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_crm_etapa.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=crm_etapa_service,
        model=CrmEtapa,
        schema=CrmEtapaSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_crm_etapa.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=crm_etapa_service,
        model=CrmEtapa,
        db_session=current_app.db.session,
    )
