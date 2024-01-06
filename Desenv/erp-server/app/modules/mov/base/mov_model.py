import app
from sqlalchemy import Text
from app.generics.generic_model import generic_model


# ==========================================================


class MovTipo(generic_model, app.db.Model):
    __tablename__ = "mov_tipo"

    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_mov_tipo = app.db.Column(app.db.String(50))
    tipo_mov = app.db.Column(app.db.String(10))
    configuracao = app.db.Column(Text)


# ==========================================================


class MovStatus(generic_model, app.db.Model):
    __tablename__ = "mov_status"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_mov_status = app.db.Column(app.db.String(50))
    tipo_status = app.db.Column(app.db.String(1))


# ==========================================================


class MovUnitParam(generic_model, app.db.Model):
    __tablename__ = "mov_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================


class MovOperacao(generic_model, app.db.Model):
    __tablename__ = "mov_operacao"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_mov_operacao = app.db.Column(app.db.String(50))
    finalidade_doc = app.db.Column(app.db.Integer)
    tipo_es = app.db.Column(app.db.String(1))
    configuracao = app.db.Column(Text)

    ger_numeracao_id = app.db.Column(app.db.ForeignKey("ger_numeracao.id"))
    ger_numeracao_id_obj = app.db.relationship("GerNumeracao")

    mov_tipo_id_obj = app.db.relationship("MovTipo")
    mov_tipo_id = app.db.Column(app.db.ForeignKey("mov_tipo.id"))

    mov_operacao_status_childs = app.db.relationship(
        "MovOperacaoStatus",
        primaryjoin="MovOperacaoStatus.mov_operacao_id == MovOperacao.id",
        cascade="all,delete-orphan",
    )


# ==========================================================


class MovOperacaoStatus(generic_model, app.db.Model):
    __tablename__ = "mov_operacao_status"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    mov_operacao_id = app.db.Column(app.db.ForeignKey("mov_operacao.id"))

    mov_operacao_id_prox = app.db.Column(app.db.ForeignKey("mov_operacao.id"))
    mov_operacao_id_prox_obj = app.db.relationship(
        "MovOperacao",
        primaryjoin="MovOperacaoStatus.mov_operacao_id_prox == MovOperacao.id",
    )

    mov_status_id = app.db.Column(app.db.ForeignKey("mov_status.id"))
    mov_status_id_obj = app.db.relationship(
        "MovStatus", primaryjoin="MovOperacaoStatus.mov_status_id == MovStatus.id"
    )

    mov_status_id_prox = app.db.Column(app.db.ForeignKey("mov_status.id"))
    mov_status_id_prox_obj = app.db.relationship(
        "MovStatus", primaryjoin="MovOperacaoStatus.mov_status_id_prox == MovStatus.id"
    )


# ==========================================================


