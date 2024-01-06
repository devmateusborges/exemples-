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
@Table(name="ope_centro2_ord_rec")
@NamedQuery(name="OpeCentro2OrdRec.findAll", query="SELECT o FROM OpeCentro2OrdRec o")
public class OpeCentro2OrdRec implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

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

	@Column(name="observacao_externa", length=250)
	private String observacaoExterna;

	@Column(name="observacao_interna", length=250)
	private String observacaoInterna;

	@Column(name="perc_util", nullable=false, precision=18, scale=6)
	private BigDecimal percUtil;

	@Column(name="qnt_rend", nullable=false, precision=18, scale=6)
	private BigDecimal qntRend;

	@Column(name="qnt_total_util", nullable=false, precision=18, scale=6)
	private BigDecimal qntTotalUtil;

	@Column(name="valor_total_util", nullable=false, precision=18, scale=6)
	private BigDecimal valorTotalUtil;

	@Column(name="valor_unit_util", nullable=false, precision=18, scale=6)
	private BigDecimal valorUnitUtil;

	//bi-directional many-to-one association to CtbComp
	@ManyToOne
	@JoinColumn(name="ctb_comp_id", nullable=false)
	private CtbComp ctbComp1;

	//bi-directional many-to-one association to CtbComp
	@ManyToOne
	@JoinColumn(name="ctb_comp_id_imp01")
	private CtbComp ctbComp2;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_exec", nullable=false)
	private GerPessoaEndereco gerPessoaEndereco;

	//bi-directional many-to-one association to OpeCentro1
	@ManyToOne
	@JoinColumn(name="ope_centro1_id")
	private OpeCentro1 opeCentro11;

	//bi-directional many-to-one association to OpeCentro1
	@ManyToOne
	@JoinColumn(name="ope_centro1_id_imp01")
	private OpeCentro1 opeCentro12;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id")
	private OpeCentro2 opeCentro21;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id_imp01")
	private OpeCentro2 opeCentro22;

	//bi-directional many-to-one association to OpeCentro2OrdAtiv
	@ManyToOne
	@JoinColumn(name="ope_centro2_ord_ativ_id", nullable=false)
	private OpeCentro2OrdAtiv opeCentro2OrdAtiv;

	//bi-directional many-to-one association to OpeCompart
	@ManyToOne
	@JoinColumn(name="ope_compart_id")
	private OpeCompart opeCompart;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentro2OrdRec() {
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

	public String getObservacaoExterna() {
		return this.observacaoExterna;
	}

	public void setObservacaoExterna(String observacaoExterna) {
		this.observacaoExterna = observacaoExterna;
	}

	public String getObservacaoInterna() {
		return this.observacaoInterna;
	}

	public void setObservacaoInterna(String observacaoInterna) {
		this.observacaoInterna = observacaoInterna;
	}

	public BigDecimal getPercUtil() {
		return this.percUtil;
	}

	public void setPercUtil(BigDecimal percUtil) {
		this.percUtil = percUtil;
	}

	public BigDecimal getQntRend() {
		return this.qntRend;
	}

	public void setQntRend(BigDecimal qntRend) {
		this.qntRend = qntRend;
	}

	public BigDecimal getQntTotalUtil() {
		return this.qntTotalUtil;
	}

	public void setQntTotalUtil(BigDecimal qntTotalUtil) {
		this.qntTotalUtil = qntTotalUtil;
	}

	public BigDecimal getValorTotalUtil() {
		return this.valorTotalUtil;
	}

	public void setValorTotalUtil(BigDecimal valorTotalUtil) {
		this.valorTotalUtil = valorTotalUtil;
	}

	public BigDecimal getValorUnitUtil() {
		return this.valorUnitUtil;
	}

	public void setValorUnitUtil(BigDecimal valorUnitUtil) {
		this.valorUnitUtil = valorUnitUtil;
	}

	public CtbComp getCtbComp1() {
		return this.ctbComp1;
	}

	public void setCtbComp1(CtbComp ctbComp1) {
		this.ctbComp1 = ctbComp1;
	}

	public CtbComp getCtbComp2() {
		return this.ctbComp2;
	}

	public void setCtbComp2(CtbComp ctbComp2) {
		this.ctbComp2 = ctbComp2;
	}

	public GerPessoaEndereco getGerPessoaEndereco() {
		return this.gerPessoaEndereco;
	}

	public void setGerPessoaEndereco(GerPessoaEndereco gerPessoaEndereco) {
		this.gerPessoaEndereco = gerPessoaEndereco;
	}

	public OpeCentro1 getOpeCentro11() {
		return this.opeCentro11;
	}

	public void setOpeCentro11(OpeCentro1 opeCentro11) {
		this.opeCentro11 = opeCentro11;
	}

	public OpeCentro1 getOpeCentro12() {
		return this.opeCentro12;
	}

	public void setOpeCentro12(OpeCentro1 opeCentro12) {
		this.opeCentro12 = opeCentro12;
	}

	public OpeCentro2 getOpeCentro21() {
		return this.opeCentro21;
	}

	public void setOpeCentro21(OpeCentro2 opeCentro21) {
		this.opeCentro21 = opeCentro21;
	}

	public OpeCentro2 getOpeCentro22() {
		return this.opeCentro22;
	}

	public void setOpeCentro22(OpeCentro2 opeCentro22) {
		this.opeCentro22 = opeCentro22;
	}

	public OpeCentro2OrdAtiv getOpeCentro2OrdAtiv() {
		return this.opeCentro2OrdAtiv;
	}

	public void setOpeCentro2OrdAtiv(OpeCentro2OrdAtiv opeCentro2OrdAtiv) {
		this.opeCentro2OrdAtiv = opeCentro2OrdAtiv;
	}

	public OpeCompart getOpeCompart() {
		return this.opeCompart;
	}

	public void setOpeCompart(OpeCompart opeCompart) {
		this.opeCompart = opeCompart;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}