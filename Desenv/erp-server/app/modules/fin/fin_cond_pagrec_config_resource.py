from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fin.fin_cond_pagrec_config_service import (
    fin_cond_pagrec_config_service,
)

from app.modules.fin.base.fin_serealizer import FinCondPagrecConfigSchema
from app.modules.fin.base.fin_model import FinCondPagrecConfig
from app.generics.generic_resource import generic_resource


routes_fin_cond_pagrec_config = Blueprint(
    "fincondpagrecconfig", __name__, url_prefix="/api/fin/fincondpagrecconfig"
)


# ==============================


@routes_fin_cond_pagrec_config.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fin_cond_pagrec_config_service,
        model=FinCondPagrecConfig,
        schema=FinCondPagrecConfigSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fin_cond_pagrec_config.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fin_cond_pagrec_config_service,
        model=FinCondPagrecConfig,
        schema=FinCondPagrecConfigSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fin_cond_pagrec_config.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fin_cond_pagrec_config_service,
        model=FinCondPagrecConfig,
        schema=FinCondPagrecConfigSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fin_cond_pagrec_config.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fin_cond_pagrec_config_service,
        model=FinCondPagrecConfig,
        db_session=current_app.db.session,
    )
