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
@Table(name="fin_pagrec_banco")
@NamedQuery(name="FinPagrecBanco.findAll", query="SELECT f FROM FinPagrecBanco f")
public class FinPagrecBanco implements Serializable {
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

	@Column(length=250)
	private String observacao;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor;

	//bi-directional many-to-one association to FinConta
	@ManyToOne
	@JoinColumn(name="fin_conta_id", nullable=false)
	private FinConta finConta;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FinPagrecClass
	@OneToMany(mappedBy="finPagrecBanco")
	private List<FinPagrecClass> finPagrecClasses;

	//bi-directional many-to-one association to FinPagrecOrigem
	@OneToMany(mappedBy="finPagrecBanco")
	private List<FinPagrecOrigem> finPagrecOrigems;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="finPagrecBanco")
	private List<OpeCentroDest> opeCentroDests;

	public FinPagrecBanco() {
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

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public BigDecimal getValor() {
		return this.valor;
	}

	public void setValor(BigDecimal valor) {
		this.valor = valor;
	}

	public FinConta getFinConta() {
		return this.finConta;
	}

	public void setFinConta(FinConta finConta) {
		this.finConta = finConta;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
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
		finPagrecClass.setFinPagrecBanco(this);

		return finPagrecClass;
	}

	public FinPagrecClass removeFinPagrecClass(FinPagrecClass finPagrecClass) {
		getFinPagrecClasses().remove(finPagrecClass);
		finPagrecClass.setFinPagrecBanco(null);

		return finPagrecClass;
	}

	public List<FinPagrecOrigem> getFinPagrecOrigems() {
		return this.finPagrecOrigems;
	}

	public void setFinPagrecOrigems(List<FinPagrecOrigem> finPagrecOrigems) {
		this.finPagrecOrigems = finPagrecOrigems;
	}

	public FinPagrecOrigem addFinPagrecOrigem(FinPagrecOrigem finPagrecOrigem) {
		getFinPagrecOrigems().add(finPagrecOrigem);
		finPagrecOrigem.setFinPagrecBanco(this);

		return finPagrecOrigem;
	}

	public FinPagrecOrigem removeFinPagrecOrigem(FinPagrecOrigem finPagrecOrigem) {
		getFinPagrecOrigems().remove(finPagrecOrigem);
		finPagrecOrigem.setFinPagrecBanco(null);

		return finPagrecOrigem;
	}

	public List<OpeCentroDest> getOpeCentroDests() {
		return this.opeCentroDests;
	}

	public void setOpeCentroDests(List<OpeCentroDest> opeCentroDests) {
		this.opeCentroDests = opeCentroDests;
	}

	public OpeCentroDest addOpeCentroDest(OpeCentroDest opeCentroDest) {
		getOpeCentroDests().add(opeCentroDest);
		opeCentroDest.setFinPagrecBanco(this);

		return opeCentroDest;
	}

	public OpeCentroDest removeOpeCentroDest(OpeCentroDest opeCentroDest) {
		getOpeCentroDests().remove(opeCentroDest);
		opeCentroDest.setFinPagrecBanco(null);

		return opeCentroDest;
	}

}