from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ger.ger_empresa_service import ger_empresa_service

from app.modules.ger.base.ger_serealizer import GerEmpresaSchema
from app.modules.ger.base.ger_model import GerEmpresa
from app.generics.generic_resource import generic_resource


routes_ger_empresa = Blueprint("gerempresa", __name__, url_prefix="/api/ger/gerempresa")


# ==============================


@routes_ger_empresa.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ger_empresa_service,
        model=GerEmpresa,
        schema=GerEmpresaSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ger_empresa.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ger_empresa_service,
        model=GerEmpresa,
        schema=GerEmpresaSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ger_empresa.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ger_empresa_service,
        model=GerEmpresa,
        schema=GerEmpresaSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ger_empresa.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ger_empresa_service,
        model=GerEmpresa,
        db_session=current_app.db.session,
    )
