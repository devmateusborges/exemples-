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
@Table(name="fin_pagrec_banco_extrato")
@NamedQuery(name="FinPagrecBancoExtrato.findAll", query="SELECT f FROM FinPagrecBancoExtrato f")
public class FinPagrecBancoExtrato implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_extrato", nullable=false)
	private Date dataExtrato;

	@Column(length=250)
	private String descricao;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="numero_doc", nullable=false, length=50)
	private String numeroDoc;

	@Column(nullable=false, length=2)
	private String status;

	@Column(name="status_observacao", length=250)
	private String statusObservacao;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor;

	//bi-directional many-to-one association to FinConta
	@ManyToOne
	@JoinColumn(name="fin_conta_id", nullable=false)
	private FinConta finConta;

	//bi-directional many-to-one association to SysProcessLog
	@ManyToOne
	@JoinColumn(name="process_id")
	private SysProcessLog sysProcessLog;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FinPagrecOrigem
	@OneToMany(mappedBy="finPagrecBancoExtrato")
	private List<FinPagrecOrigem> finPagrecOrigems;

	public FinPagrecBancoExtrato() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataExtrato() {
		return this.dataExtrato;
	}

	public void setDataExtrato(Date dataExtrato) {
		this.dataExtrato = dataExtrato;
	}

	public String getDescricao() {
		return this.descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
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

	public String getNumeroDoc() {
		return this.numeroDoc;
	}

	public void setNumeroDoc(String numeroDoc) {
		this.numeroDoc = numeroDoc;
	}

	public String getStatus() {
		return this.status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public String getStatusObservacao() {
		return this.statusObservacao;
	}

	public void setStatusObservacao(String statusObservacao) {
		this.statusObservacao = statusObservacao;
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

	public List<FinPagrecOrigem> getFinPagrecOrigems() {
		return this.finPagrecOrigems;
	}

	public void setFinPagrecOrigems(List<FinPagrecOrigem> finPagrecOrigems) {
		this.finPagrecOrigems = finPagrecOrigems;
	}

	public FinPagrecOrigem addFinPagrecOrigem(FinPagrecOrigem finPagrecOrigem) {
		getFinPagrecOrigems().add(finPagrecOrigem);
		finPagrecOrigem.setFinPagrecBancoExtrato(this);

		return finPagrecOrigem;
	}

	public FinPagrecOrigem removeFinPagrecOrigem(FinPagrecOrigem finPagrecOrigem) {
		getFinPagrecOrigems().remove(finPagrecOrigem);
		finPagrecOrigem.setFinPagrecBancoExtrato(null);

		return finPagrecOrigem;
	}

}