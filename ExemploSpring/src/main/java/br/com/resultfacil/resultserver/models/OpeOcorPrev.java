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
@Table(name="ope_ocor_prev")
@NamedQuery(name="OpeOcorPrev.findAll", query="SELECT o FROM OpeOcorPrev o")
public class OpeOcorPrev implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_ult_solucao")
	private Date dataUltSolucao;

	@Temporal(TemporalType.DATE)
	@Column(name="data_valid_ini", nullable=false)
	private Date dataValidIni;

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

	@Column(name="qnt_aviso", nullable=false)
	private Integer qntAviso;

	@Column(name="qnt_dia_aviso", nullable=false)
	private Integer qntDiaAviso;

	@Column(name="qnt_dia_limite", nullable=false)
	private Integer qntDiaLimite;

	@Column(name="qnt_limite", nullable=false)
	private Integer qntLimite;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id", nullable=false)
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeCompart
	@ManyToOne
	@JoinColumn(name="ope_compart_id")
	private OpeCompart opeCompart;

	//bi-directional many-to-one association to OpeOcor
	@ManyToOne
	@JoinColumn(name="ope_ocor_id", nullable=false)
	private OpeOcor opeOcor;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeOcorPrev() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataUltSolucao() {
		return this.dataUltSolucao;
	}

	public void setDataUltSolucao(Date dataUltSolucao) {
		this.dataUltSolucao = dataUltSolucao;
	}

	public Date getDataValidIni() {
		return this.dataValidIni;
	}

	public void setDataValidIni(Date dataValidIni) {
		this.dataValidIni = dataValidIni;
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

	public Integer getQntAviso() {
		return this.qntAviso;
	}

	public void setQntAviso(Integer qntAviso) {
		this.qntAviso = qntAviso;
	}

	public Integer getQntDiaAviso() {
		return this.qntDiaAviso;
	}

	public void setQntDiaAviso(Integer qntDiaAviso) {
		this.qntDiaAviso = qntDiaAviso;
	}

	public Integer getQntDiaLimite() {
		return this.qntDiaLimite;
	}

	public void setQntDiaLimite(Integer qntDiaLimite) {
		this.qntDiaLimite = qntDiaLimite;
	}

	public Integer getQntLimite() {
		return this.qntLimite;
	}

	public void setQntLimite(Integer qntLimite) {
		this.qntLimite = qntLimite;
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

	public OpeOcor getOpeOcor() {
		return this.opeOcor;
	}

	public void setOpeOcor(OpeOcor opeOcor) {
		this.opeOcor = opeOcor;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}