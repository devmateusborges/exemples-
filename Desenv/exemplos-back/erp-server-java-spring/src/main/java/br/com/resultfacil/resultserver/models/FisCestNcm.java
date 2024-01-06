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
@Table(name="fis_cest_ncm")
@NamedQuery(name="FisCestNcm.findAll", query="SELECT f FROM FisCestNcm f")
public class FisCestNcm implements Serializable {
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

	//bi-directional many-to-one association to FisCest
	@ManyToOne
	@JoinColumn(name="fis_cest_id", nullable=false)
	private FisCest fisCest;

	//bi-directional many-to-one association to FisNcm
	@ManyToOne
	@JoinColumn(name="fis_ncm_id", nullable=false)
	private FisNcm fisNcm;

	public FisCestNcm() {
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

	public FisCest getFisCest() {
		return this.fisCest;
	}

	public void setFisCest(FisCest fisCest) {
		this.fisCest = fisCest;
	}

	public FisNcm getFisNcm() {
		return this.fisNcm;
	}

	public void setFisNcm(FisNcm fisNcm) {
		this.fisNcm = fisNcm;
	}

}