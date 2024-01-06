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
@Table(name="fin_pagrec")
@NamedQuery(name="FinPagrec.findAll", query="SELECT f FROM FinPagrec f")
public class FinPagrec implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_mov", nullable=false)
	private Date dataMov;

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

	@Column(name="numero_doc_pagrec", nullable=false, length=50)
	private String numeroDocPagrec;

	@Column(name="numero_parc_total", nullable=false)
	private Integer numeroParcTotal;

	@Column(length=250)
	private String observacao;

	@Column(name="tipo_es", nullable=false, length=1)
	private String tipoEs;

	@Column(name="valor_pagrec", nullable=false, precision=18, scale=2)
	private BigDecimal valorPagrec;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="fin_cond_pagrec_id", nullable=false)
	private FinCondPagrec finCondPagrec;

	//bi-directional many-to-one association to FinDocTipo
	@ManyToOne
	@JoinColumn(name="fin_doc_tipo_id")
	private FinDocTipo finDocTipo;

	//bi-directional many-to-one association to FinPagrecTipo
	@ManyToOne
	@JoinColumn(name="fin_pagrec_tipo_id", nullable=false)
	private FinPagrecTipo finPagrecTipo;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="ger_pessoa_id", nullable=false)
	private GerPessoa gerPessoa1;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="ger_pessoa_id_pagrec", nullable=false)
	private GerPessoa gerPessoa2;

	//bi-directional many-to-one association to OpeCentroRatTipo
	@ManyToOne
	@JoinColumn(name="ope_centro_rat_tipo_id")
	private OpeCentroRatTipo opeCentroRatTipo;

	//bi-directional many-to-one association to SysProcessLog
	@ManyToOne
	@JoinColumn(name="process_id")
	private SysProcessLog sysProcessLog;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FinPagrecClass
	@OneToMany(mappedBy="finPagrec")
	private List<FinPagrecClass> finPagrecClasses;

	//bi-directional many-to-one association to FinPagrecOrigem
	@OneToMany(mappedBy="finPagrec1")
	private List<FinPagrecOrigem> finPagrecOrigems1;

	//bi-directional many-to-one association to FinPagrecOrigem
	@OneToMany(mappedBy="finPagrec2")
	private List<FinPagrecOrigem> finPagrecOrigems2;

	//bi-directional many-to-one association to FinPagrecParc
	@OneToMany(mappedBy="finPagrec")
	private List<FinPagrecParc> finPagrecParcs;

	//bi-directional many-to-one association to FisTributacao
	@OneToMany(mappedBy="finPagrec")
	private List<FisTributacao> fisTributacaos;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="finPagrec")
	private List<OpeCentroDest> opeCentroDests;

	//bi-directional many-to-one association to SysDocument
	@OneToMany(mappedBy="finPagrec")
	private List<SysDocument> sysDocuments;

	public FinPagrec() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataMov() {
		return this.dataMov;
	}

	public void setDataMov(Date dataMov) {
		this.dataMov = dataMov;
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

	public String getNumeroDocPagrec() {
		return this.numeroDocPagrec;
	}

	public void setNumeroDocPagrec(String numeroDocPagrec) {
		this.numeroDocPagrec = numeroDocPagrec;
	}

	public Integer getNumeroParcTotal() {
		return this.numeroParcTotal;
	}

	public void setNumeroParcTotal(Integer numeroParcTotal) {
		this.numeroParcTotal = numeroParcTotal;
	}

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public String getTipoEs() {
		return this.tipoEs;
	}

	public void setTipoEs(String tipoEs) {
		this.tipoEs = tipoEs;
	}

	public BigDecimal getValorPagrec() {
		return this.valorPagrec;
	}

	public void setValorPagrec(BigDecimal valorPagrec) {
		this.valorPagrec = valorPagrec;
	}

	public FinCondPagrec getFinCondPagrec() {
		return this.finCondPagrec;
	}

	public void setFinCondPagrec(FinCondPagrec finCondPagrec) {
		this.finCondPagrec = finCondPagrec;
	}

	public FinDocTipo getFinDocTipo() {
		return this.finDocTipo;
	}

	public void setFinDocTipo(FinDocTipo finDocTipo) {
		this.finDocTipo = finDocTipo;
	}

	public FinPagrecTipo getFinPagrecTipo() {
		return this.finPagrecTipo;
	}

	public void setFinPagrecTipo(FinPagrecTipo finPagrecTipo) {
		this.finPagrecTipo = finPagrecTipo;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public GerPessoa getGerPessoa1() {
		return this.gerPessoa1;
	}

	public void setGerPessoa1(GerPessoa gerPessoa1) {
		this.gerPessoa1 = gerPessoa1;
	}

	public GerPessoa getGerPessoa2() {
		return this.gerPessoa2;
	}

	public void setGerPessoa2(GerPessoa gerPessoa2) {
		this.gerPessoa2 = gerPessoa2;
	}

	public OpeCentroRatTipo getOpeCentroRatTipo() {
		return this.opeCentroRatTipo;
	}

	public void setOpeCentroRatTipo(OpeCentroRatTipo opeCentroRatTipo) {
		this.opeCentroRatTipo = opeCentroRatTipo;
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

	public List<FinPagrecClass> getFinPagrecClasses() {
		return this.finPagrecClasses;
	}

	public void setFinPagrecClasses(List<FinPagrecClass> finPagrecClasses) {
		this.finPagrecClasses = finPagrecClasses;
	}

	public FinPagrecClass addFinPagrecClass(FinPagrecClass finPagrecClass) {
		getFinPagrecClasses().add(finPagrecClass);
		finPagrecClass.setFinPagrec(this);

		return finPagrecClass;
	}

	public FinPagrecClass removeFinPagrecClass(FinPagrecClass finPagrecClass) {
		getFinPagrecClasses().remove(finPagrecClass);
		finPagrecClass.setFinPagrec(null);

		return finPagrecClass;
	}

	public List<FinPagrecOrigem> getFinPagrecOrigems1() {
		return this.finPagrecOrigems1;
	}

	public void setFinPagrecOrigems1(List<FinPagrecOrigem> finPagrecOrigems1) {
		this.finPagrecOrigems1 = finPagrecOrigems1;
	}

	public FinPagrecOrigem addFinPagrecOrigems1(FinPagrecOrigem finPagrecOrigems1) {
		getFinPagrecOrigems1().add(finPagrecOrigems1);
		finPagrecOrigems1.setFinPagrec1(this);

		return finPagrecOrigems1;
	}

	public FinPagrecOrigem removeFinPagrecOrigems1(FinPagrecOrigem finPagrecOrigems1) {
		getFinPagrecOrigems1().remove(finPagrecOrigems1);
		finPagrecOrigems1.setFinPagrec1(null);

		return finPagrecOrigems1;
	}

	public List<FinPagrecOrigem> getFinPagrecOrigems2() {
		return this.finPagrecOrigems2;
	}

	public void setFinPagrecOrigems2(List<FinPagrecOrigem> finPagrecOrigems2) {
		this.finPagrecOrigems2 = finPagrecOrigems2;
	}

	public FinPagrecOrigem addFinPagrecOrigems2(FinPagrecOrigem finPagrecOrigems2) {
		getFinPagrecOrigems2().add(finPagrecOrigems2);
		finPagrecOrigems2.setFinPagrec2(this);

		return finPagrecOrigems2;
	}

	public FinPagrecOrigem removeFinPagrecOrigems2(FinPagrecOrigem finPagrecOrigems2) {
		getFinPagrecOrigems2().remove(finPagrecOrigems2);
		finPagrecOrigems2.setFinPagrec2(null);

		return finPagrecOrigems2;
	}

	public List<FinPagrecParc> getFinPagrecParcs() {
		return this.finPagrecParcs;
	}

	public void setFinPagrecParcs(List<FinPagrecParc> finPagrecParcs) {
		this.finPagrecParcs = finPagrecParcs;
	}

	public FinPagrecParc addFinPagrecParc(FinPagrecParc finPagrecParc) {
		getFinPagrecParcs().add(finPagrecParc);
		finPagrecParc.setFinPagrec(this);

		return finPagrecParc;
	}

	public FinPagrecParc removeFinPagrecParc(FinPagrecParc finPagrecParc) {
		getFinPagrecParcs().remove(finPagrecParc);
		finPagrecParc.setFinPagrec(null);

		return finPagrecParc;
	}

	public List<FisTributacao> getFisTributacaos() {
		return this.fisTributacaos;
	}

	public void setFisTributacaos(List<FisTributacao> fisTributacaos) {
		this.fisTributacaos = fisTributacaos;
	}

	public FisTributacao addFisTributacao(FisTributacao fisTributacao) {
		getFisTributacaos().add(fisTributacao);
		fisTributacao.setFinPagrec(this);

		return fisTributacao;
	}

	public FisTributacao removeFisTributacao(FisTributacao fisTributacao) {
		getFisTributacaos().remove(fisTributacao);
		fisTributacao.setFinPagrec(null);

		return fisTributacao;
	}

	public List<OpeCentroDest> getOpeCentroDests() {
		return this.opeCentroDests;
	}

	public void setOpeCentroDests(List<OpeCentroDest> opeCentroDests) {
		this.opeCentroDests = opeCentroDests;
	}

	public OpeCentroDest addOpeCentroDest(OpeCentroDest opeCentroDest) {
		getOpeCentroDests().add(opeCentroDest);
		opeCentroDest.setFinPagrec(this);

		return opeCentroDest;
	}

	public OpeCentroDest removeOpeCentroDest(OpeCentroDest opeCentroDest) {
		getOpeCentroDests().remove(opeCentroDest);
		opeCentroDest.setFinPagrec(null);

		return opeCentroDest;
	}

	public List<SysDocument> getSysDocuments() {
		return this.sysDocuments;
	}

	public void setSysDocuments(List<SysDocument> sysDocuments) {
		this.sysDocuments = sysDocuments;
	}

	public SysDocument addSysDocument(SysDocument sysDocument) {
		getSysDocuments().add(sysDocument);
		sysDocument.setFinPagrec(this);

		return sysDocument;
	}

	public SysDocument removeSysDocument(SysDocument sysDocument) {
		getSysDocuments().remove(sysDocument);
		sysDocument.setFinPagrec(null);

		return sysDocument;
	}

}