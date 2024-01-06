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
@Table(name="mov_cotacao_anal")
@NamedQuery(name="MovCotacaoAnal.findAll", query="SELECT m FROM MovCotacaoAnal m")
public class MovCotacaoAnal implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="c01_data_status")
	private Timestamp c01DataStatus;

	@Column(name="c01_observacao1", length=250)
	private String c01Observacao1;

	@Column(name="c01_observacao2", length=250)
	private String c01Observacao2;

	@Column(name="c01_qnt_cot", precision=18, scale=6)
	private BigDecimal c01QntCot;

	@Column(name="c01_status", length=1)
	private String c01Status;

	@Column(name="c01_valor_desc_cot", precision=18, scale=6)
	private BigDecimal c01ValorDescCot;

	@Column(name="c01_valor_frete_cot", precision=18, scale=6)
	private BigDecimal c01ValorFreteCot;

	@Column(name="c01_valor_outro_cot", precision=18, scale=6)
	private BigDecimal c01ValorOutroCot;

	@Column(name="c01_valor_total_cot", precision=18, scale=6)
	private BigDecimal c01ValorTotalCot;

	@Column(name="c01_valor_total_trib_cot", precision=18, scale=6)
	private BigDecimal c01ValorTotalTribCot;

	@Column(name="c01_valor_unit_cot", precision=18, scale=6)
	private BigDecimal c01ValorUnitCot;

	@Column(name="c02_data_status")
	private Timestamp c02DataStatus;

	@Column(name="c02_observacao1", length=250)
	private String c02Observacao1;

	@Column(name="c02_observacao2", length=250)
	private String c02Observacao2;

	@Column(name="c02_qnt_cot", precision=18, scale=6)
	private BigDecimal c02QntCot;

	@Column(name="c02_status", length=1)
	private String c02Status;

	@Column(name="c02_valor_desc_cot", precision=18, scale=6)
	private BigDecimal c02ValorDescCot;

	@Column(name="c02_valor_frete_cot", precision=18, scale=6)
	private BigDecimal c02ValorFreteCot;

	@Column(name="c02_valor_outro_cot", precision=18, scale=6)
	private BigDecimal c02ValorOutroCot;

	@Column(name="c02_valor_total_cot", precision=18, scale=6)
	private BigDecimal c02ValorTotalCot;

	@Column(name="c02_valor_total_trib_cot", precision=18, scale=6)
	private BigDecimal c02ValorTotalTribCot;

	@Column(name="c02_valor_unit_cot", precision=18, scale=6)
	private BigDecimal c02ValorUnitCot;

	@Column(name="c03_data_status")
	private Timestamp c03DataStatus;

	@Column(name="c03_observacao1", length=250)
	private String c03Observacao1;

	@Column(name="c03_observacao2", length=250)
	private String c03Observacao2;

	@Column(name="c03_qnt_cot", precision=18, scale=6)
	private BigDecimal c03QntCot;

	@Column(name="c03_status", length=1)
	private String c03Status;

	@Column(name="c03_valor_desc_cot", precision=18, scale=6)
	private BigDecimal c03ValorDescCot;

	@Column(name="c03_valor_frete_cot", precision=18, scale=6)
	private BigDecimal c03ValorFreteCot;

	@Column(name="c03_valor_outro_cot", precision=18, scale=6)
	private BigDecimal c03ValorOutroCot;

	@Column(name="c03_valor_total_cot", precision=18, scale=6)
	private BigDecimal c03ValorTotalCot;

	@Column(name="c03_valor_total_trib_cot", precision=18, scale=6)
	private BigDecimal c03ValorTotalTribCot;

	@Column(name="c03_valor_unit_cot", precision=18, scale=6)
	private BigDecimal c03ValorUnitCot;

	@Column(name="c04_data_status")
	private Timestamp c04DataStatus;

	@Column(name="c04_observacao1", length=250)
	private String c04Observacao1;

	@Column(name="c04_observacao2", length=250)
	private String c04Observacao2;

	@Column(name="c04_qnt_cot", precision=18, scale=6)
	private BigDecimal c04QntCot;

	@Column(name="c04_status", length=1)
	private String c04Status;

	@Column(name="c04_valor_desc_cot", precision=18, scale=6)
	private BigDecimal c04ValorDescCot;

	@Column(name="c04_valor_frete_cot", precision=18, scale=6)
	private BigDecimal c04ValorFreteCot;

	@Column(name="c04_valor_outro_cot", precision=18, scale=6)
	private BigDecimal c04ValorOutroCot;

	@Column(name="c04_valor_total_cot", precision=18, scale=6)
	private BigDecimal c04ValorTotalCot;

	@Column(name="c04_valor_total_trib_cot", precision=18, scale=6)
	private BigDecimal c04ValorTotalTribCot;

	@Column(name="c04_valor_unit_cot", precision=18, scale=6)
	private BigDecimal c04ValorUnitCot;

	@Column(name="c05_data_status")
	private Timestamp c05DataStatus;

	@Column(name="c05_observacao1", length=250)
	private String c05Observacao1;

	@Column(name="c05_observacao2", length=250)
	private String c05Observacao2;

	@Column(name="c05_qnt_cot", precision=18, scale=6)
	private BigDecimal c05QntCot;

	@Column(name="c05_status", length=1)
	private String c05Status;

	@Column(name="c05_valor_desc_cot", precision=18, scale=6)
	private BigDecimal c05ValorDescCot;

	@Column(name="c05_valor_frete_cot", precision=18, scale=6)
	private BigDecimal c05ValorFreteCot;

	@Column(name="c05_valor_outro_cot", precision=18, scale=6)
	private BigDecimal c05ValorOutroCot;

	@Column(name="c05_valor_total_cot", precision=18, scale=6)
	private BigDecimal c05ValorTotalCot;

	@Column(name="c05_valor_total_trib_cot", precision=18, scale=6)
	private BigDecimal c05ValorTotalTribCot;

	@Column(name="c05_valor_unit_cot", precision=18, scale=6)
	private BigDecimal c05ValorUnitCot;

	@Column(name="c06_data_status")
	private Timestamp c06DataStatus;

	@Column(name="c06_observacao1", length=250)
	private String c06Observacao1;

	@Column(name="c06_observacao2", length=250)
	private String c06Observacao2;

	@Column(name="c06_qnt_cot", precision=18, scale=6)
	private BigDecimal c06QntCot;

	@Column(name="c06_status", length=1)
	private String c06Status;

	@Column(name="c06_valor_desc_cot", precision=18, scale=6)
	private BigDecimal c06ValorDescCot;

	@Column(name="c06_valor_frete_cot", precision=18, scale=6)
	private BigDecimal c06ValorFreteCot;

	@Column(name="c06_valor_outro_cot", precision=18, scale=6)
	private BigDecimal c06ValorOutroCot;

	@Column(name="c06_valor_total_cot", precision=18, scale=6)
	private BigDecimal c06ValorTotalCot;

	@Column(name="c06_valor_total_trib_cot", precision=18, scale=6)
	private BigDecimal c06ValorTotalTribCot;

	@Column(name="c06_valor_unit_cot", precision=18, scale=6)
	private BigDecimal c06ValorUnitCot;

	@Column(name="c07_data_status")
	private Timestamp c07DataStatus;

	@Column(name="c07_observacao1", length=250)
	private String c07Observacao1;

	@Column(name="c07_observacao2", length=250)
	private String c07Observacao2;

	@Column(name="c07_qnt_cot", precision=18, scale=6)
	private BigDecimal c07QntCot;

	@Column(name="c07_status", length=1)
	private String c07Status;

	@Column(name="c07_valor_desc_cot", precision=18, scale=6)
	private BigDecimal c07ValorDescCot;

	@Column(name="c07_valor_frete_cot", precision=18, scale=6)
	private BigDecimal c07ValorFreteCot;

	@Column(name="c07_valor_outro_cot", precision=18, scale=6)
	private BigDecimal c07ValorOutroCot;

	@Column(name="c07_valor_total_cot", precision=18, scale=6)
	private BigDecimal c07ValorTotalCot;

	@Column(name="c07_valor_total_trib_cot", precision=18, scale=6)
	private BigDecimal c07ValorTotalTribCot;

	@Column(name="c07_valor_unit_cot", precision=18, scale=6)
	private BigDecimal c07ValorUnitCot;

	@Column(name="c08_data_status")
	private Timestamp c08DataStatus;

	@Column(name="c08_observacao1", length=250)
	private String c08Observacao1;

	@Column(name="c08_observacao2", length=250)
	private String c08Observacao2;

	@Column(name="c08_qnt_cot", precision=18, scale=6)
	private BigDecimal c08QntCot;

	@Column(name="c08_status", length=1)
	private String c08Status;

	@Column(name="c08_valor_desc_cot", precision=18, scale=6)
	private BigDecimal c08ValorDescCot;

	@Column(name="c08_valor_frete_cot", precision=18, scale=6)
	private BigDecimal c08ValorFreteCot;

	@Column(name="c08_valor_outro_cot", precision=18, scale=6)
	private BigDecimal c08ValorOutroCot;

	@Column(name="c08_valor_total_cot", precision=18, scale=6)
	private BigDecimal c08ValorTotalCot;

	@Column(name="c08_valor_total_trib_cot", precision=18, scale=6)
	private BigDecimal c08ValorTotalTribCot;

	@Column(name="c08_valor_unit_cot", precision=18, scale=6)
	private BigDecimal c08ValorUnitCot;

	@Column(name="c09_data_status")
	private Timestamp c09DataStatus;

	@Column(name="c09_observacao1", length=250)
	private String c09Observacao1;

	@Column(name="c09_observacao2", length=250)
	private String c09Observacao2;

	@Column(name="c09_qnt_cot", precision=18, scale=6)
	private BigDecimal c09QntCot;

	@Column(name="c09_status", length=1)
	private String c09Status;

	@Column(name="c09_valor_desc_cot", precision=18, scale=6)
	private BigDecimal c09ValorDescCot;

	@Column(name="c09_valor_frete_cot", precision=18, scale=6)
	private BigDecimal c09ValorFreteCot;

	@Column(name="c09_valor_outro_cot", precision=18, scale=6)
	private BigDecimal c09ValorOutroCot;

	@Column(name="c09_valor_total_cot", precision=18, scale=6)
	private BigDecimal c09ValorTotalCot;

	@Column(name="c09_valor_total_trib_cot", precision=18, scale=6)
	private BigDecimal c09ValorTotalTribCot;

	@Column(name="c09_valor_unit_cot", precision=18, scale=6)
	private BigDecimal c09ValorUnitCot;

	@Column(name="c10_data_status")
	private Timestamp c10DataStatus;

	@Column(name="c10_observacao1", length=250)
	private String c10Observacao1;

	@Column(name="c10_observacao2", length=250)
	private String c10Observacao2;

	@Column(name="c10_qnt_cot", precision=18, scale=6)
	private BigDecimal c10QntCot;

	@Column(name="c10_status", length=1)
	private String c10Status;

	@Column(name="c10_valor_desc_cot", precision=18, scale=6)
	private BigDecimal c10ValorDescCot;

	@Column(name="c10_valor_frete_cot", precision=18, scale=6)
	private BigDecimal c10ValorFreteCot;

	@Column(name="c10_valor_outro_cot", precision=18, scale=6)
	private BigDecimal c10ValorOutroCot;

	@Column(name="c10_valor_total_cot", precision=18, scale=6)
	private BigDecimal c10ValorTotalCot;

	@Column(name="c10_valor_total_trib_cot", precision=18, scale=6)
	private BigDecimal c10ValorTotalTribCot;

	@Column(name="c10_valor_unit_cot", precision=18, scale=6)
	private BigDecimal c10ValorUnitCot;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="c01_fin_cond_pagrec_id")
	private FinCondPagrec finCondPagrec1;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="c02_fin_cond_pagrec_id")
	private FinCondPagrec finCondPagrec2;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="c03_fin_cond_pagrec_id")
	private FinCondPagrec finCondPagrec3;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="c04_fin_cond_pagrec_id")
	private FinCondPagrec finCondPagrec4;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="c05_fin_cond_pagrec_id")
	private FinCondPagrec finCondPagrec5;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="c06_fin_cond_pagrec_id")
	private FinCondPagrec finCondPagrec6;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="c07_fin_cond_pagrec_id")
	private FinCondPagrec finCondPagrec7;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="c08_fin_cond_pagrec_id")
	private FinCondPagrec finCondPagrec8;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="c09_fin_cond_pagrec_id")
	private FinCondPagrec finCondPagrec9;

	//bi-directional many-to-one association to FinCondPagrec
	@ManyToOne
	@JoinColumn(name="c10_fin_cond_pagrec_id")
	private FinCondPagrec finCondPagrec10;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id", nullable=false)
	private GerItemserv gerItemserv;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="c01_ger_pessoa_id")
	private GerPessoa gerPessoa1;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="c02_ger_pessoa_id")
	private GerPessoa gerPessoa2;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="c03_ger_pessoa_id")
	private GerPessoa gerPessoa3;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="c04_ger_pessoa_id")
	private GerPessoa gerPessoa4;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="c05_ger_pessoa_id")
	private GerPessoa gerPessoa5;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="c06_ger_pessoa_id")
	private GerPessoa gerPessoa6;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="c07_ger_pessoa_id")
	private GerPessoa gerPessoa7;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="c08_ger_pessoa_id")
	private GerPessoa gerPessoa8;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="c09_ger_pessoa_id")
	private GerPessoa gerPessoa9;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="c10_ger_pessoa_id")
	private GerPessoa gerPessoa10;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="c01_ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco1;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="c02_ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco2;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="c03_ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco3;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="c04_ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco4;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="c05_ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco5;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="c06_ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco6;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="c07_ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco7;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="c08_ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco8;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="c09_ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco9;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="c10_ger_pessoa_endereco_id")
	private GerPessoaEndereco gerPessoaEndereco10;

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
	@JoinColumn(name="c01_sys_user_id_aprov")
	private SysUser sysUser1;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="c02_sys_user_id_aprov")
	private SysUser sysUser2;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="c03_sys_user_id_aprov")
	private SysUser sysUser3;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="c04_sys_user_id_aprov")
	private SysUser sysUser4;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="c05_sys_user_id_aprov")
	private SysUser sysUser5;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="c06_sys_user_id_aprov")
	private SysUser sysUser6;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="c07_sys_user_id_aprov")
	private SysUser sysUser7;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="c08_sys_user_id_aprov")
	private SysUser sysUser8;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="c09_sys_user_id_aprov")
	private SysUser sysUser9;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="c10_sys_user_id_aprov")
	private SysUser sysUser10;

	public MovCotacaoAnal() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Timestamp getC01DataStatus() {
		return this.c01DataStatus;
	}

	public void setC01DataStatus(Timestamp c01DataStatus) {
		this.c01DataStatus = c01DataStatus;
	}

	public String getC01Observacao1() {
		return this.c01Observacao1;
	}

	public void setC01Observacao1(String c01Observacao1) {
		this.c01Observacao1 = c01Observacao1;
	}

	public String getC01Observacao2() {
		return this.c01Observacao2;
	}

	public void setC01Observacao2(String c01Observacao2) {
		this.c01Observacao2 = c01Observacao2;
	}

	public BigDecimal getC01QntCot() {
		return this.c01QntCot;
	}

	public void setC01QntCot(BigDecimal c01QntCot) {
		this.c01QntCot = c01QntCot;
	}

	public String getC01Status() {
		return this.c01Status;
	}

	public void setC01Status(String c01Status) {
		this.c01Status = c01Status;
	}

	public BigDecimal getC01ValorDescCot() {
		return this.c01ValorDescCot;
	}

	public void setC01ValorDescCot(BigDecimal c01ValorDescCot) {
		this.c01ValorDescCot = c01ValorDescCot;
	}

	public BigDecimal getC01ValorFreteCot() {
		return this.c01ValorFreteCot;
	}

	public void setC01ValorFreteCot(BigDecimal c01ValorFreteCot) {
		this.c01ValorFreteCot = c01ValorFreteCot;
	}

	public BigDecimal getC01ValorOutroCot() {
		return this.c01ValorOutroCot;
	}

	public void setC01ValorOutroCot(BigDecimal c01ValorOutroCot) {
		this.c01ValorOutroCot = c01ValorOutroCot;
	}

	public BigDecimal getC01ValorTotalCot() {
		return this.c01ValorTotalCot;
	}

	public void setC01ValorTotalCot(BigDecimal c01ValorTotalCot) {
		this.c01ValorTotalCot = c01ValorTotalCot;
	}

	public BigDecimal getC01ValorTotalTribCot() {
		return this.c01ValorTotalTribCot;
	}

	public void setC01ValorTotalTribCot(BigDecimal c01ValorTotalTribCot) {
		this.c01ValorTotalTribCot = c01ValorTotalTribCot;
	}

	public BigDecimal getC01ValorUnitCot() {
		return this.c01ValorUnitCot;
	}

	public void setC01ValorUnitCot(BigDecimal c01ValorUnitCot) {
		this.c01ValorUnitCot = c01ValorUnitCot;
	}

	public Timestamp getC02DataStatus() {
		return this.c02DataStatus;
	}

	public void setC02DataStatus(Timestamp c02DataStatus) {
		this.c02DataStatus = c02DataStatus;
	}

	public String getC02Observacao1() {
		return this.c02Observacao1;
	}

	public void setC02Observacao1(String c02Observacao1) {
		this.c02Observacao1 = c02Observacao1;
	}

	public String getC02Observacao2() {
		return this.c02Observacao2;
	}

	public void setC02Observacao2(String c02Observacao2) {
		this.c02Observacao2 = c02Observacao2;
	}

	public BigDecimal getC02QntCot() {
		return this.c02QntCot;
	}

	public void setC02QntCot(BigDecimal c02QntCot) {
		this.c02QntCot = c02QntCot;
	}

	public String getC02Status() {
		return this.c02Status;
	}

	public void setC02Status(String c02Status) {
		this.c02Status = c02Status;
	}

	public BigDecimal getC02ValorDescCot() {
		return this.c02ValorDescCot;
	}

	public void setC02ValorDescCot(BigDecimal c02ValorDescCot) {
		this.c02ValorDescCot = c02ValorDescCot;
	}

	public BigDecimal getC02ValorFreteCot() {
		return this.c02ValorFreteCot;
	}

	public void setC02ValorFreteCot(BigDecimal c02ValorFreteCot) {
		this.c02ValorFreteCot = c02ValorFreteCot;
	}

	public BigDecimal getC02ValorOutroCot() {
		return this.c02ValorOutroCot;
	}

	public void setC02ValorOutroCot(BigDecimal c02ValorOutroCot) {
		this.c02ValorOutroCot = c02ValorOutroCot;
	}

	public BigDecimal getC02ValorTotalCot() {
		return this.c02ValorTotalCot;
	}

	public void setC02ValorTotalCot(BigDecimal c02ValorTotalCot) {
		this.c02ValorTotalCot = c02ValorTotalCot;
	}

	public BigDecimal getC02ValorTotalTribCot() {
		return this.c02ValorTotalTribCot;
	}

	public void setC02ValorTotalTribCot(BigDecimal c02ValorTotalTribCot) {
		this.c02ValorTotalTribCot = c02ValorTotalTribCot;
	}

	public BigDecimal getC02ValorUnitCot() {
		return this.c02ValorUnitCot;
	}

	public void setC02ValorUnitCot(BigDecimal c02ValorUnitCot) {
		this.c02ValorUnitCot = c02ValorUnitCot;
	}

	public Timestamp getC03DataStatus() {
		return this.c03DataStatus;
	}

	public void setC03DataStatus(Timestamp c03DataStatus) {
		this.c03DataStatus = c03DataStatus;
	}

	public String getC03Observacao1() {
		return this.c03Observacao1;
	}

	public void setC03Observacao1(String c03Observacao1) {
		this.c03Observacao1 = c03Observacao1;
	}

	public String getC03Observacao2() {
		return this.c03Observacao2;
	}

	public void setC03Observacao2(String c03Observacao2) {
		this.c03Observacao2 = c03Observacao2;
	}

	public BigDecimal getC03QntCot() {
		return this.c03QntCot;
	}

	public void setC03QntCot(BigDecimal c03QntCot) {
		this.c03QntCot = c03QntCot;
	}

	public String getC03Status() {
		return this.c03Status;
	}

	public void setC03Status(String c03Status) {
		this.c03Status = c03Status;
	}

	public BigDecimal getC03ValorDescCot() {
		return this.c03ValorDescCot;
	}

	public void setC03ValorDescCot(BigDecimal c03ValorDescCot) {
		this.c03ValorDescCot = c03ValorDescCot;
	}

	public BigDecimal getC03ValorFreteCot() {
		return this.c03ValorFreteCot;
	}

	public void setC03ValorFreteCot(BigDecimal c03ValorFreteCot) {
		this.c03ValorFreteCot = c03ValorFreteCot;
	}

	public BigDecimal getC03ValorOutroCot() {
		return this.c03ValorOutroCot;
	}

	public void setC03ValorOutroCot(BigDecimal c03ValorOutroCot) {
		this.c03ValorOutroCot = c03ValorOutroCot;
	}

	public BigDecimal getC03ValorTotalCot() {
		return this.c03ValorTotalCot;
	}

	public void setC03ValorTotalCot(BigDecimal c03ValorTotalCot) {
		this.c03ValorTotalCot = c03ValorTotalCot;
	}

	public BigDecimal getC03ValorTotalTribCot() {
		return this.c03ValorTotalTribCot;
	}

	public void setC03ValorTotalTribCot(BigDecimal c03ValorTotalTribCot) {
		this.c03ValorTotalTribCot = c03ValorTotalTribCot;
	}

	public BigDecimal getC03ValorUnitCot() {
		return this.c03ValorUnitCot;
	}

	public void setC03ValorUnitCot(BigDecimal c03ValorUnitCot) {
		this.c03ValorUnitCot = c03ValorUnitCot;
	}

	public Timestamp getC04DataStatus() {
		return this.c04DataStatus;
	}

	public void setC04DataStatus(Timestamp c04DataStatus) {
		this.c04DataStatus = c04DataStatus;
	}

	public String getC04Observacao1() {
		return this.c04Observacao1;
	}

	public void setC04Observacao1(String c04Observacao1) {
		this.c04Observacao1 = c04Observacao1;
	}

	public String getC04Observacao2() {
		return this.c04Observacao2;
	}

	public void setC04Observacao2(String c04Observacao2) {
		this.c04Observacao2 = c04Observacao2;
	}

	public BigDecimal getC04QntCot() {
		return this.c04QntCot;
	}

	public void setC04QntCot(BigDecimal c04QntCot) {
		this.c04QntCot = c04QntCot;
	}

	public String getC04Status() {
		return this.c04Status;
	}

	public void setC04Status(String c04Status) {
		this.c04Status = c04Status;
	}

	public BigDecimal getC04ValorDescCot() {
		return this.c04ValorDescCot;
	}

	public void setC04ValorDescCot(BigDecimal c04ValorDescCot) {
		this.c04ValorDescCot = c04ValorDescCot;
	}

	public BigDecimal getC04ValorFreteCot() {
		return this.c04ValorFreteCot;
	}

	public void setC04ValorFreteCot(BigDecimal c04ValorFreteCot) {
		this.c04ValorFreteCot = c04ValorFreteCot;
	}

	public BigDecimal getC04ValorOutroCot() {
		return this.c04ValorOutroCot;
	}

	public void setC04ValorOutroCot(BigDecimal c04ValorOutroCot) {
		this.c04ValorOutroCot = c04ValorOutroCot;
	}

	public BigDecimal getC04ValorTotalCot() {
		return this.c04ValorTotalCot;
	}

	public void setC04ValorTotalCot(BigDecimal c04ValorTotalCot) {
		this.c04ValorTotalCot = c04ValorTotalCot;
	}

	public BigDecimal getC04ValorTotalTribCot() {
		return this.c04ValorTotalTribCot;
	}

	public void setC04ValorTotalTribCot(BigDecimal c04ValorTotalTribCot) {
		this.c04ValorTotalTribCot = c04ValorTotalTribCot;
	}

	public BigDecimal getC04ValorUnitCot() {
		return this.c04ValorUnitCot;
	}

	public void setC04ValorUnitCot(BigDecimal c04ValorUnitCot) {
		this.c04ValorUnitCot = c04ValorUnitCot;
	}

	public Timestamp getC05DataStatus() {
		return this.c05DataStatus;
	}

	public void setC05DataStatus(Timestamp c05DataStatus) {
		this.c05DataStatus = c05DataStatus;
	}

	public String getC05Observacao1() {
		return this.c05Observacao1;
	}

	public void setC05Observacao1(String c05Observacao1) {
		this.c05Observacao1 = c05Observacao1;
	}

	public String getC05Observacao2() {
		return this.c05Observacao2;
	}

	public void setC05Observacao2(String c05Observacao2) {
		this.c05Observacao2 = c05Observacao2;
	}

	public BigDecimal getC05QntCot() {
		return this.c05QntCot;
	}

	public void setC05QntCot(BigDecimal c05QntCot) {
		this.c05QntCot = c05QntCot;
	}

	public String getC05Status() {
		return this.c05Status;
	}

	public void setC05Status(String c05Status) {
		this.c05Status = c05Status;
	}

	public BigDecimal getC05ValorDescCot() {
		return this.c05ValorDescCot;
	}

	public void setC05ValorDescCot(BigDecimal c05ValorDescCot) {
		this.c05ValorDescCot = c05ValorDescCot;
	}

	public BigDecimal getC05ValorFreteCot() {
		return this.c05ValorFreteCot;
	}

	public void setC05ValorFreteCot(BigDecimal c05ValorFreteCot) {
		this.c05ValorFreteCot = c05ValorFreteCot;
	}

	public BigDecimal getC05ValorOutroCot() {
		return this.c05ValorOutroCot;
	}

	public void setC05ValorOutroCot(BigDecimal c05ValorOutroCot) {
		this.c05ValorOutroCot = c05ValorOutroCot;
	}

	public BigDecimal getC05ValorTotalCot() {
		return this.c05ValorTotalCot;
	}

	public void setC05ValorTotalCot(BigDecimal c05ValorTotalCot) {
		this.c05ValorTotalCot = c05ValorTotalCot;
	}

	public BigDecimal getC05ValorTotalTribCot() {
		return this.c05ValorTotalTribCot;
	}

	public void setC05ValorTotalTribCot(BigDecimal c05ValorTotalTribCot) {
		this.c05ValorTotalTribCot = c05ValorTotalTribCot;
	}

	public BigDecimal getC05ValorUnitCot() {
		return this.c05ValorUnitCot;
	}

	public void setC05ValorUnitCot(BigDecimal c05ValorUnitCot) {
		this.c05ValorUnitCot = c05ValorUnitCot;
	}

	public Timestamp getC06DataStatus() {
		return this.c06DataStatus;
	}

	public void setC06DataStatus(Timestamp c06DataStatus) {
		this.c06DataStatus = c06DataStatus;
	}

	public String getC06Observacao1() {
		return this.c06Observacao1;
	}

	public void setC06Observacao1(String c06Observacao1) {
		this.c06Observacao1 = c06Observacao1;
	}

	public String getC06Observacao2() {
		return this.c06Observacao2;
	}

	public void setC06Observacao2(String c06Observacao2) {
		this.c06Observacao2 = c06Observacao2;
	}

	public BigDecimal getC06QntCot() {
		return this.c06QntCot;
	}

	public void setC06QntCot(BigDecimal c06QntCot) {
		this.c06QntCot = c06QntCot;
	}

	public String getC06Status() {
		return this.c06Status;
	}

	public void setC06Status(String c06Status) {
		this.c06Status = c06Status;
	}

	public BigDecimal getC06ValorDescCot() {
		return this.c06ValorDescCot;
	}

	public void setC06ValorDescCot(BigDecimal c06ValorDescCot) {
		this.c06ValorDescCot = c06ValorDescCot;
	}

	public BigDecimal getC06ValorFreteCot() {
		return this.c06ValorFreteCot;
	}

	public void setC06ValorFreteCot(BigDecimal c06ValorFreteCot) {
		this.c06ValorFreteCot = c06ValorFreteCot;
	}

	public BigDecimal getC06ValorOutroCot() {
		return this.c06ValorOutroCot;
	}

	public void setC06ValorOutroCot(BigDecimal c06ValorOutroCot) {
		this.c06ValorOutroCot = c06ValorOutroCot;
	}

	public BigDecimal getC06ValorTotalCot() {
		return this.c06ValorTotalCot;
	}

	public void setC06ValorTotalCot(BigDecimal c06ValorTotalCot) {
		this.c06ValorTotalCot = c06ValorTotalCot;
	}

	public BigDecimal getC06ValorTotalTribCot() {
		return this.c06ValorTotalTribCot;
	}

	public void setC06ValorTotalTribCot(BigDecimal c06ValorTotalTribCot) {
		this.c06ValorTotalTribCot = c06ValorTotalTribCot;
	}

	public BigDecimal getC06ValorUnitCot() {
		return this.c06ValorUnitCot;
	}

	public void setC06ValorUnitCot(BigDecimal c06ValorUnitCot) {
		this.c06ValorUnitCot = c06ValorUnitCot;
	}

	public Timestamp getC07DataStatus() {
		return this.c07DataStatus;
	}

	public void setC07DataStatus(Timestamp c07DataStatus) {
		this.c07DataStatus = c07DataStatus;
	}

	public String getC07Observacao1() {
		return this.c07Observacao1;
	}

	public void setC07Observacao1(String c07Observacao1) {
		this.c07Observacao1 = c07Observacao1;
	}

	public String getC07Observacao2() {
		return this.c07Observacao2;
	}

	public void setC07Observacao2(String c07Observacao2) {
		this.c07Observacao2 = c07Observacao2;
	}

	public BigDecimal getC07QntCot() {
		return this.c07QntCot;
	}

	public void setC07QntCot(BigDecimal c07QntCot) {
		this.c07QntCot = c07QntCot;
	}

	public String getC07Status() {
		return this.c07Status;
	}

	public void setC07Status(String c07Status) {
		this.c07Status = c07Status;
	}

	public BigDecimal getC07ValorDescCot() {
		return this.c07ValorDescCot;
	}

	public void setC07ValorDescCot(BigDecimal c07ValorDescCot) {
		this.c07ValorDescCot = c07ValorDescCot;
	}

	public BigDecimal getC07ValorFreteCot() {
		return this.c07ValorFreteCot;
	}

	public void setC07ValorFreteCot(BigDecimal c07ValorFreteCot) {
		this.c07ValorFreteCot = c07ValorFreteCot;
	}

	public BigDecimal getC07ValorOutroCot() {
		return this.c07ValorOutroCot;
	}

	public void setC07ValorOutroCot(BigDecimal c07ValorOutroCot) {
		this.c07ValorOutroCot = c07ValorOutroCot;
	}

	public BigDecimal getC07ValorTotalCot() {
		return this.c07ValorTotalCot;
	}

	public void setC07ValorTotalCot(BigDecimal c07ValorTotalCot) {
		this.c07ValorTotalCot = c07ValorTotalCot;
	}

	public BigDecimal getC07ValorTotalTribCot() {
		return this.c07ValorTotalTribCot;
	}

	public void setC07ValorTotalTribCot(BigDecimal c07ValorTotalTribCot) {
		this.c07ValorTotalTribCot = c07ValorTotalTribCot;
	}

	public BigDecimal getC07ValorUnitCot() {
		return this.c07ValorUnitCot;
	}

	public void setC07ValorUnitCot(BigDecimal c07ValorUnitCot) {
		this.c07ValorUnitCot = c07ValorUnitCot;
	}

	public Timestamp getC08DataStatus() {
		return this.c08DataStatus;
	}

	public void setC08DataStatus(Timestamp c08DataStatus) {
		this.c08DataStatus = c08DataStatus;
	}

	public String getC08Observacao1() {
		return this.c08Observacao1;
	}

	public void setC08Observacao1(String c08Observacao1) {
		this.c08Observacao1 = c08Observacao1;
	}

	public String getC08Observacao2() {
		return this.c08Observacao2;
	}

	public void setC08Observacao2(String c08Observacao2) {
		this.c08Observacao2 = c08Observacao2;
	}

	public BigDecimal getC08QntCot() {
		return this.c08QntCot;
	}

	public void setC08QntCot(BigDecimal c08QntCot) {
		this.c08QntCot = c08QntCot;
	}

	public String getC08Status() {
		return this.c08Status;
	}

	public void setC08Status(String c08Status) {
		this.c08Status = c08Status;
	}

	public BigDecimal getC08ValorDescCot() {
		return this.c08ValorDescCot;
	}

	public void setC08ValorDescCot(BigDecimal c08ValorDescCot) {
		this.c08ValorDescCot = c08ValorDescCot;
	}

	public BigDecimal getC08ValorFreteCot() {
		return this.c08ValorFreteCot;
	}

	public void setC08ValorFreteCot(BigDecimal c08ValorFreteCot) {
		this.c08ValorFreteCot = c08ValorFreteCot;
	}

	public BigDecimal getC08ValorOutroCot() {
		return this.c08ValorOutroCot;
	}

	public void setC08ValorOutroCot(BigDecimal c08ValorOutroCot) {
		this.c08ValorOutroCot = c08ValorOutroCot;
	}

	public BigDecimal getC08ValorTotalCot() {
		return this.c08ValorTotalCot;
	}

	public void setC08ValorTotalCot(BigDecimal c08ValorTotalCot) {
		this.c08ValorTotalCot = c08ValorTotalCot;
	}

	public BigDecimal getC08ValorTotalTribCot() {
		return this.c08ValorTotalTribCot;
	}

	public void setC08ValorTotalTribCot(BigDecimal c08ValorTotalTribCot) {
		this.c08ValorTotalTribCot = c08ValorTotalTribCot;
	}

	public BigDecimal getC08ValorUnitCot() {
		return this.c08ValorUnitCot;
	}

	public void setC08ValorUnitCot(BigDecimal c08ValorUnitCot) {
		this.c08ValorUnitCot = c08ValorUnitCot;
	}

	public Timestamp getC09DataStatus() {
		return this.c09DataStatus;
	}

	public void setC09DataStatus(Timestamp c09DataStatus) {
		this.c09DataStatus = c09DataStatus;
	}

	public String getC09Observacao1() {
		return this.c09Observacao1;
	}

	public void setC09Observacao1(String c09Observacao1) {
		this.c09Observacao1 = c09Observacao1;
	}

	public String getC09Observacao2() {
		return this.c09Observacao2;
	}

	public void setC09Observacao2(String c09Observacao2) {
		this.c09Observacao2 = c09Observacao2;
	}

	public BigDecimal getC09QntCot() {
		return this.c09QntCot;
	}

	public void setC09QntCot(BigDecimal c09QntCot) {
		this.c09QntCot = c09QntCot;
	}

	public String getC09Status() {
		return this.c09Status;
	}

	public void setC09Status(String c09Status) {
		this.c09Status = c09Status;
	}

	public BigDecimal getC09ValorDescCot() {
		return this.c09ValorDescCot;
	}

	public void setC09ValorDescCot(BigDecimal c09ValorDescCot) {
		this.c09ValorDescCot = c09ValorDescCot;
	}

	public BigDecimal getC09ValorFreteCot() {
		return this.c09ValorFreteCot;
	}

	public void setC09ValorFreteCot(BigDecimal c09ValorFreteCot) {
		this.c09ValorFreteCot = c09ValorFreteCot;
	}

	public BigDecimal getC09ValorOutroCot() {
		return this.c09ValorOutroCot;
	}

	public void setC09ValorOutroCot(BigDecimal c09ValorOutroCot) {
		this.c09ValorOutroCot = c09ValorOutroCot;
	}

	public BigDecimal getC09ValorTotalCot() {
		return this.c09ValorTotalCot;
	}

	public void setC09ValorTotalCot(BigDecimal c09ValorTotalCot) {
		this.c09ValorTotalCot = c09ValorTotalCot;
	}

	public BigDecimal getC09ValorTotalTribCot() {
		return this.c09ValorTotalTribCot;
	}

	public void setC09ValorTotalTribCot(BigDecimal c09ValorTotalTribCot) {
		this.c09ValorTotalTribCot = c09ValorTotalTribCot;
	}

	public BigDecimal getC09ValorUnitCot() {
		return this.c09ValorUnitCot;
	}

	public void setC09ValorUnitCot(BigDecimal c09ValorUnitCot) {
		this.c09ValorUnitCot = c09ValorUnitCot;
	}

	public Timestamp getC10DataStatus() {
		return this.c10DataStatus;
	}

	public void setC10DataStatus(Timestamp c10DataStatus) {
		this.c10DataStatus = c10DataStatus;
	}

	public String getC10Observacao1() {
		return this.c10Observacao1;
	}

	public void setC10Observacao1(String c10Observacao1) {
		this.c10Observacao1 = c10Observacao1;
	}

	public String getC10Observacao2() {
		return this.c10Observacao2;
	}

	public void setC10Observacao2(String c10Observacao2) {
		this.c10Observacao2 = c10Observacao2;
	}

	public BigDecimal getC10QntCot() {
		return this.c10QntCot;
	}

	public void setC10QntCot(BigDecimal c10QntCot) {
		this.c10QntCot = c10QntCot;
	}

	public String getC10Status() {
		return this.c10Status;
	}

	public void setC10Status(String c10Status) {
		this.c10Status = c10Status;
	}

	public BigDecimal getC10ValorDescCot() {
		return this.c10ValorDescCot;
	}

	public void setC10ValorDescCot(BigDecimal c10ValorDescCot) {
		this.c10ValorDescCot = c10ValorDescCot;
	}

	public BigDecimal getC10ValorFreteCot() {
		return this.c10ValorFreteCot;
	}

	public void setC10ValorFreteCot(BigDecimal c10ValorFreteCot) {
		this.c10ValorFreteCot = c10ValorFreteCot;
	}

	public BigDecimal getC10ValorOutroCot() {
		return this.c10ValorOutroCot;
	}

	public void setC10ValorOutroCot(BigDecimal c10ValorOutroCot) {
		this.c10ValorOutroCot = c10ValorOutroCot;
	}

	public BigDecimal getC10ValorTotalCot() {
		return this.c10ValorTotalCot;
	}

	public void setC10ValorTotalCot(BigDecimal c10ValorTotalCot) {
		this.c10ValorTotalCot = c10ValorTotalCot;
	}

	public BigDecimal getC10ValorTotalTribCot() {
		return this.c10ValorTotalTribCot;
	}

	public void setC10ValorTotalTribCot(BigDecimal c10ValorTotalTribCot) {
		this.c10ValorTotalTribCot = c10ValorTotalTribCot;
	}

	public BigDecimal getC10ValorUnitCot() {
		return this.c10ValorUnitCot;
	}

	public void setC10ValorUnitCot(BigDecimal c10ValorUnitCot) {
		this.c10ValorUnitCot = c10ValorUnitCot;
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

	public FinCondPagrec getFinCondPagrec1() {
		return this.finCondPagrec1;
	}

	public void setFinCondPagrec1(FinCondPagrec finCondPagrec1) {
		this.finCondPagrec1 = finCondPagrec1;
	}

	public FinCondPagrec getFinCondPagrec2() {
		return this.finCondPagrec2;
	}

	public void setFinCondPagrec2(FinCondPagrec finCondPagrec2) {
		this.finCondPagrec2 = finCondPagrec2;
	}

	public FinCondPagrec getFinCondPagrec3() {
		return this.finCondPagrec3;
	}

	public void setFinCondPagrec3(FinCondPagrec finCondPagrec3) {
		this.finCondPagrec3 = finCondPagrec3;
	}

	public FinCondPagrec getFinCondPagrec4() {
		return this.finCondPagrec4;
	}

	public void setFinCondPagrec4(FinCondPagrec finCondPagrec4) {
		this.finCondPagrec4 = finCondPagrec4;
	}

	public FinCondPagrec getFinCondPagrec5() {
		return this.finCondPagrec5;
	}

	public void setFinCondPagrec5(FinCondPagrec finCondPagrec5) {
		this.finCondPagrec5 = finCondPagrec5;
	}

	public FinCondPagrec getFinCondPagrec6() {
		return this.finCondPagrec6;
	}

	public void setFinCondPagrec6(FinCondPagrec finCondPagrec6) {
		this.finCondPagrec6 = finCondPagrec6;
	}

	public FinCondPagrec getFinCondPagrec7() {
		return this.finCondPagrec7;
	}

	public void setFinCondPagrec7(FinCondPagrec finCondPagrec7) {
		this.finCondPagrec7 = finCondPagrec7;
	}

	public FinCondPagrec getFinCondPagrec8() {
		return this.finCondPagrec8;
	}

	public void setFinCondPagrec8(FinCondPagrec finCondPagrec8) {
		this.finCondPagrec8 = finCondPagrec8;
	}

	public FinCondPagrec getFinCondPagrec9() {
		return this.finCondPagrec9;
	}

	public void setFinCondPagrec9(FinCondPagrec finCondPagrec9) {
		this.finCondPagrec9 = finCondPagrec9;
	}

	public FinCondPagrec getFinCondPagrec10() {
		return this.finCondPagrec10;
	}

	public void setFinCondPagrec10(FinCondPagrec finCondPagrec10) {
		this.finCondPagrec10 = finCondPagrec10;
	}

	public GerItemserv getGerItemserv() {
		return this.gerItemserv;
	}

	public void setGerItemserv(GerItemserv gerItemserv) {
		this.gerItemserv = gerItemserv;
	}

	public GerPessoa getGerPessoa1() {
		return this.gerPessoa1;
	}

	public void setGerPessoa1(GerPessoa gerPessoa1) {
		this.gerPessoa1 = gerPessoa1;
	}

	public GerPessoa getGerPessoa2() {
		return this.gerPessoa2;
	}

	public void setGerPessoa2(GerPessoa gerPessoa2) {
		this.gerPessoa2 = gerPessoa2;
	}

	public GerPessoa getGerPessoa3() {
		return this.gerPessoa3;
	}

	public void setGerPessoa3(GerPessoa gerPessoa3) {
		this.gerPessoa3 = gerPessoa3;
	}

	public GerPessoa getGerPessoa4() {
		return this.gerPessoa4;
	}

	public void setGerPessoa4(GerPessoa gerPessoa4) {
		this.gerPessoa4 = gerPessoa4;
	}

	public GerPessoa getGerPessoa5() {
		return this.gerPessoa5;
	}

	public void setGerPessoa5(GerPessoa gerPessoa5) {
		this.gerPessoa5 = gerPessoa5;
	}

	public GerPessoa getGerPessoa6() {
		return this.gerPessoa6;
	}

	public void setGerPessoa6(GerPessoa gerPessoa6) {
		this.gerPessoa6 = gerPessoa6;
	}

	public GerPessoa getGerPessoa7() {
		return this.gerPessoa7;
	}

	public void setGerPessoa7(GerPessoa gerPessoa7) {
		this.gerPessoa7 = gerPessoa7;
	}

	public GerPessoa getGerPessoa8() {
		return this.gerPessoa8;
	}

	public void setGerPessoa8(GerPessoa gerPessoa8) {
		this.gerPessoa8 = gerPessoa8;
	}

	public GerPessoa getGerPessoa9() {
		return this.gerPessoa9;
	}

	public void setGerPessoa9(GerPessoa gerPessoa9) {
		this.gerPessoa9 = gerPessoa9;
	}

	public GerPessoa getGerPessoa10() {
		return this.gerPessoa10;
	}

	public void setGerPessoa10(GerPessoa gerPessoa10) {
		this.gerPessoa10 = gerPessoa10;
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

	public GerPessoaEndereco getGerPessoaEndereco8() {
		return this.gerPessoaEndereco8;
	}

	public void setGerPessoaEndereco8(GerPessoaEndereco gerPessoaEndereco8) {
		this.gerPessoaEndereco8 = gerPessoaEndereco8;
	}

	public GerPessoaEndereco getGerPessoaEndereco9() {
		return this.gerPessoaEndereco9;
	}

	public void setGerPessoaEndereco9(GerPessoaEndereco gerPessoaEndereco9) {
		this.gerPessoaEndereco9 = gerPessoaEndereco9;
	}

	public GerPessoaEndereco getGerPessoaEndereco10() {
		return this.gerPessoaEndereco10;
	}

	public void setGerPessoaEndereco10(GerPessoaEndereco gerPessoaEndereco10) {
		this.gerPessoaEndereco10 = gerPessoaEndereco10;
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

	public SysUser getSysUser1() {
		return this.sysUser1;
	}

	public void setSysUser1(SysUser sysUser1) {
		this.sysUser1 = sysUser1;
	}

	public SysUser getSysUser2() {
		return this.sysUser2;
	}

	public void setSysUser2(SysUser sysUser2) {
		this.sysUser2 = sysUser2;
	}

	public SysUser getSysUser3() {
		return this.sysUser3;
	}

	public void setSysUser3(SysUser sysUser3) {
		this.sysUser3 = sysUser3;
	}

	public SysUser getSysUser4() {
		return this.sysUser4;
	}

	public void setSysUser4(SysUser sysUser4) {
		this.sysUser4 = sysUser4;
	}

	public SysUser getSysUser5() {
		return this.sysUser5;
	}

	public void setSysUser5(SysUser sysUser5) {
		this.sysUser5 = sysUser5;
	}

	public SysUser getSysUser6() {
		return this.sysUser6;
	}

	public void setSysUser6(SysUser sysUser6) {
		this.sysUser6 = sysUser6;
	}

	public SysUser getSysUser7() {
		return this.sysUser7;
	}

	public void setSysUser7(SysUser sysUser7) {
		this.sysUser7 = sysUser7;
	}

	public SysUser getSysUser8() {
		return this.sysUser8;
	}

	public void setSysUser8(SysUser sysUser8) {
		this.sysUser8 = sysUser8;
	}

	public SysUser getSysUser9() {
		return this.sysUser9;
	}

	public void setSysUser9(SysUser sysUser9) {
		this.sysUser9 = sysUser9;
	}

	public SysUser getSysUser10() {
		return this.sysUser10;
	}

	public void setSysUser10(SysUser sysUser10) {
		this.sysUser10 = sysUser10;
	}

}