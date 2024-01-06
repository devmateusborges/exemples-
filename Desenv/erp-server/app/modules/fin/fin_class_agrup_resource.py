from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fin.fin_class_agrup_service import fin_class_agrup_service

from app.modules.fin.base.fin_serealizer import FinClassAgrupSchema
from app.modules.fin.base.fin_model import FinClassAgrup
from app.generics.generic_resource import generic_resource


routes_fin_class_agrup = Blueprint(
    "finclassagrup", __name__, url_prefix="/api/fin/finclassagrup"
)


# ==============================


@routes_fin_class_agrup.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fin_class_agrup_service,
        model=FinClassAgrup,
        schema=FinClassAgrupSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fin_class_agrup.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fin_class_agrup_service,
        model=FinClassAgrup,
        schema=FinClassAgrupSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fin_class_agrup.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fin_class_agrup_service,
        model=FinClassAgrup,
        schema=FinClassAgrupSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fin_class_agrup.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fin_class_agrup_service,
        model=FinClassAgrup,
        db_session=current_app.db.session,
    )
