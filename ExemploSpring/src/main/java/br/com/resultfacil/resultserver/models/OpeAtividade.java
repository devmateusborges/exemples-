package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_atividade")
@NamedQuery(name="OpeAtividade.findAll", query="SELECT o FROM OpeAtividade o")
public class OpeAtividade implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(name="index_bor", length=50)
	private String indexBor;

	@Column(precision=18, scale=6)
	private BigDecimal largura;

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

	@Column(nullable=false, length=1)
	private String parada;

	@Column(name="sigla_atividade", nullable=false, length=50)
	private String siglaAtividade;

	@Column(name="valida_itemserv_i", length=1)
	private String validaItemservI;

	@Column(name="valida_itemserv_s", length=1)
	private String validaItemservS;

	@Column(name="valida_prev_itemserv", length=1)
	private String validaPrevItemserv;

	@Column(name="valida_prev_rec", length=1)
	private String validaPrevRec;

	@Column(name="valida_rec_equip", length=1)
	private String validaRecEquip;

	@Column(name="valida_rec_pessoa", length=1)
	private String validaRecPessoa;

	@Column(name="valida_regra_config", length=1)
	private String validaRegraConfig;

	@Column(name="valida_saldo_area_aberta", length=1)
	private String validaSaldoAreaAberta;

	@Column(name="valida_seq_medicao_trab_centro", length=1)
	private String validaSeqMedicaoTrabCentro;

	@Column(name="valida_tipo_executor", length=2)
	private String validaTipoExecutor;

	@Column(name="valida_tipo_prop_rec_equip", length=2)
	private String validaTipoPropRecEquip;

	@Column(name="valida_tipo_prop_rec_pessoa", length=2)
	private String validaTipoPropRecPessoa;

	@Column(name="valida_tot_area_acum_per_centro_exec", length=1)
	private String validaTotAreaAcumPerCentroExec;

	@Column(name="valida_tot_area_acum_per_centro_plan", length=1)
	private String validaTotAreaAcumPerCentroPlan;

	@Column(name="valida_tot_area_ord_exec", length=1)
	private String validaTotAreaOrdExec;

	//bi-directional many-to-one association to CtbLancDet
	@OneToMany(mappedBy="opeAtividade")
	private List<CtbLancDet> ctbLancDets;

	//bi-directional many-to-one association to FinPagrecPrevDest
	@OneToMany(mappedBy="opeAtividade")
	private List<FinPagrecPrevDest> finPagrecPrevDests;

	//bi-directional many-to-one association to GerUmedida
	@ManyToOne
	@JoinColumn(name="ger_umedida_id", nullable=false)
	private GerUmedida gerUmedida;

	//bi-directional many-to-one association to OpeAtividadeGrupo
	@ManyToOne
	@JoinColumn(name="ope_atividade_grupo_id", nullable=false)
	private OpeAtividadeGrupo opeAtividadeGrupo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeAtividadeRelacProd
	@OneToMany(mappedBy="opeAtividade1")
	private List<OpeAtividadeRelacProd> opeAtividadeRelacProds1;

	//bi-directional many-to-one association to OpeAtividadeRelacProd
	@OneToMany(mappedBy="opeAtividade2")
	private List<OpeAtividadeRelacProd> opeAtividadeRelacProds2;

	//bi-directional many-to-one association to OpeCentro2OrdAtiv
	@OneToMany(mappedBy="opeAtividade")
	private List<OpeCentro2OrdAtiv> opeCentro2OrdAtivs;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="opeAtividade")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="opeAtividade")
	private List<OpeCentroDest> opeCentroDests;

	//bi-directional many-to-one association to OpeCentroPrev
	@OneToMany(mappedBy="opeAtividade")
	private List<OpeCentroPrev> opeCentroPrevs;

	//bi-directional many-to-one association to OpeCentroRend
	@OneToMany(mappedBy="opeAtividade")
	private List<OpeCentroRend> opeCentroRends;

	public OpeAtividade() {
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

	public String getIndexBor() {
		return this.indexBor;
	}

	public void setIndexBor(String indexBor) {
		this.indexBor = indexBor;
	}

	public BigDecimal getLargura() {
		return this.largura;
	}

	public void setLargura(BigDecimal largura) {
		this.largura = largura;
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

	public String getParada() {
		return this.parada;
	}

	public void setParada(String parada) {
		this.parada = parada;
	}

	public String getSiglaAtividade() {
		return this.siglaAtividade;
	}

	public void setSiglaAtividade(String siglaAtividade) {
		this.siglaAtividade = siglaAtividade;
	}

	public String getValidaItemservI() {
		return this.validaItemservI;
	}

	public void setValidaItemservI(String validaItemservI) {
		this.validaItemservI = validaItemservI;
	}

	public String getValidaItemservS() {
		return this.validaItemservS;
	}

	public void setValidaItemservS(String validaItemservS) {
		this.validaItemservS = validaItemservS;
	}

	public String getValidaPrevItemserv() {
		return this.validaPrevItemserv;
	}

	public void setValidaPrevItemserv(String validaPrevItemserv) {
		this.validaPrevItemserv = validaPrevItemserv;
	}

	public String getValidaPrevRec() {
		return this.validaPrevRec;
	}

	public void setValidaPrevRec(String validaPrevRec) {
		this.validaPrevRec = validaPrevRec;
	}

	public String getValidaRecEquip() {
		return this.validaRecEquip;
	}

	public void setValidaRecEquip(String validaRecEquip) {
		this.validaRecEquip = validaRecEquip;
	}

	public String getValidaRecPessoa() {
		return this.validaRecPessoa;
	}

	public void setValidaRecPessoa(String validaRecPessoa) {
		this.validaRecPessoa = validaRecPessoa;
	}

	public String getValidaRegraConfig() {
		return this.validaRegraConfig;
	}

	public void setValidaRegraConfig(String validaRegraConfig) {
		this.validaRegraConfig = validaRegraConfig;
	}

	public String getValidaSaldoAreaAberta() {
		return this.validaSaldoAreaAberta;
	}

	public void setValidaSaldoAreaAberta(String validaSaldoAreaAberta) {
		this.validaSaldoAreaAberta = validaSaldoAreaAberta;
	}

	public String getValidaSeqMedicaoTrabCentro() {
		return this.validaSeqMedicaoTrabCentro;
	}

	public void setValidaSeqMedicaoTrabCentro(String validaSeqMedicaoTrabCentro) {
		this.validaSeqMedicaoTrabCentro = validaSeqMedicaoTrabCentro;
	}

	public String getValidaTipoExecutor() {
		return this.validaTipoExecutor;
	}

	public void setValidaTipoExecutor(String validaTipoExecutor) {
		this.validaTipoExecutor = validaTipoExecutor;
	}

	public String getValidaTipoPropRecEquip() {
		return this.validaTipoPropRecEquip;
	}

	public void setValidaTipoPropRecEquip(String validaTipoPropRecEquip) {
		this.validaTipoPropRecEquip = validaTipoPropRecEquip;
	}

	public String getValidaTipoPropRecPessoa() {
		return this.validaTipoPropRecPessoa;
	}

	public void setValidaTipoPropRecPessoa(String validaTipoPropRecPessoa) {
		this.validaTipoPropRecPessoa = validaTipoPropRecPessoa;
	}

	public String getValidaTotAreaAcumPerCentroExec() {
		return this.validaTotAreaAcumPerCentroExec;
	}

	public void setValidaTotAreaAcumPerCentroExec(String validaTotAreaAcumPerCentroExec) {
		this.validaTotAreaAcumPerCentroExec = validaTotAreaAcumPerCentroExec;
	}

	public String getValidaTotAreaAcumPerCentroPlan() {
		return this.validaTotAreaAcumPerCentroPlan;
	}

	public void setValidaTotAreaAcumPerCentroPlan(String validaTotAreaAcumPerCentroPlan) {
		this.validaTotAreaAcumPerCentroPlan = validaTotAreaAcumPerCentroPlan;
	}

	public String getValidaTotAreaOrdExec() {
		return this.validaTotAreaOrdExec;
	}

	public void setValidaTotAreaOrdExec(String validaTotAreaOrdExec) {
		this.validaTotAreaOrdExec = validaTotAreaOrdExec;
	}

	public List<CtbLancDet> getCtbLancDets() {
		return this.ctbLancDets;
	}

	public void setCtbLancDets(List<CtbLancDet> ctbLancDets) {
		this.ctbLancDets = ctbLancDets;
	}

	public CtbLancDet addCtbLancDet(CtbLancDet ctbLancDet) {
		getCtbLancDets().add(ctbLancDet);
		ctbLancDet.setOpeAtividade(this);

		return ctbLancDet;
	}

	public CtbLancDet removeCtbLancDet(CtbLancDet ctbLancDet) {
		getCtbLancDets().remove(ctbLancDet);
		ctbLancDet.setOpeAtividade(null);

		return ctbLancDet;
	}

	public List<FinPagrecPrevDest> getFinPagrecPrevDests() {
		return this.finPagrecPrevDests;
	}

	public void setFinPagrecPrevDests(List<FinPagrecPrevDest> finPagrecPrevDests) {
		this.finPagrecPrevDests = finPagrecPrevDests;
	}

	public FinPagrecPrevDest addFinPagrecPrevDest(FinPagrecPrevDest finPagrecPrevDest) {
		getFinPagrecPrevDests().add(finPagrecPrevDest);
		finPagrecPrevDest.setOpeAtividade(this);

		return finPagrecPrevDest;
	}

	public FinPagrecPrevDest removeFinPagrecPrevDest(FinPagrecPrevDest finPagrecPrevDest) {
		getFinPagrecPrevDests().remove(finPagrecPrevDest);
		finPagrecPrevDest.setOpeAtividade(null);

		return finPagrecPrevDest;
	}

	public GerUmedida getGerUmedida() {
		return this.gerUmedida;
	}

	public void setGerUmedida(GerUmedida gerUmedida) {
		this.gerUmedida = gerUmedida;
	}

	public OpeAtividadeGrupo getOpeAtividadeGrupo() {
		return this.opeAtividadeGrupo;
	}

	public void setOpeAtividadeGrupo(OpeAtividadeGrupo opeAtividadeGrupo) {
		this.opeAtividadeGrupo = opeAtividadeGrupo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeAtividadeRelacProd> getOpeAtividadeRelacProds1() {
		return this.opeAtividadeRelacProds1;
	}

	public void setOpeAtividadeRelacProds1(List<OpeAtividadeRelacProd> opeAtividadeRelacProds1) {
		this.opeAtividadeRelacProds1 = opeAtividadeRelacProds1;
	}

	public OpeAtividadeRelacProd addOpeAtividadeRelacProds1(OpeAtividadeRelacProd opeAtividadeRelacProds1) {
		getOpeAtividadeRelacProds1().add(opeAtividadeRelacProds1);
		opeAtividadeRelacProds1.setOpeAtividade1(this);

		return opeAtividadeRelacProds1;
	}

	public OpeAtividadeRelacProd removeOpeAtividadeRelacProds1(OpeAtividadeRelacProd opeAtividadeRelacProds1) {
		getOpeAtividadeRelacProds1().remove(opeAtividadeRelacProds1);
		opeAtividadeRelacProds1.setOpeAtividade1(null);

		return opeAtividadeRelacProds1;
	}

	public List<OpeAtividadeRelacProd> getOpeAtividadeRelacProds2() {
		return this.opeAtividadeRelacProds2;
	}

	public void setOpeAtividadeRelacProds2(List<OpeAtividadeRelacProd> opeAtividadeRelacProds2) {
		this.opeAtividadeRelacProds2 = opeAtividadeRelacProds2;
	}

	public OpeAtividadeRelacProd addOpeAtividadeRelacProds2(OpeAtividadeRelacProd opeAtividadeRelacProds2) {
		getOpeAtividadeRelacProds2().add(opeAtividadeRelacProds2);
		opeAtividadeRelacProds2.setOpeAtividade2(this);

		return opeAtividadeRelacProds2;
	}

	public OpeAtividadeRelacProd removeOpeAtividadeRelacProds2(OpeAtividadeRelacProd opeAtividadeRelacProds2) {
		getOpeAtividadeRelacProds2().remove(opeAtividadeRelacProds2);
		opeAtividadeRelacProds2.setOpeAtividade2(null);

		return opeAtividadeRelacProds2;
	}

	public List<OpeCentro2OrdAtiv> getOpeCentro2OrdAtivs() {
		return this.opeCentro2OrdAtivs;
	}

	public void setOpeCentro2OrdAtivs(List<OpeCentro2OrdAtiv> opeCentro2OrdAtivs) {
		this.opeCentro2OrdAtivs = opeCentro2OrdAtivs;
	}

	public OpeCentro2OrdAtiv addOpeCentro2OrdAtiv(OpeCentro2OrdAtiv opeCentro2OrdAtiv) {
		getOpeCentro2OrdAtivs().add(opeCentro2OrdAtiv);
		opeCentro2OrdAtiv.setOpeAtividade(this);

		return opeCentro2OrdAtiv;
	}

	public OpeCentro2OrdAtiv removeOpeCentro2OrdAtiv(OpeCentro2OrdAtiv opeCentro2OrdAtiv) {
		getOpeCentro2OrdAtivs().remove(opeCentro2OrdAtiv);
		opeCentro2OrdAtiv.setOpeAtividade(null);

		return opeCentro2OrdAtiv;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setOpeAtividade(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setOpeAtividade(null);

		return opeCentroConfig;
	}

	public List<OpeCentroDest> getOpeCentroDests() {
		return this.opeCentroDests;
	}

	public void setOpeCentroDests(List<OpeCentroDest> opeCentroDests) {
		this.opeCentroDests = opeCentroDests;
	}

	public OpeCentroDest addOpeCentroDest(OpeCentroDest opeCentroDest) {
		getOpeCentroDests().add(opeCentroDest);
		opeCentroDest.setOpeAtividade(this);

		return opeCentroDest;
	}

	public OpeCentroDest removeOpeCentroDest(OpeCentroDest opeCentroDest) {
		getOpeCentroDests().remove(opeCentroDest);
		opeCentroDest.setOpeAtividade(null);

		return opeCentroDest;
	}

	public List<OpeCentroPrev> getOpeCentroPrevs() {
		return this.opeCentroPrevs;
	}

	public void setOpeCentroPrevs(List<OpeCentroPrev> opeCentroPrevs) {
		this.opeCentroPrevs = opeCentroPrevs;
	}

	public OpeCentroPrev addOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().add(opeCentroPrev);
		opeCentroPrev.setOpeAtividade(this);

		return opeCentroPrev;
	}

	public OpeCentroPrev removeOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().remove(opeCentroPrev);
		opeCentroPrev.setOpeAtividade(null);

		return opeCentroPrev;
	}

	public List<OpeCentroRend> getOpeCentroRends() {
		return this.opeCentroRends;
	}

	public void setOpeCentroRends(List<OpeCentroRend> opeCentroRends) {
		this.opeCentroRends = opeCentroRends;
	}

	public OpeCentroRend addOpeCentroRend(OpeCentroRend opeCentroRend) {
		getOpeCentroRends().add(opeCentroRend);
		opeCentroRend.setOpeAtividade(this);

		return opeCentroRend;
	}

	public OpeCentroRend removeOpeCentroRend(OpeCentroRend opeCentroRend) {
		getOpeCentroRends().remove(opeCentroRend);
		opeCentroRend.setOpeAtividade(null);

		return opeCentroRend;
	}

}