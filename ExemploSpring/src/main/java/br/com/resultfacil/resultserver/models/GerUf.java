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
@Table(name="ger_uf")
@NamedQuery(name="GerUf.findAll", query="SELECT g FROM GerUf g")
public class GerUf implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(nullable=false, length=100)
	private String nome;

	@Column(name="nr_uf", nullable=false, length=50)
	private String nrUf;

	@Column(name="sigla_uf", nullable=false, length=50)
	private String siglaUf;

	//bi-directional many-to-one association to FisIbpt
	@OneToMany(mappedBy="gerUf")
	private List<FisIbpt> fisIbpts;

	//bi-directional many-to-one association to GerCidade
	@OneToMany(mappedBy="gerUf")
	private List<GerCidade> gerCidades;

	//bi-directional many-to-one association to GerPai
	@ManyToOne
	@JoinColumn(name="ger_pais_id", nullable=false)
	private GerPais gerPai;

	public GerUf() {
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

	public String getNrUf() {
		return this.nrUf;
	}

	public void setNrUf(String nrUf) {
		this.nrUf = nrUf;
	}

	public String getSiglaUf() {
		return this.siglaUf;
	}

	public void setSiglaUf(String siglaUf) {
		this.siglaUf = siglaUf;
	}

	public List<FisIbpt> getFisIbpts() {
		return this.fisIbpts;
	}

	public void setFisIbpts(List<FisIbpt> fisIbpts) {
		this.fisIbpts = fisIbpts;
	}

	public FisIbpt addFisIbpt(FisIbpt fisIbpt) {
		getFisIbpts().add(fisIbpt);
		fisIbpt.setGerUf(this);

		return fisIbpt;
	}

	public FisIbpt removeFisIbpt(FisIbpt fisIbpt) {
		getFisIbpts().remove(fisIbpt);
		fisIbpt.setGerUf(null);

		return fisIbpt;
	}

	public List<GerCidade> getGerCidades() {
		return this.gerCidades;
	}

	public void setGerCidades(List<GerCidade> gerCidades) {
		this.gerCidades = gerCidades;
	}

	public GerCidade addGerCidade(GerCidade gerCidade) {
		getGerCidades().add(gerCidade);
		gerCidade.setGerUf(this);

		return gerCidade;
	}

	public GerCidade removeGerCidade(GerCidade gerCidade) {
		getGerCidades().remove(gerCidade);
		gerCidade.setGerUf(null);

		return gerCidade;
	}

	public GerPais getGerPai() {
		return this.gerPai;
	}

	public void setGerPai(GerPais gerPai) {
		this.gerPai = gerPai;
	}

}