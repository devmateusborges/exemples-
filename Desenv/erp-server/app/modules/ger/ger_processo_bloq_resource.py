from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ger.ger_processo_bloq_service import ger_processo_bloq_service

from app.modules.ger.base.ger_serealizer import GerProcessoBloqSchema
from app.modules.ger.base.ger_model import GerProcessoBloq
from app.generics.generic_resource import generic_resource


routes_ger_processo_bloq = Blueprint(
    "gerprocessobloq", __name__, url_prefix="/api/ger/gerprocessobloq"
)


# ==============================


@routes_ger_processo_bloq.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ger_processo_bloq_service,
        model=GerProcessoBloq,
        schema=GerProcessoBloqSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ger_processo_bloq.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ger_processo_bloq_service,
        model=GerProcessoBloq,
        schema=GerProcessoBloqSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ger_processo_bloq.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ger_processo_bloq_service,
        model=GerProcessoBloq,
        schema=GerProcessoBloqSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ger_processo_bloq.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ger_processo_bloq_service,
        model=GerProcessoBloq,
        db_session=current_app.db.session,
    )
