package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_ocor_mov_dest")
@NamedQuery(name="OpeOcorMovDest.findAll", query="SELECT o FROM OpeOcorMovDest o")
public class OpeOcorMovDest implements Serializable {
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

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id", nullable=false)
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeCompart
	@ManyToOne
	@JoinColumn(name="ope_compart_id")
	private OpeCompart opeCompart;

	//bi-directional many-to-one association to OpeOcorMov
	@ManyToOne
	@JoinColumn(name="ope_ocor_mov_id", nullable=false)
	private OpeOcorMov opeOcorMov;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeOcorMovDet
	@OneToMany(mappedBy="opeOcorMovDest")
	private List<OpeOcorMovDet> opeOcorMovDets;

	public OpeOcorMovDest() {
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

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
	}

	public OpeCompart getOpeCompart() {
		return this.opeCompart;
	}

	public void setOpeCompart(OpeCompart opeCompart) {
		this.opeCompart = opeCompart;
	}

	public OpeOcorMov getOpeOcorMov() {
		return this.opeOcorMov;
	}

	public void setOpeOcorMov(OpeOcorMov opeOcorMov) {
		this.opeOcorMov = opeOcorMov;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeOcorMovDet> getOpeOcorMovDets() {
		return this.opeOcorMovDets;
	}

	public void setOpeOcorMovDets(List<OpeOcorMovDet> opeOcorMovDets) {
		this.opeOcorMovDets = opeOcorMovDets;
	}

	public OpeOcorMovDet addOpeOcorMovDet(OpeOcorMovDet opeOcorMovDet) {
		getOpeOcorMovDets().add(opeOcorMovDet);
		opeOcorMovDet.setOpeOcorMovDest(this);

		return opeOcorMovDet;
	}

	public OpeOcorMovDet removeOpeOcorMovDet(OpeOcorMovDet opeOcorMovDet) {
		getOpeOcorMovDets().remove(opeOcorMovDet);
		opeOcorMovDet.setOpeOcorMovDest(null);

		return opeOcorMovDet;
	}

}