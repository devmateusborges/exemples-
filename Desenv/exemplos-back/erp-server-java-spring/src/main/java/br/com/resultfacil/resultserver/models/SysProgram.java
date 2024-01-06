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
@Table(name="sys_program")
@NamedQuery(name="SysProgram.findAll", query="SELECT s FROM SysProgram s")
public class SysProgram implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String admin;

	@Column(nullable=false, length=100)
	private String controller;

	@Column(length=50)
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

	@Column(nullable=false, length=1)
	private String menu;

	@Column(nullable=false, length=100)
	private String name;

	@Column(name="type_program", nullable=false, length=1)
	private String typeProgram;

	@OneToMany(mappedBy="sysProgram")
	private List<SysGroupProgram> sysGroupPrograms;

	@OneToMany(mappedBy="sysProgram")
	private List<SysGroupProgramFeature> sysGroupProgramFeatures;

	@ManyToOne
	@JoinColumn(name="module_id", nullable=false)
	private SysModule sysModule;

	@OneToMany(mappedBy="sysProgram")
	private List<SysProgramFavorite> sysProgramFavorites;

	@OneToMany(mappedBy="sysProgram")
	private List<SysProgramFeature> sysProgramFeatures;

	@OneToMany(mappedBy="sysProgram")
	private List<SysUserProgram> sysUserPrograms;

	@OneToMany(mappedBy="sysProgram")
	private List<SysUserProgramFeature> sysUserProgramFeatures;


}