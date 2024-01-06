import app
from app.modules.fin.base.fin_model import (
    FinBanco,
    FinClass,
    FinClassAgrup,
    FinClassAgrupGrupo,
    FinClassGrupo,
    FinCondPagrec,
    FinCondPagrecConfig,
    FinConta,
    FinDocTipo,
    FinLote,
    FinPagrec,
    FinPagrecBaixa,
    FinPagrecBaixaVar,
    FinPagrecBanco,
    FinPagrecBancoExtrato,
    FinPagrecBancoTransf,
    FinPagrecClass,
    FinPagrecOrigem,
    FinPagrecParc,
    FinPagrecParcVar,
    FinPagrecPrev,
    FinPagrecPrevDest,
    FinPagrecPrevVar,
    FinPagrecTipo,
    FinPagrecVersao,
    FinRecibo,
    FinReciboTipo,
    FinTipoVariacao,
    FinUnitParam,
)

from app.generics.generic_schema import generic_schema
from marshmallow import EXCLUDE, fields
from app.generics.generic_schema_field import fields_Type_Obj_Sql
from app.utils.validator_util import valid_type_choice_sql


# ==========================================================


class FinReciboSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinRecibo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_recibo = fields.Str(required=True)
    conteudo = fields.Str(required=True)
    valor = fields.Number(required=True)
    ger_pessoa_endereco_id = fields.Str(required=False)
    nome_pessoa = fields.Str(required=True)
    nr_doc_pessoa = fields.Str(required=True)
    tipo_doc_pessoa = fields.Str(required=True)
    status = fields.Str(
        validate=valid_type_choice_sql(
            table_name="fin_recibo", field_name="status", session=app.db.session
        ),
    )
    status_obj = fields_Type_Obj_Sql(
        field_choice="status",
        table_name="fin_recibo",
        field_name="status",
        session=app.db.session,
    )
    status_observacao = fields.Str(required=True)


# ==========================================================


class FinBancoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinBanco
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
    nr_banco = fields.Str(required=True)


# ==========================================================


class FinClassSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinClass
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

    tipo_es = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="fin_class", field_name="tipo_es", session=app.db.session
        ),
    )
    tipo_es_obj = fields_Type_Obj_Sql(
        field_choice="tipo_es",
        table_name="fin_class",
        field_name="tipo_es",
        session=app.db.session,
    )

    tipo_fluxo = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="fin_class", field_name="tipo_fluxo", session=app.db.session
        ),
    )
    tipo_fluxo_obj = fields_Type_Obj_Sql(
        field_choice="tipo_fluxo",
        table_name="fin_class",
        field_name="tipo_fluxo",
        session=app.db.session,
    )

    fixo_variavel = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="fin_class", field_name="fixo_variavel", session=app.db.session
        ),
    )
    fixo_variavel_obj = fields_Type_Obj_Sql(
        field_choice="fixo_variavel",
        table_name="fin_class",
        field_name="fixo_variavel",
        session=app.db.session,
    )

    sigla_class = fields.Str(required=True)

    tipo_prev = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    tipo_prev_obj = fields_Type_Obj_Sql(
        field_choice="tipo_prev",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )


# ==========================================================


class FinClassAgrupSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinClassAgrup
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
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

    fin_class_agrup_grupo_childs = fields.Nested("FinClassAgrupGrupoSchema", many=True)


# ==========================================================


class FinClassGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinClassGrupo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    estrutura = fields.Str(required=True)
    sigla_class_grupo = fields.Str(required=True)

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


class FinCondPagrecSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinCondPagrec
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    sigla_cond_pagamento = fields.Str(required=True)
    qnt_dia_ini = fields.Integer(required=True)
    observacao = fields.Str(required=True)

    considera_feriado = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    considera_feriado_obj = fields_Type_Obj_Sql(
        field_choice="considera_feriado",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    considera_final_sem = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    considera_final_sem_obj = fields_Type_Obj_Sql(
        field_choice="considera_final_sem",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    tipo_prazo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    tipo_prazo_obj = fields_Type_Obj_Sql(
        field_choice="tipo_prazo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

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


class FinPagrecTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecTipo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    sigla_fin_pagrec_tipo = fields.Str(required=True)

    aceita_entrada = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aceita_entrada_obj = fields_Type_Obj_Sql(
        field_choice="aceita_entrada",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    aceita_saida = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aceita_saida_obj = fields_Type_Obj_Sql(
        field_choice="aceita_saida",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

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

    gla_fin_pagrec_tipo = app.db.Column(app.db.String(100))


# ==========================================================


class FinPagrecVersaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecVersao
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)

    sigla_versao = fields.Str(required=True)
    data_per_ini = fields.Str(required=True)
    data_per_fin = fields.Str(required=True)

    versao_atual = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    versao_atual_obj = fields_Type_Obj_Sql(
        field_choice="versao_atual",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    tipo_per = fields.Str(
        load_default="M",
        validate=valid_type_choice_sql(
            table_name="fin_pagrec_versao",
            field_name="tipo_per",
            session=app.db.session,
        ),
    )
    tipo_per_obj = fields_Type_Obj_Sql(
        field_choice="tipo_per",
        table_name="fin_pagrec_versao",
        field_name="tipo_per",
        session=app.db.session,
    )

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


class FinReciboTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinReciboTipo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
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
    sigla_fin_recibo_tipo = fields.Str(required=True)

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


class FinTipoVariacaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinTipoVariacao
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    tipo = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="fin_tipo_variacao", field_name="tipo", session=app.db.session
        ),
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="fin_tipo_variacao",
        field_name="tipo",
        session=app.db.session,
    )

    valor_positivo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    valor_positivo_obj = fields_Type_Obj_Sql(
        field_choice="valor_positivo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    sigla_fin_tipo_variacao = fields.Str(required=True)

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


class FinUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)


# ==========================================================


class FinClassAgrupGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinClassAgrupGrupo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    fin_class_id = fields.Str(required=True)
    fin_class_id_obj = fields.Nested("FinClassSchema")

    fin_class_grupo_id = fields.Str(required=True)
    fin_class_grupo_id_obj = fields.Nested("FinClassGrupoSchema")


# ==========================================================


class FinCondPagrecConfigSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinCondPagrecConfig
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    qnt_dia = fields.Str(required=True)

    fin_cond_pag_rec_id = fields.Str(required=True)
    fin_cond_pag_rec_id_obj = fields.Nested("FinCondPagrecSchema")


# ==========================================================


class FinDocTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinDocTipo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    sigla_fin_doc_tipo = fields.Str(required=True)

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

    ger_numeracao_id = fields.Str(required=True)
    ger_numeracao_id_obj = fields.Nested("GerNumeracaoSchema")


# ==========================================================


class FinContaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinConta
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    nr_agencia = fields.Str(required=True)
    nr_conta = fields.Str(required=True)

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

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema")

    fin_banco_id = fields.Str(required=True)
    fin_banco_id_obj = fields.Nested("FinBancoSchema")


# ==========================================================


class FinLoteSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinLote
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    data_lote = fields.Str(required=True)
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
    sigla_fin_lote = fields.Str(required=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema")


# ==========================================================


class FinPagrecSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrec
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    numero_doc_pagrec = fields.Str(required=True)
    observacao = fields.Str(required=True)
    data_mov = fields.Str(required=True)
    valor_pagrec = fields.Str(required=True)
    numero_parc_total = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    tipo_es = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="fin_pagrec", field_name="tipo_es", session=app.db.session
        ),
    )
    tipo_es_obj = fields_Type_Obj_Sql(
        field_choice="tipo_es",
        table_name="fin_pagrec",
        field_name="tipo_es",
        session=app.db.session,
    )

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema")

    fin_cond_pagrec_id = fields.Str(required=True)
    fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema")

    fin_pagrec_tipo_id = fields.Str(required=True)
    fin_pagrec_tipo_id_obj = fields.Nested("FinPagrecTipoSchema")

    ger_pessoa_id = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema")

    ger_pessoa_id_pagrec = fields.Str(required=True)
    ger_pessoa_id_pagrec_obj = fields.Nested("GerPessoaSchema")

    ope_centro_rat_tipo_id = fields.Str(required=True)
    ope_centro_rat_tipo_id_obj = fields.Nested("OpeCentroRatTipoSchema")

    fin_doc_tipo_id = fields.Str(required=True)
    fin_doc_tipo_id_obj = fields.Nested("FinDocTipoSchema")

    process_id = fields.Str(required=True)
    process_id_obj = fields.Nested("SysProcessLogSchema")

    fin_pagrec_parc_childs = fields.Nested("FinPagrecParcSchema", many=True)


# ==========================================================


class FinPagrecPrevSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecPrev
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_per = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema")

    fin_class_id = fields.Str(required=True)
    fin_class_id_obj = fields.Nested("FinClassSchema")

    ger_pessoa_id = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema")

    fin_pagrec_versao_id = fields.Str(required=True)
    fin_pagrec_versao_id_obj = fields.Nested("FinPagrecVersaoSchema")

    process_id = fields.Str(required=True)
    process_id_obj = fields.Nested("SysProcessLogSchema")

    tipo_es = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="fin_pagrec_prev", field_name="tipo_es", session=app.db.session
        ),
    )
    tipo_es_obj = fields_Type_Obj_Sql(
        field_choice="tipo_es",
        table_name="fin_pagrec_prev",
        field_name="tipo_es",
        session=app.db.session,
    )

    valor01 = fields.Str(required=True)
    valor02 = fields.Str(required=True)
    valor03 = fields.Str(required=True)
    valor04 = fields.Str(required=True)
    valor05 = fields.Str(required=True)
    valor06 = fields.Str(required=True)
    valor07 = fields.Str(required=True)
    valor08 = fields.Str(required=True)
    valor09 = fields.Str(required=True)
    valor10 = fields.Str(required=True)
    valor11 = fields.Str(required=True)
    valor12 = fields.Str(required=True)
    valor13 = fields.Str(required=True)
    valor14 = fields.Str(required=True)
    valor15 = fields.Str(required=True)
    valor16 = fields.Str(required=True)
    valor17 = fields.Str(required=True)
    valor18 = fields.Str(required=True)
    valor19 = fields.Str(required=True)
    valor20 = fields.Str(required=True)
    valor21 = fields.Str(required=True)
    valor22 = fields.Str(required=True)
    valor23 = fields.Str(required=True)
    valor24 = fields.Str(required=True)
    valor25 = fields.Str(required=True)
    valor26 = fields.Str(required=True)
    valor27 = fields.Str(required=True)
    valor28 = fields.Str(required=True)
    valor29 = fields.Str(required=True)
    valor30 = fields.Str(required=True)
    valor31 = fields.Str(required=True)

    fin_pagrec_prev_var_childs = fields.Nested("FinPagrecPrevVarSchema", many=True)

    fin_pagrec_prev_dest_childs = fields.Nested("FinPagrecPrevDestSchema", many=True)


