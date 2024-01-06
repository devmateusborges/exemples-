import app
from app.modules.ger.base.ger_model import (
    GerCidade,
    GerDevice,
    GerDeviceParam,
    GerEmpresa,
    GerEmpresaGrupo,
    GerEmpresaPessoa,
    GerEstNivel,
    GerIndex,
    GerIndexMov,
    GerItemserv,
    GerItemservBarra,
    GerItemservCompos,
    GerItemservComposTipo,
    GerItemservGrupo,
    GerItemservLocal,
    GerItemservLote,
    GerItemservPessoa,
    GerItemservSubGrupo,
    GerItemservVar,
    GerMarca,
    GerMarcaModelo,
    GerMarcaPessoa,
    GerNumeracao,
    GerPais,
    GerPer,
    GerPerTipo,
    GerPessoa,
    GerPessoaContaBanco,
    GerPessoaEndereco,
    GerProcessoBloq,
    GerProcessoBloqUser,
    GerUf,
    GerUmedida,
    GerUmedidaConv,
    GerUnitParam,
)

from app.generics.generic_schema import generic_schema
from marshmallow import EXCLUDE, fields
from app.generics.generic_schema_field import fields_Type_Obj_Sql
from app.utils.validator_util import valid_type_choice_sql


# ==========================================================


class GerMarcaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerMarca
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    sigla_ger_marca = fields.Str(required=True)

    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    ger_marca_modelo_childs = fields.Nested("GerMarcaModeloSchema", many=True)
    ger_marca_pessoa_childs = fields.Nested("GerMarcaPessoaSchema", many=True)


# ==========================================================


class GerItemservComposTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerItemservComposTipo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    sigla_ger_itemserv_compos_tipo = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )


# ==========================================================


class GerPaisSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerPais
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    nr_pais = fields.Str(required=True)
    sigla_pais = fields.Str(required=True)

    ger_uf_childs = fields.Nested("GerUfSchema", many=True)


# ==========================================================


class GerUmedidaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerUmedida
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    sigla_umedida = fields.Str(required=True)

    ger_umedida_conv_childs = fields.Nested("GerUmedidaConvSchema", many=True)


# ==========================================================


class GerUfSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerUf
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    nr_uf = fields.Str(required=True)
    sigla_uf = fields.Str(required=True)

    ger_pais_id = fields.Str(required=False, allow_none=True)


# ==========================================================


class GerCidadeSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerCidade
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    nr_cidade = fields.Str(required=True)

    ger_uf_id = fields.Str(required=True)
    ger_uf_id_obj = fields.Nested("GerUfSchema", dump_only=True)


# ==========================================================


class GerDeviceParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerDeviceParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    sigla_param = fields.Str(required=True)
    valor_tx = fields.Str(required=True)
    valor_dt = fields.Str(required=True)
    valor_nm = fields.Number(required=True)
    observacao = fields.Str(required=True)


# ==========================================================


class GerIndexMovSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerIndexMov
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_mov = fields.Str(required=True)
    valor1 = fields.Str(required=True)
    valor2 = fields.Str(required=True)

    ger_index_id = fields.Str(required=True)
    ger_index_id_obj = fields.Nested("GerIndexSchema", dump_only=True)


# ==========================================================


class GerItemservSubGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerItemservSubGrupo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ctb_comp_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    sigla_ger_itemserv_subgrupo = fields.Str(required=True)

    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    ger_itemserv_grupo_id = fields.Str(required=False, allow_none=True)


# ==========================================================


class GerItemservVarSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerItemservVar
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    sigla_itemserv_var = fields.Str(required=True)

    ope_ciclo_var_id = fields.Str(required=True)
    ope_ciclo_var_id_obj = fields.Nested("OpeCicloVarSchema", dump_only=True)


# ==========================================================


class GerMarcaPessoaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerMarcaPessoa
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    observacao = fields.Str(required=True)

    ger_pessoa_id = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)


# ==========================================================


class GerPessoaContaBancoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerPessoaContaBanco
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    agencia = fields.Str(required=True)
    conta = fields.Str(required=True)
    observacao = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    fin_banco_id = fields.Str(required=True)
    fin_banco_id_obj = fields.Nested("FinBancoSchema", dump_only=True)


