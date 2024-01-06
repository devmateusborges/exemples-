import app
from app.generics.generic_schema import generic_schema
from marshmallow import EXCLUDE, fields
from app.generics.generic_schema_field import fields_Type_Obj_Sql
from app.utils.validator_util import valid_type_choice_sql

from app.modules.ope.base.ope_model import (
    OpeAtividade,
    OpeAtividadeGrupo,
    OpeAtividadeProd,
    OpeAtividadeSistema,
    OpeCentro1,
    OpeCentro2,
    OpeCentro2Area,
    OpeCentro2Equip,
    OpeCentro2Estoque,
    OpeCentro2MapaCoord,
    OpeCentro2MapaGeometria,
    OpeCentro2MovMedia,
    OpeCentro2Ord,
    OpeCentro2OrdAtiv,
    OpeCentro2OrdDest,
    OpeCentro2OrdItemserv,
    OpeCentro2OrdRec,
    OpeCentro2OrdStatus,
    OpeCentro2OrdTipo,
    OpeCentro2ParamPer,
    OpeCentro2Pessoa,
    OpeCentroConfig,
    OpeCentroDest,
    OpeCentroGrupo,
    OpeCentroPrev,
    OpeCentroPrevDest,
    OpeCentroRatFator,
    OpeCentroRatPeriodo,
    OpeCentroRatTipo,
    OpeCentroRend,
    OpeCentroRendFator,
    OpeCentroSubgrupo,
    OpeCentroSubtipo,
    OpeCentroTipo,
    OpeCentroVersao,
    OpeCicloVar,
    OpeCompart,
    OpeCompartGrupo,
    OpeCompartItemserv,
    OpeCompartMedida,
    OpeCompartOcor,
    OpeCompartPosicao,
    OpeCompartStatus,
    OpeCompartSubgrupo,
    OpeCompartTipo,
    OpeEspac,
    OpeEstagio,
    OpeFrenteTrabalho,
    OpeOcor,
    OpeOcorCompartMov,
    OpeOcorCompartMovDet,
    OpeOcorGrupo,
    OpeOcorMov,
    OpeOcorMovDest,
    OpeOcorMovDet,
    OpeOcorPrev,
    OpeOcorStatus,
    OpeOcorTipo,
    OpePeriodo,
    OpeRegiao,
    OpeTipoSolo,
    OpeUnitParam,
)


# ==========================================================


class OpeCentroTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroTipo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nome = fields.Str(required=True)
    tipo_es = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="ope_centro_tipo", field_name="tipo_es", session=app.db.session
        ),
    )
    tipo_es_obj = fields_Type_Obj_Sql(
        field_choice="tipo_es",
        table_name="ope_centro_tipo",
        field_name="tipo_es",
        session=app.db.session,
    )


# ==========================================================


class OpeAtividadeGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeAtividadeGrupo
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

    sigla_atividade_grupo = fields.Str(required=True)
    ordem = fields.Str(required=True)


# ==========================================================


class OpeAtividadeSistemaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeAtividadeSistema
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

    sigla_atividade_sistema = fields.Str(required=True)


# ==========================================================


class OpeCentro2OrdStatusSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2OrdStatus
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
    sigla_ord_status = fields.Str(required=True)
    tipo_status = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_status",
            field_name="tipo_status",
            session=app.db.session,
        )
    )
    tipo_status_obj = fields_Type_Obj_Sql(
        field_choice="tipo_status",
        table_name="ope_centro2_ord_status",
        field_name="tipo_status",
        session=app.db.session,
    )


# ==========================================================


class OpeCentro2OrdTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2OrdTipo
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

    sigla_ord_tipo = fields.Str(required=True)

    valida_saldo_area_aberta = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_tipo",
            field_name="valida_saldo_area_aberta",
            session=app.db.session,
        )
    )
    valida_saldo_area_aberta_obj = fields_Type_Obj_Sql(
        field_choice="valida_saldo_area_aberta",
        table_name="ope_centro2_ord_tipo",
        field_name="valida_saldo_area_aberta",
        session=app.db.session,
    )

    valida_prev_itemserv = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_tipo",
            field_name="valida_prev_itemserv",
            session=app.db.session,
        )
    )
    valida_prev_itemserv_obj = fields_Type_Obj_Sql(
        field_choice="valida_prev_itemserv",
        table_name="ope_centro2_ord_tipo",
        field_name="valida_prev_itemserv",
        session=app.db.session,
    )

    valida_prev_rec = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_tipo",
            field_name="valida_prev_rec",
            session=app.db.session,
        )
    )
    valida_prev_rec_obj = fields_Type_Obj_Sql(
        field_choice="valida_prev_rec",
        table_name="ope_centro2_ord_tipo",
        field_name="valida_prev_rec",
        session=app.db.session,
    )

    valida_regra_config = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_tipo",
            field_name="valida_regra_config",
            session=app.db.session,
        )
    )
    valida_regra_config_obj = fields_Type_Obj_Sql(
        field_choice="valida_regra_config",
        table_name="ope_centro2_ord_tipo",
        field_name="valida_regra_config",
        session=app.db.session,
    )

    valida_tipo_executor = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_tipo",
            field_name="valida_tipo_executor",
            session=app.db.session,
        )
    )
    valida_tipo_executor_obj = fields_Type_Obj_Sql(
        field_choice="valida_tipo_executor",
        table_name="ope_centro2_ord_tipo",
        field_name="valida_tipo_executor",
        session=app.db.session,
    )

    valida_rec_equip = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_tipo",
            field_name="valida_rec_equip",
            session=app.db.session,
        )
    )
    valida_rec_equip_obj = fields_Type_Obj_Sql(
        field_choice="valida_rec_equip",
        table_name="ope_centro2_ord_tipo",
        field_name="valida_rec_equip",
        session=app.db.session,
    )

    valida_rec_pessoa = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_tipo",
            field_name="valida_rec_pessoa",
            session=app.db.session,
        )
    )
    valida_rec_pessoa_obj = fields_Type_Obj_Sql(
        field_choice="valida_rec_pessoa",
        table_name="ope_centro2_ord_tipo",
        field_name="valida_rec_pessoa",
        session=app.db.session,
    )

    valida_itemserv_i = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_tipo",
            field_name="valida_itemserv_i",
            session=app.db.session,
        )
    )
    valida_itemserv_i_obj = fields_Type_Obj_Sql(
        field_choice="valida_itemserv_i",
        table_name="ope_centro2_ord_tipo",
        field_name="valida_itemserv_i",
        session=app.db.session,
    )

    valida_itemserv_s = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_tipo",
            field_name="valida_itemserv_s",
            session=app.db.session,
        )
    )
    valida_itemserv_s_obj = fields_Type_Obj_Sql(
        field_choice="valida_itemserv_s",
        table_name="ope_centro2_ord_tipo",
        field_name="valida_itemserv_s",
        session=app.db.session,
    )

    valida_tipo_prop_rec_equip = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_tipo",
            field_name="valida_tipo_prop_rec_equip",
            session=app.db.session,
        )
    )
    valida_tipo_prop_rec_equip_obj = fields_Type_Obj_Sql(
        field_choice="valida_tipo_prop_rec_equip",
        table_name="ope_centro2_ord_tipo",
        field_name="valida_tipo_prop_rec_equip",
        session=app.db.session,
    )

    valida_tipo_prop_rec_pessoa = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_tipo",
            field_name="valida_tipo_prop_rec_pessoa",
            session=app.db.session,
        )
    )
    valida_tipo_prop_rec_pessoa_obj = fields_Type_Obj_Sql(
        field_choice="valida_tipo_prop_rec_pessoa",
        table_name="ope_centro2_ord_tipo",
        field_name="valida_tipo_prop_rec_pessoa",
        session=app.db.session,
    )


