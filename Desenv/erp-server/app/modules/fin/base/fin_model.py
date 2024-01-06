import app
from app.generics.generic_model import generic_model


# ==========================================================


class FinRecibo(generic_model, app.db.Model):
    __tablename__ = "fin_recibo"

    unit_id = app.db.Column(app.db.String(36))
    data_recibo = app.db.Column(app.db.app.db.Date)
    conteudo = app.db.Column(app.db.Text)
    valor = app.db.Column(app.db.Numeric(18, 2))
    ger_pessoa_endereco_id = app.db.Column(app.db.String(36))
    nome_pessoa = app.db.Column(app.db.String(100))
    nr_doc_pessoa = app.db.Column(app.db.String(50))
    tipo_doc_pessoa = app.db.Column(app.db.String(50))
    status = app.db.Column(app.db.String(2))
    status_observacao = app.db.Column(app.db.String(250))


# ==========================================================


class FinBanco(generic_model, app.db.Model):
    __tablename__ = "fin_banco"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    nr_banco = app.db.Column(app.db.String(50))


# ==========================================================


class FinClass(generic_model, app.db.Model):
    __tablename__ = "fin_class"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    tipo_es = app.db.Column(app.db.String(1))
    tipo_fluxo = app.db.Column(app.db.String(2))
    fixo_variavel = app.db.Column(app.db.String(1))
    sigla_class = app.db.Column(app.db.String(15))
    tipo_prev = app.db.Column(app.db.String(1))


# ==========================================================


class FinClassAgrup(generic_model, app.db.Model):
    __tablename__ = "fin_class_agrup"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    padrao = app.db.Column(app.db.String(1))
    fin_class_agrup_grupo_childs = app.db.relationship(
        "FinClassAgrupGrupo", cascade="all,delete-orphan"
    )


# ==========================================================


class FinClassGrupo(generic_model, app.db.Model):
    __tablename__ = "fin_class_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    estrutura = app.db.Column(app.db.String(50))
    sigla_class_grupo = app.db.Column(app.db.String(255))
    ativo = app.db.Column(app.db.String(1))


# ==========================================================


class FinCondPagrec(generic_model, app.db.Model):
    __tablename__ = "fin_cond_pagrec"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    sigla_cond_pagamento = app.db.Column(app.db.String(50))
    considera_feriado = app.db.Column(app.db.String(1))
    considera_final_sem = app.db.Column(app.db.String(1))
    qnt_dia_ini = app.db.Column(app.db.app.db.Integer)
    observacao = app.db.Column(app.db.String(250))
    tipo_prazo = app.db.Column(app.db.String(1))
    ativo = app.db.Column(app.db.String(1))


# ==========================================================


