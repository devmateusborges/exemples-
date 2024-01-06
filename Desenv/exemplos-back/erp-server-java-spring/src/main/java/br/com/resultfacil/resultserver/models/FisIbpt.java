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
@Table(name="fis_ibpt")
@NamedQuery(name="FisIbpt.findAll", query="SELECT f FROM FisIbpt f")
public class FisIbpt implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_validade_fin", nullable=false)
	private Date dataValidadeFin;

	@Temporal(TemporalType.DATE)
	@Column(name="data_validade_ini", nullable=false)
	private Date dataValidadeIni;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="perc_importado", nullable=false, precision=18, scale=6)
	private BigDecimal percImportado;

	@Column(name="perc_municipal", nullable=false, precision=18, scale=6)
	private BigDecimal percMunicipal;

	@Column(name="perc_nacional", nullable=false, precision=18, scale=6)
	private BigDecimal percNacional;

	//bi-directional many-to-one association to FisNb
	@ManyToOne
	@JoinColumn(name="fis_nbs_id")
	private FisNbs fisNb;

	//bi-directional many-to-one association to FisNcm
	@ManyToOne
	@JoinColumn(name="fis_ncm_id")
	private FisNcm fisNcm;

	//bi-directional many-to-one association to GerUf
	@ManyToOne
	@JoinColumn(name="ger_uf_id", nullable=false)
	private GerUf gerUf;

	public FisIbpt() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataValidadeFin() {
		return this.dataValidadeFin;
	}

	public void setDataValidadeFin(Date dataValidadeFin) {
		this.dataValidadeFin = dataValidadeFin;
	}

	public Date getDataValidadeIni() {
		return this.dataValidadeIni;
	}

	public void setDataValidadeIni(Date dataValidadeIni) {
		this.dataValidadeIni = dataValidadeIni;
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

	public BigDecimal getPercImportado() {
		return this.percImportado;
	}

	public void setPercImportado(BigDecimal percImportado) {
		this.percImportado = percImportado;
	}

	public BigDecimal getPercMunicipal() {
		return this.percMunicipal;
	}

	public void setPercMunicipal(BigDecimal percMunicipal) {
		this.percMunicipal = percMunicipal;
	}

	public BigDecimal getPercNacional() {
		return this.percNacional;
	}

	public void setPercNacional(BigDecimal percNacional) {
		this.percNacional = percNacional;
	}

	public FisNbs getFisNb() {
		return this.fisNb;
	}

	public void setFisNb(FisNbs fisNb) {
		this.fisNb = fisNb;
	}

	public FisNcm getFisNcm() {
		return this.fisNcm;
	}

	public void setFisNcm(FisNcm fisNcm) {
		this.fisNcm = fisNcm;
	}

	public GerUf getGerUf() {
		return this.gerUf;
	}

	public void setGerUf(GerUf gerUf) {
		this.gerUf = gerUf;
	}

}