# ==========================================================


class GerEmpresaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerEmpresa
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    razao_social = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    sigla_empresa = fields.Str(required=True)
    doc_cnpj = fields.Str(required=True)
    doc_cpf = fields.Str(required=True)
    doc_ie = fields.Str(required=True)
    doc_im = fields.Str(required=True)
    doc_cnae = fields.Str(required=True)
    data_abertura = fields.Str(required=True)
    doc_junta = fields.Str(required=True)

    fis_regime = fields.Str(
        load_default=None,
        validate=valid_type_choice_sql(
            table_name="ger_empresa", field_name="fis_regime", session=app.db.session
        ),
    )
    fis_regime_obj = fields_Type_Obj_Sql(
        load_default=None,
        field_choice="fis_regime",
        table_name="ger_empresa",
        field_name="fis_regime",
        session=app.db.session,
    )

    data_validade_a3 = fields.Str(required=True)
    data_validade_a1 = fields.Str(required=True)
    end_logradouro = fields.Str(required=True)
    end_logradouro_nr = fields.Str(required=True)
    end_bairro = fields.Str(required=True)
    end_complemento = fields.Str(required=True)
    end_cep = fields.Str(required=True)
    fone_1 = fields.Str(required=True)
    fone_2 = fields.Str(required=True)
    fone_3 = fields.Str(required=True)
    contato_1 = fields.Str(required=True)
    contato_2 = fields.Str(required=True)
    contato_3 = fields.Str(required=True)
    email_1 = fields.Str(required=True)
    doc_rntrc = fields.Str(required=True)
    fis_dfe_ambiente = fields.Str(required=True)
    fis_dfe_api_token = fields.Str(required=True)

    fis_regime_trib_nfs = fields.Str(
        load_default=None,
        validate=valid_type_choice_sql(
            table_name="ger_empresa",
            field_name="fis_regime_trib_nfs",
            session=app.db.session,
        ),
    )
    fis_regime_trib_nfs_obj = fields_Type_Obj_Sql(
        field_choice="fis_regime_trib_nfs",
        table_name="ger_empresa",
        field_name="fis_regime_trib_nfs",
        session=app.db.session,
    )

    fis_provedor_nfs = fields.Str(
        load_default=None,
        validate=valid_type_choice_sql(
            table_name="ger_empresa",
            field_name="fis_provedor_nfs",
            session=app.db.session,
        ),
    )
    fis_provedor_nfs_obj = fields_Type_Obj_Sql(
        field_choice="fis_provedor_nfs",
        table_name="ger_empresa",
        field_name="fis_provedor_nfs",
        session=app.db.session,
    )

    fis_incent_cultura = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    fis_incent_cultura_obj = fields_Type_Obj_Sql(
        field_choice="fis_incent_cultura",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    fis_incent_fiscal_nfs = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    fis_incent_fiscal_nfs_obj = fields_Type_Obj_Sql(
        field_choice="fis_incent_fiscal_nfs",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    end_ger_cidade_id = fields.Str(required=True)
    end_ger_cidade_id_obj = fields.Nested("GerCidadeSchema", dump_only=True)

    fis_certificado_id = fields.Str(required=True)
    fis_certificado_id_obj = fields.Nested("FisCertificadoSchema", dump_only=True)

    ger_empresa_grupo_id = fields.Str(required=True)
    ger_empresa_grupo_id_obj = fields.Nested("GerEmpresaGrupoSchema", dump_only=True)

    ger_per_tipo_id = fields.Str(required=True)
    ger_per_tipo_id_obj = fields.Nested("GerPerTipoSchema", dump_only=True)

    ger_empresa_pessoa_childs = fields.Nested("GerEmpresaPessoaSchema", many=True)


# ==========================================================


class GerItemservSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerItemserv
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    referencia1 = fields.Str(required=True)
    referencia2 = fields.Str(required=True)
    referencia3 = fields.Str(required=True)

    tipo = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ger_itemserv", field_name="tipo", session=app.db.session
        ),
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="ger_itemserv",
        field_name="tipo",
        session=app.db.session,
    )

    tipo_ctb_comp = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ger_itemserv",
            field_name="tipo_ctb_comp",
            session=app.db.session,
        ),
    )
    tipo_ctb_comp_obj = fields_Type_Obj_Sql(
        field_choice="tipo_ctb_comp",
        table_name="ger_itemserv",
        field_name="tipo_ctb_comp",
        session=app.db.session,
    )

    origem_fiscal = fields.Number(required=True)
    fis_doc_cnae_nfs = fields.Str(required=True)
    fis_sigla_servico_municipio = fields.Str(required=True)
    sigla_itemserv = fields.Str(required=True)
    nome_alternativo = fields.Str(required=True)

    tipo_composicao = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ger_itemserv",
            field_name="tipo_composicao",
            session=app.db.session,
        ),
    )
    tipo_composicao_obj = fields_Type_Obj_Sql(
        field_choice="tipo_composicao",
        table_name="ger_itemserv",
        field_name="tipo_composicao",
        session=app.db.session,
    )

    fis_sigla_servico = fields.Str(required=True)

    ger_itemserv_subgrupo_id = fields.Str(required=True)
    ger_itemserv_subgrupo_id_obj = fields.Nested(
        "GerItemservSubGrupoSchema", dump_only=True
    )

    fis_ncm_id = fields.Str(required=True)
    fis_ncm_id_obj = fields.Nested("FisNcmSchema", dump_only=True)

    ger_umedida_id = fields.Str(required=True)
    ger_umedida_id_obj = fields.Nested("GerUmedidaSchema", dump_only=True)

    fis_cest_id = fields.Str(required=True)
    fis_cest_id_obj = fields.Nested("FisCestSchema", dump_only=True)

    fis_nbs_id = fields.Str(required=True)
    fis_nbs_id_obj = fields.Nested("FisNbsSchema", dump_only=True)

    ctb_comp_id = fields.Str(required=True)
    ctb_comp_id_obj = fields.Nested("CtbCompSchema", dump_only=True)

    ger_itemserv_barra_childs = fields.Nested("GerItemservBarraSchema", many=True)

    ger_itemserv_local_childs = fields.Nested("GerItemservLocalSchema", many=True)

    ger_itemserv_lote_childs = fields.Nested("GerItemservLoteSchema", many=True)

    ger_itemserv_pessoa_childs = fields.Nested("GerItemservPessoaSchema", many=True)


