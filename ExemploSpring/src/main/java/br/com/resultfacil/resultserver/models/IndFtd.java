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
@Table(name="ind_ftd")
@NamedQuery(name="IndFtd.findAll", query="SELECT i FROM IndFtd i")
public class IndFtd implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(length=1)
	private String ativo;

	@Column(name="config_ftd", length=2147483647)
	private String configFtd;

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

	@Column(name="nome_tecnico", length=50)
	private String nomeTecnico;

	//bi-directional many-to-one association to IndCjdRelacFtd
	@OneToMany(mappedBy="indFtd")
	private List<IndCjdRelacFtd> indCjdRelacFtds;

	//bi-directional many-to-one association to IndCnd
	@ManyToOne
	@JoinColumn(name="ind_cnd_id")
	private IndCnd indCnd;

	//bi-directional many-to-one association to IndFtdRelacPrm
	@OneToMany(mappedBy="indFtd")
	private List<IndFtdRelacPrm> indFtdRelacPrms;

	//bi-directional many-to-one association to IndRel
	@OneToMany(mappedBy="indFtd")
	private List<IndRel> indRels;

	public IndFtd() {
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

	public String getConfigFtd() {
		return this.configFtd;
	}

	public void setConfigFtd(String configFtd) {
		this.configFtd = configFtd;
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

	public List<IndCjdRelacFtd> getIndCjdRelacFtds() {
		return this.indCjdRelacFtds;
	}

	public void setIndCjdRelacFtds(List<IndCjdRelacFtd> indCjdRelacFtds) {
		this.indCjdRelacFtds = indCjdRelacFtds;
	}

	public IndCjdRelacFtd addIndCjdRelacFtd(IndCjdRelacFtd indCjdRelacFtd) {
		getIndCjdRelacFtds().add(indCjdRelacFtd);
		indCjdRelacFtd.setIndFtd(this);

		return indCjdRelacFtd;
	}

	public IndCjdRelacFtd removeIndCjdRelacFtd(IndCjdRelacFtd indCjdRelacFtd) {
		getIndCjdRelacFtds().remove(indCjdRelacFtd);
		indCjdRelacFtd.setIndFtd(null);

		return indCjdRelacFtd;
	}

	public IndCnd getIndCnd() {
		return this.indCnd;
	}

	public void setIndCnd(IndCnd indCnd) {
		this.indCnd = indCnd;
	}

	public List<IndFtdRelacPrm> getIndFtdRelacPrms() {
		return this.indFtdRelacPrms;
	}

	public void setIndFtdRelacPrms(List<IndFtdRelacPrm> indFtdRelacPrms) {
		this.indFtdRelacPrms = indFtdRelacPrms;
	}

	public IndFtdRelacPrm addIndFtdRelacPrm(IndFtdRelacPrm indFtdRelacPrm) {
		getIndFtdRelacPrms().add(indFtdRelacPrm);
		indFtdRelacPrm.setIndFtd(this);

		return indFtdRelacPrm;
	}

	public IndFtdRelacPrm removeIndFtdRelacPrm(IndFtdRelacPrm indFtdRelacPrm) {
		getIndFtdRelacPrms().remove(indFtdRelacPrm);
		indFtdRelacPrm.setIndFtd(null);

		return indFtdRelacPrm;
	}

	public List<IndRel> getIndRels() {
		return this.indRels;
	}

	public void setIndRels(List<IndRel> indRels) {
		this.indRels = indRels;
	}

	public IndRel addIndRel(IndRel indRel) {
		getIndRels().add(indRel);
		indRel.setIndFtd(this);

		return indRel;
	}

	public IndRel removeIndRel(IndRel indRel) {
		getIndRels().remove(indRel);
		indRel.setIndFtd(null);

		return indRel;
	}

}