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
@Table(name="sys_plan_restriction")
@NamedQuery(name="SysPlanRestriction.findAll", query="SELECT s FROM SysPlanRestriction s")
public class SysPlanRestriction implements Serializable {
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

	@Column(name="value_restriction", nullable=false)
	private Integer valueRestriction;

	//bi-directional many-to-one association to SysPlan
	@ManyToOne
	@JoinColumn(name="sys_plan_id", nullable=false)
	private SysPlan sysPlan;

	//bi-directional many-to-one association to SysRestriction
	@ManyToOne
	@JoinColumn(name="sys_restriction_id", nullable=false)
	private SysRestriction sysRestriction;

	public SysPlanRestriction() {
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

	public Integer getValueRestriction() {
		return this.valueRestriction;
	}

	public void setValueRestriction(Integer valueRestriction) {
		this.valueRestriction = valueRestriction;
	}

	public SysPlan getSysPlan() {
		return this.sysPlan;
	}

	public void setSysPlan(SysPlan sysPlan) {
		this.sysPlan = sysPlan;
	}

	public SysRestriction getSysRestriction() {
		return this.sysRestriction;
	}

	public void setSysRestriction(SysRestriction sysRestriction) {
		this.sysRestriction = sysRestriction;
	}

}