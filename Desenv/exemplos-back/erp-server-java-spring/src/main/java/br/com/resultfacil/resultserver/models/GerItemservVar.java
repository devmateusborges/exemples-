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
@Table(name="ger_itemserv_var")
@NamedQuery(name="GerItemservVar.findAll", query="SELECT g FROM GerItemservVar g")
public class GerItemservVar implements Serializable {
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

	@Column(name="sigla_itemserv_var", length=50)
	private String siglaItemservVar;

	//bi-directional many-to-one association to OpeCicloVar
	@ManyToOne
	@JoinColumn(name="ope_ciclo_var_id")
	private OpeCicloVar opeCicloVar;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to MovItemserv
	@OneToMany(mappedBy="gerItemservVar")
	private List<MovItemserv> movItemservs;

	//bi-directional many-to-one association to OpeCentro2Area
	@OneToMany(mappedBy="gerItemservVar1")
	private List<OpeCentro2Area> opeCentro2Areas1;

	//bi-directional many-to-one association to OpeCentro2Area
	@OneToMany(mappedBy="gerItemservVar2")
	private List<OpeCentro2Area> opeCentro2Areas2;

	public GerItemservVar() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getAtivo() {
		return this.ativo;
	}

	public void setAtivo(String ativo) {
		this.ativo = ativo;
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

	public String getNome() {
		return this.nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getSiglaItemservVar() {
		return this.siglaItemservVar;
	}

	public void setSiglaItemservVar(String siglaItemservVar) {
		this.siglaItemservVar = siglaItemservVar;
	}

	public OpeCicloVar getOpeCicloVar() {
		return this.opeCicloVar;
	}

	public void setOpeCicloVar(OpeCicloVar opeCicloVar) {
		this.opeCicloVar = opeCicloVar;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<MovItemserv> getMovItemservs() {
		return this.movItemservs;
	}

	public void setMovItemservs(List<MovItemserv> movItemservs) {
		this.movItemservs = movItemservs;
	}

	public MovItemserv addMovItemserv(MovItemserv movItemserv) {
		getMovItemservs().add(movItemserv);
		movItemserv.setGerItemservVar(this);

		return movItemserv;
	}

	public MovItemserv removeMovItemserv(MovItemserv movItemserv) {
		getMovItemservs().remove(movItemserv);
		movItemserv.setGerItemservVar(null);

		return movItemserv;
	}

	public List<OpeCentro2Area> getOpeCentro2Areas1() {
		return this.opeCentro2Areas1;
	}

	public void setOpeCentro2Areas1(List<OpeCentro2Area> opeCentro2Areas1) {
		this.opeCentro2Areas1 = opeCentro2Areas1;
	}

	public OpeCentro2Area addOpeCentro2Areas1(OpeCentro2Area opeCentro2Areas1) {
		getOpeCentro2Areas1().add(opeCentro2Areas1);
		opeCentro2Areas1.setGerItemservVar1(this);

		return opeCentro2Areas1;
	}

	public OpeCentro2Area removeOpeCentro2Areas1(OpeCentro2Area opeCentro2Areas1) {
		getOpeCentro2Areas1().remove(opeCentro2Areas1);
		opeCentro2Areas1.setGerItemservVar1(null);

		return opeCentro2Areas1;
	}

	public List<OpeCentro2Area> getOpeCentro2Areas2() {
		return this.opeCentro2Areas2;
	}

	public void setOpeCentro2Areas2(List<OpeCentro2Area> opeCentro2Areas2) {
		this.opeCentro2Areas2 = opeCentro2Areas2;
	}

	public OpeCentro2Area addOpeCentro2Areas2(OpeCentro2Area opeCentro2Areas2) {
		getOpeCentro2Areas2().add(opeCentro2Areas2);
		opeCentro2Areas2.setGerItemservVar2(this);

		return opeCentro2Areas2;
	}

	public OpeCentro2Area removeOpeCentro2Areas2(OpeCentro2Area opeCentro2Areas2) {
		getOpeCentro2Areas2().remove(opeCentro2Areas2);
		opeCentro2Areas2.setGerItemservVar2(null);

		return opeCentro2Areas2;
	}

}