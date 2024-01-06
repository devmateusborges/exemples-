import app

from app.modules.fis.base.fis_model import (
    FisCertificado,
    FisCest,
    FisCestNcm,
    FisCfop,
    FisDoc,
    FisDocEvento,
    FisDocTipo,
    FisIbpt,
    FisNbs,
    FisNcm,
    FisObs,
    FisTributacao,
    FisTributo,
    FisUnitParam,
)
from app.generics.generic_schema import generic_schema
from marshmallow import EXCLUDE, fields
from app.generics.generic_schema_field import fields_Type_Obj_Sql
from app.utils.validator_util import valid_type_choice_sql


# ==========================================================


class FisCestSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisCest
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nr_cest = fields.Str(required=True)
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
    data_validade = fields.Str(required=True)

    fis_cest_ncm_childs = fields.Nested("FisCestNcmSchema", many=True)


# ==========================================================


class FisCfopSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisCfop
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nr_cfop = fields.Str(required=True)
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
    data_validade = fields.Str(required=True)


# ==========================================================


class FisDocTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisDocTipo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    modelo = fields.Str(required=True)
    nome = fields.Str(required=True)
    sigla_fis_doc_tipo = fields.Str(required=True)
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


class FisNbsSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisNbs
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nr_nbs = fields.Str(required=True)
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
    data_validade = fields.Str(required=True)


# ==========================================================


class FisNcmSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisNcm
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nr_ncm = fields.Str(required=True)
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
    data_validade = fields.Str(required=True)


# ==========================================================


class FisTributoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisTributo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nr_tributo = fields.Str(required=True)
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


# ==========================================================


class FisCertificadoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisCertificado
        sqla_session = app.db.session
        load_instance = True
        include_fk = True
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
    sys_document_childs = fields.Nested("SysDocumentSchema", many=True)
    senha = fields.Str(required=True)


# ==========================================================


class FisCestNcmSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisCestNcm
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    fis_ncm_id = fields.Str(required=True)
    fis_ncm_id_obj = fields.Nested("FisNcmSchema", dump_only=True)


# ==========================================================


class FisObsSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisObs
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


# ==========================================================


class FisUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)


# ==========================================================


class FisIbptSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisIbpt
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    data_validade_ini = fields.Str(required=True)
    data_validade_fin = fields.Str(required=True)
    perc_nacional = fields.Number(required=True)
    perc_importado = fields.Number(required=True)
    perc_municipal = fields.Number(required=True)

    fis_nbs_id = fields.Str(required=True)
    fis_nbs_id_obj = fields.Nested("FisNbsSchema", dump_only=True)

    fis_ncm_id = fields.Str(required=True)
    fis_ncm_id_obj = fields.Nested("FisNcmSchema", dump_only=True)

    ger_uf_id = fields.Str(required=True)
    ger_uf_id_obj = fields.Nested("GerUfSchema", dump_only=True)


# ==========================================================


class FisDocSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisDoc
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    data_emissao = fields.Str(required=True)
    chave = fields.Str(required=True)
    numero = fields.Str(required=True)
    serie = fields.Str(required=True)
    numero_ini = fields.Str(required=True)
    numero_fin = fields.Str(required=True)
    data_autorizado = fields.Str(required=True)
    data_cancelado = fields.Str(required=True)
    data_encerrado = fields.Str(required=True)
    xml_assinado = fields.Str(required=True)

    ambiente = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="fis_doc", field_name="ambiente", session=app.db.session
        ),
    )
    ambiente_obj = fields_Type_Obj_Sql(
        field_choice="ambiente",
        table_name="fis_doc",
        field_name="ambiente",
        session=app.db.session,
    )

    tipo_emissao = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="fis_doc", field_name="tipo_emissao", session=app.db.session
        ),
    )
    tipo_emissao_obj = fields_Type_Obj_Sql(
        field_choice="tipo_emissao",
        table_name="fis_doc",
        field_name="tipo_emissao",
        session=app.db.session,
    )

    status_sefaz = fields.Str(required=True)
    xml_protocolado = fields.Str(required=True)
    pdf_emitido = fields.Str(required=True)
    numero_pre = fields.Str(required=True)
    serie_pre = fields.Str(required=True)

    fis_doc_tipo_id = fields.Str(required=True)
    fis_doc_tipo_id_obj = fields.Nested("FisDocTipoSchema", dump_only=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)

    fis_doc_evento_childs = fields.Nested("FisDocEventoSchema", many=True)


