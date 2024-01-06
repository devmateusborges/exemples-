import app
from sqlalchemy import Text
from app.generics.generic_model import generic_model, get_now
from passlib.hash import pbkdf2_sha256


# ==========================================================


class SysUnit(generic_model, app.db.Model):
    __tablename__ = "sys_unit"

    name = app.db.Column(app.db.String(100))
    code_unit = app.db.Column(app.db.String(100))
    active = app.db.Column(app.db.String(1))

    sys_unit_manager_id = app.db.Column(app.db.ForeignKey("sys_unit_manager.id"))
    sys_unit_manager_id_obj = app.db.relationship("SysUnitManager")


# ==========================================================


class SysUser(generic_model, app.db.Model):
    __tablename__ = "sys_user"

    name = app.db.Column(app.db.String(100))
    login = app.db.Column(app.db.String(100), unique=True)
    email = app.db.Column(app.db.String(100), unique=True)
    password = app.db.Column(app.db.String(100))
    active = app.db.Column(app.db.String(1), default="S")
    active_message = app.db.Column(app.db.Text)
    phone = app.db.Column(app.db.String(50))
    document = app.db.Column(app.db.String(50))
    admin = app.db.Column(app.db.String(1), default="N")
    login_ext = app.db.Column(app.db.String(100))
    origem = app.db.Column(app.db.String(1))
    chat = app.db.Column(app.db.String(1), default="N")
    image_url = app.db.Column(app.db.String(1000))
    email_verified = app.db.Column(app.db.String(1), default="N")
    provider = app.db.Column(app.db.String(50), default="LOCAL")
    provider_code = app.db.Column(app.db.String(50))
    gtm_default = app.db.Column(app.db.String(50))
    sys_tran_lang_id_default = app.db.Column(app.db.ForeignKey("sys_translate_lang.id"))
    sys_tran_lang_id_default_obj = app.db.relationship("SysTranslateLang")

    def gen_hash(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)


# ==========================================================


class SysDocumentCategory(generic_model, app.db.Model):
    __tablename__ = "sys_document_category"

    name = app.db.Column(app.db.String(100))
    active = app.db.Column(app.db.String(1))
    code_document_category = app.db.Column(app.db.String(50))


# ==========================================================


class SysGroup(generic_model, app.db.Model):
    __tablename__ = "sys_group"

    name = app.db.Column(app.db.String(100))
    active = app.db.Column(app.db.String(1))
    code_group = app.db.Column(app.db.String(100))
    sys_group_program_childs = app.db.relationship(
        "SysGroupProgram", cascade="all,delete-orphan"
    )


# ==========================================================


class SysDocumentGroup(generic_model, app.db.Model):
    __tablename__ = "sys_document_group"

    document_id = app.db.Column(app.db.ForeignKey("sys_document.id"))
    document_id_obj = app.db.relationship("SysDocument")

    sys_group_id = app.db.Column(app.db.ForeignKey("sys_group.id"))
    sys_group_id_obj = app.db.relationship("SysGroup")


# ==========================================================


class SysDocument(generic_model, app.db.Model):
    __tablename__ = "sys_document"

    title = app.db.Column(app.db.Text)
    description = app.db.Column(app.db.Text)
    submission_date = app.db.Column(app.db.Date)
    filename = app.db.Column(app.db.Text)
    content_type = app.db.Column(app.db.String(100))
    active = app.db.Column(app.db.String(1))
    archive_date = app.db.Column(app.db.Date)
    code_document = app.db.Column(app.db.String(50))
    sys_category_id = app.db.Column(app.db.ForeignKey("sys_document_category.id"))
    sys_category_id_obj = app.db.relationship("SysDocumentCategory")
    test1_id = app.db.Column(app.db.ForeignKey("test1.id"))
    test1_child_id = app.db.Column(app.db.ForeignKey("test1_child.id"))
    test1a_child_id = app.db.Column(app.db.ForeignKey("test1a_child.id"))
    fis_certificado_id = app.db.Column(app.db.ForeignKey("fis_certificado.id"))
    cms_post_id = app.db.Column(app.db.ForeignKey("cms_post.id"))


# ==========================================================
class SysDocumentUser(generic_model, app.db.Model):
    __tablename__ = "sys_document_user"

    sys_document_id = app.db.Column(app.db.ForeignKey("sys_document.id"))
    sys_document_id_obj = app.db.relationship("SysDocument")

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")


