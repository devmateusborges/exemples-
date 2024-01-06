import app
from sqlalchemy import Text
from app.generics.generic_model import generic_model

# ==========================================================


class CrmAviso(generic_model, app.db.Model):
    __tablename__ = "crm_aviso"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(Text)
    ativo = app.db.Column(app.db.String(1))
    sigla_aviso = app.db.Column(app.db.String(50))


# ==========================================================


class CrmChatGrupo(generic_model, app.db.Model):
    __tablename__ = "crm_chat_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_chat_grupo = app.db.Column(app.db.String(50))
    tipo = app.db.Column(app.db.String(1))
    senha = app.db.Column(app.db.String(100))
    acesso_privado = app.db.Column(app.db.String(1))

    sys_user_id_dest = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_dest_obj = app.db.relationship(
        "SysUser", primaryjoin="CrmChatGrupo.sys_user_id_dest == SysUser.id"
    )

    sys_user_id_orig = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_orig_obj = app.db.relationship(
        "SysUser", primaryjoin="CrmChatGrupo.sys_user_id_orig == SysUser.id"
    )


# ==========================================================


class CrmClassGrupo(generic_model, app.db.Model):
    __tablename__ = "crm_class_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_class_grupo = app.db.Column(app.db.String(50))
    crm_class_subgrupo_childs = app.db.relationship(
        "CrmClassSubgrupo", cascade="all,delete-orphan"
    )


# ==========================================================


class CrmEtapa(generic_model, app.db.Model):
    __tablename__ = "crm_etapa"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_etapa = app.db.Column(app.db.String(50))


# ==========================================================


class CrmOrg(generic_model, app.db.Model):
    __tablename__ = "crm_org"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_org = app.db.Column(app.db.String(50))
    ger_visual_user = app.db.Column(
        app.db.String(1),
    )
    user_visual_user = app.db.Column(
        app.db.String(1),
    )


# ==========================================================


class CrmPrioridade(generic_model, app.db.Model):
    __tablename__ = "crm_prioridade"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_prioridade = app.db.Column(app.db.String(50))


# ==========================================================


class CrmResposta(generic_model, app.db.Model):
    __tablename__ = "crm_resposta"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(Text)
    ativo = app.db.Column(app.db.String(1))
    sigla_resposta = app.db.Column(app.db.String(50))


# ==========================================================


class CrmStatus(generic_model, app.db.Model):
    __tablename__ = "crm_status"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_status = app.db.Column(app.db.String(50))
    tipo_status = app.db.Column(app.db.String(2))
    obrig_motivo = app.db.Column(app.db.String(1))
    crm_status_prox_childs = app.db.relationship(
        "CrmStatusProx",
        primaryjoin="CrmStatusProx.crm_status_id == CrmStatus.id",
        cascade="all,delete-orphan",
    )


# ==========================================================


class CrmTag(generic_model, app.db.Model):
    __tablename__ = "crm_tag"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(Text)
    ativo = app.db.Column(app.db.String(1))
    sigla_tag = app.db.Column(app.db.String(50))


# ==========================================================


class CrmUnitParam(generic_model, app.db.Model):
    __tablename__ = "crm_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================


class CrmAvisoOrg(generic_model, app.db.Model):
    __tablename__ = "crm_aviso_org"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    crm_aviso_id = app.db.Column(app.db.ForeignKey("crm_aviso.id"))
    crm_aviso_id_obj = app.db.relationship("CrmAviso")

    crm_org_id = app.db.Column(app.db.ForeignKey("crm_org.id"))
    crm_org_id_obj = app.db.relationship("CrmOrg")


# ==========================================================


class CrmChatMsg(generic_model, app.db.Model):
    __tablename__ = "crm_chat_msg"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    corpo = app.db.Column(app.db.Text)
    data_msg = app.db.Column(app.db.Date)

    crm_chat_grupo_id = app.db.Column(app.db.ForeignKey("crm_chat_grupo.id"))
    crm_chat_grupo_id_obj = app.db.relationship("CrmChatGrupo")

    sys_user_id_orig = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")


# ==========================================================


class CrmClassSubgrupo(generic_model, app.db.Model):
    __tablename__ = "crm_class_subgrupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_class_subgrupo = app.db.Column(app.db.String(50))

    crm_class_grupo_id = app.db.Column(app.db.ForeignKey("crm_class_grupo.id"))


