import app
from sqlalchemy import Text
from app.generics.generic_model import generic_model


# ==========================================================


class IndCjd(generic_model, app.db.Model):
    __tablename__ = "ind_cjd"

    nome = app.db.Column(app.db.String(250))
    ativo = app.db.Column(app.db.String(1))
    nome_tecnico = app.db.Column(app.db.String(50))
    ind_cjd_ftd_childs = app.db.relationship("IndCjdFtd", cascade="all,delete-orphan")


# ==========================================================


class IndCnd(generic_model, app.db.Model):
    __tablename__ = "ind_cnd"

    nome = app.db.Column(app.db.String(250))
    ativo = app.db.Column(app.db.String(1))
    tipo = app.db.Column(app.db.String(2))
    config_cnd = app.db.Column(Text)
    sigla_ind_cnd = app.db.Column(app.db.String(50))


# ==========================================================


class IndPnl(generic_model, app.db.Model):
    __tablename__ = "ind_pnl"

    nome = app.db.Column(app.db.String(250))
    tipo = app.db.Column(app.db.String(1))
    icon = app.db.Column(app.db.String(50))

    ind_pnl_rel_childs = app.db.relationship("IndPnlRel", cascade="all,delete-orphan")


# ==========================================================


class IndLegenda(generic_model, app.db.Model):
    __tablename__ = "ind_legenda"
    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    sigla_ind_legenda = app.db.Column(app.db.String(50))
    nome = app.db.Column(app.db.String(250))
    ativo = app.db.Column(app.db.String(1))

    ind_legenda_config_childs = app.db.relationship(
        "IndLegendaConfig", cascade="all,delete-orphan"
    )


# ==========================================================


class IndLegendaConfig(generic_model, app.db.Model):
    __tablename__ = "ind_legenda_config"
    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    qnt_de = app.db.Column(app.db.Numeric(18, 6))
    qnt_ate = app.db.Column(app.db.Numeric(18, 6))
    cor = app.db.Column(app.db.String(50))
    icon = app.db.Column(app.db.String(50))
    observacao = app.db.Column(app.db.String(250))

    ind_legenda_id = app.db.Column(app.db.ForeignKey("ind_legenda.id"))


# ==========================================================


class IndPrm(generic_model, app.db.Model):
    __tablename__ = "ind_prm"

    nome = app.db.Column(app.db.String(250))
    ativo = app.db.Column(app.db.String(1))
    nome_tecnico = app.db.Column(app.db.String(100))
    tipo_dado = app.db.Column(app.db.String(2))
    tipo_entrada = app.db.Column(app.db.String(2))
    internal = app.db.Column(app.db.String(1))
    busca_tabela = app.db.Column(app.db.String(50))
    busca_campo_nome = app.db.Column(app.db.String(50))
    busca_campo_id = app.db.Column(app.db.String(50))
    busca_valores = app.db.Column(app.db.String(250))
    obrigatorio = app.db.Column(app.db.String(1))
    valor_padrao = app.db.Column(Text)
    visivel = app.db.Column(app.db.String(1))
    busca_tabela_classe = app.db.Column(app.db.String(50))
    busca_campo_nome_classe = app.db.Column(app.db.String(50))
    busca_campo_id_classe = app.db.Column(app.db.String(50))
    valor_prefixo = app.db.Column(app.db.String(250))
    valor_sufixo = app.db.Column(app.db.String(250))
    ind_ftd_id = app.db.Column(app.db.ForeignKey("ind_ftd.id"))
    ind_ftd_id_obj = app.db.relationship("IndFtd")


# ==========================================================


