from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ope.ope_ocor_prev_service import ope_ocor_prev_service

from app.modules.ope.base.ope_serealizer import OpeOcorPrevSchema
from app.modules.ope.base.ope_model import OpeOcorPrev
from app.generics.generic_resource import generic_resource


routes_ope_ocor_prev = Blueprint(
    "opeocorprev", __name__, url_prefix="/api/ope/opeocorprev"
)


# ==============================


@routes_ope_ocor_prev.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ope_ocor_prev_service,
        model=OpeOcorPrev,
        schema=OpeOcorPrevSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ope_ocor_prev.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ope_ocor_prev_service,
        model=OpeOcorPrev,
        schema=OpeOcorPrevSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ope_ocor_prev.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ope_ocor_prev_service,
        model=OpeOcorPrev,
        schema=OpeOcorPrevSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ope_ocor_prev.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ope_ocor_prev_service,
        model=OpeOcorPrev,
        db_session=current_app.db.session,
    )
