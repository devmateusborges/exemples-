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
@Table(name="ctb_lanc_det")
@NamedQuery(name="CtbLancDet.findAll", query="SELECT c FROM CtbLancDet c")
public class CtbLancDet implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

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

	@Column(name="origem_id", nullable=false, length=36)
	private String origemId;

	@Column(name="origem_tipo", nullable=false, length=50)
	private String origemTipo;

	@Column(nullable=false, precision=18, scale=6)
	private BigDecimal qnt;

	@Column(name="tipo_dc", nullable=false, length=1)
	private String tipoDc;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor;

	//bi-directional many-to-one association to CtbComp
	@ManyToOne
	@JoinColumn(name="ctb_comp_id")
	private CtbComp ctbComp;

	//bi-directional many-to-one association to CtbConta
	@ManyToOne
	@JoinColumn(name="ctb_conta_id", nullable=false)
	private CtbConta ctbConta;

	//bi-directional many-to-one association to CtbLanc
	@ManyToOne
	@JoinColumn(name="ctb_lanc_id", nullable=false)
	private CtbLanc ctbLanc;

	//bi-directional many-to-one association to OpeAtividade
	@ManyToOne
	@JoinColumn(name="ope_atividade_id")
	private OpeAtividade opeAtividade;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id")
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to SysProcessLog
	@ManyToOne
	@JoinColumn(name="process_id")
	private SysProcessLog sysProcessLog;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public CtbLancDet() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
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

	public String getOrigemId() {
		return this.origemId;
	}

	public void setOrigemId(String origemId) {
		this.origemId = origemId;
	}

	public String getOrigemTipo() {
		return this.origemTipo;
	}

	public void setOrigemTipo(String origemTipo) {
		this.origemTipo = origemTipo;
	}

	public BigDecimal getQnt() {
		return this.qnt;
	}

	public void setQnt(BigDecimal qnt) {
		this.qnt = qnt;
	}

	public String getTipoDc() {
		return this.tipoDc;
	}

	public void setTipoDc(String tipoDc) {
		this.tipoDc = tipoDc;
	}

	public BigDecimal getValor() {
		return this.valor;
	}

	public void setValor(BigDecimal valor) {
		this.valor = valor;
	}

	public CtbComp getCtbComp() {
		return this.ctbComp;
	}

	public void setCtbComp(CtbComp ctbComp) {
		this.ctbComp = ctbComp;
	}

	public CtbConta getCtbConta() {
		return this.ctbConta;
	}

	public void setCtbConta(CtbConta ctbConta) {
		this.ctbConta = ctbConta;
	}

	public CtbLanc getCtbLanc() {
		return this.ctbLanc;
	}

	public void setCtbLanc(CtbLanc ctbLanc) {
		this.ctbLanc = ctbLanc;
	}

	public OpeAtividade getOpeAtividade() {
		return this.opeAtividade;
	}

	public void setOpeAtividade(OpeAtividade opeAtividade) {
		this.opeAtividade = opeAtividade;
	}

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
	}

	public SysProcessLog getSysProcessLog() {
		return this.sysProcessLog;
	}

	public void setSysProcessLog(SysProcessLog sysProcessLog) {
		this.sysProcessLog = sysProcessLog;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}