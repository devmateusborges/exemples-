package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="mov_frete")
@NamedQuery(name="MovFrete.findAll", query="SELECT m FROM MovFrete m")
public class MovFrete implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="adic_frete_base_cal_icms", nullable=false, length=1)
	private String adicFreteBaseCalIcms;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="perc_aliquota", nullable=false, precision=18, scale=6)
	private BigDecimal percAliquota;

	@Column(name="valor_base_calc", nullable=false, precision=18, scale=6)
	private BigDecimal valorBaseCalc;

	@Column(name="valor_cofins", nullable=false, precision=18, scale=6)
	private BigDecimal valorCofins;

	@Column(name="valor_frete", nullable=false, precision=18, scale=6)
	private BigDecimal valorFrete;

	@Column(name="valor_imposto", nullable=false, precision=18, scale=6)
	private BigDecimal valorImposto;

	@Column(name="valor_pis", nullable=false, precision=18, scale=6)
	private BigDecimal valorPis;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_condutor")
	private GerPessoaEndereco gerPessoaEndereco1;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_transp")
	private GerPessoaEndereco gerPessoaEndereco2;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id", nullable=false)
	private Mov mov;

	//bi-directional many-to-one association to OpeCentro2Equip
	@ManyToOne
	@JoinColumn(name="ope_centro2_id_equip")
	private OpeCentro2Equip opeCentro2Equip;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public MovFrete() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getAdicFreteBaseCalIcms() {
		return this.adicFreteBaseCalIcms;
	}

	public void setAdicFreteBaseCalIcms(String adicFreteBaseCalIcms) {
		this.adicFreteBaseCalIcms = adicFreteBaseCalIcms;
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

	public BigDecimal getPercAliquota() {
		return this.percAliquota;
	}

	public void setPercAliquota(BigDecimal percAliquota) {
		this.percAliquota = percAliquota;
	}

	public BigDecimal getValorBaseCalc() {
		return this.valorBaseCalc;
	}

	public void setValorBaseCalc(BigDecimal valorBaseCalc) {
		this.valorBaseCalc = valorBaseCalc;
	}

	public BigDecimal getValorCofins() {
		return this.valorCofins;
	}

	public void setValorCofins(BigDecimal valorCofins) {
		this.valorCofins = valorCofins;
	}

	public BigDecimal getValorFrete() {
		return this.valorFrete;
	}

	public void setValorFrete(BigDecimal valorFrete) {
		this.valorFrete = valorFrete;
	}

	public BigDecimal getValorImposto() {
		return this.valorImposto;
	}

	public void setValorImposto(BigDecimal valorImposto) {
		this.valorImposto = valorImposto;
	}

	public BigDecimal getValorPis() {
		return this.valorPis;
	}

	public void setValorPis(BigDecimal valorPis) {
		this.valorPis = valorPis;
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

	public Mov getMov() {
		return this.mov;
	}

	public void setMov(Mov mov) {
		this.mov = mov;
	}

	public OpeCentro2Equip getOpeCentro2Equip() {
		return this.opeCentro2Equip;
	}

	public void setOpeCentro2Equip(OpeCentro2Equip opeCentro2Equip) {
		this.opeCentro2Equip = opeCentro2Equip;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}