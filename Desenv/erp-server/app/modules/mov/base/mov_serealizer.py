import app

from app.generics.generic_schema import generic_schema
from marshmallow import EXCLUDE, fields
from app.generics.generic_schema_field import fields_Type_Obj_Sql


from app.modules.mov.base.mov_model import (
    Mov,
    MovCiot,
    MovComp,
    MovCondutor,
    MovCotacao,
    MovCotacaoAnal,
    MovEntrega,
    MovEntregaDoc,
    MovEstNivel,
    MovFrete,
    MovItemserv,
    MovLacre,
    MovMedida,
    MovOperacao,
    MovOperacaoStatus,
    MovOrigem,
    MovPedagio,
    MovPercurso,
    MovReboque,
    MovSeguradora,
    MovStatus,
    MovTipo,
    MovTomador,
    MovUnitParam,
)

from app.utils.validator_util import valid_type_choice_sql


# ======================================== ==================


class MovTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovTipo
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
    sigla_mov_tipo = fields.Str(required=True)
    tipo_mov = fields.Str(required=True)
    configuracao = fields.Str(required=True)


# ==========================================================


class MovStatusSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovStatus
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
    sigla_mov_status = fields.Str(required=True)

    tipo_status = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="mov_status", field_name="tipo_status", session=app.db.session
        ),
    )
    tipo_status_obj = fields_Type_Obj_Sql(
        field_choice="tipo_status",
        table_name="mov_status",
        field_name="tipo_status",
        session=app.db.session,
    )


# ==========================================================


class MovUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)


# ==========================================================


class MovOperacaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovOperacao
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
    sigla_mov_operacao = fields.Str(required=True)
    configuracao = fields.Str(required=True)

    finalidade_doc = fields.Str(
        validate=valid_type_choice_sql(
            table_name="mov_operacao",
            field_name="finalidade_doc",
            session=app.db.session,
        )
    )
    finalidade_doc_obj = fields_Type_Obj_Sql(
        field_choice="finalidade_doc",
        table_name="mov_operacao",
        field_name="finalidade_doc",
        session=app.db.session,
    )

    tipo_es = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="mov_operacao", field_name="tipo_es", session=app.db.session
        ),
    )
    tipo_es_obj = fields_Type_Obj_Sql(
        field_choice="tipo_es",
        table_name="mov_operacao",
        field_name="tipo_es",
        session=app.db.session,
    )

    ger_numeracao_id = fields.Str(required=True)
    ger_numeracao_id_obj = fields.Nested("GerNumeracaoSchema", dump_only=True)

    mov_tipo_id = fields.Str(required=True)
    mov_tipo_id_obj = fields.Nested("MovTipoSchema", dump_only=True)

    mov_operacao_status_childs = fields.Nested("MovOperacaoStatusSchema", many=True)


# ==========================================================


class MovOperacaoStatusSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovOperacaoStatus
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    mov_operacao_id_prox = fields.Str(required=False, allow_none=True)
    mov_operacao_id_prox_obj = fields.Nested("MovOperacaoSchema", dump_only=True)

    mov_status_id = fields.Str(required=True)
    mov_status_id_obj = fields.Nested("MovStatusSchema", dump_only=True)

    mov_status_id_prox = fields.Str(required=True)
    mov_status_id_prox_obj = fields.Nested("MovStatusSchema", dump_only=True)


# ==========================================================


class MovSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = Mov
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nr_externo = fields.Str(required=True)
    data_mov = fields.Str(required=True)
    numero_mov = fields.Str(required=True)
    data_emissao = fields.Str(required=True)
    serie_mov = fields.Str(required=True)
    valor_total = fields.Str(required=True)
    observacao = fields.Str(required=True)

    tipo_frete = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="mov", field_name="tipo_frete", session=app.db.session
        ),
    )
    tipo_frete_obj = fields_Type_Obj_Sql(
        field_choice="tipo_frete",
        table_name="mov",
        field_name="tipo_frete",
        session=app.db.session,
    )

    tipo_emissao_carga = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="mov", field_name="tipo_emissao_carga", session=app.db.session
        ),
    )
    tipo_emissao_carga_obj = fields_Type_Obj_Sql(
        field_choice="tipo_emissao_carga",
        table_name="mov",
        field_name="tipo_emissao_carga",
        session=app.db.session,
    )

    data_entrega = fields.Str(required=True)
    data_entrada_saida = fields.Str(required=True)

    tipo_modal_carga = fields.Str(required=True)
    tipo_transportador_carga = fields.Str(required=True)
    valor_carga = fields.Str(required=True)

    tipo_umedida_carga = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="mov", field_name="tipo_umedida_carga", session=app.db.session
        ),
    )
    tipo_umedida_carga_obj = fields_Type_Obj_Sql(
        field_choice="tipo_umedida_carga",
        table_name="mov",
        field_name="tipo_umedida_carga",
        session=app.db.session,
    )

    qnt_carga = fields.Str(required=True)
    observacao_transp = fields.Str(required=True)
    observacao_serv = fields.Str(required=True)
    tipo_fretamento = fields.Str(required=True)
    tipo_serv_frete = fields.Str(required=True)
    tipo_tomador_serv_frete = fields.Str(required=True)
    taf = fields.Str(required=True)
    data_anulacao = fields.Str(required=True)
    observacao_item = fields.Str(required=True)
    valor_financeiro_total = fields.Str(required=True)
    valor_item_frete_total = fields.Str(required=True)
    observacao_fiscal = fields.Str(required=True)

    fis_tipo_resp_reten = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="mov", field_name="fis_tipo_resp_reten", session=app.db.session
        ),
    )
    fis_tipo_resp_reten_obj = fields_Type_Obj_Sql(
        field_choice="fis_tipo_resp_reten",
        table_name="mov",
        field_name="fis_tipo_resp_reten",
        session=app.db.session,
    )

    fis_exig_iss_nfs = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="mov", field_name="fis_exig_iss_nfs", session=app.db.session
        ),
    )
    fis_exig_iss_nfs_obj = fields_Type_Obj_Sql(
        field_choice="fis_exig_iss_nfs",
        table_name="mov",
        field_name="fis_exig_iss_nfs",
        session=app.db.session,
    )

    fis_iss_retido_nfs = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="mov", field_name="fis_iss_retido_nfs", session=app.db.session
        ),
    )
    fis_iss_retido_nfs_obj = fields_Type_Obj_Sql(
        field_choice="fis_iss_retido_nfs",
        table_name="mov",
        field_name="fis_iss_retido_nfs",
        session=app.db.session,
    )

    fis_nat_ope_nfs = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="mov", field_name="fis_nat_ope_nfs", session=app.db.session
        ),
    )
    fis_nat_ope_nfs_obj = fields_Type_Obj_Sql(
        field_choice="fis_nat_ope_nfs",
        table_name="mov",
        field_name="fis_nat_ope_nfs",
        session=app.db.session,
    )

    numero_mov_pre = fields.Str(required=True)
    serio_mov_pre = fields.Str(required=True)
    cep_carreg = fields.Str(required=True)
    cep_descarreg = fields.Str(required=True)

    tipo_carga = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="mov", field_name="tipo_carga", session=app.db.session
        ),
    )
    tipo_carga_obj = fields_Type_Obj_Sql(
        field_choice="tipo_carga",
        table_name="mov",
        field_name="tipo_carga",
        session=app.db.session,
    )

    data_valid = fields.Str(required=True)

    fin_cond_pagrec_id = fields.Str(required=True)
    fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    fis_doc_tipo_id = fields.Str(required=True)
    fis_doc_tipo_id_obj = fields.Nested("FisDocTipoSchema", dump_only=True)

    ger_cidade_id_carreg = fields.Str(required=True)
    ger_cidade_id_carreg_obj = fields.Nested("GerCidadeSchema", dump_only=True)

    ger_cidade_id_descarreg = fields.Str(required=True)
    ger_cidade_id_descarreg_obj = fields.Nested("GerCidadeSchema", dump_only=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)

    ger_pessoa_endereco_id_dest = fields.Str(required=True)
    ger_pessoa_endereco_id_dest_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ger_pessoa_endereco_id_entrega = fields.Str(required=True)
    ger_pessoa_endereco_id_entrega_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ger_pessoa_endereco_id_expe = fields.Str(required=True)
    ger_pessoa_endereco_id_expe_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ger_pessoa_endereco_id_fiscal = fields.Str(required=True)
    ger_pessoa_endereco_id_fiscal_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ger_pessoa_endereco_id_inter = fields.Str(required=True)
    ger_pessoa_endereco_id_inter_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ger_pessoa_endereco_id_rece = fields.Str(required=True)
    ger_pessoa_endereco_id_rece_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ger_pessoa_endereco_id_reme = fields.Str(required=True)
    ger_pessoa_endereco_id_reme_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ger_pessoa_id = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    mov_operacao_id = fields.Str(required=True)
    mov_operacao_id_obj = fields.Nested("MovOperacaoSchema", dump_only=True)

    mov_status_id = fields.Str(required=True)
    mov_status_id_obj = fields.Nested("MovStatusSchema", dump_only=True)

    sys_user_id_resp = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)