class IndIndic(generic_model, app.db.Model):
    __tablename__ = "ind_indic"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    sigla_ind = app.db.Column(app.db.String(50))
    nome = app.db.Column(app.db.String(100))
    ger_umedida_id = app.db.Column(app.db.ForeignKey("ger_umedida.id"))
    ger_umedida_id_obj = app.db.relationship("GerUmedida")
    casas_dec = app.db.Column(app.db.Integer)
    campo_ordenacao = app.db.Column(app.db.String(50))
    metodo_ordenacao = app.db.Column(app.db.Integer)
    totalizador_atributo = app.db.Column(app.db.Integer)
    exibir_media_real = app.db.Column(app.db.String(1))
    exibir_media_meta = app.db.Column(app.db.String(1))
    exibir_dia = app.db.Column(app.db.String(1))
    exibir_semana = app.db.Column(app.db.String(1))
    exibir_quinzena = app.db.Column(app.db.String(1))
    exibir_mes = app.db.Column(app.db.String(1))
    exibir_bimestre = app.db.Column(app.db.String(1))
    exibir_trimestre = app.db.Column(app.db.String(1))
    exibir_quadrimestre = app.db.Column(app.db.String(1))
    exibir_semestre = app.db.Column(app.db.String(1))
    exibir_ano = app.db.Column(app.db.String(1))
    acumular_semana = app.db.Column(app.db.String(1))
    acumular_quinzena = app.db.Column(app.db.String(1))
    acumular_mes = app.db.Column(app.db.String(1))
    acumular_bimestre = app.db.Column(app.db.String(1))
    acumular_trimestre = app.db.Column(app.db.String(1))
    acumular_quadrimestre = app.db.Column(app.db.String(1))
    acumular_semestre = app.db.Column(app.db.String(1))
    acumular_ano = app.db.Column(app.db.String(1))
    tipo_acumulo = app.db.Column(app.db.Integer)
    ind_indic_id_pond = app.db.Column(app.db.ForeignKey("ind_indic.id"))
    grafico_tipo_atributo = app.db.Column(app.db.Integer)
    grafico_valor_vazio_zero = app.db.Column(app.db.String(1))
    grafico_tipo_ind = app.db.Column(app.db.Integer)
    ativo = app.db.Column(app.db.String(1))
    tipo_meta = app.db.Column(app.db.String(1))
    tipo_meta_var = app.db.Column(app.db.String(1))
    exibir_dia_ant = app.db.Column(app.db.Integer)
    exibir_dia_pos = app.db.Column(app.db.Integer)
    exibir_semana_ant = app.db.Column(app.db.Integer)
    exibir_semana_pos = app.db.Column(app.db.Integer)
    exibir_quinzena_ant = app.db.Column(app.db.Integer)
    exibir_quinzena_pos = app.db.Column(app.db.Integer)
    exibir_mes_ant = app.db.Column(app.db.Integer)
    exibir_mes_pos = app.db.Column(app.db.Integer)
    exibir_bimestre_ant = app.db.Column(app.db.Integer)
    exibir_bimestre_pos = app.db.Column(app.db.Integer)
    exibir_trimestre_ant = app.db.Column(app.db.Integer)
    exibir_trimestre_pos = app.db.Column(app.db.Integer)
    exibir_quadrimestre_ant = app.db.Column(app.db.Integer)
    exibir_quadrimestre_pos = app.db.Column(app.db.Integer)
    exibir_semestre_ant = app.db.Column(app.db.Integer)
    exibir_semestre_pos = app.db.Column(app.db.Integer)
    exibir_ano_ant = app.db.Column(app.db.Integer)
    exibir_ano_pos = app.db.Column(app.db.Integer)

    ind_legenda_id = app.db.Column(app.db.ForeignKey("ind_legenda.id"))
    ind_legenda_id_obj = app.db.relationship("IndLegenda")

    ind_indic_indic_childs = app.db.relationship(
        "IndIndicIndic",
        primaryjoin="IndIndic.id == IndIndicIndic.ind_indic_id",
        cascade="all,delete-orphan",
    )

    ind_indic_subgrupo_childs = app.db.relationship(
        "IndIndicSubgrupo",
        primaryjoin="IndIndic.id == IndIndicSubgrupo.ind_indic_id",
        cascade="all,delete-orphan",
    )


# ==========================================================


