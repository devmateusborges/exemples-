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
@Table(name="crm_status")
@NamedQuery(name="CrmStatus.findAll", query="SELECT c FROM CrmStatus c")
public class CrmStatus implements Serializable {
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

	@Column(name="obrig_motivo", nullable=false, length=1)
	private String obrigMotivo;

	@Column(name="sigla_status", nullable=false, length=50)
	private String siglaStatus;

	@Column(name="tipo_status", nullable=false, length=2)
	private String tipoStatus;

	@OneToMany(mappedBy="crmStatus")
	private List<CrmMov> crmMovs;

	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	@OneToMany(mappedBy="crmStatus1")
	private List<CrmStatusProx> crmStatusProxs1;

	@OneToMany(mappedBy="crmStatus2")
	private List<CrmStatusProx> crmStatusProxs2;


}