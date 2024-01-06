from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fin.fin_class_service import fin_class_service

from app.modules.fin.base.fin_serealizer import FinClassSchema
from app.modules.fin.base.fin_model import FinClass
from app.generics.generic_resource import generic_resource


routes_fin_class = Blueprint("finclass", __name__, url_prefix="/api/fin/finclass")


# ==============================


@routes_fin_class.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fin_class_service,
        model=FinClass,
        schema=FinClassSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fin_class.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fin_class_service,
        model=FinClass,
        schema=FinClassSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fin_class.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fin_class_service,
        model=FinClass,
        schema=FinClassSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fin_class.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fin_class_service,
        model=FinClass,
        db_session=current_app.db.session,
    )
