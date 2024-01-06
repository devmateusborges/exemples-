package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.util.Date;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="fis_nbs")
@NamedQuery(name="FisNbs.findAll", query="SELECT f FROM FisNbs f")
public class FisNbs implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Temporal(TemporalType.DATE)
	@Column(name="data_validade", nullable=false)
	private Date dataValidade;

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

	@Column(name="nr_nbs", nullable=false, length=50)
	private String nrNbs;

	//bi-directional many-to-one association to FisIbpt
	@OneToMany(mappedBy="fisNb")
	private List<FisIbpt> fisIbpts;

	//bi-directional many-to-one association to GerItemserv
	@OneToMany(mappedBy="fisNb")
	private List<GerItemserv> gerItemservs;

	public FisNbs() {
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

	public Date getDataValidade() {
		return this.dataValidade;
	}

	public void setDataValidade(Date dataValidade) {
		this.dataValidade = dataValidade;
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

	public String getNrNbs() {
		return this.nrNbs;
	}

	public void setNrNbs(String nrNbs) {
		this.nrNbs = nrNbs;
	}

	public List<FisIbpt> getFisIbpts() {
		return this.fisIbpts;
	}

	public void setFisIbpts(List<FisIbpt> fisIbpts) {
		this.fisIbpts = fisIbpts;
	}

	public FisIbpt addFisIbpt(FisIbpt fisIbpt) {
		getFisIbpts().add(fisIbpt);
		fisIbpt.setFisNb(this);

		return fisIbpt;
	}

	public FisIbpt removeFisIbpt(FisIbpt fisIbpt) {
		getFisIbpts().remove(fisIbpt);
		fisIbpt.setFisNb(null);

		return fisIbpt;
	}

	public List<GerItemserv> getGerItemservs() {
		return this.gerItemservs;
	}

	public void setGerItemservs(List<GerItemserv> gerItemservs) {
		this.gerItemservs = gerItemservs;
	}

	public GerItemserv addGerItemserv(GerItemserv gerItemserv) {
		getGerItemservs().add(gerItemserv);
		gerItemserv.setFisNb(this);

		return gerItemserv;
	}

	public GerItemserv removeGerItemserv(GerItemserv gerItemserv) {
		getGerItemservs().remove(gerItemserv);
		gerItemserv.setFisNb(null);

		return gerItemserv;
	}

}