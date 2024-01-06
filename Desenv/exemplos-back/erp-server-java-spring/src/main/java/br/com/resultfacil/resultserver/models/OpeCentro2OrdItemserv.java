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
@Table(name="ope_centro2_ord_itemserv")
@NamedQuery(name="OpeCentro2OrdItemserv.findAll", query="SELECT o FROM OpeCentro2OrdItemserv o")
public class OpeCentro2OrdItemserv implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

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

	@Column(name="observacao_externa", length=250)
	private String observacaoExterna;

	@Column(name="observacao_interna", length=250)
	private String observacaoInterna;

	@Column(name="perc_util", nullable=false, precision=18, scale=6)
	private BigDecimal percUtil;

	@Column(name="qnt_rend", nullable=false, precision=18, scale=6)
	private BigDecimal qntRend;

	@Column(name="qnt_total_util", nullable=false, precision=18, scale=6)
	private BigDecimal qntTotalUtil;

	@Column(name="valor_total_util", nullable=false, precision=18, scale=6)
	private BigDecimal valorTotalUtil;

	@Column(name="valor_unit_util", nullable=false, precision=18, scale=6)
	private BigDecimal valorUnitUtil;

	//bi-directional many-to-one association to CtbComp
	@ManyToOne
	@JoinColumn(name="ctb_comp_id", nullable=false)
	private CtbComp ctbComp;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id")
	private GerItemserv gerItemserv;

	//bi-directional many-to-one association to OpeCentro2OrdAtiv
	@ManyToOne
	@JoinColumn(name="ope_centro2_ord_ativ_id", nullable=false)
	private OpeCentro2OrdAtiv opeCentro2OrdAtiv;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentro2OrdItemserv() {
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

	public String getObservacaoExterna() {
		return this.observacaoExterna;
	}

	public void setObservacaoExterna(String observacaoExterna) {
		this.observacaoExterna = observacaoExterna;
	}

	public String getObservacaoInterna() {
		return this.observacaoInterna;
	}

	public void setObservacaoInterna(String observacaoInterna) {
		this.observacaoInterna = observacaoInterna;
	}

	public BigDecimal getPercUtil() {
		return this.percUtil;
	}

	public void setPercUtil(BigDecimal percUtil) {
		this.percUtil = percUtil;
	}

	public BigDecimal getQntRend() {
		return this.qntRend;
	}

	public void setQntRend(BigDecimal qntRend) {
		this.qntRend = qntRend;
	}

	public BigDecimal getQntTotalUtil() {
		return this.qntTotalUtil;
	}

	public void setQntTotalUtil(BigDecimal qntTotalUtil) {
		this.qntTotalUtil = qntTotalUtil;
	}

	public BigDecimal getValorTotalUtil() {
		return this.valorTotalUtil;
	}

	public void setValorTotalUtil(BigDecimal valorTotalUtil) {
		this.valorTotalUtil = valorTotalUtil;
	}

	public BigDecimal getValorUnitUtil() {
		return this.valorUnitUtil;
	}

	public void setValorUnitUtil(BigDecimal valorUnitUtil) {
		this.valorUnitUtil = valorUnitUtil;
	}

	public CtbComp getCtbComp() {
		return this.ctbComp;
	}

	public void setCtbComp(CtbComp ctbComp) {
		this.ctbComp = ctbComp;
	}

	public GerItemserv getGerItemserv() {
		return this.gerItemserv;
	}

	public void setGerItemserv(GerItemserv gerItemserv) {
		this.gerItemserv = gerItemserv;
	}

	public OpeCentro2OrdAtiv getOpeCentro2OrdAtiv() {
		return this.opeCentro2OrdAtiv;
	}

	public void setOpeCentro2OrdAtiv(OpeCentro2OrdAtiv opeCentro2OrdAtiv) {
		this.opeCentro2OrdAtiv = opeCentro2OrdAtiv;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}