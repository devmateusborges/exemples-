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
@Table(name="fin_pagrec_prev")
@NamedQuery(name="FinPagrecPrev.findAll", query="SELECT f FROM FinPagrecPrev f")
public class FinPagrecPrev implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_per", nullable=false)
	private Date dataPer;

	@Temporal(TemporalType.DATE)
	@Column(name="data_valid")
	private Date dataValid;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="tipo_es", length=1)
	private String tipoEs;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor01;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor02;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor03;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor04;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor05;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor06;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor07;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor08;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor09;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor10;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor11;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor12;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor13;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor14;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor15;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor16;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor17;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor18;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor19;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor20;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor21;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor22;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor23;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor24;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor25;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor26;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor27;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor28;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor29;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor30;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor31;

	//bi-directional many-to-one association to FinClass
	@ManyToOne
	@JoinColumn(name="fin_class_id", nullable=false)
	private FinClass finClass;

	//bi-directional many-to-one association to FinPagrecVersao
	@ManyToOne
	@JoinColumn(name="fin_pagrec_versao_id", nullable=false)
	private FinPagrecVersao finPagrecVersao;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="ger_pessoa_id", nullable=false)
	private GerPessoa gerPessoa;

	//bi-directional many-to-one association to SysProcessLog
	@ManyToOne
	@JoinColumn(name="process_id")
	private SysProcessLog sysProcessLog;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FinPagrecPrevDest
	@OneToMany(mappedBy="finPagrecPrev")
	private List<FinPagrecPrevDest> finPagrecPrevDests;

	//bi-directional many-to-one association to FinPagrecPrevVar
	@OneToMany(mappedBy="finPagrecPrev")
	private List<FinPagrecPrevVar> finPagrecPrevVars;

	public FinPagrecPrev() {
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

	public Date getDataValid() {
		return this.dataValid;
	}

	public void setDataValid(Date dataValid) {
		this.dataValid = dataValid;
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

	public String getTipoEs() {
		return this.tipoEs;
	}

	public void setTipoEs(String tipoEs) {
		this.tipoEs = tipoEs;
	}

	public BigDecimal getValor01() {
		return this.valor01;
	}

	public void setValor01(BigDecimal valor01) {
		this.valor01 = valor01;
	}

	public BigDecimal getValor02() {
		return this.valor02;
	}

	public void setValor02(BigDecimal valor02) {
		this.valor02 = valor02;
	}

	public BigDecimal getValor03() {
		return this.valor03;
	}

	public void setValor03(BigDecimal valor03) {
		this.valor03 = valor03;
	}

	public BigDecimal getValor04() {
		return this.valor04;
	}

	public void setValor04(BigDecimal valor04) {
		this.valor04 = valor04;
	}

	public BigDecimal getValor05() {
		return this.valor05;
	}

	public void setValor05(BigDecimal valor05) {
		this.valor05 = valor05;
	}

	public BigDecimal getValor06() {
		return this.valor06;
	}

	public void setValor06(BigDecimal valor06) {
		this.valor06 = valor06;
	}

	public BigDecimal getValor07() {
		return this.valor07;
	}

	public void setValor07(BigDecimal valor07) {
		this.valor07 = valor07;
	}

	public BigDecimal getValor08() {
		return this.valor08;
	}

	public void setValor08(BigDecimal valor08) {
		this.valor08 = valor08;
	}

	public BigDecimal getValor09() {
		return this.valor09;
	}

	public void setValor09(BigDecimal valor09) {
		this.valor09 = valor09;
	}

	public BigDecimal getValor10() {
		return this.valor10;
	}

	public void setValor10(BigDecimal valor10) {
		this.valor10 = valor10;
	}

	public BigDecimal getValor11() {
		return this.valor11;
	}

	public void setValor11(BigDecimal valor11) {
		this.valor11 = valor11;
	}

	public BigDecimal getValor12() {
		return this.valor12;
	}

	public void setValor12(BigDecimal valor12) {
		this.valor12 = valor12;
	}

	public BigDecimal getValor13() {
		return this.valor13;
	}

	public void setValor13(BigDecimal valor13) {
		this.valor13 = valor13;
	}

	public BigDecimal getValor14() {
		return this.valor14;
	}

	public void setValor14(BigDecimal valor14) {
		this.valor14 = valor14;
	}

	public BigDecimal getValor15() {
		return this.valor15;
	}

	public void setValor15(BigDecimal valor15) {
		this.valor15 = valor15;
	}

	public BigDecimal getValor16() {
		return this.valor16;
	}

	public void setValor16(BigDecimal valor16) {
		this.valor16 = valor16;
	}

	public BigDecimal getValor17() {
		return this.valor17;
	}

	public void setValor17(BigDecimal valor17) {
		this.valor17 = valor17;
	}

	public BigDecimal getValor18() {
		return this.valor18;
	}

	public void setValor18(BigDecimal valor18) {
		this.valor18 = valor18;
	}

	public BigDecimal getValor19() {
		return this.valor19;
	}

	public void setValor19(BigDecimal valor19) {
		this.valor19 = valor19;
	}

	public BigDecimal getValor20() {
		return this.valor20;
	}

	public void setValor20(BigDecimal valor20) {
		this.valor20 = valor20;
	}

	public BigDecimal getValor21() {
		return this.valor21;
	}

	public void setValor21(BigDecimal valor21) {
		this.valor21 = valor21;
	}

	public BigDecimal getValor22() {
		return this.valor22;
	}

	public void setValor22(BigDecimal valor22) {
		this.valor22 = valor22;
	}

	public BigDecimal getValor23() {
		return this.valor23;
	}

	public void setValor23(BigDecimal valor23) {
		this.valor23 = valor23;
	}

	public BigDecimal getValor24() {
		return this.valor24;
	}

	public void setValor24(BigDecimal valor24) {
		this.valor24 = valor24;
	}

	public BigDecimal getValor25() {
		return this.valor25;
	}

	public void setValor25(BigDecimal valor25) {
		this.valor25 = valor25;
	}

	public BigDecimal getValor26() {
		return this.valor26;
	}

	public void setValor26(BigDecimal valor26) {
		this.valor26 = valor26;
	}

	public BigDecimal getValor27() {
		return this.valor27;
	}

	public void setValor27(BigDecimal valor27) {
		this.valor27 = valor27;
	}

	public BigDecimal getValor28() {
		return this.valor28;
	}

	public void setValor28(BigDecimal valor28) {
		this.valor28 = valor28;
	}

	public BigDecimal getValor29() {
		return this.valor29;
	}

	public void setValor29(BigDecimal valor29) {
		this.valor29 = valor29;
	}

	public BigDecimal getValor30() {
		return this.valor30;
	}

	public void setValor30(BigDecimal valor30) {
		this.valor30 = valor30;
	}

	public BigDecimal getValor31() {
		return this.valor31;
	}

	public void setValor31(BigDecimal valor31) {
		this.valor31 = valor31;
	}

	public FinClass getFinClass() {
		return this.finClass;
	}

	public void setFinClass(FinClass finClass) {
		this.finClass = finClass;
	}

	public FinPagrecVersao getFinPagrecVersao() {
		return this.finPagrecVersao;
	}

	public void setFinPagrecVersao(FinPagrecVersao finPagrecVersao) {
		this.finPagrecVersao = finPagrecVersao;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public GerPessoa getGerPessoa() {
		return this.gerPessoa;
	}

	public void setGerPessoa(GerPessoa gerPessoa) {
		this.gerPessoa = gerPessoa;
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

	public List<FinPagrecPrevDest> getFinPagrecPrevDests() {
		return this.finPagrecPrevDests;
	}

	public void setFinPagrecPrevDests(List<FinPagrecPrevDest> finPagrecPrevDests) {
		this.finPagrecPrevDests = finPagrecPrevDests;
	}

	public FinPagrecPrevDest addFinPagrecPrevDest(FinPagrecPrevDest finPagrecPrevDest) {
		getFinPagrecPrevDests().add(finPagrecPrevDest);
		finPagrecPrevDest.setFinPagrecPrev(this);

		return finPagrecPrevDest;
	}

	public FinPagrecPrevDest removeFinPagrecPrevDest(FinPagrecPrevDest finPagrecPrevDest) {
		getFinPagrecPrevDests().remove(finPagrecPrevDest);
		finPagrecPrevDest.setFinPagrecPrev(null);

		return finPagrecPrevDest;
	}

	public List<FinPagrecPrevVar> getFinPagrecPrevVars() {
		return this.finPagrecPrevVars;
	}

	public void setFinPagrecPrevVars(List<FinPagrecPrevVar> finPagrecPrevVars) {
		this.finPagrecPrevVars = finPagrecPrevVars;
	}

	public FinPagrecPrevVar addFinPagrecPrevVar(FinPagrecPrevVar finPagrecPrevVar) {
		getFinPagrecPrevVars().add(finPagrecPrevVar);
		finPagrecPrevVar.setFinPagrecPrev(this);

		return finPagrecPrevVar;
	}

	public FinPagrecPrevVar removeFinPagrecPrevVar(FinPagrecPrevVar finPagrecPrevVar) {
		getFinPagrecPrevVars().remove(finPagrecPrevVar);
		finPagrecPrevVar.setFinPagrecPrev(null);

		return finPagrecPrevVar;
	}

}