import app
from sqlalchemy import Text
from app.generics.generic_model import generic_model


# ==========================================================


class FisCest(generic_model, app.db.Model):
    __tablename__ = "fis_cest"

    nr_cest = app.db.Column(app.db.String(50))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    data_validade = app.db.Column(app.db.Date)

    fis_cest_ncm_childs = app.db.relationship("FisCestNcm", cascade="all,delete-orphan")


# ==========================================================


class FisCfop(generic_model, app.db.Model):
    __tablename__ = "fis_cfop"

    nr_cfop = app.db.Column(app.db.String(50))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    data_validade = app.db.Column(app.db.Date)


# ==========================================================


class FisDocTipo(generic_model, app.db.Model):
    __tablename__ = "fis_doc_tipo"

    modelo = app.db.Column(app.db.String(50))
    sigla_fis_doc_tipo = app.db.Column(app.db.String(100))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))


# ==========================================================


class FisNbs(generic_model, app.db.Model):
    __tablename__ = "fis_nbs"

    nr_nbs = app.db.Column(app.db.String(50))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    data_validade = app.db.Column(app.db.Date)


# ==========================================================


class FisNcm(generic_model, app.db.Model):
    __tablename__ = "fis_ncm"

    nr_ncm = app.db.Column(app.db.String(50))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    data_validade = app.db.Column(app.db.Date)


# ==========================================================


class FisTributo(generic_model, app.db.Model):
    __tablename__ = "fis_tributo"

    nr_tributo = app.db.Column(app.db.String(50))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))


# ==========================================================


class FisCertificado(generic_model, app.db.Model):
    __tablename__ = "fis_certificado"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    senha = app.db.Column(app.db.String(50))
    sys_document_childs = app.db.relationship(
        "SysDocument", cascade="all,delete-orphan"
    )


# ==========================================================


class FisCestNcm(generic_model, app.db.Model):
    __tablename__ = "fis_cest_ncm"

    fis_cest_id = app.db.Column(app.db.ForeignKey("fis_cest.id"))

    fis_ncm_id = app.db.Column(app.db.ForeignKey("fis_ncm.id"))
    fis_ncm_id_obj = app.db.relationship("FisNcm")


# ==========================================================


class FisObs(generic_model, app.db.Model):
    __tablename__ = "fis_obs"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    observacao = app.db.Column(Text)


# ==========================================================


class FisUnitParam(generic_model, app.db.Model):
    __tablename__ = "fis_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================


class FisIbpt(generic_model, app.db.Model):
    __tablename__ = "fis_ibpt"

    data_validade_ini = app.db.Column(app.db.Date)
    data_validade_fin = app.db.Column(app.db.Date)

    perc_nacional = app.db.Column(app.db.Numeric(18, 6))
    perc_importado = app.db.Column(app.db.Numeric(18, 6))
    perc_municipal = app.db.Column(app.db.Numeric(18, 6))

    fis_nbs_id = app.db.Column(app.db.ForeignKey("fis_nbs.id"))
    fis_nbs_id_obj = app.db.relationship("FisNbs")

    fis_ncm_id = app.db.Column(app.db.ForeignKey("fis_ncm.id"))
    fis_ncm_id_obj = app.db.relationship("FisNcm")

    ger_uf_id = app.db.Column(app.db.ForeignKey("ger_uf.id"))
    ger_uf_id_obj = app.db.relationship("GerUf")


# ==========================================================


class FisDoc(generic_model, app.db.Model):
    __tablename__ = "fis_doc"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_emissao = app.db.Column(app.db.TIMESTAMP())
    chave = app.db.Column(app.db.String(50))
    numero = app.db.Column(app.db.Integer)
    serie = app.db.Column(app.db.String(3))
    numero_ini = app.db.Column(app.db.Integer)
    numero_fin = app.db.Column(app.db.Integer)
    data_autorizado = app.db.Column(app.db.TIMESTAMP())
    data_cancelado = app.db.Column(app.db.TIMESTAMP())
    data_encerrado = app.db.Column(app.db.TIMESTAMP())
    xml_assinado = app.db.Column(Text)
    ambiente = app.db.Column(app.db.Integer)
    tipo_emissao = app.db.Column(app.db.Integer)
    status_sefaz = app.db.Column(app.db.Integer)
    xml_protocolado = app.db.Column(Text)
    pdf_emitido = app.db.Column(Text)
    numero_pre = app.db.Column(app.db.Integer)
    serie_pre = app.db.Column(app.db.String(3))

    fis_doc_tipo_id = app.db.Column(app.db.ForeignKey("fis_doc_tipo.id"))
    fis_doc_tipo_id_obj = app.db.relationship("FisDocTipo")

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    mov_id = app.db.Column(app.db.ForeignKey("mov.id"))
    mov_id_obj = app.db.relationship("Mov")

    fis_doc_evento_childs = app.db.relationship(
        "FisDocEvento", cascade="all,delete-orphan"
    )


