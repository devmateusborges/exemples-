package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.util.Date;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="fis_tributacao")
@NamedQuery(name="FisTributacao.findAll", query="SELECT f FROM FisTributacao f")
public class FisTributacao implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=4)
	private String cst;

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

	@Column(name="margem_agregada_st", nullable=false, precision=18, scale=6)
	private BigDecimal margemAgregadaSt;

	@Column(name="modalidade_base_calc", nullable=false)
	private Integer modalidadeBaseCalc;

	@Column(name="modalidade_base_calc_st")
	private Integer modalidadeBaseCalcSt;

	@Column(name="motivo_imposto_desonerado")
	private Integer motivoImpostoDesonerado;

	@Column(length=250)
	private String observacao;

	@Column(name="perc_aliquota", nullable=false, precision=18, scale=6)
	private BigDecimal percAliquota;

	@Column(name="perc_aliquota_credito", precision=18, scale=6)
	private BigDecimal percAliquotaCredito;

	@Column(name="perc_aliquota_efetiva", precision=18, scale=6)
	private BigDecimal percAliquotaEfetiva;

	@Column(name="perc_aliquota_fcp", nullable=false, precision=18, scale=6)
	private BigDecimal percAliquotaFcp;

	@Column(name="perc_aliquota_fcp_st", nullable=false, precision=18, scale=6)
	private BigDecimal percAliquotaFcpSt;

	@Column(name="perc_aliquota_fcp_st_ret", precision=18, scale=6)
	private BigDecimal percAliquotaFcpStRet;

	@Column(name="perc_aliquota_isento", nullable=false, precision=18, scale=6)
	private BigDecimal percAliquotaIsento;

	@Column(name="perc_aliquota_red_base_calc_efetiva", precision=18, scale=6)
	private BigDecimal percAliquotaRedBaseCalcEfetiva;

	@Column(name="perc_aliquota_st", nullable=false, precision=18, scale=6)
	private BigDecimal percAliquotaSt;

	@Column(name="perc_credito_sn", nullable=false, precision=18, scale=6)
	private BigDecimal percCreditoSn;

	@Column(name="perc_interestadual_uf_fim", precision=18, scale=6)
	private BigDecimal percInterestadualUfFim;

	@Column(name="perc_interna_uf_fim", precision=18, scale=6)
	private BigDecimal percInternaUfFim;

	@Column(name="perc_partilha_uf_fim", precision=18, scale=6)
	private BigDecimal percPartilhaUfFim;

	@Column(name="perc_reducao_base_calc", nullable=false, precision=18, scale=6)
	private BigDecimal percReducaoBaseCalc;

	@Column(name="perc_uf_fim_fcp", precision=18, scale=6)
	private BigDecimal percUfFimFcp;

	@Column(name="valor_base_calc", nullable=false, precision=18, scale=6)
	private BigDecimal valorBaseCalc;

	@Column(name="valor_base_calc_efetiva", precision=18, scale=6)
	private BigDecimal valorBaseCalcEfetiva;

	@Column(name="valor_base_calc_fcp", nullable=false, precision=18, scale=6)
	private BigDecimal valorBaseCalcFcp;

	@Column(name="valor_base_calc_fcp_st", nullable=false, precision=18, scale=6)
	private BigDecimal valorBaseCalcFcpSt;

	@Column(name="valor_base_calc_fcp_st_ret", precision=18, scale=6)
	private BigDecimal valorBaseCalcFcpStRet;

	@Column(name="valor_base_calc_isento", nullable=false, precision=18, scale=6)
	private BigDecimal valorBaseCalcIsento;

	@Column(name="valor_base_calc_st", nullable=false, precision=18, scale=6)
	private BigDecimal valorBaseCalcSt;

	@Column(name="valor_base_calc_st_ret", precision=18, scale=6)
	private BigDecimal valorBaseCalcStRet;

	@Column(name="valor_base_calc_uf_fim", precision=18, scale=6)
	private BigDecimal valorBaseCalcUfFim;

	@Column(name="valor_credito_sn", nullable=false, precision=18, scale=6)
	private BigDecimal valorCreditoSn;

	@Column(name="valor_imposto", nullable=false, precision=18, scale=6)
	private BigDecimal valorImposto;

	@Column(name="valor_imposto_credito", precision=18, scale=6)
	private BigDecimal valorImpostoCredito;

	@Column(name="valor_imposto_desonerado", precision=18, scale=6)
	private BigDecimal valorImpostoDesonerado;

	@Column(name="valor_imposto_diferido", nullable=false, precision=18, scale=6)
	private BigDecimal valorImpostoDiferido;

	@Column(name="valor_imposto_efetiva", precision=18, scale=6)
	private BigDecimal valorImpostoEfetiva;

	@Column(name="valor_imposto_fcp", nullable=false, precision=18, scale=6)
	private BigDecimal valorImpostoFcp;

	@Column(name="valor_imposto_fcp_st", nullable=false, precision=18, scale=6)
	private BigDecimal valorImpostoFcpSt;

	@Column(name="valor_imposto_fcp_st_ret", precision=18, scale=6)
	private BigDecimal valorImpostoFcpStRet;

	@Column(name="valor_imposto_isento", nullable=false, precision=18, scale=6)
	private BigDecimal valorImpostoIsento;

	@Column(name="valor_imposto_operacao", nullable=false, precision=18, scale=6)
	private BigDecimal valorImpostoOperacao;

	@Column(name="valor_imposto_st", nullable=false, precision=18, scale=6)
	private BigDecimal valorImpostoSt;

	@Column(name="valor_imposto_st_ret", precision=18, scale=6)
	private BigDecimal valorImpostoStRet;

	@Column(name="valor_imposto_substituto", precision=18, scale=6)
	private BigDecimal valorImpostoSubstituto;

	@Column(name="valor_partilha_uf_fim", precision=18, scale=6)
	private BigDecimal valorPartilhaUfFim;

	@Column(name="valor_partilha_uf_inicio", precision=18, scale=6)
	private BigDecimal valorPartilhaUfInicio;

	@Column(name="valor_total_uf_fim_fcp", precision=18, scale=6)
	private BigDecimal valorTotalUfFimFcp;

	//bi-directional many-to-one association to FinPagrec
	@ManyToOne
	@JoinColumn(name="fin_pagrec_id")
	private FinPagrec finPagrec;

	//bi-directional many-to-one association to FisTributo
	@ManyToOne
	@JoinColumn(name="fis_tributo_id", nullable=false)
	private FisTributo fisTributo;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id")
	private Mov mov;

	//bi-directional many-to-one association to MovItemserv
	@ManyToOne
	@JoinColumn(name="mov_itemserv_id")
	private MovItemserv movItemserv;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public FisTributacao() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getCst() {
		return this.cst;
	}

	public void setCst(String cst) {
		this.cst = cst;
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

	public BigDecimal getMargemAgregadaSt() {
		return this.margemAgregadaSt;
	}

	public void setMargemAgregadaSt(BigDecimal margemAgregadaSt) {
		this.margemAgregadaSt = margemAgregadaSt;
	}

	public Integer getModalidadeBaseCalc() {
		return this.modalidadeBaseCalc;
	}

	public void setModalidadeBaseCalc(Integer modalidadeBaseCalc) {
		this.modalidadeBaseCalc = modalidadeBaseCalc;
	}

	public Integer getModalidadeBaseCalcSt() {
		return this.modalidadeBaseCalcSt;
	}

	public void setModalidadeBaseCalcSt(Integer modalidadeBaseCalcSt) {
		this.modalidadeBaseCalcSt = modalidadeBaseCalcSt;
	}

	public Integer getMotivoImpostoDesonerado() {
		return this.motivoImpostoDesonerado;
	}

	public void setMotivoImpostoDesonerado(Integer motivoImpostoDesonerado) {
		this.motivoImpostoDesonerado = motivoImpostoDesonerado;
	}

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public BigDecimal getPercAliquota() {
		return this.percAliquota;
	}

	public void setPercAliquota(BigDecimal percAliquota) {
		this.percAliquota = percAliquota;
	}

	public BigDecimal getPercAliquotaCredito() {
		return this.percAliquotaCredito;
	}

	public void setPercAliquotaCredito(BigDecimal percAliquotaCredito) {
		this.percAliquotaCredito = percAliquotaCredito;
	}

	public BigDecimal getPercAliquotaEfetiva() {
		return this.percAliquotaEfetiva;
	}

	public void setPercAliquotaEfetiva(BigDecimal percAliquotaEfetiva) {
		this.percAliquotaEfetiva = percAliquotaEfetiva;
	}

	public BigDecimal getPercAliquotaFcp() {
		return this.percAliquotaFcp;
	}

	public void setPercAliquotaFcp(BigDecimal percAliquotaFcp) {
		this.percAliquotaFcp = percAliquotaFcp;
	}

	public BigDecimal getPercAliquotaFcpSt() {
		return this.percAliquotaFcpSt;
	}

	public void setPercAliquotaFcpSt(BigDecimal percAliquotaFcpSt) {
		this.percAliquotaFcpSt = percAliquotaFcpSt;
	}

	public BigDecimal getPercAliquotaFcpStRet() {
		return this.percAliquotaFcpStRet;
	}

	public void setPercAliquotaFcpStRet(BigDecimal percAliquotaFcpStRet) {
		this.percAliquotaFcpStRet = percAliquotaFcpStRet;
	}

	public BigDecimal getPercAliquotaIsento() {
		return this.percAliquotaIsento;
	}

	public void setPercAliquotaIsento(BigDecimal percAliquotaIsento) {
		this.percAliquotaIsento = percAliquotaIsento;
	}

	public BigDecimal getPercAliquotaRedBaseCalcEfetiva() {
		return this.percAliquotaRedBaseCalcEfetiva;
	}

	public void setPercAliquotaRedBaseCalcEfetiva(BigDecimal percAliquotaRedBaseCalcEfetiva) {
		this.percAliquotaRedBaseCalcEfetiva = percAliquotaRedBaseCalcEfetiva;
	}

	public BigDecimal getPercAliquotaSt() {
		return this.percAliquotaSt;
	}

	public void setPercAliquotaSt(BigDecimal percAliquotaSt) {
		this.percAliquotaSt = percAliquotaSt;
	}

	public BigDecimal getPercCreditoSn() {
		return this.percCreditoSn;
	}

	public void setPercCreditoSn(BigDecimal percCreditoSn) {
		this.percCreditoSn = percCreditoSn;
	}

	public BigDecimal getPercInterestadualUfFim() {
		return this.percInterestadualUfFim;
	}

	public void setPercInterestadualUfFim(BigDecimal percInterestadualUfFim) {
		this.percInterestadualUfFim = percInterestadualUfFim;
	}

	public BigDecimal getPercInternaUfFim() {
		return this.percInternaUfFim;
	}

	public void setPercInternaUfFim(BigDecimal percInternaUfFim) {
		this.percInternaUfFim = percInternaUfFim;
	}

	public BigDecimal getPercPartilhaUfFim() {
		return this.percPartilhaUfFim;
	}

	public void setPercPartilhaUfFim(BigDecimal percPartilhaUfFim) {
		this.percPartilhaUfFim = percPartilhaUfFim;
	}

	public BigDecimal getPercReducaoBaseCalc() {
		return this.percReducaoBaseCalc;
	}

	public void setPercReducaoBaseCalc(BigDecimal percReducaoBaseCalc) {
		this.percReducaoBaseCalc = percReducaoBaseCalc;
	}

	public BigDecimal getPercUfFimFcp() {
		return this.percUfFimFcp;
	}

	public void setPercUfFimFcp(BigDecimal percUfFimFcp) {
		this.percUfFimFcp = percUfFimFcp;
	}

	public BigDecimal getValorBaseCalc() {
		return this.valorBaseCalc;
	}

	public void setValorBaseCalc(BigDecimal valorBaseCalc) {
		this.valorBaseCalc = valorBaseCalc;
	}

	public BigDecimal getValorBaseCalcEfetiva() {
		return this.valorBaseCalcEfetiva;
	}

	public void setValorBaseCalcEfetiva(BigDecimal valorBaseCalcEfetiva) {
		this.valorBaseCalcEfetiva = valorBaseCalcEfetiva;
	}

	public BigDecimal getValorBaseCalcFcp() {
		return this.valorBaseCalcFcp;
	}

	public void setValorBaseCalcFcp(BigDecimal valorBaseCalcFcp) {
		this.valorBaseCalcFcp = valorBaseCalcFcp;
	}

	public BigDecimal getValorBaseCalcFcpSt() {
		return this.valorBaseCalcFcpSt;
	}

	public void setValorBaseCalcFcpSt(BigDecimal valorBaseCalcFcpSt) {
		this.valorBaseCalcFcpSt = valorBaseCalcFcpSt;
	}

	public BigDecimal getValorBaseCalcFcpStRet() {
		return this.valorBaseCalcFcpStRet;
	}

	public void setValorBaseCalcFcpStRet(BigDecimal valorBaseCalcFcpStRet) {
		this.valorBaseCalcFcpStRet = valorBaseCalcFcpStRet;
	}

	public BigDecimal getValorBaseCalcIsento() {
		return this.valorBaseCalcIsento;
	}

	public void setValorBaseCalcIsento(BigDecimal valorBaseCalcIsento) {
		this.valorBaseCalcIsento = valorBaseCalcIsento;
	}

	public BigDecimal getValorBaseCalcSt() {
		return this.valorBaseCalcSt;
	}

	public void setValorBaseCalcSt(BigDecimal valorBaseCalcSt) {
		this.valorBaseCalcSt = valorBaseCalcSt;
	}

	public BigDecimal getValorBaseCalcStRet() {
		return this.valorBaseCalcStRet;
	}

	public void setValorBaseCalcStRet(BigDecimal valorBaseCalcStRet) {
		this.valorBaseCalcStRet = valorBaseCalcStRet;
	}

	public BigDecimal getValorBaseCalcUfFim() {
		return this.valorBaseCalcUfFim;
	}

	public void setValorBaseCalcUfFim(BigDecimal valorBaseCalcUfFim) {
		this.valorBaseCalcUfFim = valorBaseCalcUfFim;
	}

	public BigDecimal getValorCreditoSn() {
		return this.valorCreditoSn;
	}

	public void setValorCreditoSn(BigDecimal valorCreditoSn) {
		this.valorCreditoSn = valorCreditoSn;
	}

	public BigDecimal getValorImposto() {
		return this.valorImposto;
	}

	public void setValorImposto(BigDecimal valorImposto) {
		this.valorImposto = valorImposto;
	}

	public BigDecimal getValorImpostoCredito() {
		return this.valorImpostoCredito;
	}

	public void setValorImpostoCredito(BigDecimal valorImpostoCredito) {
		this.valorImpostoCredito = valorImpostoCredito;
	}

	public BigDecimal getValorImpostoDesonerado() {
		return this.valorImpostoDesonerado;
	}

	public void setValorImpostoDesonerado(BigDecimal valorImpostoDesonerado) {
		this.valorImpostoDesonerado = valorImpostoDesonerado;
	}

	public BigDecimal getValorImpostoDiferido() {
		return this.valorImpostoDiferido;
	}

	public void setValorImpostoDiferido(BigDecimal valorImpostoDiferido) {
		this.valorImpostoDiferido = valorImpostoDiferido;
	}

	public BigDecimal getValorImpostoEfetiva() {
		return this.valorImpostoEfetiva;
	}

	public void setValorImpostoEfetiva(BigDecimal valorImpostoEfetiva) {
		this.valorImpostoEfetiva = valorImpostoEfetiva;
	}

	public BigDecimal getValorImpostoFcp() {
		return this.valorImpostoFcp;
	}

	public void setValorImpostoFcp(BigDecimal valorImpostoFcp) {
		this.valorImpostoFcp = valorImpostoFcp;
	}

	public BigDecimal getValorImpostoFcpSt() {
		return this.valorImpostoFcpSt;
	}

	public void setValorImpostoFcpSt(BigDecimal valorImpostoFcpSt) {
		this.valorImpostoFcpSt = valorImpostoFcpSt;
	}

	public BigDecimal getValorImpostoFcpStRet() {
		return this.valorImpostoFcpStRet;
	}

	public void setValorImpostoFcpStRet(BigDecimal valorImpostoFcpStRet) {
		this.valorImpostoFcpStRet = valorImpostoFcpStRet;
	}

	public BigDecimal getValorImpostoIsento() {
		return this.valorImpostoIsento;
	}

	public void setValorImpostoIsento(BigDecimal valorImpostoIsento) {
		this.valorImpostoIsento = valorImpostoIsento;
	}

	public BigDecimal getValorImpostoOperacao() {
		return this.valorImpostoOperacao;
	}

	public void setValorImpostoOperacao(BigDecimal valorImpostoOperacao) {
		this.valorImpostoOperacao = valorImpostoOperacao;
	}

	public BigDecimal getValorImpostoSt() {
		return this.valorImpostoSt;
	}

	public void setValorImpostoSt(BigDecimal valorImpostoSt) {
		this.valorImpostoSt = valorImpostoSt;
	}

	public BigDecimal getValorImpostoStRet() {
		return this.valorImpostoStRet;
	}

	public void setValorImpostoStRet(BigDecimal valorImpostoStRet) {
		this.valorImpostoStRet = valorImpostoStRet;
	}

	public BigDecimal getValorImpostoSubstituto() {
		return this.valorImpostoSubstituto;
	}

	public void setValorImpostoSubstituto(BigDecimal valorImpostoSubstituto) {
		this.valorImpostoSubstituto = valorImpostoSubstituto;
	}

	public BigDecimal getValorPartilhaUfFim() {
		return this.valorPartilhaUfFim;
	}

	public void setValorPartilhaUfFim(BigDecimal valorPartilhaUfFim) {
		this.valorPartilhaUfFim = valorPartilhaUfFim;
	}

	public BigDecimal getValorPartilhaUfInicio() {
		return this.valorPartilhaUfInicio;
	}

	public void setValorPartilhaUfInicio(BigDecimal valorPartilhaUfInicio) {
		this.valorPartilhaUfInicio = valorPartilhaUfInicio;
	}

	public BigDecimal getValorTotalUfFimFcp() {
		return this.valorTotalUfFimFcp;
	}

	public void setValorTotalUfFimFcp(BigDecimal valorTotalUfFimFcp) {
		this.valorTotalUfFimFcp = valorTotalUfFimFcp;
	}

	public FinPagrec getFinPagrec() {
		return this.finPagrec;
	}

	public void setFinPagrec(FinPagrec finPagrec) {
		this.finPagrec = finPagrec;
	}

	public FisTributo getFisTributo() {
		return this.fisTributo;
	}

	public void setFisTributo(FisTributo fisTributo) {
		this.fisTributo = fisTributo;
	}

	public GerPessoaEndereco getGerPessoaEndereco() {
		return this.gerPessoaEndereco;
	}

	public void setGerPessoaEndereco(GerPessoaEndereco gerPessoaEndereco) {
		this.gerPessoaEndereco = gerPessoaEndereco;
	}

	public Mov getMov() {
		return this.mov;
	}

	public void setMov(Mov mov) {
		this.mov = mov;
	}

	public MovItemserv getMovItemserv() {
		return this.movItemserv;
	}

	public void setMovItemserv(MovItemserv movItemserv) {
		this.movItemserv = movItemserv;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}