package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.util.Date;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ctb_conta_versao")
@NamedQuery(name="CtbContaVersao.findAll", query="SELECT c FROM CtbContaVersao c")
public class CtbContaVersao implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Temporal(TemporalType.DATE)
	@Column(name="data_valid_ini", nullable=false)
	private Date dataValidIni;

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

	@Column(name="sigla_versao", nullable=false, length=50)
	private String siglaVersao;

	@Column(name="versao_atual", nullable=false, length=2147483647)
	private String versaoAtual;

	//bi-directional many-to-one association to CtbConta
	@OneToMany(mappedBy="ctbContaVersao")
	private List<CtbConta> ctbContas;

	//bi-directional many-to-one association to CtbContaGrupo
	@OneToMany(mappedBy="ctbContaVersao")
	private List<CtbContaGrupo> ctbContaGrupos;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public CtbContaVersao() {
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

	public Date getDataValidIni() {
		return this.dataValidIni;
	}

	public void setDataValidIni(Date dataValidIni) {
		this.dataValidIni = dataValidIni;
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

	public String getSiglaVersao() {
		return this.siglaVersao;
	}

	public void setSiglaVersao(String siglaVersao) {
		this.siglaVersao = siglaVersao;
	}

	public String getVersaoAtual() {
		return this.versaoAtual;
	}

	public void setVersaoAtual(String versaoAtual) {
		this.versaoAtual = versaoAtual;
	}

	public List<CtbConta> getCtbContas() {
		return this.ctbContas;
	}

	public void setCtbContas(List<CtbConta> ctbContas) {
		this.ctbContas = ctbContas;
	}

	public CtbConta addCtbConta(CtbConta ctbConta) {
		getCtbContas().add(ctbConta);
		ctbConta.setCtbContaVersao(this);

		return ctbConta;
	}

	public CtbConta removeCtbConta(CtbConta ctbConta) {
		getCtbContas().remove(ctbConta);
		ctbConta.setCtbContaVersao(null);

		return ctbConta;
	}

	public List<CtbContaGrupo> getCtbContaGrupos() {
		return this.ctbContaGrupos;
	}

	public void setCtbContaGrupos(List<CtbContaGrupo> ctbContaGrupos) {
		this.ctbContaGrupos = ctbContaGrupos;
	}

	public CtbContaGrupo addCtbContaGrupo(CtbContaGrupo ctbContaGrupo) {
		getCtbContaGrupos().add(ctbContaGrupo);
		ctbContaGrupo.setCtbContaVersao(this);

		return ctbContaGrupo;
	}

	public CtbContaGrupo removeCtbContaGrupo(CtbContaGrupo ctbContaGrupo) {
		getCtbContaGrupos().remove(ctbContaGrupo);
		ctbContaGrupo.setCtbContaVersao(null);

		return ctbContaGrupo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}