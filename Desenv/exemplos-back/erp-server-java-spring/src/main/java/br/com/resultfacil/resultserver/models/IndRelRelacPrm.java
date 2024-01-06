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
@Table(name="ind_rel_relac_prm")
@NamedQuery(name="IndRelRelacPrm.findAll", query="SELECT i FROM IndRelRelacPrm i")
public class IndRelRelacPrm implements Serializable {
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

	@Column(name="ordem_exib", nullable=false)
	private Integer ordemExib;

	@Column(name="valor_padrao")
	private String valorPadrao;

	//bi-directional many-to-one association to IndPrm
	@ManyToOne
	@JoinColumn(name="ind_prm_id", nullable=false)
	private IndPrm indPrm;

	//bi-directional many-to-one association to IndRel
	@ManyToOne
	@JoinColumn(name="ind_rel_id", nullable=false)
	private IndRel indRel;

	public IndRelRelacPrm() {
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

	public Integer getOrdemExib() {
		return this.ordemExib;
	}

	public void setOrdemExib(Integer ordemExib) {
		this.ordemExib = ordemExib;
	}

	public Object getValorPadrao() {
		return this.valorPadrao;
	}

	public void setValorPadrao(String valorPadrao) {
		this.valorPadrao = valorPadrao;
	}

	public IndPrm getIndPrm() {
		return this.indPrm;
	}

	public void setIndPrm(IndPrm indPrm) {
		this.indPrm = indPrm;
	}

	public IndRel getIndRel() {
		return this.indRel;
	}

	public void setIndRel(IndRel indRel) {
		this.indRel = indRel;
	}

}