package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.util.Date;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="crm_mov")
@NamedQuery(name="CrmMov.findAll", query="SELECT c FROM CrmMov c")
public class CrmMov implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_mov", nullable=false)
	private Date dataMov;

	@Temporal(TemporalType.DATE)
	@Column(name="data_status", nullable=false)
	private Date dataStatus;

	@Column(name="descritivo_ext", nullable=false, length=2147483647)
	private String descritivoExt;

	@Column(name="descritivo_int", length=2147483647)
	private String descritivoInt;

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

	@Column(nullable=false, length=10)
	private String numero;

	@Column(length=200)
	private String titulo;

	@ManyToOne
	@JoinColumn(name="crm_etapa_id", nullable=false)
	private CrmEtapa crmEtapa;

	@ManyToOne
	@JoinColumn(name="crm_prioridade_id", nullable=false)
	private CrmPrioridade crmPrioridade;

	@ManyToOne
	@JoinColumn(name="crm_status_id", nullable=false)
	private CrmStatus crmStatus;

	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	@ManyToOne
	@JoinColumn(name="sys_user_id_atend_ant")
	private SysUser sysUser1;

	@ManyToOne
	@JoinColumn(name="sys_user_id_atend_atu")
	private SysUser sysUser2;

	@ManyToOne
	@JoinColumn(name="sys_user_id_solic", nullable=false)
	private SysUser sysUser3;

	@OneToMany(mappedBy="crmMov")
	private List<CrmMovHist> crmMovHists;

	@OneToMany(mappedBy="crmMov")
	private List<CrmMovTag> crmMovTags;

	@OneToMany(mappedBy="crmMov")
	private List<SysDocument> sysDocuments;

}