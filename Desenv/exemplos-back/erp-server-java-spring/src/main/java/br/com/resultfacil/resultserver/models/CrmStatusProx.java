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
@Table(name="crm_status_prox")
@NamedQuery(name="CrmStatusProx.findAll", query="SELECT c FROM CrmStatusProx c")
public class CrmStatusProx implements Serializable {
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

	@Column(nullable=false)
	private Integer ordem;

	@Column(name="tipo_status_ant", length=2)
	private String tipoStatusAnt;

	@ManyToOne
	@JoinColumn(name="crm_status_id", nullable=false)
	private CrmStatus crmStatus1;

	@ManyToOne
	@JoinColumn(name="crm_status_id_prox", nullable=false)
	private CrmStatus crmStatus2;

	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;


}