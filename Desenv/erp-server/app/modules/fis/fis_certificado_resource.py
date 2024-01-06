from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.fis.fis_certificado_service import fis_certificado_service
from app.generics.generic_service import generic_service
from app.modules.sys.sys_document_service import sys_document_service
from app.modules.fis.base.fis_serealizer import FisCertificadoSchema
from app.modules.fis.base.fis_model import FisCertificado
from app.generics.generic_resource import generic_resource


routes_fis_certificado = Blueprint(
    "fiscertificado", __name__, url_prefix="/api/fis/fiscertificado"
)


# ==============================


@routes_fis_certificado.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=fis_certificado_service,
        model=FisCertificado,
        schema=FisCertificadoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_fis_certificado.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=fis_certificado_service,
        model=FisCertificado,
        schema=FisCertificadoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_fis_certificado.route("/", methods=["POST"])
@jwt_required()
def save():
    docuSrv = sys_document_service(generic_service)
    docuSrv.handle_delete_files(
        body=request.get_json(),
        docFieldName="sys_document_childs",
        parentPk="id",
        parentFieldName="fis_certificado_id",
        childsFieldName=[],
    )

    result = generic_resource.save(
        body=request.get_json(),
        service=fis_certificado_service,
        model=FisCertificado,
        schema=FisCertificadoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
        autoCommit=False,
    )

    docuSrv.handle_save_files(
        body=request.get_json(),
        docFieldName="sys_document_childs",
        docChildsFieldName=[],
    )

    current_app.db.session.commit()
    resultJson = FisCertificadoSchema().jsonify(result), 201
    current_app.db.session.close()

    return resultJson


# ==============================


@routes_fis_certificado.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=fis_certificado_service,
        model=FisCertificado,
        db_session=current_app.db.session,
    )
