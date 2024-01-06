from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required


from app.exceptions.ApiException import ApiException
from app.modules.sys.sys_document_service import sys_document_service

from app.modules.sys.base.sys_serealizer import SysDocumentSchema
from app.modules.sys.base.sys_model import SysDocument
from app.generics.generic_resource import generic_resource


routes_sys_document = Blueprint(
    "sysdocument", __name__, url_prefix="/api/sys/sysdocument"
)


# ==============================


@routes_sys_document.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=sys_document_service,
        model=SysDocument,
        schema=SysDocumentSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_sys_document.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=sys_document_service,
        model=SysDocument,
        schema=SysDocumentSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_document.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=sys_document_service,
        model=SysDocument,
        schema=SysDocumentSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_sys_document.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=sys_document_service,
        model=SysDocument,
        db_session=current_app.db.session,
    )


# ==============================


@routes_sys_document.route("/upload/<id>", methods=["POST"])
@jwt_required()
def post_file(id):
    srv = sys_document_service(SysDocument)

    data = request.get_json()

    if data.get("filename") is None:
        raise ApiException(
            message={"filename": "File name required"}, name="VALIDATION_ERROR"
        )

    if data.get("file_64") is None:
        raise ApiException(
            message={"file_64": "File 64 required"}, name="VALIDATION_ERROR"
        )

    if data.get("file_content_type") is None:
        raise ApiException(
            message={"file_content_type": "File ContentType required"},
            name="VALIDATION_ERROR",
        )

    # todo storage_type
    result = srv.uploadfile(
        id, data.get("file_64"), data.get("filename"), data.get("file_content_type"), 1
    )
    current_app.db.session.commit()
    current_app.db.session.close()
    return jsonify(result), 201


# ==============================
@routes_sys_document.route("/download/<id>", methods=["GET"])
# @jwt_required() TODO analisar autenticação
def get_file(id):

    srv = sys_document_service(SysDocument)

    return srv.download(id, 1)


# ==============================
@routes_sys_document.route("/downloadopen/<path:filename>", methods=["GET"])
def get_file_open(filename):
    srv = sys_document_service(SysDocument)

    return srv.download_open(filename)