# ==========================================================


class SysGroupProgram(generic_model, app.db.Model):
    __tablename__ = "sys_group_program"

    sys_group_id = app.db.Column(app.db.ForeignKey("sys_group.id"))

    sys_program_id = app.db.Column(app.db.ForeignKey("sys_program.id"))
    sys_program_id_obj = app.db.relationship("SysProgram")


# ==========================================================


class SysUserGroup(generic_model, app.db.Model):
    __tablename__ = "sys_user_group"

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")

    sys_group_id = app.db.Column(app.db.ForeignKey("sys_group.id"))
    sys_group_id_obj = app.db.relationship("SysGroup")


# ==========================================================


class SysRestriction(generic_model, app.db.Model):
    __tablename__ = "sys_restriction"

    name = app.db.Column(app.db.String(100))
    code_restriction = app.db.Column(app.db.String(100))
    active = app.db.Column(app.db.String(1))
    type_value = app.db.Column(app.db.String(1))


# ==========================================================


class Sys(generic_model, app.db.Model):
    __tablename__ = "sys"

    name = app.db.Column(app.db.String(100))
    active = app.db.Column(app.db.String(1))
    code_sys = app.db.Column(app.db.String(100))


# ==========================================================


class SysModule(generic_model, app.db.Model):
    __tablename__ = "sys_module"

    name = app.db.Column(app.db.String(100))
    code_module = app.db.Column(app.db.String(50))
    active = app.db.Column(app.db.String(1))
    order_visual = app.db.Column(app.db.String(30))
    sys_id = app.db.Column(app.db.ForeignKey("sys.id"))
    sys_id_obj = app.db.relationship("Sys")
    code_module = app.db.Column(app.db.String(100))
    icon = app.db.Column(app.db.String(100))
    color = app.db.Column(app.db.String(100))


# ==========================================================


class SysLicence(generic_model, app.db.Model):
    __tablename__ = "sys_licence"

    tipo_doc = app.db.Column(app.db.String(100))
    nome_solicitante = app.db.Column(app.db.String(100))
    doc = app.db.Column(app.db.String(100))
    end_logradouro = app.db.Column(app.db.String(100))
    end_bairro = app.db.Column(app.db.String(100))
    end_numero = app.db.Column(app.db.String(100))
    end_cidade = app.db.Column(app.db.String(100))
    end_uf = app.db.Column(app.db.String(100))
    end_pais = app.db.Column(app.db.String(100))
    status = app.db.Column(app.db.String(2))
    status_data = app.db.Column(app.db.TIMESTAMP())
    status_observacao = app.db.Column(app.db.String(250))
    sys_version = app.db.Column(app.db.String(50))
    chamado_id = app.db.Column(app.db.String(100))
    active = app.db.Column(app.db.String(1))
    code_licence = app.db.Column(app.db.String(50))
    sys_plan_id = app.db.Column(app.db.ForeignKey("sys_plan.id"))
    sys_plan_id_obj = app.db.relationship("SysPlan")

    sys_id = app.db.Column(app.db.ForeignKey("sys.id"))
    sys_id_obj = app.db.relationship("Sys")

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id", ondelete="CASCADE"))
    sys_user_id_obj = app.db.relationship("SysUser")

    sys_licence_restriction_childs = app.db.relationship(
        "SysLicenceRestriction", cascade="all,delete-orphan"
    )
    sys_licence_device_childs = app.db.relationship(
        "SysLicenceDevice", cascade="all,delete-orphan"
    )


# ==========================================================


class SysPlan(generic_model, app.db.Model):
    __tablename__ = "sys_plan"

    name = app.db.Column(app.db.String(100))
    type_plan = app.db.Column(app.db.String(2))
    description = app.db.Column(app.db.Text)
    active = app.db.Column(app.db.String(1))
    indicated = app.db.Column(app.db.String(1))
    code_plan = app.db.Column(app.db.String(100))

    sys_id = app.db.Column(app.db.ForeignKey("sys.id"))
    sys_id_obj = app.db.relationship("Sys")

    sys_plan_restriction_childs = app.db.relationship(
        "SysPlanRestriction", cascade="all,delete-orphan"
    )


# ==========================================================


