package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.util.Date;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_centro2_mov_media")
@NamedQuery(name="OpeCentro2MovMedia.findAll", query="SELECT o FROM OpeCentro2MovMedia o")
public class OpeCentro2MovMedia implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(precision=18, scale=6)
	private BigDecimal capacidade;

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

	@Column(length=250)
	private String observacao;

	@Column(name="qnt_media_max", nullable=false, precision=18, scale=6)
	private BigDecimal qntMediaMax;

	@Column(name="qnt_media_min", nullable=false, precision=18, scale=6)
	private BigDecimal qntMediaMin;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id", nullable=false)
	private GerItemserv gerItemserv;

	//bi-directional many-to-one association to GerMarcaModelo
	@ManyToOne
	@JoinColumn(name="ger_marca_modelo_id")
	private GerMarcaModelo gerMarcaModelo;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id")
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeCompart
	@ManyToOne
	@JoinColumn(name="ope_compart_id", nullable=false)
	private OpeCompart opeCompart;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentro2MovMedia() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public BigDecimal getCapacidade() {
		return this.capacidade;
	}

	public void setCapacidade(BigDecimal capacidade) {
		this.capacidade = capacidade;
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

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public BigDecimal getQntMediaMax() {
		return this.qntMediaMax;
	}

	public void setQntMediaMax(BigDecimal qntMediaMax) {
		this.qntMediaMax = qntMediaMax;
	}

	public BigDecimal getQntMediaMin() {
		return this.qntMediaMin;
	}

	public void setQntMediaMin(BigDecimal qntMediaMin) {
		this.qntMediaMin = qntMediaMin;
	}

	public GerItemserv getGerItemserv() {
		return this.gerItemserv;
	}

	public void setGerItemserv(GerItemserv gerItemserv) {
		this.gerItemserv = gerItemserv;
	}

	public GerMarcaModelo getGerMarcaModelo() {
		return this.gerMarcaModelo;
	}

	public void setGerMarcaModelo(GerMarcaModelo gerMarcaModelo) {
		this.gerMarcaModelo = gerMarcaModelo;
	}

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
	}

	public OpeCompart getOpeCompart() {
		return this.opeCompart;
	}

	public void setOpeCompart(OpeCompart opeCompart) {
		this.opeCompart = opeCompart;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}