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
@Table(name="mov_itemserv")
@NamedQuery(name="MovItemserv.findAll", query="SELECT m FROM MovItemserv m")
public class MovItemserv implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_valid")
	private Date dataValid;

	@Column(name="fis_doc_cnae_nfs", length=50)
	private String fisDocCnaeNfs;

	@Column(name="fis_numero_proc_susp_nfs", length=50)
	private String fisNumeroProcSuspNfs;

	@Column(name="fis_obra_art", length=50)
	private String fisObraArt;

	@Column(name="fis_obra_cei", length=50)
	private String fisObraCei;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="nome_itemserv", length=250)
	private String nomeItemserv;

	@Column(length=250)
	private String observacao;

	@Column(name="qnt_altura", precision=18, scale=6)
	private BigDecimal qntAltura;

	@Column(name="qnt_comprimento", precision=18, scale=6)
	private BigDecimal qntComprimento;

	@Column(name="qnt_conv", nullable=false, precision=18, scale=6)
	private BigDecimal qntConv;

	@Column(name="qnt_devolvida", nullable=false, precision=18, scale=6)
	private BigDecimal qntDevolvida;

	@Column(name="qnt_largura", precision=18, scale=6)
	private BigDecimal qntLargura;

	@Column(name="qnt_min_pessoa_cot")
	private Integer qntMinPessoaCot;

	@Column(name="qnt_orig", nullable=false, precision=18, scale=6)
	private BigDecimal qntOrig;

	@Column(name="valor_acrecimo", nullable=false, precision=18, scale=6)
	private BigDecimal valorAcrecimo;

	@Column(name="valor_bruto", nullable=false, precision=18, scale=6)
	private BigDecimal valorBruto;

	@Column(name="valor_deducao", precision=18, scale=6)
	private BigDecimal valorDeducao;

	@Column(name="valor_desconto", nullable=false, precision=18, scale=6)
	private BigDecimal valorDesconto;

	@Column(name="valor_desconto_cond", precision=18, scale=6)
	private BigDecimal valorDescontoCond;

	@Column(name="valor_desconto_incond", precision=18, scale=6)
	private BigDecimal valorDescontoIncond;

	@Column(name="valor_frete", nullable=false, precision=18, scale=6)
	private BigDecimal valorFrete;

	@Column(name="valor_liquido", nullable=false, precision=18, scale=6)
	private BigDecimal valorLiquido;

	@Column(name="valor_outros", nullable=false, precision=18, scale=6)
	private BigDecimal valorOutros;

	@Column(name="valor_outros_tributo_ret", precision=18, scale=6)
	private BigDecimal valorOutrosTributoRet;

	@Column(name="valor_seguro", nullable=false, precision=18, scale=6)
	private BigDecimal valorSeguro;

	@Column(name="valor_tributo_retido", nullable=false, precision=18, scale=6)
	private BigDecimal valorTributoRetido;

	@Column(name="valor_tributo_total", precision=18, scale=6)
	private BigDecimal valorTributoTotal;

	@Column(name="valor_unit_conv", nullable=false, precision=18, scale=6)
	private BigDecimal valorUnitConv;

	@Column(name="valor_unit_orig", nullable=false, precision=18, scale=6)
	private BigDecimal valorUnitOrig;

	//bi-directional many-to-one association to FisTributacao
	@OneToMany(mappedBy="movItemserv")
	private List<FisTributacao> fisTributacaos;

	//bi-directional many-to-one association to FisCfop
	@ManyToOne
	@JoinColumn(name="fis_cfop_id")
	private FisCfop fisCfop;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id", nullable=false)
	private GerItemserv gerItemserv;

	//bi-directional many-to-one association to GerItemservLote
	@ManyToOne
	@JoinColumn(name="ger_itemserv_lote_id")
	private GerItemservLote gerItemservLote;

	//bi-directional many-to-one association to GerItemservVar
	@ManyToOne
	@JoinColumn(name="ger_itemserv_var_id")
	private GerItemservVar gerItemservVar;

	//bi-directional many-to-one association to GerUmedida
	@ManyToOne
	@JoinColumn(name="ger_umedida_id_conv", nullable=false)
	private GerUmedida gerUmedida;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id", nullable=false)
	private Mov mov;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to MovOrigem
	@OneToMany(mappedBy="movItemserv1")
	private List<MovOrigem> movOrigems1;

	//bi-directional many-to-one association to MovOrigem
	@OneToMany(mappedBy="movItemserv2")
	private List<MovOrigem> movOrigems2;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="movItemserv")
	private List<OpeCentroDest> opeCentroDests;

	public MovItemserv() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataValid() {
		return this.dataValid;
	}

	public void setDataValid(Date dataValid) {
		this.dataValid = dataValid;
	}

	public String getFisDocCnaeNfs() {
		return this.fisDocCnaeNfs;
	}

	public void setFisDocCnaeNfs(String fisDocCnaeNfs) {
		this.fisDocCnaeNfs = fisDocCnaeNfs;
	}

	public String getFisNumeroProcSuspNfs() {
		return this.fisNumeroProcSuspNfs;
	}

	public void setFisNumeroProcSuspNfs(String fisNumeroProcSuspNfs) {
		this.fisNumeroProcSuspNfs = fisNumeroProcSuspNfs;
	}

	public String getFisObraArt() {
		return this.fisObraArt;
	}

	public void setFisObraArt(String fisObraArt) {
		this.fisObraArt = fisObraArt;
	}

	public String getFisObraCei() {
		return this.fisObraCei;
	}

	public void setFisObraCei(String fisObraCei) {
		this.fisObraCei = fisObraCei;
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

	public String getNomeItemserv() {
		return this.nomeItemserv;
	}

	public void setNomeItemserv(String nomeItemserv) {
		this.nomeItemserv = nomeItemserv;
	}

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public BigDecimal getQntAltura() {
		return this.qntAltura;
	}

	public void setQntAltura(BigDecimal qntAltura) {
		this.qntAltura = qntAltura;
	}

	public BigDecimal getQntComprimento() {
		return this.qntComprimento;
	}

	public void setQntComprimento(BigDecimal qntComprimento) {
		this.qntComprimento = qntComprimento;
	}

	public BigDecimal getQntConv() {
		return this.qntConv;
	}

	public void setQntConv(BigDecimal qntConv) {
		this.qntConv = qntConv;
	}

	public BigDecimal getQntDevolvida() {
		return this.qntDevolvida;
	}

	public void setQntDevolvida(BigDecimal qntDevolvida) {
		this.qntDevolvida = qntDevolvida;
	}

	public BigDecimal getQntLargura() {
		return this.qntLargura;
	}

	public void setQntLargura(BigDecimal qntLargura) {
		this.qntLargura = qntLargura;
	}

	public Integer getQntMinPessoaCot() {
		return this.qntMinPessoaCot;
	}

	public void setQntMinPessoaCot(Integer qntMinPessoaCot) {
		this.qntMinPessoaCot = qntMinPessoaCot;
	}

	public BigDecimal getQntOrig() {
		return this.qntOrig;
	}

	public void setQntOrig(BigDecimal qntOrig) {
		this.qntOrig = qntOrig;
	}

	public BigDecimal getValorAcrecimo() {
		return this.valorAcrecimo;
	}

	public void setValorAcrecimo(BigDecimal valorAcrecimo) {
		this.valorAcrecimo = valorAcrecimo;
	}

	public BigDecimal getValorBruto() {
		return this.valorBruto;
	}

	public void setValorBruto(BigDecimal valorBruto) {
		this.valorBruto = valorBruto;
	}

	public BigDecimal getValorDeducao() {
		return this.valorDeducao;
	}

	public void setValorDeducao(BigDecimal valorDeducao) {
		this.valorDeducao = valorDeducao;
	}

	public BigDecimal getValorDesconto() {
		return this.valorDesconto;
	}

	public void setValorDesconto(BigDecimal valorDesconto) {
		this.valorDesconto = valorDesconto;
	}

	public BigDecimal getValorDescontoCond() {
		return this.valorDescontoCond;
	}

	public void setValorDescontoCond(BigDecimal valorDescontoCond) {
		this.valorDescontoCond = valorDescontoCond;
	}

	public BigDecimal getValorDescontoIncond() {
		return this.valorDescontoIncond;
	}

	public void setValorDescontoIncond(BigDecimal valorDescontoIncond) {
		this.valorDescontoIncond = valorDescontoIncond;
	}

	public BigDecimal getValorFrete() {
		return this.valorFrete;
	}

	public void setValorFrete(BigDecimal valorFrete) {
		this.valorFrete = valorFrete;
	}

	public BigDecimal getValorLiquido() {
		return this.valorLiquido;
	}

	public void setValorLiquido(BigDecimal valorLiquido) {
		this.valorLiquido = valorLiquido;
	}

	public BigDecimal getValorOutros() {
		return this.valorOutros;
	}

	public void setValorOutros(BigDecimal valorOutros) {
		this.valorOutros = valorOutros;
	}

	public BigDecimal getValorOutrosTributoRet() {
		return this.valorOutrosTributoRet;
	}

	public void setValorOutrosTributoRet(BigDecimal valorOutrosTributoRet) {
		this.valorOutrosTributoRet = valorOutrosTributoRet;
	}

	public BigDecimal getValorSeguro() {
		return this.valorSeguro;
	}

	public void setValorSeguro(BigDecimal valorSeguro) {
		this.valorSeguro = valorSeguro;
	}

	public BigDecimal getValorTributoRetido() {
		return this.valorTributoRetido;
	}

	public void setValorTributoRetido(BigDecimal valorTributoRetido) {
		this.valorTributoRetido = valorTributoRetido;
	}

	public BigDecimal getValorTributoTotal() {
		return this.valorTributoTotal;
	}

	public void setValorTributoTotal(BigDecimal valorTributoTotal) {
		this.valorTributoTotal = valorTributoTotal;
	}

	public BigDecimal getValorUnitConv() {
		return this.valorUnitConv;
	}

	public void setValorUnitConv(BigDecimal valorUnitConv) {
		this.valorUnitConv = valorUnitConv;
	}

	public BigDecimal getValorUnitOrig() {
		return this.valorUnitOrig;
	}

	public void setValorUnitOrig(BigDecimal valorUnitOrig) {
		this.valorUnitOrig = valorUnitOrig;
	}

	public List<FisTributacao> getFisTributacaos() {
		return this.fisTributacaos;
	}

	public void setFisTributacaos(List<FisTributacao> fisTributacaos) {
		this.fisTributacaos = fisTributacaos;
	}

	public FisTributacao addFisTributacao(FisTributacao fisTributacao) {
		getFisTributacaos().add(fisTributacao);
		fisTributacao.setMovItemserv(this);

		return fisTributacao;
	}

	public FisTributacao removeFisTributacao(FisTributacao fisTributacao) {
		getFisTributacaos().remove(fisTributacao);
		fisTributacao.setMovItemserv(null);

		return fisTributacao;
	}

	public FisCfop getFisCfop() {
		return this.fisCfop;
	}

	public void setFisCfop(FisCfop fisCfop) {
		this.fisCfop = fisCfop;
	}

	public GerItemserv getGerItemserv() {
		return this.gerItemserv;
	}

	public void setGerItemserv(GerItemserv gerItemserv) {
		this.gerItemserv = gerItemserv;
	}

	public GerItemservLote getGerItemservLote() {
		return this.gerItemservLote;
	}

	public void setGerItemservLote(GerItemservLote gerItemservLote) {
		this.gerItemservLote = gerItemservLote;
	}

	public GerItemservVar getGerItemservVar() {
		return this.gerItemservVar;
	}

	public void setGerItemservVar(GerItemservVar gerItemservVar) {
		this.gerItemservVar = gerItemservVar;
	}

	public GerUmedida getGerUmedida() {
		return this.gerUmedida;
	}

	public void setGerUmedida(GerUmedida gerUmedida) {
		this.gerUmedida = gerUmedida;
	}

	public Mov getMov() {
		return this.mov;
	}

	public void setMov(Mov mov) {
		this.mov = mov;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<MovOrigem> getMovOrigems1() {
		return this.movOrigems1;
	}

	public void setMovOrigems1(List<MovOrigem> movOrigems1) {
		this.movOrigems1 = movOrigems1;
	}

	public MovOrigem addMovOrigems1(MovOrigem movOrigems1) {
		getMovOrigems1().add(movOrigems1);
		movOrigems1.setMovItemserv1(this);

		return movOrigems1;
	}

	public MovOrigem removeMovOrigems1(MovOrigem movOrigems1) {
		getMovOrigems1().remove(movOrigems1);
		movOrigems1.setMovItemserv1(null);

		return movOrigems1;
	}

	public List<MovOrigem> getMovOrigems2() {
		return this.movOrigems2;
	}

	public void setMovOrigems2(List<MovOrigem> movOrigems2) {
		this.movOrigems2 = movOrigems2;
	}

	public MovOrigem addMovOrigems2(MovOrigem movOrigems2) {
		getMovOrigems2().add(movOrigems2);
		movOrigems2.setMovItemserv2(this);

		return movOrigems2;
	}

	public MovOrigem removeMovOrigems2(MovOrigem movOrigems2) {
		getMovOrigems2().remove(movOrigems2);
		movOrigems2.setMovItemserv2(null);

		return movOrigems2;
	}

	public List<OpeCentroDest> getOpeCentroDests() {
		return this.opeCentroDests;
	}

	public void setOpeCentroDests(List<OpeCentroDest> opeCentroDests) {
		this.opeCentroDests = opeCentroDests;
	}

	public OpeCentroDest addOpeCentroDest(OpeCentroDest opeCentroDest) {
		getOpeCentroDests().add(opeCentroDest);
		opeCentroDest.setMovItemserv(this);

		return opeCentroDest;
	}

	public OpeCentroDest removeOpeCentroDest(OpeCentroDest opeCentroDest) {
		getOpeCentroDests().remove(opeCentroDest);
		opeCentroDest.setMovItemserv(null);

		return opeCentroDest;
	}

}