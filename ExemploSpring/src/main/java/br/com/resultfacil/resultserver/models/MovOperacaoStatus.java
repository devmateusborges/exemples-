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
@Table(name="mov_operacao_status")
@NamedQuery(name="MovOperacaoStatus.findAll", query="SELECT m FROM MovOperacaoStatus m")
public class MovOperacaoStatus implements Serializable {
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

	//bi-directional many-to-one association to MovOperacao
	@ManyToOne
	@JoinColumn(name="mov_operacao_id", nullable=false)
	private MovOperacao movOperacao1;

	//bi-directional many-to-one association to MovOperacao
	@ManyToOne
	@JoinColumn(name="mov_operacao_id_prox")
	private MovOperacao movOperacao2;

	//bi-directional many-to-one association to MovStatus
	@ManyToOne
	@JoinColumn(name="mov_status_id", nullable=false)
	private MovStatus movStatus1;

	//bi-directional many-to-one association to MovStatus
	@ManyToOne
	@JoinColumn(name="mov_status_id_prox")
	private MovStatus movStatus2;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public MovOperacaoStatus() {
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

	public MovOperacao getMovOperacao1() {
		return this.movOperacao1;
	}

	public void setMovOperacao1(MovOperacao movOperacao1) {
		this.movOperacao1 = movOperacao1;
	}

	public MovOperacao getMovOperacao2() {
		return this.movOperacao2;
	}

	public void setMovOperacao2(MovOperacao movOperacao2) {
		this.movOperacao2 = movOperacao2;
	}

	public MovStatus getMovStatus1() {
		return this.movStatus1;
	}

	public void setMovStatus1(MovStatus movStatus1) {
		this.movStatus1 = movStatus1;
	}

	public MovStatus getMovStatus2() {
		return this.movStatus2;
	}

	public void setMovStatus2(MovStatus movStatus2) {
		this.movStatus2 = movStatus2;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}