from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.cms.cms_post_hist_service import cms_post_hist_service

from app.modules.cms.base.cms_serealizer import CmsPostHistSchema
from app.modules.cms.base.cms_model import CmsPostHist
from app.generics.generic_resource import generic_resource


routes_cms_post_hist = Blueprint(
    "cmsposthist", __name__, url_prefix="/api/cms/cmsposthist"
)


# ==============================


@routes_cms_post_hist.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        cms_post_hist_service, CmsPostHist, CmsPostHistSchema, current_app.db.session
    )


# ==============================
@routes_cms_post_hist.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id,
        cms_post_hist_service,
        CmsPostHist,
        CmsPostHistSchema,
        current_app.db.session,
    )


# ==============================


@routes_cms_post_hist.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=cms_post_hist_service,
        model=CmsPostHist,
        schema=CmsPostHistSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_cms_post_hist.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id, cms_post_hist_service, CmsPostHist, current_app.db.session
    )
