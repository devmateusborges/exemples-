import app
from app.generics.generic_schema import generic_schema

from marshmallow import EXCLUDE, fields

from app.modules.ind.base.ind_model import (
    IndIndic,
    IndIndicSubgrupo,
    IndCjd,
    IndCjdFtd,
    IndCnd,
    IndFtd,
    IndFtdPrm,
    IndGrupo,
    IndGrupoSubgrupo,
    IndPnl,
    IndPnlRel,
    IndPrm,
    IndRel,
    IndRelPrm,
    IndRelVar,
    IndIndicIndic,
    IndSubgrupo,
    IndUnitParam,
    IndVrAno,
    IndVrBimestre,
    IndVrDia,
    IndVrMes,
    IndVrMeta,
    IndVrQuadrimestre,
    IndVrQuinzena,
    IndVrSemana,
    IndVrSemestre,
    IndVrTrimestre,
    IndLegenda,
    IndLegendaConfig,
)

from app.utils.validator_util import valid_type_choice_sql
from app.generics.generic_schema_field import fields_Type_Obj_Sql

# ==========================================================


class IndCjdSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndCjd
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
    nome_tecnico = fields.Str(required=True)

    ind_cjd_ftd_childs = fields.Nested("IndCjdFtdSchema", many=True)


# ==========================================================


class IndCndSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndCnd
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

    tipo = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ind_cnd", field_name="tipo", session=app.db.session
        ),
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="ind_cnd",
        field_name="tipo",
        session=app.db.session,
    )

    config_cnd = fields.Str(required=True)
    sigla_ind_cnd = fields.Str(required=True)


# ==========================================================


class IndPnlSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndPnl
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nome = fields.Str(required=True)

    tipo = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ind_pnl", field_name="tipo", session=app.db.session
        ),
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="ind_pnl",
        field_name="tipo",
        session=app.db.session,
    )
    icon = fields.Str(required=True)

    ind_pnl_rel_childs = fields.Nested("IndPnlRelSchema", many=True)


# ==========================================================


class IndPrmSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndPrm
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
    nome_tecnico = fields.Str(required=True)

    tipo_dado = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ind_prm", field_name="tipo_dado", session=app.db.session
        ),
    )
    tipo_dado_obj = fields_Type_Obj_Sql(
        field_choice="tipo_dado",
        table_name="ind_prm",
        field_name="tipo_dado",
        session=app.db.session,
    )

    tipo_entrada = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ind_prm", field_name="tipo_entrada", session=app.db.session
        ),
    )
    tipo_entrada_obj = fields_Type_Obj_Sql(
        field_choice="tipo_entrada",
        table_name="ind_prm",
        field_name="tipo_entrada",
        session=app.db.session,
    )

    internal = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    internal_obj = fields_Type_Obj_Sql(
        field_choice="internal",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    busca_tabela = fields.Str(required=True)
    busca_campo_nome = fields.Str(required=True)
    busca_campo_id = fields.Str(required=True)
    busca_valores = fields.Str(required=True)

    obrigatorio = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    obrigatorio_obj = fields_Type_Obj_Sql(
        field_choice="obrigatorio",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    visivel = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    visivel_obj = fields_Type_Obj_Sql(
        field_choice="visivel",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    valor_padrao = fields.Str(required=True)

    busca_tabela_classe = fields.Str(required=True)
    busca_campo_nome_classe = fields.Str(required=True)
    busca_campo_id_classe = fields.Str(required=True)
    valor_prefixo = fields.Str(required=True)
    valor_sufixo = fields.Str(required=True)
    ind_ftd_id = fields.Str(required=True)
    ind_ftd_id_obj = fields.Nested("IndFtdSchema", dump_only=True)


# ==========================================================


class IndIndicSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndIndic
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    sigla_ind = fields.Str(required=True)
    nome = fields.Str(required=True)
    casas_dec = fields.Number(required=True)

    campo_ordenacao = fields.Str(
        load_default="1",
        validate=valid_type_choice_sql(
            table_name="ind_indic", field_name="campo_ordenacao", session=app.db.session
        ),
    )
    campo_ordenacao_obj = fields_Type_Obj_Sql(
        field_choice="campo_ordenacao",
        table_name="ind_indic",
        field_name="campo_ordenacao",
        session=app.db.session,
    )

    metodo_ordenacao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="ind_indic",
            field_name="metodo_ordenacao",
            session=app.db.session,
        ),
    )
    metodo_ordenacao_obj = fields_Type_Obj_Sql(
        field_choice="metodo_ordenacao",
        table_name="ind_indic",
        field_name="metodo_ordenacao",
        session=app.db.session,
    )

    totalizador_atributo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="ind_indic",
            field_name="totalizador_atributo",
            session=app.db.session,
        ),
    )
    totalizador_atributo_obj = fields_Type_Obj_Sql(
        field_choice="totalizador_atributo",
        table_name="ind_indic",
        field_name="totalizador_atributo",
        session=app.db.session,
    )

    exibir_media_real = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    exibir_media_real_obj = fields_Type_Obj_Sql(
        field_choice="exibir_media_real",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    exibir_media_meta = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    exibir_media_meta_obj = fields_Type_Obj_Sql(
        field_choice="exibir_media_meta",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    exibir_dia = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    exibir_dia_obj = fields_Type_Obj_Sql(
        field_choice="exibir_dia",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    exibir_semana = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    exibir_semana_obj = fields_Type_Obj_Sql(
        field_choice="exibir_semana",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    exibir_quinzena = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    exibir_quinzena_obj = fields_Type_Obj_Sql(
        field_choice="exibir_quinzena",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    exibir_mes = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    exibir_mes_obj = fields_Type_Obj_Sql(
        field_choice="exibir_mes",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    exibir_bimestre = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    exibir_bimestre_obj = fields_Type_Obj_Sql(
        field_choice="exibir_bimestre",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    exibir_trimestre = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    exibir_trimestre_obj = fields_Type_Obj_Sql(
        field_choice="exibir_trimestre",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    exibir_quadrimestre = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    exibir_quadrimestre_obj = fields_Type_Obj_Sql(
        field_choice="exibir_quadrimestre",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    exibir_semestre = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    exibir_semestre_obj = fields_Type_Obj_Sql(
        field_choice="exibir_semestre",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    exibir_ano = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    exibir_ano_obj = fields_Type_Obj_Sql(
        field_choice="exibir_ano",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    acumular_semana = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    acumular_semana_obj = fields_Type_Obj_Sql(
        field_choice="acumular_semana",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    acumular_quinzena = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    acumular_quinzena_obj = fields_Type_Obj_Sql(
        field_choice="acumular_quinzena",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    acumular_mes = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    acumular_mes_obj = fields_Type_Obj_Sql(
        field_choice="acumular_mes",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    acumular_bimestre = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    acumular_bimestre_obj = fields_Type_Obj_Sql(
        field_choice="acumular_bimestre",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    acumular_trimestre = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    acumular_trimestre_obj = fields_Type_Obj_Sql(
        field_choice="acumular_trimestre",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    acumular_quadrimestre = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    acumular_quadrimestre_obj = fields_Type_Obj_Sql(
        field_choice="acumular_quadrimestre",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    acumular_semestre = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    acumular_semestre_obj = fields_Type_Obj_Sql(
        field_choice="acumular_semestre",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    acumular_ano = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    acumular_ano_obj = fields_Type_Obj_Sql(
        field_choice="acumular_ano",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    tipo_acumulo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="ind_indic", field_name="tipo_acumulo", session=app.db.session
        ),
    )
    tipo_acumulo_obj = fields_Type_Obj_Sql(
        field_choice="tipo_acumulo",
        table_name="ind_indic",
        field_name="tipo_acumulo",
        session=app.db.session,
    )

    ind_indic_id_pond = fields.Str(required=False, allow_none=True)

    grafico_tipo_atributo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="ind_indic",
            field_name="grafico_tipo_atributo",
            session=app.db.session,
        ),
    )
    grafico_tipo_atributo_obj = fields_Type_Obj_Sql(
        field_choice="grafico_tipo_atributo",
        table_name="ind_indic",
        field_name="grafico_tipo_atributo",
        session=app.db.session,
    )

    grafico_valor_vazio_zero = fields.Str(required=True)

    grafico_tipo_ind = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="ind_indic",
            field_name="grafico_tipo_ind",
            session=app.db.session,
        ),
    )
    grafico_tipo_ind_obj = fields_Type_Obj_Sql(
        field_choice="grafico_tipo_ind",
        table_name="ind_indic",
        field_name="grafico_tipo_ind",
        session=app.db.session,
    )
    tipo_meta = fields.Str(
        load_default="1",
        validate=valid_type_choice_sql(
            table_name="ind_indic", field_name="tipo_meta", session=app.db.session
        ),
    )
    tipo_meta_obj = fields_Type_Obj_Sql(
        field_choice="tipo_meta",
        table_name="ind_indic",
        field_name="tipo_meta",
        session=app.db.session,
    )
    tipo_meta_var = fields.Str(
        load_default="1",
        validate=valid_type_choice_sql(
            table_name="ind_indic", field_name="tipo_meta_var", session=app.db.session
        ),
    )
    tipo_meta_var_obj = fields_Type_Obj_Sql(
        field_choice="tipo_meta_var",
        table_name="ind_indic",
        field_name="tipo_meta_var",
        session=app.db.session,
    )

    exibir_dia_ant = fields.Number(required=True)
    exibir_dia_pos = fields.Number(required=True)
    exibir_semana_ant = fields.Number(required=True)
    exibir_semana_pos = fields.Number(required=True)
    exibir_quinzena_ant = fields.Number(required=True)
    exibir_quinzena_pos = fields.Number(required=True)
    exibir_mes_ant = fields.Number(required=True)
    exibir_mes_pos = fields.Number(required=True)
    exibir_bimestre_ant = fields.Number(required=True)
    exibir_bimestre_pos = fields.Number(required=True)
    exibir_trimestre_ant = fields.Number(required=True)
    exibir_trimestre_pos = fields.Number(required=True)
    exibir_quadrimestre_ant = fields.Number(required=True)
    exibir_quadrimestre_pos = fields.Number(required=True)
    exibir_semestre_ant = fields.Number(required=True)
    exibir_semestre_pos = fields.Number(required=True)
    exibir_ano_ant = fields.Number(required=True)
    exibir_ano_pos = fields.Number(required=True)

    ger_umedida_id = fields.Str(required=True)
    ger_umedida_id_obj = fields.Nested("GerUmedidaSchema", dump_only=True)

    ind_legenda_id = fields.Str(required=True)
    ind_legenda_id_obj = fields.Nested("IndLegendaSchema", dump_only=True)

    ind_indic_indic_childs = fields.Nested("IndIndicIndicSchema", many=True)
    ind_indic_subgrupo_childs = fields.Nested("IndIndicSubgrupoSchema", many=True)


# ==========================================================


class IndFtdSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndFtd
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
    config_ftd = fields.Str(required=True)
    nome_tecnico = fields.Str(required=True)

    ind_cnd_id = fields.Str(required=True)
    ind_cnd_id_obj = fields.Nested("IndCndSchema", dump_only=True)
    ind_ftd_prm_childs = fields.Nested("IndFtdPrmSchema", many=True)


# ==========================================================


class IndGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndGrupo
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
    ordem_exibicao = fields.Str(required=True)
    sigla_grupo = fields.Str(required=True)

    ind_grupo_subgrupo_childs = fields.Nested("IndGrupoSubgrupoSchema", many=True)


# ==========================================================


class IndSubgrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndSubgrupo
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
    ordem_exibicao = fields.Str(required=True)
    sigla_subgrupo = fields.Str(required=True)


# ==========================================================


class IndUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)


# ==========================================================


class IndCjdFtdSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndCjdFtd
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    ind_ftd_id = fields.Str(required=True)
    ind_ftd_id_obj = fields.Nested("IndFtdSchema", dump_only=True)


# ==========================================================


class IndFtdPrmSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndFtdPrm
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    ind_ftd_id = fields.Str(required=True)

    ind_prm_id = fields.Str(required=True)
    ind_prm_id_obj = fields.Nested("IndPrmSchema", dump_only=True)


# ==========================================================


class IndGrupoSubgrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndGrupoSubgrupo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    ind_subgrupo_id = fields.Str(required=True)
    ind_subgrupo_id_obj = fields.Nested("IndSubgrupoSchema", dump_only=True)


# ==========================================================


class IndRelSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndRel
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nome = fields.Str(required=True)
    nome_tecnico = fields.Str(required=True)

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
            table_name="ind_rel", field_name="tipo", session=app.db.session
        ),
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="ind_rel",
        field_name="tipo",
        session=app.db.session,
    )

    ind_cjd_id = fields.Str(required=True)
    ind_cjd_id_obj = fields.Nested("IndCjdSchema", dump_only=True)

    ind_ftd_id = fields.Str(required=True)
    ind_ftd_id_obj = fields.Nested("IndFtdSchema", dump_only=True)

    ind_rel_prm_childs = fields.Nested("IndRelPrmSchema", many=True)
    ind_rel_var_childs = fields.Nested("IndRelVarSchema", many=True)


# ==========================================================


class IndIndicIndicSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndIndicIndic
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    ind_indic_id_relac = fields.Str(required=True)
    ind_indic_id_relac_obj = fields.Nested("IndIndicSchema", dump_only=True)


# ==========================================================


class IndLegendaConfigSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndLegendaConfig
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    qnt_de = fields.Float(required=True)
    qnt_ate = fields.Float(required=True)
    cor = fields.Str(required=True)
    icon = fields.Str(required=True)
    observacao = fields.Str(required=False)


# ==========================================================


class IndLegendaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndLegenda
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    sigla_ind_legenda = fields.Str(required=True)
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

    ind_legenda_config_childs = fields.Nested("IndLegendaConfigSchema", many=True)


# ==========================================================


class IndIndicSubgrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndIndicSubgrupo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    ind_subgrupo_id = fields.Str(required=True)
    ind_subgrupo_id_obj = fields.Nested("IndSubgrupoSchema", dump_only=True)


# ==========================================================


class IndPnlRelSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndPnlRel
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    ind_rel_id = fields.Str(required=True)
    ind_rel_id_obj = fields.Nested("IndRelSchema", dump_only=True)


# ==========================================================


class IndRelPrmSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndRelPrm
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    ordem_exib = fields.Str(required=True)
    valor_padrao = fields.Str(required=True)

    ind_prm_id = fields.Str(required=True)
    ind_prm_id_obj = fields.Nested("IndPrmSchema", dump_only=True)


# ==========================================================


class IndRelVarSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndRelVar
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    var_nome_tecnico = fields.Str(required=True)
    var_nome_descritivo = fields.Str(required=True)
    var_agrupavel = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    var_agrupavel_obj = fields_Type_Obj_Sql(
        field_choice="var_agrupavel",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    ordem_padrao = fields.Str(required=True)
    largura = fields.Str(required=True)
    visivel = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    visivel_obj = fields_Type_Obj_Sql(
        field_choice="visivel",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    var_nome_tecnico_prefixo = fields.Str(required=True)


# ==========================================================


class IndVrAnoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndVrAno
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)
    ger_per_id = fields.Str(required=True)
    ger_per_id_obj = fields.Nested("GerPerSchema", dump_only=True)
    ind_indic_id = fields.Str(required=True)
    atributo = fields.Str(required=True)
    valor_real = fields.Str(required=True)
    valor_meta = fields.Str(required=True)
    aprovado_exibicao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aprovado_exibicao_obj = fields_Type_Obj_Sql(
        field_choice="aprovado_exibicao",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    import_id = fields.Str(required=True)
    import_arquivo = fields.Str(required=True)
    atributo1 = fields.Str(required=False)
    atributo2 = fields.Str(required=False)
    atributo3 = fields.Str(required=False)
    atributo4 = fields.Str(required=False)
    atributo5 = fields.Str(required=False)
    atributo_nivel = fields.Integer(required=False)


# ==========================================================


class IndVrBimestreSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndVrBimestre
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)
    ger_per_id = fields.Str(required=True)
    ger_per_id_obj = fields.Nested("GerPerSchema", dump_only=True)
    ind_indic_id = fields.Str(required=True)
    atributo = fields.Str(required=True)
    valor_real = fields.Str(required=True)
    valor_meta = fields.Str(required=True)
    aprovado_exibicao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aprovado_exibicao_obj = fields_Type_Obj_Sql(
        field_choice="aprovado_exibicao",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    import_id = fields.Str(required=True)
    import_arquivo = fields.Str(required=True)
    atributo1 = fields.Str(required=False)
    atributo2 = fields.Str(required=False)
    atributo3 = fields.Str(required=False)
    atributo4 = fields.Str(required=False)
    atributo5 = fields.Str(required=False)
    atributo_nivel = fields.Integer(required=False)


# ==========================================================


class IndVrDiaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndVrDia
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)
    ger_per_id = fields.Str(required=True)
    ger_per_id_obj = fields.Nested("GerPerSchema", dump_only=True)
    ind_indic_id = fields.Str(required=True)
    atributo = fields.Str(required=True)
    valor_real = fields.Str(required=True)
    valor_meta = fields.Str(required=True)
    aprovado_exibicao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aprovado_exibicao_obj = fields_Type_Obj_Sql(
        field_choice="aprovado_exibicao",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    import_id = fields.Str(required=True)
    import_arquivo = fields.Str(required=True)
    atributo1 = fields.Str(required=False)
    atributo2 = fields.Str(required=False)
    atributo3 = fields.Str(required=False)
    atributo4 = fields.Str(required=False)
    atributo5 = fields.Str(required=False)
    atributo_nivel = fields.Integer(required=False)


# ==========================================================


class IndVrMesSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndVrMes
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)
    ger_per_id = fields.Str(required=True)
    ger_per_id_obj = fields.Nested("GerPerSchema", dump_only=True)
    ind_indic_id = fields.Str(required=True)
    atributo = fields.Str(required=True)
    valor_real = fields.Str(required=True)
    valor_meta = fields.Str(required=True)
    aprovado_exibicao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aprovado_exibicao_obj = fields_Type_Obj_Sql(
        field_choice="aprovado_exibicao",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    import_id = fields.Str(required=True)
    import_arquivo = fields.Str(required=True)
    atributo1 = fields.Str(required=False)
    atributo2 = fields.Str(required=False)
    atributo3 = fields.Str(required=False)
    atributo4 = fields.Str(required=False)
    atributo5 = fields.Str(required=False)
    atributo_nivel = fields.Integer(required=False)


# ==========================================================


class IndVrQuadrimestreSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndVrQuadrimestre
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)
    ger_per_id = fields.Str(required=True)
    ger_per_id_obj = fields.Nested("GerPerSchema", dump_only=True)
    ind_indic_id = fields.Str(required=True)
    atributo = fields.Str(required=True)
    valor_real = fields.Str(required=True)
    valor_meta = fields.Str(required=True)
    aprovado_exibicao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aprovado_exibicao_obj = fields_Type_Obj_Sql(
        field_choice="aprovado_exibicao",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    import_id = fields.Str(required=True)
    import_arquivo = fields.Str(required=True)
    atributo1 = fields.Str(required=False)
    atributo2 = fields.Str(required=False)
    atributo3 = fields.Str(required=False)
    atributo4 = fields.Str(required=False)
    atributo5 = fields.Str(required=False)
    atributo_nivel = fields.Integer(required=False)


# ==========================================================


class IndVrQuinzenaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndVrQuinzena
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)
    ger_per_id = fields.Str(required=True)
    ger_per_id_obj = fields.Nested("GerPerSchema", dump_only=True)
    ind_indic_id = fields.Str(required=True)
    atributo = fields.Str(required=True)
    valor_real = fields.Str(required=True)
    valor_meta = fields.Str(required=True)
    aprovado_exibicao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aprovado_exibicao_obj = fields_Type_Obj_Sql(
        field_choice="aprovado_exibicao",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    import_id = fields.Str(required=True)
    import_arquivo = fields.Str(required=True)
    atributo1 = fields.Str(required=False)
    atributo2 = fields.Str(required=False)
    atributo3 = fields.Str(required=False)
    atributo4 = fields.Str(required=False)
    atributo5 = fields.Str(required=False)
    atributo_nivel = fields.Integer(required=False)


# ==========================================================


class IndVrSemanaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndVrSemana
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)
    ger_per_id = fields.Str(required=True)
    ger_per_id_obj = fields.Nested("GerPerSchema", dump_only=True)
    ind_indic_id = fields.Str(required=True)
    atributo = fields.Str(required=True)
    valor_real = fields.Str(required=True)
    valor_meta = fields.Str(required=True)
    aprovado_exibicao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aprovado_exibicao_obj = fields_Type_Obj_Sql(
        field_choice="aprovado_exibicao",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    import_id = fields.Str(required=True)
    import_arquivo = fields.Str(required=True)
    atributo1 = fields.Str(required=False)
    atributo2 = fields.Str(required=False)
    atributo3 = fields.Str(required=False)
    atributo4 = fields.Str(required=False)
    atributo5 = fields.Str(required=False)
    atributo_nivel = fields.Integer(required=False)


# ==========================================================


class IndVrSemestreSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndVrSemestre
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)
    ger_per_id = fields.Str(required=True)
    ger_per_id_obj = fields.Nested("GerPerSchema", dump_only=True)
    ind_indic_id = fields.Str(required=True)
    atributo = fields.Str(required=True)
    valor_real = fields.Str(required=True)
    valor_meta = fields.Str(required=True)
    aprovado_exibicao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aprovado_exibicao_obj = fields_Type_Obj_Sql(
        field_choice="aprovado_exibicao",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    import_id = fields.Str(required=True)
    import_arquivo = fields.Str(required=True)
    atributo1 = fields.Str(required=False)
    atributo2 = fields.Str(required=False)
    atributo3 = fields.Str(required=False)
    atributo4 = fields.Str(required=False)
    atributo5 = fields.Str(required=False)
    atributo_nivel = fields.Integer(required=False)


# ==========================================================


class IndVrTrimestreSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndVrTrimestre
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)
    ger_per_id = fields.Str(required=True)
    ger_per_id_obj = fields.Nested("GerPerSchema", dump_only=True)
    ind_indic_id = fields.Str(required=True)
    atributo = fields.Str(required=True)
    valor_real = fields.Str(required=True)
    valor_meta = fields.Str(required=True)
    aprovado_exibicao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aprovado_exibicao_obj = fields_Type_Obj_Sql(
        field_choice="aprovado_exibicao",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    import_id = fields.Str(required=True)
    import_arquivo = fields.Str(required=True)
    atributo1 = fields.Str(required=False)
    atributo2 = fields.Str(required=False)
    atributo3 = fields.Str(required=False)
    atributo4 = fields.Str(required=False)
    atributo5 = fields.Str(required=False)
    atributo_nivel = fields.Integer(required=False)


# ==========================================================


class IndVrMetaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = IndVrMeta
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)
    ger_per_id = fields.Str(required=True)
    ger_per_id_obj = fields.Nested("GerPerSchema", dump_only=True)
    ind_indic_id = fields.Str(required=True)
    atributo = fields.Str(required=True)
    valor_meta = fields.Str(required=True)
    aprovado_exibicao = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    aprovado_exibicao_obj = fields_Type_Obj_Sql(
        field_choice="aprovado_exibicao",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    ordem = fields.Str(required=True)
    import_id = fields.Str(required=True)
    import_arquivo = fields.Str(required=True)
    atributo1 = fields.Str(required=False)
    atributo2 = fields.Str(required=False)
    atributo3 = fields.Str(required=False)
    atributo4 = fields.Str(required=False)
    atributo5 = fields.Str(required=False)
    atributo_nivel = fields.Integer(required=False)


# ==========================================================
