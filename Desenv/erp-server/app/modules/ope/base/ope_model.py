import app

from app.generics.generic_model import generic_model


# ==========================================================


class OpeCentroTipo(generic_model, app.db.Model):
    __tablename__ = "ope_centro_tipo"

    nome = app.db.Column(app.db.String(100))
    tipo_es = app.db.Column(app.db.String(1))


# ==========================================================


class OpeAtividadeGrupo(generic_model, app.db.Model):
    __tablename__ = "ope_atividade_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_atividade_grupo = app.db.Column(app.db.String(50))
    ordem = app.db.Column(app.db.String(3))


# ==========================================================


class OpeAtividadeSistema(generic_model, app.db.Model):
    __tablename__ = "ope_atividade_sistema"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_atividade_sistema = app.db.Column(app.db.String(50))


# ==========================================================


class OpeCentro2OrdStatus(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_ord_status"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ord_status = app.db.Column(app.db.String(50))
    tipo_status = app.db.Column(app.db.String(1))


# ==========================================================


class OpeCentro2OrdTipo(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_ord_tipo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ord_tipo = app.db.Column(app.db.String(50))
    valida_saldo_area_aberta = app.db.Column(app.db.String(1))
    valida_prev_itemserv = app.db.Column(app.db.String(1))
    valida_prev_rec = app.db.Column(app.db.String(1))
    valida_regra_config = app.db.Column(app.db.String(1))
    valida_tipo_executor = app.db.Column(app.db.String(2))
    valida_rec_equip = app.db.Column(app.db.String(1))
    valida_rec_pessoa = app.db.Column(app.db.String(1))
    valida_itemserv_i = app.db.Column(app.db.String(1))
    valida_itemserv_s = app.db.Column(app.db.String(1))
    valida_tipo_prop_rec_equip = app.db.Column(app.db.String(2))
    valida_tipo_prop_rec_pessoa = app.db.Column(app.db.String(2))


# ==========================================================


class OpeCentroSubtipo(generic_model, app.db.Model):
    __tablename__ = "ope_centro_subtipo"

    nome = app.db.Column(app.db.String(100))
    tipo_destinacao = app.db.Column(app.db.String(1))

    ope_centro_tipo_id = app.db.Column(app.db.ForeignKey("ope_centro_tipo.id"))
    ope_centro_tipo_id_obj = app.db.relationship("OpeCentroTipo")

    sigla_centro_subtipo = app.db.Column(app.db.String(50))


# ==========================================================


class OpeCentroVersao(generic_model, app.db.Model):
    __tablename__ = "ope_centro_versao"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_versao = app.db.Column(app.db.String(50))
    versao_atual = app.db.Column(app.db.String(1))
    data_per_ini = app.db.Column(app.db.Date)
    data_per_fin = app.db.Column(app.db.Date)
    tipo_per = app.db.Column(app.db.String(1))


# ==========================================================


class OpeCicloVar(generic_model, app.db.Model):
    __tablename__ = "ope_ciclo_var"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ope_ciclo_var = app.db.Column(app.db.String(50))


# ==========================================================


class OpeCompartGrupo(generic_model, app.db.Model):
    __tablename__ = "ope_compart_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_compart_grupo = app.db.Column(app.db.String(50))


# ==========================================================


class OpeCompartMedida(generic_model, app.db.Model):
    __tablename__ = "ope_compart_medida"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_compart_medida = app.db.Column(app.db.String(50))


# ==========================================================


class OpeCompartPosicao(generic_model, app.db.Model):
    __tablename__ = "ope_compart_posicao"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_compart_posicao = app.db.Column(app.db.String(50))
    numero_eixo = app.db.Column(app.db.Integer)
    posicao = app.db.Column(app.db.String(1))
    banda_montagem = app.db.Column(app.db.String(1))
    lado_montagem = app.db.Column(app.db.String(1))


# ==========================================================


class OpeCompartStatus(generic_model, app.db.Model):
    __tablename__ = "ope_compart_status"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_compart_status = app.db.Column(app.db.String(50))
    tipo_status = app.db.Column(app.db.String(1))


# ==========================================================


class OpeEspac(generic_model, app.db.Model):
    __tablename__ = "ope_espac"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_espac = app.db.Column(app.db.String(50))


# ==========================================================


class OpeEstagio(generic_model, app.db.Model):
    __tablename__ = "ope_estagio"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_estagio = app.db.Column(app.db.String(50))


# ==========================================================


class OpeOcorGrupo(generic_model, app.db.Model):
    __tablename__ = "ope_ocor_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ocor_grupo = app.db.Column(app.db.String(50))


# ==========================================================


class OpeOcorStatus(generic_model, app.db.Model):
    __tablename__ = "ope_ocor_status"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ocor_status = app.db.Column(app.db.String(50))
    tipo_status = app.db.Column(app.db.String(1))


# ==========================================================


class OpeOcorTipo(generic_model, app.db.Model):
    __tablename__ = "ope_ocor_tipo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ocor_tipo = app.db.Column(app.db.String(50))
    tipo = app.db.Column(app.db.String(1))
    obrig_ope_compart = app.db.Column(app.db.String(1))


# ==========================================================


class OpePeriodo(generic_model, app.db.Model):
    __tablename__ = "ope_periodo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_periodo = app.db.Column(app.db.String(50))
    data_ini = app.db.Column(app.db.Date)
    data_fin = app.db.Column(app.db.Date)


# ==========================================================


class OpeRegiao(generic_model, app.db.Model):
    __tablename__ = "ope_regiao"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_regiao = app.db.Column(app.db.String(50))


# ==========================================================


class OpeTipoSolo(generic_model, app.db.Model):
    __tablename__ = "ope_tipo_solo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_tipo_solo = app.db.Column(app.db.String(50))


# ==========================================================


class OpeUnitParam(generic_model, app.db.Model):
    __tablename__ = "ope_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================


class OpeAtividade(generic_model, app.db.Model):
    __tablename__ = "ope_atividade"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_atividade = app.db.Column(app.db.String(50))
    parada = app.db.Column(app.db.String(1))
    index_bor = app.db.Column(app.db.String(50))
    largura = app.db.Column(app.db.Numeric(18, 6))
    valida_seq_medicao_trab_centro = app.db.Column(app.db.String(1))
    valida_saldo_area_aberta = app.db.Column(app.db.String(1))
    valida_prev_itemserv = app.db.Column(app.db.String(1))
    valida_prev_rec = app.db.Column(app.db.String(1))
    valida_regra_config = app.db.Column(app.db.String(1))
    valida_tipo_executor = app.db.Column(app.db.String(2))
    valida_rec_equip = app.db.Column(app.db.String(1))
    valida_rec_pessoa = app.db.Column(app.db.String(1))
    valida_itemserv_i = app.db.Column(app.db.String(1))
    valida_itemserv_s = app.db.Column(app.db.String(1))
    valida_tipo_prop_rec_equip = app.db.Column(app.db.String(2))
    valida_tipo_prop_rec_pessoa = app.db.Column(app.db.String(2))
    valida_tot_area_acum_per_centro_plan = app.db.Column(app.db.String(1))
    valida_tot_area_acum_per_centro_exec = app.db.Column(app.db.String(1))
    valida_tot_area_ord_exec = app.db.Column(app.db.String(1))

    ger_umedida_id = app.db.Column(app.db.ForeignKey("ger_umedida.id"))
    ger_umedida_id_obj = app.db.relationship("GerUmedida")

    ope_atividade_grupo_id = app.db.Column(app.db.ForeignKey("ope_atividade_grupo.id"))
    ope_atividade_grupo_id_obj = app.db.relationship("OpeAtividadeGrupo")

    ope_atividade_prod_childs = app.db.relationship(
        "OpeAtividadeProd",
        primaryjoin="OpeAtividadeProd.ope_atividade_id == OpeAtividade.id",
        cascade="all,delete-orphan",
    )


# ==========================================================


class OpeCentroGrupo(generic_model, app.db.Model):
    __tablename__ = "ope_centro_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_centro_grupo = app.db.Column(app.db.String(50))

    ope_centro_subtipo_id = app.db.Column(app.db.ForeignKey("ope_centro_subtipo.id"))
    ope_centro_subtipo_id_obj = app.db.relationship("OpeCentroSubtipo")


# ==========================================================


class OpeCentroRatTipo(generic_model, app.db.Model):
    __tablename__ = "ope_centro_rat_tipo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    tipo_ps = app.db.Column(app.db.String(1))
    observacao = app.db.Column(app.db.String(250))
    tipo_apur = app.db.Column(app.db.String(1))
    sigla_centro_rat_tipo = app.db.Column(app.db.String(50))

    ope_centro_versao_id = app.db.Column(app.db.ForeignKey("ope_centro_versao.id"))
    ope_centro_versao_id_obj = app.db.relationship("OpeCentroVersao")

    ope_centro_rat_periodo_childs = app.db.relationship(
        "OpeCentroRatPeriodo", cascade="all,delete-orphan"
    )


# ==========================================================


class OpeCompartOcor(generic_model, app.db.Model):
    __tablename__ = "ope_compart_ocor"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_compart_ocor = app.db.Column(app.db.String(50))
    tipo_ocor = app.db.Column(app.db.String(1))

    ope_compart_status_id = app.db.Column(app.db.ForeignKey("ope_compart_status.id"))
    ope_compart_status_id_obj = app.db.relationship("OpeCompartStatus")


# ==========================================================


class OpeCompartSubgrupo(generic_model, app.db.Model):
    __tablename__ = "ope_compart_subgrupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_compart_subgrupo = app.db.Column(app.db.String(50))

    ope_compart_grupo_id = app.db.Column(app.db.ForeignKey("ope_compart_grupo.id"))
    ope_compart_grupo_id_obj = app.db.relationship("OpeCompartGrupo")


# ==========================================================


class OpeCompartTipo(generic_model, app.db.Model):
    __tablename__ = "ope_compart_tipo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_compart_tipo = app.db.Column(app.db.String(50))
    tipo_compart = app.db.Column(app.db.String(1))
    qnt_lonas = app.db.Column(app.db.Numeric(18, 3))
    qnt_sulco_min = app.db.Column(
        app.db.Numeric(18, 3),
    )
    qnt_sulco_max = app.db.Column(app.db.Numeric(18, 3))

    ope_compart_medida_id = app.db.Column(app.db.ForeignKey("ope_compart_medida.id"))
    ope_compart_medida_id_obj = app.db.relationship("OpeCompartMedida")


# ==========================================================


class OpeOcor(generic_model, app.db.Model):
    __tablename__ = "ope_ocor"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ocor = app.db.Column(app.db.String(50))
    icon = app.db.Column(app.db.String(50))
    tipo = app.db.Column(app.db.String(1))
    tipo_lanc = app.db.Column(app.db.String(1))

    ger_umedida_id = app.db.Column(app.db.ForeignKey("ger_umedida.id"))
    ger_umedida_id_obj = app.db.relationship("GerUmedida")

    ope_ocor_grupo_id = app.db.Column(app.db.ForeignKey("ope_ocor_grupo.id"))
    ope_ocor_grupo_id_obj = app.db.relationship("OpeOcorGrupo")


# ==========================================================


class OpeAtividadeProd(generic_model, app.db.Model):
    __tablename__ = "ope_atividade_prod"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ordem_visual = app.db.Column(app.db.String(1))

    ope_atividade_id = app.db.Column(app.db.ForeignKey("ope_atividade.id"))

    ope_atividade_id_prod = app.db.Column(app.db.ForeignKey("ope_atividade.id"))
    ope_atividade_id_prod_obj = app.db.relationship(
        "OpeAtividade",
        primaryjoin="OpeAtividadeProd.ope_atividade_id_prod == OpeAtividade.id",
    )


# ==========================================================


class OpeCentro1(generic_model, app.db.Model):
    __tablename__ = "ope_centro1"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_centro1 = app.db.Column(app.db.String(50))
    observacao = app.db.Column(app.db.String(250))
    data_valid = app.db.Column(app.db.Date)

    ctb_comp_id = app.db.Column(app.db.ForeignKey("ctb_comp.id"))
    ctb_comp_id_obj = app.db.relationship("CtbComp")

    ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_obj = app.db.relationship("GerPessoa")

    ope_centro_subtipo_id = app.db.Column(app.db.ForeignKey("ope_centro_subtipo.id"))
    ope_centro_subtipo_id_obj = app.db.relationship("OpeCentroSubtipo")


# ==========================================================


class OpeCentroRatPeriodo(generic_model, app.db.Model):
    __tablename__ = "ope_centro_rat_periodo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_ini = app.db.Column(app.db.Date)
    tipo_rp = app.db.Column(app.db.String(1))

    ope_centro_rat_tipo_id = app.db.Column(app.db.ForeignKey("ope_centro_rat_tipo.id"))

    ope_centro_rat_fator_childs = app.db.relationship(
        "OpeCentroRatFator", cascade="all,delete-orphan"
    )


# ==========================================================


class OpeCentroRend(generic_model, app.db.Model):
    __tablename__ = "ope_centro_rend"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    observacao = app.db.Column(app.db.String(250))

    ope_atividade_id = app.db.Column(app.db.ForeignKey("ope_atividade.id"))
    ope_atividade_id_obj = app.db.relationship("OpeAtividade")

    ope_centro_versao_id = app.db.Column(app.db.ForeignKey("ope_centro_versao.id"))
    ope_centro_versao_id_obj = app.db.relationship("OpeCentroVersao")

    ope_centro_rend_fator_childs = app.db.relationship(
        "OpeCentroRendFator", cascade="all,delete-orphan"
    )


# ==========================================================


class OpeCentroSubgrupo(generic_model, app.db.Model):
    __tablename__ = "ope_centro_subgrupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_centro_subgrupo = app.db.Column(app.db.String(50))
    icon = app.db.Column(app.db.String(50))

    ctb_comp_id = app.db.Column(app.db.ForeignKey("ctb_comp.id"))
    ctb_comp_id_obj = app.db.relationship("CtbComp")

    ope_centro_grupo_id = app.db.Column(app.db.ForeignKey("ope_centro_grupo.id"))
    ope_centro_grupo_id_obj = app.db.relationship("OpeCentroGrupo")


# ==========================================================


class OpeCompart(generic_model, app.db.Model):
    __tablename__ = "ope_compart"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_compart = app.db.Column(app.db.String(50))
    capacidade = app.db.Column(app.db.Numeric(18, 6))
    valida_itemserv = app.db.Column(app.db.String(1))
    medicao_trab_centro = app.db.Column(app.db.String(1))
    data_aquisicao = app.db.Column(app.db.String(255))
    data_baixa = app.db.Column(app.db.String(255))
    data_status = app.db.Column(app.db.Date)
    observacao = app.db.Column(app.db.String(250))
    valor_aquisicao = app.db.Column(app.db.Numeric(18, 2))
    numero_serie = app.db.Column(app.db.String(100))

    ope_compart_status_id = app.db.Column(app.db.ForeignKey("ope_compart_status.id"))
    ope_compart_status_id_obj = app.db.relationship("OpeCompartStatus")

    ope_compart_subgrupo_id = app.db.Column(
        app.db.ForeignKey("ope_compart_subgrupo.id")
    )
    ope_compart_subgrupo_id_obj = app.db.relationship("OpeCompartSubgrupo")


# ==========================================================


class OpeCentro2(generic_model, app.db.Model):
    __tablename__ = "ope_centro2"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_centro2 = app.db.Column(app.db.String(50))
    utiliza_compart = app.db.Column(app.db.String(1))
    observacao = app.db.Column(app.db.String(250))
    tipo_prop = app.db.Column(app.db.String(1))
    tipo_destinacao = app.db.Column(app.db.String(1))
    tipo_ctb_comp = app.db.Column(app.db.String(1))
    medicao_trab_centro = app.db.Column(app.db.String(1))
    valida_seq_medicao_trab_centro = app.db.Column(app.db.String(1))
    data_valid = app.db.Column(app.db.Date)

    ctb_comp_id = app.db.Column(app.db.ForeignKey("ctb_comp.id"))
    ctb_comp_id_obj = app.db.relationship("CtbComp")

    ger_marca_modelo_id = app.db.Column(app.db.ForeignKey("ger_marca_modelo.id"))
    ger_marca_modelo_id_obj = app.db.relationship("GerMarcaModelo")

    ger_pessoa_endereco_id = app.db.Column(app.db.ForeignKey("ger_pessoa_endereco.id"))
    ger_pessoa_endereco_id_obj = app.db.relationship("GerPessoaEndereco")

    ger_umedida_id = app.db.Column(app.db.ForeignKey("ger_umedida.id"))
    ger_umedida_id_obj = app.db.relationship("GerUmedida")

    ope_centro1_id = app.db.Column(app.db.ForeignKey("ope_centro1.id"))
    ope_centro1_id_obj = app.db.relationship("OpeCentro1")

    ope_centro_rat_tipo_id = app.db.Column(app.db.ForeignKey("ope_centro_rat_tipo.id"))
    ope_centro_rat_tipo_id_obj = app.db.relationship("OpeCentroRatTipo")

    ope_centro_subgrupo_id = app.db.Column(app.db.ForeignKey("ope_centro_subgrupo.id"))
    ope_centro_subgrupo_id_obj = app.db.relationship("OpeCentroSubgrupo")

    ope_regiao_id = app.db.Column(app.db.ForeignKey("ope_regiao.id"))
    ope_regiao_id_obj = app.db.relationship("OpeRegiao")


# ==========================================================


class OpeCompartItemserv(generic_model, app.db.Model):
    __tablename__ = "ope_compart_itemserv"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao = app.db.Column(app.db.String(250))
    ativo = app.db.Column(app.db.String(1))
    ger_itemserv_id = app.db.Column(app.db.String(36))

    ope_compart_id = app.db.Column(app.db.ForeignKey("ope_compart.id"))
    ope_compart_id_obj = app.db.relationship("OpeCompart")


# ==========================================================


class OpeFrenteTrabalho(generic_model, app.db.Model):
    __tablename__ = "ope_frente_trabalho"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_frente_trabalho = app.db.Column(app.db.String(50))

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")


# ==========================================================


class OpeOcorCompartMov(generic_model, app.db.Model):
    __tablename__ = "ope_ocor_compart_mov"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao = app.db.Column(app.db.String(250))
    data_mov = app.db.Column(app.db.Date)
    numero = app.db.Column(app.db.String(50))

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    ger_pessoa_endereco_id_exec = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_exec_obj = app.db.relationship("GerPessoaEndereco")

    ope_ocor_compart_mov_det_childs = app.db.relationship(
        "OpeOcorCompartMovDet", cascade="all,delete-orphan"
    )


# ==========================================================


class OpeOcorMov(generic_model, app.db.Model):
    __tablename__ = "ope_ocor_mov"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao = app.db.Column(app.db.String(250))
    data_mov = app.db.Column(app.db.Date)
    numero = app.db.Column(app.db.String(50))

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    ger_pessoa_endereco_id_exec = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_obj = app.db.relationship("GerPessoaEndereco")

    ope_ocor_tipo_id = app.db.Column(app.db.ForeignKey("ope_ocor_tipo.id"))
    ope_ocor_tipo_id_obj = app.db.relationship("OpeOcorTipo")

    ope_ocor_mov_dest_childs = app.db.relationship(
        "OpeOcorMovDest", cascade="all,delete-orphan"
    )
    ope_ocor_mov_det_childs = app.db.relationship(
        "OpeOcorMovDet", cascade="all,delete-orphan"
    )


# ==========================================================


class OpeCentro2Area(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_area"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ativo = app.db.Column(app.db.String(1))
    qnt_area_prod = app.db.Column(
        app.db.Numeric(18, 6),
    )
    qnt_area_improd = app.db.Column(
        app.db.Numeric(18, 6),
    )
    qnt_plantas_estande = app.db.Column(app.db.Numeric(18, 6))
    bloco_col = app.db.Column(app.db.String(100))
    observacao = app.db.Column(app.db.String(250))
    lat_x = app.db.Column(app.db.String(100))
    long_y = app.db.Column(app.db.String(100))
    alt_z = app.db.Column(app.db.String(100))
    data_ini_plan = app.db.Column(app.db.Date)
    data_fin_plan = app.db.Column(app.db.Date)
    data_ult_plan = app.db.Column(app.db.Date)
    data_ini_col = app.db.Column(app.db.Date)
    data_fin_col = app.db.Column(app.db.Date)
    data_ult_col = app.db.Column(app.db.Date)
    data_emerg = app.db.Column(app.db.Date)
    data_florada_1 = app.db.Column(app.db.Date)

    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_obj = app.db.relationship(
        "GerItemserv", primaryjoin="OpeCentro2Area.ger_itemserv_id == GerItemserv.id"
    )

    ger_itemserv_id_ult = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv1_id_obj = app.db.relationship(
        "GerItemserv",
        primaryjoin="OpeCentro2Area.ger_itemserv_id_ult == GerItemserv.id",
    )

    ger_itemserv_var_id = app.db.Column(app.db.ForeignKey("ger_itemserv_var.id"))
    ger_itemserv_var_id_obj = app.db.relationship(
        "GerItemservVar",
        primaryjoin="OpeCentro2Area.ger_itemserv_var_id == GerItemservVar.id",
    )

    ger_itemserv_var_id_ult = app.db.Column(app.db.ForeignKey("ger_itemserv_var.id"))
    ger_itemserv_var1_id_obj = app.db.relationship(
        "GerItemservVar",
        primaryjoin="OpeCentro2Area.ger_itemserv_var_id_ult == GerItemservVar.id",
    )

    ger_umedida_id = app.db.Column(app.db.ForeignKey("ger_umedida.id"))
    ger_umedida_id_obj = app.db.relationship("GerUmedida")

    ope_atividade_sistema_id_col = app.db.Column(
        app.db.ForeignKey("ope_atividade_sistema.id")
    )
    ope_atividade_sistema_id_obj = app.db.relationship(
        "OpeAtividadeSistema",
        primaryjoin="OpeCentro2Area.ope_atividade_sistema_id_col == OpeAtividadeSistema.id",
    )

    ope_atividade_sistema_id_cult = app.db.Column(
        app.db.ForeignKey("ope_atividade_sistema.id")
    )
    ope_atividade_sistema1_id_obj = app.db.relationship(
        "OpeAtividadeSistema",
        primaryjoin="OpeCentro2Area.ope_atividade_sistema_id_cult == OpeAtividadeSistema.id",
    )

    ope_atividade_sistema_id_plan = app.db.Column(
        app.db.ForeignKey("ope_atividade_sistema.id")
    )
    ope_atividade_sistema2_id_obj = app.db.relationship(
        "OpeAtividadeSistema",
        primaryjoin="OpeCentro2Area.ope_atividade_sistema_id_plan == OpeAtividadeSistema.id",
    )

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_espac_id = app.db.Column(app.db.ForeignKey("ope_espac.id"))
    ope_espac_id_obj = app.db.relationship("OpeEspac")

    ope_estagio_id = app.db.Column(app.db.ForeignKey("ope_estagio.id"))
    ope_estagio_id_obj = app.db.relationship("OpeEstagio")

    ope_periodo_id = app.db.Column(app.db.ForeignKey("ope_periodo.id"))
    ope_periodo_id_obj = app.db.relationship("OpePeriodo")

    ope_tipo_solo_id = app.db.Column(app.db.ForeignKey("ope_tipo_solo.id"))
    ope_tipo_solo_id_obj = app.db.relationship("OpeTipoSolo")

    ope_centro2_mapa_coord_childs = app.db.relationship(
        "OpeCentro2MapaCoord", cascade="all,delete-orphan"
    )


# ==========================================================


class OpeCentro2Equip(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_equip"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    tipo_rodado = app.db.Column(app.db.String(100))
    tipo_carroceria = app.db.Column(app.db.String(100))
    placa = app.db.Column(app.db.String(100))
    renavam = app.db.Column(app.db.String(100))
    tara = app.db.Column(app.db.Numeric(18, 6))
    capacidade_kg = app.db.Column(app.db.Numeric(18, 6))
    capacidade_m3 = app.db.Column(app.db.Numeric(18, 6))
    potencia = app.db.Column(app.db.String(100))
    nr_chassi = app.db.Column(app.db.String(100))
    nr_serie = app.db.Column(app.db.String(100))
    liberado_abastec = app.db.Column(app.db.String(1))
    largura = app.db.Column(app.db.Numeric(18, 6))
    altura = app.db.Column(app.db.Numeric(18, 6))
    nr_registro_estadual = app.db.Column(app.db.String(50))
    tipo_tracao = app.db.Column(app.db.Integer)
    tipo_transp_auto_carga = app.db.Column(app.db.Integer)
    data_venc_licenciamento = app.db.Column(app.db.Date)
    data_venc_imposto = app.db.Column(app.db.Date)

    ger_cidade_id = app.db.Column(app.db.ForeignKey("ger_cidade.id"))
    ger_cidade_id_obj = app.db.relationship("GerCidade")

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_frente_trabalho_id = app.db.Column(app.db.ForeignKey("ope_frente_trabalho.id"))
    ope_frente_trabalho_id_obj = app.db.relationship("OpeFrenteTrabalho")


# ==========================================================


class OpeCentro2Estoque(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_estoque"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    tipo = app.db.Column(app.db.String(1))

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")


# ==========================================================


class OpeCentro2MovMedia(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_mov_media"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao = app.db.Column(app.db.String(250))
    qnt_media_min = app.db.Column(app.db.Numeric(18, 6))
    qnt_media_max = app.db.Column(app.db.Numeric(18, 6))
    capacidade = app.db.Column(app.db.Numeric(18, 6))
    dt_valid_ini = app.db.Column(app.db.Date)

    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_obj = app.db.relationship("GerItemserv")

    ger_marca_modelo_id = app.db.Column(app.db.ForeignKey("ger_marca_modelo.id"))
    ger_marca_modelo_id_obj = app.db.relationship("GerMarcaModelo")

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_compart_id = app.db.Column(app.db.ForeignKey("ope_compart.id"))
    ope_compart_id_obj = app.db.relationship("OpeCompart")


# ==========================================================


class OpeCentro2ParamPer(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_param_per"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    dt_valid_ini = app.db.Column(app.db.Date)

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    ope_frente_trabalho_id = app.db.Column(app.db.ForeignKey("ope_frente_trabalho.id"))
    ope_frente_trabalho_id_obj = app.db.relationship("OpeFrenteTrabalho")


# ==========================================================


class OpeCentro2Pessoa(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_pessoa"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    pto_idenf_tipo = app.db.Column(app.db.String(1))
    pto_idenf = app.db.Column(app.db.String(50))

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_frente_trabalho_id = app.db.Column(app.db.ForeignKey("ope_frente_trabalho.id"))
    ope_frente_trabalho_id_obj = app.db.relationship("OpeFrenteTrabalho")


# ==========================================================


class OpeCentroConfig(generic_model, app.db.Model):
    __tablename__ = "ope_centro_config"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    tipo_regra = app.db.Column(app.db.String(1))
    observacao = app.db.Column(app.db.String(250))
    ativo = app.db.Column(app.db.String(1))

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    ger_itemserv_grupo_id = app.db.Column(app.db.ForeignKey("ger_itemserv_grupo.id"))
    ger_itemserv_grupo_id_obj = app.db.relationship("GerItemservGrupo")

    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_obj = app.db.relationship("GerItemserv")

    ger_itemserv_subgrupo_id = app.db.Column(
        app.db.ForeignKey("ger_itemserv_subgrupo.id")
    )
    ger_itemserv_subgrupo_id_obj = app.db.relationship("GerItemservSubGrupo")

    mov_operacao_id = app.db.Column(app.db.ForeignKey("mov_operacao.id"))
    mov_operacao_id_obj = app.db.relationship("MovOperacao")

    ope_atividade_id_obj = app.db.relationship("OpeAtividade")
    ope_atividade_id = app.db.Column(app.db.ForeignKey("ope_atividade.id"))

    ope_centro1_id = app.db.Column(app.db.ForeignKey("ope_centro1.id"))
    ope_centro1_id_obj = app.db.relationship("OpeCentro1")

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_centro2_ord_tipo_id = app.db.Column(
        app.db.ForeignKey("ope_centro2_ord_tipo.id")
    )
    ope_centro2_ord_tipo_id_obj = app.db.relationship("OpeCentro2OrdTipo")

    ope_centro_grupo_id = app.db.Column(app.db.ForeignKey("ope_centro_grupo.id"))
    ope_centro_grupo_id_obj = app.db.relationship("OpeCentroGrupo")

    ope_centro_subgrupo_id = app.db.Column(app.db.ForeignKey("ope_centro_subgrupo.id"))
    ope_centro_subgrupo_id_obj = app.db.relationship("OpeCentroSubgrupo")

    ope_centro_subtipo_id = app.db.Column(app.db.ForeignKey("ope_centro_subtipo.id"))
    ope_centro_subtipo_id_obj = app.db.relationship("OpeCentroSubtipo")

    ope_centro_tipo_id = app.db.Column(app.db.ForeignKey("ope_centro_tipo.id"))
    ope_centro_tipo_id_obj = app.db.relationship("OpeCentroTipo")

    ope_compart_grupo_id = app.db.Column(app.db.ForeignKey("ope_compart_grupo.id"))
    ope_compart_grupo_id_obj = app.db.relationship("OpeCompartGrupo")

    ope_compart_id = app.db.Column(app.db.ForeignKey("ope_compart.id"))
    ope_compart_id_obj = app.db.relationship("OpeCompart")

    ope_compart_subgrupo_id = app.db.Column(
        app.db.ForeignKey("ope_compart_subgrupo.id")
    )
    ope_compart_subgrupo_id_obj = app.db.relationship("OpeCompartSubgrupo")

    ope_estagio_id = app.db.Column(app.db.ForeignKey("ope_estagio.id"))
    ope_estagio_id_obj = app.db.relationship("OpeEstagio")


# ==========================================================


class OpeCentroPrev(generic_model, app.db.Model):
    __tablename__ = "ope_centro_prev"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    qnt01 = app.db.Column(app.db.Numeric(18, 2))
    qnt02 = app.db.Column(app.db.Numeric(18, 2))
    qnt03 = app.db.Column(app.db.Numeric(18, 2))
    qnt04 = app.db.Column(app.db.Numeric(18, 2))
    qnt05 = app.db.Column(app.db.Numeric(18, 2))
    qnt06 = app.db.Column(app.db.Numeric(18, 2))
    qnt07 = app.db.Column(app.db.Numeric(18, 2))
    qnt08 = app.db.Column(app.db.Numeric(18, 2))
    qnt09 = app.db.Column(app.db.Numeric(18, 2))
    qnt10 = app.db.Column(app.db.Numeric(18, 2))
    qnt11 = app.db.Column(app.db.Numeric(18, 2))
    qnt12 = app.db.Column(app.db.Numeric(18, 2))
    qnt13 = app.db.Column(app.db.Numeric(18, 2))
    qnt14 = app.db.Column(app.db.Numeric(18, 2))
    qnt15 = app.db.Column(app.db.Numeric(18, 2))
    qnt16 = app.db.Column(app.db.Numeric(18, 2))
    qnt17 = app.db.Column(app.db.Numeric(18, 2))
    qnt18 = app.db.Column(app.db.Numeric(18, 2))
    qnt19 = app.db.Column(app.db.Numeric(18, 2))
    qnt20 = app.db.Column(app.db.Numeric(18, 2))
    qnt21 = app.db.Column(app.db.Numeric(18, 2))
    qnt22 = app.db.Column(app.db.Numeric(18, 2))
    qnt23 = app.db.Column(app.db.Numeric(18, 2))
    qnt24 = app.db.Column(app.db.Numeric(18, 2))
    qnt25 = app.db.Column(app.db.Numeric(18, 2))
    qnt26 = app.db.Column(app.db.Numeric(18, 2))
    qnt27 = app.db.Column(app.db.Numeric(18, 2))
    qnt28 = app.db.Column(app.db.Numeric(18, 2))
    qnt29 = app.db.Column(app.db.Numeric(18, 2))
    qnt30 = app.db.Column(app.db.Numeric(18, 2))
    qnt31 = app.db.Column(app.db.Numeric(18, 2))
    ordem_exec = app.db.Column(app.db.String(3))
    tipo_executor = app.db.Column(app.db.String(1))
    data_per = app.db.Column(app.db.Date)

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    ope_atividade_id = app.db.Column(app.db.ForeignKey("ope_atividade.id"))
    ope_atividade_id_obj = app.db.relationship("OpeAtividade")

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_centro2_ord_tipo_id = app.db.Column(
        app.db.ForeignKey("ope_centro2_ord_tipo.id")
    )
    ope_centro2_ord_tipo_id_obj = app.db.relationship("OpeCentro2OrdTipo")

    ope_centro_versao_id = app.db.Column(app.db.ForeignKey("ope_centro_versao.id"))
    ope_centro_versao_id_obj = app.db.relationship("OpeCentroVersao")

    ope_periodo_id = app.db.Column(app.db.ForeignKey("ope_periodo.id"))
    ope_periodo_id_obj = app.db.relationship("OpePeriodo")

    process_id = app.db.Column(app.db.ForeignKey("sys_process_log.id"))
    process_id_obj = app.db.relationship("SysProcessLog")

    ope_centro_prev_dest_childs = app.db.relationship(
        "OpeCentroPrevDest", cascade="all,delete-orphan"
    )


# ==========================================================


class OpeCentroRatFator(generic_model, app.db.Model):
    __tablename__ = "ope_centro_rat_fator"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    fator_rat = app.db.Column(app.db.Numeric(18, 6))
    perc_rat = app.db.Column(app.db.Numeric(18, 6))

    ctb_centro_id = app.db.Column(app.db.ForeignKey("ctb_centro.id"))
    ctb_centro_id_obj = app.db.relationship("CtbCentro")

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    ope_centro1_id = app.db.Column(app.db.ForeignKey("ope_centro1.id"))
    ope_centro1_id_obj = app.db.relationship("OpeCentro1")

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_centro_rat_periodo_id = app.db.Column(
        app.db.ForeignKey("ope_centro_rat_periodo.id")
    )

    ope_centro_subtipo_id = app.db.Column(app.db.ForeignKey("ope_centro_subtipo.id"))
    ope_centro_subtipo_id_obj = app.db.relationship("OpeCentroSubtipo")

    ope_periodo_id = app.db.Column(app.db.ForeignKey("ope_periodo.id"))
    ope_periodo_id_obj = app.db.relationship("OpePeriodo")


# ==========================================================


class OpeCentroRendFator(generic_model, app.db.Model):
    __tablename__ = "ope_centro_rend_fator"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    fator_rend = app.db.Column(
        app.db.Numeric(18, 4),
    )
    fator_util = app.db.Column(app.db.Numeric(18, 4))

    ctb_comp_id = app.db.Column(app.db.ForeignKey("ctb_comp.id"))
    ctb_comp_id_obj = app.db.relationship("CtbComp")

    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_obj = app.db.relationship("GerItemserv")

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_centro_rend_id = app.db.Column(app.db.ForeignKey("ope_centro_rend.id"))


# ==========================================================


class OpeOcorCompartMovDet(generic_model, app.db.Model):
    __tablename__ = "ope_ocor_compart_mov_det"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao = app.db.Column(app.db.String(250))
    qnt_medicao = app.db.Column(app.db.Numeric(18, 6))

    ope_compart_id = app.db.Column(app.db.ForeignKey("ope_compart.id"))
    ope_compart_id_obj = app.db.relationship("OpeCompart")

    ope_compart_mov_id = app.db.Column(app.db.ForeignKey("ope_ocor_compart_mov.id"))

    ope_compart_ocor_id = app.db.Column(app.db.ForeignKey("ope_compart_ocor.id"))
    ope_compart_ocor_id_obj = app.db.relationship("OpeCompartOcor")


# ==========================================================


class OpeOcorMovDest(generic_model, app.db.Model):
    __tablename__ = "ope_ocor_mov_dest"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao = app.db.Column(app.db.String(250))

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_compart_id = app.db.Column(app.db.ForeignKey("ope_compart.id"))
    ope_compart_id_obj = app.db.relationship("OpeCompart")

    ope_ocor_mov_id = app.db.Column(app.db.ForeignKey("ope_ocor_mov.id"))


# ==========================================================


class OpeOcorPrev(generic_model, app.db.Model):
    __tablename__ = "ope_ocor_prev"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao = app.db.Column(app.db.String(250))
    data_ult_solucao = app.db.Column(app.db.Date)
    qnt_limite = app.db.Column(
        app.db.Integer,
    )
    qnt_aviso = app.db.Column(
        app.db.Integer,
    )
    qnt_dia_limite = app.db.Column(
        app.db.Integer,
    )
    qnt_dia_aviso = app.db.Column(
        app.db.Integer,
    )
    data_valid_ini = app.db.Column(app.db.Date)

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_compart_id = app.db.Column(app.db.ForeignKey("ope_compart.id"))
    ope_compart_id_obj = app.db.relationship("OpeCompart")

    ope_ocor_id = app.db.Column(app.db.ForeignKey("ope_ocor.id"))
    ope_ocor_id_obj = app.db.relationship("OpeOcor")


# ==========================================================


class OpeCentro2MapaCoord(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_mapa_coord"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    lat_x = app.db.Column(app.db.String(100))
    long_y = app.db.Column(app.db.String(100))
    ordem = app.db.Column(app.db.Integer)
    ope_centro2_id_area = app.db.Column(app.db.ForeignKey("ope_centro2_area.id"))


# ==========================================================


class OpeCentro2MapaGeometria(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_mapa_geometria"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    geom = app.db.Column(index=True)

    ope_centro2_id_area = app.db.Column(app.db.ForeignKey("ope_centro2_area.id"))
    ope_centro2_area_id_obj = app.db.relationship("OpeCentro2Area")


# ==========================================================


class OpeCentro2Ord(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_ord"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_ini_exec = app.db.Column(app.db.Date)
    data_fin_exec = app.db.Column(app.db.Date)
    data_status = app.db.Column(app.db.Date)
    observacao_interna = app.db.Column(app.db.String(250))
    observacao_externa = app.db.Column(app.db.String(250))
    data_ini_exec_prev = app.db.Column(app.db.Date)
    data_fin_exec_prev = app.db.Column(app.db.Date)
    numero_ord = app.db.Column(app.db.String(50))
    data_valid = app.db.Column(app.db.Date)

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    ger_pessoa_endereco_id_exec = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_obj = app.db.relationship("GerPessoaEndereco")

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_centro2_ord_status_id = app.db.Column(
        app.db.ForeignKey("ope_centro2_ord_status.id")
    )
    ope_centro2_ord_status_id_obj = app.db.relationship("OpeCentro2OrdStatus")

    ope_centro2_ord_tipo_id = app.db.Column(
        app.db.ForeignKey("ope_centro2_ord_tipo.id")
    )
    ope_centro2_ord_tipo_id_obj = app.db.relationship("OpeCentro2OrdTipo")

    ope_centro2_pessoa_id_solic = app.db.Column(
        app.db.ForeignKey("ope_centro2_pessoa.id")
    )
    ope_centro2_pessoa_id_obj = app.db.relationship("OpeCentro2Pessoa")

    ope_centro_versao_id = app.db.Column(app.db.ForeignKey("ope_centro_versao.id"))
    ope_centro_versao_id_obj = app.db.relationship("OpeCentroVersao")

    ope_frente_trabalho_id = app.db.Column(app.db.ForeignKey("ope_frente_trabalho.id"))
    ope_frente_trabalho_id_obj = app.db.relationship("OpeFrenteTrabalho")

    ope_periodo_id = app.db.Column(app.db.ForeignKey("ope_periodo.id"))
    ope_periodo_id_obj = app.db.relationship("OpePeriodo")

    process_id = app.db.Column(app.db.ForeignKey("sys_process_log.id"))
    process_id_obj = app.db.relationship("SysProcessLog")

    ope_centro2_ord_ativ_childs = app.db.relationship(
        "OpeCentro2OrdAtiv", cascade="all,delete-orphan"
    )
    ope_centro2_ord_dest_childs = app.db.relationship(
        "OpeCentro2OrdDest", cascade="all,delete-orphan"
    )


# ==========================================================


class OpeCentroDest(generic_model, app.db.Model):
    __tablename__ = "ope_centro_dest"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    valor = app.db.Column(
        app.db.Numeric(18, 2),
    )
    qnt = app.db.Column(app.db.Numeric(18, 6))

    tipo_es = app.db.Column(app.db.String(1))

    fin_pagrec_banco_id = app.db.Column(app.db.ForeignKey("fin_pagrec_banco.id"))
    fin_pagrec_banco_id_obj = app.db.relationship("FinPagrecBanco")

    fin_pagrec_id = app.db.Column(app.db.ForeignKey("fin_pagrec.id"))
    fin_pagrec_id_obj = app.db.relationship("FinPagrec")

    mov_itemserv_id = app.db.Column(app.db.ForeignKey("mov_itemserv.id"))
    mov_itemserv_id_obj = app.db.relationship("MovItemserv")

    ope_atividade_id = app.db.Column(app.db.ForeignKey("ope_atividade.id"))
    ope_atividade_id_obj = app.db.relationship("OpeAtividade")

    ope_centro1_id = app.db.Column(app.db.ForeignKey("ope_centro1.id"))
    ope_centro1_id_obj = app.db.relationship(
        "OpeCentro1", primaryjoin="OpeCentroDest.ope_centro1_id == OpeCentro1.id"
    )

    ope_centro1_id_dest_pri = app.db.Column(app.db.ForeignKey("ope_centro1.id"))
    ope_centro11_id_obj = app.db.relationship(
        "OpeCentro1",
        primaryjoin="OpeCentroDest.ope_centro1_id_dest_pri == OpeCentro1.id",
    )

    ope_centro1_id_dest_sec = app.db.Column(app.db.ForeignKey("ope_centro1.id"))
    ope_centro12_id_obj = app.db.relationship(
        "OpeCentro1",
        primaryjoin="OpeCentroDest.ope_centro1_id_dest_sec == OpeCentro1.id",
    )

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship(
        "OpeCentro2", primaryjoin="OpeCentroDest.ope_centro2_id == OpeCentro2.id"
    )

    ope_centro2_id_dest_pri = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro21_id_obj = app.db.relationship(
        "OpeCentro2",
        primaryjoin="OpeCentroDest.ope_centro2_id_dest_pri == OpeCentro2.id",
    )

    ope_centro2_id_dest_sec = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro22_id_obj = app.db.relationship(
        "OpeCentro2",
        primaryjoin="OpeCentroDest.ope_centro2_id_dest_sec == OpeCentro2.id",
    )

    ope_compart_id_pri = app.db.Column(app.db.ForeignKey("ope_compart.id"))
    ope_compart_id_obj = app.db.relationship(
        "OpeCompart", primaryjoin="OpeCentroDest.ope_compart_id_pri == OpeCompart.id"
    )

    ope_compart_id_sec = app.db.Column(app.db.ForeignKey("ope_compart.id"))
    ope_compart1_id_obj = app.db.relationship(
        "OpeCompart", primaryjoin="OpeCentroDest.ope_compart_id_sec == OpeCompart.id"
    )

    ope_periodo_id_desc_pri = app.db.Column(app.db.ForeignKey("ope_periodo.id"))
    ope_periodo_id_obj = app.db.relationship(
        "OpePeriodo",
        primaryjoin="OpeCentroDest.ope_periodo_id_desc_pri == OpePeriodo.id",
    )

    ope_periodo_id_desc_sec = app.db.Column(app.db.ForeignKey("ope_periodo.id"))
    ope_periodo1_id_obj = app.db.relationship(
        "OpePeriodo",
        primaryjoin="OpeCentroDest.ope_periodo_id_desc_sec == OpePeriodo.id",
    )


# ==========================================================


class OpeCentroPrevDest(generic_model, app.db.Model):
    __tablename__ = "ope_centro_prev_dest"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    qnt01 = app.db.Column(app.db.Numeric(18, 2))
    qnt02 = app.db.Column(app.db.Numeric(18, 2))
    qnt03 = app.db.Column(app.db.Numeric(18, 2))
    qnt04 = app.db.Column(app.db.Numeric(18, 2))
    qnt05 = app.db.Column(app.db.Numeric(18, 2))
    qnt06 = app.db.Column(app.db.Numeric(18, 2))
    qnt07 = app.db.Column(app.db.Numeric(18, 2))
    qnt08 = app.db.Column(app.db.Numeric(18, 2))
    qnt09 = app.db.Column(app.db.Numeric(18, 2))
    qnt10 = app.db.Column(app.db.Numeric(18, 2))
    qnt11 = app.db.Column(app.db.Numeric(18, 2))
    qnt12 = app.db.Column(app.db.Numeric(18, 2))
    qnt13 = app.db.Column(app.db.Numeric(18, 2))
    qnt14 = app.db.Column(app.db.Numeric(18, 2))
    qnt15 = app.db.Column(app.db.Numeric(18, 2))
    qnt16 = app.db.Column(app.db.Numeric(18, 2))
    qnt17 = app.db.Column(app.db.Numeric(18, 2))
    qnt18 = app.db.Column(app.db.Numeric(18, 2))
    qnt19 = app.db.Column(app.db.Numeric(18, 2))
    qnt20 = app.db.Column(app.db.Numeric(18, 2))
    qnt21 = app.db.Column(app.db.Numeric(18, 2))
    qnt22 = app.db.Column(app.db.Numeric(18, 2))
    qnt23 = app.db.Column(app.db.Numeric(18, 2))
    qnt24 = app.db.Column(app.db.Numeric(18, 2))
    qnt25 = app.db.Column(app.db.Numeric(18, 2))
    qnt26 = app.db.Column(app.db.Numeric(18, 2))
    qnt27 = app.db.Column(app.db.Numeric(18, 2))
    qnt28 = app.db.Column(app.db.Numeric(18, 2))
    qnt29 = app.db.Column(app.db.Numeric(18, 2))
    qnt30 = app.db.Column(app.db.Numeric(18, 2))
    qnt31 = app.db.Column(app.db.Numeric(18, 2))
    tipo_prev = app.db.Column(app.db.String(1))

    ctb_comp_id = app.db.Column(app.db.ForeignKey("ctb_comp.id"))
    ctb_comp_id_obj = app.db.relationship("CtbComp")

    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_obj = app.db.relationship("GerItemserv")

    ope_centro1_id = app.db.Column(app.db.ForeignKey("ope_centro1.id"))
    ope_centro1_id_obj = app.db.relationship("OpeCentro1")

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")

    ope_centro_prev_id = app.db.Column(app.db.ForeignKey("ope_centro_prev.id"))

    process_id = app.db.Column(app.db.ForeignKey("sys_process_log.id"))
    process_id_obj = app.db.relationship("SysProcessLog")


# ==========================================================


class OpeOcorMovDet(generic_model, app.db.Model):
    __tablename__ = "ope_ocor_mov_det"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    observacao = app.db.Column(app.db.String(250))
    qnt_ocor = app.db.Column(app.db.Numeric(18, 6))
    qnt_ocor_calc = app.db.Column(app.db.Numeric(18, 6))
    data_status = app.db.Column(app.db.Date)
    lat_x = app.db.Column(app.db.String(50))
    long_y = app.db.Column(app.db.String(50))
    ponto = app.db.Column(app.db.String(50))

    ope_ocor_id = app.db.Column(app.db.ForeignKey("ope_ocor.id"))
    ope_ocor_id_obj = app.db.relationship("OpeOcor")

    ope_ocor_mov_dest_id = app.db.Column(app.db.ForeignKey("ope_ocor_mov_dest.id"))
    # ope_ocor_mov_dest_id_obj = app.db.relationship('OpeOcorMovDest')

    ope_ocor_mov_id = app.db.Column(app.db.ForeignKey("ope_ocor_mov.id"))

    ope_ocor_status_id = app.db.Column(app.db.ForeignKey("ope_ocor_status.id"))
    ope_ocor_status_id_obj = app.db.relationship("OpeOcorStatus")


# ==========================================================


class OpeCentro2OrdAtiv(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_ord_ativ"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao_interna = app.db.Column(app.db.String(250))
    observacao_externa = app.db.Column(app.db.String(250))
    ordem_exec = app.db.Column(app.db.String(3))
    tipo_executor = app.db.Column(app.db.String(1))
    data_valid = app.db.Column(app.db.Date)

    ope_atividade_id = app.db.Column(app.db.ForeignKey("ope_atividade.id"))
    ope_atividade_id_obj = app.db.relationship("OpeAtividade")

    ope_centro2_ord_id = app.db.Column(app.db.ForeignKey("ope_centro2_ord.id"))

    ope_frente_trabalho_id = app.db.Column(app.db.ForeignKey("ope_frente_trabalho.id"))
    ope_frente_trabalho_id_obj = app.db.relationship("OpeFrenteTrabalho")


# ==========================================================


class OpeCentro2OrdDest(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_ord_dest"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    qnt_obj = app.db.Column(app.db.Numeric(18, 6))
    qnt_prev_obj = app.db.Column(app.db.Numeric(18, 6))
    valor_unit_prev = app.db.Column(app.db.Numeric(18, 6))
    valor_total_prev = app.db.Column(app.db.Numeric(18, 6))
    observacao_interna = app.db.Column(app.db.String(250))
    observacao_externa = app.db.Column(app.db.String(250))
    valor_unit = app.db.Column(app.db.Numeric(18, 6))
    valor_total = app.db.Column(app.db.Numeric(18, 6))
    data_valid = app.db.Column(app.db.Date)

    ger_umedida_id_dest = app.db.Column(app.db.ForeignKey("ger_umedida.id"))
    ger_umedida_id_obj = app.db.relationship("GerUmedida")

    ope_centro2_ord_id = app.db.Column(app.db.ForeignKey("ope_centro2_ord.id"))

    ope_centro2_id_dest = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship("OpeCentro2")


# ==========================================================


class OpeCentro2OrdItemserv(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_ord_itemserv"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao_interna = app.db.Column(app.db.String(250))
    observacao_externa = app.db.Column(app.db.String(250))
    qnt_rend = app.db.Column(
        app.db.Numeric(18, 6),
    )
    perc_util = app.db.Column(
        app.db.Numeric(18, 6),
    )
    qnt_total_util = app.db.Column(
        app.db.Numeric(18, 6),
    )
    valor_unit_util = app.db.Column(
        app.db.Numeric(18, 6),
    )
    valor_total_util = app.db.Column(
        app.db.Numeric(18, 6),
    )
    data_valid = app.db.Column(app.db.Date)

    ctb_comp_id = app.db.Column(app.db.ForeignKey("ctb_comp.id"))
    ctb_comp_id_obj = app.db.relationship("CtbComp")

    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_obj = app.db.relationship("GerItemserv")

    ope_centro2_ord_ativ_id = app.db.Column(
        app.db.ForeignKey("ope_centro2_ord_ativ.id")
    )
    ope_centro2_ord_ativ_id_obj = app.db.relationship("OpeCentro2OrdAtiv")


# ==========================================================


class OpeCentro2OrdRec(generic_model, app.db.Model):
    __tablename__ = "ope_centro2_ord_rec"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao_interna = app.db.Column(app.db.String(250))
    observacao_externa = app.db.Column(app.db.String(250))
    qnt_rend = app.db.Column(app.db.Numeric(18, 6))
    perc_util = app.db.Column(app.db.Numeric(18, 6))
    qnt_total_util = app.db.Column(app.db.Numeric(18, 6))
    valor_unit_util = app.db.Column(app.db.Numeric(18, 6))
    valor_total_util = app.db.Column(app.db.Numeric(18, 6))
    data_valid = app.db.Column(app.db.Date)

    ctb_comp_id = app.db.Column(app.db.ForeignKey("ctb_comp.id"))
    ctb_comp_id_obj = app.db.relationship(
        "CtbComp", primaryjoin="OpeCentro2OrdRec.ctb_comp_id == CtbComp.id"
    )

    ctb_comp_id_imp01 = app.db.Column(app.db.ForeignKey("ctb_comp.id"))
    ctb_comp_id_imp01_obj = app.db.relationship(
        "CtbComp", primaryjoin="OpeCentro2OrdRec.ctb_comp_id_imp01 == CtbComp.id"
    )

    ger_pessoa_endereco_id_exec = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_exec_obj = app.db.relationship("GerPessoaEndereco")

    ope_centro1_id = app.db.Column(app.db.ForeignKey("ope_centro1.id"))
    ope_centro1_id_obj = app.db.relationship(
        "OpeCentro1", primaryjoin="OpeCentro2OrdRec.ope_centro1_id == OpeCentro1.id"
    )

    ope_centro1_id_imp01 = app.db.Column(app.db.ForeignKey("ope_centro1.id"))
    pe_centro1_id_imp01_obj = app.db.relationship(
        "OpeCentro1",
        primaryjoin="OpeCentro2OrdRec.ope_centro1_id_imp01 == OpeCentro1.id",
    )

    ope_centro2_id = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship(
        "OpeCentro2", primaryjoin="OpeCentro2OrdRec.ope_centro2_id == OpeCentro2.id"
    )

    ope_centro2_id_imp01 = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_imp01_obj = app.db.relationship(
        "OpeCentro2",
        primaryjoin="OpeCentro2OrdRec.ope_centro2_id_imp01 == OpeCentro2.id",
    )

    ope_centro2_ord_ativ_id = app.db.Column(
        app.db.ForeignKey("ope_centro2_ord_ativ.id")
    )
    ope_centro2_ord_ativ_id_obj = app.db.relationship("OpeCentro2OrdAtiv")

    ope_compart_id = app.db.Column(app.db.ForeignKey("ope_compart.id"))
    ope_compart_id_obj = app.db.relationship("OpeCompart")


# ==========================================================
