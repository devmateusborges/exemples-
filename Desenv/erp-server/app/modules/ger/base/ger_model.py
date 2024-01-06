import app
from sqlalchemy import Text
from app.generics.generic_model import generic_model


# ==========================================================


class GerMarca(generic_model, app.db.Model):
    __tablename__ = "ger_marca"

    unit_id = app.db.Column(app.db.String(36))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ger_marca = app.db.Column(app.db.String(100))

    ger_marca_modelo_childs = app.db.relationship(
        "GerMarcaModelo", cascade="all,delete-orphan"
    )

    ger_marca_pessoa_childs = app.db.relationship(
        "GerMarcaPessoa", cascade="all,delete-orphan"
    )


# ==========================================================


class GerItemservComposTipo(generic_model, app.db.Model):
    __tablename__ = "ger_itemserv_compos_tipo"

    unit_id = app.db.Column(app.db.String(36))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ger_itemserv_compos_tipo = app.db.Column(app.db.String(100))


# ==========================================================


class GerPais(generic_model, app.db.Model):
    __tablename__ = "ger_pais"

    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    nr_pais = app.db.Column(app.db.String(50))
    sigla_pais = app.db.Column(app.db.String(50))

    ger_uf_childs = app.db.relationship("GerUf", cascade="all,delete-orphan")


# ==========================================================


class GerUmedida(generic_model, app.db.Model):
    __tablename__ = "ger_umedida"

    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_umedida = app.db.Column(app.db.String(50))
    ger_umedida_conv_childs = app.db.relationship(
        "GerUmedidaConv",
        primaryjoin="GerUmedidaConv.ger_umedida_id_de == GerUmedida.id",
        cascade="all,delete-orphan",
    )


# ==========================================================


class GerUf(generic_model, app.db.Model):
    __tablename__ = "ger_uf"

    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    nr_uf = app.db.Column(app.db.String(50))
    sigla_uf = app.db.Column(app.db.String(50))
    ger_pais_id = app.db.Column(app.db.ForeignKey("ger_pais.id"))


# ==========================================================


class GerCidade(generic_model, app.db.Model):
    __tablename__ = "ger_cidade"

    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    nr_cidade = app.db.Column(app.db.String(50))
    ger_uf_id = app.db.Column(app.db.ForeignKey("ger_uf.id"))
    ger_uf_id_obj = app.db.relationship("GerUf")


# ==========================================================


class GerDeviceParam(generic_model, app.db.Model):
    __tablename__ = "ger_device_param"

    unit_id = app.db.Column(app.db.String(36))
    sigla_param = app.db.Column(app.db.String(50))
    valor_tx = app.db.Column(app.db.String(250))
    valor_dt = app.db.Column(app.db.Date)
    valor_nm = app.db.Column(app.db.Numeric(18, 6))
    observacao = app.db.Column(app.db.String(250))
    ger_device_id = app.db.Column(app.db.ForeignKey("ger_device.id"))


# ==========================================================


class GerIndexMov(generic_model, app.db.Model):
    __tablename__ = "ger_index_mov"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_mov = app.db.Column(app.db.Date)
    valor1 = app.db.Column(app.db.Numeric(18, 6))
    valor2 = app.db.Column(app.db.Numeric(18, 6))

    ger_index_id = app.db.Column(app.db.ForeignKey("ger_index.id"))
    ger_index_id_obj = app.db.relationship("GerIndex")


# ==========================================================


class GerItemservSubGrupo(generic_model, app.db.Model):
    __tablename__ = "ger_itemserv_subgrupo"

    unit_id = app.db.Column(app.db.String(36))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    ctb_comp_id = app.db.Column(app.db.String(36))
    sigla_ger_itemserv_subgrupo = app.db.Column(app.db.String(100))
    ger_itemserv_grupo_id = app.db.Column(app.db.ForeignKey("ger_itemserv_grupo.id"))


# ==========================================================


class GerItemservVar(generic_model, app.db.Model):
    __tablename__ = "ger_itemserv_var"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_itemserv_var = app.db.Column(app.db.String(50))

    ope_ciclo_var_id = app.db.Column(app.db.ForeignKey("ope_ciclo_var.id"))
    ope_ciclo_var_id_obj = app.db.relationship("OpeCicloVar")