# ==========================================================


class OpeCentroSubtipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroSubtipo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    nome = fields.Str(required=True)
    tipo_destinacao = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro_subtipo",
            field_name="tipo_destinacao",
            session=app.db.session,
        )
    )
    tipo_destinacao_obj = fields_Type_Obj_Sql(
        field_choice="tipo_destinacao",
        table_name="ope_centro_subtipo",
        field_name="tipo_destinacao",
        session=app.db.session,
    )

    ope_centro_tipo_id = fields.Str(required=True)
    ope_centro_tipo_id_obj = fields.Nested("OpeCentroTipoSchema", dump_only=True)
    sigla_centro_subtipo = fields.Str(required=True)


# ==========================================================


class OpeCentroVersaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroVersao
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
    data_per_ini = fields.Str(required=True)
    data_per_fin = fields.Str(required=True)

    tipo_per = fields.Str(
        load_default="D",
        validate=valid_type_choice_sql(
            table_name="ope_centro_versao",
            field_name="tipo_per",
            session=app.db.session,
        ),
    )
    tipo_per_obj = fields_Type_Obj_Sql(
        field_choice="tipo_per",
        table_name="ope_centro_versao",
        field_name="tipo_per",
        session=app.db.session,
    )


# ==========================================================


class OpeCicloVarSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCicloVar
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

    sigla_ope_ciclo_var = fields.Str(required=True)


# ==========================================================


class OpeCompartGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCompartGrupo
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

    sigla_compart_grupo = fields.Str(required=True)


# ==========================================================


class OpeCompartMedidaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCompartMedida
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

    sigla_compart_medida = fields.Str(required=True)


# ==========================================================


class OpeCompartPosicaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCompartPosicao
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

    sigla_compart_posicao = fields.Str(required=True)
    numero_eixo = fields.Number(required=True)

    posicao = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_compart_posicao",
            field_name="posicao",
            session=app.db.session,
        )
    )
    posicao_obj = fields_Type_Obj_Sql(
        field_choice="posicao",
        table_name="ope_compart_posicao",
        field_name="posicao",
        session=app.db.session,
    )

    banda_montagem = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_compart_posicao",
            field_name="banda_montagem",
            session=app.db.session,
        )
    )
    banda_montagem_obj = fields_Type_Obj_Sql(
        field_choice="banda_montagem",
        table_name="ope_compart_posicao",
        field_name="banda_montagem",
        session=app.db.session,
    )

    lado_montagem = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_compart_posicao",
            field_name="lado_montagem",
            session=app.db.session,
        )
    )
    lado_montagem_obj = fields_Type_Obj_Sql(
        field_choice="lado_montagem",
        table_name="ope_compart_posicao",
        field_name="lado_montagem",
        session=app.db.session,
    )


# ==========================================================


class OpeCompartStatusSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCompartStatus
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
    sigla_compart_status = fields.Str(required=True)

    tipo_status = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_compart_status",
            field_name="tipo_status",
            session=app.db.session,
        )
    )
    tipo_status_obj = fields_Type_Obj_Sql(
        field_choice="tipo_status",
        table_name="ope_compart_status",
        field_name="tipo_status",
        session=app.db.session,
    )


# ==========================================================


class OpeEspacSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeEspac
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

    sigla_espac = fields.Str(required=True)


# ==========================================================


class OpeEstagioSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeEstagio
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

    sigla_estagio = fields.Str(required=True)


# ==========================================================


class OpeOcorGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeOcorGrupo
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

    sigla_ocor_grupo = fields.Str(required=True)


# ==========================================================


class OpeOcorStatusSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeOcorStatus
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
    sigla_ocor_status = fields.Str(required=True)

    tipo_status = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_ocor_status",
            field_name="tipo_status",
            session=app.db.session,
        )
    )
    tipo_status_obj = fields_Type_Obj_Sql(
        field_choice="tipo_status",
        table_name="ope_ocor_status",
        field_name="tipo_status",
        session=app.db.session,
    )


# ==========================================================


class OpeOcorTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeOcorTipo
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

    sigla_ocor_tipo = fields.Str(required=True)

    tipo = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_ocor_tipo", field_name="tipo", session=app.db.session
        )
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="ope_ocor_tipo",
        field_name="tipo",
        session=app.db.session,
    )

    obrig_ope_compart = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_ocor_tipo",
            field_name="obrig_ope_compart",
            session=app.db.session,
        )
    )
    obrig_ope_compart_obj = fields_Type_Obj_Sql(
        field_choice="obrig_ope_compart",
        table_name="ope_ocor_tipo",
        field_name="obrig_ope_compart",
        session=app.db.session,
    )


# ==========================================================


class OpePeriodoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpePeriodo
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

    sigla_periodo = fields.Str(required=True)
    data_ini = fields.Str(required=True)
    data_fin = fields.Str(required=True)


# ==========================================================


class OpeRegiaoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeRegiao
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

    sigla_regiao = fields.Str(required=True)


# ==========================================================


class OpeTipoSoloSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeTipoSolo
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

    sigla_tipo_solo = fields.Str(required=True)


# ==========================================================


class OpeUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)


# ==========================================================


class OpeAtividadeSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeAtividade
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

    sigla_atividade = fields.Str(required=True)
    parada = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    parada_obj = fields_Type_Obj_Sql(
        field_choice="parada",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    index_bor = fields.Str(required=True)
    largura = fields.Number(required=True)

    valida_seq_medicao_trab_centro = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_seq_medicao_trab_centro",
            session=app.db.session,
        )
    )
    valida_seq_medicao_trab_centro_obj = fields_Type_Obj_Sql(
        field_choice="valida_seq_medicao_trab_centro",
        table_name="ope_atividade",
        field_name="valida_seq_medicao_trab_centro",
        session=app.db.session,
    )

    valida_saldo_area_aberta = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_saldo_area_aberta",
            session=app.db.session,
        )
    )
    valida_saldo_area_aberta_obj = fields_Type_Obj_Sql(
        field_choice="valida_saldo_area_aberta",
        table_name="ope_atividade",
        field_name="valida_saldo_area_aberta",
        session=app.db.session,
    )

    valida_prev_itemserv = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_prev_itemserv",
            session=app.db.session,
        )
    )
    valida_prev_itemserv_obj = fields_Type_Obj_Sql(
        field_choice="valida_prev_itemserv",
        table_name="ope_atividade",
        field_name="valida_prev_itemserv",
        session=app.db.session,
    )

    valida_prev_rec = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_prev_rec",
            session=app.db.session,
        )
    )
    valida_prev_rec_obj = fields_Type_Obj_Sql(
        field_choice="valida_prev_rec",
        table_name="ope_atividade",
        field_name="valida_prev_rec",
        session=app.db.session,
    )

    valida_regra_config = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_regra_config",
            session=app.db.session,
        )
    )
    valida_regra_config_obj = fields_Type_Obj_Sql(
        field_choice="valida_regra_config",
        table_name="ope_atividade",
        field_name="valida_regra_config",
        session=app.db.session,
    )

    valida_tipo_executor = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_tipo_executor",
            session=app.db.session,
        )
    )
    valida_tipo_executor_obj = fields_Type_Obj_Sql(
        field_choice="valida_tipo_executor",
        table_name="ope_atividade",
        field_name="valida_tipo_executor",
        session=app.db.session,
    )

    valida_rec_equip = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_rec_equip",
            session=app.db.session,
        )
    )
    valida_rec_equip_obj = fields_Type_Obj_Sql(
        field_choice="valida_rec_equip",
        table_name="ope_atividade",
        field_name="valida_rec_equip",
        session=app.db.session,
    )

    valida_rec_pessoa = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_rec_pessoa",
            session=app.db.session,
        )
    )
    valida_rec_pessoa_obj = fields_Type_Obj_Sql(
        field_choice="valida_rec_pessoa",
        table_name="ope_atividade",
        field_name="valida_rec_pessoa",
        session=app.db.session,
    )

    valida_itemserv_i = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_itemserv_i",
            session=app.db.session,
        )
    )
    valida_itemserv_i_obj = fields_Type_Obj_Sql(
        field_choice="valida_itemserv_i",
        table_name="ope_atividade",
        field_name="valida_itemserv_i",
        session=app.db.session,
    )

    valida_itemserv_s = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_itemserv_s",
            session=app.db.session,
        )
    )
    valida_itemserv_s_obj = fields_Type_Obj_Sql(
        field_choice="valida_itemserv_s",
        table_name="ope_atividade",
        field_name="valida_itemserv_s",
        session=app.db.session,
    )

    valida_tipo_prop_rec_equip = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_tipo_prop_rec_equip",
            session=app.db.session,
        )
    )
    valida_tipo_prop_rec_equip_obj = fields_Type_Obj_Sql(
        field_choice="valida_tipo_prop_rec_equip",
        table_name="ope_atividade",
        field_name="valida_tipo_prop_rec_equip",
        session=app.db.session,
    )

    valida_tipo_prop_rec_pessoa = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_tipo_prop_rec_pessoa",
            session=app.db.session,
        )
    )
    valida_tipo_prop_rec_pessoa_obj = fields_Type_Obj_Sql(
        field_choice="valida_tipo_prop_rec_pessoa",
        table_name="ope_atividade",
        field_name="valida_tipo_prop_rec_pessoa",
        session=app.db.session,
    )

    valida_tot_area_acum_per_centro_plan = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_tot_area_acum_per_centro_plan",
            session=app.db.session,
        )
    )
    valida_tot_area_acum_per_centro_plan_obj = fields_Type_Obj_Sql(
        field_choice="valida_tot_area_acum_per_centro_plan",
        table_name="ope_atividade",
        field_name="valida_tot_area_acum_per_centro_plan",
        session=app.db.session,
    )

    valida_tot_area_acum_per_centro_exec = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_tot_area_acum_per_centro_exec",
            session=app.db.session,
        )
    )
    valida_tot_area_acum_per_centro_exec_obj = fields_Type_Obj_Sql(
        field_choice="valida_tot_area_acum_per_centro_exec",
        table_name="ope_atividade",
        field_name="valida_tot_area_acum_per_centro_exec",
        session=app.db.session,
    )

    valida_tot_area_ord_exec = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_atividade",
            field_name="valida_tot_area_ord_exec",
            session=app.db.session,
        )
    )
    valida_tot_area_ord_exec_obj = fields_Type_Obj_Sql(
        field_choice="valida_tot_area_ord_exec",
        table_name="ope_atividade",
        field_name="valida_tot_area_ord_exec",
        session=app.db.session,
    )

    ger_umedida_id = fields.Str(required=True)
    ger_umedida_id_obj = fields.Nested("GerUmedidaSchema", dump_only=True)

    ope_atividade_grupo_id = fields.Str(required=True)
    ope_atividade_grupo_id_obj = fields.Nested(
        "OpeAtividadeGrupoSchema", dump_only=True
    )

    ope_atividade_prod_childs = fields.Nested("OpeAtividadeProdSchema", many=True)


# ==========================================================


class OpeCentroGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroGrupo
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

    ope_centro_subtipo_id = fields.Str(required=True)
    ope_centro_subtipo_id_obj = fields.Nested("OpeCentroSubtipoSchema", dump_only=True)


# ==========================================================


class OpeCentroRatTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroRatTipo
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

    tipo_ps = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro_rat_tipo",
            field_name="tipo_ps",
            session=app.db.session,
        )
    )
    tipo_ps_obj = fields_Type_Obj_Sql(
        field_choice="tipo_ps",
        table_name="ope_centro_rat_tipo",
        field_name="tipo_ps",
        session=app.db.session,
    )

    tipo_apur = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro_rat_tipo",
            field_name="tipo_apur",
            session=app.db.session,
        )
    )
    tipo_apur_obj = fields_Type_Obj_Sql(
        field_choice="tipo_apur",
        table_name="ope_centro_rat_tipo",
        field_name="tipo_apur",
        session=app.db.session,
    )
    observacao = fields.Str(required=True)
    sigla_centro_rat_tipo = fields.Str(required=True)
    ope_centro_versao_id = fields.Str(required=True)
    ope_centro_versao_id_obj = fields.Nested("OpeCentroVersaoSchema", dump_only=True)

    ope_centro_rat_periodo_childs = fields.Nested(
        "OpeCentroRatPeriodoSchema", many=True
    )


# ==========================================================


class OpeCompartOcorSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCompartOcor
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

    sigla_compart_ocor = fields.Str(required=True)

    tipo_ocor = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_compart_ocor",
            field_name="tipo_ocor",
            session=app.db.session,
        )
    )
    tipo_ocor_obj = fields_Type_Obj_Sql(
        field_choice="tipo_ocor",
        table_name="ope_compart_ocor",
        field_name="tipo_ocor",
        session=app.db.session,
    )

    ope_compart_status_id = fields.Str(required=True)
    ope_compart_status_id_obj = fields.Nested("OpeCompartStatusSchema", dump_only=True)


# ==========================================================


class OpeCompartSubgrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCompartSubgrupo
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

    sigla_compart_subgrupo = fields.Str(required=True)

    ope_compart_grupo_id = fields.Str(required=True)
    ope_compart_grupo_id_obj = fields.Nested("OpeCompartGrupoSchema", dump_only=True)


# ==========================================================


class OpeCompartTipoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCompartTipo
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

    sigla_compart_tipo = fields.Str(required=True)

    tipo_compart = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_compart_tipo",
            field_name="tipo_compart",
            session=app.db.session,
        )
    )
    tipo_compart_obj = fields_Type_Obj_Sql(
        field_choice="tipo_compart",
        table_name="ope_compart_tipo",
        field_name="tipo_compart",
        session=app.db.session,
    )

    qnt_lonas = fields.Number(required=True)
    qnt_sulco_min = fields.Number(required=True)
    qnt_sulco_max = fields.Number(required=True)

    ope_compart_medida_id = fields.Str(required=True)
    ope_compart_medida_id_obj = fields.Nested("OpeCompartMedidaSchema", dump_only=True)


# ==========================================================


class OpeOcorSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeOcor
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

    sigla_ocor = fields.Str(required=True)
    icon = fields.Str(required=True)

    tipo = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_ocor", field_name="tipo", session=app.db.session
        )
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="ope_ocor",
        field_name="tipo",
        session=app.db.session,
    )

    tipo_lanc = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_ocor", field_name="tipo_lanc", session=app.db.session
        )
    )
    tipo_lanc_obj = fields_Type_Obj_Sql(
        field_choice="tipo_lanc",
        table_name="ope_ocor",
        field_name="tipo_lanc",
        session=app.db.session,
    )

    ger_umedida_id = fields.Str(required=True)
    ger_umedida_id_obj = fields.Nested("GerUmedidaSchema", dump_only=True)

    ope_ocor_grupo_id = fields.Str(required=True)
    ope_ocor_grupo_id_obj = fields.Nested("OpeOcorGrupoSchema", dump_only=True)


# ==========================================================


class OpeAtividadeProdSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeAtividadeProd
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ordem_visual = fields.Str(required=True)

    ope_atividade_id_prod = fields.Str(required=True)
    ope_atividade_id_prod_obj = fields.Nested("OpeAtividadeSchema", dump_only=True)


# ==========================================================


class OpeCentro1Schema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro1
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

    sigla_centro1 = fields.Str(required=True)
    observacao = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    ctb_comp_id = fields.Str(required=True)
    ctb_comp_id_obj = fields.Nested("CtbCompSchema", dump_only=True)

    ger_pessoa_id = fields.Str(required=True)
    ger_pessoa_id_obj = fields.Nested("GerPessoaSchema", dump_only=True)

    ope_centro_subtipo_id = fields.Str(required=True)
    ope_centro_subtipo_id_obj = fields.Nested("OpeCentroSubtipoSchema", dump_only=True)


# ==========================================================


class OpeCentroRatPeriodoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroRatPeriodo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_ini = fields.Str(required=True)

    tipo_rp = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro_rat_periodo",
            field_name="tipo_rp",
            session=app.db.session,
        )
    )
    tipo_rp_obj = fields_Type_Obj_Sql(
        field_choice="tipo_rp",
        table_name="ope_centro_rat_periodo",
        field_name="tipo_rp",
        session=app.db.session,
    )

    ope_centro_rat_fator_childs = fields.Nested("OpeCentroRatFatorSchema", many=True)


# ==========================================================


class OpeCentroRendSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroRend
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

    ope_atividade_id = fields.Str(required=True)
    ope_atividade_id_obj = fields.Nested("OpeAtividadeSchema", dump_only=True)

    ope_centro_versao_id = fields.Str(required=True)
    ope_centro_versao_id_obj = fields.Nested("OpeCentroVersaoSchema", dump_only=True)

    ope_centro_rend_fator_childs = fields.Nested("OpeCentroRendFatorSchema", many=True)


# ==========================================================


class OpeCentroSubgrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroSubgrupo
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

    sigla_centro_subgrupo = fields.Str(required=True)
    icon = fields.Str(required=True)

    ctb_comp_id = fields.Str(required=True)
    ctb_comp_id_obj = fields.Nested("CtbCompSchema", dump_only=True)

    ope_centro_grupo_id = fields.Str(required=True)
    ope_centro_grupo_id_obj = fields.Nested("OpeCentroGrupoSchema", dump_only=True)


# ==========================================================


class OpeCompartSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCompart
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

    sigla_compart = fields.Str(required=True)
    capacidade = fields.Number(required=True)

    valida_itemserv = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    valida_itemserv_obj = fields_Type_Obj_Sql(
        field_choice="valida_itemserv",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    medicao_trab_centro = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_compart",
            field_name="medicao_trab_centro",
            session=app.db.session,
        )
    )
    medicao_trab_centro_obj = fields_Type_Obj_Sql(
        field_choice="medicao_trab_centro",
        table_name="ope_compart",
        field_name="medicao_trab_centro",
        session=app.db.session,
    )

    data_aquisicao = fields.Str(required=True)
    data_baixa = fields.Str(required=True)
    data_status = fields.Str(required=True)
    observacao = fields.Str(required=True)
    valor_aquisicao = fields.Number(required=True)
    numero_serie = fields.Str(required=True)

    ope_compart_status_id = fields.Str(required=True)
    ope_compart_status_id_obj = fields.Nested("OpeCompartStatusSchema", dump_only=True)

    ope_compart_subgrupo_id = fields.Str(required=True)
    ope_compart_subgrupo_id_obj = fields.Nested(
        "OpeCompartSubgrupoSchema", dump_only=True
    )


# ==========================================================


class OpeCentro2Schema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2
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

    sigla_centro2 = fields.Str(required=True)

    utiliza_compart = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    utiliza_compart_obj = fields_Type_Obj_Sql(
        field_choice="utiliza_compart",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    observacao = fields.Str(required=True)

    tipo_prop = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2", field_name="tipo_prop", session=app.db.session
        )
    )
    tipo_prop_obj = fields_Type_Obj_Sql(
        field_choice="tipo_prop",
        table_name="ope_centro2",
        field_name="tipo_prop",
        session=app.db.session,
    )

    tipo_destinacao = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2",
            field_name="tipo_destinacao",
            session=app.db.session,
        )
    )
    tipo_destinacao_obj = fields_Type_Obj_Sql(
        field_choice="tipo_destinacao",
        table_name="ope_centro2",
        field_name="tipo_destinacao",
        session=app.db.session,
    )

    tipo_ctb_comp = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2", field_name="tipo_ctb_comp", session=app.db.session
        )
    )
    tipo_ctb_comp_obj = fields_Type_Obj_Sql(
        field_choice="tipo_ctb_comp",
        table_name="ope_centro2",
        field_name="tipo_ctb_comp",
        session=app.db.session,
    )

    medicao_trab_centro = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2",
            field_name="medicao_trab_centro",
            session=app.db.session,
        )
    )
    medicao_trab_centro_obj = fields_Type_Obj_Sql(
        field_choice="medicao_trab_centro",
        table_name="ope_centro2",
        field_name="medicao_trab_centro",
        session=app.db.session,
    )

    valida_seq_medicao_trab_centro = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2",
            field_name="valida_seq_medicao_trab_centro",
            session=app.db.session,
        )
    )
    valida_seq_medicao_trab_centro_obj = fields_Type_Obj_Sql(
        field_choice="valida_seq_medicao_trab_centro",
        table_name="ope_centro2",
        field_name="valida_seq_medicao_trab_centro",
        session=app.db.session,
    )

    data_valid = fields.Str(required=True)

    ctb_comp_id = fields.Str(required=True)
    ctb_comp_id_obj = fields.Nested("CtbCompSchema", dump_only=True)

    ger_marca_modelo_id = fields.Str(required=True)
    ger_marca_modelo_id_obj = fields.Nested("GerMarcaModeloSchema", dump_only=True)

    ger_pessoa_endereco_id = fields.Str(required=True)
    ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ger_umedida_id = fields.Str(required=True)
    ger_umedida_id_obj = fields.Nested("GerUmedidaSchema", dump_only=True)

    ope_centro1_id = fields.Str(required=True)
    ope_centro1_id_obj = fields.Nested("OpeCentro1Schema", dump_only=True)

    ope_centro_rat_tipo_id = fields.Str(required=True)
    ope_centro_rat_tipo_id_obj = fields.Nested("OpeCentroRatTipoSchema", dump_only=True)

    ope_centro_subgrupo_id = fields.Str(required=True)
    ope_centro_subgrupo_id_obj = fields.Nested(
        "OpeCentroSubgrupoSchema", dump_only=True
    )

    ope_regiao_id = fields.Str(required=True)
    ope_regiao_id_obj = fields.Nested("OpeRegiaoSchema", dump_only=True)


# ==========================================================


class OpeCompartItemservSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCompartItemserv
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
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

    ger_itemserv_id = fields.Str(required=True)

    ope_compart_id = fields.Str(required=True)
    ope_compart_id_obj = fields.Nested("OpeCompartSchema", dump_only=True)


# ==========================================================


class OpeFrenteTrabalhoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeFrenteTrabalho
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

    sigla_frente_trabalho = fields.Str(required=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)


# ==========================================================


class OpeOcorCompartMovSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeOcorCompartMov
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    observacao = fields.Str(required=True)
    data_mov = fields.Str(required=True)
    numero = fields.Str(required=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)

    ger_pessoa_endereco_id_exec = fields.Str(required=True)
    ger_pessoa_endereco_id_exec_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ope_ocor_compart_mov_det_childs = fields.Nested(
        "OpeOcorCompartMovDetSchema", many=True
    )


# ==========================================================


class OpeOcorMovSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeOcorMov
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    observacao = fields.Str(required=True)
    data_mov = fields.Str(required=True)
    numero = fields.Str(required=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)

    ger_pessoa_endereco_id_exec = fields.Str(required=True)
    ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ope_ocor_tipo_id = fields.Str(required=True)
    ope_ocor_tipo_id_obj = fields.Nested("OpeOcorTipoSchema", dump_only=True)

    ope_ocor_mov_dest_childs = fields.Nested("OpeOcorMovDestSchema", many=True)
    ope_ocor_mov_det_childs = fields.Nested("OpeOcorMovDetSchema", many=True)


# ==========================================================


class OpeCentro2AreaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2Area
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

    qnt_area_prod = fields.Str(required=True)
    qnt_area_improd = fields.Str(required=True)
    qnt_plantas_estande = fields.Str(required=True)
    bloco_col = fields.Str(required=True)
    observacao = fields.Str(required=True)
    lat_x = fields.Str(required=True)
    long_y = fields.Str(required=True)
    alt_z = fields.Str(required=True)
    data_ini_plan = fields.Str(required=True)
    data_fin_plan = fields.Str(required=True)
    data_ult_plan = fields.Str(required=True)
    data_ini_col = fields.Str(required=True)
    data_fin_col = fields.Str(required=True)
    data_ult_col = fields.Str(required=True)
    data_emerg = fields.Str(required=True)
    data_florada_1 = fields.Str(required=True)

    ger_itemserv_id = fields.Str(required=True)
    ger_itemserv_id_obj = fields.Nested("GerItemservSchema", dump_only=True)

    ger_itemserv_id_ult = fields.Str(required=True)
    ger_itemserv1_id_obj = fields.Nested("GerItemservSchema", dump_only=True)

    ger_itemserv_var_id = fields.Str(required=True)
    ger_itemserv_var_id_obj = fields.Nested("GerItemservVarSchema", dump_only=True)

    ger_itemserv_var_id_ult = fields.Str(required=True)
    ger_itemserv_var1_id_obj = fields.Nested("GerItemservVarSchema", dump_only=True)

    ger_umedida_id = fields.Str(required=True)
    ger_umedida_id_obj = fields.Nested("GerUmedidaSchema", dump_only=True)

    ope_atividade_sistema_id_col = fields.Str(required=True)
    ope_atividade_sistema_id_obj = fields.Nested(
        "OpeAtividadeSistemaSchema", dump_only=True
    )

    ope_atividade_sistema_id_cult = fields.Str(required=True)
    ope_atividade_sistema1_id_obj = fields.Nested(
        "OpeAtividadeSistemaSchema", dump_only=True
    )

    ope_atividade_sistema_id_plan = fields.Str(required=True)
    ope_atividade_sistema2_id_obj = fields.Nested(
        "OpeAtividadeSistemaSchema", dump_only=True
    )

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_espac_id = fields.Str(required=True)
    ope_espac_id_obj = fields.Nested("OpeEspacSchema", dump_only=True)

    ope_estagio_id = fields.Str(required=True)
    ope_estagio_id_obj = fields.Nested("OpeEstagioSchema", dump_only=True)

    ope_periodo_id = fields.Str(required=True)
    ope_periodo_id_obj = fields.Nested("OpePeriodoSchema", dump_only=True)

    ope_tipo_solo_id = fields.Str(required=True)
    ope_tipo_solo_id_obj = fields.Nested("OpeTipoSoloSchema", dump_only=True)

    ope_centro2_mapa_coord_childs = fields.Nested(
        "OpeCentro2MapaCoordSchema", many=True
    )


# ==========================================================


class OpeCentro2EquipSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2Equip
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    tipo_rodado = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_equip",
            field_name="tipo_rodado",
            session=app.db.session,
        )
    )
    tipo_rodado_obj = fields_Type_Obj_Sql(
        field_choice="tipo_rodado",
        table_name="ope_centro2_equip",
        field_name="tipo_rodado",
        session=app.db.session,
    )

    tipo_carroceria = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_equip",
            field_name="tipo_carroceria",
            session=app.db.session,
        )
    )
    tipo_carroceria_obj = fields_Type_Obj_Sql(
        field_choice="tipo_carroceria",
        table_name="ope_centro2_equip",
        field_name="tipo_carroceria",
        session=app.db.session,
    )

    placa = fields.Str(required=True)
    renavam = fields.Str(required=True)
    tara = fields.Str(required=True)
    capacidade_kg = fields.Str(required=True)
    capacidade_m3 = fields.Str(required=True)
    potencia = fields.Str(required=True)
    nr_chassi = fields.Str(required=True)
    nr_serie = fields.Str(required=True)

    liberado_abastec = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    liberado_abastec_obj = fields_Type_Obj_Sql(
        field_choice="liberado_abastec",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    largura = fields.Str(required=True)

    altura = fields.Str(required=True)
    nr_registro_estadual = fields.Str(required=True)

    tipo_tracao = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_equip",
            field_name="tipo_tracao",
            session=app.db.session,
        )
    )
    tipo_tracao_obj = fields_Type_Obj_Sql(
        field_choice="tipo_tracao",
        table_name="ope_centro2_equip",
        field_name="tipo_tracao",
        session=app.db.session,
    )

    tipo_transp_auto_carga = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_equip",
            field_name="tipo_transp_auto_carga",
            session=app.db.session,
        )
    )
    tipo_transp_auto_carga_obj = fields_Type_Obj_Sql(
        field_choice="tipo_transp_auto_carga",
        table_name="ope_centro2_equip",
        field_name="tipo_transp_auto_carga",
        session=app.db.session,
    )

    data_venc_licenciamento = fields.Str(required=True)
    data_venc_imposto = fields.Str(required=True)

    ger_cidade_id = fields.Str(required=True)
    ger_cidade_id_obj = fields.Nested("GerCidadeSchema", dump_only=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_frente_trabalho_id = fields.Str(required=True)
    ope_frente_trabalho_id_obj = fields.Nested(
        "OpeFrenteTrabalhoSchema", dump_only=True
    )


# ==========================================================


class OpeCentro2EstoqueSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2Estoque
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    tipo = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_estoque", field_name="tipo", session=app.db.session
        )
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="ope_centro2_estoque",
        field_name="tipo",
        session=app.db.session,
    )

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)


# ==========================================================


