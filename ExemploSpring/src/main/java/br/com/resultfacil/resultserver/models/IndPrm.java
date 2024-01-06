package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ind_prm")
@NamedQuery(name="IndPrm.findAll", query="SELECT i FROM IndPrm i")
public class IndPrm implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(length=1)
	private String ativo;

	@Column(name="busca_campo_id", length=50)
	private String buscaCampoId;

	@Column(name="busca_campo_id_classe", length=50)
	private String buscaCampoIdClasse;

	@Column(name="busca_campo_nome", length=50)
	private String buscaCampoNome;

	@Column(name="busca_campo_nome_classe", length=50)
	private String buscaCampoNomeClasse;

	@Column(name="busca_tabela", length=50)
	private String buscaTabela;

	@Column(name="busca_tabela_classe", length=50)
	private String buscaTabelaClasse;

	@Column(name="busca_valores", length=250)
	private String buscaValores;

	@Column(length=1)
	private String internal;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(length=250)
	private String nome;

	@Column(name="nome_tecnico", length=100)
	private String nomeTecnico;

	@Column(length=1)
	private String obrigatorio;

	@Column(name="tipo_dado", nullable=false, length=2)
	private String tipoDado;

	@Column(name="tipo_entrada", length=2)
	private String tipoEntrada;

	@Column(name="valor_padrao", length=2147483647)
	private String valorPadrao;

	@Column(name="valor_prefixo", length=250)
	private String valorPrefixo;

	@Column(name="valor_sufixo", length=250)
	private String valorSufixo;

	@Column(length=1)
	private String visivel;

	//bi-directional many-to-one association to IndFtdRelacPrm
	@OneToMany(mappedBy="indPrm")
	private List<IndFtdRelacPrm> indFtdRelacPrms;

	//bi-directional many-to-one association to IndRelRelacPrm
	@OneToMany(mappedBy="indPrm")
	private List<IndRelRelacPrm> indRelRelacPrms;

	public IndPrm() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getAtivo() {
		return this.ativo;
	}

	public void setAtivo(String ativo) {
		this.ativo = ativo;
	}

	public String getBuscaCampoId() {
		return this.buscaCampoId;
	}

	public void setBuscaCampoId(String buscaCampoId) {
		this.buscaCampoId = buscaCampoId;
	}

	public String getBuscaCampoIdClasse() {
		return this.buscaCampoIdClasse;
	}

	public void setBuscaCampoIdClasse(String buscaCampoIdClasse) {
		this.buscaCampoIdClasse = buscaCampoIdClasse;
	}

	public String getBuscaCampoNome() {
		return this.buscaCampoNome;
	}

	public void setBuscaCampoNome(String buscaCampoNome) {
		this.buscaCampoNome = buscaCampoNome;
	}

	public String getBuscaCampoNomeClasse() {
		return this.buscaCampoNomeClasse;
	}

	public void setBuscaCampoNomeClasse(String buscaCampoNomeClasse) {
		this.buscaCampoNomeClasse = buscaCampoNomeClasse;
	}

	public String getBuscaTabela() {
		return this.buscaTabela;
	}

	public void setBuscaTabela(String buscaTabela) {
		this.buscaTabela = buscaTabela;
	}

	public String getBuscaTabelaClasse() {
		return this.buscaTabelaClasse;
	}

	public void setBuscaTabelaClasse(String buscaTabelaClasse) {
		this.buscaTabelaClasse = buscaTabelaClasse;
	}

	public String getBuscaValores() {
		return this.buscaValores;
	}

	public void setBuscaValores(String buscaValores) {
		this.buscaValores = buscaValores;
	}

	public String getInternal() {
		return this.internal;
	}

	public void setInternal(String internal) {
		this.internal = internal;
	}

	public Timestamp getLogDateIns() {
		return this.logDateIns;
	}

	public void setLogDateIns(Timestamp logDateIns) {
		this.logDateIns = logDateIns;
	}

	public Timestamp getLogDateUpd() {
		return this.logDateUpd;
	}

	public void setLogDateUpd(Timestamp logDateUpd) {
		this.logDateUpd = logDateUpd;
	}

	public String getLogUserIns() {
		return this.logUserIns;
	}

	public void setLogUserIns(String logUserIns) {
		this.logUserIns = logUserIns;
	}

	public String getLogUserUpd() {
		return this.logUserUpd;
	}

	public void setLogUserUpd(String logUserUpd) {
		this.logUserUpd = logUserUpd;
	}

	public String getNome() {
		return this.nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getNomeTecnico() {
		return this.nomeTecnico;
	}

	public void setNomeTecnico(String nomeTecnico) {
		this.nomeTecnico = nomeTecnico;
	}

	public String getObrigatorio() {
		return this.obrigatorio;
	}

	public void setObrigatorio(String obrigatorio) {
		this.obrigatorio = obrigatorio;
	}

	public String getTipoDado() {
		return this.tipoDado;
	}

	public void setTipoDado(String tipoDado) {
		this.tipoDado = tipoDado;
	}

	public String getTipoEntrada() {
		return this.tipoEntrada;
	}

	public void setTipoEntrada(String tipoEntrada) {
		this.tipoEntrada = tipoEntrada;
	}

	public String getValorPadrao() {
		return this.valorPadrao;
	}

	public void setValorPadrao(String valorPadrao) {
		this.valorPadrao = valorPadrao;
	}

	public String getValorPrefixo() {
		return this.valorPrefixo;
	}

	public void setValorPrefixo(String valorPrefixo) {
		this.valorPrefixo = valorPrefixo;
	}

	public String getValorSufixo() {
		return this.valorSufixo;
	}

	public void setValorSufixo(String valorSufixo) {
		this.valorSufixo = valorSufixo;
	}

	public String getVisivel() {
		return this.visivel;
	}

	public void setVisivel(String visivel) {
		this.visivel = visivel;
	}

	public List<IndFtdRelacPrm> getIndFtdRelacPrms() {
		return this.indFtdRelacPrms;
	}

	public void setIndFtdRelacPrms(List<IndFtdRelacPrm> indFtdRelacPrms) {
		this.indFtdRelacPrms = indFtdRelacPrms;
	}

	public IndFtdRelacPrm addIndFtdRelacPrm(IndFtdRelacPrm indFtdRelacPrm) {
		getIndFtdRelacPrms().add(indFtdRelacPrm);
		indFtdRelacPrm.setIndPrm(this);

		return indFtdRelacPrm;
	}

	public IndFtdRelacPrm removeIndFtdRelacPrm(IndFtdRelacPrm indFtdRelacPrm) {
		getIndFtdRelacPrms().remove(indFtdRelacPrm);
		indFtdRelacPrm.setIndPrm(null);

		return indFtdRelacPrm;
	}

	public List<IndRelRelacPrm> getIndRelRelacPrms() {
		return this.indRelRelacPrms;
	}

	public void setIndRelRelacPrms(List<IndRelRelacPrm> indRelRelacPrms) {
		this.indRelRelacPrms = indRelRelacPrms;
	}

	public IndRelRelacPrm addIndRelRelacPrm(IndRelRelacPrm indRelRelacPrm) {
		getIndRelRelacPrms().add(indRelRelacPrm);
		indRelRelacPrm.setIndPrm(this);

		return indRelRelacPrm;
	}

	public IndRelRelacPrm removeIndRelRelacPrm(IndRelRelacPrm indRelRelacPrm) {
		getIndRelRelacPrms().remove(indRelRelacPrm);
		indRelRelacPrm.setIndPrm(null);

		return indRelRelacPrm;
	}

}