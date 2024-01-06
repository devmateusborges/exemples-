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
@Table(name="sys_plan")
@NamedQuery(name="SysPlan.findAll", query="SELECT s FROM SysPlan s")
public class SysPlan implements Serializable {
	private static final long serialVersionUID = 1L;

	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=2147483647)
	private String description;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(length=100)
	private String name;

	@Column(name="type_plan", nullable=false, length=2)
	private String typePlan;

	//bi-directional many-to-one association to SysLicence
	@OneToMany(mappedBy="sysPlan")
	private List<SysLicence> sysLicences;

	//bi-directional many-to-one association to Sy
	@ManyToOne
	@JoinColumn(name="sys_id", nullable=false)
	private Sys sys;

	//bi-directional many-to-one association to SysPlanRestriction
	@OneToMany(mappedBy="sysPlan")
	private List<SysPlanRestriction> sysPlanRestrictions;

	public SysPlan() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getDescription() {
		return this.description;
	}

	public void setDescription(String description) {
		this.description = description;
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

	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getTypePlan() {
		return this.typePlan;
	}

	public void setTypePlan(String typePlan) {
		this.typePlan = typePlan;
	}

	public List<SysLicence> getSysLicences() {
		return this.sysLicences;
	}

	public void setSysLicences(List<SysLicence> sysLicences) {
		this.sysLicences = sysLicences;
	}

	public SysLicence addSysLicence(SysLicence sysLicence) {
		getSysLicences().add(sysLicence);
		sysLicence.setSysPlan(this);

		return sysLicence;
	}

	public SysLicence removeSysLicence(SysLicence sysLicence) {
		getSysLicences().remove(sysLicence);
		sysLicence.setSysPlan(null);

		return sysLicence;
	}

	public Sys getSys() {
		return this.sys;
	}

	public void setSys(Sys sys) {
		this.sys = sys;
	}

	public List<SysPlanRestriction> getSysPlanRestrictions() {
		return this.sysPlanRestrictions;
	}

	public void setSysPlanRestrictions(List<SysPlanRestriction> sysPlanRestrictions) {
		this.sysPlanRestrictions = sysPlanRestrictions;
	}

	public SysPlanRestriction addSysPlanRestriction(SysPlanRestriction sysPlanRestriction) {
		getSysPlanRestrictions().add(sysPlanRestriction);
		sysPlanRestriction.setSysPlan(this);

		return sysPlanRestriction;
	}

	public SysPlanRestriction removeSysPlanRestriction(SysPlanRestriction sysPlanRestriction) {
		getSysPlanRestrictions().remove(sysPlanRestriction);
		sysPlanRestriction.setSysPlan(null);

		return sysPlanRestriction;
	}

}