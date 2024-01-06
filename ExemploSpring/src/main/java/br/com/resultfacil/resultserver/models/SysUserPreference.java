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
@Table(name="sys_user_preference")
@NamedQuery(name="SysUserPreference.findAll", query="SELECT s FROM SysUserPreference s")
public class SysUserPreference implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=100)
	private String id;

	@Column(length=1)
	private String defaultd;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="object_id", nullable=false, length=36)
	private String objectId;

	@Column(name="object_type", nullable=false, length=36)
	private String objectType;

	@Column(name="preference_description", nullable=false, length=50)
	private String preferenceDescription;

	@Column(length=2147483647)
	private String value;

	@ManyToOne
	@JoinColumn(name="sys_user_id", nullable=false)
	private SysUser sysUser;

}