class OpeCentro2MovMediaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2MovMedia
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    observacao = fields.Str(required=True)
    qnt_media_min = fields.Str(required=True)
    qnt_media_max = fields.Str(required=True)
    capacidade = fields.Str(required=True)
    dt_valid_ini = fields.Str(required=True)

    ger_itemserv_id = fields.Str(required=True)
    ger_itemserv_id_obj = fields.Nested("GerItemservSchema", dump_only=True)

    ger_marca_modelo_id = fields.Str(required=True)
    ger_marca_modelo_id_obj = fields.Nested("GerMarcaModeloSchema", dump_only=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_compart_id = fields.Str(required=True)
    ope_compart_id_obj = fields.Nested("OpeCompartSchema", dump_only=True)


# ==========================================================


class OpeCentro2ParamPerSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2ParamPer
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    dt_valid_ini = fields.Str(required=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)

    ope_frente_trabalho_id = fields.Str(required=True)
    ope_frente_trabalho_id_obj = fields.Nested(
        "OpeFrenteTrabalhoSchema", dump_only=True
    )


# ==========================================================


class OpeCentro2PessoaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2Pessoa
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    pto_idenf_tipo = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_pessoa",
            field_name="pto_idenf_tipo",
            session=app.db.session,
        )
    )
    pto_idenf_tipo_obj = fields_Type_Obj_Sql(
        field_choice="pto_idenf_tipo",
        table_name="ope_centro2_pessoa",
        field_name="pto_idenf_tipo",
        session=app.db.session,
    )

    pto_idenf = fields.Str(required=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_frente_trabalho_id = fields.Str(required=True)
    ope_frente_trabalho_id_obj = fields.Nested(
        "OpeFrenteTrabalhoSchema", dump_only=True
    )


# ==========================================================


class OpeCentroConfigSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroConfig
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    tipo_regra = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro_config",
            field_name="tipo_regra",
            session=app.db.session,
        )
    )
    tipo_regra_obj = fields_Type_Obj_Sql(
        field_choice="tipo_regra",
        table_name="ope_centro_config",
        field_name="tipo_regra",
        session=app.db.session,
    )

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

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)

    ger_itemserv_grupo_id = fields.Str(required=True)
    ger_itemserv_grupo_id_obj = fields.Nested("GerItemservGrupoSchema", dump_only=True)

    ger_itemserv_id = fields.Str(required=True)
    ger_itemserv_id_obj = fields.Nested("GerItemservSchema", dump_only=True)

    ger_itemserv_subgrupo_id = fields.Str(required=True)
    ger_itemserv_subgrupo_id_obj = fields.Nested(
        "GerItemservSubGrupoSchema", dump_only=True
    )

    mov_operacao_id = fields.Str(required=True)
    mov_operacao_id_obj = fields.Nested("MovOperacaoSchema", dump_only=True)

    ope_atividade_id_obj = fields.Nested("OpeAtividadeSchema", dump_only=True)
    ope_atividade_id = fields.Str(required=True)

    ope_centro1_id = fields.Str(required=True)
    ope_centro1_id_obj = fields.Nested("OpeCentro1Schema", dump_only=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_centro2_ord_tipo_id = fields.Str(required=True)
    ope_centro2_ord_tipo_id_obj = fields.Nested(
        "OpeCentro2OrdTipoSchema", dump_only=True
    )

    ope_centro_grupo_id = fields.Str(required=True)
    ope_centro_grupo_id_obj = fields.Nested("OpeCentroGrupoSchema", dump_only=True)

    ope_centro_subgrupo_id = fields.Str(required=True)
    ope_centro_subgrupo_id_obj = fields.Nested(
        "OpeCentroSubgrupoSchema", dump_only=True
    )

    ope_centro_subtipo_id = fields.Str(required=True)
    ope_centro_subtipo_id_obj = fields.Nested("OpeCentroSubtipoSchema", dump_only=True)

    ope_centro_tipo_id = fields.Str(required=True)
    ope_centro_tipo_id_obj = fields.Nested("OpeCentroTipoSchema", dump_only=True)

    ope_compart_grupo_id = fields.Str(required=True)
    ope_compart_grupo_id_obj = fields.Nested("OpeCompartGrupoSchema", dump_only=True)

    ope_compart_id = fields.Str(required=True)
    ope_compart_id_obj = fields.Nested("OpeCompartSchema", dump_only=True)

    ope_compart_subgrupo_id = fields.Str(required=True)
    ope_compart_subgrupo_id_obj = fields.Nested(
        "OpeCompartSubgrupoSchema", dump_only=True
    )

    ope_estagio_id = fields.Str(required=True)
    ope_estagio_id_obj = fields.Nested("OpeEstagioSchema", dump_only=True)


# ==========================================================


class OpeCentroPrevSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroPrev
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    qnt01 = fields.Str(required=True)
    qnt02 = fields.Str(required=True)
    qnt03 = fields.Str(required=True)
    qnt04 = fields.Str(required=True)
    qnt05 = fields.Str(required=True)
    qnt06 = fields.Str(required=True)
    qnt07 = fields.Str(required=True)
    qnt08 = fields.Str(required=True)
    qnt09 = fields.Str(required=True)
    qnt10 = fields.Str(required=True)
    qnt11 = fields.Str(required=True)
    qnt12 = fields.Str(required=True)
    qnt13 = fields.Str(required=True)
    qnt14 = fields.Str(required=True)
    qnt15 = fields.Str(required=True)
    qnt16 = fields.Str(required=True)
    qnt17 = fields.Str(required=True)
    qnt18 = fields.Str(required=True)
    qnt19 = fields.Str(required=True)
    qnt20 = fields.Str(required=True)
    qnt21 = fields.Str(required=True)
    qnt22 = fields.Str(required=True)
    qnt23 = fields.Str(required=True)
    qnt24 = fields.Str(required=True)
    qnt25 = fields.Str(required=True)
    qnt26 = fields.Str(required=True)
    qnt27 = fields.Str(required=True)
    qnt28 = fields.Str(required=True)
    qnt29 = fields.Str(required=True)
    qnt30 = fields.Str(required=True)
    qnt31 = fields.Str(required=True)
    ordem_exec = fields.Str(required=True)

    tipo_executor = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro_prev",
            field_name="tipo_executor",
            session=app.db.session,
        )
    )
    tipo_executor_obj = fields_Type_Obj_Sql(
        field_choice="tipo_executor",
        table_name="ope_centro_prev",
        field_name="tipo_executor",
        session=app.db.session,
    )

    data_per = fields.Str(required=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)

    ope_atividade_id = fields.Str(required=True)
    ope_atividade_id_obj = fields.Nested("OpeAtividadeSchema", dump_only=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_centro2_ord_tipo_id = fields.Str(required=True)
    ope_centro2_ord_tipo_id_obj = fields.Nested(
        "OpeCentro2OrdTipoSchema", dump_only=True
    )

    ope_centro_versao_id = fields.Str(required=True)
    ope_centro_versao_id_obj = fields.Nested("OpeCentroVersaoSchema", dump_only=True)

    ope_periodo_id = fields.Str(required=True)
    ope_periodo_id_obj = fields.Nested("OpePeriodoSchema", dump_only=True)

    process_id = fields.Str(required=True)
    process_id_obj = fields.Nested("SysProcessLogSchema", dump_only=True)

    ope_centro_prev_dest_childs = fields.Nested("OpeCentroPrevDestSchema", many=True)


# ==========================================================


class OpeCentroRatFatorSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroRatFator
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    fator_rat = fields.Str(required=True)
    perc_rat = fields.Str(required=True)

    ctb_centro_id = fields.Str(required=True)
    ctb_centro_id_obj = fields.Nested("CtbCentroSchema", dump_only=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)

    ope_centro1_id = fields.Str(required=True)
    ope_centro1_id_obj = fields.Nested("OpeCentro1Schema", dump_only=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_centro_subtipo_id = fields.Str(required=True)
    ope_centro_subtipo_id_obj = fields.Nested("OpeCentroSubtipoSchema", dump_only=True)

    ope_periodo_id = fields.Str(required=True)
    ope_periodo_id_obj = fields.Nested("OpePeriodoSchema", dump_only=True)


# ==========================================================


class OpeCentroRendFatorSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroRendFator
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    fator_rend = fields.Str(required=True)
    fator_util = fields.Str(required=True)

    ctb_comp_id = fields.Str(required=True)
    ctb_comp_id_obj = fields.Nested("CtbCompSchema", dump_only=True)

    ger_itemserv_id = fields.Str(required=True)
    ger_itemserv_id_obj = fields.Nested("GerItemservSchema", dump_only=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)


# ==========================================================


class OpeOcorCompartMovDetSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeOcorCompartMovDet
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    observacao = fields.Str(required=True)
    qnt_medicao = fields.Str(required=True)

    ope_compart_id = fields.Str(required=True)
    ope_compart_id_obj = fields.Nested("OpeCompartSchema", dump_only=True)

    ope_compart_ocor_id = fields.Str(required=True)
    ope_compart_ocor_id_obj = fields.Nested("OpeCompartOcorSchema", dump_only=True)


# ==========================================================


class OpeOcorMovDestSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeOcorMovDest
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    observacao = fields.Str(required=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_compart_id = fields.Str(required=True)
    ope_compart_id_obj = fields.Nested("OpeCompartSchema", dump_only=True)


# ==========================================================


class OpeOcorPrevSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeOcorPrev
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    observacao = fields.Str(required=True)
    data_ult_solucao = fields.Str(required=True)
    qnt_limite = fields.Str(required=True)
    qnt_aviso = fields.Str(required=True)
    qnt_dia_limite = fields.Str(required=True)
    qnt_dia_aviso = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_compart_id = fields.Str(required=True)
    ope_compart_id_obj = fields.Nested("OpeCompartSchema", dump_only=True)

    ope_ocor_id = fields.Str(required=True)
    ope_ocor_id_obj = fields.Nested("OpeOcorSchema", dump_only=True)


# ==========================================================


class OpeCentro2MapaCoordSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2MapaCoord
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    lat_x = fields.Str(required=True)
    long_y = fields.Str(required=True)
    ordem = fields.Str(required=True)


# ==========================================================


class OpeCentro2MapaGeometriaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2MapaGeometria
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    geom = fields.Str(required=True)

    ope_centro2_id_area = fields.Str(required=True)
    ope_centro2_area_id_obj = fields.Nested("OpeCentro2AreaSchema", dump_only=True)


# ==========================================================


class OpeCentro2OrdSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2Ord
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_ini_exec = fields.Str(required=True)
    data_fin_exec = fields.Str(required=True)
    data_status = fields.Str(required=True)
    observacao_interna = fields.Str(required=True)
    observacao_externa = fields.Str(required=True)
    data_ini_exec_prev = fields.Str(required=True)
    data_fin_exec_prev = fields.Str(required=True)
    numero_ord = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    ger_empresa_id = fields.Str(required=True)
    ger_empresa_id_obj = fields.Nested("GerEmpresaSchema", dump_only=True)

    ger_pessoa_endereco_id_exec = fields.Str(required=True)
    ger_pessoa_endereco_id_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_centro2_ord_status_id = fields.Str(required=True)
    ope_centro2_ord_status_id_obj = fields.Nested(
        "OpeCentro2OrdStatusSchema", dump_only=True
    )

    ope_centro2_ord_tipo_id = fields.Str(required=True)
    ope_centro2_ord_tipo_id_obj = fields.Nested(
        "OpeCentro2OrdTipoSchema", dump_only=True
    )

    ope_centro2_pessoa_id_solic = fields.Str(required=True)
    ope_centro2_pessoa_id_obj = fields.Nested("OpeCentro2PessoaSchema", dump_only=True)

    ope_centro_versao_id = fields.Str(required=True)
    ope_centro_versao_id_obj = fields.Nested("OpeCentroVersaoSchema", dump_only=True)

    ope_frente_trabalho_id = fields.Str(required=True)
    ope_frente_trabalho_id_obj = fields.Nested(
        "OpeFrenteTrabalhoSchema", dump_only=True
    )

    ope_periodo_id = fields.Str(required=True)
    ope_periodo_id_obj = fields.Nested("OpePeriodoSchema", dump_only=True)

    process_id = fields.Str(required=True)
    process_id_obj = fields.Nested("SysProcessLogSchema", dump_only=True)

    ope_centro2_ord_ativ_childs = fields.Nested("OpeCentro2OrdAtivSchema", many=True)
    ope_centro2_ord_dest_childs = fields.Nested("OpeCentro2OrdDestSchema", many=True)


# ==========================================================


class OpeCentroDestSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroDest
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    valor = fields.Str(required=True)
    qnt = fields.Str(required=True)

    tipo_es = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro_dest", field_name="tipo_es", session=app.db.session
        )
    )
    tipo_es_obj = fields_Type_Obj_Sql(
        field_choice="tipo_es",
        table_name="ope_centro_dest",
        field_name="tipo_es",
        session=app.db.session,
    )

    fin_pagrec_banco_id = fields.Str(required=True)
    fin_pagrec_banco_id_obj = fields.Nested("FinPagrecBancoSchema", dump_only=True)

    fin_pagrec_id = fields.Str(required=True)
    fin_pagrec_id_obj = fields.Nested("FinPagrecSchema", dump_only=True)

    mov_itemserv_id = fields.Str(required=True)
    mov_itemserv_id_obj = fields.Nested("MovItemservSchema", dump_only=True)

    ope_atividade_id = fields.Str(required=True)
    ope_atividade_id_obj = fields.Nested("OpeAtividadeSchema", dump_only=True)

    ope_centro1_id = fields.Str(required=True)
    ope_centro1_id_obj = fields.Nested("OpeCentro1Schema", dump_only=True)

    ope_centro1_id_dest_pri = fields.Str(required=True)
    ope_centro11_id_obj = fields.Nested("OpeCentro1Schema", dump_only=True)

    ope_centro1_id_dest_sec = fields.Str(required=True)
    ope_centro12_id_obj = fields.Nested("OpeCentro1Schema", dump_only=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_centro2_id_dest_pri = fields.Str(required=True)
    ope_centro21_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_centro2_id_dest_sec = fields.Str(required=True)
    ope_centro22_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_compart_id_pri = fields.Str(required=True)
    ope_compart_id_obj = fields.Nested("OpeCompartSchema", dump_only=True)

    ope_compart_id_sec = fields.Str(required=True)
    ope_compart1_id_obj = fields.Nested("OpeCompartSchema", dump_only=True)

    ope_periodo_id_desc_pri = fields.Str(required=True)
    ope_periodo_id_obj = fields.Nested("OpePeriodoSchema", dump_only=True)

    ope_periodo_id_desc_sec = fields.Str(required=True)
    ope_periodo1_id_obj = fields.Nested("OpePeriodoSchema", dump_only=True)


# ==========================================================


class OpeCentroPrevDestSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentroPrevDest
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    qnt01 = fields.Str(required=True)
    qnt02 = fields.Str(required=True)
    qnt03 = fields.Str(required=True)
    qnt04 = fields.Str(required=True)
    qnt05 = fields.Str(required=True)
    qnt06 = fields.Str(required=True)
    qnt07 = fields.Str(required=True)
    qnt08 = fields.Str(required=True)
    qnt09 = fields.Str(required=True)
    qnt10 = fields.Str(required=True)
    qnt11 = fields.Str(required=True)
    qnt12 = fields.Str(required=True)
    qnt13 = fields.Str(required=True)
    qnt14 = fields.Str(required=True)
    qnt15 = fields.Str(required=True)
    qnt16 = fields.Str(required=True)
    qnt17 = fields.Str(required=True)
    qnt18 = fields.Str(required=True)
    qnt19 = fields.Str(required=True)
    qnt20 = fields.Str(required=True)
    qnt21 = fields.Str(required=True)
    qnt22 = fields.Str(required=True)
    qnt23 = fields.Str(required=True)
    qnt24 = fields.Str(required=True)
    qnt25 = fields.Str(required=True)
    qnt26 = fields.Str(required=True)
    qnt27 = fields.Str(required=True)
    qnt28 = fields.Str(required=True)
    qnt29 = fields.Str(required=True)
    qnt30 = fields.Str(required=True)
    qnt31 = fields.Str(required=True)

    tipo_prev = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro_prev_dest",
            field_name="tipo_prev",
            session=app.db.session,
        )
    )
    tipo_prev_obj = fields_Type_Obj_Sql(
        field_choice="tipo_prev",
        table_name="ope_centro_prev_dest",
        field_name="tipo_prev",
        session=app.db.session,
    )

    ctb_comp_id = fields.Str(required=True)
    ctb_comp_id_obj = fields.Nested("CtbCompSchema", dump_only=True)

    ger_itemserv_id = fields.Str(required=True)
    ger_itemserv_id_obj = fields.Nested("GerItemservSchema", dump_only=True)

    ope_centro1_id = fields.Str(required=True)
    ope_centro1_id_obj = fields.Nested("OpeCentro1Schema", dump_only=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    process_id = fields.Str(required=True)
    process_id_obj = fields.Nested("SysProcessLogSchema", dump_only=True)


# ==========================================================


class OpeOcorMovDetSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeOcorMovDet
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    observacao = fields.Str(required=True)
    qnt_ocor = fields.Str(required=True)
    qnt_ocor_calc = fields.Str(required=True)
    data_status = fields.Str(required=True)
    lat_x = fields.Str(required=True)
    long_y = fields.Str(required=True)
    ponto = fields.Str(required=True)

    ope_ocor_id = fields.Str(required=True)
    ope_ocor_id_obj = fields.Nested("OpeOcorSchema", dump_only=True)

    ope_ocor_mov_dest_id = fields.Str(required=False, allow_none=True)

    ope_ocor_status_id = fields.Str(required=True)
    ope_ocor_status_id_obj = fields.Nested("OpeOcorStatusSchema", dump_only=True)


# ==========================================================


class OpeCentro2OrdAtivSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2OrdAtiv
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    observacao_interna = fields.Str(required=True)
    observacao_externa = fields.Str(required=True)
    ordem_exec = fields.Str(required=True)

    tipo_executor = fields.Str(
        validate=valid_type_choice_sql(
            table_name="ope_centro2_ord_ativ",
            field_name="tipo_executor",
            session=app.db.session,
        )
    )
    tipo_executor_obj = fields_Type_Obj_Sql(
        field_choice="tipo_executor",
        table_name="ope_centro2_ord_ativ",
        field_name="tipo_executor",
        session=app.db.session,
    )

    data_valid = fields.Str(required=True)

    ope_atividade_id = fields.Str(required=True)
    ope_atividade_id_obj = fields.Nested("OpeAtividadeSchema", dump_only=True)

    ope_frente_trabalho_id = fields.Str(required=True)
    ope_frente_trabalho_id_obj = fields.Nested(
        "OpeFrenteTrabalhoSchema", dump_only=True
    )


# ==========================================================


class OpeCentro2OrdDestSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2OrdDest
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    qnt_obj = fields.Str(required=True)
    qnt_prev_obj = fields.Str(required=True)
    valor_unit_prev = fields.Str(required=True)
    valor_total_prev = fields.Str(required=True)
    observacao_interna = fields.Str(required=True)
    observacao_externa = fields.Str(required=True)
    valor_unit = fields.Str(required=True)
    valor_total = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    ger_umedida_id_dest = fields.Str(required=True)
    ger_umedida_id_obj = fields.Nested("GerUmedidaSchema", dump_only=True)

    ope_centro2_id_dest = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)