# ==========================================================


class GerPessoaEnderecoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerPessoaEndereco
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    tipo = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ger_pessoa_endereco", field_name="tipo", session=app.db.session
        ),
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="ger_pessoa_endereco",
        field_name="tipo",
        session=app.db.session,
    )

    padrao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    padrao_obj = fields_Type_Obj_Sql(
        field_choice="padrao",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    end_logradouro = fields.Str(required=True)
    end_logradouro_nr = fields.Str(required=True)
    end_bairro = fields.Str(required=True)
    end_complemento = fields.Str(required=True)
    end_cep = fields.Str(required=True)
    fone = fields.Str(required=True)
    email = fields.Str(required=True)
    contato = fields.Str(required=True)
    end_ger_cidade_id = fields.Str(required=True)
    end_ger_cidade_id_obj = fields.Nested("GerCidadeSchema", dump_only=True)


# ==========================================================


class GerDeviceSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerDevice
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    sigla_device = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    ger_device_param_childs = fields.Nested("GerDeviceParamSchema", many=True)


# ==========================================================


class GerEmpresaGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerEmpresaGrupo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    sigla_ger_empresa_grupo = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )


# ==========================================================


class GerEstNivelSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerEstNivel
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    observacao = fields.Str(required=True)
    bloq_mov_solic = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    bloq_mov_solic_obj = fields_Type_Obj_Sql(
        field_choice="bloq_mov_solic",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    bloq_mov_pedido = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    bloq_mov_pedido_obj = fields_Type_Obj_Sql(
        field_choice="bloq_mov_pedido",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    sigla_ger_est_nivel = fields.Str(required=True)


# ==========================================================


class GerIndexSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerIndex
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    sigla_index = fields.Str(required=True)


# ==========================================================


class GerItemservGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerItemservGrupo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    sigla_ger_itemserv_grupo = fields.Str(required=True)

    ger_itemserv_subgrupo_childs = fields.Nested("GerItemservSubGrupoSchema", many=True)


# ==========================================================


class GerItemservLoteSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerItemservLote
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    data_ini = fields.Str(required=True)
    data_fin = fields.Str(required=True)
    observacao = fields.Str(required=True)
    data_validade = fields.Str(required=True)
    sigla_ger_itemserv_lote = fields.Str(required=True)


# ==========================================================


class GerMarcaModeloSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerMarcaModelo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    sigla_ger_marca_modelo = fields.Str(required=True)


# ==========================================================


class GerNumeracaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerNumeracao
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    serie = fields.Str(required=True)
    ultimo_nr = fields.Integer(required=True)
    sigla_ger_numeracao = fields.Str(required=True)


# ==========================================================


class GerPerSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerPer
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_dia_inicial = fields.Str(required=True)
    dia_nome = fields.Str(required=True)
    data_semana_inicial = fields.Str(required=True)
    semana_nome = fields.Str(required=True)
    data_quinzena_inicial = fields.Str(required=True)
    quinzena_nome = fields.Str(required=True)
    data_mes_inicial = fields.Str(required=True)
    mes_nome = fields.Str(required=True)
    data_bimestre_inicial = fields.Str(required=True)
    bimestre_nome = fields.Str(required=True)
    data_trimestre_inicial = fields.Str(required=True)
    trimestre_nome = fields.Str(required=True)
    data_quadrimestre_inicial = fields.Str(required=True)
    quadrimestre_nome = fields.Str(required=True)
    data_semestre_inicial = fields.Str(required=True)
    semestre_nome = fields.Str(required=True)
    data_ano_inicial = fields.Str(required=True)
    ano_nome = fields.Str(required=True)
    ger_per_tipo_id = fields.Str(required=True)
    ger_per_tipo_id_obj = fields.Nested("GerPerTipoSchema", dump_only=True)
    sys_process_log_id = fields.Str(required=True)
    sys_process_log_id_obj = fields.Nested("SysProcessLogSchema", dump_only=True)

    data_dia_final = fields.Str(required=True)
    data_quinzena_final = fields.Str(required=True)
    data_semana_final = fields.Str(required=True)
    data_mes_final = fields.Str(required=True)
    data_bimestre_final = fields.Str(required=True)
    data_trimestre_final = fields.Str(required=True)
    data_quadrimestre_final = fields.Str(required=True)
    data_semestre_final = fields.Str(required=True)
    data_ano_final = fields.Str(required=True)

    dia_numero = fields.Str(required=True)
    quinzena_numero = fields.Str(required=True)
    semana_numero = fields.Str(required=True)
    mes_numero = fields.Str(required=True)
    bimestre_numero = fields.Str(required=True)
    trimestre_numero = fields.Str(required=True)
    quadrimestre_numero = fields.Str(required=True)
    semestre_numero = fields.Str(required=True)
    ano_numero = fields.Str(required=True)

    dia_tipo = fields.Str(required=True)
    quinzena_tipo = fields.Str(required=True)
    semana_tipo = fields.Str(required=True)
    mes_tipo = fields.Str(required=True)
    bimestre_tipo = fields.Str(required=True)
    trimestre_tipo = fields.Str(required=True)
    quadrimestre_tipo = fields.Str(required=True)
    semestre_tipo = fields.Str(required=True)
    ano_tipo = fields.Str(required=True)


# ==========================================================


class GerPessoaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerPessoa
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    razao_social = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    doc_cnpj = fields.Str(required=True)
    doc_cpf = fields.Str(required=True)
    doc_ie = fields.Str(required=True)
    doc_im = fields.Str(required=True)
    doc_cnae = fields.Str(required=True)
    data_abertura = fields.Str(required=True)
    doc_junta = fields.Str(required=True)
    fis_regime = fields.Str(required=True)
    fone_1 = fields.Str(required=True)
    fone_2 = fields.Str(required=True)
    fone_3 = fields.Str(required=True)
    contato_1 = fields.Str(required=True)
    contato_2 = fields.Str(required=True)
    contato_3 = fields.Str(required=True)
    contrib_icms = fields.Integer(required=False)
    nr_rntrc = fields.Str(required=True)
    doc_rg = fields.Str(required=True)
    doc_rg_org_exp = fields.Str(required=True)
    doc_crc_seq = fields.Str(required=True)
    doc_crc = fields.Str(required=True)
    doc_crc_org_exp = fields.Str(required=True)
    sigla_pes = fields.Str(required=True)
    nr_registro_est_cte = fields.Str(required=True)
    doc_taf = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    ger_pessoa_conta_banco_childs = fields.Nested(
        "GerPessoaContaBancoSchema", many=True
    )

    ger_pessoa_endereco_childs = fields.Nested("GerPessoaEnderecoSchema", many=True)


# ==========================================================


class GerUmedidaConvSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerUmedidaConv
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    fator_mult = fields.Number(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    ger_umedida_id_para = fields.Str(required=True)
    ger_umedida_id_para_obj = fields.Nested("GerUmedidaSchema", dump_only=True)


# ==========================================================


class GerUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)


# ==========================================================


class GerEmpresaPessoaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerEmpresaPessoa
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    tipo = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ger_empresa_pessoa", field_name="tipo", session=app.db.session
        ),
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="ger_empresa_pessoa",
        field_name="tipo",
        session=app.db.session,
    )

    observacao = fields.Str(required=True)

    ger_pessoa_id = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)


