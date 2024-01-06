# ====================================================================================
# Code Owner ..: EDUARDO JUNQUEIRA - ME - CNPJ: 12.138.668/0001-89
# Create_at ...: 25/10/2022
# History Update
# 30/09/2022 - EJ - Ajuste metodos retirando padrao deixando apenas customizados.
# ====================================================================================

from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required
from app.generics.generic_resource import generic_resource
from app.modules.sys.base.sys_model import SysUserPreference

from app.modules.sys.sys_user_preference_service import sys_user_preference_service

from app.modules.sys.base.sys_serealizer import SysUserPreferenceSchema
from app.utils.funcs_util import funcs_util


routes_sys_user_preference = Blueprint(
    "sysuserpreference", __name__, url_prefix="/api/sys/sysuserpreference"
)


# ==============================


@routes_sys_user_preference.route("/", methods=["GET"])
@jwt_required()
def list():
    srv = sys_user_preference_service(SysUserPreference, SysUserPreferenceSchema)

    filters = {
        "filter": {
            "and": {
                "object_id": request.args.get("pobjectid", ""),
                "object_sub_id": request.args.get("pobjectsubid", ""),
                "sys_user_id": request.args.get("psysuserid", ""),
                "object_type": request.args.get("pobjecttype", ""),
            }
        }
    }
    result = srv.find_all(
        page=1,
        per_page=100,
        filters=filters,
        enabled_filter_fields=[
            "object_id",
            "object_sub_id",
            "sys_user_id",
            "object_type",
        ],
    )

    response = funcs_util.getResponseJson(result)
    current_app.db.session.close()
    return response


# ==============================


@routes_sys_user_preference.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_user_preference_service,
        model=SysUserPreference,
        schema=SysUserPreferenceSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_user_preference.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id,
        service=sys_user_preference_service,
        model=SysUserPreference,
        db_session=current_app.db.session,
    )