class IndFtd(generic_model, app.db.Model):
    __tablename__ = "ind_ftd"

    nome = app.db.Column(app.db.String(250))
    ativo = app.db.Column(app.db.String(1))
    config_ftd = app.db.Column(Text)
    nome_tecnico = app.db.Column(app.db.String(50))
    ind_cnd_id = app.db.Column(app.db.ForeignKey("ind_cnd.id"))
    ind_cnd_id_obj = app.db.relationship("IndCnd")

    ind_ftd_prm_childs = app.db.relationship(
        "IndFtdPrm",
        primaryjoin="IndFtdPrm.ind_ftd_id == IndFtd.id",
        cascade="all,delete-orphan",
    )


# ==========================================================


class IndGrupo(generic_model, app.db.Model):
    __tablename__ = "ind_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    ordem_exibicao = app.db.Column(
        app.db.Integer,
    )
    sigla_grupo = app.db.Column(app.db.String(50))

    ind_grupo_subgrupo_childs = app.db.relationship(
        "IndGrupoSubgrupo", cascade="all,delete-orphan"
    )


# ==========================================================


class IndSubgrupo(generic_model, app.db.Model):
    __tablename__ = "ind_subgrupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    ordem_exibicao = app.db.Column(app.db.Integer)
    sigla_subgrupo = app.db.Column(app.db.String(50))


# ==========================================================


class IndUnitParam(generic_model, app.db.Model):
    __tablename__ = "ind_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================


class IndCjdFtd(generic_model, app.db.Model):
    __tablename__ = "ind_cjd_ftd"

    ind_cjd_id = app.db.Column(app.db.ForeignKey("ind_cjd.id"))

    ind_ftd_id = app.db.Column(app.db.ForeignKey("ind_ftd.id"))
    ind_ftd_id_obj = app.db.relationship("IndFtd")


# ==========================================================


class IndFtdPrm(generic_model, app.db.Model):
    __tablename__ = "ind_ftd_prm"

    ind_ftd_id = app.db.Column(app.db.ForeignKey("ind_ftd.id"))

    ind_prm_id = app.db.Column(app.db.ForeignKey("ind_prm.id"))
    ind_prm_id_obj = app.db.relationship("IndPrm")


# ==========================================================


class IndGrupoSubgrupo(generic_model, app.db.Model):
    __tablename__ = "ind_grupo_subgrupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ind_grupo_id = app.db.Column(app.db.ForeignKey("ind_grupo.id"))

    ind_subgrupo_id = app.db.Column(app.db.ForeignKey("ind_subgrupo.id"))
    ind_subgrupo_id_obj = app.db.relationship("IndSubgrupo")


# ==========================================================


class IndRel(generic_model, app.db.Model):
    __tablename__ = "ind_rel"

    nome = app.db.Column(app.db.String(250))
    nome_tecnico = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    tipo = app.db.Column(app.db.String(1))

    ind_cjd_id = app.db.Column(app.db.ForeignKey("ind_cjd.id"))
    ind_cjd_id_obj = app.db.relationship("IndCjd")

    ind_ftd_id = app.db.Column(app.db.ForeignKey("ind_ftd.id"))
    ind_ftd_id_obj = app.db.relationship("IndFtd")

    ind_rel_var_childs = app.db.relationship("IndRelVar", cascade="all,delete-orphan")
    ind_rel_prm_childs = app.db.relationship("IndRelPrm", cascade="all,delete-orphan")


# ==========================================================


class IndIndicIndic(generic_model, app.db.Model):
    __tablename__ = "ind_indic_indic"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ind_indic_id = app.db.Column(app.db.ForeignKey("ind_indic.id"))

    ind_indic_id_relac = app.db.Column(app.db.ForeignKey("ind_indic.id"))
    ind_indic_id_relac_obj = app.db.relationship(
        "IndIndic", primaryjoin="IndIndicIndic.ind_indic_id_relac == IndIndic.id"
    )


# ==========================================================


class IndIndicSubgrupo(generic_model, app.db.Model):
    __tablename__ = "ind_indic_subgrupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ind_indic_id = app.db.Column(app.db.ForeignKey("ind_indic.id"))

    ind_subgrupo_id = app.db.Column(app.db.ForeignKey("ind_subgrupo.id"))
    ind_subgrupo_id_obj = app.db.relationship("IndSubgrupo")


# ==========================================================


