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
@Table(name="ope_ocor_compart_mov_det")
@NamedQuery(name="OpeOcorCompartMovDet.findAll", query="SELECT o FROM OpeOcorCompartMovDet o")
public class OpeOcorCompartMovDet implements Serializable {
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

	@Column(name="qnt_medicao", nullable=false, precision=18, scale=6)
	private BigDecimal qntMedicao;

	//bi-directional many-to-one association to OpeCompart
	@ManyToOne
	@JoinColumn(name="ope_compart_id", nullable=false)
	private OpeCompart opeCompart;

	//bi-directional many-to-one association to OpeCompartOcor
	@ManyToOne
	@JoinColumn(name="ope_compart_ocor_id", nullable=false)
	private OpeCompartOcor opeCompartOcor;

	//bi-directional many-to-one association to OpeOcorCompartMov
	@ManyToOne
	@JoinColumn(name="ope_compart_mov_id", nullable=false)
	private OpeOcorCompartMov opeOcorCompartMov;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeOcorCompartMovDet() {
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

	public BigDecimal getQntMedicao() {
		return this.qntMedicao;
	}

	public void setQntMedicao(BigDecimal qntMedicao) {
		this.qntMedicao = qntMedicao;
	}

	public OpeCompart getOpeCompart() {
		return this.opeCompart;
	}

	public void setOpeCompart(OpeCompart opeCompart) {
		this.opeCompart = opeCompart;
	}

	public OpeCompartOcor getOpeCompartOcor() {
		return this.opeCompartOcor;
	}

	public void setOpeCompartOcor(OpeCompartOcor opeCompartOcor) {
		this.opeCompartOcor = opeCompartOcor;
	}

	public OpeOcorCompartMov getOpeOcorCompartMov() {
		return this.opeOcorCompartMov;
	}

	public void setOpeOcorCompartMov(OpeOcorCompartMov opeOcorCompartMov) {
		this.opeOcorCompartMov = opeOcorCompartMov;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}