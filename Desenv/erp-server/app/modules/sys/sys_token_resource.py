from flask import Blueprint, current_app, request
from app.modules.sys.sys_token_service import sys_token_service
from app.utils.funcs_util import funcs_util
from flask_jwt_extended import jwt_required

routes_sys_token = Blueprint("systoken", __name__, url_prefix="/api/sys/systoken")


# ==============================
@routes_sys_token.route("/gettoken/", methods=["GET"])
@jwt_required()
def get_token():
    req_param_token = request.args.get("token", default="", type=str)
    srv = sys_token_service()
    result = srv.get_token(session=current_app.db.session, token=req_param_token)
    resultAux = {"token": result.token, "data_token": result.data_token}
    current_app.db.session.commit()
    current_app.db.session.close()
    return funcs_util.getResponseJsonCode(
        code=200,
        msg="Token valid",
        data=resultAux,
    )


# ==============================
@routes_sys_token.route("/generatetoken/", methods=["POST"])
@jwt_required()
def generate_token():
    params = request.get_json()
    srv = sys_token_service()
    result = srv.generate_token(
        session=current_app.db.session,
        hours=params["hours"],
        data_token=params["data_token"],
    )
    current_app.db.session.commit()
    current_app.db.session.close()
    return funcs_util.getResponseJsonCode(code=200, msg="Token valid", data=result)
