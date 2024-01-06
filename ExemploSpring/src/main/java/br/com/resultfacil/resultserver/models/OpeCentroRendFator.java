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
@Table(name="ope_centro_rend_fator")
@NamedQuery(name="OpeCentroRendFator.findAll", query="SELECT o FROM OpeCentroRendFator o")
public class OpeCentroRendFator implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="fator_rend", nullable=false, precision=18, scale=4)
	private BigDecimal fatorRend;

	@Column(name="fator_util", nullable=false, precision=18, scale=4)
	private BigDecimal fatorUtil;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	//bi-directional many-to-one association to CtbComp
	@ManyToOne
	@JoinColumn(name="ctb_comp_id", nullable=false)
	private CtbComp ctbComp;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id")
	private GerItemserv gerItemserv;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id")
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeCentroRend
	@ManyToOne
	@JoinColumn(name="ope_centro_rend_id", nullable=false)
	private OpeCentroRend opeCentroRend;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentroRendFator() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public BigDecimal getFatorRend() {
		return this.fatorRend;
	}

	public void setFatorRend(BigDecimal fatorRend) {
		this.fatorRend = fatorRend;
	}

	public BigDecimal getFatorUtil() {
		return this.fatorUtil;
	}

	public void setFatorUtil(BigDecimal fatorUtil) {
		this.fatorUtil = fatorUtil;
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

	public CtbComp getCtbComp() {
		return this.ctbComp;
	}

	public void setCtbComp(CtbComp ctbComp) {
		this.ctbComp = ctbComp;
	}

	public GerItemserv getGerItemserv() {
		return this.gerItemserv;
	}

	public void setGerItemserv(GerItemserv gerItemserv) {
		this.gerItemserv = gerItemserv;
	}

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
	}

	public OpeCentroRend getOpeCentroRend() {
		return this.opeCentroRend;
	}

	public void setOpeCentroRend(OpeCentroRend opeCentroRend) {
		this.opeCentroRend = opeCentroRend;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}