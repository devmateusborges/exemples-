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
@Table(name="sys_program_favorite")
@NamedQuery(name="SysProgramFavorite.findAll", query="SELECT s FROM SysProgramFavorite s")
public class SysProgramFavorite implements Serializable {
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

	//bi-directional many-to-one association to SysProgram
	@ManyToOne
	@JoinColumn(name="sys_program_id")
	private SysProgram sysProgram;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="sys_user_id")
	private SysUser sysUser;


}