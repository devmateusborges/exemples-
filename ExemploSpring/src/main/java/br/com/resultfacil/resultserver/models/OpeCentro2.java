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
@Table(name="ope_centro2")
@NamedQuery(name="OpeCentro2.findAll", query="SELECT o FROM OpeCentro2 o")
public class OpeCentro2 implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Temporal(TemporalType.DATE)
	@Column(name="data_valid")
	private Date dataValid;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="medicao_trab_centro", length=1)
	private String medicaoTrabCentro;

	@Column(nullable=false, length=100)
	private String nome;

	@Column(length=250)
	private String observacao;

	@Column(name="sigla_centro2", nullable=false, length=50)
	private String siglaCentro2;

	@Column(name="tipo_ctb_comp", length=1)
	private String tipoCtbComp;

	@Column(name="tipo_destinacao", length=1)
	private String tipoDestinacao;

	@Column(name="tipo_prop", length=1)
	private String tipoProp;

	@Column(name="utiliza_compart", nullable=false, length=1)
	private String utilizaCompart;

	@Column(name="valida_seq_medicao_trab_centro", length=1)
	private String validaSeqMedicaoTrabCentro;

	//bi-directional many-to-one association to CtbLancDet
	@OneToMany(mappedBy="opeCentro2")
	private List<CtbLancDet> ctbLancDets;

	//bi-directional many-to-one association to FinPagrecPrevDest
	@OneToMany(mappedBy="opeCentro21")
	private List<FinPagrecPrevDest> finPagrecPrevDests1;

	//bi-directional many-to-one association to FinPagrecPrevDest
	@OneToMany(mappedBy="opeCentro22")
	private List<FinPagrecPrevDest> finPagrecPrevDests2;

	//bi-directional many-to-one association to CtbComp
	@ManyToOne
	@JoinColumn(name="ctb_comp_id")
	private CtbComp ctbComp;

	//bi-directional many-to-one association to GerMarcaModelo
	@ManyToOne
	@JoinColumn(name="ger_marca_modelo_id", nullable=false)
	private GerMarcaModelo gerMarcaModelo;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco;

	//bi-directional many-to-one association to GerUmedida
	@ManyToOne
	@JoinColumn(name="ger_umedida_id")
	private GerUmedida gerUmedida;

	//bi-directional many-to-one association to OpeCentro1
	@ManyToOne
	@JoinColumn(name="ope_centro1_id", nullable=false)
	private OpeCentro1 opeCentro1;

	//bi-directional many-to-one association to OpeCentroRatTipo
	@ManyToOne
	@JoinColumn(name="ope_centro_rat_tipo_id")
	private OpeCentroRatTipo opeCentroRatTipo;

	//bi-directional many-to-one association to OpeCentroSubgrupo
	@ManyToOne
	@JoinColumn(name="ope_centro_subgrupo_id", nullable=false)
	private OpeCentroSubgrupo opeCentroSubgrupo;

	//bi-directional many-to-one association to OpeRegiao
	@ManyToOne
	@JoinColumn(name="ope_regiao_id")
	private OpeRegiao opeRegiao;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCentro2Area
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentro2Area> opeCentro2Areas;

	//bi-directional many-to-one association to OpeCentro2Equip
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentro2Equip> opeCentro2Equips;

	//bi-directional many-to-one association to OpeCentro2Estoque
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentro2Estoque> opeCentro2Estoques;

	//bi-directional many-to-one association to OpeCentro2MovMedia
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentro2MovMedia> opeCentro2MovMedias;

	//bi-directional many-to-one association to OpeCentro2Ord
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentro2Ord> opeCentro2Ords;

	//bi-directional many-to-one association to OpeCentro2OrdDest
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentro2OrdDest> opeCentro2OrdDests;

	//bi-directional many-to-one association to OpeCentro2OrdRec
	@OneToMany(mappedBy="opeCentro21")
	private List<OpeCentro2OrdRec> opeCentro2OrdRecs1;

	//bi-directional many-to-one association to OpeCentro2OrdRec
	@OneToMany(mappedBy="opeCentro22")
	private List<OpeCentro2OrdRec> opeCentro2OrdRecs2;

	//bi-directional many-to-one association to OpeCentro2ParamPer
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentro2ParamPer> opeCentro2ParamPers;

	//bi-directional many-to-one association to OpeCentro2Pessoa
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentro2Pessoa> opeCentro2Pessoas;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="opeCentro21")
	private List<OpeCentroDest> opeCentroDests1;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="opeCentro22")
	private List<OpeCentroDest> opeCentroDests2;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="opeCentro23")
	private List<OpeCentroDest> opeCentroDests3;

	//bi-directional many-to-one association to OpeCentroPrev
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentroPrev> opeCentroPrevs;

	//bi-directional many-to-one association to OpeCentroPrevDest
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentroPrevDest> opeCentroPrevDests;

	//bi-directional many-to-one association to OpeCentroRatFator
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentroRatFator> opeCentroRatFators;

	//bi-directional many-to-one association to OpeCentroRendFator
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeCentroRendFator> opeCentroRendFators;

	//bi-directional many-to-one association to OpeOcorMovDest
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeOcorMovDest> opeOcorMovDests;

	//bi-directional many-to-one association to OpeOcorPrev
	@OneToMany(mappedBy="opeCentro2")
	private List<OpeOcorPrev> opeOcorPrevs;

	//bi-directional many-to-one association to SysDocument
	@OneToMany(mappedBy="opeCentro2")
	private List<SysDocument> sysDocuments;

	public OpeCentro2() {
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

	public Date getDataValid() {
		return this.dataValid;
	}

	public void setDataValid(Date dataValid) {
		this.dataValid = dataValid;
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

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public String getSiglaCentro2() {
		return this.siglaCentro2;
	}

	public void setSiglaCentro2(String siglaCentro2) {
		this.siglaCentro2 = siglaCentro2;
	}

	public String getTipoCtbComp() {
		return this.tipoCtbComp;
	}

	public void setTipoCtbComp(String tipoCtbComp) {
		this.tipoCtbComp = tipoCtbComp;
	}

	public String getTipoDestinacao() {
		return this.tipoDestinacao;
	}

	public void setTipoDestinacao(String tipoDestinacao) {
		this.tipoDestinacao = tipoDestinacao;
	}

	public String getTipoProp() {
		return this.tipoProp;
	}

	public void setTipoProp(String tipoProp) {
		this.tipoProp = tipoProp;
	}

	public String getUtilizaCompart() {
		return this.utilizaCompart;
	}

	public void setUtilizaCompart(String utilizaCompart) {
		this.utilizaCompart = utilizaCompart;
	}

	public String getValidaSeqMedicaoTrabCentro() {
		return this.validaSeqMedicaoTrabCentro;
	}

	public void setValidaSeqMedicaoTrabCentro(String validaSeqMedicaoTrabCentro) {
		this.validaSeqMedicaoTrabCentro = validaSeqMedicaoTrabCentro;
	}

	public List<CtbLancDet> getCtbLancDets() {
		return this.ctbLancDets;
	}

	public void setCtbLancDets(List<CtbLancDet> ctbLancDets) {
		this.ctbLancDets = ctbLancDets;
	}

	public CtbLancDet addCtbLancDet(CtbLancDet ctbLancDet) {
		getCtbLancDets().add(ctbLancDet);
		ctbLancDet.setOpeCentro2(this);

		return ctbLancDet;
	}

	public CtbLancDet removeCtbLancDet(CtbLancDet ctbLancDet) {
		getCtbLancDets().remove(ctbLancDet);
		ctbLancDet.setOpeCentro2(null);

		return ctbLancDet;
	}

	public List<FinPagrecPrevDest> getFinPagrecPrevDests1() {
		return this.finPagrecPrevDests1;
	}

	public void setFinPagrecPrevDests1(List<FinPagrecPrevDest> finPagrecPrevDests1) {
		this.finPagrecPrevDests1 = finPagrecPrevDests1;
	}

	public FinPagrecPrevDest addFinPagrecPrevDests1(FinPagrecPrevDest finPagrecPrevDests1) {
		getFinPagrecPrevDests1().add(finPagrecPrevDests1);
		finPagrecPrevDests1.setOpeCentro21(this);

		return finPagrecPrevDests1;
	}

	public FinPagrecPrevDest removeFinPagrecPrevDests1(FinPagrecPrevDest finPagrecPrevDests1) {
		getFinPagrecPrevDests1().remove(finPagrecPrevDests1);
		finPagrecPrevDests1.setOpeCentro21(null);

		return finPagrecPrevDests1;
	}

	public List<FinPagrecPrevDest> getFinPagrecPrevDests2() {
		return this.finPagrecPrevDests2;
	}

	public void setFinPagrecPrevDests2(List<FinPagrecPrevDest> finPagrecPrevDests2) {
		this.finPagrecPrevDests2 = finPagrecPrevDests2;
	}

	public FinPagrecPrevDest addFinPagrecPrevDests2(FinPagrecPrevDest finPagrecPrevDests2) {
		getFinPagrecPrevDests2().add(finPagrecPrevDests2);
		finPagrecPrevDests2.setOpeCentro22(this);

		return finPagrecPrevDests2;
	}

	public FinPagrecPrevDest removeFinPagrecPrevDests2(FinPagrecPrevDest finPagrecPrevDests2) {
		getFinPagrecPrevDests2().remove(finPagrecPrevDests2);
		finPagrecPrevDests2.setOpeCentro22(null);

		return finPagrecPrevDests2;
	}

	public CtbComp getCtbComp() {
		return this.ctbComp;
	}

	public void setCtbComp(CtbComp ctbComp) {
		this.ctbComp = ctbComp;
	}

	public GerMarcaModelo getGerMarcaModelo() {
		return this.gerMarcaModelo;
	}

	public void setGerMarcaModelo(GerMarcaModelo gerMarcaModelo) {
		this.gerMarcaModelo = gerMarcaModelo;
	}

	public GerPessoaEndereco getGerPessoaEndereco() {
		return this.gerPessoaEndereco;
	}

	public void setGerPessoaEndereco(GerPessoaEndereco gerPessoaEndereco) {
		this.gerPessoaEndereco = gerPessoaEndereco;
	}

	public GerUmedida getGerUmedida() {
		return this.gerUmedida;
	}

	public void setGerUmedida(GerUmedida gerUmedida) {
		this.gerUmedida = gerUmedida;
	}

	public OpeCentro1 getOpeCentro1() {
		return this.opeCentro1;
	}

	public void setOpeCentro1(OpeCentro1 opeCentro1) {
		this.opeCentro1 = opeCentro1;
	}

	public OpeCentroRatTipo getOpeCentroRatTipo() {
		return this.opeCentroRatTipo;
	}

	public void setOpeCentroRatTipo(OpeCentroRatTipo opeCentroRatTipo) {
		this.opeCentroRatTipo = opeCentroRatTipo;
	}

	public OpeCentroSubgrupo getOpeCentroSubgrupo() {
		return this.opeCentroSubgrupo;
	}

	public void setOpeCentroSubgrupo(OpeCentroSubgrupo opeCentroSubgrupo) {
		this.opeCentroSubgrupo = opeCentroSubgrupo;
	}

	public OpeRegiao getOpeRegiao() {
		return this.opeRegiao;
	}

	public void setOpeRegiao(OpeRegiao opeRegiao) {
		this.opeRegiao = opeRegiao;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCentro2Area> getOpeCentro2Areas() {
		return this.opeCentro2Areas;
	}

	public void setOpeCentro2Areas(List<OpeCentro2Area> opeCentro2Areas) {
		this.opeCentro2Areas = opeCentro2Areas;
	}

	public OpeCentro2Area addOpeCentro2Area(OpeCentro2Area opeCentro2Area) {
		getOpeCentro2Areas().add(opeCentro2Area);
		opeCentro2Area.setOpeCentro2(this);

		return opeCentro2Area;
	}

	public OpeCentro2Area removeOpeCentro2Area(OpeCentro2Area opeCentro2Area) {
		getOpeCentro2Areas().remove(opeCentro2Area);
		opeCentro2Area.setOpeCentro2(null);

		return opeCentro2Area;
	}

	public List<OpeCentro2Equip> getOpeCentro2Equips() {
		return this.opeCentro2Equips;
	}

	public void setOpeCentro2Equips(List<OpeCentro2Equip> opeCentro2Equips) {
		this.opeCentro2Equips = opeCentro2Equips;
	}

	public OpeCentro2Equip addOpeCentro2Equip(OpeCentro2Equip opeCentro2Equip) {
		getOpeCentro2Equips().add(opeCentro2Equip);
		opeCentro2Equip.setOpeCentro2(this);

		return opeCentro2Equip;
	}

	public OpeCentro2Equip removeOpeCentro2Equip(OpeCentro2Equip opeCentro2Equip) {
		getOpeCentro2Equips().remove(opeCentro2Equip);
		opeCentro2Equip.setOpeCentro2(null);

		return opeCentro2Equip;
	}

	public List<OpeCentro2Estoque> getOpeCentro2Estoques() {
		return this.opeCentro2Estoques;
	}

	public void setOpeCentro2Estoques(List<OpeCentro2Estoque> opeCentro2Estoques) {
		this.opeCentro2Estoques = opeCentro2Estoques;
	}

	public OpeCentro2Estoque addOpeCentro2Estoque(OpeCentro2Estoque opeCentro2Estoque) {
		getOpeCentro2Estoques().add(opeCentro2Estoque);
		opeCentro2Estoque.setOpeCentro2(this);

		return opeCentro2Estoque;
	}

	public OpeCentro2Estoque removeOpeCentro2Estoque(OpeCentro2Estoque opeCentro2Estoque) {
		getOpeCentro2Estoques().remove(opeCentro2Estoque);
		opeCentro2Estoque.setOpeCentro2(null);

		return opeCentro2Estoque;
	}

	public List<OpeCentro2MovMedia> getOpeCentro2MovMedias() {
		return this.opeCentro2MovMedias;
	}

	public void setOpeCentro2MovMedias(List<OpeCentro2MovMedia> opeCentro2MovMedias) {
		this.opeCentro2MovMedias = opeCentro2MovMedias;
	}

	public OpeCentro2MovMedia addOpeCentro2MovMedia(OpeCentro2MovMedia opeCentro2MovMedia) {
		getOpeCentro2MovMedias().add(opeCentro2MovMedia);
		opeCentro2MovMedia.setOpeCentro2(this);

		return opeCentro2MovMedia;
	}

	public OpeCentro2MovMedia removeOpeCentro2MovMedia(OpeCentro2MovMedia opeCentro2MovMedia) {
		getOpeCentro2MovMedias().remove(opeCentro2MovMedia);
		opeCentro2MovMedia.setOpeCentro2(null);

		return opeCentro2MovMedia;
	}

	public List<OpeCentro2Ord> getOpeCentro2Ords() {
		return this.opeCentro2Ords;
	}

	public void setOpeCentro2Ords(List<OpeCentro2Ord> opeCentro2Ords) {
		this.opeCentro2Ords = opeCentro2Ords;
	}

	public OpeCentro2Ord addOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().add(opeCentro2Ord);
		opeCentro2Ord.setOpeCentro2(this);

		return opeCentro2Ord;
	}

	public OpeCentro2Ord removeOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().remove(opeCentro2Ord);
		opeCentro2Ord.setOpeCentro2(null);

		return opeCentro2Ord;
	}

	public List<OpeCentro2OrdDest> getOpeCentro2OrdDests() {
		return this.opeCentro2OrdDests;
	}

	public void setOpeCentro2OrdDests(List<OpeCentro2OrdDest> opeCentro2OrdDests) {
		this.opeCentro2OrdDests = opeCentro2OrdDests;
	}

	public OpeCentro2OrdDest addOpeCentro2OrdDest(OpeCentro2OrdDest opeCentro2OrdDest) {
		getOpeCentro2OrdDests().add(opeCentro2OrdDest);
		opeCentro2OrdDest.setOpeCentro2(this);

		return opeCentro2OrdDest;
	}

	public OpeCentro2OrdDest removeOpeCentro2OrdDest(OpeCentro2OrdDest opeCentro2OrdDest) {
		getOpeCentro2OrdDests().remove(opeCentro2OrdDest);
		opeCentro2OrdDest.setOpeCentro2(null);

		return opeCentro2OrdDest;
	}

	public List<OpeCentro2OrdRec> getOpeCentro2OrdRecs1() {
		return this.opeCentro2OrdRecs1;
	}

	public void setOpeCentro2OrdRecs1(List<OpeCentro2OrdRec> opeCentro2OrdRecs1) {
		this.opeCentro2OrdRecs1 = opeCentro2OrdRecs1;
	}

	public OpeCentro2OrdRec addOpeCentro2OrdRecs1(OpeCentro2OrdRec opeCentro2OrdRecs1) {
		getOpeCentro2OrdRecs1().add(opeCentro2OrdRecs1);
		opeCentro2OrdRecs1.setOpeCentro21(this);

		return opeCentro2OrdRecs1;
	}

	public OpeCentro2OrdRec removeOpeCentro2OrdRecs1(OpeCentro2OrdRec opeCentro2OrdRecs1) {
		getOpeCentro2OrdRecs1().remove(opeCentro2OrdRecs1);
		opeCentro2OrdRecs1.setOpeCentro21(null);

		return opeCentro2OrdRecs1;
	}

	public List<OpeCentro2OrdRec> getOpeCentro2OrdRecs2() {
		return this.opeCentro2OrdRecs2;
	}

	public void setOpeCentro2OrdRecs2(List<OpeCentro2OrdRec> opeCentro2OrdRecs2) {
		this.opeCentro2OrdRecs2 = opeCentro2OrdRecs2;
	}

	public OpeCentro2OrdRec addOpeCentro2OrdRecs2(OpeCentro2OrdRec opeCentro2OrdRecs2) {
		getOpeCentro2OrdRecs2().add(opeCentro2OrdRecs2);
		opeCentro2OrdRecs2.setOpeCentro22(this);

		return opeCentro2OrdRecs2;
	}

	public OpeCentro2OrdRec removeOpeCentro2OrdRecs2(OpeCentro2OrdRec opeCentro2OrdRecs2) {
		getOpeCentro2OrdRecs2().remove(opeCentro2OrdRecs2);
		opeCentro2OrdRecs2.setOpeCentro22(null);

		return opeCentro2OrdRecs2;
	}

	public List<OpeCentro2ParamPer> getOpeCentro2ParamPers() {
		return this.opeCentro2ParamPers;
	}

	public void setOpeCentro2ParamPers(List<OpeCentro2ParamPer> opeCentro2ParamPers) {
		this.opeCentro2ParamPers = opeCentro2ParamPers;
	}

	public OpeCentro2ParamPer addOpeCentro2ParamPer(OpeCentro2ParamPer opeCentro2ParamPer) {
		getOpeCentro2ParamPers().add(opeCentro2ParamPer);
		opeCentro2ParamPer.setOpeCentro2(this);

		return opeCentro2ParamPer;
	}

	public OpeCentro2ParamPer removeOpeCentro2ParamPer(OpeCentro2ParamPer opeCentro2ParamPer) {
		getOpeCentro2ParamPers().remove(opeCentro2ParamPer);
		opeCentro2ParamPer.setOpeCentro2(null);

		return opeCentro2ParamPer;
	}

	public List<OpeCentro2Pessoa> getOpeCentro2Pessoas() {
		return this.opeCentro2Pessoas;
	}

	public void setOpeCentro2Pessoas(List<OpeCentro2Pessoa> opeCentro2Pessoas) {
		this.opeCentro2Pessoas = opeCentro2Pessoas;
	}

	public OpeCentro2Pessoa addOpeCentro2Pessoa(OpeCentro2Pessoa opeCentro2Pessoa) {
		getOpeCentro2Pessoas().add(opeCentro2Pessoa);
		opeCentro2Pessoa.setOpeCentro2(this);

		return opeCentro2Pessoa;
	}

	public OpeCentro2Pessoa removeOpeCentro2Pessoa(OpeCentro2Pessoa opeCentro2Pessoa) {
		getOpeCentro2Pessoas().remove(opeCentro2Pessoa);
		opeCentro2Pessoa.setOpeCentro2(null);

		return opeCentro2Pessoa;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setOpeCentro2(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setOpeCentro2(null);

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
		opeCentroDests1.setOpeCentro21(this);

		return opeCentroDests1;
	}

	public OpeCentroDest removeOpeCentroDests1(OpeCentroDest opeCentroDests1) {
		getOpeCentroDests1().remove(opeCentroDests1);
		opeCentroDests1.setOpeCentro21(null);

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
		opeCentroDests2.setOpeCentro22(this);

		return opeCentroDests2;
	}

	public OpeCentroDest removeOpeCentroDests2(OpeCentroDest opeCentroDests2) {
		getOpeCentroDests2().remove(opeCentroDests2);
		opeCentroDests2.setOpeCentro22(null);

		return opeCentroDests2;
	}

	public List<OpeCentroDest> getOpeCentroDests3() {
		return this.opeCentroDests3;
	}

	public void setOpeCentroDests3(List<OpeCentroDest> opeCentroDests3) {
		this.opeCentroDests3 = opeCentroDests3;
	}

	public OpeCentroDest addOpeCentroDests3(OpeCentroDest opeCentroDests3) {
		getOpeCentroDests3().add(opeCentroDests3);
		opeCentroDests3.setOpeCentro23(this);

		return opeCentroDests3;
	}

	public OpeCentroDest removeOpeCentroDests3(OpeCentroDest opeCentroDests3) {
		getOpeCentroDests3().remove(opeCentroDests3);
		opeCentroDests3.setOpeCentro23(null);

		return opeCentroDests3;
	}

	public List<OpeCentroPrev> getOpeCentroPrevs() {
		return this.opeCentroPrevs;
	}

	public void setOpeCentroPrevs(List<OpeCentroPrev> opeCentroPrevs) {
		this.opeCentroPrevs = opeCentroPrevs;
	}

	public OpeCentroPrev addOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().add(opeCentroPrev);
		opeCentroPrev.setOpeCentro2(this);

		return opeCentroPrev;
	}

	public OpeCentroPrev removeOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().remove(opeCentroPrev);
		opeCentroPrev.setOpeCentro2(null);

		return opeCentroPrev;
	}

	public List<OpeCentroPrevDest> getOpeCentroPrevDests() {
		return this.opeCentroPrevDests;
	}

	public void setOpeCentroPrevDests(List<OpeCentroPrevDest> opeCentroPrevDests) {
		this.opeCentroPrevDests = opeCentroPrevDests;
	}

	public OpeCentroPrevDest addOpeCentroPrevDest(OpeCentroPrevDest opeCentroPrevDest) {
		getOpeCentroPrevDests().add(opeCentroPrevDest);
		opeCentroPrevDest.setOpeCentro2(this);

		return opeCentroPrevDest;
	}

	public OpeCentroPrevDest removeOpeCentroPrevDest(OpeCentroPrevDest opeCentroPrevDest) {
		getOpeCentroPrevDests().remove(opeCentroPrevDest);
		opeCentroPrevDest.setOpeCentro2(null);

		return opeCentroPrevDest;
	}

	public List<OpeCentroRatFator> getOpeCentroRatFators() {
		return this.opeCentroRatFators;
	}

	public void setOpeCentroRatFators(List<OpeCentroRatFator> opeCentroRatFators) {
		this.opeCentroRatFators = opeCentroRatFators;
	}

	public OpeCentroRatFator addOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().add(opeCentroRatFator);
		opeCentroRatFator.setOpeCentro2(this);

		return opeCentroRatFator;
	}

	public OpeCentroRatFator removeOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().remove(opeCentroRatFator);
		opeCentroRatFator.setOpeCentro2(null);

		return opeCentroRatFator;
	}

	public List<OpeCentroRendFator> getOpeCentroRendFators() {
		return this.opeCentroRendFators;
	}

	public void setOpeCentroRendFators(List<OpeCentroRendFator> opeCentroRendFators) {
		this.opeCentroRendFators = opeCentroRendFators;
	}

	public OpeCentroRendFator addOpeCentroRendFator(OpeCentroRendFator opeCentroRendFator) {
		getOpeCentroRendFators().add(opeCentroRendFator);
		opeCentroRendFator.setOpeCentro2(this);

		return opeCentroRendFator;
	}

	public OpeCentroRendFator removeOpeCentroRendFator(OpeCentroRendFator opeCentroRendFator) {
		getOpeCentroRendFators().remove(opeCentroRendFator);
		opeCentroRendFator.setOpeCentro2(null);

		return opeCentroRendFator;
	}

	public List<OpeOcorMovDest> getOpeOcorMovDests() {
		return this.opeOcorMovDests;
	}

	public void setOpeOcorMovDests(List<OpeOcorMovDest> opeOcorMovDests) {
		this.opeOcorMovDests = opeOcorMovDests;
	}

	public OpeOcorMovDest addOpeOcorMovDest(OpeOcorMovDest opeOcorMovDest) {
		getOpeOcorMovDests().add(opeOcorMovDest);
		opeOcorMovDest.setOpeCentro2(this);

		return opeOcorMovDest;
	}

	public OpeOcorMovDest removeOpeOcorMovDest(OpeOcorMovDest opeOcorMovDest) {
		getOpeOcorMovDests().remove(opeOcorMovDest);
		opeOcorMovDest.setOpeCentro2(null);

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
		opeOcorPrev.setOpeCentro2(this);

		return opeOcorPrev;
	}

	public OpeOcorPrev removeOpeOcorPrev(OpeOcorPrev opeOcorPrev) {
		getOpeOcorPrevs().remove(opeOcorPrev);
		opeOcorPrev.setOpeCentro2(null);

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
		sysDocument.setOpeCentro2(this);

		return sysDocument;
	}

	public SysDocument removeSysDocument(SysDocument sysDocument) {
		getSysDocuments().remove(sysDocument);
		sysDocument.setOpeCentro2(null);

		return sysDocument;
	}

}