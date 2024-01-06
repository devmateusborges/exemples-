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
@Table(name="sys_module")
@NamedQuery(name="SysModule.findAll", query="SELECT s FROM SysModule s")
public class SysModule implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=50)
	private String color;

	@Column(nullable=false, length=50)
	private String icon;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(nullable=false, length=100)
	private String name;

	@Column(name="sigla_module", nullable=false, length=50)
	private String siglaModule;

	//bi-directional many-to-one association to Sy
	@ManyToOne
	@JoinColumn(name="sys_id", nullable=false)
	private Sys sys;

	//bi-directional many-to-one association to SysProgram
	@OneToMany(mappedBy="sysModule")
	private List<SysProgram> sysPrograms;

	public SysModule() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getColor() {
		return this.color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public String getIcon() {
		return this.icon;
	}

	public void setIcon(String icon) {
		this.icon = icon;
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

	public String getSiglaModule() {
		return this.siglaModule;
	}

	public void setSiglaModule(String siglaModule) {
		this.siglaModule = siglaModule;
	}

	public Sys getSys() {
		return this.sys;
	}

	public void setSys(Sys sys) {
		this.sys = sys;
	}

	public List<SysProgram> getSysPrograms() {
		return this.sysPrograms;
	}

	public void setSysPrograms(List<SysProgram> sysPrograms) {
		this.sysPrograms = sysPrograms;
	}

	public SysProgram addSysProgram(SysProgram sysProgram) {
		getSysPrograms().add(sysProgram);
		sysProgram.setSysModule(this);

		return sysProgram;
	}

	public SysProgram removeSysProgram(SysProgram sysProgram) {
		getSysPrograms().remove(sysProgram);
		sysProgram.setSysModule(null);

		return sysProgram;
	}

}