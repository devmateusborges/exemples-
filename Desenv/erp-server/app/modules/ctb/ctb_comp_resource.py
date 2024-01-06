from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ctb.ctb_comp_service import ctb_comp_service

from app.modules.ctb.base.ctb_serealizer import CtbCompSchema
from app.modules.ctb.base.ctb_model import CtbComp
from app.generics.generic_resource import generic_resource


routes_ctb_comp = Blueprint("ctbcomp", __name__, url_prefix="/api/ctb/ctbcomp")


# ==============================


@routes_ctb_comp.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ctb_comp_service,
        model=CtbComp,
        schema=CtbCompSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ctb_comp.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ctb_comp_service,
        model=CtbComp,
        schema=CtbCompSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ctb_comp.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ctb_comp_service,
        model=CtbComp,
        schema=CtbCompSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ctb_comp.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ctb_comp_service,
        model=CtbComp,
        db_session=current_app.db.session,
    )