class IndPnlRel(generic_model, app.db.Model):
    __tablename__ = "ind_pnl_rel"

    ind_rel_id = app.db.Column(app.db.ForeignKey("ind_rel.id"))
    ind_rel_id_obj = app.db.relationship("IndRel")

    ind_pnl_id = app.db.Column(app.db.ForeignKey("ind_pnl.id"))


# ==========================================================


class IndRelPrm(generic_model, app.db.Model):
    __tablename__ = "ind_rel_prm"

    ind_prm_id = app.db.Column(app.db.ForeignKey("ind_prm.id"))
    ind_prm_id_obj = app.db.relationship("IndPrm")
    ordem_exib = app.db.Column(app.db.Integer)
    valor_padrao = app.db.Column(app.db.String(100))

    ind_rel_id = app.db.Column(app.db.ForeignKey("ind_rel.id"))


# ==========================================================


class IndRelVar(generic_model, app.db.Model):
    __tablename__ = "ind_rel_var"

    var_nome_tecnico = app.db.Column(app.db.String(50))
    var_nome_descritivo = app.db.Column(app.db.String(50))
    var_agrupavel = app.db.Column(app.db.String(1))
    ordem_padrao = app.db.Column(app.db.Integer)
    largura = app.db.Column(app.db.Numeric(18, 2))
    visivel = app.db.Column(app.db.String(1))
    var_nome_tecnico_prefixo = app.db.Column(app.db.String(50))

    ind_rel_id = app.db.Column(app.db.ForeignKey("ind_rel.id"))


# ==========================================================


class IndVrAno(generic_model, app.db.Model):
    __tablename__ = "ind_vr_ano"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")
    ger_per_id = app.db.Column(app.db.ForeignKey("ger_per.id"))
    ger_per_id_obj = app.db.relationship("GerPer")
    ind_indic_id = app.db.Column(app.db.String(36))
    atributo = app.db.Column(app.db.String(100))
    valor_real = app.db.Column(app.db.Numeric(18, 6))
    valor_meta = app.db.Column(app.db.Numeric(18, 6))
    aprovado_exibicao = app.db.Column(app.db.String(1))
    import_id = app.db.Column(app.db.String(50))
    import_arquivo = app.db.Column(app.db.String(100))
    atributo1 = app.db.Column(app.db.String(100))
    atributo2 = app.db.Column(app.db.String(100))
    atributo3 = app.db.Column(app.db.String(100))
    atributo4 = app.db.Column(app.db.String(100))
    atributo5 = app.db.Column(app.db.String(100))
    atributo_nivel = app.db.Column(app.db.Integer)


# ==========================================================


class IndVrBimestre(generic_model, app.db.Model):
    __tablename__ = "ind_vr_bimestre"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")
    ger_per_id = app.db.Column(app.db.ForeignKey("ger_per.id"))
    ger_per_id_obj = app.db.relationship("GerPer")
    ind_indic_id = app.db.Column(app.db.String(36))
    atributo = app.db.Column(app.db.String(100))
    valor_real = app.db.Column(app.db.Numeric(18, 6))
    valor_meta = app.db.Column(app.db.Numeric(18, 6))
    aprovado_exibicao = app.db.Column(app.db.String(1))
    import_id = app.db.Column(app.db.String(50))
    import_arquivo = app.db.Column(app.db.String(100))
    atributo1 = app.db.Column(app.db.String(100))
    atributo2 = app.db.Column(app.db.String(100))
    atributo3 = app.db.Column(app.db.String(100))
    atributo4 = app.db.Column(app.db.String(100))
    atributo5 = app.db.Column(app.db.String(100))
    atributo_nivel = app.db.Column(app.db.Integer)


# ==========================================================


