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
@Table(name="fin_pagrec_versao")
@NamedQuery(name="FinPagrecVersao.findAll", query="SELECT f FROM FinPagrecVersao f")
public class FinPagrecVersao implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Temporal(TemporalType.DATE)
	@Column(name="data_per_fin", nullable=false)
	private Date dataPerFin;

	@Temporal(TemporalType.DATE)
	@Column(name="data_per_ini", nullable=false)
	private Date dataPerIni;

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

	@Column(name="tipo_per", nullable=false, length=1)
	private String tipoPer;

	@Column(name="versao_atual", nullable=false, length=1)
	private String versaoAtual;

	//bi-directional many-to-one association to FinPagrecPrev
	@OneToMany(mappedBy="finPagrecVersao")
	private List<FinPagrecPrev> finPagrecPrevs;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public FinPagrecVersao() {
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

	public Date getDataPerFin() {
		return this.dataPerFin;
	}

	public void setDataPerFin(Date dataPerFin) {
		this.dataPerFin = dataPerFin;
	}

	public Date getDataPerIni() {
		return this.dataPerIni;
	}

	public void setDataPerIni(Date dataPerIni) {
		this.dataPerIni = dataPerIni;
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

	public String getTipoPer() {
		return this.tipoPer;
	}

	public void setTipoPer(String tipoPer) {
		this.tipoPer = tipoPer;
	}

	public String getVersaoAtual() {
		return this.versaoAtual;
	}

	public void setVersaoAtual(String versaoAtual) {
		this.versaoAtual = versaoAtual;
	}

	public List<FinPagrecPrev> getFinPagrecPrevs() {
		return this.finPagrecPrevs;
	}

	public void setFinPagrecPrevs(List<FinPagrecPrev> finPagrecPrevs) {
		this.finPagrecPrevs = finPagrecPrevs;
	}

	public FinPagrecPrev addFinPagrecPrev(FinPagrecPrev finPagrecPrev) {
		getFinPagrecPrevs().add(finPagrecPrev);
		finPagrecPrev.setFinPagrecVersao(this);

		return finPagrecPrev;
	}

	public FinPagrecPrev removeFinPagrecPrev(FinPagrecPrev finPagrecPrev) {
		getFinPagrecPrevs().remove(finPagrecPrev);
		finPagrecPrev.setFinPagrecVersao(null);

		return finPagrecPrev;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}