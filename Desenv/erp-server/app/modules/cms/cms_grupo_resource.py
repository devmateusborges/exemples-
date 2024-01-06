from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.cms.cms_grupo_service import cms_grupo_service

from app.modules.cms.base.cms_serealizer import CmsGrupoSchema
from app.modules.cms.base.cms_model import CmsGrupo
from app.generics.generic_resource import generic_resource


routes_cms_grupo = Blueprint("cmsgrupo", __name__, url_prefix="/api/cms/cmsgrupo")


# ==============================


@routes_cms_grupo.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=cms_grupo_service,
        model=CmsGrupo,
        schema=CmsGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_cms_grupo.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=cms_grupo_service,
        model=CmsGrupo,
        schema=CmsGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_cms_grupo.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=cms_grupo_service,
        model=CmsGrupo,
        schema=CmsGrupoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_cms_grupo.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=cms_grupo_service,
        model=CmsGrupo,
        db_session=current_app.db.session,
    )
