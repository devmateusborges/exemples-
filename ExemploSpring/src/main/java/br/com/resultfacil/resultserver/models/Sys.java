package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import java.sql.Timestamp;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.NamedQuery;
import javax.persistence.OneToMany;
import javax.persistence.Table;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="sys")
@NamedQuery(name="Sys.findAll", query="SELECT s FROM Sys s")
public class Sys implements Serializable {
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

	@Column(length=100)
	private String name;

	@OneToMany(mappedBy="sys")
	private List<SysAccessLog> sysAccessLogs;

	@OneToMany(mappedBy="sys")
	private List<SysLicence> sysLicences;

	@OneToMany(mappedBy="sys")
	private List<SysModule> sysModules;

	@OneToMany(mappedBy="sys")
	private List<SysParam> sysParams;

	@OneToMany(mappedBy="sys")
	private List<SysPlan> sysPlans;

	public Sys() {
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

	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public List<SysAccessLog> getSysAccessLogs() {
		return this.sysAccessLogs;
	}

	public void setSysAccessLogs(List<SysAccessLog> sysAccessLogs) {
		this.sysAccessLogs = sysAccessLogs;
	}

	public SysAccessLog addSysAccessLog(SysAccessLog sysAccessLog) {
		getSysAccessLogs().add(sysAccessLog);
		sysAccessLog.setSys(this);

		return sysAccessLog;
	}

	public SysAccessLog removeSysAccessLog(SysAccessLog sysAccessLog) {
		getSysAccessLogs().remove(sysAccessLog);
		sysAccessLog.setSys(null);

		return sysAccessLog;
	}

	public List<SysLicence> getSysLicences() {
		return this.sysLicences;
	}

	public void setSysLicences(List<SysLicence> sysLicences) {
		this.sysLicences = sysLicences;
	}

	public SysLicence addSysLicence(SysLicence sysLicence) {
		getSysLicences().add(sysLicence);
		sysLicence.setSys(this);

		return sysLicence;
	}

	public SysLicence removeSysLicence(SysLicence sysLicence) {
		getSysLicences().remove(sysLicence);
		sysLicence.setSys(null);

		return sysLicence;
	}

	public List<SysModule> getSysModules() {
		return this.sysModules;
	}

	public void setSysModules(List<SysModule> sysModules) {
		this.sysModules = sysModules;
	}

	public SysModule addSysModule(SysModule sysModule) {
		getSysModules().add(sysModule);
		sysModule.setSys(this);

		return sysModule;
	}

	public SysModule removeSysModule(SysModule sysModule) {
		getSysModules().remove(sysModule);
		sysModule.setSys(null);

		return sysModule;
	}

	public List<SysParam> getSysParams() {
		return this.sysParams;
	}

	public void setSysParams(List<SysParam> sysParams) {
		this.sysParams = sysParams;
	}

	public SysParam addSysParam(SysParam sysParam) {
		getSysParams().add(sysParam);
		sysParam.setSys(this);

		return sysParam;
	}

	public SysParam removeSysParam(SysParam sysParam) {
		getSysParams().remove(sysParam);
		sysParam.setSys(null);

		return sysParam;
	}

	public List<SysPlan> getSysPlans() {
		return this.sysPlans;
	}

	public void setSysPlans(List<SysPlan> sysPlans) {
		this.sysPlans = sysPlans;
	}

	public SysPlan addSysPlan(SysPlan sysPlan) {
		getSysPlans().add(sysPlan);
		sysPlan.setSys(this);

		return sysPlan;
	}

	public SysPlan removeSysPlan(SysPlan sysPlan) {
		getSysPlans().remove(sysPlan);
		sysPlan.setSys(null);

		return sysPlan;
	}

}