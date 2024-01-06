import app
from app.modules.ctb.base.ctb_model import (
    CtbCentro,
    CtbCentroGrupo,
    CtbComp,
    CtbCompGrupo,
    CtbConta,
    CtbContaGrupo,
    CtbContaVersao,
    CtbHistorico,
    CtbLanc,
    CtbLancDet,
    CtbLote,
    CtbTipoSaldo,
    CtbUnitParam,
    CtbVersao,
)
from app.generics.generic_schema import generic_schema
from marshmallow import EXCLUDE, fields


from app.generics.generic_schema_field import fields_Type_Obj_Sql

from app.utils.validator_util import valid_type_choice_sql


# ==========================================================


class CtbVersaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbVersao
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
    sigla_versao = fields.Str(required=True)

    tipo_rp = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="ctb_versao", field_name="tipo_rp", session=app.db.session
        ),
    )
    tipo_rp_obj = fields_Type_Obj_Sql(
        field_choice="tipo_rp",
        table_name="ctb_versao",
        field_name="tipo_rp",
        session=app.db.session,
    )

    versao_atual = fields.Str(
        load_default="N",
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
    data_per_ini = fields.Str(required=True)
    data_per_fin = fields.Str(required=True)


# ==========================================================


class CtbCentroGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbCentroGrupo
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
    sigla_centro_grupo = fields.Str(required=True)


# ==========================================================


class CtbContaVersaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbContaVersao
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
    sigla_versao = fields.Str(required=True)
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
    data_valid_ini = fields.Str(required=True)


# ==========================================================


class CtbHistoricoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbHistorico
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
    sigla_historico = fields.Str(required=True)


# ==========================================================


class CtbLoteSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbLote
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
    sigla_lote = fields.Str(required=True)


# ==========================================================


class CtbTipoSaldoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbTipoSaldo
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

    sigla_tipo_saldo = fields.Str(required=True)
    mes_ini_fechamento = fields.Number(required=True)
    mes_fin_fechamento = fields.Number(required=True)


# ==========================================================


class CtbUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)


# ==========================================================


class CtbCentroSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbCentro
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
    sigla_centro = fields.Str(required=True)

    ctb_centro_grupo_id = fields.Str(required=True)
    ctb_centro_grupo_id_obj = fields.Nested("CtbCentroGrupoSchema", dump_only=True)


# ==========================================================


class CtbCompSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbComp
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
    sigla_comp = fields.Str(required=True)
    ctb_comp_id_calc_orig = fields.Str(required=True, dump_only=True)

    fator_calc_origem = fields.Number(required=True)

    ctb_comp_grupo_id = fields.Str(required=True)
    ctb_comp_grupo_id_obj = fields.Nested("CtbCompGrupoSchema", dump_only=True)

    ger_umedida_id = fields.Str(required=True)
    ger_umedida_id_obj = fields.Nested("GerUmedidaSchema", dump_only=True)


# ==========================================================


class CtbContaGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbContaGrupo
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
    sigla_conta_grupo = fields.Str(required=True)
    estrutura = fields.Str(required=True)

    ctb_conta_versao_id = fields.Str(required=True)
    ctb_conta_versao_id_obj = fields.Nested("CtbContaVersaoSchema", dump_only=True)


# ==========================================================


class CtbContaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbConta
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
    sigla_conta = fields.Str(required=True)

    tipo_variacao = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ctb_conta", field_name="tipo_variacao", session=app.db.session
        ),
    )
    tipo_variacao_obj = fields_Type_Obj_Sql(
        field_choice="tipo_variacao",
        table_name="ctb_conta",
        field_name="tipo_variacao",
        session=app.db.session,
    )

    tipo_dc = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ctb_conta", field_name="tipo_dc", session=app.db.session
        ),
    )
    tipo_dc_obj = fields_Type_Obj_Sql(
        field_choice="tipo_dc",
        table_name="ctb_conta",
        field_name="tipo_dc",
        session=app.db.session,
    )

    tipo_conta = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ctb_conta", field_name="tipo_conta", session=app.db.session
        ),
    )
    tipo_conta_obj = fields_Type_Obj_Sql(
        field_choice="tipo_conta",
        table_name="ctb_conta",
        field_name="tipo_conta",
        session=app.db.session,
    )

    ctb_conta_grupo_id = fields.Str(required=True)
    ctb_conta_grupo_id_obj = fields.Nested("CtbContaGrupoSchema", dump_only=True)

    ctb_conta_versao_id = fields.Str(required=True)
    ctb_conta_versao_id_obj = fields.Nested("CtbContaVersaoSchema", dump_only=True)


# ==========================================================


class CtbLancSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbLanc
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    numero_lanc = fields.Str(required=True)
    data_lanc = fields.Str(required=True)
    historico = fields.Str(required=True)

    status = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ctb_lanc", field_name="status", session=app.db.session
        ),
    )
    status_obj = fields_Type_Obj_Sql(
        field_choice="status",
        table_name="ctb_lanc",
        field_name="status",
        session=app.db.session,
    )

    status_observacao = fields.Str(required=True)

    ctb_historico_id = fields.Str(required=True)
    ctb_historico_id_obj = fields.Nested("CtbHistoricoSchema", dump_only=True)

    ctb_lote_id = fields.Str(required=True)
    ctb_lote_id_obj = fields.Nested("CtbLoteSchema", dump_only=True)

    ctb_versao_id = fields.Str(required=True)
    ctb_versao_id_obj = fields.Nested("CtbVersaoSchema", dump_only=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)


# ==========================================================


class CtbLancDetSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbLancDet
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    tipo_dc = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="ctb_lanc_det", field_name="tipo_dc", session=app.db.session
        ),
    )
    tipo_dc_obj = fields_Type_Obj_Sql(
        field_choice="tipo_dc",
        table_name="ctb_lanc_det",
        field_name="tipo_dc",
        session=app.db.session,
    )

    valor = fields.Str(required=True)
    origem_tipo = fields.Str(required=True)
    origem_id = fields.Str(required=True)
    observacao = fields.Str(required=True)
    qnt = fields.Str(required=True)

    ctb_comp_id = fields.Str(required=True)
    ctb_comp_id_obj = fields.Nested("CtbCompSchema", dump_only=True)

    ctb_conta_id = fields.Str(required=True)
    ctb_conta_id_obj = fields.Nested("CtbContaSchema", dump_only=True)

    ctb_lanc_id = fields.Str(required=True)
    ctb_lanc_id_obj = fields.Nested("CtbLancSchema", dump_only=True)

    ope_atividade_id = fields.Str(required=True)
    ope_atividade_id_obj = fields.Nested("OpeAtividadeSchema", dump_only=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    process_id = fields.Str(required=True)
    process_id_obj = fields.Nested("SysProcessLogSchema", dump_only=True)

    # ==========================================================


class CtbCompGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CtbCompGrupo
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
    sigla_comp_grupo = fields.Str(required=True)
