from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ind.ind_rel_service import ind_rel_service

from app.modules.ind.base.ind_serealizer import IndRelSchema
from app.modules.ind.base.ind_model import IndRel
from app.generics.generic_resource import generic_resource
from app.utils.funcs_util import funcs_util


routes_ind_rel = Blueprint("indrel", __name__, url_prefix="/api/ind/indrel")


# ==============================


@routes_ind_rel.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ind_rel_service,
        model=IndRel,
        schema=IndRelSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ind_rel.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ind_rel_service,
        model=IndRel,
        schema=IndRelSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ind_rel.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ind_rel_service,
        model=IndRel,
        schema=IndRelSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ind_rel.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id, service=ind_rel_service, model=IndRel, db_session=current_app.db.session
    )


@routes_ind_rel.route("/generatereport", methods=["POST"])
@jwt_required()
def generate_report():

    srv = ind_rel_service(model=IndRel)

    result = srv.generate_report(
        session=current_app.db.session, body=request.get_json()
    )
    return funcs_util.getResponseJsonCode(
        code=200, msg="Report in processing queue", data=result
    )