class Mov(generic_model, app.db.Model):
    __tablename__ = "mov"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nr_externo = app.db.Column(app.db.String(50))
    data_mov = app.db.Column(app.db.TIMESTAMP())
    numero_mov = app.db.Column(app.db.Integer)
    data_emissao = app.db.Column(app.db.TIMESTAMP())
    serie_mov = app.db.Column(app.db.String(3))
    valor_total = app.db.Column(app.db.Numeric(18, 6))
    observacao = app.db.Column(app.db.String(250))
    tipo_frete = app.db.Column(app.db.Integer)
    data_entrega = app.db.Column(app.db.Date)
    data_entrada_saida = app.db.Column(app.db.Date)
    tipo_emissao_carga = app.db.Column(app.db.Integer)
    tipo_modal_carga = app.db.Column(app.db.String(2))
    tipo_transportador_carga = app.db.Column(app.db.Integer)
    valor_carga = app.db.Column(app.db.Numeric(18, 6))
    tipo_umedida_carga = app.db.Column(app.db.String(2))
    qnt_carga = app.db.Column(app.db.Numeric(18, 6))
    observacao_transp = app.db.Column(app.db.String(250))
    observacao_serv = app.db.Column(app.db.String(250))
    tipo_fretamento = app.db.Column(app.db.Integer)
    tipo_serv_frete = app.db.Column(app.db.Integer)
    tipo_tomador_serv_frete = app.db.Column(app.db.Integer)
    taf = app.db.Column(app.db.String(50))
    data_anulacao = app.db.Column(app.db.Date)
    observacao_item = app.db.Column(app.db.String(250))
    valor_financeiro_total = app.db.Column(app.db.Numeric(18, 6))
    valor_item_frete_total = app.db.Column(app.db.Numeric(18, 6))
    observacao_fiscal = app.db.Column(app.db.String(250))
    fis_tipo_resp_reten = app.db.Column(app.db.String(1))
    fis_exig_iss_nfs = app.db.Column(app.db.String(1))

    fis_nat_ope_nfs = app.db.Column(app.db.String(1))
    numero_mov_pre = app.db.Column(app.db.Integer)
    serio_mov_pre = app.db.Column(app.db.String(3))
    cep_carreg = app.db.Column(app.db.String(50))
    cep_descarreg = app.db.Column(app.db.String(50))
    tipo_carga = app.db.Column(app.db.String(2))
    data_valid = app.db.Column(app.db.Date)
    fis_iss_retido_nfs = app.db.Column(app.db.String(1))
    fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    fin_cond_pagrec_id_obj = app.db.relationship("FinCondPagrec")

    fis_doc_tipo_id = app.db.Column(app.db.ForeignKey("fis_doc_tipo.id"))
    fis_doc_tipo_id_obj = app.db.relationship("FisDocTipo")

    ger_cidade_id_carreg = app.db.Column(app.db.ForeignKey("ger_cidade.id"))
    ger_cidade_id_carreg_obj = app.db.relationship(
        "GerCidade", primaryjoin="Mov.ger_cidade_id_carreg == GerCidade.id"
    )

    ger_cidade_id_descarreg = app.db.Column(app.db.ForeignKey("ger_cidade.id"))
    ger_cidade_id_descarreg_obj = app.db.relationship(
        "GerCidade", primaryjoin="Mov.ger_cidade_id_descarreg == GerCidade.id"
    )

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    ger_pessoa_endereco_id_dest = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_dest_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="Mov.ger_pessoa_endereco_id_dest == GerPessoaEndereco.id",
    )

    ger_pessoa_endereco_id_entrega = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_entrega_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="Mov.ger_pessoa_endereco_id_entrega == GerPessoaEndereco.id",
    )

    ger_pessoa_endereco_id_expe = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_expe_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="Mov.ger_pessoa_endereco_id_expe == GerPessoaEndereco.id",
    )

    ger_pessoa_endereco_id_fiscal = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_fiscal_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="Mov.ger_pessoa_endereco_id_fiscal == GerPessoaEndereco.id",
    )

    ger_pessoa_endereco_id_inter = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_inter_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="Mov.ger_pessoa_endereco_id_inter == GerPessoaEndereco.id",
    )

    ger_pessoa_endereco_id_rece = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_rece_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="Mov.ger_pessoa_endereco_id_rece == GerPessoaEndereco.id",
    )

    ger_pessoa_endereco_id_reme = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_reme_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="Mov.ger_pessoa_endereco_id_reme == GerPessoaEndereco.id",
    )

    ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_obj = app.db.relationship("GerPessoa")

    mov_operacao_id = app.db.Column(app.db.ForeignKey("mov_operacao.id"))
    mov_operacao_id_obj = app.db.relationship("MovOperacao")

    mov_status_id = app.db.Column(app.db.ForeignKey("mov_status.id"))
    mov_status_id_obj = app.db.relationship("MovStatus")

    sys_user_id_resp = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")


# ==========================================================


class MovEstNivel(generic_model, app.db.Model):
    __tablename__ = "mov_est_nivel"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    qnt_min = app.db.Column(app.db.Numeric(18, 6))
    qnt_max = app.db.Column(app.db.Numeric(18, 6))
    qnt_nesc = app.db.Column(app.db.Numeric(18, 6))
    observacao = app.db.Column(app.db.String(250))

    ger_est_nivel_id = app.db.Column(app.db.ForeignKey("ger_est_nivel.id"))
    ger_est_nivel_id_obj = app.db.relationship("GerEstNivel")

    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_obj = app.db.relationship("GerItemserv")


# ==========================================================


class MovCiot(generic_model, app.db.Model):
    __tablename__ = "mov_ciot"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nr_ciot = app.db.Column(app.db.String(50))

    ger_pessoa_id_responsavel = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_obj = app.db.relationship("GerPessoa")

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")


# ==========================================================


class MovComp(generic_model, app.db.Model):
    __tablename__ = "mov_comp"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome_comp = app.db.Column(app.db.String(50))
    qnt_comp = app.db.Column(app.db.Numeric(18, 6))

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")


# ==========================================================


class MovCondutor(generic_model, app.db.Model):
    __tablename__ = "mov_condutor"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    ger_pessoa_id_condutor = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_obj = app.db.relationship("GerPessoa")

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")


# ==========================================================


