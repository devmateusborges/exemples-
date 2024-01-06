from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.tst.test1Fk_service import test1Fk_service
from app.generics.generic_resource import generic_resource
from app.modules.tst.base.tst_serealizer import Test1FkSchema
from app.modules.tst.base.tst_model import Test1Fk


routes_test1Fk = Blueprint("test1Fk", __name__, url_prefix="/api/tst/test1fk")

# ==============================


@routes_test1Fk.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=test1Fk_service,
        model=Test1Fk,
        schema=Test1FkSchema,
        db_session=current_app.db.session,
        enabled_filter_fields=["codigo", "descricao"],
    )


# ==============================


@routes_test1Fk.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=test1Fk_service,
        model=Test1Fk,
        schema=Test1FkSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_test1Fk.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=test1Fk_service,
        model=Test1Fk,
        schema=Test1FkSchema,
        db_session=current_app.db.session,
        unique_fields=["codigo"],
    )


# ==============================


@routes_test1Fk.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id, server=test1Fk_service, model=Test1Fk, db_session=current_app.db.session
    )