class SysPlanRestriction(generic_model, app.db.Model):
    __tablename__ = "sys_plan_restriction"

    sys_plan_id = app.db.Column(app.db.ForeignKey("sys_plan.id"))

    days_blocked = app.db.Column(app.db.Integer)
    days_blocked_extra = app.db.Column(app.db.Integer)
    value_restriction = app.db.Column(app.db.Integer)
    value_restriction_blocked = app.db.Column(app.db.Integer)

    sys_restriction_id = app.db.Column(app.db.ForeignKey("sys_restriction.id"))
    sys_restriction_id_obj = app.db.relationship("SysRestriction")


# ==========================================================


class SysLicenceRestriction(generic_model, app.db.Model):
    __tablename__ = "sys_licence_restriction"

    sys_restriction_id = app.db.Column(app.db.ForeignKey("sys_restriction.id"))
    sys_restriction_id_obj = app.db.relationship("SysRestriction")

    sys_licence_id = app.db.Column(
        app.db.ForeignKey("sys_licence.id", ondelete="CASCADE")
    )

    days_blocked_extra = app.db.Column(app.db.Integer)
    days_blocked = app.db.Column(app.db.Integer)

    value_restriction = app.db.Column(app.db.Integer)
    value_restriction_blocked = app.db.Column(app.db.Integer)


# ==========================================================


class SysProgram(generic_model, app.db.Model):
    __tablename__ = "sys_program"

    name = app.db.Column(app.db.String(100))
    controller = app.db.Column(app.db.String(100))
    menu = app.db.Column(app.db.String(1))
    type_program = app.db.Column(app.db.String(1))
    icon = app.db.Column(app.db.String(50))
    admin = app.db.Column(app.db.String(1))
    active = app.db.Column(app.db.String(1))
    code_program = app.db.Column(app.db.String(50))
    sys_module_id = app.db.Column(app.db.ForeignKey("sys_module.id"))
    sys_module_id_obj = app.db.relationship("SysModule")

    sys_program_action_childs = app.db.relationship(
        "SysProgramAction", cascade="all,delete-orphan"
    )


# ==========================================================


class SysLicenceDevice(generic_model, app.db.Model):
    __tablename__ = "sys_licence_device"

    sigla_device = app.db.Column(app.db.String(100))

    sys_licence_id = app.db.Column(app.db.ForeignKey("sys_licence.id"))
    # sys_licence_id_obj = app.db.relationship("SysLicence")


# ==========================================================


class SysProgramFavorite(generic_model, app.db.Model):
    __tablename__ = "sys_program_favorite"

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")

    sys_program_id = app.db.Column(app.db.ForeignKey("sys_program.id"))
    sys_program_id_obj = app.db.relationship("SysProgram")


# ==========================================================


class SysAction(generic_model, app.db.Model):
    __tablename__ = "sys_action"

    name = app.db.Column(app.db.String(100))
    code = app.db.Column(app.db.String(50))
    active = app.db.Column(app.db.String(1))


# ===========================================================


class SysProgramAction(generic_model, app.db.Model):
    __tablename__ = "sys_program_action"

    sys_action_id = app.db.Column(app.db.ForeignKey("sys_action.id"))
    sys_action_id_obj = app.db.relationship("SysAction")

    sys_program_id = app.db.Column(app.db.ForeignKey("sys_program.id"))


# ===========================================================


class SysGroupProgramAction(generic_model, app.db.Model):
    __tablename__ = "sys_group_program_action"
    sys_group_id = app.db.Column(app.db.ForeignKey("sys_group.id"))
    sys_group_id_obj = app.db.relationship("SysGroup")

    sys_program_action_id = app.db.Column(app.db.ForeignKey("sys_program_action.id"))
    sys_program_action_id_obj = app.db.relationship("SysProgramAction")


# ===========================================================


class SysUserProgramAction(generic_model, app.db.Model):
    __tablename__ = "sys_user_program_action"
    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")

    sys_program_action_id = app.db.Column(app.db.ForeignKey("sys_program_action.id"))
    sys_program_action_id_obj = app.db.relationship("SysProgramAction")

    exclude_action = app.db.Column(app.db.String(1))


# ===========================================================


