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
@Table(name="ope_compart_status")
@NamedQuery(name="OpeCompartStatus.findAll", query="SELECT o FROM OpeCompartStatus o")
public class OpeCompartStatus implements Serializable {
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

	@Column(name="sigla_compart_status", nullable=false, length=50)
	private String siglaCompartStatus;

	@Column(name="tipo_status", nullable=false, length=1)
	private String tipoStatus;

	//bi-directional many-to-one association to OpeCompart
	@OneToMany(mappedBy="opeCompartStatus")
	private List<OpeCompart> opeComparts;

	//bi-directional many-to-one association to OpeCompartOcor
	@OneToMany(mappedBy="opeCompartStatus")
	private List<OpeCompartOcor> opeCompartOcors;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCompartStatus() {
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

	public String getSiglaCompartStatus() {
		return this.siglaCompartStatus;
	}

	public void setSiglaCompartStatus(String siglaCompartStatus) {
		this.siglaCompartStatus = siglaCompartStatus;
	}

	public String getTipoStatus() {
		return this.tipoStatus;
	}

	public void setTipoStatus(String tipoStatus) {
		this.tipoStatus = tipoStatus;
	}

	public List<OpeCompart> getOpeComparts() {
		return this.opeComparts;
	}

	public void setOpeComparts(List<OpeCompart> opeComparts) {
		this.opeComparts = opeComparts;
	}

	public OpeCompart addOpeCompart(OpeCompart opeCompart) {
		getOpeComparts().add(opeCompart);
		opeCompart.setOpeCompartStatus(this);

		return opeCompart;
	}

	public OpeCompart removeOpeCompart(OpeCompart opeCompart) {
		getOpeComparts().remove(opeCompart);
		opeCompart.setOpeCompartStatus(null);

		return opeCompart;
	}

	public List<OpeCompartOcor> getOpeCompartOcors() {
		return this.opeCompartOcors;
	}

	public void setOpeCompartOcors(List<OpeCompartOcor> opeCompartOcors) {
		this.opeCompartOcors = opeCompartOcors;
	}

	public OpeCompartOcor addOpeCompartOcor(OpeCompartOcor opeCompartOcor) {
		getOpeCompartOcors().add(opeCompartOcor);
		opeCompartOcor.setOpeCompartStatus(this);

		return opeCompartOcor;
	}

	public OpeCompartOcor removeOpeCompartOcor(OpeCompartOcor opeCompartOcor) {
		getOpeCompartOcors().remove(opeCompartOcor);
		opeCompartOcor.setOpeCompartStatus(null);

		return opeCompartOcor;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}