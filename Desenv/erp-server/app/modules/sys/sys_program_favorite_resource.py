# ====================================================================================
# Code Owner ..: EDUARDO JUNQUEIRA - ME - CNPJ: 12.138.668/0001-89
# Create_at ...: 01/01/2021
# History Update
# 30/09/2022 - EJ - Ajuste metodos retirando padrao deixando apenas customizados.
# ====================================================================================

from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.sys.sys_program_favorite_service import sys_program_favorite_service

from app.utils.funcs_util import funcs_util
from app.utils.resource_util import resource_util

routes_sys_program_favorite = Blueprint(
    "sysprogramfavorite", __name__, url_prefix="/api/sys/sysprogramfavorite"
)


# ==============================
@routes_sys_program_favorite.route("/getbyuserlogin/", methods=["GET"])
@jwt_required()
def get_by_user_login():
    req_param = resource_util.req_param_default()
    srv = sys_program_favorite_service()
    result = srv.get_by_user_login(
        session=current_app.db.session, pfilters=req_param["pfilters"]
    )

    print(req_param["pfilters"])

    response = funcs_util.getResponseJsonList(result)

    current_app.db.session.close()
    return response


# ==============================
@routes_sys_program_favorite.route("/favorite/", methods=["POST"])
@jwt_required()
def favorite():

    srv = sys_program_favorite_service()
    result = srv.favotite(
        session=current_app.db.session,
        obj=request.get_json(),
    )

    response = funcs_util.getResponseJson(result)
    current_app.db.session.commit()
    return response
