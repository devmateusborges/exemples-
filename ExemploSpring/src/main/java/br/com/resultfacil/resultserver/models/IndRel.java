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
@Table(name="ind_rel")
@NamedQuery(name="IndRel.findAll", query="SELECT i FROM IndRel i")
public class IndRel implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(length=1)
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

	@Column(length=250)
	private String nome;

	@Column(name="nome_tecnico", length=100)
	private String nomeTecnico;

	@Column(length=1)
	private String tipo;

	//bi-directional many-to-one association to IndPnlRelacRel
	@OneToMany(mappedBy="indRel")
	private List<IndPnlRelacRel> indPnlRelacRels;

	//bi-directional many-to-one association to IndCjd
	@ManyToOne
	@JoinColumn(name="ind_cjd_id")
	private IndCjd indCjd;

	//bi-directional many-to-one association to IndFtd
	@ManyToOne
	@JoinColumn(name="ind_ftd_id")
	private IndFtd indFtd;

	//bi-directional many-to-one association to IndRelRelacPrm
	@OneToMany(mappedBy="indRel")
	private List<IndRelRelacPrm> indRelRelacPrms;

	//bi-directional many-to-one association to IndRelVar
	@OneToMany(mappedBy="indRel")
	private List<IndRelVar> indRelVars;

	public IndRel() {
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

	public String getNomeTecnico() {
		return this.nomeTecnico;
	}

	public void setNomeTecnico(String nomeTecnico) {
		this.nomeTecnico = nomeTecnico;
	}

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public List<IndPnlRelacRel> getIndPnlRelacRels() {
		return this.indPnlRelacRels;
	}

	public void setIndPnlRelacRels(List<IndPnlRelacRel> indPnlRelacRels) {
		this.indPnlRelacRels = indPnlRelacRels;
	}

	public IndPnlRelacRel addIndPnlRelacRel(IndPnlRelacRel indPnlRelacRel) {
		getIndPnlRelacRels().add(indPnlRelacRel);
		indPnlRelacRel.setIndRel(this);

		return indPnlRelacRel;
	}

	public IndPnlRelacRel removeIndPnlRelacRel(IndPnlRelacRel indPnlRelacRel) {
		getIndPnlRelacRels().remove(indPnlRelacRel);
		indPnlRelacRel.setIndRel(null);

		return indPnlRelacRel;
	}

	public IndCjd getIndCjd() {
		return this.indCjd;
	}

	public void setIndCjd(IndCjd indCjd) {
		this.indCjd = indCjd;
	}

	public IndFtd getIndFtd() {
		return this.indFtd;
	}

	public void setIndFtd(IndFtd indFtd) {
		this.indFtd = indFtd;
	}

	public List<IndRelRelacPrm> getIndRelRelacPrms() {
		return this.indRelRelacPrms;
	}

	public void setIndRelRelacPrms(List<IndRelRelacPrm> indRelRelacPrms) {
		this.indRelRelacPrms = indRelRelacPrms;
	}

	public IndRelRelacPrm addIndRelRelacPrm(IndRelRelacPrm indRelRelacPrm) {
		getIndRelRelacPrms().add(indRelRelacPrm);
		indRelRelacPrm.setIndRel(this);

		return indRelRelacPrm;
	}

	public IndRelRelacPrm removeIndRelRelacPrm(IndRelRelacPrm indRelRelacPrm) {
		getIndRelRelacPrms().remove(indRelRelacPrm);
		indRelRelacPrm.setIndRel(null);

		return indRelRelacPrm;
	}

	public List<IndRelVar> getIndRelVars() {
		return this.indRelVars;
	}

	public void setIndRelVars(List<IndRelVar> indRelVars) {
		this.indRelVars = indRelVars;
	}

	public IndRelVar addIndRelVar(IndRelVar indRelVar) {
		getIndRelVars().add(indRelVar);
		indRelVar.setIndRel(this);

		return indRelVar;
	}

	public IndRelVar removeIndRelVar(IndRelVar indRelVar) {
		getIndRelVars().remove(indRelVar);
		indRelVar.setIndRel(null);

		return indRelVar;
	}

}