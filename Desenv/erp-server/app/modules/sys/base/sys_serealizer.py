import app
from app.modules.sys.base.sys_model import (
    Sys,
    SysAccessLog,
    SysNotificationToken,
    SysUnitManager,
    SysAction,
    SysDic,
    SysDocument,
    SysDocumentCategory,
    SysDocumentGroup,
    SysDocumentUser,
    SysEmailLog,
    SysGroup,
    SysGroupProgram,
    SysGroupProgramAction,
    SysLicence,
    SysLicenceDevice,
    SysLicenceRestriction,
    SysMigration,
    SysModule,
    SysNotificationLog,
    SysParam,
    SysPlan,
    SysPlanRestriction,
    SysProcessLog,
    SysProgram,
    SysProgramAction,
    SysProgramFavorite,
    SysRestriction,
    SysToken,
    SysTranslate,
    SysTranslateLang,
    SysTypeDescription,
    SysUnit,
    SysUnitParam,
    SysUser,
    SysUserChatGrupo,
    SysUserCmsGrupo,
    SysUserGroup,
    SysUserIndPnl,
    SysUserPreference,
    SysUserProgramAction,
    SysUserUnit,
    SysUserProgram,
)
from app.generics.generic_schema import generic_schema
from marshmallow import EXCLUDE, fields, post_load
from app.generics.generic_schema_field import fields_Type_Obj_Sql

from app.utils.validator_util import valid_type_choice_sql


# ==========================================================


class SysUnitSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUnit
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    name = fields.Str(required=True)
    code_unit = fields.Str(required=True)

    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    sys_unit_manager_id = fields.Str(required=True)
    sys_unit_manager_id_obj = fields.Nested("SysUnitManagerSchema", dump_only=True)


# ==========================================================


class SysUserSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUser
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    login = fields.Str(required=False)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    active_message = fields.Str(
        load_default="Not message",
        validate=valid_type_choice_sql(
            table_name="sys_user", field_name="active_message", session=app.db.session
        ),
        required=False,
        allow_none=True,
    )

    active_message_obj = fields_Type_Obj_Sql(
        field_choice="active_message",
        table_name="sys_user",
        field_name="active_message",
        session=app.db.session,
    )
    phone = fields.Str(required=False, allow_none=True)
    document = fields.Str(required=False, allow_none=True)
    admin = fields.Str(
        load_default="N",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    admin_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    login_ext = fields.Str(required=False, allow_none=True)

    origem = fields.Str(
        load_default="1",
        validate=valid_type_choice_sql(
            table_name="sys_user", field_name="origem", session=app.db.session
        ),
    )
    origem_obj = fields_Type_Obj_Sql(
        field_choice="origem",
        table_name="sys_user",
        field_name="origem",
        session=app.db.session,
    )

    chat = fields.Str(
        load_default="N",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    chat_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    image_url = fields.Str(required=False, allow_none=True)
    email_verified = fields.Str(
        load_default="N",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    email_verified_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    provider = fields.Str(required=False)
    provider_code = fields.Str(required=False, allow_none=True)
    gtm_default = fields.Str(required=False, load_only=True)
    sys_tran_lang_id_default = fields.Str(required=True)
    sys_tran_lang_id_default_obj = fields.Nested(
        "SysTranslateLangSchema", dump_only=True
    )

    @post_load
    def role_login(self, item, **kwargs):
        if item.login is None:
            item.login = item.email
        return item


# ==========================================================


class SysDocumentCategorySchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysDocumentCategory
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    name = fields.Str(required=True)
    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    code_document_category = fields.Str(required=True)


# ==========================================================


class SysGroupSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysGroup
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    name = fields.Str(required=True)
    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    code_group = fields.Str(required=True)
    sys_group_program_childs = fields.Nested("SysGroupProgramSchema", many=True)


# ==========================================================


class SysDocumentGroupSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysDocumentGroup
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    document_fk_id = fields.Str(required=True)
    document_fk_id_obj = fields.Nested("SysDocumentSchema", dump_only=True)
    sys_group_fk_id = fields.Str(required=True)
    code_document = fields.Str(required=True)
    sys_group_fk_id_obj = fields.Nested("SysGroupSchema", dump_only=True)


# ==========================================================


class SysDocumentSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysDocument
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    title = fields.Str(allow_none=True)
    description = fields.Str(allow_none=True)
    submission_date = fields.Str(allow_none=True)
    filename = fields.Str(required=True)

    content_type = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="sys_document", field_name="content_type", session=app.db.session
        ),
    )
    content_type_obj = fields_Type_Obj_Sql(
        field_choice="content_type",
        table_name="sys_document",
        field_name="content_type",
        session=app.db.session,
    )

    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    archive_date = fields.Str(allow_none=True)

    code_document = fields.Str(required=True)

    sys_category_id = fields.Str(allow_none=True)
    sys_category_id_obj = fields.Nested("SysDocumentCategorySchema", dump_only=True)


# ===========================================================


class SysDocumentUserSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysDocumentUser
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_document_id = fields.Str(required=True)
    sys_document_id_obj = fields.Nested("SysDocumentSchema", dump_only=True)

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)