class MovCotacao(generic_model, app.db.Model):
    __tablename__ = "mov_cotacao"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao1 = app.db.Column(app.db.String(250))
    observacao2 = app.db.Column(app.db.String(250))
    qnt_cot = app.db.Column(app.db.Numeric(18, 6))
    valor_unit_cot = app.db.Column(app.db.Numeric(18, 6))
    valor_total_cot = app.db.Column(app.db.Numeric(18, 6))
    valor_desc_cot = app.db.Column(app.db.Numeric(18, 6))
    valor_frete_cot = app.db.Column(app.db.Numeric(18, 6))
    valor_outro_cot = app.db.Column(app.db.Numeric(18, 6))
    valor_total_trib_cot = app.db.Column(app.db.Numeric(18, 6))
    status = app.db.Column(app.db.String(1))
    data_status = app.db.Column(app.db.DateTime)

    fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    fin_cond_pagrec_id_obj = app.db.relationship("FinCondPagrec")

    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_obj = app.db.relationship("GerItemserv")

    ger_pessoa_endereco_id = app.db.Column(app.db.ForeignKey("ger_pessoa_endereco.id"))
    ger_pessoa_endereco_id_obj = app.db.relationship("GerPessoaEndereco")

    ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_obj = app.db.relationship("GerPessoa")

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")

    sys_user_id_aprov = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")


# mov_cotacao_anal_childs = app.db.relationship("MovCotacaoAnal", cascade='all,delete-orphan')

# ==========================================================