# ==========================================================


class MovEstNivelSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovEstNivel
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    qnt_min = fields.Str(required=True)
    qnt_max = fields.Str(required=True)
    qnt_nesc = fields.Str(required=True)
    observacao = fields.Str(required=True)

    ger_est_nivel_id = fields.Str(required=True)
    ger_est_nivel_id_obj = fields.Nested("GerEstNivelSchema", dump_only=True)

    ger_itemserv_id = fields.Str(required=True)
    ger_itemserv_id_obj = fields.Nested("GerItemservSchema", dump_only=True)


# ==========================================================


class MovCiotSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovCiot
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nr_ciot = fields.Str(required=True)

    ger_pessoa_id_responsavel = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)


# ==========================================================


class MovCompSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovComp
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome_comp = fields.Str(required=True)
    qnt_comp = fields.Str(required=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)


# ==========================================================


class MovCondutorSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovCondutor
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    ger_pessoa_id_condutor = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)


# ==========================================================


class MovCotacaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovCotacao
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    observacao1 = fields.Str(required=True)
    observacao2 = fields.Str(required=True)
    qnt_cot = fields.Str(required=True)
    valor_unit_cot = fields.Str(required=True)
    valor_total_cot = fields.Str(required=True)
    valor_desc_cot = fields.Str(required=True)
    valor_frete_cot = fields.Str(required=True)
    valor_outro_cot = fields.Str(required=True)
    valor_total_trib_cot = fields.Str(required=True)

    status = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="mov_cotacao", field_name="status", session=app.db.session
        ),
    )
    status_obj = fields_Type_Obj_Sql(
        field_choice="status",
        table_name="mov_cotacao",
        field_name="status",
        session=app.db.session,
    )

    data_status = fields.Str(required=True)

    fin_cond_pagrec_id = fields.Str(required=True)
    fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    ger_itemserv_id = fields.Str(required=True)
    ger_itemserv_id_obj = fields.Nested("GerItemservSchema", dump_only=True)

    ger_pessoa_endereco_id = fields.Str(required=True)
    ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ger_pessoa_id = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)

    sys_user_id_aprov = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)


# ==========================================================


class MovCotacaoAnalSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovCotacaoAnal
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    c01_observacao1 = fields.Str(required=True)
    c01_observacao2 = fields.Str(required=True)
    c01_qnt_cot = fields.Str(required=True)
    c01_valor_unit_cot = fields.Str(required=True)
    c01_valor_total_cot = fields.Str(required=True)
    c01_valor_desc_cot = fields.Str(required=True)
    c01_valor_frete_cot = fields.Str(required=True)
    c01_valor_outro_cot = fields.Str(required=True)
    c01_valor_total_trib_cot = fields.Str(required=True)
    c01_status = fields.Str(required=True)
    c01_data_status = fields.Str(required=True)
    c02_observacao1 = fields.Str(required=True)
    c02_observacao2 = fields.Str(required=True)
    c02_qnt_cot = fields.Str(required=True)
    c02_valor_unit_cot = fields.Str(required=True)
    c02_valor_total_cot = fields.Str(required=True)
    c02_valor_desc_cot = fields.Str(required=True)
    c02_valor_frete_cot = fields.Str(required=True)
    c02_valor_outro_cot = fields.Str(required=True)
    c02_valor_total_trib_cot = fields.Str(required=True)
    c02_status = fields.Str(required=True)
    c02_data_status = fields.Str(required=True)
    c03_observacao1 = fields.Str(required=True)
    c03_observacao2 = fields.Str(required=True)
    c03_qnt_cot = fields.Str(required=True)
    c03_valor_unit_cot = fields.Str(required=True)
    c03_valor_total_cot = fields.Str(required=True)
    c03_valor_desc_cot = fields.Str(required=True)
    c03_valor_frete_cot = fields.Str(required=True)
    c03_valor_outro_cot = fields.Str(required=True)
    c03_valor_total_trib_cot = fields.Str(required=True)
    c03_status = fields.Str(required=True)
    c03_data_status = fields.Str(required=True)
    c04_observacao1 = fields.Str(required=True)
    c04_observacao2 = fields.Str(required=True)
    c04_qnt_cot = fields.Str(required=True)
    c04_valor_unit_cot = fields.Str(required=True)
    c04_valor_total_cot = fields.Str(required=True)
    c04_valor_desc_cot = fields.Str(required=True)
    c04_valor_frete_cot = fields.Str(required=True)
    c04_valor_outro_cot = fields.Str(required=True)
    c04_valor_total_trib_cot = fields.Str(required=True)
    c04_status = fields.Str(required=True)
    c04_data_status = fields.Str(required=True)
    c05_observacao1 = fields.Str(required=True)
    c05_observacao2 = fields.Str(required=True)
    c05_qnt_cot = fields.Str(required=True)
    c05_valor_unit_cot = fields.Str(required=True)
    c05_valor_total_cot = fields.Str(required=True)
    c05_valor_desc_cot = fields.Str(required=True)
    c05_valor_frete_cot = fields.Str(required=True)
    c05_valor_outro_cot = fields.Str(required=True)
    c05_valor_total_trib_cot = fields.Str(required=True)
    c05_status = fields.Str(required=True)
    c05_data_status = fields.Str(required=True)
    c06_observacao1 = fields.Str(required=True)
    c06_observacao2 = fields.Str(required=True)
    c06_qnt_cot = fields.Str(required=True)
    c06_valor_unit_cot = fields.Str(required=True)
    c06_valor_total_cot = fields.Str(required=True)
    c06_valor_desc_cot = fields.Str(required=True)
    c06_valor_frete_cot = fields.Str(required=True)
    c06_valor_outro_cot = fields.Str(required=True)
    c06_valor_total_trib_cot = fields.Str(required=True)
    c06_status = fields.Str(required=True)
    c06_data_status = fields.Str(required=True)
    c07_observacao1 = fields.Str(required=True)
    c07_observacao2 = fields.Str(required=True)
    c07_qnt_cot = fields.Str(required=True)
    c07_valor_unit_cot = fields.Str(required=True)
    c07_valor_total_cot = fields.Str(required=True)
    c07_valor_desc_cot = fields.Str(required=True)
    c07_valor_frete_cot = fields.Str(required=True)
    c07_valor_outro_cot = fields.Str(required=True)
    c07_valor_total_trib_cot = fields.Str(required=True)
    c07_status = fields.Str(required=True)
    c07_data_status = fields.Str(required=True)
    c08_observacao1 = fields.Str(required=True)
    c08_observacao2 = fields.Str(required=True)
    c08_qnt_cot = fields.Str(required=True)
    c08_valor_unit_cot = fields.Str(required=True)
    c08_valor_total_cot = fields.Str(required=True)
    c08_valor_desc_cot = fields.Str(required=True)
    c08_valor_frete_cot = fields.Str(required=True)
    c08_valor_outro_cot = fields.Str(required=True)
    c08_valor_total_trib_cot = fields.Str(required=True)
    c08_status = fields.Str(required=True)
    c08_data_status = fields.Str(required=True)
    c09_observacao1 = fields.Str(required=True)
    c09_observacao2 = fields.Str(required=True)
    c09_qnt_cot = fields.Str(required=True)
    c09_valor_unit_cot = fields.Str(required=True)
    c09_valor_total_cot = fields.Str(required=True)
    c09_valor_desc_cot = fields.Str(required=True)
    c09_valor_frete_cot = fields.Str(required=True)
    c09_valor_outro_cot = fields.Str(required=True)
    c09_valor_total_trib_cot = fields.Str(required=True)
    c09_status = fields.Str(required=True)
    c09_data_status = fields.Str(required=True)
    c10_observacao1 = fields.Str(required=True)
    c10_observacao2 = fields.Str(required=True)
    c10_qnt_cot = fields.Str(required=True)
    c10_valor_unit_cot = fields.Str(required=True)
    c10_valor_total_cot = fields.Str(required=True)
    c10_valor_desc_cot = fields.Str(required=True)
    c10_valor_frete_cot = fields.Str(required=True)
    c10_valor_outro_cot = fields.Str(required=True)
    c10_valor_total_trib_cot = fields.Str(required=True)
    c10_status = fields.Str(required=True)
    c10_data_status = fields.Str(required=True)

    c01_fin_cond_pagrec_id = fields.Str(required=True)
    c01_fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    c01_ger_pessoa_endereco_id = fields.Str(required=True)
    c01_ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    c01_ger_pessoa_id = fields.Str(required=True, dump_only=True)
    c01_ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    c01_sys_user_id_aprov = fields.Str(required=True)
    c01_sys_user_id_aprov_obj = fields.Nested("SysUserSchema", dump_only=True)

    c02_fin_cond_pagrec_id = fields.Str(required=True)
    c02_fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    c02_ger_pessoa_endereco_id = fields.Str(required=True)
    c02_ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    c02_ger_pessoa_id = fields.Str(required=True)
    c02_ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    c02_sys_user_id_aprov = fields.Str(required=True)
    c02_sys_user_id_aprov_obj = fields.Nested("SysUserSchema", dump_only=True)

    c03_fin_cond_pagrec_id = fields.Str(required=True)
    c03_fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    c03_ger_pessoa_endereco_id = fields.Str(required=True)
    c03_ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    c03_ger_pessoa_id = fields.Str(required=True)
    c03_ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    c03_sys_user_id_aprov = fields.Str(required=True)
    c03_sys_user_id_aprov_obj = fields.Nested("SysUserSchema", dump_only=True)

    c04_fin_cond_pagrec_id = fields.Str(required=True)
    c04_fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    c04_ger_pessoa_endereco_id = fields.Str(required=True)
    c04_ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    c04_ger_pessoa_id = fields.Str(required=True)
    c04_ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    c04_sys_user_id_aprov = fields.Str(required=True)
    c04_sys_user_id_aprov_obj = fields.Nested("SysUserSchema", dump_only=True)

    c05_fin_cond_pagrec_id = fields.Str(required=True)
    c05_fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    c05_ger_pessoa_endereco_id = fields.Str(required=True)
    c05_ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    c05_ger_pessoa_id = fields.Str(required=True)
    c05_ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    c05_sys_user_id_aprov = fields.Str(required=True)
    c05_sys_user_id_aprov_obj = fields.Nested("SysUserSchema", dump_only=True)

    c06_fin_cond_pagrec_id = fields.Str(required=True)
    c06_fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    c06_ger_pessoa_endereco_id = fields.Str(required=True)
    c06_ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    c06_ger_pessoa_id = fields.Str(required=True)
    c06_ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    c06_sys_user_id_aprov = fields.Str(required=True)
    c06_sys_user_id_aprov_obj = fields.Nested("SysUserSchema", dump_only=True)

    c07_fin_cond_pagrec_id = fields.Str(required=True)
    c07_fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    c07_ger_pessoa_endereco_id = fields.Str(required=True)
    c07_ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    c07_ger_pessoa_id = fields.Str(required=True)
    c07_ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    c07_sys_user_id_aprov = fields.Str(required=True)
    c07_sys_user_id_aprov_obj = fields.Nested("SysUserSchema", dump_only=True)

    c08_fin_cond_pagrec_id = fields.Str(required=True)
    c08_fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    c08_ger_pessoa_endereco_id = fields.Str(required=True)
    c08_ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    c08_ger_pessoa_id = fields.Str(required=True)
    c08_ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    c08_sys_user_id_aprov = fields.Str(required=True)
    c08_sys_user_id_aprov_obj = fields.Nested("SysUserSchema", dump_only=True)

    c09_fin_cond_pagrec_id = fields.Str(required=True)
    c09_fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    c09_ger_pessoa_endereco_id = fields.Str(required=True)
    c09_ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    c09_ger_pessoa_id = fields.Str(required=True)
    c09_ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    c09_sys_user_id_aprov = fields.Str(required=True)
    c09_sys_user_id_aprov_obj = fields.Nested("SysUserSchema", dump_only=True)

    c10_fin_cond_pagrec_id = fields.Str(required=True)
    c10_fin_cond_pagrec_id_obj = fields.Nested("FinCondPagrecSchema", dump_only=True)

    c10_ger_pessoa_endereco_id = fields.Str(required=True)
    c10_ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    c10_ger_pessoa_id = fields.Str(required=True)
    c10_ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    c10_sys_user_id_aprov = fields.Str(required=True)
    c10_sys_user_id_aprov_obj = fields.Nested("SysUserSchema", dump_only=True)

    ger_itemserv_id = fields.Str(required=True)
    ger_itemserv_id_obj = fields.Nested("GerItemservSchema", dump_only=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)