# ==========================================================


class SysGroupProgramSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysGroupProgram
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_program_id = fields.Str(required=True)
    sys_program_id_obj = fields.Nested("SysProgramSchema", dump_only=True)


# ==========================================================


class SysUserGroupSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUserGroup
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)

    sys_group_id = fields.Str(required=True)
    sys_group_id_obj = fields.Nested("SysGroupSchema", dump_only=True)


# ==========================================================


class SysRestrictionSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysRestriction
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    name = fields.Str(required=True)
    code_restriction = fields.Str(required=True)
    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    type_value = fields.Str(
        load_default="Q",
        validate=valid_type_choice_sql(
            table_name="sys_restriction",
            field_name="type_value",
            session=app.db.session,
        ),
    )
    type_value_obj = fields_Type_Obj_Sql(
        field_choice="type_value",
        table_name="sys_restriction",
        field_name="type_value",
        session=app.db.session,
    )


# ==========================================================


class SysSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = Sys
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    name = fields.Str(required=True)
    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    code_sys = fields.Str(required=True)


# ==========================================================


class SysModuleSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysModule
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    name = fields.Str(required=True)
    code_module = fields.Str(required=True)
    icon = fields.Str(required=True)
    color = fields.Str(required=True)
    order_visual = fields.Integer(required=True)
    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    sys_id = fields.Str(required=True)
    sys_id_obj = fields.Nested("SysSchema", dump_only=True)


# ==========================================================


class SysLicenceSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysLicence
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    tipo_doc = fields.Str(required=True)
    nome_solicitante = fields.Str(required=True)
    doc = fields.Str(required=True)
    end_logradouro = fields.Str(required=True)
    end_bairro = fields.Str(required=True)
    end_numero = fields.Str(required=True)
    end_cidade = fields.Str(required=True)
    end_pais = fields.Str(required=True)
    end_uf = fields.Str(required=True)
    code_licence = fields.Str(required=True)
    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    status = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="sys_licence", field_name="status", session=app.db.session
        ),
    )
    status_obj = fields_Type_Obj_Sql(
        field_choice="status",
        table_name="sys_licence",
        field_name="status",
        session=app.db.session,
    )

    status_data = fields.Str(required=True)
    status_observacao = fields.Str(required=True)
    sys_version = fields.Str(required=True)
    chamado_id = fields.Str(required=True)
    sys_plan_id = fields.Str(required=True)
    sys_plan_id_obj = fields.Nested("SysPlanSchema", dump_only=True)

    sys_id = fields.Str(required=True)
    sys_id_obj = fields.Nested("SysSchema", dump_only=True)

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)

    sys_licence_restriction_childs = fields.Nested(
        "SysLicenceRestrictionSchema", many=True
    )

    sys_licence_device_childs = fields.Nested("SysLicenceDeviceSchema", many=True)


# ==========================================================


class SysPlanSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysPlan
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    name = fields.Str(required=True)
    code_plan = fields.Str(required=True)
    type_plan = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="sys_plan", field_name="type_plan", session=app.db.session
        ),
    )
    type_plan_obj = fields_Type_Obj_Sql(
        field_choice="type_plan",
        table_name="sys_plan",
        field_name="type_plan",
        session=app.db.session,
    )

    description = fields.Str(required=True)
    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    indicated = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    indicated_obj = fields_Type_Obj_Sql(
        field_choice="indicated",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    sys_id = fields.Str(required=True)
    sys_id_obj = fields.Nested("SysSchema", dump_only=True)

    sys_plan_restriction_childs = fields.Nested("SysPlanRestrictionSchema", many=True)


# ==========================================================


class SysPlanRestrictionSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysPlanRestriction
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    value_restriction = fields.Number(required=True)
    value_restriction_blocked = fields.Number(required=True)
    days_blocked = fields.Number(required=True)
    days_blocked_extra = fields.Number(required=True)

    sys_restriction_id = fields.Str(required=True)
    sys_restriction_id_obj = fields.Nested("SysRestrictionSchema", dump_only=True)


# ==========================================================


class SysLicenceRestrictionSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysLicenceRestriction
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    value_restriction = fields.Number(required=True)
    days_blocked_extra = fields.Number(required=True)
    days_blocked = fields.Number(required=True)

    value_restriction_blocked = fields.Number(required=True)
    sys_restriction_id = fields.Str(required=True)
    sys_restriction_id_obj = fields.Nested("SysRestrictionSchema", dump_only=True)


# ==========================================================


class SysProgramSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysProgram
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    name = fields.Str(required=True)
    controller = fields.Str(required=True)
    menu = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    menu_obj = fields_Type_Obj_Sql(
        field_choice="menu",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    type_program = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="sys_program", field_name="type_program", session=app.db.session
        ),
    )
    type_program_obj = fields_Type_Obj_Sql(
        field_choice="type_program",
        table_name="sys_program",
        field_name="type_program",
        session=app.db.session,
    )

    icon = fields.Str(required=True)

    admin = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    admin_obj = fields_Type_Obj_Sql(
        field_choice="admin",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    icon = fields.Str(required=True)
    sys_module_id = fields.Str(required=True)
    code_program = fields.Str(required=True)
    sys_module_id_obj = fields.Nested("SysModuleSchema", dump_only=True)

    sys_program_action_childs = fields.Nested("SysProgramActionSchema", many=True)


# ==========================================================


class SysLicenceDeviceSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysLicenceDevice
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sigla_device = fields.Str(required=True)
    sys_licence_id = fields.Str(required=True)


# ==========================================================


class SysProgramFavoriteSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysProgramFavorite
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)

    sys_program_id = fields.Str(required=True)
    sys_program_id_obj = fields.Nested("SysProgramSchema", dump_only=True)


# ==========================================================


class SysEmailLogSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysEmailLog
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_unit_id = fields.Str(required=True)
    sys_unit_id_obj = fields.Nested("SysUnitSchema", dump_only=True)

    type_in_out = fields.Str(required=True)
    date_log = fields.Str(required=True)
    email_from = fields.Str(required=True)
    subject = fields.Str(required=True)
    body = fields.Str(required=True)
    error_message = fields.Str(required=True)
    email_to = fields.Str(required=True)
    login = fields.Str(required=True)
    date_send = fields.Str(required=True)
    body_type = fields.Str(required=True)


# ==========================================================


class SysActionSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysAction
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = False

    name = fields.Str(required=True)
    code = fields.Str(required=True)
    active = fields.Str(required=True)


# ==========================================================


class SysProgramActionSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysProgramAction
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_program_id = fields.Str(required=True)
    sys_program_id_obj = fields.Nested("SysProgramSchema", dump_only=True)

    sys_action_id = fields.Str(required=True)
    sys_action_id_obj = fields.Nested("SysActionSchema", dump_only=True)


# ==========================================================


class SysGroupProgramActionSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysGroupProgramAction
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_group_id = fields.Str(required=True)
    sys_group_id_obj = fields.Nested("SysGroupSchema", dump_only=True)

    sys_program_action_id = fields.Str(required=True)
    sys_program_action_id_obj = fields.Nested("SysProgramActionSchema", dump_only=True)


# ==========================================================


class SysUserProgramActionSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUserProgramAction
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)

    sys_program_action_id = fields.Str(required=True)
    sys_program_action_id_obj = fields.Nested("SysProgramActionSchema", dump_only=True)

    exclude_action = fields.Str(required=True)


