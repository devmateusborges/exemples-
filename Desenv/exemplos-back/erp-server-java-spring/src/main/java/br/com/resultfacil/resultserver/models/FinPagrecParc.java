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
@Table(name="fin_pagrec_parc")
@NamedQuery(name="FinPagrecParc.findAll", query="SELECT f FROM FinPagrecParc f")
public class FinPagrecParc implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_valid")
	private Date dataValid;

	@Temporal(TemporalType.DATE)
	@Column(name="data_venc")
	private Date dataVenc;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="numero_parc", nullable=false)
	private Integer numeroParc;

	@Column(name="valor_desconto", nullable=false, precision=18, scale=2)
	private BigDecimal valorDesconto;

	@Column(name="valor_juro", nullable=false, precision=18, scale=2)
	private BigDecimal valorJuro;

	@Column(name="valor_multa", nullable=false, precision=18, scale=2)
	private BigDecimal valorMulta;

	@Column(name="valor_pagrec", nullable=false, precision=18, scale=2)
	private BigDecimal valorPagrec;

	//bi-directional many-to-one association to FinPagrecBaixa
	@OneToMany(mappedBy="finPagrecParc")
	private List<FinPagrecBaixa> finPagrecBaixas;

	//bi-directional many-to-one association to FinPagrecOrigem
	@OneToMany(mappedBy="finPagrecParc1")
	private List<FinPagrecOrigem> finPagrecOrigems1;

	//bi-directional many-to-one association to FinPagrecOrigem
	@OneToMany(mappedBy="finPagrecParc2")
	private List<FinPagrecOrigem> finPagrecOrigems2;

	//bi-directional many-to-one association to FinDocTipo
	@ManyToOne
	@JoinColumn(name="fin_doc_tipo_id", nullable=false)
	private FinDocTipo finDocTipo;

	//bi-directional many-to-one association to FinPagrec
	@ManyToOne
	@JoinColumn(name="fin_pagrec_id", nullable=false)
	private FinPagrec finPagrec;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FinPagrecParcVar
	@OneToMany(mappedBy="finPagrecParc")
	private List<FinPagrecParcVar> finPagrecParcVars;

	public FinPagrecParc() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataValid() {
		return this.dataValid;
	}

	public void setDataValid(Date dataValid) {
		this.dataValid = dataValid;
	}

	public Date getDataVenc() {
		return this.dataVenc;
	}

	public void setDataVenc(Date dataVenc) {
		this.dataVenc = dataVenc;
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

	public Integer getNumeroParc() {
		return this.numeroParc;
	}

	public void setNumeroParc(Integer numeroParc) {
		this.numeroParc = numeroParc;
	}

	public BigDecimal getValorDesconto() {
		return this.valorDesconto;
	}

	public void setValorDesconto(BigDecimal valorDesconto) {
		this.valorDesconto = valorDesconto;
	}

	public BigDecimal getValorJuro() {
		return this.valorJuro;
	}

	public void setValorJuro(BigDecimal valorJuro) {
		this.valorJuro = valorJuro;
	}

	public BigDecimal getValorMulta() {
		return this.valorMulta;
	}

	public void setValorMulta(BigDecimal valorMulta) {
		this.valorMulta = valorMulta;
	}

	public BigDecimal getValorPagrec() {
		return this.valorPagrec;
	}

	public void setValorPagrec(BigDecimal valorPagrec) {
		this.valorPagrec = valorPagrec;
	}

	public List<FinPagrecBaixa> getFinPagrecBaixas() {
		return this.finPagrecBaixas;
	}

	public void setFinPagrecBaixas(List<FinPagrecBaixa> finPagrecBaixas) {
		this.finPagrecBaixas = finPagrecBaixas;
	}

	public FinPagrecBaixa addFinPagrecBaixa(FinPagrecBaixa finPagrecBaixa) {
		getFinPagrecBaixas().add(finPagrecBaixa);
		finPagrecBaixa.setFinPagrecParc(this);

		return finPagrecBaixa;
	}

	public FinPagrecBaixa removeFinPagrecBaixa(FinPagrecBaixa finPagrecBaixa) {
		getFinPagrecBaixas().remove(finPagrecBaixa);
		finPagrecBaixa.setFinPagrecParc(null);

		return finPagrecBaixa;
	}

	public List<FinPagrecOrigem> getFinPagrecOrigems1() {
		return this.finPagrecOrigems1;
	}

	public void setFinPagrecOrigems1(List<FinPagrecOrigem> finPagrecOrigems1) {
		this.finPagrecOrigems1 = finPagrecOrigems1;
	}

	public FinPagrecOrigem addFinPagrecOrigems1(FinPagrecOrigem finPagrecOrigems1) {
		getFinPagrecOrigems1().add(finPagrecOrigems1);
		finPagrecOrigems1.setFinPagrecParc1(this);

		return finPagrecOrigems1;
	}

	public FinPagrecOrigem removeFinPagrecOrigems1(FinPagrecOrigem finPagrecOrigems1) {
		getFinPagrecOrigems1().remove(finPagrecOrigems1);
		finPagrecOrigems1.setFinPagrecParc1(null);

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
		finPagrecOrigems2.setFinPagrecParc2(this);

		return finPagrecOrigems2;
	}

	public FinPagrecOrigem removeFinPagrecOrigems2(FinPagrecOrigem finPagrecOrigems2) {
		getFinPagrecOrigems2().remove(finPagrecOrigems2);
		finPagrecOrigems2.setFinPagrecParc2(null);

		return finPagrecOrigems2;
	}

	public FinDocTipo getFinDocTipo() {
		return this.finDocTipo;
	}

	public void setFinDocTipo(FinDocTipo finDocTipo) {
		this.finDocTipo = finDocTipo;
	}

	public FinPagrec getFinPagrec() {
		return this.finPagrec;
	}

	public void setFinPagrec(FinPagrec finPagrec) {
		this.finPagrec = finPagrec;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<FinPagrecParcVar> getFinPagrecParcVars() {
		return this.finPagrecParcVars;
	}

	public void setFinPagrecParcVars(List<FinPagrecParcVar> finPagrecParcVars) {
		this.finPagrecParcVars = finPagrecParcVars;
	}

	public FinPagrecParcVar addFinPagrecParcVar(FinPagrecParcVar finPagrecParcVar) {
		getFinPagrecParcVars().add(finPagrecParcVar);
		finPagrecParcVar.setFinPagrecParc(this);

		return finPagrecParcVar;
	}

	public FinPagrecParcVar removeFinPagrecParcVar(FinPagrecParcVar finPagrecParcVar) {
		getFinPagrecParcVars().remove(finPagrecParcVar);
		finPagrecParcVar.setFinPagrecParc(null);

		return finPagrecParcVar;
	}

}