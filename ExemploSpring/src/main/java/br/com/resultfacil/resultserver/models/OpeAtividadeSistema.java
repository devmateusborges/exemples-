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
@Table(name="ope_atividade_sistema")
@NamedQuery(name="OpeAtividadeSistema.findAll", query="SELECT o FROM OpeAtividadeSistema o")
public class OpeAtividadeSistema implements Serializable {
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

	@Column(name="sigla_atividade_grupo", length=50)
	private String siglaAtividadeGrupo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCentro2Area
	@OneToMany(mappedBy="opeAtividadeSistema1")
	private List<OpeCentro2Area> opeCentro2Areas1;

	//bi-directional many-to-one association to OpeCentro2Area
	@OneToMany(mappedBy="opeAtividadeSistema2")
	private List<OpeCentro2Area> opeCentro2Areas2;

	//bi-directional many-to-one association to OpeCentro2Area
	@OneToMany(mappedBy="opeAtividadeSistema3")
	private List<OpeCentro2Area> opeCentro2Areas3;

	public OpeAtividadeSistema() {
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

	public String getSiglaAtividadeGrupo() {
		return this.siglaAtividadeGrupo;
	}

	public void setSiglaAtividadeGrupo(String siglaAtividadeGrupo) {
		this.siglaAtividadeGrupo = siglaAtividadeGrupo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCentro2Area> getOpeCentro2Areas1() {
		return this.opeCentro2Areas1;
	}

	public void setOpeCentro2Areas1(List<OpeCentro2Area> opeCentro2Areas1) {
		this.opeCentro2Areas1 = opeCentro2Areas1;
	}

	public OpeCentro2Area addOpeCentro2Areas1(OpeCentro2Area opeCentro2Areas1) {
		getOpeCentro2Areas1().add(opeCentro2Areas1);
		opeCentro2Areas1.setOpeAtividadeSistema1(this);

		return opeCentro2Areas1;
	}

	public OpeCentro2Area removeOpeCentro2Areas1(OpeCentro2Area opeCentro2Areas1) {
		getOpeCentro2Areas1().remove(opeCentro2Areas1);
		opeCentro2Areas1.setOpeAtividadeSistema1(null);

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
		opeCentro2Areas2.setOpeAtividadeSistema2(this);

		return opeCentro2Areas2;
	}

	public OpeCentro2Area removeOpeCentro2Areas2(OpeCentro2Area opeCentro2Areas2) {
		getOpeCentro2Areas2().remove(opeCentro2Areas2);
		opeCentro2Areas2.setOpeAtividadeSistema2(null);

		return opeCentro2Areas2;
	}

	public List<OpeCentro2Area> getOpeCentro2Areas3() {
		return this.opeCentro2Areas3;
	}

	public void setOpeCentro2Areas3(List<OpeCentro2Area> opeCentro2Areas3) {
		this.opeCentro2Areas3 = opeCentro2Areas3;
	}

	public OpeCentro2Area addOpeCentro2Areas3(OpeCentro2Area opeCentro2Areas3) {
		getOpeCentro2Areas3().add(opeCentro2Areas3);
		opeCentro2Areas3.setOpeAtividadeSistema3(this);

		return opeCentro2Areas3;
	}

	public OpeCentro2Area removeOpeCentro2Areas3(OpeCentro2Area opeCentro2Areas3) {
		getOpeCentro2Areas3().remove(opeCentro2Areas3);
		opeCentro2Areas3.setOpeAtividadeSistema3(null);

		return opeCentro2Areas3;
	}

}