class MovCotacaoAnal(generic_model, app.db.Model):
    __tablename__ = "mov_cotacao_anal"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    c01_observacao1 = app.db.Column(app.db.String(250))
    c01_observacao2 = app.db.Column(app.db.String(250))
    c01_qnt_cot = app.db.Column(app.db.Numeric(18, 6))
    c01_valor_unit_cot = app.db.Column(app.db.Numeric(18, 6))
    c01_valor_total_cot = app.db.Column(app.db.Numeric(18, 6))
    c01_valor_desc_cot = app.db.Column(app.db.Numeric(18, 6))
    c01_valor_frete_cot = app.db.Column(app.db.Numeric(18, 6))
    c01_valor_outro_cot = app.db.Column(app.db.Numeric(18, 6))
    c01_valor_total_trib_cot = app.db.Column(app.db.Numeric(18, 6))
    c01_status = app.db.Column(
        app.db.String(1),
    )
    c01_data_status = app.db.Column(app.db.TIMESTAMP())
    c02_observacao1 = app.db.Column(app.db.String(250))
    c02_observacao2 = app.db.Column(app.db.String(250))
    c02_qnt_cot = app.db.Column(app.db.Numeric(18, 6))
    c02_valor_unit_cot = app.db.Column(app.db.Numeric(18, 6))
    c02_valor_total_cot = app.db.Column(app.db.Numeric(18, 6))
    c02_valor_desc_cot = app.db.Column(app.db.Numeric(18, 6))
    c02_valor_frete_cot = app.db.Column(app.db.Numeric(18, 6))
    c02_valor_outro_cot = app.db.Column(app.db.Numeric(18, 6))
    c02_valor_total_trib_cot = app.db.Column(app.db.Numeric(18, 6))
    c02_status = app.db.Column(app.db.String(1))
    c02_data_status = app.db.Column(app.db.TIMESTAMP())
    c03_observacao1 = app.db.Column(app.db.String(250))
    c03_observacao2 = app.db.Column(app.db.String(250))
    c03_qnt_cot = app.db.Column(app.db.Numeric(18, 6))
    c03_valor_unit_cot = app.db.Column(app.db.Numeric(18, 6))
    c03_valor_total_cot = app.db.Column(app.db.Numeric(18, 6))
    c03_valor_desc_cot = app.db.Column(app.db.Numeric(18, 6))
    c03_valor_frete_cot = app.db.Column(app.db.Numeric(18, 6))
    c03_valor_outro_cot = app.db.Column(app.db.Numeric(18, 6))
    c03_valor_total_trib_cot = app.db.Column(app.db.Numeric(18, 6))
    c03_status = app.db.Column(
        app.db.String(1),
    )
    c03_data_status = app.db.Column(app.db.TIMESTAMP())
    c04_observacao1 = app.db.Column(app.db.String(250))
    c04_observacao2 = app.db.Column(app.db.String(250))
    c04_qnt_cot = app.db.Column(app.db.Numeric(18, 6))
    c04_valor_unit_cot = app.db.Column(app.db.Numeric(18, 6))
    c04_valor_total_cot = app.db.Column(app.db.Numeric(18, 6))
    c04_valor_desc_cot = app.db.Column(app.db.Numeric(18, 6))
    c04_valor_frete_cot = app.db.Column(app.db.Numeric(18, 6))
    c04_valor_outro_cot = app.db.Column(app.db.Numeric(18, 6))
    c04_valor_total_trib_cot = app.db.Column(app.db.Numeric(18, 6))
    c04_status = app.db.Column(
        app.db.String(1),
    )
    c04_data_status = app.db.Column(app.db.TIMESTAMP())
    c05_observacao1 = app.db.Column(app.db.String(250))
    c05_observacao2 = app.db.Column(app.db.String(250))
    c05_qnt_cot = app.db.Column(app.db.Numeric(18, 6))
    c05_valor_unit_cot = app.db.Column(app.db.Numeric(18, 6))
    c05_valor_total_cot = app.db.Column(app.db.Numeric(18, 6))
    c05_valor_desc_cot = app.db.Column(app.db.Numeric(18, 6))
    c05_valor_frete_cot = app.db.Column(app.db.Numeric(18, 6))
    c05_valor_outro_cot = app.db.Column(app.db.Numeric(18, 6))
    c05_valor_total_trib_cot = app.db.Column(app.db.Numeric(18, 6))
    c05_status = app.db.Column(
        app.db.String(1),
    )
    c05_data_status = app.db.Column(app.db.TIMESTAMP())
    c06_observacao1 = app.db.Column(app.db.String(250))
    c06_observacao2 = app.db.Column(app.db.String(250))
    c06_qnt_cot = app.db.Column(app.db.Numeric(18, 6))
    c06_valor_unit_cot = app.db.Column(app.db.Numeric(18, 6))
    c06_valor_total_cot = app.db.Column(app.db.Numeric(18, 6))
    c06_valor_desc_cot = app.db.Column(app.db.Numeric(18, 6))
    c06_valor_frete_cot = app.db.Column(app.db.Numeric(18, 6))
    c06_valor_outro_cot = app.db.Column(app.db.Numeric(18, 6))
    c06_valor_total_trib_cot = app.db.Column(app.db.Numeric(18, 6))
    c06_status = app.db.Column(
        app.db.String(1),
    )
    c06_data_status = app.db.Column(app.db.TIMESTAMP())
    c07_observacao1 = app.db.Column(app.db.String(250))
    c07_observacao2 = app.db.Column(app.db.String(250))
    c07_qnt_cot = app.db.Column(app.db.Numeric(18, 6))
    c07_valor_unit_cot = app.db.Column(app.db.Numeric(18, 6))
    c07_valor_total_cot = app.db.Column(app.db.Numeric(18, 6))
    c07_valor_desc_cot = app.db.Column(app.db.Numeric(18, 6))
    c07_valor_frete_cot = app.db.Column(app.db.Numeric(18, 6))
    c07_valor_outro_cot = app.db.Column(app.db.Numeric(18, 6))
    c07_valor_total_trib_cot = app.db.Column(app.db.Numeric(18, 6))
    c07_status = app.db.Column(
        app.db.String(1),
    )
    c07_data_status = app.db.Column(app.db.TIMESTAMP())
    c08_observacao1 = app.db.Column(app.db.String(250))
    c08_observacao2 = app.db.Column(app.db.String(250))
    c08_qnt_cot = app.db.Column(app.db.Numeric(18, 6))
    c08_valor_unit_cot = app.db.Column(app.db.Numeric(18, 6))
    c08_valor_total_cot = app.db.Column(app.db.Numeric(18, 6))
    c08_valor_desc_cot = app.db.Column(app.db.Numeric(18, 6))
    c08_valor_frete_cot = app.db.Column(app.db.Numeric(18, 6))
    c08_valor_outro_cot = app.db.Column(app.db.Numeric(18, 6))
    c08_valor_total_trib_cot = app.db.Column(app.db.Numeric(18, 6))
    c08_status = app.db.Column(
        app.db.String(1),
    )
    c08_data_status = app.db.Column(app.db.TIMESTAMP())
    c09_observacao1 = app.db.Column(app.db.String(250))
    c09_observacao2 = app.db.Column(app.db.String(250))
    c09_qnt_cot = app.db.Column(app.db.Numeric(18, 6))
    c09_valor_unit_cot = app.db.Column(app.db.Numeric(18, 6))
    c09_valor_total_cot = app.db.Column(app.db.Numeric(18, 6))
    c09_valor_desc_cot = app.db.Column(app.db.Numeric(18, 6))
    c09_valor_frete_cot = app.db.Column(app.db.Numeric(18, 6))
    c09_valor_outro_cot = app.db.Column(app.db.Numeric(18, 6))
    c09_valor_total_trib_cot = app.db.Column(app.db.Numeric(18, 6))
    c09_status = app.db.Column(app.db.String(1))
    c09_data_status = app.db.Column(app.db.TIMESTAMP())
    c10_observacao1 = app.db.Column(app.db.String(250))
    c10_observacao2 = app.db.Column(app.db.String(250))
    c10_qnt_cot = app.db.Column(app.db.Numeric(18, 6))
    c10_valor_unit_cot = app.db.Column(app.db.Numeric(18, 6))
    c10_valor_total_cot = app.db.Column(app.db.Numeric(18, 6))
    c10_valor_desc_cot = app.db.Column(app.db.Numeric(18, 6))
    c10_valor_frete_cot = app.db.Column(app.db.Numeric(18, 6))
    c10_valor_outro_cot = app.db.Column(app.db.Numeric(18, 6))
    c10_valor_total_trib_cot = app.db.Column(app.db.Numeric(18, 6))
    c10_status = app.db.Column(app.db.String(1))
    c10_data_status = app.db.Column(app.db.TIMESTAMP())

    c01_fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    c01_fin_cond_pagrec_id_obj = app.db.relationship(
        "FinCondPagrec",
        primaryjoin="MovCotacaoAnal.c01_fin_cond_pagrec_id == FinCondPagrec.id",
    )

    c01_ger_pessoa_endereco_id = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    c01_ger_pessoa_endereco_id_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovCotacaoAnal.c01_ger_pessoa_endereco_id == GerPessoaEndereco.id",
    )

    c01_ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    c01_ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovCotacaoAnal.c01_ger_pessoa_id == GerPessoa.id"
    )

    c01_sys_user_id_aprov = app.db.Column(app.db.ForeignKey("sys_user.id"))
    c01_sys_user_id_aprov_obj = app.db.relationship(
        "SysUser", primaryjoin="MovCotacaoAnal.c01_sys_user_id_aprov == SysUser.id"
    )

    c02_fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    c02_fin_cond_pagrec_id_obj = app.db.relationship(
        "FinCondPagrec",
        primaryjoin="MovCotacaoAnal.c02_fin_cond_pagrec_id == FinCondPagrec.id",
    )

    c02_ger_pessoa_endereco_id = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    c02_ger_pessoa_endereco_id_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovCotacaoAnal.c02_ger_pessoa_endereco_id == GerPessoaEndereco.id",
    )

    c02_ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    c02_ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovCotacaoAnal.c02_ger_pessoa_id == GerPessoa.id"
    )

    c02_sys_user_id_aprov = app.db.Column(app.db.ForeignKey("sys_user.id"))
    c02_sys_user_id_aprov_obj = app.db.relationship(
        "SysUser", primaryjoin="MovCotacaoAnal.c02_sys_user_id_aprov == SysUser.id"
    )

    c03_fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    c03_fin_cond_pagrec_id_obj = app.db.relationship(
        "FinCondPagrec",
        primaryjoin="MovCotacaoAnal.c03_fin_cond_pagrec_id == FinCondPagrec.id",
    )

    c03_ger_pessoa_endereco_id = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    c03_ger_pessoa_endereco_id_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovCotacaoAnal.c03_ger_pessoa_endereco_id == GerPessoaEndereco.id",
    )

    c03_ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    c03_ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovCotacaoAnal.c03_ger_pessoa_id == GerPessoa.id"
    )

    c03_sys_user_id_aprov = app.db.Column(app.db.ForeignKey("sys_user.id"))
    c03_sys_user_id_aprov_obj = app.db.relationship(
        "SysUser", primaryjoin="MovCotacaoAnal.c03_sys_user_id_aprov == SysUser.id"
    )

    c04_fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    c04_fin_cond_pagrec_id_obj = app.db.relationship(
        "FinCondPagrec",
        primaryjoin="MovCotacaoAnal.c04_fin_cond_pagrec_id == FinCondPagrec.id",
    )

    c04_ger_pessoa_endereco_id = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    c04_ger_pessoa_endereco_id_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovCotacaoAnal.c04_ger_pessoa_endereco_id == GerPessoaEndereco.id",
    )

    c04_ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    c04_ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovCotacaoAnal.c04_ger_pessoa_id == GerPessoa.id"
    )

    c04_sys_user_id_aprov = app.db.Column(app.db.ForeignKey("sys_user.id"))
    c04_sys_user_id_aprov_obj = app.db.relationship(
        "SysUser", primaryjoin="MovCotacaoAnal.c04_sys_user_id_aprov == SysUser.id"
    )

    c05_fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    c05_fin_cond_pagrec_id_obj = app.db.relationship(
        "FinCondPagrec",
        primaryjoin="MovCotacaoAnal.c05_fin_cond_pagrec_id == FinCondPagrec.id",
    )

    c05_ger_pessoa_endereco_id = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    c05_ger_pessoa_endereco_id_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovCotacaoAnal.c05_ger_pessoa_endereco_id == GerPessoaEndereco.id",
    )

    c05_ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    c05_ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovCotacaoAnal.c05_ger_pessoa_id == GerPessoa.id"
    )

    c05_sys_user_id_aprov = app.db.Column(app.db.ForeignKey("sys_user.id"))
    c05_sys_user_id_aprov_obj = app.db.relationship(
        "SysUser", primaryjoin="MovCotacaoAnal.c05_sys_user_id_aprov == SysUser.id"
    )

    c06_fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    c06_fin_cond_pagrec_id_obj = app.db.relationship(
        "FinCondPagrec",
        primaryjoin="MovCotacaoAnal.c06_fin_cond_pagrec_id == FinCondPagrec.id",
    )

    c06_ger_pessoa_endereco_id = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    c06_ger_pessoa_endereco_id_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovCotacaoAnal.c06_ger_pessoa_endereco_id == GerPessoaEndereco.id",
    )

    c06_ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    c06_ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovCotacaoAnal.c06_ger_pessoa_id == GerPessoa.id"
    )

    c06_sys_user_id_aprov = app.db.Column(app.db.ForeignKey("sys_user.id"))
    c06_sys_user_id_aprov_obj = app.db.relationship(
        "SysUser", primaryjoin="MovCotacaoAnal.c06_sys_user_id_aprov == SysUser.id"
    )

    c07_fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    c07_fin_cond_pagrec_id_obj = app.db.relationship(
        "FinCondPagrec",
        primaryjoin="MovCotacaoAnal.c07_fin_cond_pagrec_id == FinCondPagrec.id",
    )

    c07_ger_pessoa_endereco_id = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    c07_ger_pessoa_endereco_id_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovCotacaoAnal.c07_ger_pessoa_endereco_id == GerPessoaEndereco.id",
    )

    c07_ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    c07_ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovCotacaoAnal.c07_ger_pessoa_id == GerPessoa.id"
    )

    c07_sys_user_id_aprov = app.db.Column(app.db.ForeignKey("sys_user.id"))
    c07_sys_user_id_aprov_obj = app.db.relationship(
        "SysUser", primaryjoin="MovCotacaoAnal.c07_sys_user_id_aprov == SysUser.id"
    )

    c08_fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    c08_fin_cond_pagrec_id_obj = app.db.relationship(
        "FinCondPagrec",
        primaryjoin="MovCotacaoAnal.c08_fin_cond_pagrec_id == FinCondPagrec.id",
    )

    c08_ger_pessoa_endereco_id = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    c08_ger_pessoa_endereco_id_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovCotacaoAnal.c08_ger_pessoa_endereco_id == GerPessoaEndereco.id",
    )

    c08_ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    c08_ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovCotacaoAnal.c08_ger_pessoa_id == GerPessoa.id"
    )

    c08_sys_user_id_aprov = app.db.Column(app.db.ForeignKey("sys_user.id"))
    c08_sys_user_id_aprov_obj = app.db.relationship(
        "SysUser", primaryjoin="MovCotacaoAnal.c08_sys_user_id_aprov == SysUser.id"
    )

    c09_fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    c09_fin_cond_pagrec_id_obj = app.db.relationship(
        "FinCondPagrec",
        primaryjoin="MovCotacaoAnal.c09_fin_cond_pagrec_id == FinCondPagrec.id",
    )

    c09_ger_pessoa_endereco_id = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    c09_ger_pessoa_endereco_id_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovCotacaoAnal.c09_ger_pessoa_endereco_id == GerPessoaEndereco.id",
    )

    c09_ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    c09_ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovCotacaoAnal.c09_ger_pessoa_id == GerPessoa.id"
    )

    c09_sys_user_id_aprov = app.db.Column(app.db.ForeignKey("sys_user.id"))
    c09_sys_user_id_aprov_obj = app.db.relationship(
        "SysUser", primaryjoin="MovCotacaoAnal.c09_sys_user_id_aprov == SysUser.id"
    )

    c10_fin_cond_pagrec_id = app.db.Column(app.db.ForeignKey("fin_cond_pagrec.id"))
    c10_fin_cond_pagrec_id_obj = app.db.relationship(
        "FinCondPagrec",
        primaryjoin="MovCotacaoAnal.c10_fin_cond_pagrec_id == FinCondPagrec.id",
    )

    c10_ger_pessoa_endereco_id = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    c10_ger_pessoa_endereco_id_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovCotacaoAnal.c10_ger_pessoa_endereco_id == GerPessoaEndereco.id",
    )

    c10_ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    c10_ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovCotacaoAnal.c10_ger_pessoa_id == GerPessoa.id"
    )

    c10_sys_user_id_aprov = app.db.Column(app.db.ForeignKey("sys_user.id"))
    c10_sys_user_id_aprov_obj = app.db.relationship(
        "SysUser", primaryjoin="MovCotacaoAnal.c10_sys_user_id_aprov == SysUser.id"
    )

    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_obj = app.db.relationship("GerItemserv")

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")

    mov_cotacao_id = app.db.Column(app.db.ForeignKey("mov_cotacao.id"))


