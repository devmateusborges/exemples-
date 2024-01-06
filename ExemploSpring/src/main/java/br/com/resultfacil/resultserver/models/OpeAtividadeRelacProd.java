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
@Table(name="ope_atividade_relac_prod")
@NamedQuery(name="OpeAtividadeRelacProd.findAll", query="SELECT o FROM OpeAtividadeRelacProd o")
public class OpeAtividadeRelacProd implements Serializable {
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

	@Column(name="ordem_visual", nullable=false, length=1)
	private String ordemVisual;

	//bi-directional many-to-one association to OpeAtividade
	@ManyToOne
	@JoinColumn(name="ope_atividade_id", nullable=false)
	private OpeAtividade opeAtividade1;

	//bi-directional many-to-one association to OpeAtividade
	@ManyToOne
	@JoinColumn(name="ope_atividade_id_prod", nullable=false)
	private OpeAtividade opeAtividade2;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeAtividadeRelacProd() {
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

	public String getOrdemVisual() {
		return this.ordemVisual;
	}

	public void setOrdemVisual(String ordemVisual) {
		this.ordemVisual = ordemVisual;
	}

	public OpeAtividade getOpeAtividade1() {
		return this.opeAtividade1;
	}

	public void setOpeAtividade1(OpeAtividade opeAtividade1) {
		this.opeAtividade1 = opeAtividade1;
	}

	public OpeAtividade getOpeAtividade2() {
		return this.opeAtividade2;
	}

	public void setOpeAtividade2(OpeAtividade opeAtividade2) {
		this.opeAtividade2 = opeAtividade2;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}