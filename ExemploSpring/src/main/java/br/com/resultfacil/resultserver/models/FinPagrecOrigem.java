package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="fin_pagrec_origem")
@NamedQuery(name="FinPagrecOrigem.findAll", query="SELECT f FROM FinPagrecOrigem f")
public class FinPagrecOrigem implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(length=50)
	private String tipo;

	//bi-directional many-to-one association to FinPagrec
	@ManyToOne
	@JoinColumn(name="fin_pagrec_id", nullable=false)
	private FinPagrec finPagrec1;

	//bi-directional many-to-one association to FinPagrec
	@ManyToOne
	@JoinColumn(name="fin_pagrec_id_origem")
	private FinPagrec finPagrec2;

	//bi-directional many-to-one association to FinPagrecBaixa
	@ManyToOne
	@JoinColumn(name="fin_pagrec_baixa_id")
	private FinPagrecBaixa finPagrecBaixa;

	//bi-directional many-to-one association to FinPagrecBanco
	@ManyToOne
	@JoinColumn(name="fin_pagrec_banco_id")
	private FinPagrecBanco finPagrecBanco;

	//bi-directional many-to-one association to FinPagrecBancoExtrato
	@ManyToOne
	@JoinColumn(name="fin_extrato_id")
	private FinPagrecBancoExtrato finPagrecBancoExtrato;

	//bi-directional many-to-one association to FinPagrecParc
	@ManyToOne
	@JoinColumn(name="fin_pagrec_parc_id")
	private FinPagrecParc finPagrecParc1;

	//bi-directional many-to-one association to FinPagrecParc
	@ManyToOne
	@JoinColumn(name="fin_pagrec_parc_id_origem")
	private FinPagrecParc finPagrecParc2;

	//bi-directional many-to-one association to FinRecibo
	@ManyToOne
	@JoinColumn(name="fin_recibo_id")
	private FinRecibo finRecibo;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id")
	private Mov mov;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public FinPagrecOrigem() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
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

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public FinPagrec getFinPagrec1() {
		return this.finPagrec1;
	}

	public void setFinPagrec1(FinPagrec finPagrec1) {
		this.finPagrec1 = finPagrec1;
	}

	public FinPagrec getFinPagrec2() {
		return this.finPagrec2;
	}

	public void setFinPagrec2(FinPagrec finPagrec2) {
		this.finPagrec2 = finPagrec2;
	}

	public FinPagrecBaixa getFinPagrecBaixa() {
		return this.finPagrecBaixa;
	}

	public void setFinPagrecBaixa(FinPagrecBaixa finPagrecBaixa) {
		this.finPagrecBaixa = finPagrecBaixa;
	}

	public FinPagrecBanco getFinPagrecBanco() {
		return this.finPagrecBanco;
	}

	public void setFinPagrecBanco(FinPagrecBanco finPagrecBanco) {
		this.finPagrecBanco = finPagrecBanco;
	}

	public FinPagrecBancoExtrato getFinPagrecBancoExtrato() {
		return this.finPagrecBancoExtrato;
	}

	public void setFinPagrecBancoExtrato(FinPagrecBancoExtrato finPagrecBancoExtrato) {
		this.finPagrecBancoExtrato = finPagrecBancoExtrato;
	}

	public FinPagrecParc getFinPagrecParc1() {
		return this.finPagrecParc1;
	}

	public void setFinPagrecParc1(FinPagrecParc finPagrecParc1) {
		this.finPagrecParc1 = finPagrecParc1;
	}

	public FinPagrecParc getFinPagrecParc2() {
		return this.finPagrecParc2;
	}

	public void setFinPagrecParc2(FinPagrecParc finPagrecParc2) {
		this.finPagrecParc2 = finPagrecParc2;
	}

	public FinRecibo getFinRecibo() {
		return this.finRecibo;
	}

	public void setFinRecibo(FinRecibo finRecibo) {
		this.finRecibo = finRecibo;
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

}