# ==========================================================


class CrmEtapaProx(generic_model, app.db.Model):
    __tablename__ = "crm_etapa_prox"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ordem = app.db.Column(app.db.Integer)

    crm_etapa_id = app.db.Column(app.db.ForeignKey("crm_etapa.id"))
    crm_etapa_id_obj = app.db.relationship(
        "CrmEtapa", primaryjoin="CrmEtapaProx.crm_etapa_id == CrmEtapa.id"
    )

    crm_etapa_id_prox = app.db.Column(app.db.ForeignKey("crm_etapa.id"))
    crm_etapa_id_prox_obj = app.db.relationship(
        "CrmEtapa", primaryjoin="CrmEtapaProx.crm_etapa_id_prox == CrmEtapa.id"
    )


# ==========================================================


class CrmMov(generic_model, app.db.Model):
    __tablename__ = "crm_mov"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    numero = app.db.Column(app.db.String(10))
    data_mov = app.db.Column(app.db.Date)
    envia_email_ext = app.db.Column(app.db.String(1))
    descritivo_ext = app.db.Column(app.db.Text)
    descritivo_int = app.db.Column(app.db.Text)
    data_status = app.db.Column(app.db.Date)
    titulo = app.db.Column(app.db.String(200))

    crm_etapa_id = app.db.Column(app.db.ForeignKey("crm_etapa.id"))
    crm_etapa_id_obj = app.db.relationship("CrmEtapa")

    crm_prioridade_id = app.db.Column(app.db.ForeignKey("crm_prioridade.id"))
    crm_prioridade_id_obj = app.db.relationship("CrmPrioridade")

    crm_status_id = app.db.Column(app.db.ForeignKey("crm_status.id"))
    crm_status_id_obj = app.db.relationship("CrmStatus")

    sys_user_id_atend_ant = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_atend_ant_obj = app.db.relationship(
        "SysUser", primaryjoin="CrmMov.sys_user_id_atend_ant == SysUser.id"
    )

    sys_user_id_atend_atu = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_atend_atu_obj = app.db.relationship(
        "SysUser", primaryjoin="CrmMov.sys_user_id_atend_atu == SysUser.id"
    )

    sys_user_id_solic = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_solic_obj = app.db.relationship(
        "SysUser", primaryjoin="CrmMov.sys_user_id_solic == SysUser.id"
    )


# ==========================================================


class CrmStatusProx(generic_model, app.db.Model):
    __tablename__ = "crm_status_prox"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ordem = app.db.Column(app.db.Integer)
    tipo_status_ant = app.db.Column(app.db.String(2))

    crm_status_id = app.db.Column(app.db.ForeignKey("crm_status.id"))

    crm_status_id_prox = app.db.Column(app.db.ForeignKey("crm_status.id"))
    crm_status_id_prox_obj = app.db.relationship(
        "CrmStatus", primaryjoin="CrmStatusProx.crm_status_id_prox == CrmStatus.id"
    )


# ==========================================================


class CrmClass(generic_model, app.db.Model):
    __tablename__ = "crm_class"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_class = app.db.Column(app.db.String(50))

    crm_class_subgrupo_id = app.db.Column(app.db.ForeignKey("crm_class_subgrupo.id"))
    crm_class_subgrupo_id_obj = app.db.relationship("CrmClassSubgrupo")


# ==========================================================


class CrmMovHist(generic_model, app.db.Model):
    __tablename__ = "crm_mov_hist"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_hist = app.db.Column(app.db.Date)
    descritivo = app.db.Column(app.db.Text)
    visual_ext = app.db.Column(app.db.String(1))
    envia_email_ext = app.db.Column(app.db.String(1))

    crm_mov_id = app.db.Column(app.db.ForeignKey("crm_mov.id"))
    crm_mov_id_obj = app.db.relationship("CrmMov")

    sys_user_id_hist = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")


# ==========================================================


class CrmMovTag(generic_model, app.db.Model):
    __tablename__ = "crm_mov_tag"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    crm_mov_id = app.db.Column(app.db.ForeignKey("crm_mov.id"))
    crm_mov_id_obj = app.db.relationship("CrmMov")
