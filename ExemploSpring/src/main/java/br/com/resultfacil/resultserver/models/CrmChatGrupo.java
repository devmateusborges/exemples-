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
@Table(name="crm_chat_grupo")
@NamedQuery(name="CrmChatGrupo.findAll", query="SELECT c FROM CrmChatGrupo c")
public class CrmChatGrupo implements Serializable {
	private static final long serialVersionUID = 1L;
	
	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="acesso_privado", nullable=false, length=1)
	private String acessoPrivado;

	@Column(nullable=false, length=1)
	private String ativo;

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
	private String nome;

	@Column(length=100)
	private String senha;

	@Column(name="sigla_chat_grupo", nullable=false, length=50)
	private String siglaChatGrupo;

	@Column(nullable=false, length=1)
	private String tipo;

	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	@ManyToOne
	@JoinColumn(name="sys_user_id_dest")
	private SysUser sysUser1;

	@ManyToOne
	@JoinColumn(name="sys_user_id_orig", nullable=false)
	private SysUser sysUser2;

	@OneToMany(mappedBy="crmChatGrupo")
	private List<CrmChatMsg> crmChatMsgs;

	@OneToMany(mappedBy="crmChatGrupo")
	private List<SysUserChatGrupo> sysUserChatGrupos;


}