# ==========================================================


class MovEntregaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovEntrega
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    ger_cidade_id = fields.Str(required=True)
    ger_cidade_id_obj = fields.Nested("GerCidadeSchema", dump_only=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)

    mov_entrega_doc_childs = fields.Nested("MovEntregaDocSchema", many=True)


# ==========================================================


class MovItemservSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovItemserv
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    qnt_orig = fields.Str(required=True)
    valor_unit_orig = fields.Str(required=True)
    qnt_conv = fields.Str(required=True)
    valor_unit_conv = fields.Str(required=True)
    valor_bruto = fields.Str(required=True)
    valor_desconto = fields.Str(required=True)
    valor_acrecimo = fields.Str(required=True)
    valor_outros = fields.Str(required=True)
    valor_liquido = fields.Str(required=True)
    qnt_devolvida = fields.Str(required=True)
    valor_frete = fields.Str(required=True)
    valor_seguro = fields.Str(required=True)
    observacao = fields.Str(required=True)
    valor_tributo_retido = fields.Str(required=True)
    valor_tributo_total = fields.Str(required=True)
    qnt_altura = fields.Str(required=True)
    qnt_largura = fields.Str(required=True)
    qnt_comprimento = fields.Str(required=True)
    nome_itemserv = fields.Str(required=True)
    fis_obra_art = fields.Str(required=True)
    fis_obra_cei = fields.Str(required=True)
    fis_numero_proc_susp_nfs = fields.Str(required=True)
    fis_doc_cnae_nfs = fields.Str(required=True)
    valor_outros_tributo_ret = fields.Str(required=True)
    valor_desconto_cond = fields.Str(required=True)
    valor_desconto_incond = fields.Str(required=True)
    valor_deducao = fields.Str(required=True)
    qnt_min_pessoa_cot = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    fis_cfop_id = fields.Str(required=True)
    fis_cfop_id_obj = fields.Nested("FisCfopSchema", dump_only=True)

    ger_itemserv_id = fields.Str(required=True)
    ger_itemserv_id_obj = fields.Nested("GerItemservSchema", dump_only=True)

    ger_itemserv_lote_id = fields.Str(required=True)
    ger_itemserv_lote_id_obj = fields.Nested("GerItemservLoteSchema", dump_only=True)

    ger_itemserv_var_id = fields.Str(required=True)
    ger_itemserv_var_id_obj = fields.Nested("GerItemservVarSchema", dump_only=True)

    ger_umedida_id_conv = fields.Str(required=True)
    ger_umedida_id_obj = fields.Nested("GerUmedidaSchema", dump_only=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)


