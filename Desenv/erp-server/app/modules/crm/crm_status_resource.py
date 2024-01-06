from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.crm.crm_status_service import crm_status_service

from app.modules.crm.base.crm_serealizer import CrmStatusSchema
from app.modules.crm.base.crm_model import CrmStatus
from app.generics.generic_resource import generic_resource


routes_crm_status = Blueprint("crmstatus", __name__, url_prefix="/api/crm/crmstatus")


# ==============================


@routes_crm_status.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=crm_status_service,
        model=CrmStatus,
        schema=CrmStatusSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_crm_status.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=crm_status_service,
        model=CrmStatus,
        schema=CrmStatusSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_crm_status.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=crm_status_service,
        model=CrmStatus,
        schema=CrmStatusSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_crm_status.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=crm_status_service,
        model=CrmStatus,
        db_session=current_app.db.session,
    )
