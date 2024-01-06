package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;



import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="sys_user_chat_grupo")
@NamedQuery(name="SysUserChatGrupo.findAll", query="SELECT s FROM SysUserChatGrupo s")
public class SysUserChatGrupo implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@ManyToOne
	@JoinColumn(name="crm_chat_grupo_id", nullable=false)
	private CrmChatGrupo crmChatGrupo;

	@ManyToOne
	@JoinColumn(name="sys_user_id", nullable=false)
	private SysUser sysUser;


}