# ==========================================================


class FisDocEventoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisDocEvento
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    xml_retorno = fields.Str(required=True)

    tipo_evento = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="fis_doce_vento",
            field_name="tipo_evento",
            session=app.db.session,
        ),
    )
    tipo_evento_obj = fields_Type_Obj_Sql(
        field_choice="tipo_evento",
        table_name="fis_doce_vento",
        field_name="tipo_evento",
        session=app.db.session,
    )

    nr_protocolo = fields.Str(required=True)
    qnt_evento = fields.Str(required=True)
    descricao_evento = fields.Str(required=True)
    pdf_retorno = fields.Str(required=True)


# ==========================================================


class FisTributacaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FisTributacao
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    cst = fields.Str(required=True)
    modalidade_base_calc = fields.Str(required=True)
    valor_base_calc = fields.Str(required=True)
    perc_aliquota = fields.Str(required=True)
    valor_imposto = fields.Str(required=True)
    valor_base_calc_isento = fields.Str(required=True)
    perc_aliquota_isento = fields.Str(required=True)
    valor_imposto_isento = fields.Str(required=True)
    valor_base_calc_st = fields.Str(required=True)
    margem_agregada_st = fields.Str(required=True)
    perc_aliquota_st = fields.Str(required=True)
    valor_imposto_st = fields.Str(required=True)
    perc_reducao_base_calc = fields.Str(required=True)
    observacao = fields.Str(required=True)
    valor_imposto_operacao = fields.Str(required=True)
    valor_imposto_diferido = fields.Str(required=True)
    perc_credito_sn = fields.Str(required=True)
    valor_credito_sn = fields.Str(required=True)
    valor_base_calc_fcp = fields.Str(required=True)
    perc_aliquota_fcp = fields.Str(required=True)
    valor_imposto_fcp = fields.Str(required=True)
    valor_base_calc_fcp_st = fields.Str(required=True)
    perc_aliquota_fcp_st = fields.Str(required=True)
    valor_imposto_fcp_st = fields.Str(required=True)
    perc_uf_fim_fcp = fields.Str(required=True)
    valor_total_uf_fim_fcp = fields.Str(required=True)
    valor_imposto_fcp_st_ret = fields.Str(required=True)
    valor_base_calc_fcp_st_ret = fields.Str(required=True)
    perc_aliquota_fcp_st_ret = fields.Str(required=True)
    valor_imposto_desonerado = fields.Str(required=True)
    motivo_imposto_desonerado = fields.Str(required=True)
    modalidade_base_calc_st = fields.Str(required=True)
    valor_base_calc_st_ret = fields.Str(required=True)
    valor_imposto_st_ret = fields.Str(required=True)
    perc_aliquota_red_base_calc_efetiva = fields.Str(required=True)
    valor_base_calc_efetiva = fields.Str(required=True)
    perc_aliquota_efetiva = fields.Str(required=True)
    valor_imposto_efetiva = fields.Str(required=True)
    perc_aliquota_credito = fields.Str(required=True)
    valor_imposto_credito = fields.Str(required=True)
    valor_base_calc_uf_fim = fields.Str(required=True)
    perc_interna_uf_fim = fields.Str(required=True)
    perc_interestadual_uf_fim = fields.Str(required=True)
    perc_partilha_uf_fim = fields.Str(required=True)
    valor_partilha_uf_fim = fields.Str(required=True)
    valor_partilha_uf_inicio = fields.Str(required=True)
    valor_imposto_substituto = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    fin_pagrec_id = fields.Str(required=True)
    fin_pagrec_id_obj = fields.Nested("FinPagrecSchema", dump_only=True)

    fis_tributo_id = fields.Str(required=True)
    fis_tributo_id_obj = fields.Nested("FisTributoSchema", dump_only=True)

    ger_pessoa_endereco_id = fields.Str(required=True)
    ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)

    mov_itemserv_id = fields.Str(required=True)
    mov_itemserv_id_obj = fields.Nested("MovItemservSchema", dump_only=True)


# ==========================================================
