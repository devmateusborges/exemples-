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
@Table(name="ope_ciclo_var")
@NamedQuery(name="OpeCicloVar.findAll", query="SELECT o FROM OpeCicloVar o")
public class OpeCicloVar implements Serializable {
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

	@Column(name="sigla_ope_ciclo_var", length=50)
	private String siglaOpeCicloVar;

	//bi-directional many-to-one association to GerItemservVar
	@OneToMany(mappedBy="opeCicloVar")
	private List<GerItemservVar> gerItemservVars;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCicloVar() {
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

	public String getSiglaOpeCicloVar() {
		return this.siglaOpeCicloVar;
	}

	public void setSiglaOpeCicloVar(String siglaOpeCicloVar) {
		this.siglaOpeCicloVar = siglaOpeCicloVar;
	}

	public List<GerItemservVar> getGerItemservVars() {
		return this.gerItemservVars;
	}

	public void setGerItemservVars(List<GerItemservVar> gerItemservVars) {
		this.gerItemservVars = gerItemservVars;
	}

	public GerItemservVar addGerItemservVar(GerItemservVar gerItemservVar) {
		getGerItemservVars().add(gerItemservVar);
		gerItemservVar.setOpeCicloVar(this);

		return gerItemservVar;
	}

	public GerItemservVar removeGerItemservVar(GerItemservVar gerItemservVar) {
		getGerItemservVars().remove(gerItemservVar);
		gerItemservVar.setOpeCicloVar(null);

		return gerItemservVar;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}