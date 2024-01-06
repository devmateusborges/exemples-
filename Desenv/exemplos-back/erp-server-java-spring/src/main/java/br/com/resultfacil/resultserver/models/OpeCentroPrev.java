package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.util.Date;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_centro_prev")
@NamedQuery(name="OpeCentroPrev.findAll", query="SELECT o FROM OpeCentroPrev o")
public class OpeCentroPrev implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_per", nullable=false)
	private Date dataPer;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="ordem_exec", length=3)
	private String ordemExec;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt01;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt02;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt03;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt04;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt05;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt06;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt07;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt08;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt09;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt10;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt11;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt12;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt13;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt14;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt15;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt16;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt17;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt18;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt19;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt20;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt21;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt22;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt23;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt24;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt25;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt26;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt27;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt28;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt29;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt30;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal qnt31;

	@Column(name="tipo_executor", length=1)
	private String tipoExecutor;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to OpeAtividade
	@ManyToOne
	@JoinColumn(name="ope_atividade_id", nullable=false)
	private OpeAtividade opeAtividade;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id")
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeCentro2OrdTipo
	@ManyToOne
	@JoinColumn(name="ope_centro2_ord_tipo_id")
	private OpeCentro2OrdTipo opeCentro2OrdTipo;

	//bi-directional many-to-one association to OpeCentroVersao
	@ManyToOne
	@JoinColumn(name="ope_centro_versao_id", nullable=false)
	private OpeCentroVersao opeCentroVersao;

	//bi-directional many-to-one association to OpePeriodo
	@ManyToOne
	@JoinColumn(name="ope_periodo_id", nullable=false)
	private OpePeriodo opePeriodo;

	//bi-directional many-to-one association to SysProcessLog
	@ManyToOne
	@JoinColumn(name="process_id")
	private SysProcessLog sysProcessLog;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCentroPrevDest
	@OneToMany(mappedBy="opeCentroPrev")
	private List<OpeCentroPrevDest> opeCentroPrevDests;

	public OpeCentroPrev() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataPer() {
		return this.dataPer;
	}

	public void setDataPer(Date dataPer) {
		this.dataPer = dataPer;
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

	public String getOrdemExec() {
		return this.ordemExec;
	}

	public void setOrdemExec(String ordemExec) {
		this.ordemExec = ordemExec;
	}

	public BigDecimal getQnt01() {
		return this.qnt01;
	}

	public void setQnt01(BigDecimal qnt01) {
		this.qnt01 = qnt01;
	}

	public BigDecimal getQnt02() {
		return this.qnt02;
	}

	public void setQnt02(BigDecimal qnt02) {
		this.qnt02 = qnt02;
	}

	public BigDecimal getQnt03() {
		return this.qnt03;
	}

	public void setQnt03(BigDecimal qnt03) {
		this.qnt03 = qnt03;
	}

	public BigDecimal getQnt04() {
		return this.qnt04;
	}

	public void setQnt04(BigDecimal qnt04) {
		this.qnt04 = qnt04;
	}

	public BigDecimal getQnt05() {
		return this.qnt05;
	}

	public void setQnt05(BigDecimal qnt05) {
		this.qnt05 = qnt05;
	}

	public BigDecimal getQnt06() {
		return this.qnt06;
	}

	public void setQnt06(BigDecimal qnt06) {
		this.qnt06 = qnt06;
	}

	public BigDecimal getQnt07() {
		return this.qnt07;
	}

	public void setQnt07(BigDecimal qnt07) {
		this.qnt07 = qnt07;
	}

	public BigDecimal getQnt08() {
		return this.qnt08;
	}

	public void setQnt08(BigDecimal qnt08) {
		this.qnt08 = qnt08;
	}

	public BigDecimal getQnt09() {
		return this.qnt09;
	}

	public void setQnt09(BigDecimal qnt09) {
		this.qnt09 = qnt09;
	}

	public BigDecimal getQnt10() {
		return this.qnt10;
	}

	public void setQnt10(BigDecimal qnt10) {
		this.qnt10 = qnt10;
	}

	public BigDecimal getQnt11() {
		return this.qnt11;
	}

	public void setQnt11(BigDecimal qnt11) {
		this.qnt11 = qnt11;
	}

	public BigDecimal getQnt12() {
		return this.qnt12;
	}

	public void setQnt12(BigDecimal qnt12) {
		this.qnt12 = qnt12;
	}

	public BigDecimal getQnt13() {
		return this.qnt13;
	}

	public void setQnt13(BigDecimal qnt13) {
		this.qnt13 = qnt13;
	}

	public BigDecimal getQnt14() {
		return this.qnt14;
	}

	public void setQnt14(BigDecimal qnt14) {
		this.qnt14 = qnt14;
	}

	public BigDecimal getQnt15() {
		return this.qnt15;
	}

	public void setQnt15(BigDecimal qnt15) {
		this.qnt15 = qnt15;
	}

	public BigDecimal getQnt16() {
		return this.qnt16;
	}

	public void setQnt16(BigDecimal qnt16) {
		this.qnt16 = qnt16;
	}

	public BigDecimal getQnt17() {
		return this.qnt17;
	}

	public void setQnt17(BigDecimal qnt17) {
		this.qnt17 = qnt17;
	}

	public BigDecimal getQnt18() {
		return this.qnt18;
	}

	public void setQnt18(BigDecimal qnt18) {
		this.qnt18 = qnt18;
	}

	public BigDecimal getQnt19() {
		return this.qnt19;
	}

	public void setQnt19(BigDecimal qnt19) {
		this.qnt19 = qnt19;
	}

	public BigDecimal getQnt20() {
		return this.qnt20;
	}

	public void setQnt20(BigDecimal qnt20) {
		this.qnt20 = qnt20;
	}

	public BigDecimal getQnt21() {
		return this.qnt21;
	}

	public void setQnt21(BigDecimal qnt21) {
		this.qnt21 = qnt21;
	}

	public BigDecimal getQnt22() {
		return this.qnt22;
	}

	public void setQnt22(BigDecimal qnt22) {
		this.qnt22 = qnt22;
	}

	public BigDecimal getQnt23() {
		return this.qnt23;
	}

	public void setQnt23(BigDecimal qnt23) {
		this.qnt23 = qnt23;
	}

	public BigDecimal getQnt24() {
		return this.qnt24;
	}

	public void setQnt24(BigDecimal qnt24) {
		this.qnt24 = qnt24;
	}

	public BigDecimal getQnt25() {
		return this.qnt25;
	}

	public void setQnt25(BigDecimal qnt25) {
		this.qnt25 = qnt25;
	}

	public BigDecimal getQnt26() {
		return this.qnt26;
	}

	public void setQnt26(BigDecimal qnt26) {
		this.qnt26 = qnt26;
	}

	public BigDecimal getQnt27() {
		return this.qnt27;
	}

	public void setQnt27(BigDecimal qnt27) {
		this.qnt27 = qnt27;
	}

	public BigDecimal getQnt28() {
		return this.qnt28;
	}

	public void setQnt28(BigDecimal qnt28) {
		this.qnt28 = qnt28;
	}

	public BigDecimal getQnt29() {
		return this.qnt29;
	}

	public void setQnt29(BigDecimal qnt29) {
		this.qnt29 = qnt29;
	}

	public BigDecimal getQnt30() {
		return this.qnt30;
	}

	public void setQnt30(BigDecimal qnt30) {
		this.qnt30 = qnt30;
	}

	public BigDecimal getQnt31() {
		return this.qnt31;
	}

	public void setQnt31(BigDecimal qnt31) {
		this.qnt31 = qnt31;
	}

	public String getTipoExecutor() {
		return this.tipoExecutor;
	}

	public void setTipoExecutor(String tipoExecutor) {
		this.tipoExecutor = tipoExecutor;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
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

	public OpeCentro2OrdTipo getOpeCentro2OrdTipo() {
		return this.opeCentro2OrdTipo;
	}

	public void setOpeCentro2OrdTipo(OpeCentro2OrdTipo opeCentro2OrdTipo) {
		this.opeCentro2OrdTipo = opeCentro2OrdTipo;
	}

	public OpeCentroVersao getOpeCentroVersao() {
		return this.opeCentroVersao;
	}

	public void setOpeCentroVersao(OpeCentroVersao opeCentroVersao) {
		this.opeCentroVersao = opeCentroVersao;
	}

	public OpePeriodo getOpePeriodo() {
		return this.opePeriodo;
	}

	public void setOpePeriodo(OpePeriodo opePeriodo) {
		this.opePeriodo = opePeriodo;
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

	public List<OpeCentroPrevDest> getOpeCentroPrevDests() {
		return this.opeCentroPrevDests;
	}

	public void setOpeCentroPrevDests(List<OpeCentroPrevDest> opeCentroPrevDests) {
		this.opeCentroPrevDests = opeCentroPrevDests;
	}

	public OpeCentroPrevDest addOpeCentroPrevDest(OpeCentroPrevDest opeCentroPrevDest) {
		getOpeCentroPrevDests().add(opeCentroPrevDest);
		opeCentroPrevDest.setOpeCentroPrev(this);

		return opeCentroPrevDest;
	}

	public OpeCentroPrevDest removeOpeCentroPrevDest(OpeCentroPrevDest opeCentroPrevDest) {
		getOpeCentroPrevDests().remove(opeCentroPrevDest);
		opeCentroPrevDest.setOpeCentroPrev(null);

		return opeCentroPrevDest;
	}

}