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
@Table(name="ope_centro2_ord_dest")
@NamedQuery(name="OpeCentro2OrdDest.findAll", query="SELECT o FROM OpeCentro2OrdDest o")
public class OpeCentro2OrdDest implements Serializable {
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

	@Column(name="qnt_obj", precision=18, scale=6)
	private BigDecimal qntObj;

	@Column(name="qnt_prev_obj", precision=18, scale=6)
	private BigDecimal qntPrevObj;

	@Column(name="valor_total", precision=18, scale=6)
	private BigDecimal valorTotal;

	@Column(name="valor_total_prev", precision=18, scale=6)
	private BigDecimal valorTotalPrev;

	@Column(name="valor_unit", precision=18, scale=6)
	private BigDecimal valorUnit;

	@Column(name="valor_unit_prev", precision=18, scale=6)
	private BigDecimal valorUnitPrev;

	//bi-directional many-to-one association to GerUmedida
	@ManyToOne
	@JoinColumn(name="ger_umedida_id_dest")
	private GerUmedida gerUmedida;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id_dest")
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeCentro2Ord
	@ManyToOne
	@JoinColumn(name="ope_centro2_ord_id")
	private OpeCentro2Ord opeCentro2Ord;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentro2OrdDest() {
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

	public BigDecimal getQntObj() {
		return this.qntObj;
	}

	public void setQntObj(BigDecimal qntObj) {
		this.qntObj = qntObj;
	}

	public BigDecimal getQntPrevObj() {
		return this.qntPrevObj;
	}

	public void setQntPrevObj(BigDecimal qntPrevObj) {
		this.qntPrevObj = qntPrevObj;
	}

	public BigDecimal getValorTotal() {
		return this.valorTotal;
	}

	public void setValorTotal(BigDecimal valorTotal) {
		this.valorTotal = valorTotal;
	}

	public BigDecimal getValorTotalPrev() {
		return this.valorTotalPrev;
	}

	public void setValorTotalPrev(BigDecimal valorTotalPrev) {
		this.valorTotalPrev = valorTotalPrev;
	}

	public BigDecimal getValorUnit() {
		return this.valorUnit;
	}

	public void setValorUnit(BigDecimal valorUnit) {
		this.valorUnit = valorUnit;
	}

	public BigDecimal getValorUnitPrev() {
		return this.valorUnitPrev;
	}

	public void setValorUnitPrev(BigDecimal valorUnitPrev) {
		this.valorUnitPrev = valorUnitPrev;
	}

	public GerUmedida getGerUmedida() {
		return this.gerUmedida;
	}

	public void setGerUmedida(GerUmedida gerUmedida) {
		this.gerUmedida = gerUmedida;
	}

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
	}

	public OpeCentro2Ord getOpeCentro2Ord() {
		return this.opeCentro2Ord;
	}

	public void setOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		this.opeCentro2Ord = opeCentro2Ord;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}