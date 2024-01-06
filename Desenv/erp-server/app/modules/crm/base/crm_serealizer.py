import app
from app.generics.generic_schema_field import fields_Type_Obj_Sql
from app.modules.crm.base.crm_model import (
    CrmAviso,
    CrmAvisoOrg,
    CrmChatGrupo,
    CrmChatMsg,
    CrmClass,
    CrmClassGrupo,
    CrmClassSubgrupo,
    CrmEtapa,
    CrmEtapaProx,
    CrmMov,
    CrmMovHist,
    CrmMovTag,
    CrmOrg,
    CrmPrioridade,
    CrmResposta,
    CrmStatus,
    CrmStatusProx,
    CrmTag,
    CrmUnitParam,
)

from app.generics.generic_schema import generic_schema
from marshmallow import EXCLUDE, fields
from app.utils.validator_util import valid_type_choice_sql

# ==========================================================


class CrmAvisoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmAviso
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
    sigla_aviso = fields.Str(required=True)


# ==========================================================


class CrmChatGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmChatGrupo
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
    sigla_chat_grupo = fields.Str(required=True)

    tipo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="crm_chat_grupo", field_name="tipo", session=app.db.session
        ),
    )
    tipo_obj = fields_Type_Obj_Sql(
        field_choice="tipo",
        table_name="crm_chat_grupo",
        field_name="tipo",
        session=app.db.session,
    )

    senha = fields.Str(required=True)
    acesso_privado = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    acesso_privado_obj = fields_Type_Obj_Sql(
        field_choice="acesso_privado",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    sys_user_id_dest = fields.Str(required=True)
    sys_user_id_dest_obj = fields.Nested("SysUserSchema", dump_only=True)

    sys_user_id_orig = fields.Str(required=True)
    sys_user_id_orig_obj = fields.Nested("SysUserSchema", dump_only=True)


# ==========================================================


class CrmClassGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmClassGrupo
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
    sigla_class_grupo = fields.Str(required=True)
    crm_class_subgrupo_childs = fields.Nested("CrmClassSubgrupoSchema", many=True)


# ==========================================================


class CrmEtapaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmEtapa
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
    sigla_etapa = fields.Str(required=True)


# ==========================================================


class CrmOrgSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmOrg
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
    sigla_org = fields.Str(required=True)

    ger_visual_user = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    ger_visual_user_obj = fields_Type_Obj_Sql(
        field_choice="ger_visual_user",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    user_visual_user = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    user_visual_user_obj = fields_Type_Obj_Sql(
        field_choice="user_visual_user",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )


# ==========================================================


class CrmPrioridadeSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmPrioridade
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
    sigla_prioridade = fields.Str(required=True)


# ==========================================================


class CrmRespostaSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmResposta
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
    sigla_resposta = fields.Str(required=True)


# ==========================================================


class CrmStatusSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmStatus
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
    sigla_status = fields.Str(required=True)

    tipo_status = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="crm_status", field_name="tipo_status", session=app.db.session
        ),
    )
    tipo_status_obj = fields_Type_Obj_Sql(
        field_choice="tipo_status",
        table_name="crm_status",
        field_name="tipo_status",
        session=app.db.session,
    )

    obrig_motivo = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    obrig_motivo_obj = fields_Type_Obj_Sql(
        field_choice="obrig_motivo",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    crm_status_prox_childs = fields.Nested("CrmStatusProxSchema", many=True)


# ==========================================================


class CrmTagSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmTag
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
    sigla_tag = fields.Str(required=True)


# ==========================================================


class CrmUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_valid_ini = fields.Str(required=True)


# ==========================================================


class CrmAvisoOrgSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmAvisoOrg
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    crm_aviso_id = fields.Str(required=True)
    crm_aviso_id_obj = fields.Nested("CrmAvisoSchema", dump_only=True)

    crm_org_id = fields.Str(required=True)
    crm_org_id_obj = fields.Nested("CrmOrgSchema", dump_only=True)


# ==========================================================


class CrmChatMsgSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmChatMsg
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    corpo = fields.Str(required=True)
    data_msg = fields.Str(required=True)

    crm_chat_grupo_id = fields.Str(required=True)
    crm_chat_grupo_id_obj = fields.Nested("CrmChatGrupoSchema", dump_only=True)

    sys_user_id_orig = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)


