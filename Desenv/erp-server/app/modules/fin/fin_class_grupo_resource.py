from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fin.fin_class_grupo_service import fin_class_grupo_service

from app.modules.fin.base.fin_serealizer import FinClassGrupoSchema
from app.modules.fin.base.fin_model import FinClassGrupo
from app.generics.generic_resource import generic_resource


routes_fin_class_grupo = Blueprint(
    "finclassgrupo", __name__, url_prefix="/api/fin/finclassgrupo"
)


# ==============================


@routes_fin_class_grupo.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fin_class_grupo_service,
        model=FinClassGrupo,
        schema=FinClassGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fin_class_grupo.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fin_class_grupo_service,
        model=FinClassGrupo,
        schema=FinClassGrupoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fin_class_grupo.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=fin_class_grupo_service,
        model=FinClassGrupo,
        schema=FinClassGrupoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_fin_class_grupo.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fin_class_grupo_service,
        model=FinClassGrupo,
        db_session=current_app.db.session,
    )
