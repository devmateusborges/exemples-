import os
from flask import Blueprint, current_app, request, jsonify, send_from_directory, session
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.modules.test.test1_service import test1_service

from app.modules.test.base.test_serealizer import Test1Schema
from app.modules.test.base.test_model import Test1
from app.utils.email_util import email_util
UPLOAD_FOLDER = "C:\\RF\\Desenv\\exemplos-back\\flask-marshmallow\\app\\modules\\sys\\upload"

routes_test1 = Blueprint('test', __name__,url_prefix="/api/test")

 
@routes_test1.route('/', methods=['GET'])
@jwt_required()
def find_all():
    srv = test1_service(Test1)
    result = srv.find_all()
    return  Test1Schema(many=True).jsonify(result), 200


@routes_test1.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    srv = test1_service(Test1)
    result = srv.delete(id)
    return jsonify(result), 204

@routes_test1.route('/', methods=['POST'])
@jwt_required()
def save():
    srv = test1_service(Test1)    
    
    try:
        obj = Test1Schema().load(request.get_json())
    except ValidationError as err:
        return jsonify( err.messages), 400

    result = srv.save(obj)        

    return Test1Schema().jsonify(result), 201


@routes_test1.route('/sendemailtemplate', methods=['POST'])
@jwt_required()
def send_email():
    srv = email_util()

    template_data = {"text_to":"Eduardo",
                    "text_body":"Este é email de teste",
                    "website_brand":"RESULTFACIL | Simples e Objetivo",
                    "website_url":"www.resultfacil.com.br"}
    
    result = srv.send_mail_template("junqueiraeduardo@gmail.com","admin@admin.com.br","test send email","generic_email",template_data)
    return  jsonify(result)

#==========================================================


@routes_test1.route("/arquivos", methods=["GET"])
def lista_arquivos():
    arquivos = []

    for nome_do_arquivo in os.listdir(UPLOAD_FOLDER):
        endereco_do_arquivo = os.path.join(UPLOAD_FOLDER, nome_do_arquivo)

        if(os.path.isfile(endereco_do_arquivo)):
            arquivos.append(nome_do_arquivo)

    return jsonify(arquivos)


@routes_test1.route("/arquivos/<nome_do_arquivo>",  methods=["GET"])
def get_arquivo(nome_do_arquivo):
    return send_from_directory(UPLOAD_FOLDER, nome_do_arquivo, as_attachment=True)


@routes_test1.route("/arquivos", methods=["POST"])
def post_arquivo():
    arquivo = request.files.get("meuArquivo")

    print(arquivo)
    nome_do_arquivo = arquivo.filename
    arquivo.save(os.path.join(UPLOAD_FOLDER, nome_do_arquivo))

    return '', 201