# ==========================================================


class OpeCentro2OrdItemservSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2OrdItemserv
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    observacao_interna = fields.Str(required=True)
    observacao_externa = fields.Str(required=True)
    qnt_rend = fields.Str(required=True)
    perc_util = fields.Str(required=True)
    qnt_total_util = fields.Str(required=True)
    valor_unit_util = fields.Str(required=True)
    valor_total_util = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    ctb_comp_id = fields.Str(required=True)
    ctb_comp_id_obj = fields.Nested("CtbCompSchema", dump_only=True)

    ger_itemserv_id = fields.Str(required=True)
    ger_itemserv_id_obj = fields.Nested("GerItemservSchema", dump_only=True)

    ope_centro2_ord_ativ_id = fields.Str(required=True)
    ope_centro2_ord_ativ_id_obj = fields.Nested(
        "OpeCentro2OrdAtivSchema", dump_only=True
    )


# ==========================================================


class OpeCentro2OrdRecSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = OpeCentro2OrdRec
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    observacao_interna = fields.Str(required=True)
    observacao_externa = fields.Str(required=True)
    qnt_rend = fields.Str(required=True)
    perc_util = fields.Str(required=True)
    qnt_total_util = fields.Str(required=True)
    valor_unit_util = fields.Str(required=True)
    valor_total_util = fields.Str(required=True)
    data_valid = fields.Str(required=True)

    ctb_comp_id = fields.Str(required=True)
    ctb_comp_id_obj = fields.Nested("CtbCompSchema", dump_only=True)

    ctb_comp_id_imp01 = fields.Str(required=True)
    ctb_comp_id_imp01_obj = fields.Nested("CtbCompSchema", dump_only=True)

    ger_pessoa_endereco_id_exec = fields.Str(required=True)
    ger_pessoa_endereco_id_exec_obj = fields.Nested(
        "GerPessoaEnderecoSchema", dump_only=True
    )

    ope_centro1_id = fields.Str(required=True)
    ope_centro1_id_obj = fields.Nested("OpeCentro1Schema", dump_only=True)

    ope_centro1_id_imp01 = fields.Str(required=True)
    ope_centro1_id_imp01_obj = fields.Nested("OpeCentro1Schema", dump_only=True)

    ope_centro2_id = fields.Str(required=True)
    ope_centro2_id_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_centro2_id_imp01 = fields.Str(required=True)
    ope_centro2_id_imp01_obj = fields.Nested("OpeCentro2Schema", dump_only=True)

    ope_centro2_ord_ativ_id = fields.Str(required=True)
    ope_centro2_ord_ativ_id_obj = fields.Nested(
        "OpeCentro2OrdAtivSchema", dump_only=True
    )

    ope_compart_id = fields.Str(required=True)
    ope_compart_id_obj = fields.Nested("OpeCompartSchema", dump_only=True)


# ==========================================================