# ==========================================================


class GerMarcaPessoa(generic_model, app.db.Model):
    __tablename__ = "ger_marca_pessoa"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    observacao = app.db.Column(app.db.String(250))
    ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_obj = app.db.relationship("GerPessoa")
    ger_marca_id = app.db.Column(app.db.ForeignKey("ger_marca.id"))


# ==========================================================


class GerPessoaContaBanco(generic_model, app.db.Model):
    __tablename__ = "ger_pessoa_conta_banco"

    unit_id = app.db.Column(app.db.String(36))
    agencia = app.db.Column(app.db.String(100))
    conta = app.db.Column(app.db.String(100))
    observacao = app.db.Column(app.db.String(250))
    ativo = app.db.Column(app.db.String(1))
    ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    fin_banco_id = app.db.Column(app.db.ForeignKey("fin_banco.id"))
    fin_banco_id_obj = app.db.relationship("FinBanco")


# ==========================================================


class GerEmpresa(generic_model, app.db.Model):
    __tablename__ = "ger_empresa"

    nome = app.db.Column(app.db.String(100))
    razao_social = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_empresa = app.db.Column(app.db.String(50))
    doc_cnpj = app.db.Column(app.db.String(50))
    doc_cpf = app.db.Column(app.db.String(50))
    doc_ie = app.db.Column(app.db.String(50))
    doc_im = app.db.Column(app.db.String(50))
    doc_cnae = app.db.Column(app.db.String(50))
    data_abertura = app.db.Column(app.db.Date)
    doc_junta = app.db.Column(app.db.String(50))
    fis_regime = app.db.Column(app.db.String(50))
    data_validade_a3 = app.db.Column(app.db.Date)
    data_validade_a1 = app.db.Column(app.db.Date)
    end_logradouro = app.db.Column(app.db.String(100))
    end_logradouro_nr = app.db.Column(app.db.String(10))
    end_bairro = app.db.Column(app.db.String(100))
    end_complemento = app.db.Column(app.db.String(100))
    end_cep = app.db.Column(app.db.String(100))
    fone_1 = app.db.Column(app.db.String(100))
    fone_2 = app.db.Column(app.db.String(100))
    fone_3 = app.db.Column(app.db.String(100))
    contato_1 = app.db.Column(app.db.String(100))
    contato_2 = app.db.Column(app.db.String(100))
    contato_3 = app.db.Column(app.db.String(100))
    email_1 = app.db.Column(app.db.String(255))
    doc_rntrc = app.db.Column(app.db.String(100))
    fis_dfe_ambiente = app.db.Column(app.db.String(1))
    fis_dfe_api_token = app.db.Column(Text)
    fis_regime_trib_nfs = app.db.Column(app.db.String(1))
    fis_provedor_nfs = app.db.Column(app.db.String(1))
    fis_incent_cultura = app.db.Column(app.db.String(1))
    fis_incent_fiscal_nfs = app.db.Column(app.db.String(1))

    end_ger_cidade_id = app.db.Column(app.db.ForeignKey("ger_cidade.id"))
    end_ger_cidade_id_obj = app.db.relationship("GerCidade")

    fis_certificado_id = app.db.Column(
        app.db.ForeignKey("fis_certificado.id"),
    )
    fis_certificado_id_obj = app.db.relationship(
        "modules.fis.base.fis_model.FisCertificado"
    )

    ger_empresa_grupo_id = app.db.Column(app.db.ForeignKey("ger_empresa_grupo.id"))
    ger_empresa_grupo_id_obj = app.db.relationship("GerEmpresaGrupo")

    ger_per_tipo_id = app.db.Column(app.db.ForeignKey("ger_per_tipo.id"))
    ger_per_tipo_id_obj = app.db.relationship("GerPerTipo")

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    ger_empresa_pessoa_childs = app.db.relationship(
        "GerEmpresaPessoa", cascade="all,delete-orphan"
    )


# ==========================================================


