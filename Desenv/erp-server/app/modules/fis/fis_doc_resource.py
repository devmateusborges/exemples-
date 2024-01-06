from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fis.fis_doc_service import fis_doc_service

from app.modules.fis.base.fis_serealizer import FisDocSchema
from app.modules.fis.base.fis_model import FisDoc
from app.generics.generic_resource import generic_resource


routes_fis_doc = Blueprint("fisdoc", __name__, url_prefix="/api/fis/fisdoc")


# ==============================


@routes_fis_doc.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fis_doc_service,
        model=FisDoc,
        schema=FisDocSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fis_doc.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fis_doc_service,
        model=FisDoc,
        schema=FisDocSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fis_doc.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fis_doc_service,
        model=FisDoc,
        schema=FisDocSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fis_doc.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(id, fis_doc_service, FisDoc, current_app.db.session)