# ==========================================================


class CrmClassSubgrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmClassSubgrupo
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
    sigla_class_subgrupo = fields.Str(required=True)


# ==========================================================


class CrmEtapaProxSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmEtapaProx
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ordem = fields.Str(required=True)

    crm_etapa_id = fields.Str(required=True)
    crm_etapa_id_obj = fields.Nested("CrmEtapaSchema", dump_only=True)

    crm_etapa_id_prox = fields.Str(required=True)
    crm_etapa1_id_obj = fields.Nested("CrmEtapaSchema", dump_only=True)


# ==========================================================


class CrmMovSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmMov
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    numero = fields.Str(required=True)
    data_mov = fields.Str(required=True)
    envia_email_ext = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    envia_email_ext_obj = fields_Type_Obj_Sql(
        field_choice="envia_email_ext",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    descritivo_ext = fields.Str(required=True)
    descritivo_int = fields.Str(required=True)
    data_status = fields.Str(required=True)
    titulo = fields.Str(required=True)

    crm_etapa_id = fields.Str(required=True)
    crm_etapa_id_obj = fields.Nested("CrmEtapaSchema", dump_only=True)

    crm_prioridade_id = fields.Str(required=True)
    crm_prioridade_id_obj = fields.Nested("CrmPrioridadeSchema", dump_only=True)

    crm_status_id = fields.Str(required=True)
    crm_status_id_obj = fields.Nested("CrmStatusSchema", dump_only=True)

    sys_user_id_atend_ant = fields.Str(required=True)
    sys_user_id_atend_ant_obj = fields.Nested("SysUserSchema", dump_only=True)

    sys_user_id_atend_atu = fields.Str(required=True)
    sys_user_id_atend_atu_obj = fields.Nested("SysUserSchema", dump_only=True)

    sys_user_id_solic = fields.Str(required=True)
    sys_user_id_solic_obj = fields.Nested("SysUserSchema", dump_only=True)


# ==========================================================


class CrmStatusProxSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmStatusProx
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    ordem = fields.Number(required=True)

    tipo_status_ant = fields.Str(
        validate=valid_type_choice_sql(
            table_name="crm_status_prox",
            field_name="tipo_status_ant",
            session=app.db.session,
        ),
    )
    tipo_status_ant_obj = fields_Type_Obj_Sql(
        field_choice="tipo_status_ant",
        table_name="crm_status_prox",
        field_name="tipo_status_ant",
        session=app.db.session,
    )

    crm_status_id_prox = fields.Str(required=True)
    crm_status_id_prox_obj = fields.Nested("CrmStatusSchema", dump_only=True)


# ==========================================================


class CrmClassSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmClass
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
    sigla_class = fields.Str(required=True)

    crm_class_subgrupo_id = fields.Str(required=True)
    crm_class_subgrupo_id_obj = fields.Nested("CrmClassSubgrupoSchema", dump_only=True)


# ==========================================================


class CrmMovHistSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmMovHist
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_hist = fields.Str(required=True)
    descritivo = fields.Str(required=True)

    visual_ext = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    visual_ext_obj = fields_Type_Obj_Sql(
        field_choice="visual_ext",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    envia_email_ext = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    envia_email_ext_obj = fields_Type_Obj_Sql(
        field_choice="envia_email_ext",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    crm_mov_id = fields.Str(required=True)
    crm_mov_id_obj = fields.Nested("CrmMovSchema", dump_only=True)

    sys_user_id_hist = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)


# ==========================================================


class CrmMovTagSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CrmMovTag
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)

    crm_mov_id = fields.Str(required=True)
    crm_mov_id_obj = fields.Nested("CrmMovSchema", dump_only=True)
