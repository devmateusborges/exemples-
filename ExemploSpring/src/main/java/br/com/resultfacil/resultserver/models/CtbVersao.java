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
@Table(name="ctb_versao")
@NamedQuery(name="CtbVersao.findAll", query="SELECT c FROM CtbVersao c")
public class CtbVersao implements Serializable {
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

	@Column(name="tipo_rp", nullable=false, length=1)
	private String tipoRp;

	@Column(name="unit_id", nullable=false, length=36)
	private String unitId;

	@Column(name="versao_atual", nullable=false, length=2147483647)
	private String versaoAtual;

	//bi-directional many-to-one association to CtbLanc
	@OneToMany(mappedBy="ctbVersao")
	private List<CtbLanc> ctbLancs;

	public CtbVersao() {
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

	public String getTipoRp() {
		return this.tipoRp;
	}

	public void setTipoRp(String tipoRp) {
		this.tipoRp = tipoRp;
	}

	public String getUnitId() {
		return this.unitId;
	}

	public void setUnitId(String unitId) {
		this.unitId = unitId;
	}

	public String getVersaoAtual() {
		return this.versaoAtual;
	}

	public void setVersaoAtual(String versaoAtual) {
		this.versaoAtual = versaoAtual;
	}

	public List<CtbLanc> getCtbLancs() {
		return this.ctbLancs;
	}

	public void setCtbLancs(List<CtbLanc> ctbLancs) {
		this.ctbLancs = ctbLancs;
	}

	public CtbLanc addCtbLanc(CtbLanc ctbLanc) {
		getCtbLancs().add(ctbLanc);
		ctbLanc.setCtbVersao(this);

		return ctbLanc;
	}

	public CtbLanc removeCtbLanc(CtbLanc ctbLanc) {
		getCtbLancs().remove(ctbLanc);
		ctbLanc.setCtbVersao(null);

		return ctbLanc;
	}

}