class GerItemserv(generic_model, app.db.Model):
    __tablename__ = "ger_itemserv"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    referencia1 = app.db.Column(app.db.String(50))
    referencia2 = app.db.Column(app.db.String(50))
    referencia3 = app.db.Column(app.db.String(50))
    tipo = app.db.Column(app.db.String(1))
    tipo_ctb_comp = app.db.Column(app.db.String(1))
    origem_fiscal = app.db.Column(app.db.Integer)
    fis_doc_cnae_nfs = app.db.Column(app.db.String(50))
    fis_sigla_servico_municipio = app.db.Column(app.db.String(50))
    sigla_itemserv = app.db.Column(app.db.String(15))
    nome_alternativo = app.db.Column(app.db.String(100))
    tipo_composicao = app.db.Column(app.db.String(1))
    fis_sigla_servico = app.db.Column(app.db.String(50))

    ger_itemserv_subgrupo_id = app.db.Column(
        app.db.ForeignKey("ger_itemserv_subgrupo.id")
    )
    ger_itemserv_subgrupo_id_obj = app.db.relationship("GerItemservSubGrupo")

    fis_ncm_id = app.db.Column(app.db.ForeignKey("fis_ncm.id"))
    fis_ncm_id_obj = app.db.relationship("FisNcm")

    ger_umedida_id = app.db.Column(app.db.ForeignKey("ger_umedida.id"))
    ger_umedida_id_obj = app.db.relationship("GerUmedida")

    fis_cest_id = app.db.Column(app.db.ForeignKey("fis_cest.id"))
    fis_cest_id_obj = app.db.relationship("FisCest")

    fis_nbs_id = app.db.Column(app.db.ForeignKey("fis_nbs.id"))
    fis_nbs_id_obj = app.db.relationship("FisNbs")

    ctb_comp_id = app.db.Column(app.db.ForeignKey("ctb_comp.id"))
    ctb_comp_id_obj = app.db.relationship("CtbComp")

    ger_itemserv_barra_childs = app.db.relationship(
        "GerItemservBarra", cascade="all,delete-orphan"
    )

    ger_itemserv_local_childs = app.db.relationship(
        "GerItemservLocal", cascade="all,delete-orphan"
    )

    ger_itemserv_lote_childs = app.db.relationship(
        "GerItemservLote", cascade="all,delete-orphan"
    )

    ger_itemserv_pessoa_childs = app.db.relationship(
        "GerItemservPessoa", cascade="all,delete-orphan"
    )


# ==========================================================


class GerPessoaEndereco(generic_model, app.db.Model):
    __tablename__ = "ger_pessoa_endereco"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ativo = app.db.Column(app.db.String(1))
    tipo = app.db.Column(app.db.String(1))
    padrao = app.db.Column(app.db.String(1))
    end_logradouro = app.db.Column(app.db.String(100))
    end_logradouro_nr = app.db.Column(app.db.String(10))
    end_bairro = app.db.Column(app.db.String(100))
    end_complemento = app.db.Column(app.db.String(100))
    end_cep = app.db.Column(app.db.String(100))
    fone = app.db.Column(app.db.String(100))
    email = app.db.Column(app.db.String(100))
    contato = app.db.Column(app.db.String(100))
    ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))

    end_ger_cidade_id = app.db.Column(app.db.ForeignKey("ger_cidade.id"))
    end_ger_cidade_id_obj = app.db.relationship("GerCidade")


# ==========================================================


class GerDevice(generic_model, app.db.Model):
    __tablename__ = "ger_device"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_device = app.db.Column(app.db.String(50))

    ger_device_param_childs = app.db.relationship(
        "GerDeviceParam", cascade="all,delete-orphan"
    )


# ==========================================================


class GerEmpresaGrupo(generic_model, app.db.Model):
    __tablename__ = "ger_empresa_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ger_empresa_grupo = app.db.Column(app.db.String(100))


# ==========================================================


class GerEstNivel(generic_model, app.db.Model):
    __tablename__ = "ger_est_nivel"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    observacao = app.db.Column(app.db.String(250))
    bloq_mov_solic = app.db.Column(app.db.String(1))
    bloq_mov_pedido = app.db.Column(app.db.String(1))
    sigla_ger_est_nivel = app.db.Column(app.db.String(100))


