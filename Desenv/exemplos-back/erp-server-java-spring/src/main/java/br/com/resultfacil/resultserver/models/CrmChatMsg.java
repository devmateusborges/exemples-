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
@Table(name="crm_chat_msg")
@NamedQuery(name="CrmChatMsg.findAll", query="SELECT c FROM CrmChatMsg c")
public class CrmChatMsg implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(length=1)
	private String ativo;

	@Column(length=2147483647)
	private String corpo;

	@Temporal(TemporalType.DATE)
	@Column(name="data_msg")
	private Date dataMsg;

	@CreationTimestamp
	@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@ManyToOne
	@JoinColumn(name="crm_chat_grupo_id", nullable=false)
	private CrmChatGrupo crmChatGrupo;

	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	@ManyToOne
	@JoinColumn(name="sys_user_id_orig", nullable=false)
	private SysUser sysUser;

}