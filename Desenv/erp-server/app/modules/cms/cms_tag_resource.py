from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.cms.cms_tag_service import cms_tag_service

from app.modules.cms.base.cms_serealizer import CmsTagSchema
from app.modules.cms.base.cms_model import CmsTag
from app.generics.generic_resource import generic_resource


routes_cms_tag = Blueprint("cmstag", __name__, url_prefix="/api/cms/cmstag")


# ==============================


@routes_cms_tag.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        cms_tag_service, CmsTag, CmsTagSchema, current_app.db.session
    )


# ==============================
@routes_cms_tag.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id, cms_tag_service, CmsTag, CmsTagSchema, current_app.db.session
    )


# ==============================


@routes_cms_tag.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=cms_tag_service,
        model=CmsTag,
        schema=CmsTagSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_cms_tag.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(id, cms_tag_service, CmsTag, current_app.db.session)