class IndVrDia(generic_model, app.db.Model):
    __tablename__ = "ind_vr_dia"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")
    ger_per_id = app.db.Column(app.db.ForeignKey("ger_per.id"))
    ger_per_id_obj = app.db.relationship("GerPer")
    ind_indic_id = app.db.Column(app.db.String(36))
    atributo = app.db.Column(app.db.String(100))
    valor_real = app.db.Column(app.db.Numeric(18, 6))
    valor_meta = app.db.Column(app.db.Numeric(18, 6))
    aprovado_exibicao = app.db.Column(app.db.String(1))
    import_id = app.db.Column(app.db.String(50))
    import_arquivo = app.db.Column(app.db.String(100))
    atributo1 = app.db.Column(app.db.String(100))
    atributo2 = app.db.Column(app.db.String(100))
    atributo3 = app.db.Column(app.db.String(100))
    atributo4 = app.db.Column(app.db.String(100))
    atributo5 = app.db.Column(app.db.String(100))
    atributo_nivel = app.db.Column(app.db.Integer)


# ==========================================================


class IndVrMes(generic_model, app.db.Model):
    __tablename__ = "ind_vr_mes"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")
    ger_per_id = app.db.Column(app.db.ForeignKey("ger_per.id"))
    ger_per_id_obj = app.db.relationship("GerPer")
    ind_indic_id = app.db.Column(app.db.String(36))
    atributo = app.db.Column(app.db.String(100))
    valor_real = app.db.Column(app.db.Numeric(18, 6))
    valor_meta = app.db.Column(app.db.Numeric(18, 6))
    aprovado_exibicao = app.db.Column(app.db.String(1))
    import_id = app.db.Column(app.db.String(50))
    import_arquivo = app.db.Column(app.db.String(100))
    atributo1 = app.db.Column(app.db.String(100))
    atributo2 = app.db.Column(app.db.String(100))
    atributo3 = app.db.Column(app.db.String(100))
    atributo4 = app.db.Column(app.db.String(100))
    atributo5 = app.db.Column(app.db.String(100))
    atributo_nivel = app.db.Column(app.db.Integer)


# ==========================================================


class IndVrQuadrimestre(generic_model, app.db.Model):
    __tablename__ = "ind_vr_quadrimestre"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")
    ger_per_id = app.db.Column(app.db.ForeignKey("ger_per.id"))
    ger_per_id_obj = app.db.relationship("GerPer")
    ind_indic_id = app.db.Column(app.db.String(36))
    atributo = app.db.Column(app.db.String(100))
    valor_real = app.db.Column(app.db.Numeric(18, 6))
    valor_meta = app.db.Column(app.db.Numeric(18, 6))
    aprovado_exibicao = app.db.Column(app.db.String(1))
    import_id = app.db.Column(app.db.String(50))
    import_arquivo = app.db.Column(app.db.String(100))
    atributo1 = app.db.Column(app.db.String(100))
    atributo2 = app.db.Column(app.db.String(100))
    atributo3 = app.db.Column(app.db.String(100))
    atributo4 = app.db.Column(app.db.String(100))
    atributo5 = app.db.Column(app.db.String(100))
    atributo_nivel = app.db.Column(app.db.Integer)


# ==========================================================


class IndVrQuinzena(generic_model, app.db.Model):
    __tablename__ = "ind_vr_quinzena"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")
    ger_per_id = app.db.Column(app.db.ForeignKey("ger_per.id"))
    ger_per_id_obj = app.db.relationship("GerPer")
    ind_indic_id = app.db.Column(app.db.String(36))
    atributo = app.db.Column(app.db.String(100))
    valor_real = app.db.Column(app.db.Numeric(18, 6))
    valor_meta = app.db.Column(app.db.Numeric(18, 6))
    aprovado_exibicao = app.db.Column(app.db.String(1))
    import_id = app.db.Column(app.db.String(50))
    import_arquivo = app.db.Column(app.db.String(100))
    atributo1 = app.db.Column(app.db.String(100))
    atributo2 = app.db.Column(app.db.String(100))
    atributo3 = app.db.Column(app.db.String(100))
    atributo4 = app.db.Column(app.db.String(100))
    atributo5 = app.db.Column(app.db.String(100))
    atributo_nivel = app.db.Column(app.db.Integer)


# ==========================================================


