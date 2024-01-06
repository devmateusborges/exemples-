from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.crm.crm_aviso_org_service import crm_aviso_org_service

from app.modules.crm.base.crm_serealizer import CrmAvisoOrgSchema
from app.modules.crm.base.crm_model import CrmAvisoOrg
from app.generics.generic_resource import generic_resource


routes_crm_aviso_org = Blueprint(
    "crmavisoorg", __name__, url_prefix="/api/crm/crmavisoorg"
)


# ==============================


@routes_crm_aviso_org.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=crm_aviso_org_service,
        model=CrmAvisoOrg,
        schema=CrmAvisoOrgSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_crm_aviso_org.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=crm_aviso_org_service,
        model=CrmAvisoOrg,
        schema=CrmAvisoOrgSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_crm_aviso_org.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=crm_aviso_org_service,
        model=CrmAvisoOrg,
        schema=CrmAvisoOrgSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_crm_aviso_org.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=crm_aviso_org_service,
        model=CrmAvisoOrg,
        db_session=current_app.db.session,
    )
