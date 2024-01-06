from flask import Blueprint, current_app, request
from flask_jwt_extended import jwt_required

from app.modules.ger.ger_pessoa_endereco_service import ger_pessoa_endereco_service

from app.modules.ger.base.ger_serealizer import GerPessoaEnderecoSchema
from app.modules.ger.base.ger_model import GerPessoaEndereco
from app.generics.generic_resource import generic_resource


routes_ger_pessoa_endereco = Blueprint(
    "gerpessoaendereco", __name__, url_prefix="/api/ger/gerpessoaendereco"
)


# ==============================


@routes_ger_pessoa_endereco.route("/", methods=["GET"])
@jwt_required()
def find_all():
    return generic_resource.find_all(
        service=ger_pessoa_endereco_service,
        model=GerPessoaEndereco,
        schema=GerPessoaEnderecoSchema,
        db_session=current_app.db.session,
    )


# ==============================
@routes_ger_pessoa_endereco.route("/<id>", methods=["GET"])
@jwt_required()
def find_by_id(id):
    return generic_resource.find_by_id(
        id=id,
        service=ger_pessoa_endereco_service,
        model=GerPessoaEndereco,
        schema=GerPessoaEnderecoSchema,
        db_session=current_app.db.session,
    )


# ==============================


@routes_ger_pessoa_endereco.route("/", methods=["POST"])
@jwt_required()
def save():
    return generic_resource.save(
        body=request.get_json(),
        service=ger_pessoa_endereco_service,
        model=GerPessoaEndereco,
        schema=GerPessoaEnderecoSchema,
        db_session=current_app.db.session,
        unique_fields=None,
    )


# ==============================


@routes_ger_pessoa_endereco.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    return generic_resource.delete(
        id=id,
        service=ger_pessoa_endereco_service,
        model=GerPessoaEndereco,
        db_session=current_app.db.session,
    )
