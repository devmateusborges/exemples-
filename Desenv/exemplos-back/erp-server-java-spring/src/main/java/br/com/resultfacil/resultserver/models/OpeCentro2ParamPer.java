package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.util.Date;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_centro2_param_per")
@NamedQuery(name="OpeCentro2ParamPer.findAll", query="SELECT o FROM OpeCentro2ParamPer o")
public class OpeCentro2ParamPer implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="dt_valid_ini", nullable=false)
	private Date dtValidIni;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id")
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id", nullable=false)
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeFrenteTrabalho
	@ManyToOne
	@JoinColumn(name="ope_frente_trabalho_id")
	private OpeFrenteTrabalho opeFrenteTrabalho;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentro2ParamPer() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDtValidIni() {
		return this.dtValidIni;
	}

	public void setDtValidIni(Date dtValidIni) {
		this.dtValidIni = dtValidIni;
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

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
	}

	public OpeFrenteTrabalho getOpeFrenteTrabalho() {
		return this.opeFrenteTrabalho;
	}

	public void setOpeFrenteTrabalho(OpeFrenteTrabalho opeFrenteTrabalho) {
		this.opeFrenteTrabalho = opeFrenteTrabalho;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}