# ==========================================================


class GerItemservBarraSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerItemservBarra
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    codigo_barra = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )


# ==========================================================


class GerItemservComposSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerItemservCompos
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    fator_mult = fields.Str(required=True)
    qnt_compos = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    observacao = fields.Str(required=True)
    ordem = fields.Str(required=True)
    qnt_altura = fields.Str(required=True)
    qnt_largura = fields.Str(required=True)
    qnt_comprimento = fields.Str(required=True)

    ger_itemserv_compos_tipo_id = fields.Str(required=True)
    ger_itemserv_compos_tipo_id_obj = fields.Nested(
        "GerItemservComposTipoSchema", dump_only=True
    )

    ger_itemserv_id_de = fields.Str(required=True)
    ger_itemserv_id_de_obj = fields.Nested("GerItemservSchema", dump_only=True)

    ger_itemserv_id_para = fields.Str(required=True)
    ger_itemserv_id_para_obj = fields.Nested("GerItemservSchema", dump_only=True)


# ===========================================================


class GerItemservLocalSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerItemservLocal
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    desc_local1 = fields.Str(required=True)
    desc_local2 = fields.Str(required=True)
    desc_local3 = fields.Str(required=True)
    observacao = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )


# ===========================================================


class GerItemservPessoaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerItemservPessoa
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    cod_itemserv_ext = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    ger_pessoa_id = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)


# ===========================================================


class GerProcessoBloqSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerProcessoBloq
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    tipo_processo = fields.Str(required=True)
    data_lib_inicial = fields.Str(required=True)
    data_lib_final = fields.Str(required=True)
    observacao = fields.Str(required=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)

    ger_processo_bloq_user_childs = fields.Nested(
        "GerProcessoBloqUserSchema", many=True
    )


# ==========================================================


class GerProcessoBloqUserSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerProcessoBloqUser
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    tipo_bloq = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ger_processo_bloq_user",
            field_name="tipo_bloq",
            session=app.db.session,
        ),
    )
    tipo_bloq_obj = fields_Type_Obj_Sql(
        field_choice="tipo_bloq",
        table_name="ger_processo_bloq_user",
        field_name="tipo_bloq",
        session=app.db.session,
    )

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)


# ==========================================================


class GerPerTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = GerPerTipo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    ativo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ativo_obj = fields_Type_Obj_Sql(
        field_choice="ativo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    sigla_per_tipo = fields.Str(required=True)
    ini_semana = fields.Str(required=True)


# ==========================================================
