from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fin.fin_cond_pagrec_service import fin_cond_pagrec_service

from app.modules.fin.base.fin_serealizer import FinCondPagrecSchema
from app.modules.fin.base.fin_model import FinCondPagrec
from app.generics.generic_resource import generic_resource


routes_fin_cond_pagrec = Blueprint(
    "fincondpagrec", __name__, url_prefix="/api/fin/fincondpagrec"
)


# ==============================


@routes_fin_cond_pagrec.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fin_cond_pagrec_service,
        model=FinCondPagrec,
        schema=FinCondPagrecSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fin_cond_pagrec.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fin_cond_pagrec_service,
        model=FinCondPagrec,
        schema=FinCondPagrecSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fin_cond_pagrec.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fin_cond_pagrec_service,
        model=FinCondPagrec,
        schema=FinCondPagrecSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fin_cond_pagrec.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fin_cond_pagrec_service,
        model=FinCondPagrec,
        db_session=current_app.db.session,
    )
