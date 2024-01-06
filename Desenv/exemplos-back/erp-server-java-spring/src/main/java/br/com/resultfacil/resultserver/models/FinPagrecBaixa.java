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
@Table(name="fin_pagrec_baixa")
@NamedQuery(name="FinPagrecBaixa.findAll", query="SELECT f FROM FinPagrecBaixa f")
public class FinPagrecBaixa implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_baixa")
	private Date dataBaixa;

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

	@Column(nullable=false, length=1)
	private String tipo;

	@Column(name="valor_pagrec", nullable=false, precision=18, scale=2)
	private BigDecimal valorPagrec;

	//bi-directional many-to-one association to FinConta
	@ManyToOne
	@JoinColumn(name="fin_conta_id", nullable=false)
	private FinConta finConta;

	//bi-directional many-to-one association to FinDocTipo
	@ManyToOne
	@JoinColumn(name="fin_doc_tipo_id", nullable=false)
	private FinDocTipo finDocTipo;

	//bi-directional many-to-one association to FinLote
	@ManyToOne
	@JoinColumn(name="fin_lote_id", nullable=false)
	private FinLote finLote;

	//bi-directional many-to-one association to FinPagrecParc
	@ManyToOne
	@JoinColumn(name="fin_pagrec_parc_id", nullable=false)
	private FinPagrecParc finPagrecParc;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FinPagrecBaixaVar
	@OneToMany(mappedBy="finPagrecBaixa")
	private List<FinPagrecBaixaVar> finPagrecBaixaVars;

	//bi-directional many-to-one association to FinPagrecOrigem
	@OneToMany(mappedBy="finPagrecBaixa")
	private List<FinPagrecOrigem> finPagrecOrigems;

	public FinPagrecBaixa() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataBaixa() {
		return this.dataBaixa;
	}

	public void setDataBaixa(Date dataBaixa) {
		this.dataBaixa = dataBaixa;
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

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public BigDecimal getValorPagrec() {
		return this.valorPagrec;
	}

	public void setValorPagrec(BigDecimal valorPagrec) {
		this.valorPagrec = valorPagrec;
	}

	public FinConta getFinConta() {
		return this.finConta;
	}

	public void setFinConta(FinConta finConta) {
		this.finConta = finConta;
	}

	public FinDocTipo getFinDocTipo() {
		return this.finDocTipo;
	}

	public void setFinDocTipo(FinDocTipo finDocTipo) {
		this.finDocTipo = finDocTipo;
	}

	public FinLote getFinLote() {
		return this.finLote;
	}

	public void setFinLote(FinLote finLote) {
		this.finLote = finLote;
	}

	public FinPagrecParc getFinPagrecParc() {
		return this.finPagrecParc;
	}

	public void setFinPagrecParc(FinPagrecParc finPagrecParc) {
		this.finPagrecParc = finPagrecParc;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<FinPagrecBaixaVar> getFinPagrecBaixaVars() {
		return this.finPagrecBaixaVars;
	}

	public void setFinPagrecBaixaVars(List<FinPagrecBaixaVar> finPagrecBaixaVars) {
		this.finPagrecBaixaVars = finPagrecBaixaVars;
	}

	public FinPagrecBaixaVar addFinPagrecBaixaVar(FinPagrecBaixaVar finPagrecBaixaVar) {
		getFinPagrecBaixaVars().add(finPagrecBaixaVar);
		finPagrecBaixaVar.setFinPagrecBaixa(this);

		return finPagrecBaixaVar;
	}

	public FinPagrecBaixaVar removeFinPagrecBaixaVar(FinPagrecBaixaVar finPagrecBaixaVar) {
		getFinPagrecBaixaVars().remove(finPagrecBaixaVar);
		finPagrecBaixaVar.setFinPagrecBaixa(null);

		return finPagrecBaixaVar;
	}

	public List<FinPagrecOrigem> getFinPagrecOrigems() {
		return this.finPagrecOrigems;
	}

	public void setFinPagrecOrigems(List<FinPagrecOrigem> finPagrecOrigems) {
		this.finPagrecOrigems = finPagrecOrigems;
	}

	public FinPagrecOrigem addFinPagrecOrigem(FinPagrecOrigem finPagrecOrigem) {
		getFinPagrecOrigems().add(finPagrecOrigem);
		finPagrecOrigem.setFinPagrecBaixa(this);

		return finPagrecOrigem;
	}

	public FinPagrecOrigem removeFinPagrecOrigem(FinPagrecOrigem finPagrecOrigem) {
		getFinPagrecOrigems().remove(finPagrecOrigem);
		finPagrecOrigem.setFinPagrecBaixa(null);

		return finPagrecOrigem;
	}

}