# ==========================================================


class MovLacreSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovLacre
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    lacres = fields.Str(required=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)


# ==========================================================


class MovMedidaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovMedida
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    tipo_medida = fields.Str(required=True)
    qnt_medida = fields.Str(required=True)
    marca = fields.Str(required=True)
    nr_volume = fields.Str(required=True)
    peso_liquido = fields.Str(required=True)
    peso_bruto = fields.Str(required=True)

    ger_umedida_id = fields.Str(required=True)
    ger_umedida_id_obj = fields.Nested("GerUmedidaSchema", dump_only=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)


# ==========================================================


class MovPedagioSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovPedagio
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    valor_pedagio = fields.Str(required=True)
    nr_comprovante = fields.Str(required=True)

    ger_pessoa_id_emp_pedagio = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    ger_pessoa_id_responsavel = fields.Str(required=True)
    ger_pessoa_id_responsavel_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)


# ==========================================================


class MovPercursoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovPercurso
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    ger_cidade_id = fields.Str(required=True)
    ger_cidade_id_obj = fields.Nested("GerCidadeSchema", dump_only=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)


# ==========================================================


class MovSeguradoraSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovSeguradora
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nr_apolice = fields.Str(required=True)
    nr_averbacao = fields.Str(required=True)
    valor = fields.Str(required=True)
    tipo_responsavel = fields.Str(required=True)

    ger_pessoa_id_responsavel = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    ger_pessoa_id_seguradora = fields.Str(required=True)
    ger_pessoa1_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    mov_id_obj = fields.Nested("MovSchema", dump_only=True)
    mov_id = fields.Str(required=True)


