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
@Table(name="sys_group")
@NamedQuery(name="SysGroup.findAll", query="SELECT s FROM SysGroup s")
public class SysGroup implements Serializable {
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

	//bi-directional many-to-one association to SysDocumentGroup
	@OneToMany(mappedBy="sysGroup")
	private List<SysDocumentGroup> sysDocumentGroups;

	//bi-directional many-to-one association to SysGroupProgram
	@OneToMany(mappedBy="sysGroup")
	private List<SysGroupProgram> sysGroupPrograms;

	//bi-directional many-to-one association to SysGroupProgramFeature
	@OneToMany(mappedBy="sysGroup")
	private List<SysGroupProgramFeature> sysGroupProgramFeatures;

	//bi-directional many-to-one association to SysUserGroup
	@OneToMany(mappedBy="sysGroup")
	private List<SysUserGroup> sysUserGroups;

	public SysGroup() {
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

	public List<SysDocumentGroup> getSysDocumentGroups() {
		return this.sysDocumentGroups;
	}

	public void setSysDocumentGroups(List<SysDocumentGroup> sysDocumentGroups) {
		this.sysDocumentGroups = sysDocumentGroups;
	}

	public SysDocumentGroup addSysDocumentGroup(SysDocumentGroup sysDocumentGroup) {
		getSysDocumentGroups().add(sysDocumentGroup);
		sysDocumentGroup.setSysGroup(this);

		return sysDocumentGroup;
	}

	public SysDocumentGroup removeSysDocumentGroup(SysDocumentGroup sysDocumentGroup) {
		getSysDocumentGroups().remove(sysDocumentGroup);
		sysDocumentGroup.setSysGroup(null);

		return sysDocumentGroup;
	}

	public List<SysGroupProgram> getSysGroupPrograms() {
		return this.sysGroupPrograms;
	}

	public void setSysGroupPrograms(List<SysGroupProgram> sysGroupPrograms) {
		this.sysGroupPrograms = sysGroupPrograms;
	}

	public SysGroupProgram addSysGroupProgram(SysGroupProgram sysGroupProgram) {
		getSysGroupPrograms().add(sysGroupProgram);
		sysGroupProgram.setSysGroup(this);

		return sysGroupProgram;
	}

	public SysGroupProgram removeSysGroupProgram(SysGroupProgram sysGroupProgram) {
		getSysGroupPrograms().remove(sysGroupProgram);
		sysGroupProgram.setSysGroup(null);

		return sysGroupProgram;
	}

	public List<SysGroupProgramFeature> getSysGroupProgramFeatures() {
		return this.sysGroupProgramFeatures;
	}

	public void setSysGroupProgramFeatures(List<SysGroupProgramFeature> sysGroupProgramFeatures) {
		this.sysGroupProgramFeatures = sysGroupProgramFeatures;
	}

	public SysGroupProgramFeature addSysGroupProgramFeature(SysGroupProgramFeature sysGroupProgramFeature) {
		getSysGroupProgramFeatures().add(sysGroupProgramFeature);
		sysGroupProgramFeature.setSysGroup(this);

		return sysGroupProgramFeature;
	}

	public SysGroupProgramFeature removeSysGroupProgramFeature(SysGroupProgramFeature sysGroupProgramFeature) {
		getSysGroupProgramFeatures().remove(sysGroupProgramFeature);
		sysGroupProgramFeature.setSysGroup(null);

		return sysGroupProgramFeature;
	}

	public List<SysUserGroup> getSysUserGroups() {
		return this.sysUserGroups;
	}

	public void setSysUserGroups(List<SysUserGroup> sysUserGroups) {
		this.sysUserGroups = sysUserGroups;
	}

	public SysUserGroup addSysUserGroup(SysUserGroup sysUserGroup) {
		getSysUserGroups().add(sysUserGroup);
		sysUserGroup.setSysGroup(this);

		return sysUserGroup;
	}

	public SysUserGroup removeSysUserGroup(SysUserGroup sysUserGroup) {
		getSysUserGroups().remove(sysUserGroup);
		sysUserGroup.setSysGroup(null);

		return sysUserGroup;
	}

}