# ==========================================================


class GerIndex(generic_model, app.db.Model):
    __tablename__ = "ger_index"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_index = app.db.Column(app.db.String(50))


# ==========================================================


class GerItemservGrupo(generic_model, app.db.Model):
    __tablename__ = "ger_itemserv_grupo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ger_itemserv_grupo = app.db.Column(app.db.String(100))
    ger_itemserv_subgrupo_childs = app.db.relationship(
        "GerItemservSubGrupo", cascade="all,delete-orphan"
    )


# ==========================================================


class GerItemservLote(generic_model, app.db.Model):
    __tablename__ = "ger_itemserv_lote"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ativo = app.db.Column(app.db.String(1))
    data_ini = app.db.Column(app.db.Date)
    data_fin = app.db.Column(app.db.Date)
    observacao = app.db.Column(app.db.String(250))
    data_validade = app.db.Column(app.db.Date)
    sigla_ger_itemserv_lote = app.db.Column(app.db.String(100))
    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))


# ==========================================================


class GerMarcaModelo(generic_model, app.db.Model):
    __tablename__ = "ger_marca_modelo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    sigla_ger_marca_modelo = app.db.Column(app.db.String(100))

    ger_marca_id = app.db.Column(app.db.ForeignKey("ger_marca.id"))


# ==========================================================


class GerNumeracao(generic_model, app.db.Model):
    __tablename__ = "ger_numeracao"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    serie = app.db.Column(app.db.String(3))
    ultimo_nr = app.db.Column(app.db.Integer)
    sigla_ger_numeracao = app.db.Column(app.db.String(100))


# ==========================================================


class GerPer(generic_model, app.db.Model):
    __tablename__ = "ger_per"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_dia_inicial = app.db.Column(app.db.Date)
    dia_nome = app.db.Column(app.db.String(50))
    data_semana_inicial = app.db.Column(app.db.Date)
    semana_nome = app.db.Column(app.db.String(50))
    data_quinzena_inicial = app.db.Column(app.db.Date)
    quinzena_nome = app.db.Column(app.db.String(50))
    data_mes_inicial = app.db.Column(app.db.Date)
    mes_nome = app.db.Column(app.db.String(50))
    data_bimestre_inicial = app.db.Column(app.db.Date)
    bimestre_nome = app.db.Column(app.db.String(50))
    data_trimestre_inicial = app.db.Column(app.db.Date)
    trimestre_nome = app.db.Column(app.db.String(50))
    data_quadrimestre_inicial = app.db.Column(app.db.Date)
    quadrimestre_nome = app.db.Column(app.db.String(50))
    data_semestre_inicial = app.db.Column(app.db.Date)
    semestre_nome = app.db.Column(app.db.String(50))
    data_ano_inicial = app.db.Column(app.db.Date)
    ano_nome = app.db.Column(app.db.String(50))
    ger_per_tipo_id = app.db.Column(app.db.ForeignKey("ger_per_tipo.id"))
    ger_per_tipo_id_obj = app.db.relationship("GerPerTipo")
    sys_process_log_id = app.db.Column(app.db.ForeignKey("sys_process_log.id"))
    sys_process_log_id_obj = app.db.relationship("SysProcessLog")

    data_dia_final = app.db.Column(app.db.Date)
    data_quinzena_final = app.db.Column(app.db.Date)
    data_semana_final = app.db.Column(app.db.Date)
    data_mes_final = app.db.Column(app.db.Date)
    data_bimestre_final = app.db.Column(app.db.Date)
    data_trimestre_final = app.db.Column(app.db.Date)
    data_quadrimestre_final = app.db.Column(app.db.Date)
    data_semestre_final = app.db.Column(app.db.Date)
    data_ano_final = app.db.Column(app.db.Date)

    dia_numero = app.db.Column(app.db.String)
    quinzena_numero = app.db.Column(app.db.String)
    semana_numero = app.db.Column(app.db.String)
    mes_numero = app.db.Column(app.db.String)
    bimestre_numero = app.db.Column(app.db.String)
    trimestre_numero = app.db.Column(app.db.String)
    quadrimestre_numero = app.db.Column(app.db.String)
    semestre_numero = app.db.Column(app.db.String)
    ano_numero = app.db.Column(app.db.String)

    dia_tipo = app.db.Column(app.db.String(1))
    quinzena_tipo = app.db.Column(app.db.String(1))
    semana_tipo = app.db.Column(app.db.String(1))
    mes_tipo = app.db.Column(app.db.String(1))
    bimestre_tipo = app.db.Column(app.db.String(1))
    trimestre_tipo = app.db.Column(app.db.String(1))
    quadrimestre_tipo = app.db.Column(app.db.String(1))
    semestre_tipo = app.db.Column(app.db.String(1))
    ano_tipo = app.db.Column(app.db.String(1))