class FinPagrecTipo(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_tipo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    aceita_entrada = app.db.Column(app.db.String(1))
    aceita_saida = app.db.Column(app.db.String(1))
    ativo = app.db.Column(app.db.String(1))
    sigla_fin_pagrec_tipo = app.db.Column(app.db.String(100))


# ==========================================================


class FinPagrecVersao(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_versao"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))

    sigla_versao = app.db.Column(app.db.String(50))
    data_per_ini = app.db.Column(app.db.app.db.Date)
    data_per_fin = app.db.Column(app.db.app.db.Date)

    versao_atual = app.db.Column(app.db.String(1))
    tipo_per = app.db.Column(app.db.String(1))
    ativo = app.db.Column(app.db.String(1))


# ==========================================================


class FinReciboTipo(generic_model, app.db.Model):
    __tablename__ = "fin_recibo_tipo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    padrao = app.db.Column(app.db.String(1))
    ativo = app.db.Column(app.db.String(1))
    sigla_fin_recibo_tipo = app.db.Column(app.db.String(100))


# ==========================================================


class FinTipoVariacao(generic_model, app.db.Model):
    __tablename__ = "fin_tipo_variacao"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    tipo = app.db.Column(app.db.String(1))
    valor_positivo = app.db.Column(app.db.String(1))
    sigla_fin_tipo_variacao = app.db.Column(app.db.String(100))


# ==========================================================


class FinUnitParam(generic_model, app.db.Model):
    __tablename__ = "fin_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================


class FinClassAgrupGrupo(generic_model, app.db.Model):
    __tablename__ = "fin_class_agrup_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    fin_class_grupo_id = app.db.Column(app.db.ForeignKey("fin_class_grupo.id"))
    fin_class_grupo_id_obj = app.db.relationship("FinClassGrupo")

    fin_class_id = app.db.Column(app.db.ForeignKey("fin_class.id"))
    fin_class_id_obj = app.db.relationship("FinClass")

    fin_class_agrup_id = app.db.Column(app.db.ForeignKey("fin_class_agrup.id"))


# ==========================================================


class FinCondPagrecConfig(generic_model, app.db.Model):
    __tablename__ = "fin_cond_pagrec_config"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    qnt_dia = app.db.Column(app.db.app.db.Integer)

    fin_cond_pag_rec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    fin_cond_pag_rec_id_obj = app.db.relationship("FinCondPagrec")


# ==========================================================


class FinDocTipo(generic_model, app.db.Model):
    __tablename__ = "fin_doc_tipo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_fin_doc_tipo = app.db.Column(app.db.String(50))

    ger_numeracao_id = app.db.Column(
        app.db.ForeignKey(
            "ger_numeracao.id",
        )
    )
    ger_numeracao_id_obj = app.db.relationship("GerNumeracao")


# ==========================================================


class FinConta(generic_model, app.db.Model):
    __tablename__ = "fin_conta"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    nr_agencia = app.db.Column(app.db.String(50))
    nr_conta = app.db.Column(app.db.String(50))

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    fin_banco_id = app.db.Column(app.db.ForeignKey("fin_banco.id"))
    fin_banco_id_obj = app.db.relationship("FinBanco")


# ==========================================================


class FinLote(generic_model, app.db.Model):
    __tablename__ = "fin_lote"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    data_lote = app.db.Column(app.db.Date)
    sigla_fin_lote = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")


# ==========================================================


class FinPagrec(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    numero_doc_pagrec = app.db.Column(app.db.String(50))
    observacao = app.db.Column(app.db.String(250))
    data_mov = app.db.Column(app.db.Date)
    valor_pagrec = app.db.Column(app.db.Numeric(18, 2))
    numero_parc_total = app.db.Column(app.db.Integer)
    data_valid = app.db.Column(app.db.Date)
    tipo_es = app.db.Column(app.db.String(1))

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    fin_cond_pagrec_id_obj = app.db.relationship("FinCondPagrec")

    fin_pagrec_tipo_id = app.db.Column(app.db.ForeignKey("fin_pagrec_tipo.id"))
    fin_pagrec_tipo_id_obj = app.db.relationship("FinPagrecTipo")

    ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="FinPagrec.ger_pessoa_id == GerPessoa.id"
    )

    ger_pessoa_id_pagrec = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_pagrec_obj = app.db.relationship(
        "GerPessoa", primaryjoin="FinPagrec.ger_pessoa_id_pagrec == GerPessoa.id"
    )

    ope_centro_rat_tipo_id = app.db.Column(app.db.ForeignKey("ope_centro_rat_tipo.id"))
    ope_centro_rat_tipo_id_obj = app.db.relationship("OpeCentroRatTipo")

    fin_doc_tipo_id = app.db.Column(app.db.ForeignKey("fin_doc_tipo.id"))
    fin_doc_tipo_id_obj = app.db.relationship("FinDocTipo")

    process_id = app.db.Column(app.db.ForeignKey("sys_process_log.id"))
    process_id_obj = app.db.relationship("SysProcessLog")

    fin_pagrec_parc_childs = app.db.relationship(
        "FinPagrecParc", cascade="all,delete-orphan"
    )


# ==========================================================


class FinPagrecPrev(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_prev"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_per = app.db.Column(app.db.Date)
    data_valid = app.db.Column(app.db.app.db.Date)
    tipo_es = app.db.Column(app.db.String(1))

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    fin_class_id = app.db.Column(app.db.ForeignKey("fin_class.id"))
    fin_class_id_obj = app.db.relationship("FinClass")

    ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_obj = app.db.relationship("GerPessoa")

    fin_pagrec_versao_id = app.db.Column(app.db.ForeignKey("fin_pagrec_versao.id"))
    fin_pagrec_versao_id_obj = app.db.relationship("FinPagrecVersao")

    process_id = app.db.Column(app.db.ForeignKey("sys_process_log.id"))
    process_id_obj = app.db.relationship("SysProcessLog")

    valor01 = app.db.Column(app.db.Numeric(18, 2))
    valor02 = app.db.Column(app.db.Numeric(18, 2))
    valor03 = app.db.Column(app.db.Numeric(18, 2))
    valor04 = app.db.Column(app.db.Numeric(18, 2))
    valor05 = app.db.Column(app.db.Numeric(18, 2))
    valor06 = app.db.Column(app.db.Numeric(18, 2))
    valor07 = app.db.Column(app.db.Numeric(18, 2))
    valor08 = app.db.Column(app.db.Numeric(18, 2))
    valor09 = app.db.Column(app.db.Numeric(18, 2))
    valor10 = app.db.Column(app.db.Numeric(18, 2))
    valor11 = app.db.Column(app.db.Numeric(18, 2))
    valor12 = app.db.Column(app.db.Numeric(18, 2))
    valor13 = app.db.Column(app.db.Numeric(18, 2))
    valor14 = app.db.Column(app.db.Numeric(18, 2))
    valor15 = app.db.Column(app.db.Numeric(18, 2))
    valor16 = app.db.Column(app.db.Numeric(18, 2))
    valor17 = app.db.Column(app.db.Numeric(18, 2))
    valor18 = app.db.Column(app.db.Numeric(18, 2))
    valor19 = app.db.Column(app.db.Numeric(18, 2))
    valor20 = app.db.Column(app.db.Numeric(18, 2))
    valor21 = app.db.Column(app.db.Numeric(18, 2))
    valor22 = app.db.Column(app.db.Numeric(18, 2))
    valor23 = app.db.Column(app.db.Numeric(18, 2))
    valor24 = app.db.Column(app.db.Numeric(18, 2))
    valor25 = app.db.Column(app.db.Numeric(18, 2))
    valor26 = app.db.Column(app.db.Numeric(18, 2))
    valor27 = app.db.Column(app.db.Numeric(18, 2))
    valor28 = app.db.Column(app.db.Numeric(18, 2))
    valor29 = app.db.Column(app.db.Numeric(18, 2))
    valor30 = app.db.Column(app.db.Numeric(18, 2))
    valor31 = app.db.Column(app.db.Numeric(18, 2))

    fin_pagrec_prev_var_childs = app.db.relationship(
        "FinPagrecPrevVar", cascade="all,delete-orphan"
    )

    fin_pagrec_prev_dest_childs = app.db.relationship(
        "FinPagrecPrevDest", cascade="all,delete-orphan"
    )


# ==========================================================


class FinPagrecBanco(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_banco"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_mov = app.db.Column(app.db.Date)
    numero_doc_pagrec = app.db.Column(app.db.String(50))
    valor = app.db.Column(app.db.Numeric(18, 2))
    observacao = app.db.Column(app.db.String(250))
    data_valid = app.db.Column(app.db.Date)

    fin_conta_id = app.db.Column(app.db.ForeignKey("fin_conta.id"))
    fin_conta_id_obj = app.db.relationship("FinConta")

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")


# ==========================================================


class FinPagrecBancoExtrato(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_banco_extrato"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_extrato = app.db.Column(app.db.Date)
    numero_doc = app.db.Column(app.db.String(50))
    descricao = app.db.Column(app.db.String(250))
    valor = app.db.Column(app.db.Numeric(18, 2))
    status = app.db.Column(app.db.String(2))
    status_observacao = app.db.Column(app.db.String(250))

    fin_conta_id = app.db.Column(app.db.ForeignKey("fin_conta.id"))
    fin_conta_id_obj = app.db.relationship("FinConta")

    process_id = app.db.Column(app.db.ForeignKey("sys_process_log.id"))
    process_id_obj = app.db.relationship("SysProcessLog")


# ==========================================================


class FinPagrecBancoTransf(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_banco_transf"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_mov = app.db.Column(app.db.Date)
    valor = app.db.Column(app.db.Numeric(18, 2))
    observacao = app.db.Column(app.db.String(250))

    data_valid = app.db.Column(app.db.Date)

    fin_conta_id_origem = app.db.Column(app.db.ForeignKey("fin_conta.id"))
    fin_conta_id_origem_obj = app.db.relationship(
        "FinConta",
        primaryjoin="FinPagrecBancoTransf.fin_conta_id_origem == FinConta.id",
    )

    fin_conta_id_destino = app.db.Column(app.db.ForeignKey("fin_conta.id"))
    fin_conta_id_destino_obj = app.db.relationship(
        "FinConta",
        primaryjoin="FinPagrecBancoTransf.fin_conta_id_destino == FinConta.id",
    )

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    process_id = app.db.Column(app.db.ForeignKey("sys_process_log.id"))
    process_id_obj = app.db.relationship("SysProcessLog")


# ==========================================================


class FinPagrecParc(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_parc"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    numero_parc = app.db.Column(app.db.Integer)
    valor_pagrec = app.db.Column(app.db.Numeric(18, 2))
    valor_juro = app.db.Column(app.db.Numeric(18, 2))
    valor_desconto = app.db.Column(app.db.Numeric(18, 2))
    valor_multa = app.db.Column(app.db.Numeric(18, 2))
    data_venc = app.db.Column(app.db.Date)
    data_valid = app.db.Column(app.db.Date)

    fin_pagrec_id = app.db.Column(app.db.ForeignKey("fin_pagrec.id"))

    fin_doc_tipo_id = app.db.Column(app.db.ForeignKey("fin_doc_tipo.id"))
    fin_doc_tipo_id_obj = app.db.relationship("FinDocTipo")

    fin_pagrec_parc_var_childs = app.db.relationship(
        "FinPagrecParcVar", cascade="all,delete-orphan"
    )


# ==========================================================


class FinPagrecPrevDest(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_prev_dest"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid = app.db.Column(app.db.Date)

    fin_pagrec_prev_id = app.db.Column(app.db.ForeignKey("fin_pagrec_prev.id"))

    ope_centro1_id_dest_pri = app.db.Column(app.db.ForeignKey("ope_centro1.id"))
    ope_centro1_id_obj = app.db.relationship(
        "OpeCentro1",
        primaryjoin="FinPagrecPrevDest.ope_centro1_id_dest_pri == OpeCentro1.id",
    )

    ope_centro1_id_dest_sec = app.db.Column(app.db.ForeignKey("ope_centro1.id"))
    ope_centro11_id_obj = app.db.relationship(
        "OpeCentro1",
        primaryjoin="FinPagrecPrevDest.ope_centro1_id_dest_sec == OpeCentro1.id",
    )

    ope_centro2_id_dest_sec = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro21_id_obj = app.db.relationship(
        "OpeCentro2",
        primaryjoin="FinPagrecPrevDest.ope_centro2_id_dest_sec == OpeCentro2.id",
    )

    ope_centro2_id_dest_pri = app.db.Column(app.db.ForeignKey("ope_centro2.id"))
    ope_centro2_id_obj = app.db.relationship(
        "OpeCentro2",
        primaryjoin="FinPagrecPrevDest.ope_centro2_id_dest_pri == OpeCentro2.id",
    )

    ope_atividade_id = app.db.Column(app.db.ForeignKey("ope_atividade.id"))
    ope_atividade_id_obj = app.db.relationship("OpeAtividade")

    valor01 = app.db.Column(app.db.Numeric(18, 2))
    valor02 = app.db.Column(app.db.Numeric(18, 2))
    valor03 = app.db.Column(app.db.Numeric(18, 2))
    valor04 = app.db.Column(app.db.Numeric(18, 2))
    valor05 = app.db.Column(app.db.Numeric(18, 2))
    valor06 = app.db.Column(app.db.Numeric(18, 2))
    valor07 = app.db.Column(app.db.Numeric(18, 2))
    valor08 = app.db.Column(app.db.Numeric(18, 2))
    valor09 = app.db.Column(app.db.Numeric(18, 2))
    valor10 = app.db.Column(app.db.Numeric(18, 2))
    valor11 = app.db.Column(app.db.Numeric(18, 2))
    valor12 = app.db.Column(app.db.Numeric(18, 2))
    valor13 = app.db.Column(app.db.Numeric(18, 2))
    valor14 = app.db.Column(app.db.Numeric(18, 2))
    valor15 = app.db.Column(app.db.Numeric(18, 2))
    valor16 = app.db.Column(app.db.Numeric(18, 2))
    valor17 = app.db.Column(app.db.Numeric(18, 2))
    valor18 = app.db.Column(app.db.Numeric(18, 2))
    valor19 = app.db.Column(app.db.Numeric(18, 2))
    valor20 = app.db.Column(app.db.Numeric(18, 2))
    valor21 = app.db.Column(app.db.Numeric(18, 2))
    valor22 = app.db.Column(app.db.Numeric(18, 2))
    valor23 = app.db.Column(app.db.Numeric(18, 2))
    valor24 = app.db.Column(app.db.Numeric(18, 2))
    valor25 = app.db.Column(app.db.Numeric(18, 2))
    valor26 = app.db.Column(app.db.Numeric(18, 2))
    valor27 = app.db.Column(app.db.Numeric(18, 2))
    valor28 = app.db.Column(app.db.Numeric(18, 2))
    valor29 = app.db.Column(app.db.Numeric(18, 2))
    valor30 = app.db.Column(app.db.Numeric(18, 2))
    valor31 = app.db.Column(app.db.Numeric(18, 2))


# ==========================================================


class FinPagrecPrevVar(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_prev_var"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid = app.db.Column(app.db.Date)
    valor01 = app.db.Column(app.db.Numeric(18, 2))
    valor02 = app.db.Column(app.db.Numeric(18, 2))
    valor03 = app.db.Column(app.db.Numeric(18, 2))
    valor04 = app.db.Column(app.db.Numeric(18, 2))
    valor05 = app.db.Column(app.db.Numeric(18, 2))
    valor06 = app.db.Column(app.db.Numeric(18, 2))
    valor07 = app.db.Column(app.db.Numeric(18, 2))
    valor08 = app.db.Column(app.db.Numeric(18, 2))
    valor09 = app.db.Column(app.db.Numeric(18, 2))
    valor10 = app.db.Column(app.db.Numeric(18, 2))
    valor11 = app.db.Column(app.db.Numeric(18, 2))
    valor12 = app.db.Column(app.db.Numeric(18, 2))
    valor13 = app.db.Column(app.db.Numeric(18, 2))
    valor14 = app.db.Column(app.db.Numeric(18, 2))
    valor15 = app.db.Column(app.db.Numeric(18, 2))
    valor16 = app.db.Column(app.db.Numeric(18, 2))
    valor17 = app.db.Column(app.db.Numeric(18, 2))
    valor18 = app.db.Column(app.db.Numeric(18, 2))
    valor19 = app.db.Column(app.db.Numeric(18, 2))
    valor20 = app.db.Column(app.db.Numeric(18, 2))
    valor21 = app.db.Column(app.db.Numeric(18, 2))
    valor22 = app.db.Column(app.db.Numeric(18, 2))
    valor23 = app.db.Column(app.db.Numeric(18, 2))
    valor24 = app.db.Column(app.db.Numeric(18, 2))
    valor25 = app.db.Column(app.db.Numeric(18, 2))
    valor26 = app.db.Column(app.db.Numeric(18, 2))
    valor27 = app.db.Column(app.db.Numeric(18, 2))
    valor28 = app.db.Column(app.db.Numeric(18, 2))
    valor29 = app.db.Column(app.db.Numeric(18, 2))
    valor30 = app.db.Column(app.db.Numeric(18, 2))
    valor31 = app.db.Column(app.db.Numeric(18, 2))

    fin_pagrec_prev_id = app.db.Column(
        app.db.ForeignKey("fin_pagrec_prev.id", ondelete="CASCADE")
    )

    fin_tipo_variacao_id = app.db.Column(app.db.ForeignKey("fin_tipo_variacao.id"))
    fin_tipo_variacao_id_obj = app.db.relationship("FinTipoVariacao")


# ==========================================================


class FinPagrecBaixa(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_baixa"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    tipo = app.db.Column(app.db.String(1))
    numero_doc_pagrec = app.db.Column(app.db.String(50))
    valor_pagrec = app.db.Column(app.db.Numeric(182))
    data_baixa = app.db.Column(app.db.Date)
    data_valid = app.db.Column(app.db.Date)

    fin_conta_id = app.db.Column(app.db.ForeignKey("fin_conta.id"))
    fin_conta_id_obj = app.db.relationship("FinConta")

    fin_doc_tipo_id = app.db.Column(app.db.ForeignKey("fin_doc_tipo.id"))
    fin_doc_tipo_id_obj = app.db.relationship("FinDocTipo")

    fin_lote_id = app.db.Column(app.db.ForeignKey("fin_lote.id"))
    fin_lote_id_obj = app.db.relationship("FinLote")

    fin_pagrec_parc_id = app.db.Column(app.db.ForeignKey("fin_pagrec_parc.id"))
    fin_pagrec_parc_id_obj = app.db.relationship("FinPagrecParc")

    fin_pagrec_baixa_var_childs = app.db.relationship(
        "FinPagrecBaixaVar", cascade="all,delete-orphan"
    )


# ==========================================================


class FinPagrecClass(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_class"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    valor = app.db.Column(app.db.Numeric(18, 2))
    fator_rat = app.db.Column(app.db.Numeric(18, 6))
    perc_rat = app.db.Column(app.db.Numeric(18, 6))
    data_valid = app.db.Column(app.db.Date)

    fin_class_id = app.db.Column(app.db.ForeignKey("fin_class.id"))
    fin_class_id_obj = app.db.relationship("FinClass")

    fin_pagrec_banco_id = app.db.Column(app.db.ForeignKey("fin_pagrec_banco.id"))
    fin_pagrec_banco_id_obj = app.db.relationship("FinPagrecBanco")

    fin_pagrec_id = app.db.Column(app.db.ForeignKey("fin_pagrec.id"))
    fin_pagrec_id_obj = app.db.relationship("FinPagrec")


# ==========================================================


class FinPagrecParcVar(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_parc_var"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    valor = app.db.Column(app.db.Numeric(18, 2))
    data_valid = app.db.Column(app.db.Date)

    fin_pagrec_parc_id = app.db.Column(app.db.ForeignKey("fin_pagrec_parc.id"))
    # fin_pagrec_parc_id_obj = app.db.relationship('FinPagrecParc')

    fin_tipo_variacao_id = app.db.Column(app.db.ForeignKey("fin_tipo_variacao.id"))
    fin_tipo_variacao_id_obj = app.db.relationship("FinTipoVariacao")


# ==========================================================


class FinPagrecBaixaVar(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_baixa_var"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    valor = app.db.Column(app.db.Numeric(18, 2))
    observacao = app.db.Column(app.db.String(250))
    data_valid = app.db.Column(app.db.Date)

    fin_pagrec_baixa_id = app.db.Column(app.db.ForeignKey("fin_pagrec_baixa.id"))

    fin_tipo_variacao_id = app.db.Column(app.db.ForeignKey("fin_tipo_variacao.id"))
    fin_tipo_variacao_id_obj = app.db.relationship("FinTipoVariacao")


# ==========================================================


class FinPagrecOrigem(generic_model, app.db.Model):
    __tablename__ = "fin_pagrec_origem"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    tipo = app.db.Column(app.db.String(50))

    fin_pagrec_id = app.db.Column(app.db.ForeignKey("fin_pagrec.id"))
    fin_pagrec1_id_obj = app.db.relationship(
        "FinPagrec", primaryjoin="FinPagrecOrigem.fin_pagrec_id_origem == FinPagrec.id"
    )

    fin_pagrec_id_origem = app.db.Column(app.db.ForeignKey("fin_pagrec.id"))
    fin_pagrec_id_origem_obj = app.db.relationship(
        "FinPagrec", primaryjoin="FinPagrecOrigem.fin_pagrec_id == FinPagrec.id"
    )

    fin_pagrec_parc_id = app.db.Column(app.db.ForeignKey("fin_pagrec_parc.id"))
    fin_pagrec_parc_id_obj = app.db.relationship(
        "FinPagrecParc",
        primaryjoin="FinPagrecOrigem.fin_pagrec_parc_id == FinPagrecParc.id",
    )

    fin_pagrec_parc_id_origem = app.db.Column(app.db.ForeignKey("fin_pagrec_parc.id"))
    fin_pagrec_parc_id_origem_obj = app.db.relationship(
        "FinPagrecParc",
        primaryjoin="FinPagrecOrigem.fin_pagrec_parc_id_origem == FinPagrecParc.id",
    )

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")

    fin_pagrec_baixa_id = app.db.Column(app.db.ForeignKey("fin_pagrec_baixa.id"))
    fin_pagrec_baixa_id_obj = app.db.relationship("FinPagrecBaixa")

    fin_extrato_id = app.db.Column(app.db.ForeignKey("fin_pagrec_banco_extrato.id"))
    fin_extrato_id_obj = app.db.relationship("FinPagrecBancoExtrato")

    fin_recibo_id = app.db.Column(
        app.db.ForeignKey("fin_recibo.id"),
    )
    fin_recibo_id_obj = app.db.relationship("FinRecibo")

    fin_pagrec_banco_id = app.db.Column(app.db.ForeignKey("fin_pagrec_banco.id"))
    fin_pagrec_banco_id_obj = app.db.relationship("FinPagrecBanco")


# ==========================================================
