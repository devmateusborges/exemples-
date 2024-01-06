package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.util.Date;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_compart")
@NamedQuery(name="OpeCompart.findAll", query="SELECT o FROM OpeCompart o")
public class OpeCompart implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(nullable=false, precision=18, scale=6)
	private BigDecimal capacidade;

	@Column(name="data_aquisicao", length=255)
	private String dataAquisicao;

	@Column(name="data_baixa", length=255)
	private String dataBaixa;

	@Temporal(TemporalType.DATE)
	@Column(name="data_status")
	private Date dataStatus;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="medicao_trab_centro", nullable=false, length=1)
	private String medicaoTrabCentro;

	@Column(nullable=false, length=100)
	private String nome;

	@Column(name="numero_serie", length=100)
	private String numeroSerie;

	@Column(length=250)
	private String observacao;

	@Column(name="sigla_compart", nullable=false, length=50)
	private String siglaCompart;

	@Column(name="valida_itemserv", nullable=false, length=1)
	private String validaItemserv;

	@Column(name="valor_aquisicao", nullable=false, precision=18, scale=2)
	private BigDecimal valorAquisicao;

	//bi-directional many-to-one association to OpeCentro2MovMedia
	@OneToMany(mappedBy="opeCompart")
	private List<OpeCentro2MovMedia> opeCentro2MovMedias;

	//bi-directional many-to-one association to OpeCentro2OrdRec
	@OneToMany(mappedBy="opeCompart")
	private List<OpeCentro2OrdRec> opeCentro2OrdRecs;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="opeCompart")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="opeCompart1")
	private List<OpeCentroDest> opeCentroDests1;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="opeCompart2")
	private List<OpeCentroDest> opeCentroDests2;

	//bi-directional many-to-one association to OpeCompartStatus
	@ManyToOne
	@JoinColumn(name="ope_compart_status_id")
	private OpeCompartStatus opeCompartStatus;

	//bi-directional many-to-one association to OpeCompartSubgrupo
	@ManyToOne
	@JoinColumn(name="ope_compart_subgrupo_id")
	private OpeCompartSubgrupo opeCompartSubgrupo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCompartItemserv
	@OneToMany(mappedBy="opeCompart")
	private List<OpeCompartItemserv> opeCompartItemservs;

	//bi-directional many-to-one association to OpeOcorCompartMovDet
	@OneToMany(mappedBy="opeCompart")
	private List<OpeOcorCompartMovDet> opeOcorCompartMovDets;

	//bi-directional many-to-one association to OpeOcorMovDest
	@OneToMany(mappedBy="opeCompart")
	private List<OpeOcorMovDest> opeOcorMovDests;

	//bi-directional many-to-one association to OpeOcorPrev
	@OneToMany(mappedBy="opeCompart")
	private List<OpeOcorPrev> opeOcorPrevs;

	//bi-directional many-to-one association to SysDocument
	@OneToMany(mappedBy="opeCompart")
	private List<SysDocument> sysDocuments;

	public OpeCompart() {
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

	public BigDecimal getCapacidade() {
		return this.capacidade;
	}

	public void setCapacidade(BigDecimal capacidade) {
		this.capacidade = capacidade;
	}

	public String getDataAquisicao() {
		return this.dataAquisicao;
	}

	public void setDataAquisicao(String dataAquisicao) {
		this.dataAquisicao = dataAquisicao;
	}

	public String getDataBaixa() {
		return this.dataBaixa;
	}

	public void setDataBaixa(String dataBaixa) {
		this.dataBaixa = dataBaixa;
	}

	public Date getDataStatus() {
		return this.dataStatus;
	}

	public void setDataStatus(Date dataStatus) {
		this.dataStatus = dataStatus;
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

	public String getMedicaoTrabCentro() {
		return this.medicaoTrabCentro;
	}

	public void setMedicaoTrabCentro(String medicaoTrabCentro) {
		this.medicaoTrabCentro = medicaoTrabCentro;
	}

	public String getNome() {
		return this.nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getNumeroSerie() {
		return this.numeroSerie;
	}

	public void setNumeroSerie(String numeroSerie) {
		this.numeroSerie = numeroSerie;
	}

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public String getSiglaCompart() {
		return this.siglaCompart;
	}

	public void setSiglaCompart(String siglaCompart) {
		this.siglaCompart = siglaCompart;
	}

	public String getValidaItemserv() {
		return this.validaItemserv;
	}

	public void setValidaItemserv(String validaItemserv) {
		this.validaItemserv = validaItemserv;
	}

	public BigDecimal getValorAquisicao() {
		return this.valorAquisicao;
	}

	public void setValorAquisicao(BigDecimal valorAquisicao) {
		this.valorAquisicao = valorAquisicao;
	}

	public List<OpeCentro2MovMedia> getOpeCentro2MovMedias() {
		return this.opeCentro2MovMedias;
	}

	public void setOpeCentro2MovMedias(List<OpeCentro2MovMedia> opeCentro2MovMedias) {
		this.opeCentro2MovMedias = opeCentro2MovMedias;
	}

	public OpeCentro2MovMedia addOpeCentro2MovMedia(OpeCentro2MovMedia opeCentro2MovMedia) {
		getOpeCentro2MovMedias().add(opeCentro2MovMedia);
		opeCentro2MovMedia.setOpeCompart(this);

		return opeCentro2MovMedia;
	}

	public OpeCentro2MovMedia removeOpeCentro2MovMedia(OpeCentro2MovMedia opeCentro2MovMedia) {
		getOpeCentro2MovMedias().remove(opeCentro2MovMedia);
		opeCentro2MovMedia.setOpeCompart(null);

		return opeCentro2MovMedia;
	}

	public List<OpeCentro2OrdRec> getOpeCentro2OrdRecs() {
		return this.opeCentro2OrdRecs;
	}

	public void setOpeCentro2OrdRecs(List<OpeCentro2OrdRec> opeCentro2OrdRecs) {
		this.opeCentro2OrdRecs = opeCentro2OrdRecs;
	}

	public OpeCentro2OrdRec addOpeCentro2OrdRec(OpeCentro2OrdRec opeCentro2OrdRec) {
		getOpeCentro2OrdRecs().add(opeCentro2OrdRec);
		opeCentro2OrdRec.setOpeCompart(this);

		return opeCentro2OrdRec;
	}

	public OpeCentro2OrdRec removeOpeCentro2OrdRec(OpeCentro2OrdRec opeCentro2OrdRec) {
		getOpeCentro2OrdRecs().remove(opeCentro2OrdRec);
		opeCentro2OrdRec.setOpeCompart(null);

		return opeCentro2OrdRec;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setOpeCompart(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setOpeCompart(null);

		return opeCentroConfig;
	}

	public List<OpeCentroDest> getOpeCentroDests1() {
		return this.opeCentroDests1;
	}

	public void setOpeCentroDests1(List<OpeCentroDest> opeCentroDests1) {
		this.opeCentroDests1 = opeCentroDests1;
	}

	public OpeCentroDest addOpeCentroDests1(OpeCentroDest opeCentroDests1) {
		getOpeCentroDests1().add(opeCentroDests1);
		opeCentroDests1.setOpeCompart1(this);

		return opeCentroDests1;
	}

	public OpeCentroDest removeOpeCentroDests1(OpeCentroDest opeCentroDests1) {
		getOpeCentroDests1().remove(opeCentroDests1);
		opeCentroDests1.setOpeCompart1(null);

		return opeCentroDests1;
	}

	public List<OpeCentroDest> getOpeCentroDests2() {
		return this.opeCentroDests2;
	}

	public void setOpeCentroDests2(List<OpeCentroDest> opeCentroDests2) {
		this.opeCentroDests2 = opeCentroDests2;
	}

	public OpeCentroDest addOpeCentroDests2(OpeCentroDest opeCentroDests2) {
		getOpeCentroDests2().add(opeCentroDests2);
		opeCentroDests2.setOpeCompart2(this);

		return opeCentroDests2;
	}

	public OpeCentroDest removeOpeCentroDests2(OpeCentroDest opeCentroDests2) {
		getOpeCentroDests2().remove(opeCentroDests2);
		opeCentroDests2.setOpeCompart2(null);

		return opeCentroDests2;
	}

	public OpeCompartStatus getOpeCompartStatus() {
		return this.opeCompartStatus;
	}

	public void setOpeCompartStatus(OpeCompartStatus opeCompartStatus) {
		this.opeCompartStatus = opeCompartStatus;
	}

	public OpeCompartSubgrupo getOpeCompartSubgrupo() {
		return this.opeCompartSubgrupo;
	}

	public void setOpeCompartSubgrupo(OpeCompartSubgrupo opeCompartSubgrupo) {
		this.opeCompartSubgrupo = opeCompartSubgrupo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCompartItemserv> getOpeCompartItemservs() {
		return this.opeCompartItemservs;
	}

	public void setOpeCompartItemservs(List<OpeCompartItemserv> opeCompartItemservs) {
		this.opeCompartItemservs = opeCompartItemservs;
	}

	public OpeCompartItemserv addOpeCompartItemserv(OpeCompartItemserv opeCompartItemserv) {
		getOpeCompartItemservs().add(opeCompartItemserv);
		opeCompartItemserv.setOpeCompart(this);

		return opeCompartItemserv;
	}

	public OpeCompartItemserv removeOpeCompartItemserv(OpeCompartItemserv opeCompartItemserv) {
		getOpeCompartItemservs().remove(opeCompartItemserv);
		opeCompartItemserv.setOpeCompart(null);

		return opeCompartItemserv;
	}

	public List<OpeOcorCompartMovDet> getOpeOcorCompartMovDets() {
		return this.opeOcorCompartMovDets;
	}

	public void setOpeOcorCompartMovDets(List<OpeOcorCompartMovDet> opeOcorCompartMovDets) {
		this.opeOcorCompartMovDets = opeOcorCompartMovDets;
	}

	public OpeOcorCompartMovDet addOpeOcorCompartMovDet(OpeOcorCompartMovDet opeOcorCompartMovDet) {
		getOpeOcorCompartMovDets().add(opeOcorCompartMovDet);
		opeOcorCompartMovDet.setOpeCompart(this);

		return opeOcorCompartMovDet;
	}

	public OpeOcorCompartMovDet removeOpeOcorCompartMovDet(OpeOcorCompartMovDet opeOcorCompartMovDet) {
		getOpeOcorCompartMovDets().remove(opeOcorCompartMovDet);
		opeOcorCompartMovDet.setOpeCompart(null);

		return opeOcorCompartMovDet;
	}

	public List<OpeOcorMovDest> getOpeOcorMovDests() {
		return this.opeOcorMovDests;
	}

	public void setOpeOcorMovDests(List<OpeOcorMovDest> opeOcorMovDests) {
		this.opeOcorMovDests = opeOcorMovDests;
	}

	public OpeOcorMovDest addOpeOcorMovDest(OpeOcorMovDest opeOcorMovDest) {
		getOpeOcorMovDests().add(opeOcorMovDest);
		opeOcorMovDest.setOpeCompart(this);

		return opeOcorMovDest;
	}

	public OpeOcorMovDest removeOpeOcorMovDest(OpeOcorMovDest opeOcorMovDest) {
		getOpeOcorMovDests().remove(opeOcorMovDest);
		opeOcorMovDest.setOpeCompart(null);

		return opeOcorMovDest;
	}

	public List<OpeOcorPrev> getOpeOcorPrevs() {
		return this.opeOcorPrevs;
	}

	public void setOpeOcorPrevs(List<OpeOcorPrev> opeOcorPrevs) {
		this.opeOcorPrevs = opeOcorPrevs;
	}

	public OpeOcorPrev addOpeOcorPrev(OpeOcorPrev opeOcorPrev) {
		getOpeOcorPrevs().add(opeOcorPrev);
		opeOcorPrev.setOpeCompart(this);

		return opeOcorPrev;
	}

	public OpeOcorPrev removeOpeOcorPrev(OpeOcorPrev opeOcorPrev) {
		getOpeOcorPrevs().remove(opeOcorPrev);
		opeOcorPrev.setOpeCompart(null);

		return opeOcorPrev;
	}

	public List<SysDocument> getSysDocuments() {
		return this.sysDocuments;
	}

	public void setSysDocuments(List<SysDocument> sysDocuments) {
		this.sysDocuments = sysDocuments;
	}

	public SysDocument addSysDocument(SysDocument sysDocument) {
		getSysDocuments().add(sysDocument);
		sysDocument.setOpeCompart(this);

		return sysDocument;
	}

	public SysDocument removeSysDocument(SysDocument sysDocument) {
		getSysDocuments().remove(sysDocument);
		sysDocument.setOpeCompart(null);

		return sysDocument;
	}

}