class SysEmailLog(generic_model, app.db.Model):
    __tablename__ = "sys_email_log"

    sys_unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    sys_unit_id_obj = app.db.relationship("SysUnit")

    type_in_out = app.db.Column(app.db.String(2))
    date_log = app.db.Column(app.db.TIMESTAMP())
    email_from = app.db.Column(Text)
    subject = app.db.Column(Text)
    body = app.db.Column(Text)
    error_message = app.db.Column(Text)
    email_to = app.db.Column(Text)
    login = app.db.Column(app.db.String(50))
    date_send = app.db.Column(app.db.TIMESTAMP())
    body_type = app.db.Column(app.db.String(50))


# ==========================================================


class SysMigration(generic_model, app.db.Model):
    __tablename__ = "sys_migration"

    version_num = app.db.Column(app.db.String(32), primary_key=True)


# ==========================================================


class SysNotificationLog(generic_model, app.db.Model):
    __tablename__ = "sys_notification_log"

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")

    sys_user_to_id = app.db.Column(app.db.String(36))
    email_to = app.db.Column(app.db.String(100))
    subject = app.db.Column(Text)
    message = app.db.Column(Text)
    dt_message = app.db.Column(Text)
    type_notification = app.db.Column(app.db.String(50))
    icon = app.db.Column(Text)
    checked = app.db.Column(app.db.CHAR(1))
    action_url1 = app.db.Column(Text)
    action_label1 = app.db.Column(Text)
    action_body1 = app.db.Column(Text)
    action_header1 = app.db.Column(Text)
    action_type1 = app.db.Column(Text)
    action_url2 = app.db.Column(Text)
    action_label2 = app.db.Column(Text)
    action_body2 = app.db.Column(Text)
    action_header2 = app.db.Column(Text)
    action_type2 = app.db.Column(Text)
    action_url3 = app.db.Column(Text)
    action_label3 = app.db.Column(Text)
    action_body3 = app.db.Column(Text)
    action_header3 = app.db.Column(Text)
    action_type3 = app.db.Column(Text)


# ==========================================================


class SysNotificationToken(generic_model, app.db.Model):
    __tablename__ = "sys_notification_token"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")
    token = app.db.Column(Text, unique=True)
    data_token = app.db.Column(Text)
    expired = app.db.Column(app.db.String(1))


# ==========================================================


class SysToken(generic_model, app.db.Model):
    __tablename__ = "sys_token"

    dt_validade = app.db.Column(app.db.TIMESTAMP())
    dt_used = app.db.Column(app.db.TIMESTAMP())
    dt_token = app.db.Column(app.db.TIMESTAMP(), default=get_now)
    token = app.db.Column(Text, unique=True)
    data_token = app.db.Column(Text)


# ==========================================================


class SysTypeDescription(generic_model, app.db.Model):
    __tablename__ = "sys_type_description"

    table_name = app.db.Column(app.db.String(100))
    field_name = app.db.Column(app.db.String(100))
    value_type = app.db.Column(app.db.String(100))
    description_type = app.db.Column(app.db.String(100))


# ==========================================================


class SysProcessLog(generic_model, app.db.Model):
    __tablename__ = "sys_process_log"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    type_process = app.db.Column(app.db.String(50))
    date_ini_process = app.db.Column(app.db.TIMESTAMP())
    date_fin_process = app.db.Column(app.db.TIMESTAMP())
    reversed = app.db.Column(app.db.String(1))
    param_process = app.db.Column(Text)
    message_process = app.db.Column(Text)
    error = app.db.Column(app.db.String(1))
    code_process = app.db.Column(Text)

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")


# ===========================================================


class SysUserUnit(generic_model, app.db.Model):
    __tablename__ = "sys_user_unit"

    owner = app.db.Column(app.db.String(1))

    sys_unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    sys_unit_id_obj = app.db.relationship("SysUnit")

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")


# ===========================================================


class SysUserIndPnl(generic_model, app.db.Model):
    __tablename__ = "sys_user_ind_pnl"

    ind_pnl_id = app.db.Column(app.db.ForeignKey("ind_pnl.id"))
    ind_pnl_id_obj = app.db.relationship("IndPnl")

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")


# ===========================================================


class SysAccessLog(generic_model, app.db.Model):
    __tablename__ = "sys_access_log"

    access_ip = app.db.Column(app.db.String(45))
    login_time = app.db.Column(app.db.TIMESTAMP())

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"), name="sys_user_id")
    sys_user_id_obj = app.db.relationship("SysUser")

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"), name="unit_id")
    unit_id_obj = app.db.relationship("SysUnit")

    sys_id = app.db.Column(app.db.ForeignKey("sys.id"))
    sys_id_obj = app.db.relationship("Sys")