# ==========================================================


class SysMigrationSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysMigration
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    version_num = fields.Str(required=True)


# ==========================================================


class SysNotificationLogSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysNotificationLog
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_user_id = fields.Str(required=True)
    sys_user_to_id = fields.Str(required=True)

    email_to = fields.Str(required=True)
    subject = fields.Str(required=True)
    message = fields.Str(required=True)
    dt_message = fields.Str(required=True)
    type_notification = fields.Str(required=True)
    icon = fields.Str(required=True)

    checked = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    checked_obj = fields_Type_Obj_Sql(
        field_choice="checked",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    action_url1 = fields.Str(required=True)
    action_label1 = fields.Str(required=True)
    action_body1 = fields.Str(required=True)
    action_header1 = fields.Str(required=True)
    action_type1 = fields.Str(required=True)
    action_url2 = fields.Str(required=True)
    action_label2 = fields.Str(required=True)
    action_body2 = fields.Str(required=True)
    action_header2 = fields.Str(required=True)
    action_type2 = fields.Str(required=True)
    action_url3 = fields.Str(required=True)
    action_label3 = fields.Str(required=True)
    action_body3 = fields.Str(required=True)
    action_header3 = fields.Str(required=True)
    action_type3 = fields.Str(required=True)


# ==========================================================


class SysNotificationTokenSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysNotificationToken
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_unit_id = fields.Str(required=False)
    sys_unit_id_obj = fields.Nested("SysUnitSchema", dump_only=True)
    sys_user_id = fields.Str(required=False)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)
    token = fields.Str(required=True)
    data_token = fields.Str(required=False)
    expired = fields.Str(
        load_default="N",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    expired_obj = fields_Type_Obj_Sql(
        field_choice="expired",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )


# ==========================================================


class SysTokenSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysToken
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    dt_validade = fields.Str(required=True)
    dt_used = fields.Str(required=False, allow_none=True)
    dt_token = fields.Str(required=True)
    token = fields.Str(required=True)
    data_token = fields.Str(required=True)


# ==========================================================


class SysTypeDescriptionSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysTypeDescription
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    table_name = fields.Str(required=True)
    field_name = fields.Str(required=True)
    value_type = fields.Str(required=True)
    description_type = fields.Str(required=True)


# ==========================================================


class SysProcessLogSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysProcessLog
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    type_process = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="sys_process_log",
            field_name="type_process",
            session=app.db.session,
        ),
    )
    type_process_obj = fields_Type_Obj_Sql(
        field_choice="type_process",
        table_name="sys_process_log",
        field_name="type_process",
        session=app.db.session,
    )
    date_ini_process = fields.Str(required=False)
    date_fin_process = fields.Str(required=False)
    reversed = fields.Str(
        load_default="N",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    reversed_obj = fields_Type_Obj_Sql(
        field_choice="reversed",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    param_process = fields.Str(required=True)
    message_process = fields.Str(required=True)
    code_process = fields.Str(required=True)
    error = fields.Str(
        load_default="N",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    error_obj = fields_Type_Obj_Sql(
        field_choice="error",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    unit_id = fields.Str(required=True)
    unit_id_obj = fields.Nested("SysUnitSchema", dump_only=True)

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)


# ==========================================================


class SysUserUnitSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUserUnit
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)

    sys_unit_id = fields.Str(required=True)
    sys_unit_id_obj = fields.Nested("SysUnitSchema", dump_only=True)


# ==========================================================


class SysUserIndPnlSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUserIndPnl
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE

    ind_pnl_id = fields.Str(required=True)
    ind_pnl_id_obj = fields.Nested("IndPnlSchema", dump_only=True)

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)


# ===========================================================


class SysAccessLogSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysAccessLog
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    access_ip = fields.Str(required=True)
    login_time = fields.Str(required=True)

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)

    unit_id = fields.Str(required=True)
    unit_id_obj = fields.Nested("SysUnitSchema", dump_only=True)

    sys_id = fields.Str(required=True)
    sys_id_obj = fields.Nested("SysSchema", dump_only=True)


# ===========================================================


class SysUserPreferenceSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUserPreference
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    value = fields.Str(required=True)
    isdefault = fields.Str(
        load_default="N",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    isdefault_obj = fields_Type_Obj_Sql(
        field_choice="isdefault",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )

    preference_description = fields.Str(required=True)
    object_type = fields.Str(required=True)
    object_id = fields.Str(required=True)
    object_sub_id = fields.Str(required=True)
    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)


# ===========================================================


class SysParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    type = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="sys_param", field_name="type", session=app.db.session
        ),
    )
    type_obj = fields_Type_Obj_Sql(
        field_choice="type",
        table_name="sys_param",
        field_name="type",
        session=app.db.session,
    )

    paramkey = fields.Str(required=True)
    paramvalue = fields.Str(required=True)

    sys_id = fields.Str(required=True)
    sys_obj = fields.Nested("SysSchema", dump_only=True)


# ===========================================================


class SysUnitParamSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUnitParam
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    unit_id = fields.Str(required=True)
    unit_id_obj = fields.Nested("SysUnitSchema", dump_only=True)
    data_valid_ini = fields.Str(required=True)
    unit_id_obj = fields.Nested("SysUnitSchema", dump_only=True)


# ===========================================================


class SysUserChatGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUserChatGrupo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)

    crm_chat_grupo_id = fields.Str(required=True)
    crm_chat_grupo_id_obj = fields.Nested("CrmChatGrupoSchema", dump_only=True)


# ===========================================================


class SysUserCmsGrupoSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUserCmsGrupo
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)

    cms_grupo_id = fields.Str(required=True)
    cms_grupo_id_obj = fields.Nested("CmsGrupoSchema", dump_only=True)


# ==========================================================


class SysUserProgramSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUserProgram
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested("SysUserSchema", dump_only=True)

    sys_program_id = fields.Str(required=True)
    sys_program_id_obj = fields.Nested("SysProgramSchema", dump_only=True)


# ==========================================================


class SysTranslateSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysTranslate
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    term_group = fields.Str(required=True)
    term_orig = fields.Str(required=True)
    term_translate = fields.Str(required=True)

    sys_translate_lang_id = fields.Str(required=True)
    sys_translate_lang_id_obj = fields.Nested("SysTranslateLangSchema", dump_only=True)


# ==========================================================


class SysTranslateLangSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysTranslateLang
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    code = fields.Str(required=True)
    name = fields.Str(required=True)
    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    default_lang = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    default_lang = fields_Type_Obj_Sql(
        field_choice="default_lang",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )


# ==========================================================


class SysDicSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysDic
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    name = fields.Str(required=True)
    name_item = fields.Str(required=True)
    type_dic = fields.Str(
        required=True,
        validate=valid_type_choice_sql(
            table_name="sys_dic", field_name="type_dic", session=app.db.session
        ),
    )
    type_dic_obj = fields_Type_Obj_Sql(
        field_choice="type_dic",
        table_name="sys_dic",
        field_name="type_dic",
        session=app.db.session,
    )
    description = fields.Str(required=True)
    description_help = fields.Str(required=True)


# ==========================================================


class SysUnitManagerSchema(generic_schema, app.ma.SQLAlchemySchema):
    class Meta:
        model = SysUnitManager
        sqla_session = app.db.session
        load_instance = True
        unknown = EXCLUDE
        include_fk = True

    name = fields.Str(required=True)
    active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    subdomain_name = fields.Str(required=True)
    subdomain_active = fields.Str(
        load_default="S",
        validate=valid_type_choice_sql(
            table_name="default_sn", field_name="default", session=app.db.session
        ),
    )
    subdomain_active_obj = fields_Type_Obj_Sql(
        field_choice="active",
        table_name="default_sn",
        field_name="default",
        session=app.db.session,
    )
    color_primary = fields.Str(required=True)
    color_secondary = fields.Str(required=True)
    color_general_background = fields.Str(required=True)
    color_menu_module_background = fields.Str(required=True)
    color_menu_module_font = fields.Str(required=True)
    icon_menu = fields.Str(required=True)
    icon_login = fields.Str(required=True)
    icon_general = fields.Str(required=True)
    link_website = fields.Str(required=True)
    link_policy_private = fields.Str(required=True)
    link_term_of_use = fields.Str(required=True)
