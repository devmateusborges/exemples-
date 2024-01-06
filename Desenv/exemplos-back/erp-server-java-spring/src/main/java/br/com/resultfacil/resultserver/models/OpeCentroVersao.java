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
@Table(name="ope_centro_versao")
@NamedQuery(name="OpeCentroVersao.findAll", query="SELECT o FROM OpeCentroVersao o")
public class OpeCentroVersao implements Serializable {
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

	//bi-directional many-to-one association to OpeCentro2Ord
	@OneToMany(mappedBy="opeCentroVersao")
	private List<OpeCentro2Ord> opeCentro2Ords;

	//bi-directional many-to-one association to OpeCentroPrev
	@OneToMany(mappedBy="opeCentroVersao")
	private List<OpeCentroPrev> opeCentroPrevs;

	//bi-directional many-to-one association to OpeCentroRatTipo
	@OneToMany(mappedBy="opeCentroVersao")
	private List<OpeCentroRatTipo> opeCentroRatTipos;

	//bi-directional many-to-one association to OpeCentroRend
	@OneToMany(mappedBy="opeCentroVersao")
	private List<OpeCentroRend> opeCentroRends;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentroVersao() {
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

	public List<OpeCentro2Ord> getOpeCentro2Ords() {
		return this.opeCentro2Ords;
	}

	public void setOpeCentro2Ords(List<OpeCentro2Ord> opeCentro2Ords) {
		this.opeCentro2Ords = opeCentro2Ords;
	}

	public OpeCentro2Ord addOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().add(opeCentro2Ord);
		opeCentro2Ord.setOpeCentroVersao(this);

		return opeCentro2Ord;
	}

	public OpeCentro2Ord removeOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().remove(opeCentro2Ord);
		opeCentro2Ord.setOpeCentroVersao(null);

		return opeCentro2Ord;
	}

	public List<OpeCentroPrev> getOpeCentroPrevs() {
		return this.opeCentroPrevs;
	}

	public void setOpeCentroPrevs(List<OpeCentroPrev> opeCentroPrevs) {
		this.opeCentroPrevs = opeCentroPrevs;
	}

	public OpeCentroPrev addOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().add(opeCentroPrev);
		opeCentroPrev.setOpeCentroVersao(this);

		return opeCentroPrev;
	}

	public OpeCentroPrev removeOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().remove(opeCentroPrev);
		opeCentroPrev.setOpeCentroVersao(null);

		return opeCentroPrev;
	}

	public List<OpeCentroRatTipo> getOpeCentroRatTipos() {
		return this.opeCentroRatTipos;
	}

	public void setOpeCentroRatTipos(List<OpeCentroRatTipo> opeCentroRatTipos) {
		this.opeCentroRatTipos = opeCentroRatTipos;
	}

	public OpeCentroRatTipo addOpeCentroRatTipo(OpeCentroRatTipo opeCentroRatTipo) {
		getOpeCentroRatTipos().add(opeCentroRatTipo);
		opeCentroRatTipo.setOpeCentroVersao(this);

		return opeCentroRatTipo;
	}

	public OpeCentroRatTipo removeOpeCentroRatTipo(OpeCentroRatTipo opeCentroRatTipo) {
		getOpeCentroRatTipos().remove(opeCentroRatTipo);
		opeCentroRatTipo.setOpeCentroVersao(null);

		return opeCentroRatTipo;
	}

	public List<OpeCentroRend> getOpeCentroRends() {
		return this.opeCentroRends;
	}

	public void setOpeCentroRends(List<OpeCentroRend> opeCentroRends) {
		this.opeCentroRends = opeCentroRends;
	}

	public OpeCentroRend addOpeCentroRend(OpeCentroRend opeCentroRend) {
		getOpeCentroRends().add(opeCentroRend);
		opeCentroRend.setOpeCentroVersao(this);

		return opeCentroRend;
	}

	public OpeCentroRend removeOpeCentroRend(OpeCentroRend opeCentroRend) {
		getOpeCentroRends().remove(opeCentroRend);
		opeCentroRend.setOpeCentroVersao(null);

		return opeCentroRend;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}