# ==========================================================


class GerPessoa(generic_model, app.db.Model):
    __tablename__ = "ger_pessoa"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(100))
    razao_social = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))
    doc_cnpj = app.db.Column(app.db.String(50))
    doc_cpf = app.db.Column(app.db.String(50))
    doc_ie = app.db.Column(app.db.String(50))
    doc_im = app.db.Column(app.db.String(50))
    doc_cnae = app.db.Column(app.db.String(50))
    data_abertura = app.db.Column(app.db.String(50))
    doc_junta = app.db.Column(app.db.String(50))
    fis_regime = app.db.Column(app.db.String(50))
    fone_1 = app.db.Column(app.db.String(100))
    fone_2 = app.db.Column(app.db.String(100))
    fone_3 = app.db.Column(app.db.String(100))
    contato_1 = app.db.Column(app.db.String(100))
    contato_2 = app.db.Column(app.db.String(100))
    contato_3 = app.db.Column(app.db.String(100))
    contrib_icms = app.db.Column(app.db.Integer)
    nr_rntrc = app.db.Column(app.db.String(8))
    doc_rg = app.db.Column(app.db.String(50))
    doc_rg_org_exp = app.db.Column(app.db.String(50))
    doc_crc = app.db.Column(app.db.String(50))
    doc_crc_seq = app.db.Column(app.db.String(50))
    doc_crc_org_exp = app.db.Column(app.db.String(50))
    sigla_pes = app.db.Column(app.db.String(50))
    nr_registro_est_cte = app.db.Column(app.db.String(50))
    doc_taf = app.db.Column(app.db.String(50))
    data_valid = app.db.Column(app.db.Date)

    ger_pessoa_conta_banco_childs = app.db.relationship(
        "GerPessoaContaBanco", cascade="all,delete-orphan"
    )

    ger_pessoa_endereco_childs = app.db.relationship(
        "GerPessoaEndereco", cascade="all,delete-orphan"
    )


# ==========================================================


class GerUmedidaConv(generic_model, app.db.Model):
    __tablename__ = "ger_umedida_conv"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    ger_umedida_id_de = app.db.Column(app.db.ForeignKey("ger_umedida.id"))

    ger_umedida_id_para = app.db.Column(app.db.ForeignKey("ger_umedida.id"))
    ger_umedida_id_para_obj = app.db.relationship(
        "GerUmedida", primaryjoin="GerUmedidaConv.ger_umedida_id_para == GerUmedida.id"
    )
    fator_mult = app.db.Column(app.db.Numeric(18, 6))
    ativo = app.db.Column(app.db.String(1))


# ==========================================================


class GerUnitParam(generic_model, app.db.Model):
    __tablename__ = "ger_unit_param"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    data_valid_ini = app.db.Column(app.db.Date)


# ==========================================================


class GerEmpresaPessoa(generic_model, app.db.Model):
    __tablename__ = "ger_empresa_pessoa"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    tipo = app.db.Column(app.db.String(50))
    observacao = app.db.Column(app.db.String(250))
    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))

    ger_pessoa_id = app.db.Column(
        app.db.ForeignKey("ger_pessoa.id"),
    )
    ger_pessoa_id_obj = app.db.relationship("GerPessoa")


# ==========================================================


class GerItemservBarra(generic_model, app.db.Model):
    __tablename__ = "ger_itemserv_barra"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    codigo_barra = app.db.Column(app.db.String(100))
    ativo = app.db.Column(app.db.String(1))

    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))


