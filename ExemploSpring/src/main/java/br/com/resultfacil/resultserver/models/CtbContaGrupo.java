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
@Table(name="ctb_conta_grupo")
@NamedQuery(name="CtbContaGrupo.findAll", query="SELECT c FROM CtbContaGrupo c")
public class CtbContaGrupo implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(nullable=false, length=50)
	private String estrutura;

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

	@Column(name="sigla_conta_grupo", nullable=false, length=50)
	private String siglaContaGrupo;

	//bi-directional many-to-one association to CtbConta
	@OneToMany(mappedBy="ctbContaGrupo")
	private List<CtbConta> ctbContas;

	//bi-directional many-to-one association to CtbContaVersao
	@ManyToOne
	@JoinColumn(name="ctb_conta_versao_id", nullable=false)
	private CtbContaVersao ctbContaVersao;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public CtbContaGrupo() {
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

	public String getEstrutura() {
		return this.estrutura;
	}

	public void setEstrutura(String estrutura) {
		this.estrutura = estrutura;
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

	public String getSiglaContaGrupo() {
		return this.siglaContaGrupo;
	}

	public void setSiglaContaGrupo(String siglaContaGrupo) {
		this.siglaContaGrupo = siglaContaGrupo;
	}

	public List<CtbConta> getCtbContas() {
		return this.ctbContas;
	}

	public void setCtbContas(List<CtbConta> ctbContas) {
		this.ctbContas = ctbContas;
	}

	public CtbConta addCtbConta(CtbConta ctbConta) {
		getCtbContas().add(ctbConta);
		ctbConta.setCtbContaGrupo(this);

		return ctbConta;
	}

	public CtbConta removeCtbConta(CtbConta ctbConta) {
		getCtbContas().remove(ctbConta);
		ctbConta.setCtbContaGrupo(null);

		return ctbConta;
	}

	public CtbContaVersao getCtbContaVersao() {
		return this.ctbContaVersao;
	}

	public void setCtbContaVersao(CtbContaVersao ctbContaVersao) {
		this.ctbContaVersao = ctbContaVersao;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}