# ==========================================================


class FinPagrecBancoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecBanco
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_mov = fields.Str(required=True)
    numero_doc_pagrec = fields.Str(required=True)
    valor = fields.Str(required=True)
    observacao = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    fin_conta_id = fields.Str(required=True)
    fin_conta_id_obj = fields.Nested("FinContaSchema")

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema")


# ==========================================================


class FinPagrecPrevDestSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecPrevDest
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    ope_centro1_id_dest_pri = fields.Str(required=True)
    ope_centro1_id_obj = fields.Nested("OpeCentro1Schema")

    ope_centro1_id_dest_sec = fields.Str(required=True)
    ope_centro1_id_obj = fields.Nested("OpeCentro1Schema")

    ope_centro2_id_dest_sec = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema")

    ope_centro2_id_dest_pri = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema")

    ope_atividade_id = fields.Str(required=True)
    ope_atividade_id_obj = fields.Nested("OpeAtividadeSchema")

    valor01 = fields.Str(required=True)
    valor02 = fields.Str(required=True)
    valor03 = fields.Str(required=True)
    valor04 = fields.Str(required=True)
    valor05 = fields.Str(required=True)
    valor06 = fields.Str(required=True)
    valor07 = fields.Str(required=True)
    valor08 = fields.Str(required=True)
    valor09 = fields.Str(required=True)
    valor10 = fields.Str(required=True)
    valor11 = fields.Str(required=True)
    valor12 = fields.Str(required=True)
    valor13 = fields.Str(required=True)
    valor14 = fields.Str(required=True)
    valor15 = fields.Str(required=True)
    valor16 = fields.Str(required=True)
    valor17 = fields.Str(required=True)
    valor18 = fields.Str(required=True)
    valor19 = fields.Str(required=True)
    valor20 = fields.Str(required=True)
    valor21 = fields.Str(required=True)
    valor22 = fields.Str(required=True)
    valor23 = fields.Str(required=True)
    valor24 = fields.Str(required=True)
    valor25 = fields.Str(required=True)
    valor26 = fields.Str(required=True)
    valor27 = fields.Str(required=True)
    valor28 = fields.Str(required=True)
    valor29 = fields.Str(required=True)
    valor30 = fields.Str(required=True)
    valor31 = fields.Str(required=True)


