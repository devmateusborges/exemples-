package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_centro_rat_fator")
@NamedQuery(name="OpeCentroRatFator.findAll", query="SELECT o FROM OpeCentroRatFator o")
public class OpeCentroRatFator implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="fator_rat", nullable=false, precision=18, scale=6)
	private BigDecimal fatorRat;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="perc_rat", precision=18, scale=6)
	private BigDecimal percRat;

	//bi-directional many-to-one association to CtbCentro
	@ManyToOne
	@JoinColumn(name="ctb_centro_id")
	private CtbCentro ctbCentro;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to OpeCentro1
	@ManyToOne
	@JoinColumn(name="ope_centro1_id")
	private OpeCentro1 opeCentro1;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id")
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeCentroRatPeriodo
	@ManyToOne
	@JoinColumn(name="ope_centro_rat_periodo_id", nullable=false)
	private OpeCentroRatPeriodo opeCentroRatPeriodo;

	//bi-directional many-to-one association to OpeCentroSubtipo
	@ManyToOne
	@JoinColumn(name="ope_centro_subtipo_id", nullable=false)
	private OpeCentroSubtipo opeCentroSubtipo;

	//bi-directional many-to-one association to OpePeriodo
	@ManyToOne
	@JoinColumn(name="ope_periodo_id")
	private OpePeriodo opePeriodo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentroRatFator() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public BigDecimal getFatorRat() {
		return this.fatorRat;
	}

	public void setFatorRat(BigDecimal fatorRat) {
		this.fatorRat = fatorRat;
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

	public BigDecimal getPercRat() {
		return this.percRat;
	}

	public void setPercRat(BigDecimal percRat) {
		this.percRat = percRat;
	}

	public CtbCentro getCtbCentro() {
		return this.ctbCentro;
	}

	public void setCtbCentro(CtbCentro ctbCentro) {
		this.ctbCentro = ctbCentro;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public OpeCentro1 getOpeCentro1() {
		return this.opeCentro1;
	}

	public void setOpeCentro1(OpeCentro1 opeCentro1) {
		this.opeCentro1 = opeCentro1;
	}

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
	}

	public OpeCentroRatPeriodo getOpeCentroRatPeriodo() {
		return this.opeCentroRatPeriodo;
	}

	public void setOpeCentroRatPeriodo(OpeCentroRatPeriodo opeCentroRatPeriodo) {
		this.opeCentroRatPeriodo = opeCentroRatPeriodo;
	}

	public OpeCentroSubtipo getOpeCentroSubtipo() {
		return this.opeCentroSubtipo;
	}

	public void setOpeCentroSubtipo(OpeCentroSubtipo opeCentroSubtipo) {
		this.opeCentroSubtipo = opeCentroSubtipo;
	}

	public OpePeriodo getOpePeriodo() {
		return this.opePeriodo;
	}

	public void setOpePeriodo(OpePeriodo opePeriodo) {
		this.opePeriodo = opePeriodo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}