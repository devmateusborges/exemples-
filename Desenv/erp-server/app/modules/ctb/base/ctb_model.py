import app
from app.generics.generic_model import generic_model


# ==========================================================


class CtbVersao(generic_model, app.db.Model):
    __tablename__ = "ctb_versao"

    unit_id = app.db.Column(app.db.String(36))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_versao = app.db.Column(app.db.String(50))
    tipo_rp = app.db.Column(app.db.String(1))
    versao_atual = app.db.Column(app.db.String)
    data_per_ini = app.db.Column(app.db.Date)
    data_per_fin = app.db.Column(app.db.Date)


# ==========================================================


class CtbCentroGrupo(generic_model, app.db.Model):
    __tablename__ = "ctb_centro_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_centro_grupo = app.db.Column(app.db.String(50))


# ==========================================================


class CtbCompGrupo(generic_model, app.db.Model):
    __tablename__ = "ctb_comp_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_comp_grupo = app.db.Column(app.db.String(50))


# ==========================================================


class CtbContaVersao(generic_model, app.db.Model):
    __tablename__ = "ctb_conta_versao"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_versao = app.db.Column(app.db.String(50))
    versao_atual = app.db.Column(app.db.String)
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================


class CtbHistorico(generic_model, app.db.Model):
    __tablename__ = "ctb_historico"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_historico = app.db.Column(app.db.String(50))


# ==========================================================


class CtbLote(generic_model, app.db.Model):
    __tablename__ = "ctb_lote"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_lote = app.db.Column(app.db.String(50))


# ==========================================================


class CtbTipoSaldo(generic_model, app.db.Model):
    __tablename__ = "ctb_tipo_saldo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_tipo_saldo = app.db.Column(app.db.String(50))
    mes_ini_fechamento = app.db.Column(app.db.Integer)
    mes_fin_fechamento = app.db.Column(app.db.Integer)


# ==========================================================


class CtbUnitParam(generic_model, app.db.Model):
    __tablename__ = "ctb_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================


class CtbCentro(generic_model, app.db.Model):
    __tablename__ = "ctb_centro"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_centro = app.db.Column(app.db.String(50))

    ctb_centro_grupo_id = app.db.Column(app.db.ForeignKey("ctb_centro_grupo.id"))
    ctb_centro_grupo_id_obj = app.db.relationship("CtbCentroGrupo")


# ==========================================================


class CtbComp(generic_model, app.db.Model):
    __tablename__ = "ctb_comp"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_comp = app.db.Column(app.db.String(50))
    ctb_comp_id_calc_orig = app.db.Column(app.db.String(36))
    fator_calc_origem = app.db.Column(app.db.Numeric(18, 6))

    ctb_comp_grupo_id = app.db.Column(app.db.ForeignKey("ctb_comp_grupo.id"))
    ctb_comp_grupo_id_obj = app.db.relationship("CtbCompGrupo")

    ger_umedida_id = app.db.Column(app.db.ForeignKey("ger_umedida.id"))
    ger_umedida_id_obj = app.db.relationship("GerUmedida")


# ==========================================================


class CtbContaGrupo(generic_model, app.db.Model):
    __tablename__ = "ctb_conta_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_conta_grupo = app.db.Column(app.db.String(50))
    estrutura = app.db.Column(app.db.String(50))

    ctb_conta_versao_id = app.db.Column(app.db.ForeignKey("ctb_conta_versao.id"))
    ctb_conta_versao_id_obj = app.db.relationship("CtbContaVersao")


# ==========================================================


class CtbConta(generic_model, app.db.Model):
    __tablename__ = "ctb_conta"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_conta = app.db.Column(app.db.String(50))
    tipo_variacao = app.db.Column(app.db.String(1))
    tipo_dc = app.db.Column(app.db.String(1))
    tipo_conta = app.db.Column(app.db.String(2))

    ctb_conta_grupo_id = app.db.Column(app.db.ForeignKey("ctb_conta_grupo.id"))
    ctb_conta_grupo_id_obj = app.db.relationship("CtbContaGrupo")

    ctb_conta_versao_id = app.db.Column(app.db.ForeignKey("ctb_conta_versao.id"))
    ctb_conta_versao_id_obj = app.db.relationship("CtbContaVersao")


# ==========================================================


class CtbLanc(generic_model, app.db.Model):
    __tablename__ = "ctb_lanc"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    numero_lanc = app.db.Column(app.db.String(50))
    data_lanc = app.db.Column(app.db.Date)
    historico = app.db.Column(app.db.String(250))
    status = app.db.Column(app.db.String(2))
    status_observacao = app.db.Column(app.db.String(250))

    ctb_historico_id = app.db.Column(app.db.ForeignKey("ctb_historico.id"))
    ctb_historico_id_obj = app.db.relationship("CtbHistorico")

    ctb_lote_id = app.db.Column(app.db.ForeignKey("ctb_lote.id"))
    ctb_lote_id_obj = app.db.relationship("CtbLote")

    ctb_versao_id = app.db.Column(app.db.ForeignKey("ctb_versao.id"))
    ctb_versao_id_obj = app.db.relationship("CtbVersao")

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")


# ==========================================================


class CtbLancDet(generic_model, app.db.Model):
    __tablename__ = "ctb_lanc_det"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    tipo_dc = app.db.Column(app.db.String(1))
    valor = app.db.Column(app.db.Numeric(18, 2))
    origem_tipo = app.db.Column(app.db.String(50))
    origem_id = app.db.Column(app.db.String(36))
    observacao = app.db.Column(app.db.String(250))
    qnt = app.db.Column(app.db.Numeric(18, 6))

    ctb_comp_id = app.db.Column(app.db.ForeignKey("ctb_comp.id"))
    ctb_comp_id_obj = app.db.relationship("CtbComp")

    ctb_conta_id = app.db.Column(app.db.ForeignKey("ctb_conta.id"))
    ctb_conta_id_obj = app.db.relationship("CtbConta")

    ctb_lanc_id = app.db.Column(app.db.ForeignKey("ctb_lanc.id"))
    ctb_lanc_id_obj = app.db.relationship("CtbLanc")

    ope_atividade_id = app.db.Column(app.db.ForeignKey("ope_atividade.id"))
    ope_atividade_id_obj = app.db.relationship("OpeAtividade")

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    process_id = app.db.Column(app.db.ForeignKey("sys_process_log.id"))
    process_id_obj = app.db.relationship("SysProcessLog")


# ==========================================================