# ==========================================================
class FinPagrecBancoExtratoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecBancoExtrato
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_extrato = fields.Str(required=True)
    numero_doc = fields.Str(required=True)
    descricao = fields.Str(required=True)
    valor = fields.Str(required=True)
    status_observacao = fields.Str(required=True)

    status = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="fin_pagrec_banco_extrato",
            field_name="status",
            session=app.db.session,
        ),
    )
    status_obj = fields_Type_Obj_Sql(
        field_choice="status",
        table_name="fin_pagrec_banco_extrato",
        field_name="status",
        session=app.db.session,
    )

    fin_conta_id = fields.Str(required=True)
    fin_conta_id_obj = fields.Nested("FinContaSchema")

    process_id = fields.Str(required=True)
    process_id_obj = fields.Nested("SysProcessLogSchema")


# ==========================================================


class FinPagrecParcSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecParc
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    numero_parc = fields.Str(required=True)
    valor_pagrec = fields.Str(required=True)
    valor_juro = fields.Str(required=True)
    valor_desconto = fields.Str(required=True)
    valor_multa = fields.Str(required=True)
    data_venc = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    fin_doc_tipo_id = fields.Str(required=True)
    fin_doc_tipo_id_obj = fields.Nested("FinDocTipoSchema")

    fin_pagrec_parc_var_childs = fields.Nested("FinPagrecParcVarSchema", many=True)


# ==========================================================


class FinPagrecPrevVarSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecPrevVar
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    fin_tipo_variacao_id = fields.Str(required=True)
    fin_tipo_variacao_id_obj = fields.Nested("FinTipoVariacaoSchema")

    valor01 = fields.Str(required=True)
    valor02 = fields.Str(required=True)
    valor03 = fields.Str(required=True)
    valor04 = fields.Str(required=True)
    valor05 = fields.Str(required=True)
    valor06 = fields.Str(required=True)
    valor07 = fields.Str(required=True)
    valor08 = fields.Str(required=True)
    valor09 = fields.Str(required=True)
    valor10 = fields.Str(required=True)
    valor11 = fields.Str(required=True)
    valor12 = fields.Str(required=True)
    valor13 = fields.Str(required=True)
    valor14 = fields.Str(required=True)
    valor15 = fields.Str(required=True)
    valor16 = fields.Str(required=True)
    valor17 = fields.Str(required=True)
    valor18 = fields.Str(required=True)
    valor19 = fields.Str(required=True)
    valor20 = fields.Str(required=True)
    valor21 = fields.Str(required=True)
    valor22 = fields.Str(required=True)
    valor23 = fields.Str(required=True)
    valor24 = fields.Str(required=True)
    valor25 = fields.Str(required=True)
    valor26 = fields.Str(required=True)
    valor27 = fields.Str(required=True)
    valor28 = fields.Str(required=True)
    valor29 = fields.Str(required=True)
    valor30 = fields.Str(required=True)
    valor31 = fields.Str(required=True)


# ==========================================================


class FinPagrecBaixaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecBaixa
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    numero_doc_pagrec = fields.Str(required=True)
    valor_pagrec = fields.Str(required=True)
    data_baixa = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    tipo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="fin_pagrec_baixa", field_name="tipo", session=app.db.session
        ),
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="fin_pagrec_baixa",
        field_name="tipo",
        session=app.db.session,
    )

    fin_conta_id = fields.Str(required=True)
    fin_conta_id_obj = fields.Nested("FinContaSchema")

    fin_doc_tipo_id = fields.Str(required=True)
    fin_doc_tipo_id_obj = fields.Nested("FinDocTipoSchema")

    fin_lote_id = fields.Str(required=True)
    fin_lote_id_obj = fields.Nested("FinLoteSchema")

    fin_pagrec_parc_id = fields.Str(required=True)
    fin_pagrec_parc_id_obj = fields.Nested("FinPagrecParcSchema")

    fin_pagrec_baixa_var_childs = fields.Nested("FinPagrecBaixaVarSchema", many=True)


# ==========================================================


class FinPagrecClassSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecClass
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    valor = fields.Str(required=True)
    fator_rat = fields.Str(required=True)
    perc_rat = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    fin_class_id = fields.Str(required=True)
    fin_class_id_obj = fields.Nested("FinClassSchema")

    fin_pagrec_banco_id = fields.Str(required=True)
    fin_pagrec_banco_id_obj = fields.Nested("FinPagrecBancoSchema")

    fin_pagrec_id = fields.Str(required=True)
    fin_pagrec_id_obj = fields.Nested("FinPagrecSchema")


# ==========================================================


class FinPagrecParcVarSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecParcVar
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    valor = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    fin_tipo_variacao_id = fields.Str(required=True)
    fin_tipo_variacao_id_obj = fields.Nested("FinTipoVariacaoSchema")


# ==========================================================


class FinPagrecBaixaVarSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecBaixaVar
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    valor = fields.Str(required=True)
    observacao = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    fin_tipo_variacao_id = fields.Str(required=True)
    fin_tipo_variacao_id_obj = fields.Nested("FinTipoVariacaoSchema")


# ==========================================================


class FinPagrecBancoTransfSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecBancoTransf
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_mov = fields.Str(required=True)
    valor = fields.Str(required=True)
    observacao = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    fin_conta_id_origem = fields.Str(required=True)
    fin_conta_id_origem_obj = fields.Nested("FinContaSchema")

    fin_conta_id_destino = fields.Str(required=True)
    fin_conta_id_destino_obj = fields.Nested("FinContaSchema")

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema")

    process_id = fields.Str(required=True)
    process_id_obj = fields.Nested("SysProcessLogSchema")


# ==========================================================


class FinPagrecOrigemSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = FinPagrecOrigem
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    tipo = fields.Str(required=True)

    fin_pagrec_id = fields.Str(required=True)
    fin_pagrec_id_obj = fields.Nested("FinPagrecSchema")

    fin_pagrec_id_origem = fields.Str(required=True)
    fin_pagrec_id_origem_obj = fields.Nested("FinPagrecSchema")

    fin_pagrec_parc_id = fields.Str(required=True)
    fin_pagrec_parc_id_obj = fields.Nested("FinPagrecParcSchema")

    fin_pagrec_parc1_id_origem = fields.Str(required=True)
    fin_pagrec_parc1_id_origem_obj = fields.Nested("FinPagrecParcSchema")

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema")

    fin_pagrec_baixa_id = fields.Str(required=True)
    fin_pagrec_baixa_id_obj = fields.Nested("FinPagrecBaixaSchema")

    fin_extrato_id = fields.Str(required=True)
    fin_extrato_id_obj = fields.Nested("FinPagrecBancoExtratoSchema")

    fin_recibo_id = fields.Str(required=True)
    fin_recibo_id_obj = fields.Nested("FinReciboSchema")

    fin_pagrec_banco_id = fields.Str(required=True)
    fin_pagrec_banco_id_id_obj = fields.Nested("FinPagrecBancoSchema")


# ==========================================================