# ==========================================================


class MovEntrega(generic_model, app.db.Model):
    __tablename__ = "mov_entrega"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    ger_cidade_id = app.db.Column(app.db.ForeignKey("ger_cidade.id"))
    ger_cidade_id_obj = app.db.relationship("GerCidade")

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")

    mov_entrega_doc_childs = app.db.relationship(
        "MovEntregaDoc", cascade="all,delete-orphan"
    )


# ==========================================================


class MovItemserv(generic_model, app.db.Model):
    __tablename__ = "mov_itemserv"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    qnt_orig = app.db.Column(app.db.Numeric(18, 6))
    valor_unit_orig = app.db.Column(app.db.Numeric(18, 6))
    qnt_conv = app.db.Column(app.db.Numeric(18, 6))
    valor_unit_conv = app.db.Column(app.db.Numeric(18, 6))
    valor_bruto = app.db.Column(app.db.Numeric(18, 6))
    valor_desconto = app.db.Column(app.db.Numeric(18, 6))
    valor_acrecimo = app.db.Column(app.db.Numeric(18, 6))
    valor_outros = app.db.Column(app.db.Numeric(18, 6))
    valor_liquido = app.db.Column(app.db.Numeric(18, 6))
    qnt_devolvida = app.db.Column(app.db.Numeric(18, 6))
    valor_frete = app.db.Column(app.db.Numeric(18, 6))
    valor_seguro = app.db.Column(app.db.Numeric(18, 6))
    observacao = app.db.Column(app.db.String(250))
    valor_tributo_retido = app.db.Column(app.db.Numeric(18, 6))
    valor_tributo_total = app.db.Column(app.db.Numeric(18, 6))
    qnt_altura = app.db.Column(app.db.Numeric(18, 6))
    qnt_largura = app.db.Column(app.db.Numeric(18, 6))
    qnt_comprimento = app.db.Column(app.db.Numeric(18, 6))
    nome_itemserv = app.db.Column(app.db.String(250))
    fis_obra_art = app.db.Column(app.db.String(50))
    fis_obra_cei = app.db.Column(app.db.String(50))
    fis_numero_proc_susp_nfs = app.db.Column(app.db.String(50))
    fis_doc_cnae_nfs = app.db.Column(app.db.String(50))
    valor_outros_tributo_ret = app.db.Column(app.db.Numeric(18, 6))
    valor_desconto_cond = app.db.Column(app.db.Numeric(18, 6))
    valor_desconto_incond = app.db.Column(app.db.Numeric(18, 6))
    valor_deducao = app.db.Column(app.db.Numeric(18, 6))
    qnt_min_pessoa_cot = app.db.Column(app.db.Integer)
    data_valid = app.db.Column(app.db.Date)

    fis_cfop_id = app.db.Column(app.db.ForeignKey("fis_cfop.id"))
    fis_cfop_id_obj = app.db.relationship("FisCfop")

    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_obj = app.db.relationship("GerItemserv")

    ger_itemserv_lote_id = app.db.Column(app.db.ForeignKey("ger_itemserv_lote.id"))
    ger_itemserv_lote_id_obj = app.db.relationship("GerItemservLote")

    ger_itemserv_var_id = app.db.Column(app.db.ForeignKey("ger_itemserv_var.id"))
    ger_itemserv_var_id_obj = app.db.relationship("GerItemservVar")

    ger_umedida_id_conv = app.db.Column(app.db.ForeignKey("ger_umedida.id"))
    ger_umedida_id_obj = app.db.relationship("GerUmedida")

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")