# ==========================================================


class MovTomadorSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovTomador
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    ger_pessoa_id_responsavel = fields.Str(required=True)
    ger_pessoa_id_responsavel_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)


# ==========================================================


class MovEntregaDocSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovEntregaDoc
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    valor_total = fields.Str(required=True)
    chave_documento = fields.Str(required=True)
    modelo_documento = fields.Str(required=True)
    serie_documento = fields.Str(required=True)
    nr_documento = fields.Str(required=True)
    subserie_documento = fields.Str(required=True)
    data_emissao = fields.Str(required=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)

    mov_id_interno = fields.Str(required=True)
    mov_id_interno_obj = fields.Nested("MovSchema", dump_only=True)


# ==========================================================


class MovFreteSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovFrete
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    valor_frete = fields.Str(required=True)
    adic_frete_base_cal_icms = fields.Str(required=True)
    valor_base_calc = fields.Str(required=True)
    perc_aliquota = fields.Str(required=True)
    valor_imposto = fields.Str(required=True)
    valor_pis = fields.Str(required=True)
    valor_cofins = fields.Str(required=True)

    ger_pessoa_endereco_id_condutor = fields.Str(required=True)
    ger_pessoa_endereco_id_condutor_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ger_pessoa_endereco_id_transp = fields.Str(required=True)
    ger_pessoa_endereco_id_transp_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)

    ope_centro2_id_equip = fields.Str(required=True)
    ope_centro2_id_equip_obj = fields.Nested("OpeCentro2EquipSchema", dump_only=True)


# ==========================================================


class MovOrigemSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovOrigem
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    mov_id = fields.Str(required=True)
    tipo = fields.Str(required=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)

    mov_id_origem = fields.Str(required=True)
    mov_id_origem_obj = fields.Nested("MovSchema", dump_only=True)

    mov_itemserv_id = fields.Str(required=True)
    mov_itemserv_id_obj = fields.Nested("MovItemservSchema", dump_only=True)

    mov_itemserv_id_origem = fields.Str(required=True)
    mov_itemserv_id_origem_obj = fields.Nested("MovItemservSchema", dump_only=True)


# ==========================================================


class MovReboqueSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = MovReboque
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    mov_id = fields.Str(required=True)
    mov_id_obj = fields.Nested("MovSchema", dump_only=True)

    ope_centro2_id_equip = fields.Str(required=True)
    ope_centro2_id_equip_obj = fields.Nested("OpeCentro2EquipSchema", dump_only=True)


# ==========================================================
