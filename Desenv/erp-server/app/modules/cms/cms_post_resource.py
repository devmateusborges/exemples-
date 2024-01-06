from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required
import app
from app.modules.cms.cms_post_service import cms_post_service
from app.modules.sys.sys_document_service import sys_document_service
from app.generics.generic_service import generic_service

from app.modules.cms.base.cms_serealizer import CmsPostSchema
from app.modules.cms.base.cms_model import CmsPost
from app.generics.generic_resource import generic_resource
from app.utils.cache_util import cache_util


routes_cms_post = Blueprint("cmspost", __name__, url_prefix="/api/cms/cmspost")


# ==============================


@routes_cms_post.route("/", methods=["GET"])
# TODO @jwt_required()
@app.cache.cached(make_cache_key=cache_util.make_key)
def find_all():
    return generic_resource.find_all(
        service=cms_post_service,
        model=CmsPost,
        schema=CmsPostSchema,
        db_session=current_app.db.session,
        enabled_filter_fields=["titulo", "corpo"],
    )


# ==============================
@routes_cms_post.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=cms_post_service,
        model=CmsPost,
        schema=CmsPostSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_cms_post.route("/", methods=["POST"])
@jwt_required()
def save():
    docuSrv = sys_document_service(generic_service)
    docuSrv.handle_delete_files(
        body=request.get_json(),
        docFieldName="img_url",
        parentPk="id",
        parentFieldName="img_url_id",
        childsFieldName=[],
    )

    result = generic_resource.save(
        body=request.get_json(),
        service=cms_post_service,
        model=CmsPost,
        schema=CmsPostSchema,
        db_session=current_app.db.session,
        autoCommit=False,
    )

    docuSrv.handle_save_files(
        body=request.get_json(),
        docFieldName="img_url",
        docChildsFieldName=[],
    )

    current_app.db.session.commit()
    resultJson = CmsPostSchema().jsonify(result), 201
    current_app.db.session.close()

    return resultJson


# ==============================


@routes_cms_post.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id, cms_post_service, CmsPost, current_app.db.session
    )
