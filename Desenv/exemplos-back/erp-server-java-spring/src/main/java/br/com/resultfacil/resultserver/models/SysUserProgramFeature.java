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
@Table(name="sys_user_program_feature")
@NamedQuery(name="SysUserProgramFeature.findAll", query="SELECT s FROM SysUserProgramFeature s")
public class SysUserProgramFeature implements Serializable {
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

	@ManyToOne
	@JoinColumn(name="sys_program_id", nullable=false)
	private SysProgram sysProgram;

	@ManyToOne
	@JoinColumn(name="sys_user_id", nullable=false)
	private SysUser sysUser;

}