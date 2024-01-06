package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.util.Date;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="crm_mov_hist")
@NamedQuery(name="CrmMovHist.findAll", query="SELECT c FROM CrmMovHist c")
public class CrmMovHist implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_hist", nullable=false)
	private Date dataHist;

	@Column(nullable=false, length=2147483647)
	private String descritivo;

	@Column(name="envia_email_ext", nullable=false, length=1)
	private String enviaEmailExt;

	@CreationTimestamp
	@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="visual_ext", nullable=false, length=1)
	private String visualExt;

	@ManyToOne
	@JoinColumn(name="crm_mov_id", nullable=false)
	private CrmMov crmMov;

	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	@ManyToOne
	@JoinColumn(name="sys_user_id_hist", nullable=false)
	private SysUser sysUser;


}