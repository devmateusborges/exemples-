package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="mov_est_nivel")
@NamedQuery(name="MovEstNivel.findAll", query="SELECT m FROM MovEstNivel m")
public class MovEstNivel implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(length=250)
	private String observacao;

	@Column(name="qnt_max", nullable=false, precision=18, scale=6)
	private BigDecimal qntMax;

	@Column(name="qnt_min", nullable=false, precision=18, scale=6)
	private BigDecimal qntMin;

	@Column(name="qnt_nesc", nullable=false, precision=18, scale=6)
	private BigDecimal qntNesc;

	//bi-directional many-to-one association to GerEstNivel
	@ManyToOne
	@JoinColumn(name="ger_est_nivel_id", nullable=false)
	private GerEstNivel gerEstNivel;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id", nullable=false)
	private GerItemserv gerItemserv;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public MovEstNivel() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
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

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public BigDecimal getQntMax() {
		return this.qntMax;
	}

	public void setQntMax(BigDecimal qntMax) {
		this.qntMax = qntMax;
	}

	public BigDecimal getQntMin() {
		return this.qntMin;
	}

	public void setQntMin(BigDecimal qntMin) {
		this.qntMin = qntMin;
	}

	public BigDecimal getQntNesc() {
		return this.qntNesc;
	}

	public void setQntNesc(BigDecimal qntNesc) {
		this.qntNesc = qntNesc;
	}

	public GerEstNivel getGerEstNivel() {
		return this.gerEstNivel;
	}

	public void setGerEstNivel(GerEstNivel gerEstNivel) {
		this.gerEstNivel = gerEstNivel;
	}

	public GerItemserv getGerItemserv() {
		return this.gerItemserv;
	}

	public void setGerItemserv(GerItemserv gerItemserv) {
		this.gerItemserv = gerItemserv;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}