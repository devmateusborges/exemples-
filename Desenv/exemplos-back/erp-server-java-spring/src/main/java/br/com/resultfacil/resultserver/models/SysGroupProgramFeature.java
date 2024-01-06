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
@Table(name="sys_group_program_feature")
@NamedQuery(name="SysGroupProgramFeature.findAll", query="SELECT s FROM SysGroupProgramFeature s")
public class SysGroupProgramFeature implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="identity_feature", nullable=false, length=200)
	private String identityFeature;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	//bi-directional many-to-one association to SysGroup
	@ManyToOne
	@JoinColumn(name="sys_group_id", nullable=false)
	private SysGroup sysGroup;

	//bi-directional many-to-one association to SysProgram
	@ManyToOne
	@JoinColumn(name="sys_program_id", nullable=false)
	private SysProgram sysProgram;

	public SysGroupProgramFeature() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getIdentityFeature() {
		return this.identityFeature;
	}

	public void setIdentityFeature(String identityFeature) {
		this.identityFeature = identityFeature;
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

	public SysGroup getSysGroup() {
		return this.sysGroup;
	}

	public void setSysGroup(SysGroup sysGroup) {
		this.sysGroup = sysGroup;
	}

	public SysProgram getSysProgram() {
		return this.sysProgram;
	}

	public void setSysProgram(SysProgram sysProgram) {
		this.sysProgram = sysProgram;
	}

}