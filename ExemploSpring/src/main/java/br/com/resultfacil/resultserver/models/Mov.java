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
@Table(name="mov")
@NamedQuery(name="Mov.findAll", query="SELECT m FROM Mov m")
public class Mov implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="cep_carreg", length=50)
	private String cepCarreg;

	@Column(name="cep_descarreg", length=50)
	private String cepDescarreg;

	@Temporal(TemporalType.DATE)
	@Column(name="data_anulacao")
	private Date dataAnulacao;

	@Column(name="data_emissao")
	private Timestamp dataEmissao;

	@Temporal(TemporalType.DATE)
	@Column(name="data_entrada_saida")
	private Date dataEntradaSaida;

	@Temporal(TemporalType.DATE)
	@Column(name="data_entrega")
	private Date dataEntrega;

	@Column(name="data_mov")
	private Timestamp dataMov;

	@Temporal(TemporalType.DATE)
	@Column(name="data_valid")
	private Date dataValid;

	@Column(name="fis_exig_iss_nfs", length=1)
	private String fisExigIssNfs;

	@Column(name="fis_iss_retido_nfs", length=1)
	private String fisIssRetidoNfs;

	@Column(name="fis_nat_ope_nfs", length=1)
	private String fisNatOpeNfs;

	@Column(name="fis_tipo_resp_reten", length=1)
	private String fisTipoRespReten;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="nr_externo", length=50)
	private String nrExterno;

	@Column(name="numero_mov")
	private Integer numeroMov;

	@Column(name="numero_mov_pre")
	private Integer numeroMovPre;

	@Column(length=250)
	private String observacao;

	@Column(name="observacao_fiscal", length=250)
	private String observacaoFiscal;

	@Column(name="observacao_item", length=250)
	private String observacaoItem;

	@Column(name="observacao_serv", length=250)
	private String observacaoServ;

	@Column(name="observacao_transp", length=250)
	private String observacaoTransp;

	@Column(name="qnt_carga", precision=18, scale=6)
	private BigDecimal qntCarga;

	@Column(name="serie_mov", length=3)
	private String serieMov;

	@Column(name="serio_mov_pre", length=3)
	private String serioMovPre;

	@Column(length=50)
	private String taf;

	@Column(name="tipo_carga", length=2)
	private String tipoCarga;

	@Column(name="tipo_emissao_carga")
	private Integer tipoEmissaoCarga;

	@Column(name="tipo_fretamento")
	private Integer tipoFretamento;

	@Column(name="tipo_frete", nullable=false)
	private Integer tipoFrete;

	@Column(name="tipo_modal_carga", length=2)
	private String tipoModalCarga;

	@Column(name="tipo_serv_frete")
	private Integer tipoServFrete;

	@Column(name="tipo_tomador_serv_frete")
	private Integer tipoTomadorServFrete;

	@Column(name="tipo_transportador_carga")
	private Integer tipoTransportadorCarga;

	@Column(name="tipo_umedida_carga", length=2)
	private String tipoUmedidaCarga;

	@Column(name="valor_carga", precision=18, scale=6)
	private BigDecimal valorCarga;

	@Column(name="valor_financeiro_total", precision=18, scale=6)
	private BigDecimal valorFinanceiroTotal;

	@Column(name="valor_item_frete_total", precision=18, scale=6)
	private BigDecimal valorItemFreteTotal;

	@Column(name="valor_total", nullable=false, precision=18, scale=6)
	private BigDecimal valorTotal;

	//bi-directional many-to-one association to FinPagrecOrigem
	@OneToMany(mappedBy="mov")
	private List<FinPagrecOrigem> finPagrecOrigems;

	//bi-directional many-to-one association to FisDoc
	@OneToMany(mappedBy="mov")
	private List<FisDoc> fisDocs;

	//bi-directional many-to-one association to FisTributacao
	@OneToMany(mappedBy="mov")
	private List<FisTributacao> fisTributacaos;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="fin_cond_pagrec_id")
	private FinCondPagrec finCondPagrec;

	//bi-directional many-to-one association to FisDocTipo
	@ManyToOne
	@JoinColumn(name="fis_doc_tipo_id")
	private FisDocTipo fisDocTipo;

	//bi-directional many-to-one association to GerCidade
	@ManyToOne
	@JoinColumn(name="ger_cidade_id_carreg")
	private GerCidade gerCidade1;

	//bi-directional many-to-one association to GerCidade
	@ManyToOne
	@JoinColumn(name="ger_cidade_id_descarreg")
	private GerCidade gerCidade2;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="ger_pessoa_id", nullable=false)
	private GerPessoa gerPessoa;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_dest")
	private GerPessoaEndereco gerPessoaEndereco1;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_entrega", nullable=false)
	private GerPessoaEndereco gerPessoaEndereco2;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_expe")
	private GerPessoaEndereco gerPessoaEndereco3;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_fiscal", nullable=false)
	private GerPessoaEndereco gerPessoaEndereco4;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_inter")
	private GerPessoaEndereco gerPessoaEndereco5;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_rece")
	private GerPessoaEndereco gerPessoaEndereco6;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_reme")
	private GerPessoaEndereco gerPessoaEndereco7;

	//bi-directional many-to-one association to MovOperacao
	@ManyToOne
	@JoinColumn(name="mov_operacao_id")
	private MovOperacao movOperacao;

	//bi-directional many-to-one association to MovStatus
	@ManyToOne
	@JoinColumn(name="mov_status_id")
	private MovStatus movStatus;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="sys_user_id_resp")
	private SysUser sysUser;

	//bi-directional many-to-one association to MovCiot
	@OneToMany(mappedBy="mov")
	private List<MovCiot> movCiots;

	//bi-directional many-to-one association to MovComp
	@OneToMany(mappedBy="mov")
	private List<MovComp> movComps;

	//bi-directional many-to-one association to MovCondutor
	@OneToMany(mappedBy="mov")
	private List<MovCondutor> movCondutors;

	//bi-directional many-to-one association to MovCotacao
	@OneToMany(mappedBy="mov")
	private List<MovCotacao> movCotacaos;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="mov")
	private List<MovCotacaoAnal> movCotacaoAnals;

	//bi-directional many-to-one association to MovEntrega
	@OneToMany(mappedBy="mov")
	private List<MovEntrega> movEntregas;

	//bi-directional many-to-one association to MovEntregaDoc
	@OneToMany(mappedBy="mov1")
	private List<MovEntregaDoc> movEntregaDocs1;

	//bi-directional many-to-one association to MovEntregaDoc
	@OneToMany(mappedBy="mov2")
	private List<MovEntregaDoc> movEntregaDocs2;

	//bi-directional many-to-one association to MovFrete
	@OneToMany(mappedBy="mov")
	private List<MovFrete> movFretes;

	//bi-directional many-to-one association to MovItemserv
	@OneToMany(mappedBy="mov")
	private List<MovItemserv> movItemservs;

	//bi-directional many-to-one association to MovLacre
	@OneToMany(mappedBy="mov")
	private List<MovLacre> movLacres;

	//bi-directional many-to-one association to MovMedida
	@OneToMany(mappedBy="mov")
	private List<MovMedida> movMedidas;

	//bi-directional many-to-one association to MovOrigem
	@OneToMany(mappedBy="mov1")
	private List<MovOrigem> movOrigems1;

	//bi-directional many-to-one association to MovOrigem
	@OneToMany(mappedBy="mov2")
	private List<MovOrigem> movOrigems2;

	//bi-directional many-to-one association to MovPedagio
	@OneToMany(mappedBy="mov")
	private List<MovPedagio> movPedagios;

	//bi-directional many-to-one association to MovPercurso
	@OneToMany(mappedBy="mov")
	private List<MovPercurso> movPercursos;

	//bi-directional many-to-one association to MovReboque
	@OneToMany(mappedBy="mov")
	private List<MovReboque> movReboques;

	//bi-directional many-to-one association to MovSeguradora
	@OneToMany(mappedBy="mov")
	private List<MovSeguradora> movSeguradoras;

	//bi-directional many-to-one association to MovTomador
	@OneToMany(mappedBy="mov")
	private List<MovTomador> movTomadors;

	//bi-directional many-to-one association to SysDocument
	@OneToMany(mappedBy="mov")
	private List<SysDocument> sysDocuments;

	public Mov() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getCepCarreg() {
		return this.cepCarreg;
	}

	public void setCepCarreg(String cepCarreg) {
		this.cepCarreg = cepCarreg;
	}

	public String getCepDescarreg() {
		return this.cepDescarreg;
	}

	public void setCepDescarreg(String cepDescarreg) {
		this.cepDescarreg = cepDescarreg;
	}

	public Date getDataAnulacao() {
		return this.dataAnulacao;
	}

	public void setDataAnulacao(Date dataAnulacao) {
		this.dataAnulacao = dataAnulacao;
	}

	public Timestamp getDataEmissao() {
		return this.dataEmissao;
	}

	public void setDataEmissao(Timestamp dataEmissao) {
		this.dataEmissao = dataEmissao;
	}

	public Date getDataEntradaSaida() {
		return this.dataEntradaSaida;
	}

	public void setDataEntradaSaida(Date dataEntradaSaida) {
		this.dataEntradaSaida = dataEntradaSaida;
	}

	public Date getDataEntrega() {
		return this.dataEntrega;
	}

	public void setDataEntrega(Date dataEntrega) {
		this.dataEntrega = dataEntrega;
	}

	public Timestamp getDataMov() {
		return this.dataMov;
	}

	public void setDataMov(Timestamp dataMov) {
		this.dataMov = dataMov;
	}

	public Date getDataValid() {
		return this.dataValid;
	}

	public void setDataValid(Date dataValid) {
		this.dataValid = dataValid;
	}

	public String getFisExigIssNfs() {
		return this.fisExigIssNfs;
	}

	public void setFisExigIssNfs(String fisExigIssNfs) {
		this.fisExigIssNfs = fisExigIssNfs;
	}

	public String getFisIssRetidoNfs() {
		return this.fisIssRetidoNfs;
	}

	public void setFisIssRetidoNfs(String fisIssRetidoNfs) {
		this.fisIssRetidoNfs = fisIssRetidoNfs;
	}

	public String getFisNatOpeNfs() {
		return this.fisNatOpeNfs;
	}

	public void setFisNatOpeNfs(String fisNatOpeNfs) {
		this.fisNatOpeNfs = fisNatOpeNfs;
	}

	public String getFisTipoRespReten() {
		return this.fisTipoRespReten;
	}

	public void setFisTipoRespReten(String fisTipoRespReten) {
		this.fisTipoRespReten = fisTipoRespReten;
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

	public String getNrExterno() {
		return this.nrExterno;
	}

	public void setNrExterno(String nrExterno) {
		this.nrExterno = nrExterno;
	}

	public Integer getNumeroMov() {
		return this.numeroMov;
	}

	public void setNumeroMov(Integer numeroMov) {
		this.numeroMov = numeroMov;
	}

	public Integer getNumeroMovPre() {
		return this.numeroMovPre;
	}

	public void setNumeroMovPre(Integer numeroMovPre) {
		this.numeroMovPre = numeroMovPre;
	}

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public String getObservacaoFiscal() {
		return this.observacaoFiscal;
	}

	public void setObservacaoFiscal(String observacaoFiscal) {
		this.observacaoFiscal = observacaoFiscal;
	}

	public String getObservacaoItem() {
		return this.observacaoItem;
	}

	public void setObservacaoItem(String observacaoItem) {
		this.observacaoItem = observacaoItem;
	}

	public String getObservacaoServ() {
		return this.observacaoServ;
	}

	public void setObservacaoServ(String observacaoServ) {
		this.observacaoServ = observacaoServ;
	}

	public String getObservacaoTransp() {
		return this.observacaoTransp;
	}

	public void setObservacaoTransp(String observacaoTransp) {
		this.observacaoTransp = observacaoTransp;
	}

	public BigDecimal getQntCarga() {
		return this.qntCarga;
	}

	public void setQntCarga(BigDecimal qntCarga) {
		this.qntCarga = qntCarga;
	}

	public String getSerieMov() {
		return this.serieMov;
	}

	public void setSerieMov(String serieMov) {
		this.serieMov = serieMov;
	}

	public String getSerioMovPre() {
		return this.serioMovPre;
	}

	public void setSerioMovPre(String serioMovPre) {
		this.serioMovPre = serioMovPre;
	}

	public String getTaf() {
		return this.taf;
	}

	public void setTaf(String taf) {
		this.taf = taf;
	}

	public String getTipoCarga() {
		return this.tipoCarga;
	}

	public void setTipoCarga(String tipoCarga) {
		this.tipoCarga = tipoCarga;
	}

	public Integer getTipoEmissaoCarga() {
		return this.tipoEmissaoCarga;
	}

	public void setTipoEmissaoCarga(Integer tipoEmissaoCarga) {
		this.tipoEmissaoCarga = tipoEmissaoCarga;
	}

	public Integer getTipoFretamento() {
		return this.tipoFretamento;
	}

	public void setTipoFretamento(Integer tipoFretamento) {
		this.tipoFretamento = tipoFretamento;
	}

	public Integer getTipoFrete() {
		return this.tipoFrete;
	}

	public void setTipoFrete(Integer tipoFrete) {
		this.tipoFrete = tipoFrete;
	}

	public String getTipoModalCarga() {
		return this.tipoModalCarga;
	}

	public void setTipoModalCarga(String tipoModalCarga) {
		this.tipoModalCarga = tipoModalCarga;
	}

	public Integer getTipoServFrete() {
		return this.tipoServFrete;
	}

	public void setTipoServFrete(Integer tipoServFrete) {
		this.tipoServFrete = tipoServFrete;
	}

	public Integer getTipoTomadorServFrete() {
		return this.tipoTomadorServFrete;
	}

	public void setTipoTomadorServFrete(Integer tipoTomadorServFrete) {
		this.tipoTomadorServFrete = tipoTomadorServFrete;
	}

	public Integer getTipoTransportadorCarga() {
		return this.tipoTransportadorCarga;
	}

	public void setTipoTransportadorCarga(Integer tipoTransportadorCarga) {
		this.tipoTransportadorCarga = tipoTransportadorCarga;
	}

	public String getTipoUmedidaCarga() {
		return this.tipoUmedidaCarga;
	}

	public void setTipoUmedidaCarga(String tipoUmedidaCarga) {
		this.tipoUmedidaCarga = tipoUmedidaCarga;
	}

	public BigDecimal getValorCarga() {
		return this.valorCarga;
	}

	public void setValorCarga(BigDecimal valorCarga) {
		this.valorCarga = valorCarga;
	}

	public BigDecimal getValorFinanceiroTotal() {
		return this.valorFinanceiroTotal;
	}

	public void setValorFinanceiroTotal(BigDecimal valorFinanceiroTotal) {
		this.valorFinanceiroTotal = valorFinanceiroTotal;
	}

	public BigDecimal getValorItemFreteTotal() {
		return this.valorItemFreteTotal;
	}

	public void setValorItemFreteTotal(BigDecimal valorItemFreteTotal) {
		this.valorItemFreteTotal = valorItemFreteTotal;
	}

	public BigDecimal getValorTotal() {
		return this.valorTotal;
	}

	public void setValorTotal(BigDecimal valorTotal) {
		this.valorTotal = valorTotal;
	}

	public List<FinPagrecOrigem> getFinPagrecOrigems() {
		return this.finPagrecOrigems;
	}

	public void setFinPagrecOrigems(List<FinPagrecOrigem> finPagrecOrigems) {
		this.finPagrecOrigems = finPagrecOrigems;
	}

	public FinPagrecOrigem addFinPagrecOrigem(FinPagrecOrigem finPagrecOrigem) {
		getFinPagrecOrigems().add(finPagrecOrigem);
		finPagrecOrigem.setMov(this);

		return finPagrecOrigem;
	}

	public FinPagrecOrigem removeFinPagrecOrigem(FinPagrecOrigem finPagrecOrigem) {
		getFinPagrecOrigems().remove(finPagrecOrigem);
		finPagrecOrigem.setMov(null);

		return finPagrecOrigem;
	}

	public List<FisDoc> getFisDocs() {
		return this.fisDocs;
	}

	public void setFisDocs(List<FisDoc> fisDocs) {
		this.fisDocs = fisDocs;
	}

	public FisDoc addFisDoc(FisDoc fisDoc) {
		getFisDocs().add(fisDoc);
		fisDoc.setMov(this);

		return fisDoc;
	}

	public FisDoc removeFisDoc(FisDoc fisDoc) {
		getFisDocs().remove(fisDoc);
		fisDoc.setMov(null);

		return fisDoc;
	}

	public List<FisTributacao> getFisTributacaos() {
		return this.fisTributacaos;
	}

	public void setFisTributacaos(List<FisTributacao> fisTributacaos) {
		this.fisTributacaos = fisTributacaos;
	}

	public FisTributacao addFisTributacao(FisTributacao fisTributacao) {
		getFisTributacaos().add(fisTributacao);
		fisTributacao.setMov(this);

		return fisTributacao;
	}

	public FisTributacao removeFisTributacao(FisTributacao fisTributacao) {
		getFisTributacaos().remove(fisTributacao);
		fisTributacao.setMov(null);

		return fisTributacao;
	}

	public FinCondPagrec getFinCondPagrec() {
		return this.finCondPagrec;
	}

	public void setFinCondPagrec(FinCondPagrec finCondPagrec) {
		this.finCondPagrec = finCondPagrec;
	}

	public FisDocTipo getFisDocTipo() {
		return this.fisDocTipo;
	}

	public void setFisDocTipo(FisDocTipo fisDocTipo) {
		this.fisDocTipo = fisDocTipo;
	}

	public GerCidade getGerCidade1() {
		return this.gerCidade1;
	}

	public void setGerCidade1(GerCidade gerCidade1) {
		this.gerCidade1 = gerCidade1;
	}

	public GerCidade getGerCidade2() {
		return this.gerCidade2;
	}

	public void setGerCidade2(GerCidade gerCidade2) {
		this.gerCidade2 = gerCidade2;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public GerPessoa getGerPessoa() {
		return this.gerPessoa;
	}

	public void setGerPessoa(GerPessoa gerPessoa) {
		this.gerPessoa = gerPessoa;
	}

	public GerPessoaEndereco getGerPessoaEndereco1() {
		return this.gerPessoaEndereco1;
	}

	public void setGerPessoaEndereco1(GerPessoaEndereco gerPessoaEndereco1) {
		this.gerPessoaEndereco1 = gerPessoaEndereco1;
	}

	public GerPessoaEndereco getGerPessoaEndereco2() {
		return this.gerPessoaEndereco2;
	}

	public void setGerPessoaEndereco2(GerPessoaEndereco gerPessoaEndereco2) {
		this.gerPessoaEndereco2 = gerPessoaEndereco2;
	}

	public GerPessoaEndereco getGerPessoaEndereco3() {
		return this.gerPessoaEndereco3;
	}

	public void setGerPessoaEndereco3(GerPessoaEndereco gerPessoaEndereco3) {
		this.gerPessoaEndereco3 = gerPessoaEndereco3;
	}

	public GerPessoaEndereco getGerPessoaEndereco4() {
		return this.gerPessoaEndereco4;
	}

	public void setGerPessoaEndereco4(GerPessoaEndereco gerPessoaEndereco4) {
		this.gerPessoaEndereco4 = gerPessoaEndereco4;
	}

	public GerPessoaEndereco getGerPessoaEndereco5() {
		return this.gerPessoaEndereco5;
	}

	public void setGerPessoaEndereco5(GerPessoaEndereco gerPessoaEndereco5) {
		this.gerPessoaEndereco5 = gerPessoaEndereco5;
	}

	public GerPessoaEndereco getGerPessoaEndereco6() {
		return this.gerPessoaEndereco6;
	}

	public void setGerPessoaEndereco6(GerPessoaEndereco gerPessoaEndereco6) {
		this.gerPessoaEndereco6 = gerPessoaEndereco6;
	}

	public GerPessoaEndereco getGerPessoaEndereco7() {
		return this.gerPessoaEndereco7;
	}

	public void setGerPessoaEndereco7(GerPessoaEndereco gerPessoaEndereco7) {
		this.gerPessoaEndereco7 = gerPessoaEndereco7;
	}

	public MovOperacao getMovOperacao() {
		return this.movOperacao;
	}

	public void setMovOperacao(MovOperacao movOperacao) {
		this.movOperacao = movOperacao;
	}

	public MovStatus getMovStatus() {
		return this.movStatus;
	}

	public void setMovStatus(MovStatus movStatus) {
		this.movStatus = movStatus;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public SysUser getSysUser() {
		return this.sysUser;
	}

	public void setSysUser(SysUser sysUser) {
		this.sysUser = sysUser;
	}

	public List<MovCiot> getMovCiots() {
		return this.movCiots;
	}

	public void setMovCiots(List<MovCiot> movCiots) {
		this.movCiots = movCiots;
	}

	public MovCiot addMovCiot(MovCiot movCiot) {
		getMovCiots().add(movCiot);
		movCiot.setMov(this);

		return movCiot;
	}

	public MovCiot removeMovCiot(MovCiot movCiot) {
		getMovCiots().remove(movCiot);
		movCiot.setMov(null);

		return movCiot;
	}

	public List<MovComp> getMovComps() {
		return this.movComps;
	}

	public void setMovComps(List<MovComp> movComps) {
		this.movComps = movComps;
	}

	public MovComp addMovComp(MovComp movComp) {
		getMovComps().add(movComp);
		movComp.setMov(this);

		return movComp;
	}

	public MovComp removeMovComp(MovComp movComp) {
		getMovComps().remove(movComp);
		movComp.setMov(null);

		return movComp;
	}

	public List<MovCondutor> getMovCondutors() {
		return this.movCondutors;
	}

	public void setMovCondutors(List<MovCondutor> movCondutors) {
		this.movCondutors = movCondutors;
	}

	public MovCondutor addMovCondutor(MovCondutor movCondutor) {
		getMovCondutors().add(movCondutor);
		movCondutor.setMov(this);

		return movCondutor;
	}

	public MovCondutor removeMovCondutor(MovCondutor movCondutor) {
		getMovCondutors().remove(movCondutor);
		movCondutor.setMov(null);

		return movCondutor;
	}

	public List<MovCotacao> getMovCotacaos() {
		return this.movCotacaos;
	}

	public void setMovCotacaos(List<MovCotacao> movCotacaos) {
		this.movCotacaos = movCotacaos;
	}

	public MovCotacao addMovCotacao(MovCotacao movCotacao) {
		getMovCotacaos().add(movCotacao);
		movCotacao.setMov(this);

		return movCotacao;
	}

	public MovCotacao removeMovCotacao(MovCotacao movCotacao) {
		getMovCotacaos().remove(movCotacao);
		movCotacao.setMov(null);

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
		movCotacaoAnal.setMov(this);

		return movCotacaoAnal;
	}

	public MovCotacaoAnal removeMovCotacaoAnal(MovCotacaoAnal movCotacaoAnal) {
		getMovCotacaoAnals().remove(movCotacaoAnal);
		movCotacaoAnal.setMov(null);

		return movCotacaoAnal;
	}

	public List<MovEntrega> getMovEntregas() {
		return this.movEntregas;
	}

	public void setMovEntregas(List<MovEntrega> movEntregas) {
		this.movEntregas = movEntregas;
	}

	public MovEntrega addMovEntrega(MovEntrega movEntrega) {
		getMovEntregas().add(movEntrega);
		movEntrega.setMov(this);

		return movEntrega;
	}

	public MovEntrega removeMovEntrega(MovEntrega movEntrega) {
		getMovEntregas().remove(movEntrega);
		movEntrega.setMov(null);

		return movEntrega;
	}

	public List<MovEntregaDoc> getMovEntregaDocs1() {
		return this.movEntregaDocs1;
	}

	public void setMovEntregaDocs1(List<MovEntregaDoc> movEntregaDocs1) {
		this.movEntregaDocs1 = movEntregaDocs1;
	}

	public MovEntregaDoc addMovEntregaDocs1(MovEntregaDoc movEntregaDocs1) {
		getMovEntregaDocs1().add(movEntregaDocs1);
		movEntregaDocs1.setMov1(this);

		return movEntregaDocs1;
	}

	public MovEntregaDoc removeMovEntregaDocs1(MovEntregaDoc movEntregaDocs1) {
		getMovEntregaDocs1().remove(movEntregaDocs1);
		movEntregaDocs1.setMov1(null);

		return movEntregaDocs1;
	}

	public List<MovEntregaDoc> getMovEntregaDocs2() {
		return this.movEntregaDocs2;
	}

	public void setMovEntregaDocs2(List<MovEntregaDoc> movEntregaDocs2) {
		this.movEntregaDocs2 = movEntregaDocs2;
	}

	public MovEntregaDoc addMovEntregaDocs2(MovEntregaDoc movEntregaDocs2) {
		getMovEntregaDocs2().add(movEntregaDocs2);
		movEntregaDocs2.setMov2(this);

		return movEntregaDocs2;
	}

	public MovEntregaDoc removeMovEntregaDocs2(MovEntregaDoc movEntregaDocs2) {
		getMovEntregaDocs2().remove(movEntregaDocs2);
		movEntregaDocs2.setMov2(null);

		return movEntregaDocs2;
	}

	public List<MovFrete> getMovFretes() {
		return this.movFretes;
	}

	public void setMovFretes(List<MovFrete> movFretes) {
		this.movFretes = movFretes;
	}

	public MovFrete addMovFrete(MovFrete movFrete) {
		getMovFretes().add(movFrete);
		movFrete.setMov(this);

		return movFrete;
	}

	public MovFrete removeMovFrete(MovFrete movFrete) {
		getMovFretes().remove(movFrete);
		movFrete.setMov(null);

		return movFrete;
	}

	public List<MovItemserv> getMovItemservs() {
		return this.movItemservs;
	}

	public void setMovItemservs(List<MovItemserv> movItemservs) {
		this.movItemservs = movItemservs;
	}

	public MovItemserv addMovItemserv(MovItemserv movItemserv) {
		getMovItemservs().add(movItemserv);
		movItemserv.setMov(this);

		return movItemserv;
	}

	public MovItemserv removeMovItemserv(MovItemserv movItemserv) {
		getMovItemservs().remove(movItemserv);
		movItemserv.setMov(null);

		return movItemserv;
	}

	public List<MovLacre> getMovLacres() {
		return this.movLacres;
	}

	public void setMovLacres(List<MovLacre> movLacres) {
		this.movLacres = movLacres;
	}

	public MovLacre addMovLacre(MovLacre movLacre) {
		getMovLacres().add(movLacre);
		movLacre.setMov(this);

		return movLacre;
	}

	public MovLacre removeMovLacre(MovLacre movLacre) {
		getMovLacres().remove(movLacre);
		movLacre.setMov(null);

		return movLacre;
	}

	public List<MovMedida> getMovMedidas() {
		return this.movMedidas;
	}

	public void setMovMedidas(List<MovMedida> movMedidas) {
		this.movMedidas = movMedidas;
	}

	public MovMedida addMovMedida(MovMedida movMedida) {
		getMovMedidas().add(movMedida);
		movMedida.setMov(this);

		return movMedida;
	}

	public MovMedida removeMovMedida(MovMedida movMedida) {
		getMovMedidas().remove(movMedida);
		movMedida.setMov(null);

		return movMedida;
	}

	public List<MovOrigem> getMovOrigems1() {
		return this.movOrigems1;
	}

	public void setMovOrigems1(List<MovOrigem> movOrigems1) {
		this.movOrigems1 = movOrigems1;
	}

	public MovOrigem addMovOrigems1(MovOrigem movOrigems1) {
		getMovOrigems1().add(movOrigems1);
		movOrigems1.setMov1(this);

		return movOrigems1;
	}

	public MovOrigem removeMovOrigems1(MovOrigem movOrigems1) {
		getMovOrigems1().remove(movOrigems1);
		movOrigems1.setMov1(null);

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
		movOrigems2.setMov2(this);

		return movOrigems2;
	}

	public MovOrigem removeMovOrigems2(MovOrigem movOrigems2) {
		getMovOrigems2().remove(movOrigems2);
		movOrigems2.setMov2(null);

		return movOrigems2;
	}

	public List<MovPedagio> getMovPedagios() {
		return this.movPedagios;
	}

	public void setMovPedagios(List<MovPedagio> movPedagios) {
		this.movPedagios = movPedagios;
	}

	public MovPedagio addMovPedagio(MovPedagio movPedagio) {
		getMovPedagios().add(movPedagio);
		movPedagio.setMov(this);

		return movPedagio;
	}

	public MovPedagio removeMovPedagio(MovPedagio movPedagio) {
		getMovPedagios().remove(movPedagio);
		movPedagio.setMov(null);

		return movPedagio;
	}

	public List<MovPercurso> getMovPercursos() {
		return this.movPercursos;
	}

	public void setMovPercursos(List<MovPercurso> movPercursos) {
		this.movPercursos = movPercursos;
	}

	public MovPercurso addMovPercurso(MovPercurso movPercurso) {
		getMovPercursos().add(movPercurso);
		movPercurso.setMov(this);

		return movPercurso;
	}

	public MovPercurso removeMovPercurso(MovPercurso movPercurso) {
		getMovPercursos().remove(movPercurso);
		movPercurso.setMov(null);

		return movPercurso;
	}

	public List<MovReboque> getMovReboques() {
		return this.movReboques;
	}

	public void setMovReboques(List<MovReboque> movReboques) {
		this.movReboques = movReboques;
	}

	public MovReboque addMovReboque(MovReboque movReboque) {
		getMovReboques().add(movReboque);
		movReboque.setMov(this);

		return movReboque;
	}

	public MovReboque removeMovReboque(MovReboque movReboque) {
		getMovReboques().remove(movReboque);
		movReboque.setMov(null);

		return movReboque;
	}

	public List<MovSeguradora> getMovSeguradoras() {
		return this.movSeguradoras;
	}

	public void setMovSeguradoras(List<MovSeguradora> movSeguradoras) {
		this.movSeguradoras = movSeguradoras;
	}

	public MovSeguradora addMovSeguradora(MovSeguradora movSeguradora) {
		getMovSeguradoras().add(movSeguradora);
		movSeguradora.setMov(this);

		return movSeguradora;
	}

	public MovSeguradora removeMovSeguradora(MovSeguradora movSeguradora) {
		getMovSeguradoras().remove(movSeguradora);
		movSeguradora.setMov(null);

		return movSeguradora;
	}

	public List<MovTomador> getMovTomadors() {
		return this.movTomadors;
	}

	public void setMovTomadors(List<MovTomador> movTomadors) {
		this.movTomadors = movTomadors;
	}

	public MovTomador addMovTomador(MovTomador movTomador) {
		getMovTomadors().add(movTomador);
		movTomador.setMov(this);

		return movTomador;
	}

	public MovTomador removeMovTomador(MovTomador movTomador) {
		getMovTomadors().remove(movTomador);
		movTomador.setMov(null);

		return movTomador;
	}

	public List<SysDocument> getSysDocuments() {
		return this.sysDocuments;
	}

	public void setSysDocuments(List<SysDocument> sysDocuments) {
		this.sysDocuments = sysDocuments;
	}

	public SysDocument addSysDocument(SysDocument sysDocument) {
		getSysDocuments().add(sysDocument);
		sysDocument.setMov(this);

		return sysDocument;
	}

	public SysDocument removeSysDocument(SysDocument sysDocument) {
		getSysDocuments().remove(sysDocument);
		sysDocument.setMov(null);

		return sysDocument;
	}

}