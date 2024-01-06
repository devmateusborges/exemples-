from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required
from app.modules.ind.ind_dash_service import ind_dash_service
from app.utils.decoratos_util import unit_required
from app.utils.funcs_util import funcs_util

from app.utils.resource_util import resource_util


routes_ind_dash = Blueprint("inddash", __name__, url_prefix="/api/ind/inddash")


# ==============================


@routes_ind_dash.route("/getindics", methods=["GET"])
@jwt_required()
@unit_required()
def get_indics():
    req_param = resource_util.req_param_default()

    srv = ind_dash_service()
    result = srv.get_indics(
        session=current_app.db.session,
        punitid=request.headers.get("x-unitid"),
        pfilters=req_param["pfilters"],
    )

    response = funcs_util.getResponseJsonList(result)

    current_app.db.session.close()
    return response


# ==============================


@routes_ind_dash.route("/getpers", methods=["GET"])
@jwt_required()
@unit_required()
def get_pers():
    req_param = resource_util.req_param_default()

    srv = ind_dash_service()
    result = srv.get_pers(
        session=current_app.db.session,
        punitid=request.headers.get("x-unitid"),
        pfilters=req_param["pfilters"],
    )

    response = funcs_util.getResponseJsonList(result)

    current_app.db.session.close()
    return response


# ==============================


@routes_ind_dash.route("/getgruposubgrupo", methods=["GET"])
@jwt_required()
@unit_required()
def get_grupo_subgrupo():
    req_param = resource_util.req_param_default()

    srv = ind_dash_service()
    result = srv.get_grupo_subgrupo(
        session=current_app.db.session,
        punitid=request.headers.get("x-unitid"),
        pfilters=req_param["pfilters"],
    )

    response = funcs_util.getResponseJsonList(result)

    current_app.db.session.close()
    return response


# ==============================


@routes_ind_dash.route("/getvalores", methods=["GET"])
@jwt_required()
@unit_required()
def get_valores():
    req_param = resource_util.req_param_default()

    srv = ind_dash_service()
    result = srv.get_valores(
        session=current_app.db.session,
        punitid=request.headers.get("x-unitid"),
        pfilters=req_param["pfilters"],
    )

    response = funcs_util.getResponseJsonList(result)

    current_app.db.session.close()
    return response
