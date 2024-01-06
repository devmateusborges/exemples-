from flask import Blueprint, current_app, request, jsonify
from flask_jwt_extended import jwt_required
import app
from app.generics.generic_service import generic_service

from app.modules.tst.test1_service import test1_service
from app.generics.generic_resource import generic_resource
from app.modules.tst.base.tst_serealizer import Test1Schema
from app.modules.tst.base.tst_model import Test1
from app.utils.cache_util import cache_util
from app.utils.email_util import email_util
from app.modules.sys.sys_document_service import sys_document_service

routes_test1 = Blueprint("test1", __name__, url_prefix="/api/tst/test1")

# ==============================


@routes_test1.route("/", methods=["GET"])
@app.cache.cached(make_cache_key=cache_util.make_key)
@jwt_required()
def find_all():

    # Criar cache_util com metodos get,set,clear_all, passando request como parametro se houver para buscar unit e url string para comport
    # cache_result = current_app.cache.get("xxx")
    # if cache_result is None:

    return generic_resource.find_all(
        service=test1_service,
        model=Test1,
        schema=Test1Schema,
        db_session=current_app.db.session,
        enabled_filter_fields=[
            "codigo",
            "descricao",
            "test1_fk_id_obj.codigo",
            "ativo",
        ],
    )


# ==============================


@routes_test1.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=test1_service,
        model=Test1,
        schema=Test1Schema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_test1.route("/", methods=["POST"])
@jwt_required()
def save():
    docuSrv = sys_document_service(generic_service)
    docuSrv.handle_delete_files(
        body=request.get_json(),
        docFieldName="sys_document_childs",
        parentPk="id",
        parentFieldName="test1_id",
        childsFieldName=[
            {
                "fieldName": "test1a_childs",
                "docFieldName": "foto_analizada",
                "fieldNameId": "test1a_child_id",
                "pk": "id",
            },
            {
                "fieldName": "test1_childs",
                "docFieldName": "sys_document_foto",
                "fieldNameId": "test1_child_id",
                "pk": "id",
            },
        ],
    )

    result = generic_resource.save(
        body=request.get_json(),
        service=test1_service,
        model=Test1,
        schema=Test1Schema,
        db_session=current_app.db.session,
        unique_fields=["codigo"],
        autoCommit=False,
    )

    docuSrv.handle_save_files(
        body=request.get_json(),
        docFieldName="sys_document_childs",
        docChildsFieldName=[
            {"fieldName": "test1a_childs", "docFieldName": "foto_analizada"},
            {"fieldName": "test1_childs", "docFieldName": "sys_document_foto"},
        ],
    )

    current_app.db.session.commit()
    resultJson = Test1Schema().jsonify(result), 201
    current_app.db.session.close()

    return resultJson


# ==============================
@routes_test1.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id, service=test1_service, model=Test1, db_session=current_app.db.session
    )


# ==============================


@routes_test1.route("/sendemailtemplate", methods=["POST"])
@jwt_required()
def send_email():
    srv = email_util()

    template_data = {"text_to": "Eduardo", "text_body": "Este é email de teste"}

    result = srv.send_mail_template(
        "junqueiraeduardo@gmail.com",
        "admin@admin.com.br",
        "test send email",
        "generic_email",
        template_data,
    )
    return jsonify(result)


# ==============================


@routes_test1.route("/test1createtask", methods=["POST"])
@jwt_required()
def test1_create_task():
    body = request.get_json()
    srv = test1_service(Test1, schema=Test1Schema, unique_fields=[])
    result = srv.test1_create_task(body)
    return jsonify(result), 200
