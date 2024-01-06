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
@Table(name="ope_ocor_mov_det")
@NamedQuery(name="OpeOcorMovDet.findAll", query="SELECT o FROM OpeOcorMovDet o")
public class OpeOcorMovDet implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_status", nullable=false)
	private Date dataStatus;

	@Column(name="lat_x", length=50)
	private String latX;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="long_y", length=50)
	private String longY;

	@Column(length=250)
	private String observacao;

	@Column(length=50)
	private String ponto;

	@Column(name="qnt_ocor", nullable=false, precision=18, scale=6)
	private BigDecimal qntOcor;

	@Column(name="qnt_ocor_calc", nullable=false, precision=18, scale=6)
	private BigDecimal qntOcorCalc;

	//bi-directional many-to-one association to OpeOcor
	@ManyToOne
	@JoinColumn(name="ope_ocor_id", nullable=false)
	private OpeOcor opeOcor;

	//bi-directional many-to-one association to OpeOcorMov
	@ManyToOne
	@JoinColumn(name="ope_ocor_mov_id", nullable=false)
	private OpeOcorMov opeOcorMov;

	//bi-directional many-to-one association to OpeOcorMovDest
	@ManyToOne
	@JoinColumn(name="ope_ocor_mov_dest_id")
	private OpeOcorMovDest opeOcorMovDest;

	//bi-directional many-to-one association to OpeOcorStatus
	@ManyToOne
	@JoinColumn(name="ope_ocor_status_id", nullable=false)
	private OpeOcorStatus opeOcorStatus;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeOcorMovDet() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataStatus() {
		return this.dataStatus;
	}

	public void setDataStatus(Date dataStatus) {
		this.dataStatus = dataStatus;
	}

	public String getLatX() {
		return this.latX;
	}

	public void setLatX(String latX) {
		this.latX = latX;
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

	public String getLongY() {
		return this.longY;
	}

	public void setLongY(String longY) {
		this.longY = longY;
	}

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public String getPonto() {
		return this.ponto;
	}

	public void setPonto(String ponto) {
		this.ponto = ponto;
	}

	public BigDecimal getQntOcor() {
		return this.qntOcor;
	}

	public void setQntOcor(BigDecimal qntOcor) {
		this.qntOcor = qntOcor;
	}

	public BigDecimal getQntOcorCalc() {
		return this.qntOcorCalc;
	}

	public void setQntOcorCalc(BigDecimal qntOcorCalc) {
		this.qntOcorCalc = qntOcorCalc;
	}

	public OpeOcor getOpeOcor() {
		return this.opeOcor;
	}

	public void setOpeOcor(OpeOcor opeOcor) {
		this.opeOcor = opeOcor;
	}

	public OpeOcorMov getOpeOcorMov() {
		return this.opeOcorMov;
	}

	public void setOpeOcorMov(OpeOcorMov opeOcorMov) {
		this.opeOcorMov = opeOcorMov;
	}

	public OpeOcorMovDest getOpeOcorMovDest() {
		return this.opeOcorMovDest;
	}

	public void setOpeOcorMovDest(OpeOcorMovDest opeOcorMovDest) {
		this.opeOcorMovDest = opeOcorMovDest;
	}

	public OpeOcorStatus getOpeOcorStatus() {
		return this.opeOcorStatus;
	}

	public void setOpeOcorStatus(OpeOcorStatus opeOcorStatus) {
		this.opeOcorStatus = opeOcorStatus;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}