# ==========================================================


class MovLacre(generic_model, app.db.Model):
    __tablename__ = "mov_lacre"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    lacres = app.db.Column(app.db.String(250))

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")


# ==========================================================


class MovMedida(generic_model, app.db.Model):
    __tablename__ = "mov_medida"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    tipo_medida = app.db.Column(app.db.String(50))
    qnt_medida = app.db.Column(app.db.Numeric(18, 6))
    marca = app.db.Column(app.db.String(50))
    nr_volume = app.db.Column(app.db.Numeric(18, 6))
    peso_liquido = app.db.Column(app.db.Numeric(18, 6))
    peso_bruto = app.db.Column(app.db.Numeric(18, 6))

    ger_umedida_id = app.db.Column(app.db.ForeignKey("ger_umedida.id"))
    ger_umedida_id_obj = app.db.relationship("GerUmedida")

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")


# ==========================================================


class MovPedagio(generic_model, app.db.Model):
    __tablename__ = "mov_pedagio"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    valor_pedagio = app.db.Column(app.db.Numeric(18, 6))
    nr_comprovante = app.db.Column(app.db.String(50))

    ger_pessoa_id_emp_pedagio = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovPedagio.ger_pessoa_id_emp_pedagio == GerPessoa.id"
    )

    ger_pessoa_id_responsavel = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_responsavel_obj = app.db.relationship(
        "GerPessoa", primaryjoin="MovPedagio.ger_pessoa_id_responsavel == GerPessoa.id"
    )

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")


