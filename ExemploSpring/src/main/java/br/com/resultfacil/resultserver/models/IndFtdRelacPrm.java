package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ind_ftd_relac_prm")
@NamedQuery(name="IndFtdRelacPrm.findAll", query="SELECT i FROM IndFtdRelacPrm i")
public class IndFtdRelacPrm implements Serializable {
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

	@ManyToOne
	@JoinColumn(name="ind_ftd_id")
	private IndFtd indFtd;

	@ManyToOne
	@JoinColumn(name="ind_prm_id")
	private IndPrm indPrm;

	public IndFtdRelacPrm() {
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

	public IndFtd getIndFtd() {
		return this.indFtd;
	}

	public void setIndFtd(IndFtd indFtd) {
		this.indFtd = indFtd;
	}

	public IndPrm getIndPrm() {
		return this.indPrm;
	}

	public void setIndPrm(IndPrm indPrm) {
		this.indPrm = indPrm;
	}

}