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
@Table(name="fis_certificado")
@NamedQuery(name="FisCertificado.findAll", query="SELECT f FROM FisCertificado f")
public class FisCertificado implements Serializable {
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

	@Column(name="nome_arq_certificado", length=250)
	private String nomeArqCertificado;

	@Column(length=50)
	private String senha;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to GerEmpresa
	@OneToMany(mappedBy="fisCertificado")
	private List<GerEmpresa> gerEmpresas;

	public FisCertificado() {
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

	public String getNomeArqCertificado() {
		return this.nomeArqCertificado;
	}

	public void setNomeArqCertificado(String nomeArqCertificado) {
		this.nomeArqCertificado = nomeArqCertificado;
	}

	public String getSenha() {
		return this.senha;
	}

	public void setSenha(String senha) {
		this.senha = senha;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<GerEmpresa> getGerEmpresas() {
		return this.gerEmpresas;
	}

	public void setGerEmpresas(List<GerEmpresa> gerEmpresas) {
		this.gerEmpresas = gerEmpresas;
	}

	public GerEmpresa addGerEmpresa(GerEmpresa gerEmpresa) {
		getGerEmpresas().add(gerEmpresa);
		gerEmpresa.setFisCertificado(this);

		return gerEmpresa;
	}

	public GerEmpresa removeGerEmpresa(GerEmpresa gerEmpresa) {
		getGerEmpresas().remove(gerEmpresa);
		gerEmpresa.setFisCertificado(null);

		return gerEmpresa;
	}

}