# ==========================================================


class MovPercurso(generic_model, app.db.Model):
    __tablename__ = "mov_percurso"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    ger_cidade_id = app.db.Column(app.db.ForeignKey("ger_cidade.id"))
    ger_cidade_id_obj = app.db.relationship("GerCidade")

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")


# ==========================================================


class MovSeguradora(generic_model, app.db.Model):
    __tablename__ = "mov_seguradora"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nr_apolice = app.db.Column(app.db.String(50))
    nr_averbacao = app.db.Column(app.db.String(50))
    valor = app.db.Column(app.db.Numeric(18, 6))
    tipo_responsavel = app.db.Column(app.db.Integer)

    ger_pessoa_id_responsavel = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_obj = app.db.relationship(
        "GerPessoa",
        primaryjoin="MovSeguradora.ger_pessoa_id_responsavel == GerPessoa.id",
    )

    ger_pessoa_id_seguradora = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa1_id_obj = app.db.relationship(
        "GerPessoa",
        primaryjoin="MovSeguradora.ger_pessoa_id_seguradora == GerPessoa.id",
    )

    mov_id_obj = app.db.relationship("Mov")
    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))


# ==========================================================


class MovTomador(generic_model, app.db.Model):
    __tablename__ = "mov_tomador"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    ger_pessoa_id_responsavel = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_responsavel_obj = app.db.relationship("GerPessoa")

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")


