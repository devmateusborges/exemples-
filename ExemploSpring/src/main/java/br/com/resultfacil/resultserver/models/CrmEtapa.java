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
@Table(name="crm_etapa")
@NamedQuery(name="CrmEtapa.findAll", query="SELECT c FROM CrmEtapa c")
public class CrmEtapa implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

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

	@Column(name="sigla_etapa", nullable=false, length=50)
	private String siglaEtapa;

	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	@OneToMany(mappedBy="crmEtapa1")
	private List<CrmEtapaProx> crmEtapaProxs1;

	@OneToMany(mappedBy="crmEtapa2")
	private List<CrmEtapaProx> crmEtapaProxs2;

	@OneToMany(mappedBy="crmEtapa")
	private List<CrmMov> crmMovs;


}