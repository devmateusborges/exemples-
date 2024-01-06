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
@Table(name="fin_conta")
@NamedQuery(name="FinConta.findAll", query="SELECT f FROM FinConta f")
public class FinConta implements Serializable {
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

	@Column(name="nr_agencia", nullable=false, length=50)
	private String nrAgencia;

	@Column(name="nr_conta", nullable=false, length=50)
	private String nrConta;

	//bi-directional many-to-one association to FinBanco
	@ManyToOne
	@JoinColumn(name="fin_banco_id", nullable=false)
	private FinBanco finBanco;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FinPagrecBaixa
	@OneToMany(mappedBy="finConta")
	private List<FinPagrecBaixa> finPagrecBaixas;

	//bi-directional many-to-one association to FinPagrecBanco
	@OneToMany(mappedBy="finConta")
	private List<FinPagrecBanco> finPagrecBancos;

	//bi-directional many-to-one association to FinPagrecBancoExtrato
	@OneToMany(mappedBy="finConta")
	private List<FinPagrecBancoExtrato> finPagrecBancoExtratos;

	//bi-directional many-to-one association to FinPagrecBancoTransf
	@OneToMany(mappedBy="finConta1")
	private List<FinPagrecBancoTransf> finPagrecBancoTransfs1;

	//bi-directional many-to-one association to FinPagrecBancoTransf
	@OneToMany(mappedBy="finConta2")
	private List<FinPagrecBancoTransf> finPagrecBancoTransfs2;

	public FinConta() {
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

	public String getNrAgencia() {
		return this.nrAgencia;
	}

	public void setNrAgencia(String nrAgencia) {
		this.nrAgencia = nrAgencia;
	}

	public String getNrConta() {
		return this.nrConta;
	}

	public void setNrConta(String nrConta) {
		this.nrConta = nrConta;
	}

	public FinBanco getFinBanco() {
		return this.finBanco;
	}

	public void setFinBanco(FinBanco finBanco) {
		this.finBanco = finBanco;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<FinPagrecBaixa> getFinPagrecBaixas() {
		return this.finPagrecBaixas;
	}

	public void setFinPagrecBaixas(List<FinPagrecBaixa> finPagrecBaixas) {
		this.finPagrecBaixas = finPagrecBaixas;
	}

	public FinPagrecBaixa addFinPagrecBaixa(FinPagrecBaixa finPagrecBaixa) {
		getFinPagrecBaixas().add(finPagrecBaixa);
		finPagrecBaixa.setFinConta(this);

		return finPagrecBaixa;
	}

	public FinPagrecBaixa removeFinPagrecBaixa(FinPagrecBaixa finPagrecBaixa) {
		getFinPagrecBaixas().remove(finPagrecBaixa);
		finPagrecBaixa.setFinConta(null);

		return finPagrecBaixa;
	}

	public List<FinPagrecBanco> getFinPagrecBancos() {
		return this.finPagrecBancos;
	}

	public void setFinPagrecBancos(List<FinPagrecBanco> finPagrecBancos) {
		this.finPagrecBancos = finPagrecBancos;
	}

	public FinPagrecBanco addFinPagrecBanco(FinPagrecBanco finPagrecBanco) {
		getFinPagrecBancos().add(finPagrecBanco);
		finPagrecBanco.setFinConta(this);

		return finPagrecBanco;
	}

	public FinPagrecBanco removeFinPagrecBanco(FinPagrecBanco finPagrecBanco) {
		getFinPagrecBancos().remove(finPagrecBanco);
		finPagrecBanco.setFinConta(null);

		return finPagrecBanco;
	}

	public List<FinPagrecBancoExtrato> getFinPagrecBancoExtratos() {
		return this.finPagrecBancoExtratos;
	}

	public void setFinPagrecBancoExtratos(List<FinPagrecBancoExtrato> finPagrecBancoExtratos) {
		this.finPagrecBancoExtratos = finPagrecBancoExtratos;
	}

	public FinPagrecBancoExtrato addFinPagrecBancoExtrato(FinPagrecBancoExtrato finPagrecBancoExtrato) {
		getFinPagrecBancoExtratos().add(finPagrecBancoExtrato);
		finPagrecBancoExtrato.setFinConta(this);

		return finPagrecBancoExtrato;
	}

	public FinPagrecBancoExtrato removeFinPagrecBancoExtrato(FinPagrecBancoExtrato finPagrecBancoExtrato) {
		getFinPagrecBancoExtratos().remove(finPagrecBancoExtrato);
		finPagrecBancoExtrato.setFinConta(null);

		return finPagrecBancoExtrato;
	}

	public List<FinPagrecBancoTransf> getFinPagrecBancoTransfs1() {
		return this.finPagrecBancoTransfs1;
	}

	public void setFinPagrecBancoTransfs1(List<FinPagrecBancoTransf> finPagrecBancoTransfs1) {
		this.finPagrecBancoTransfs1 = finPagrecBancoTransfs1;
	}

	public FinPagrecBancoTransf addFinPagrecBancoTransfs1(FinPagrecBancoTransf finPagrecBancoTransfs1) {
		getFinPagrecBancoTransfs1().add(finPagrecBancoTransfs1);
		finPagrecBancoTransfs1.setFinConta1(this);

		return finPagrecBancoTransfs1;
	}

	public FinPagrecBancoTransf removeFinPagrecBancoTransfs1(FinPagrecBancoTransf finPagrecBancoTransfs1) {
		getFinPagrecBancoTransfs1().remove(finPagrecBancoTransfs1);
		finPagrecBancoTransfs1.setFinConta1(null);

		return finPagrecBancoTransfs1;
	}

	public List<FinPagrecBancoTransf> getFinPagrecBancoTransfs2() {
		return this.finPagrecBancoTransfs2;
	}

	public void setFinPagrecBancoTransfs2(List<FinPagrecBancoTransf> finPagrecBancoTransfs2) {
		this.finPagrecBancoTransfs2 = finPagrecBancoTransfs2;
	}

	public FinPagrecBancoTransf addFinPagrecBancoTransfs2(FinPagrecBancoTransf finPagrecBancoTransfs2) {
		getFinPagrecBancoTransfs2().add(finPagrecBancoTransfs2);
		finPagrecBancoTransfs2.setFinConta2(this);

		return finPagrecBancoTransfs2;
	}

	public FinPagrecBancoTransf removeFinPagrecBancoTransfs2(FinPagrecBancoTransf finPagrecBancoTransfs2) {
		getFinPagrecBancoTransfs2().remove(finPagrecBancoTransfs2);
		finPagrecBancoTransfs2.setFinConta2(null);

		return finPagrecBancoTransfs2;
	}

}