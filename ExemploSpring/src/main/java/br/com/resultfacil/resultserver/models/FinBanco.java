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
@Table(name="fin_banco")
@NamedQuery(name="FinBanco.findAll", query="SELECT f FROM FinBanco f")
public class FinBanco implements Serializable {
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

	@Column(name="nr_banco", nullable=false, length=50)
	private String nrBanco;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FinConta
	@OneToMany(mappedBy="finBanco")
	private List<FinConta> finContas;

	//bi-directional many-to-one association to GerPessoaContaBanco
	@OneToMany(mappedBy="finBanco")
	private List<GerPessoaContaBanco> gerPessoaContaBancos;

	public FinBanco() {
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

	public String getNrBanco() {
		return this.nrBanco;
	}

	public void setNrBanco(String nrBanco) {
		this.nrBanco = nrBanco;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<FinConta> getFinContas() {
		return this.finContas;
	}

	public void setFinContas(List<FinConta> finContas) {
		this.finContas = finContas;
	}

	public FinConta addFinConta(FinConta finConta) {
		getFinContas().add(finConta);
		finConta.setFinBanco(this);

		return finConta;
	}

	public FinConta removeFinConta(FinConta finConta) {
		getFinContas().remove(finConta);
		finConta.setFinBanco(null);

		return finConta;
	}

	public List<GerPessoaContaBanco> getGerPessoaContaBancos() {
		return this.gerPessoaContaBancos;
	}

	public void setGerPessoaContaBancos(List<GerPessoaContaBanco> gerPessoaContaBancos) {
		this.gerPessoaContaBancos = gerPessoaContaBancos;
	}

	public GerPessoaContaBanco addGerPessoaContaBanco(GerPessoaContaBanco gerPessoaContaBanco) {
		getGerPessoaContaBancos().add(gerPessoaContaBanco);
		gerPessoaContaBanco.setFinBanco(this);

		return gerPessoaContaBanco;
	}

	public GerPessoaContaBanco removeGerPessoaContaBanco(GerPessoaContaBanco gerPessoaContaBanco) {
		getGerPessoaContaBancos().remove(gerPessoaContaBanco);
		gerPessoaContaBanco.setFinBanco(null);

		return gerPessoaContaBanco;
	}

}