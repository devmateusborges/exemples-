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
@Table(name="mov_cotacao")
@NamedQuery(name="MovCotacao.findAll", query="SELECT m FROM MovCotacao m")
public class MovCotacao implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="data_status")
	private Timestamp dataStatus;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(length=250)
	private String observacao1;

	@Column(length=250)
	private String observacao2;

	@Column(name="qnt_cot", nullable=false, precision=18, scale=6)
	private BigDecimal qntCot;

	@Column(nullable=false, length=1)
	private String status;

	@Column(name="valor_desc_cot", nullable=false, precision=18, scale=6)
	private BigDecimal valorDescCot;

	@Column(name="valor_frete_cot", nullable=false, precision=18, scale=6)
	private BigDecimal valorFreteCot;

	@Column(name="valor_outro_cot", nullable=false, precision=18, scale=6)
	private BigDecimal valorOutroCot;

	@Column(name="valor_total_cot", nullable=false, precision=18, scale=6)
	private BigDecimal valorTotalCot;

	@Column(name="valor_total_trib_cot", nullable=false, precision=18, scale=6)
	private BigDecimal valorTotalTribCot;

	@Column(name="valor_unit_cot", nullable=false, precision=18, scale=6)
	private BigDecimal valorUnitCot;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="fin_cond_pagrec_id", nullable=false)
	private FinCondPagrec finCondPagrec;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id", nullable=false)
	private GerItemserv gerItemserv;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="ger_pessoa_id", nullable=false)
	private GerPessoa gerPessoa;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id", nullable=false)
	private Mov mov;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="sys_user_id_aprov")
	private SysUser sysUser;

	public MovCotacao() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Timestamp getDataStatus() {
		return this.dataStatus;
	}

	public void setDataStatus(Timestamp dataStatus) {
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

	public String getObservacao1() {
		return this.observacao1;
	}

	public void setObservacao1(String observacao1) {
		this.observacao1 = observacao1;
	}

	public String getObservacao2() {
		return this.observacao2;
	}

	public void setObservacao2(String observacao2) {
		this.observacao2 = observacao2;
	}

	public BigDecimal getQntCot() {
		return this.qntCot;
	}

	public void setQntCot(BigDecimal qntCot) {
		this.qntCot = qntCot;
	}

	public String getStatus() {
		return this.status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public BigDecimal getValorDescCot() {
		return this.valorDescCot;
	}

	public void setValorDescCot(BigDecimal valorDescCot) {
		this.valorDescCot = valorDescCot;
	}

	public BigDecimal getValorFreteCot() {
		return this.valorFreteCot;
	}

	public void setValorFreteCot(BigDecimal valorFreteCot) {
		this.valorFreteCot = valorFreteCot;
	}

	public BigDecimal getValorOutroCot() {
		return this.valorOutroCot;
	}

	public void setValorOutroCot(BigDecimal valorOutroCot) {
		this.valorOutroCot = valorOutroCot;
	}

	public BigDecimal getValorTotalCot() {
		return this.valorTotalCot;
	}

	public void setValorTotalCot(BigDecimal valorTotalCot) {
		this.valorTotalCot = valorTotalCot;
	}

	public BigDecimal getValorTotalTribCot() {
		return this.valorTotalTribCot;
	}

	public void setValorTotalTribCot(BigDecimal valorTotalTribCot) {
		this.valorTotalTribCot = valorTotalTribCot;
	}

	public BigDecimal getValorUnitCot() {
		return this.valorUnitCot;
	}

	public void setValorUnitCot(BigDecimal valorUnitCot) {
		this.valorUnitCot = valorUnitCot;
	}

	public FinCondPagrec getFinCondPagrec() {
		return this.finCondPagrec;
	}

	public void setFinCondPagrec(FinCondPagrec finCondPagrec) {
		this.finCondPagrec = finCondPagrec;
	}

	public GerItemserv getGerItemserv() {
		return this.gerItemserv;
	}

	public void setGerItemserv(GerItemserv gerItemserv) {
		this.gerItemserv = gerItemserv;
	}

	public GerPessoa getGerPessoa() {
		return this.gerPessoa;
	}

	public void setGerPessoa(GerPessoa gerPessoa) {
		this.gerPessoa = gerPessoa;
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

}