class IndVrSemana(generic_model, app.db.Model):
    __tablename__ = "ind_vr_semana"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")
    ger_per_id = app.db.Column(app.db.ForeignKey("ger_per.id"))
    ger_per_id_obj = app.db.relationship("GerPer")
    ind_indic_id = app.db.Column(app.db.String(36))
    atributo = app.db.Column(app.db.String(100))
    valor_real = app.db.Column(app.db.Numeric(18, 6))
    valor_meta = app.db.Column(app.db.Numeric(18, 6))
    aprovado_exibicao = app.db.Column(app.db.String(1))
    import_id = app.db.Column(app.db.String(50))
    import_arquivo = app.db.Column(app.db.String(100))
    atributo1 = app.db.Column(app.db.String(100))
    atributo2 = app.db.Column(app.db.String(100))
    atributo3 = app.db.Column(app.db.String(100))
    atributo4 = app.db.Column(app.db.String(100))
    atributo5 = app.db.Column(app.db.String(100))
    atributo_nivel = app.db.Column(app.db.Integer)


# ==========================================================


class IndVrSemestre(generic_model, app.db.Model):
    __tablename__ = "ind_vr_semestre"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")
    ger_per_id = app.db.Column(app.db.ForeignKey("ger_per.id"))
    ger_per_id_obj = app.db.relationship("GerPer")
    ind_indic_id = app.db.Column(app.db.String(36))
    atributo = app.db.Column(app.db.String(100))
    valor_real = app.db.Column(app.db.Numeric(18, 6))
    valor_meta = app.db.Column(app.db.Numeric(18, 6))
    aprovado_exibicao = app.db.Column(app.db.String(1))
    import_id = app.db.Column(app.db.String(50))
    import_arquivo = app.db.Column(app.db.String(100))
    atributo1 = app.db.Column(app.db.String(100))
    atributo2 = app.db.Column(app.db.String(100))
    atributo3 = app.db.Column(app.db.String(100))
    atributo4 = app.db.Column(app.db.String(100))
    atributo5 = app.db.Column(app.db.String(100))
    atributo_nivel = app.db.Column(app.db.Integer)


# ==========================================================


class IndVrTrimestre(generic_model, app.db.Model):
    __tablename__ = "ind_vr_trimestre"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")
    ger_per_id = app.db.Column(app.db.ForeignKey("ger_per.id"))
    ger_per_id_obj = app.db.relationship("GerPer")
    ind_indic_id = app.db.Column(app.db.String(36))
    atributo = app.db.Column(app.db.String(100))
    valor_real = app.db.Column(app.db.Numeric(18, 6))
    valor_meta = app.db.Column(app.db.Numeric(18, 6))
    aprovado_exibicao = app.db.Column(app.db.String(1))
    import_id = app.db.Column(app.db.String(50))
    import_arquivo = app.db.Column(app.db.String(100))
    atributo1 = app.db.Column(app.db.String(100))
    atributo2 = app.db.Column(app.db.String(100))
    atributo3 = app.db.Column(app.db.String(100))
    atributo4 = app.db.Column(app.db.String(100))
    atributo5 = app.db.Column(app.db.String(100))
    atributo_nivel = app.db.Column(app.db.Integer)


# ==========================================================


class IndVrMeta(generic_model, app.db.Model):
    __tablename__ = "ind_vr_meta"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")
    ger_per_id = app.db.Column(app.db.ForeignKey("ger_per.id"))
    ger_per_id_obj = app.db.relationship("GerPer")
    ind_indic_id = app.db.Column(app.db.String(36))
    atributo = app.db.Column(app.db.String(36))
    valor_meta = app.db.Column(app.db.Numeric(18, 6))
    aprovado_exibicao = app.db.Column(app.db.String(1))
    ordem = app.db.Column(app.db.String(36))
    import_id = app.db.Column(app.db.String(50))
    import_arquivo = app.db.Column(app.db.String(100))
    atributo1 = app.db.Column(app.db.String(100))
    atributo2 = app.db.Column(app.db.String(100))
    atributo3 = app.db.Column(app.db.String(100))
    atributo4 = app.db.Column(app.db.String(100))
    atributo5 = app.db.Column(app.db.String(100))
    atributo_nivel = app.db.Column(app.db.Integer)


# ==========================================================
