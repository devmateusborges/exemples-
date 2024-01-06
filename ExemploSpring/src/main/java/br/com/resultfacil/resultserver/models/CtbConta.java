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
@Table(name="ctb_conta")
@NamedQuery(name="CtbConta.findAll", query="SELECT c FROM CtbConta c")
public class CtbConta implements Serializable {
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

	@Column(name="sigla_conta", nullable=false, length=50)
	private String siglaConta;

	@Column(name="tipo_conta", nullable=false, length=2)
	private String tipoConta;

	@Column(name="tipo_dc", nullable=false, length=1)
	private String tipoDc;

	@Column(name="tipo_variacao", nullable=false, length=1)
	private String tipoVariacao;

	//bi-directional many-to-one association to CtbContaGrupo
	@ManyToOne
	@JoinColumn(name="ctb_conta_grupo_id", nullable=false)
	private CtbContaGrupo ctbContaGrupo;

	//bi-directional many-to-one association to CtbContaVersao
	@ManyToOne
	@JoinColumn(name="ctb_conta_versao_id", nullable=false)
	private CtbContaVersao ctbContaVersao;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to CtbLancDet
	@OneToMany(mappedBy="ctbConta")
	private List<CtbLancDet> ctbLancDets;

	public CtbConta() {
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

	public String getSiglaConta() {
		return this.siglaConta;
	}

	public void setSiglaConta(String siglaConta) {
		this.siglaConta = siglaConta;
	}

	public String getTipoConta() {
		return this.tipoConta;
	}

	public void setTipoConta(String tipoConta) {
		this.tipoConta = tipoConta;
	}

	public String getTipoDc() {
		return this.tipoDc;
	}

	public void setTipoDc(String tipoDc) {
		this.tipoDc = tipoDc;
	}

	public String getTipoVariacao() {
		return this.tipoVariacao;
	}

	public void setTipoVariacao(String tipoVariacao) {
		this.tipoVariacao = tipoVariacao;
	}

	public CtbContaGrupo getCtbContaGrupo() {
		return this.ctbContaGrupo;
	}

	public void setCtbContaGrupo(CtbContaGrupo ctbContaGrupo) {
		this.ctbContaGrupo = ctbContaGrupo;
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

	public List<CtbLancDet> getCtbLancDets() {
		return this.ctbLancDets;
	}

	public void setCtbLancDets(List<CtbLancDet> ctbLancDets) {
		this.ctbLancDets = ctbLancDets;
	}

	public CtbLancDet addCtbLancDet(CtbLancDet ctbLancDet) {
		getCtbLancDets().add(ctbLancDet);
		ctbLancDet.setCtbConta(this);

		return ctbLancDet;
	}

	public CtbLancDet removeCtbLancDet(CtbLancDet ctbLancDet) {
		getCtbLancDets().remove(ctbLancDet);
		ctbLancDet.setCtbConta(null);

		return ctbLancDet;
	}

}