# ==========================================================


class GerItemservCompos(generic_model, app.db.Model):
    __tablename__ = "ger_itemserv_compos"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))

    ger_itemserv_compos_tipo_id = app.db.Column(
        app.db.ForeignKey("ger_itemserv_compos_tipo.id")
    )
    ger_itemserv_compos_tipo_id_obj = app.db.relationship("GerItemservComposTipo")

    ger_itemserv_id_de = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_de_obj = app.db.relationship(
        "GerItemserv",
        primaryjoin="GerItemservCompos.ger_itemserv_id_de == GerItemserv.id",
    )

    ger_itemserv_id_para = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_itemserv_id_para_obj = app.db.relationship(
        "GerItemserv",
        primaryjoin="GerItemservCompos.ger_itemserv_id_para == GerItemserv.id",
    )

    fator_mult = app.db.Column(app.db.Numeric(18, 6))
    qnt_compos = app.db.Column(app.db.Numeric(18, 6))
    ativo = app.db.Column(app.db.String(1))
    observacao = app.db.Column(app.db.String(250))
    ordem = app.db.Column(app.db.String(50))
    qnt_altura = app.db.Column(app.db.Numeric(18, 6))
    qnt_largura = app.db.Column(app.db.Numeric(18, 6))
    qnt_comprimento = app.db.Column(app.db.Numeric(18, 6))


# ==========================================================


class GerItemservLocal(generic_model, app.db.Model):
    __tablename__ = "ger_itemserv_local"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    desc_local1 = app.db.Column(app.db.String(50))
    desc_local2 = app.db.Column(app.db.String(100))
    desc_local3 = app.db.Column(app.db.String(100))
    observacao = app.db.Column(app.db.String(250))
    ativo = app.db.Column(app.db.String(1))
    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))


# ==========================================================


class GerItemservPessoa(generic_model, app.db.Model):
    __tablename__ = "ger_itemserv_pessoa"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    cod_itemserv_ext = app.db.Column(app.db.String(50))
    ativo = app.db.Column(app.db.String(1))
    ger_itemserv_id = app.db.Column(app.db.ForeignKey("ger_itemserv.id"))
    ger_pessoa_id = app.db.Column(app.db.ForeignKey("ger_pessoa.id"))
    ger_pessoa_id_obj = app.db.relationship("GerPessoa")


# ==========================================================


class GerProcessoBloq(generic_model, app.db.Model):
    __tablename__ = "ger_processo_bloq"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    tipo_processo = app.db.Column(app.db.String(50))
    data_lib_inicial = app.db.Column(app.db.Date)
    data_lib_final = app.db.Column(app.db.Date)
    observacao = app.db.Column(app.db.String(250))

    ger_empresa_id = app.db.Column(app.db.ForeignKey("ger_empresa.id"))
    ger_empresa_id_obj = app.db.relationship("GerEmpresa")

    ger_processo_bloq_user_childs = app.db.relationship(
        "GerProcessoBloqUser", cascade="all,delete-orphan"
    )


# ==========================================================


class GerProcessoBloqUser(generic_model, app.db.Model):
    __tablename__ = "ger_processo_bloq_user"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    tipo_bloq = app.db.Column(app.db.String(255))
    ger_processo_bloq_id = app.db.Column(app.db.ForeignKey("ger_processo_bloq.id"))
    sys_user_id = app.db.Column(app.db.ForeignKey("sys_user.id"))
    sys_user_id_obj = app.db.relationship("SysUser")
    ger_processo_bloq_id = app.db.Column(app.db.ForeignKey("ger_processo_bloq.id"))


# ==========================================================
class GerPerTipo(generic_model, app.db.Model):
    __tablename__ = "ger_per_tipo"

    unit_id = app.db.Column(app.db.ForeignKey("sys_unit.id"))
    nome = app.db.Column(app.db.String(50))
    ativo = app.db.Column(app.db.String(1))
    sigla_per_tipo = app.db.Column(app.db.String(50))
    ini_semana = app.db.Column(app.db.String(1))
