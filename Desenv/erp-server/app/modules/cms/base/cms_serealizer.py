import app
from app.modules.cms.base.cms_model import (
    CmsGrupo,
    CmsPost,
    CmsPostGrupo,
    CmsPostHist,
    CmsPostTag,
    CmsTag,
)
from app.generics.generic_schema import generic_schema
from marshmallow import fields
from app.generics.generic_schema_field import fields_Type_Obj_Sql

from app.utils.validator_util import valid_type_choice_sql
from marshmallow import EXCLUDE


# ==========================================================


class CmsGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CmsGrupo
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
    sigla_grupo = fields.Str(required=True)

    publico = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    publico_obj = fields_Type_Obj_Sql(
        field_choice="publico",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    color = fields.Str(required=True)


# ==========================================================


class CmsPostSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CmsPost
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    titulo = fields.Str(required=True)
    corpo = fields.Str(required=True)
    img_url = fields.Nested("SysDocumentSchema", many=True)
    status = fields.Str(
        validate=valid_type_choice_sql(
            table_name="cms_post", field_name="status", session=app.db.session
        )
    )
    status_obj = fields_Type_Obj_Sql(
        field_choice="status",
        table_name="cms_post",
        field_name="status",
        session=app.db.session,
    )

    favorito = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    favorito_obj = fields_Type_Obj_Sql(
        field_choice="favorito",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    util_blog = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    util_blog_obj = fields_Type_Obj_Sql(
        field_choice="util_blog",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    util_depoimento = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    util_depoimento_obj = fields_Type_Obj_Sql(
        field_choice="util_depoimento",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    util_treinamento = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    util_treinamento_obj = fields_Type_Obj_Sql(
        field_choice="util_treinamento",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    util_help = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    util_help_obj = fields_Type_Obj_Sql(
        field_choice="util_help",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    tipo_render = fields.Str(
        validate=valid_type_choice_sql(
            table_name="cms_post", field_name="tipo_render", session=app.db.session
        )
    )
    tipo_render_obj = fields_Type_Obj_Sql(
        field_choice="tipo_render",
        table_name="cms_post",
        field_name="tipo_render",
        session=app.db.session,
    )

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)

    cms_post_tag_childs = fields.Nested("CmsPostTagSchema", many=True)
    cms_post_grupo_childs = fields.Nested("CmsPostGrupoSchema", many=True)


# ==========================================================


class CmsPostHistSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CmsPostHist
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    data_hist = fields.Str(required=True)

    descricao = fields.Str(
        validate=valid_type_choice_sql(
            table_name="cms_post_hist", field_name="descricao", session=app.db.session
        )
    )
    descricao_obj = fields_Type_Obj_Sql(
        field_choice="descricao",
        table_name="cms_post_hist",
        field_name="descricao",
        session=app.db.session,
    )

    tipo_hist = fields.Str(
        validate=valid_type_choice_sql(
            table_name="cms_post_hist", field_name="tipo_hist", session=app.db.session
        )
    )
    tipo_hist_obj = fields_Type_Obj_Sql(
        field_choice="tipo_hist",
        table_name="cms_post_hist",
        field_name="tipo_hist",
        session=app.db.session,
    )

    cms_post_id = fields.Str(required=True)
    cms_post_id_obj = fields.Nested("CmsPostSchema", dump_only=True)


# ==========================================================


class CmsTagSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CmsTag
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    unit_id = fields.Str(required=True)
    nome = fields.Str(required=True)
    sigla_tag = fields.Str(required=True)
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
    color = fields.Str(required=True)


# ==========================================================


class CmsPostTagSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CmsPostTag
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    cms_tag_id = fields.Str(required=True)
    cms_tag_id_obj = fields.Nested("CmsTagSchema", dump_only=True)

    cms_post_id_obj = fields.Nested("CmsPostSchema", dump_only=True)


# ==========================================================


class CmsPostGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = CmsPostGrupo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    cms_grupo_id = fields.Str(required=True)
    cms_grupo_id_obj = fields.Nested("CmsGrupoSchema")

    cms_post_id_obj = fields.Nested("CmsPostSchema", dump_only=True)


# ==========================================================
