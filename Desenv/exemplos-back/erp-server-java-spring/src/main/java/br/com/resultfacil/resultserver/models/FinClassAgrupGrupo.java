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
@Table(name="fin_class_agrup_grupo")
@NamedQuery(name="FinClassAgrupGrupo.findAll", query="SELECT f FROM FinClassAgrupGrupo f")
public class FinClassAgrupGrupo implements Serializable {
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

	//bi-directional many-to-one association to FinClass
	@ManyToOne
	@JoinColumn(name="fin_class_id", nullable=false)
	private FinClass finClass;

	//bi-directional many-to-one association to FinClassAgrup
	@ManyToOne
	@JoinColumn(name="fin_class_agrup_id", nullable=false)
	private FinClassAgrup finClassAgrup;

	//bi-directional many-to-one association to FinClassGrupo
	@ManyToOne
	@JoinColumn(name="fin_class_grupo_id", nullable=false)
	private FinClassGrupo finClassGrupo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public FinClassAgrupGrupo() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Timestamp getLogDateIns() {
		return this.logDateIns;
	}

	public void setLogDateIns(Timestamp logDateIns) {
		this.logDateIns = logDateIns;
	}

	public Timestamp getLogDateUpd() {
		return this.logDateUpd;
	}

	public void setLogDateUpd(Timestamp logDateUpd) {
		this.logDateUpd = logDateUpd;
	}

	public String getLogUserIns() {
		return this.logUserIns;
	}

	public void setLogUserIns(String logUserIns) {
		this.logUserIns = logUserIns;
	}

	public String getLogUserUpd() {
		return this.logUserUpd;
	}

	public void setLogUserUpd(String logUserUpd) {
		this.logUserUpd = logUserUpd;
	}

	public FinClass getFinClass() {
		return this.finClass;
	}

	public void setFinClass(FinClass finClass) {
		this.finClass = finClass;
	}

	public FinClassAgrup getFinClassAgrup() {
		return this.finClassAgrup;
	}

	public void setFinClassAgrup(FinClassAgrup finClassAgrup) {
		this.finClassAgrup = finClassAgrup;
	}

	public FinClassGrupo getFinClassGrupo() {
		return this.finClassGrupo;
	}

	public void setFinClassGrupo(FinClassGrupo finClassGrupo) {
		this.finClassGrupo = finClassGrupo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}