# ==========================================================


class FisDocEvento(generic_model, app.db.Model):
    __tablename__ = "fis_doc_evento"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    xml_retorno = app.db.Column(Text)
    tipo_evento = app.db.Column(app.db.Integer)
    nr_protocolo = app.db.Column(app.db.String(50))
    qnt_evento = app.db.Column(app.db.Integer)
    descricao_evento = app.db.Column(Text)
    pdf_retorno = app.db.Column(Text)

    fis_doc_id = app.db.Column(app.db.ForeignKey("fis_doc.id"))


# ==========================================================


class FisTributacao(generic_model, app.db.Model):
    __tablename__ = "fis_tributacao"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    cst = app.db.Column(app.db.String(4))
    modalidade_base_calc = app.db.Column(app.db.Integer)
    valor_base_calc = app.db.Column(app.db.Numeric(18, 6))
    perc_aliquota = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto = app.db.Column(app.db.Numeric(18, 6))
    valor_base_calc_isento = app.db.Column(app.db.Numeric(18, 6))
    perc_aliquota_isento = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto_isento = app.db.Column(app.db.Numeric(18, 6))
    valor_base_calc_st = app.db.Column(app.db.Numeric(18, 6))
    margem_agregada_st = app.db.Column(app.db.Numeric(18, 6))
    perc_aliquota_st = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto_st = app.db.Column(app.db.Numeric(18, 6))
    perc_reducao_base_calc = app.db.Column(app.db.Numeric(18, 6))
    observacao = app.db.Column(app.db.String(250))
    valor_imposto_operacao = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto_diferido = app.db.Column(app.db.Numeric(18, 6))
    perc_credito_sn = app.db.Column(app.db.Numeric(18, 6))
    valor_credito_sn = app.db.Column(app.db.Numeric(18, 6))
    valor_base_calc_fcp = app.db.Column(app.db.Numeric(18, 6))
    perc_aliquota_fcp = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto_fcp = app.db.Column(app.db.Numeric(18, 6))
    valor_base_calc_fcp_st = app.db.Column(app.db.Numeric(18, 6))
    perc_aliquota_fcp_st = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto_fcp_st = app.db.Column(app.db.Numeric(18, 6))
    perc_uf_fim_fcp = app.db.Column(app.db.Numeric(18, 6))
    valor_total_uf_fim_fcp = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto_fcp_st_ret = app.db.Column(app.db.Numeric(18, 6))
    valor_base_calc_fcp_st_ret = app.db.Column(app.db.Numeric(18, 6))
    perc_aliquota_fcp_st_ret = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto_desonerado = app.db.Column(app.db.Numeric(18, 6))
    motivo_imposto_desonerado = app.db.Column(app.db.Integer)
    modalidade_base_calc_st = app.db.Column(app.db.Integer)
    valor_base_calc_st_ret = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto_st_ret = app.db.Column(
        app.db.Numeric(18, 6),
    )
    perc_aliquota_red_base_calc_efetiva = app.db.Column(app.db.Numeric(18, 6))
    valor_base_calc_efetiva = app.db.Column(app.db.Numeric(18, 6))
    perc_aliquota_efetiva = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto_efetiva = app.db.Column(app.db.Numeric(18, 6))
    perc_aliquota_credito = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto_credito = app.db.Column(app.db.Numeric(18, 6))
    valor_base_calc_uf_fim = app.db.Column(app.db.Numeric(18, 6))
    perc_interna_uf_fim = app.db.Column(app.db.Numeric(18, 6))
    perc_interestadual_uf_fim = app.db.Column(app.db.Numeric(18, 6))
    perc_partilha_uf_fim = app.db.Column(app.db.Numeric(18, 6))
    valor_partilha_uf_fim = app.db.Column(app.db.Numeric(18, 6))
    valor_partilha_uf_inicio = app.db.Column(app.db.Numeric(18, 6))
    valor_imposto_substituto = app.db.Column(app.db.Numeric(18, 6))
    data_valid = app.db.Column(app.db.Date)

    fin_pagrec_id = app.db.Column(app.db.ForeignKey("fin_pagrec.id"))
    fin_pagrec_id_obj = app.db.relationship("FinPagrec")

    fis_tributo_id = app.db.Column(app.db.ForeignKey("fis_tributo.id"))
    fis_tributo_id_obj = app.db.relationship("FisTributo")

    ger_pessoa_endereco_id = app.db.Column(app.db.ForeignKey("ger_pessoa_endereco.id"))
    ger_pessoa_endereco_id_obj = app.db.relationship("GerPessoaEndereco")

    mov_id = app.db.Column(
        app.db.ForeignKey("mov.id"),
    )
    mov_id_obj = app.db.relationship("Mov")

    mov_itemserv_id = app.db.Column(
        app.db.ForeignKey("mov_itemserv.id"),
    )
    mov_itemserv_id_obj = app.db.relationship("MovItemserv")


# ==========================================================
