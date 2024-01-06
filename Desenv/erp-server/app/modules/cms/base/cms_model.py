import app
from app.generics.generic_model import generic_model


# ==========================================================


class CmsGrupo(generic_model, app.db.Model):
    __tablename__ = "cms_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    color = app.db.Column(app.db.String(100))
    sigla_grupo = app.db.Column(app.db.String(50))
    publico = app.db.Column(app.db.String(1))


# ==========================================================


class CmsPost(generic_model, app.db.Model):
    __tablename__ = "cms_post"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    titulo = app.db.Column(app.db.String(50))
    corpo = app.db.Column(app.db.String(50))
    status = app.db.Column(app.db.String(1))
    favorito = app.db.Column(app.db.String(1))
    util_blog = app.db.Column(app.db.String(1))
    util_depoimento = app.db.Column(app.db.String(1))
    util_treinamento = app.db.Column(app.db.String(1))
    util_help = app.db.Column(app.db.String(1))
    tipo_render = app.db.Column(app.db.String(1))
    img_url = app.db.relationship(
        "SysDocument", cascade="all,delete-orphan"
    )
    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")

    cms_post_tag_childs = app.db.relationship("CmsPostTag", cascade="all,delete-orphan")
    cms_post_grupo_childs = app.db.relationship(
        "CmsPostGrupo", cascade="all,delete-orphan"
    )



# ==========================================================


class CmsPostHist(generic_model, app.db.Model):
    __tablename__ = "cms_post_hist"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_hist = app.db.Column(app.db.Date)
    descricao = app.db.Column(app.db.String(50))
    tipo_hist = app.db.Column(app.db.String(1))

    cms_post_id = app.db.Column(app.db.ForeignKey("cms_post.id"))
    cms_post_id_obj = app.db.relationship("CmsPost")


# ==========================================================


class CmsTag(generic_model, app.db.Model):
    __tablename__ = "cms_tag"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(50))
    sigla_tag = app.db.Column(app.db.String(50))
    ativo = app.db.Column(app.db.String(1))


# ==========================================================


class CmsPostTag(generic_model, app.db.Model):
    __tablename__ = "cms_post_tag"

    cms_tag_id = app.db.Column(app.db.ForeignKey("cms_tag.id"))
    cms_tag_id_obj = app.db.relationship("CmsTag")

    cms_post_id = app.db.Column(app.db.ForeignKey("cms_post.id"))


# ==========================================================


class CmsPostGrupo(generic_model, app.db.Model):
    __tablename__ = "cms_post_grupo"

    cms_grupo_id = app.db.Column(app.db.ForeignKey("cms_grupo.id"))
    cms_grupo_id_obj = app.db.relationship("CmsGrupo")

    cms_post_id = app.db.Column(app.db.ForeignKey("cms_post.id", ondelete="CASCADE"))


# ==========================================================
