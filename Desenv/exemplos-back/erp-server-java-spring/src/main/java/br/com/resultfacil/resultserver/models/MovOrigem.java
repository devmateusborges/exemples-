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
@Table(name="mov_origem")
@NamedQuery(name="MovOrigem.findAll", query="SELECT m FROM MovOrigem m")
public class MovOrigem implements Serializable {
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

	@Column(length=50)
	private String tipo;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id", nullable=false)
	private Mov mov1;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id_origem")
	private Mov mov2;

	//bi-directional many-to-one association to MovItemserv
	@ManyToOne
	@JoinColumn(name="mov_itemserv_id")
	private MovItemserv movItemserv1;

	//bi-directional many-to-one association to MovItemserv
	@ManyToOne
	@JoinColumn(name="mov_itemserv_id_origem")
	private MovItemserv movItemserv2;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public MovOrigem() {
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

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public Mov getMov1() {
		return this.mov1;
	}

	public void setMov1(Mov mov1) {
		this.mov1 = mov1;
	}

	public Mov getMov2() {
		return this.mov2;
	}

	public void setMov2(Mov mov2) {
		this.mov2 = mov2;
	}

	public MovItemserv getMovItemserv1() {
		return this.movItemserv1;
	}

	public void setMovItemserv1(MovItemserv movItemserv1) {
		this.movItemserv1 = movItemserv1;
	}

	public MovItemserv getMovItemserv2() {
		return this.movItemserv2;
	}

	public void setMovItemserv2(MovItemserv movItemserv2) {
		this.movItemserv2 = movItemserv2;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}