# ==========================================================


class MovEntregaDoc(generic_model, app.db.Model):
    __tablename__ = "mov_entrega_doc"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    valor_total = app.db.Column(app.db.Numeric(18, 6))
    chave_documento = app.db.Column(app.db.String(50))
    modelo_documento = app.db.Column(app.db.String(2))
    serie_documento = app.db.Column(app.db.String(3))
    nr_documento = app.db.Column(app.db.String(50))
    subserie_documento = app.db.Column(app.db.String(2))
    data_emissao = app.db.Column(app.db.Date)

    mov_entrega_id = app.db.Column(app.db.ForeignKey("mov_entrega.id"))

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship(
        "Mov", primaryjoin="MovEntregaDoc.mov_id == Mov.id"
    )

    mov_id_interno = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_interno_obj = app.db.relationship(
        "Mov", primaryjoin="MovEntregaDoc.mov_id_interno == Mov.id"
    )


# ==========================================================


class MovFrete(generic_model, app.db.Model):
    __tablename__ = "mov_frete"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    valor_frete = app.db.Column(app.db.Numeric(18, 6))
    adic_frete_base_cal_icms = app.db.Column(app.db.String(1))
    valor_base_calc = app.db.Column(app.db.Numeric(18, 6))
    perc_aliquota = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto = app.db.Column(app.db.Numeric(18, 6))
    valor_pis = app.db.Column(app.db.Numeric(18, 6))
    valor_cofins = app.db.Column(app.db.Numeric(18, 6))

    ger_pessoa_endereco_id_condutor = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_condutor_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovFrete.ger_pessoa_endereco_id_condutor == GerPessoaEndereco.id",
    )

    ger_pessoa_endereco_id_transp = app.db.Column(
        app.db.ForeignKey("ger_pessoa_endereco.id")
    )
    ger_pessoa_endereco_id_transp_obj = app.db.relationship(
        "GerPessoaEndereco",
        primaryjoin="MovFrete.ger_pessoa_endereco_id_transp == GerPessoaEndereco.id",
    )

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")

    ope_centro2_id_equip = app.db.Column(app.db.ForeignKey("ope_centro2_equip.id"))
    ope_centro2_id_equip_obj = app.db.relationship("OpeCentro2Equip")


# ==========================================================


class MovOrigem(generic_model, app.db.Model):
    __tablename__ = "mov_origem"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    tipo = app.db.Column(app.db.String(50))

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov", primaryjoin="MovOrigem.mov_id == Mov.id")

    mov_id_origem = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_origem_obj = app.db.relationship(
        "Mov", primaryjoin="MovOrigem.mov_id_origem == Mov.id"
    )

    mov_itemserv_id = app.db.Column(app.db.ForeignKey("mov_itemserv.id"))
    mov_itemserv_id_obj = app.db.relationship(
        "MovItemserv", primaryjoin="MovOrigem.mov_itemserv_id == MovItemserv.id"
    )

    mov_itemserv_id_origem = app.db.Column(app.db.ForeignKey("mov_itemserv.id"))
    mov_itemserv_id_origem_obj = app.db.relationship(
        "MovItemserv", primaryjoin="MovOrigem.mov_itemserv_id_origem == MovItemserv.id"
    )


# ==========================================================


class MovReboque(generic_model, app.db.Model):
    __tablename__ = "mov_reboque"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")

    ope_centro2_equip_id_obj = app.db.relationship("OpeCentro2Equip")
    ope_centro2_id_equip = app.db.Column(app.db.ForeignKey("ope_centro2_equip.id"))


# ==========================================================