# ===========================================================


class SysUserPreference(generic_model, app.db.Model):
    __tablename__ = "sys_user_preference"

    value = app.db.Column(app.db.Text)
    isdefault = app.db.Column(app.db.String(1))
    preference_description = app.db.Column(app.db.String(50))
    object_type = app.db.Column(app.db.String(36))
    # TODO DATAGRIDSTATE
    object_sub_id = app.db.Column(app.db.String(36))
    ispublic = app.db.Column(app.db.String(1))
    object_id = app.db.Column(app.db.String(36))

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")


# ===========================================================


class SysParam(generic_model, app.db.Model):
    __tablename__ = "sys_param"

    type = app.db.Column(app.db.String(250))
    paramkey = app.db.Column(app.db.String(255))
    paramvalue = app.db.Column(app.db.Text)

    sys_id = app.db.Column(app.db.ForeignKey("sys.id"), name="sys_id")
    sys_obj = app.db.relationship("Sys")


# ===========================================================


class SysUnitParam(generic_model, app.db.Model):
    __tablename__ = "sys_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    unit_id_obj = app.db.relationship("SysUnit")
    data_valid_ini = app.db.Column(app.db.Date)


# ===========================================================


class SysUserChatGrupo(generic_model, app.db.Model):
    __tablename__ = "sys_user_chat_grupo"

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")

    crm_chat_grupo_id = app.db.Column(app.db.ForeignKey("crm_chat_grupo.id"))
    crm_chat_grupo_id_obj = app.db.relationship("CrmChatGrupo")


# ===========================================================


class SysUserCmsGrupo(generic_model, app.db.Model):
    __tablename__ = "sys_user_cms_grupo"

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")

    cms_grupo_id = app.db.Column(app.db.ForeignKey("cms_grupo.id"))
    cms_grupo_id_obj = app.db.relationship("CmsGrupo")


# ==========================================================


class SysUserProgram(generic_model, app.db.Model):
    __tablename__ = "sys_user_program"

    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")

    sys_program_id = app.db.Column(app.db.ForeignKey("sys_program.id"))
    sys_program_id_obj = app.db.relationship("SysProgram")


# ==========================================================


class SysTranslate(generic_model, app.db.Model):
    __tablename__ = "sys_translate"

    term_group = app.db.Column(app.db.String(50))
    term_orig = app.db.Column(app.db.String(500))
    term_translate = app.db.Column(app.db.String(500))

    sys_translate_lang_id = app.db.Column(app.db.ForeignKey("sys_translate_lang.id"))
    sys_translate_lang_id_obj = app.db.relationship("SysTranslateLang")


# ==========================================================


class SysTranslateLang(generic_model, app.db.Model):
    __tablename__ = "sys_translate_lang"

    code = app.db.Column(app.db.String(50))
    name = app.db.Column(app.db.String(100))
    active = app.db.Column(app.db.String(1))
    default_lang = app.db.Column(app.db.String(1))


# ==========================================================


class SysDic(generic_model, app.db.Model):
    __tablename__ = "sys_dic"

    name = app.db.Column(app.db.String(250))
    name_item = app.db.Column(app.db.String(250))
    type_dic = app.db.Column(app.db.String(2))
    description = app.db.Column(app.db.String(500))
    description_help = app.db.Column(app.db.String(500))


# ==========================================================


class SysUnitManager(generic_model, app.db.Model):
    __tablename__ = "sys_unit_manager"

    name = app.db.Column(app.db.String(100))
    active = app.db.Column(app.db.String(1))
    subdomain_name = app.db.Column(app.db.String(100))
    subdomain_active = app.db.Column(app.db.String(1))
    color_primary = app.db.Column(app.db.String(100))
    color_secondary = app.db.Column(app.db.String(100))
    color_general_background = app.db.Column(app.db.String(100))
    color_menu_module_background = app.db.Column(app.db.String(100))
    color_menu_module_font = app.db.Column(app.db.String(100))
    icon_menu = app.db.Column(app.db.String(250))
    icon_login = app.db.Column(app.db.String(250))
    icon_general = app.db.Column(app.db.String(250))
    link_website = app.db.Column(app.db.String(250))
    link_policy_private = app.db.Column(app.db.String(250))
    link_term_of_use = app.db.Column(app.db.String(250))
