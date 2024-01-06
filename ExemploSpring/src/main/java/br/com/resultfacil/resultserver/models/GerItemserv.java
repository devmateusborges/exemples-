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
@Table(name="ger_itemserv")
@NamedQuery(name="GerItemserv.findAll", query="SELECT g FROM GerItemserv g")
public class GerItemserv implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(name="fis_doc_cnae_nfs", length=50)
	private String fisDocCnaeNfs;

	@Column(name="fis_sigla_servico", length=50)
	private String fisSiglaServico;

	@Column(name="fis_sigla_servico_municipio", length=50)
	private String fisSiglaServicoMunicipio;

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

	@Column(name="nome_alternativo", length=100)
	private String nomeAlternativo;

	@Column(name="origem_fiscal", nullable=false)
	private Integer origemFiscal;

	@Column(length=50)
	private String referencia1;

	@Column(length=50)
	private String referencia2;

	@Column(length=50)
	private String referencia3;

	@Column(name="sigla_itemserv", length=15)
	private String siglaItemserv;

	@Column(nullable=false, length=1)
	private String tipo;

	@Column(name="tipo_composicao", length=1)
	private String tipoComposicao;

	@Column(name="tipo_ctb_comp", nullable=false, length=1)
	private String tipoCtbComp;

	//bi-directional many-to-one association to CtbComp
	@ManyToOne
	@JoinColumn(name="ctb_comp_id")
	private CtbComp ctbComp;

	//bi-directional many-to-one association to FisCest
	@ManyToOne
	@JoinColumn(name="fis_cest_id", nullable=false)
	private FisCest fisCest;

	//bi-directional many-to-one association to FisNb
	@ManyToOne
	@JoinColumn(name="fis_nbs_id")
	private FisNbs fisNb;

	//bi-directional many-to-one association to FisNcm
	@ManyToOne
	@JoinColumn(name="fis_ncm_id")
	private FisNcm fisNcm;

	//bi-directional many-to-one association to GerItemservSubgrupo
	@ManyToOne
	@JoinColumn(name="ger_itemserv_subgrupo_id", nullable=false)
	private GerItemservSubgrupo gerItemservSubgrupo;

	//bi-directional many-to-one association to GerUmedida
	@ManyToOne
	@JoinColumn(name="ger_umedida_id", nullable=false)
	private GerUmedida gerUmedida;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to GerItemservBarra
	@OneToMany(mappedBy="gerItemserv")
	private List<GerItemservBarra> gerItemservBarras;

	//bi-directional many-to-one association to GerItemservCompo
	@OneToMany(mappedBy="gerItemserv1")
	private List<GerItemservCompo> gerItemservCompos1;

	//bi-directional many-to-one association to GerItemservCompo
	@OneToMany(mappedBy="gerItemserv2")
	private List<GerItemservCompo> gerItemservCompos2;

	//bi-directional many-to-one association to GerItemservLocal
	@OneToMany(mappedBy="gerItemserv")
	private List<GerItemservLocal> gerItemservLocals;

	//bi-directional many-to-one association to GerItemservPessoa
	@OneToMany(mappedBy="gerItemserv")
	private List<GerItemservPessoa> gerItemservPessoas;

	//bi-directional many-to-one association to MovCotacao
	@OneToMany(mappedBy="gerItemserv")
	private List<MovCotacao> movCotacaos;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerItemserv")
	private List<MovCotacaoAnal> movCotacaoAnals;

	//bi-directional many-to-one association to MovEstNivel
	@OneToMany(mappedBy="gerItemserv")
	private List<MovEstNivel> movEstNivels;

	//bi-directional many-to-one association to MovItemserv
	@OneToMany(mappedBy="gerItemserv")
	private List<MovItemserv> movItemservs;

	//bi-directional many-to-one association to OpeCentro2Area
	@OneToMany(mappedBy="gerItemserv1")
	private List<OpeCentro2Area> opeCentro2Areas1;

	//bi-directional many-to-one association to OpeCentro2Area
	@OneToMany(mappedBy="gerItemserv2")
	private List<OpeCentro2Area> opeCentro2Areas2;

	//bi-directional many-to-one association to OpeCentro2MovMedia
	@OneToMany(mappedBy="gerItemserv")
	private List<OpeCentro2MovMedia> opeCentro2MovMedias;

	//bi-directional many-to-one association to OpeCentro2OrdItemserv
	@OneToMany(mappedBy="gerItemserv")
	private List<OpeCentro2OrdItemserv> opeCentro2OrdItemservs;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="gerItemserv")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to OpeCentroPrevDest
	@OneToMany(mappedBy="gerItemserv")
	private List<OpeCentroPrevDest> opeCentroPrevDests;

	//bi-directional many-to-one association to OpeCentroRendFator
	@OneToMany(mappedBy="gerItemserv")
	private List<OpeCentroRendFator> opeCentroRendFators;

	public GerItemserv() {
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

	public String getFisDocCnaeNfs() {
		return this.fisDocCnaeNfs;
	}

	public void setFisDocCnaeNfs(String fisDocCnaeNfs) {
		this.fisDocCnaeNfs = fisDocCnaeNfs;
	}

	public String getFisSiglaServico() {
		return this.fisSiglaServico;
	}

	public void setFisSiglaServico(String fisSiglaServico) {
		this.fisSiglaServico = fisSiglaServico;
	}

	public String getFisSiglaServicoMunicipio() {
		return this.fisSiglaServicoMunicipio;
	}

	public void setFisSiglaServicoMunicipio(String fisSiglaServicoMunicipio) {
		this.fisSiglaServicoMunicipio = fisSiglaServicoMunicipio;
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

	public String getNomeAlternativo() {
		return this.nomeAlternativo;
	}

	public void setNomeAlternativo(String nomeAlternativo) {
		this.nomeAlternativo = nomeAlternativo;
	}

	public Integer getOrigemFiscal() {
		return this.origemFiscal;
	}

	public void setOrigemFiscal(Integer origemFiscal) {
		this.origemFiscal = origemFiscal;
	}

	public String getReferencia1() {
		return this.referencia1;
	}

	public void setReferencia1(String referencia1) {
		this.referencia1 = referencia1;
	}

	public String getReferencia2() {
		return this.referencia2;
	}

	public void setReferencia2(String referencia2) {
		this.referencia2 = referencia2;
	}

	public String getReferencia3() {
		return this.referencia3;
	}

	public void setReferencia3(String referencia3) {
		this.referencia3 = referencia3;
	}

	public String getSiglaItemserv() {
		return this.siglaItemserv;
	}

	public void setSiglaItemserv(String siglaItemserv) {
		this.siglaItemserv = siglaItemserv;
	}

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public String getTipoComposicao() {
		return this.tipoComposicao;
	}

	public void setTipoComposicao(String tipoComposicao) {
		this.tipoComposicao = tipoComposicao;
	}

	public String getTipoCtbComp() {
		return this.tipoCtbComp;
	}

	public void setTipoCtbComp(String tipoCtbComp) {
		this.tipoCtbComp = tipoCtbComp;
	}

	public CtbComp getCtbComp() {
		return this.ctbComp;
	}

	public void setCtbComp(CtbComp ctbComp) {
		this.ctbComp = ctbComp;
	}

	public FisCest getFisCest() {
		return this.fisCest;
	}

	public void setFisCest(FisCest fisCest) {
		this.fisCest = fisCest;
	}

	public FisNbs getFisNb() {
		return this.fisNb;
	}

	public void setFisNb(FisNbs fisNb) {
		this.fisNb = fisNb;
	}

	public FisNcm getFisNcm() {
		return this.fisNcm;
	}

	public void setFisNcm(FisNcm fisNcm) {
		this.fisNcm = fisNcm;
	}

	public GerItemservSubgrupo getGerItemservSubgrupo() {
		return this.gerItemservSubgrupo;
	}

	public void setGerItemservSubgrupo(GerItemservSubgrupo gerItemservSubgrupo) {
		this.gerItemservSubgrupo = gerItemservSubgrupo;
	}

	public GerUmedida getGerUmedida() {
		return this.gerUmedida;
	}

	public void setGerUmedida(GerUmedida gerUmedida) {
		this.gerUmedida = gerUmedida;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<GerItemservBarra> getGerItemservBarras() {
		return this.gerItemservBarras;
	}

	public void setGerItemservBarras(List<GerItemservBarra> gerItemservBarras) {
		this.gerItemservBarras = gerItemservBarras;
	}

	public GerItemservBarra addGerItemservBarra(GerItemservBarra gerItemservBarra) {
		getGerItemservBarras().add(gerItemservBarra);
		gerItemservBarra.setGerItemserv(this);

		return gerItemservBarra;
	}

	public GerItemservBarra removeGerItemservBarra(GerItemservBarra gerItemservBarra) {
		getGerItemservBarras().remove(gerItemservBarra);
		gerItemservBarra.setGerItemserv(null);

		return gerItemservBarra;
	}

	public List<GerItemservCompo> getGerItemservCompos1() {
		return this.gerItemservCompos1;
	}

	public void setGerItemservCompos1(List<GerItemservCompo> gerItemservCompos1) {
		this.gerItemservCompos1 = gerItemservCompos1;
	}

	public GerItemservCompo addGerItemservCompos1(GerItemservCompo gerItemservCompos1) {
		getGerItemservCompos1().add(gerItemservCompos1);
		gerItemservCompos1.setGerItemserv1(this);

		return gerItemservCompos1;
	}

	public GerItemservCompo removeGerItemservCompos1(GerItemservCompo gerItemservCompos1) {
		getGerItemservCompos1().remove(gerItemservCompos1);
		gerItemservCompos1.setGerItemserv1(null);

		return gerItemservCompos1;
	}

	public List<GerItemservCompo> getGerItemservCompos2() {
		return this.gerItemservCompos2;
	}

	public void setGerItemservCompos2(List<GerItemservCompo> gerItemservCompos2) {
		this.gerItemservCompos2 = gerItemservCompos2;
	}

	public GerItemservCompo addGerItemservCompos2(GerItemservCompo gerItemservCompos2) {
		getGerItemservCompos2().add(gerItemservCompos2);
		gerItemservCompos2.setGerItemserv2(this);

		return gerItemservCompos2;
	}

	public GerItemservCompo removeGerItemservCompos2(GerItemservCompo gerItemservCompos2) {
		getGerItemservCompos2().remove(gerItemservCompos2);
		gerItemservCompos2.setGerItemserv2(null);

		return gerItemservCompos2;
	}

	public List<GerItemservLocal> getGerItemservLocals() {
		return this.gerItemservLocals;
	}

	public void setGerItemservLocals(List<GerItemservLocal> gerItemservLocals) {
		this.gerItemservLocals = gerItemservLocals;
	}

	public GerItemservLocal addGerItemservLocal(GerItemservLocal gerItemservLocal) {
		getGerItemservLocals().add(gerItemservLocal);
		gerItemservLocal.setGerItemserv(this);

		return gerItemservLocal;
	}

	public GerItemservLocal removeGerItemservLocal(GerItemservLocal gerItemservLocal) {
		getGerItemservLocals().remove(gerItemservLocal);
		gerItemservLocal.setGerItemserv(null);

		return gerItemservLocal;
	}

	public List<GerItemservPessoa> getGerItemservPessoas() {
		return this.gerItemservPessoas;
	}

	public void setGerItemservPessoas(List<GerItemservPessoa> gerItemservPessoas) {
		this.gerItemservPessoas = gerItemservPessoas;
	}

	public GerItemservPessoa addGerItemservPessoa(GerItemservPessoa gerItemservPessoa) {
		getGerItemservPessoas().add(gerItemservPessoa);
		gerItemservPessoa.setGerItemserv(this);

		return gerItemservPessoa;
	}

	public GerItemservPessoa removeGerItemservPessoa(GerItemservPessoa gerItemservPessoa) {
		getGerItemservPessoas().remove(gerItemservPessoa);
		gerItemservPessoa.setGerItemserv(null);

		return gerItemservPessoa;
	}

	public List<MovCotacao> getMovCotacaos() {
		return this.movCotacaos;
	}

	public void setMovCotacaos(List<MovCotacao> movCotacaos) {
		this.movCotacaos = movCotacaos;
	}

	public MovCotacao addMovCotacao(MovCotacao movCotacao) {
		getMovCotacaos().add(movCotacao);
		movCotacao.setGerItemserv(this);

		return movCotacao;
	}

	public MovCotacao removeMovCotacao(MovCotacao movCotacao) {
		getMovCotacaos().remove(movCotacao);
		movCotacao.setGerItemserv(null);

		return movCotacao;
	}

	public List<MovCotacaoAnal> getMovCotacaoAnals() {
		return this.movCotacaoAnals;
	}

	public void setMovCotacaoAnals(List<MovCotacaoAnal> movCotacaoAnals) {
		this.movCotacaoAnals = movCotacaoAnals;
	}

	public MovCotacaoAnal addMovCotacaoAnal(MovCotacaoAnal movCotacaoAnal) {
		getMovCotacaoAnals().add(movCotacaoAnal);
		movCotacaoAnal.setGerItemserv(this);

		return movCotacaoAnal;
	}

	public MovCotacaoAnal removeMovCotacaoAnal(MovCotacaoAnal movCotacaoAnal) {
		getMovCotacaoAnals().remove(movCotacaoAnal);
		movCotacaoAnal.setGerItemserv(null);

		return movCotacaoAnal;
	}

	public List<MovEstNivel> getMovEstNivels() {
		return this.movEstNivels;
	}

	public void setMovEstNivels(List<MovEstNivel> movEstNivels) {
		this.movEstNivels = movEstNivels;
	}

	public MovEstNivel addMovEstNivel(MovEstNivel movEstNivel) {
		getMovEstNivels().add(movEstNivel);
		movEstNivel.setGerItemserv(this);

		return movEstNivel;
	}

	public MovEstNivel removeMovEstNivel(MovEstNivel movEstNivel) {
		getMovEstNivels().remove(movEstNivel);
		movEstNivel.setGerItemserv(null);

		return movEstNivel;
	}

	public List<MovItemserv> getMovItemservs() {
		return this.movItemservs;
	}

	public void setMovItemservs(List<MovItemserv> movItemservs) {
		this.movItemservs = movItemservs;
	}

	public MovItemserv addMovItemserv(MovItemserv movItemserv) {
		getMovItemservs().add(movItemserv);
		movItemserv.setGerItemserv(this);

		return movItemserv;
	}

	public MovItemserv removeMovItemserv(MovItemserv movItemserv) {
		getMovItemservs().remove(movItemserv);
		movItemserv.setGerItemserv(null);

		return movItemserv;
	}

	public List<OpeCentro2Area> getOpeCentro2Areas1() {
		return this.opeCentro2Areas1;
	}

	public void setOpeCentro2Areas1(List<OpeCentro2Area> opeCentro2Areas1) {
		this.opeCentro2Areas1 = opeCentro2Areas1;
	}

	public OpeCentro2Area addOpeCentro2Areas1(OpeCentro2Area opeCentro2Areas1) {
		getOpeCentro2Areas1().add(opeCentro2Areas1);
		opeCentro2Areas1.setGerItemserv1(this);

		return opeCentro2Areas1;
	}

	public OpeCentro2Area removeOpeCentro2Areas1(OpeCentro2Area opeCentro2Areas1) {
		getOpeCentro2Areas1().remove(opeCentro2Areas1);
		opeCentro2Areas1.setGerItemserv1(null);

		return opeCentro2Areas1;
	}

	public List<OpeCentro2Area> getOpeCentro2Areas2() {
		return this.opeCentro2Areas2;
	}

	public void setOpeCentro2Areas2(List<OpeCentro2Area> opeCentro2Areas2) {
		this.opeCentro2Areas2 = opeCentro2Areas2;
	}

	public OpeCentro2Area addOpeCentro2Areas2(OpeCentro2Area opeCentro2Areas2) {
		getOpeCentro2Areas2().add(opeCentro2Areas2);
		opeCentro2Areas2.setGerItemserv2(this);

		return opeCentro2Areas2;
	}

	public OpeCentro2Area removeOpeCentro2Areas2(OpeCentro2Area opeCentro2Areas2) {
		getOpeCentro2Areas2().remove(opeCentro2Areas2);
		opeCentro2Areas2.setGerItemserv2(null);

		return opeCentro2Areas2;
	}

	public List<OpeCentro2MovMedia> getOpeCentro2MovMedias() {
		return this.opeCentro2MovMedias;
	}

	public void setOpeCentro2MovMedias(List<OpeCentro2MovMedia> opeCentro2MovMedias) {
		this.opeCentro2MovMedias = opeCentro2MovMedias;
	}

	public OpeCentro2MovMedia addOpeCentro2MovMedia(OpeCentro2MovMedia opeCentro2MovMedia) {
		getOpeCentro2MovMedias().add(opeCentro2MovMedia);
		opeCentro2MovMedia.setGerItemserv(this);

		return opeCentro2MovMedia;
	}

	public OpeCentro2MovMedia removeOpeCentro2MovMedia(OpeCentro2MovMedia opeCentro2MovMedia) {
		getOpeCentro2MovMedias().remove(opeCentro2MovMedia);
		opeCentro2MovMedia.setGerItemserv(null);

		return opeCentro2MovMedia;
	}

	public List<OpeCentro2OrdItemserv> getOpeCentro2OrdItemservs() {
		return this.opeCentro2OrdItemservs;
	}

	public void setOpeCentro2OrdItemservs(List<OpeCentro2OrdItemserv> opeCentro2OrdItemservs) {
		this.opeCentro2OrdItemservs = opeCentro2OrdItemservs;
	}

	public OpeCentro2OrdItemserv addOpeCentro2OrdItemserv(OpeCentro2OrdItemserv opeCentro2OrdItemserv) {
		getOpeCentro2OrdItemservs().add(opeCentro2OrdItemserv);
		opeCentro2OrdItemserv.setGerItemserv(this);

		return opeCentro2OrdItemserv;
	}

	public OpeCentro2OrdItemserv removeOpeCentro2OrdItemserv(OpeCentro2OrdItemserv opeCentro2OrdItemserv) {
		getOpeCentro2OrdItemservs().remove(opeCentro2OrdItemserv);
		opeCentro2OrdItemserv.setGerItemserv(null);

		return opeCentro2OrdItemserv;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setGerItemserv(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setGerItemserv(null);

		return opeCentroConfig;
	}

	public List<OpeCentroPrevDest> getOpeCentroPrevDests() {
		return this.opeCentroPrevDests;
	}

	public void setOpeCentroPrevDests(List<OpeCentroPrevDest> opeCentroPrevDests) {
		this.opeCentroPrevDests = opeCentroPrevDests;
	}

	public OpeCentroPrevDest addOpeCentroPrevDest(OpeCentroPrevDest opeCentroPrevDest) {
		getOpeCentroPrevDests().add(opeCentroPrevDest);
		opeCentroPrevDest.setGerItemserv(this);

		return opeCentroPrevDest;
	}

	public OpeCentroPrevDest removeOpeCentroPrevDest(OpeCentroPrevDest opeCentroPrevDest) {
		getOpeCentroPrevDests().remove(opeCentroPrevDest);
		opeCentroPrevDest.setGerItemserv(null);

		return opeCentroPrevDest;
	}

	public List<OpeCentroRendFator> getOpeCentroRendFators() {
		return this.opeCentroRendFators;
	}

	public void setOpeCentroRendFators(List<OpeCentroRendFator> opeCentroRendFators) {
		this.opeCentroRendFators = opeCentroRendFators;
	}

	public OpeCentroRendFator addOpeCentroRendFator(OpeCentroRendFator opeCentroRendFator) {
		getOpeCentroRendFators().add(opeCentroRendFator);
		opeCentroRendFator.setGerItemserv(this);

		return opeCentroRendFator;
	}

	public OpeCentroRendFator removeOpeCentroRendFator(OpeCentroRendFator opeCentroRendFator) {
		getOpeCentroRendFators().remove(opeCentroRendFator);
		opeCentroRendFator.setGerItemserv(null);

		return opeCentroRendFator;
	}

}