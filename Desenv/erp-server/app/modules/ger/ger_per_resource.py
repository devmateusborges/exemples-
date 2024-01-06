from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ger.ger_per_service import ger_per_service

from app.modules.ger.base.ger_serealizer import GerPerSchema
from app.modules.ger.base.ger_model import GerPer
from app.generics.generic_resource import generic_resource
from app.utils.funcs_util import funcs_util


routes_ger_per = Blueprint("gerper", __name__, url_prefix="/api/ger/gerper")


# ==============================


@routes_ger_per.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ger_per_service,
        model=GerPer,
        schema=GerPerSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ger_per.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ger_per_service,
        model=GerPer,
        schema=GerPerSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ger_per.route("/", methods=["POST"])
@jwt_required()
def save():

    return generic_resource.save(
        body=request.get_json(),
        service=ger_per_service,
        model=GerPer,
        schema=GerPerSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ger_per.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id, service=ger_per_service, model=GerPer, db_session=current_app.db.session
    )


# ==============================


@routes_ger_per.route("/generateper", methods=["POST"])
@jwt_required()
def generatePer():
    params = request.get_json()

    result = ger_per_service.generatePer(
        session=current_app.db.session,
        punitid=params["unit_id"],
        pgerpertipo=params["pgerpertipo"],
        pgerempresaid=params["pgerempresaid"],
        pano=params["pano"],
        psysuserid=params["psysuserid"],
        pcodeprocess=params["pcodeprocess"],
    )

    if result is not None:
        response = funcs_util.getResponseJson(result)
    else:
        response = funcs_util.getResponseJsonCode(data=None, code=400, msg="Not result")
    return response
