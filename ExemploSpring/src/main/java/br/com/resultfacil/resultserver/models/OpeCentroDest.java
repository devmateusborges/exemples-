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
@Table(name="ope_centro_dest")
@NamedQuery(name="OpeCentroDest.findAll", query="SELECT o FROM OpeCentroDest o")
public class OpeCentroDest implements Serializable {
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

	@Column(nullable=false, precision=18, scale=6)
	private BigDecimal qnt;

	@Column(name="tipo_es", nullable=false, length=1)
	private String tipoEs;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor;

	//bi-directional many-to-one association to FinPagrec
	@ManyToOne
	@JoinColumn(name="fin_pagrec_id")
	private FinPagrec finPagrec;

	//bi-directional many-to-one association to FinPagrecBanco
	@ManyToOne
	@JoinColumn(name="fin_pagrec_banco_id")
	private FinPagrecBanco finPagrecBanco;

	//bi-directional many-to-one association to MovItemserv
	@ManyToOne
	@JoinColumn(name="mov_itemserv_id")
	private MovItemserv movItemserv;

	//bi-directional many-to-one association to OpeAtividade
	@ManyToOne
	@JoinColumn(name="ope_atividade_id")
	private OpeAtividade opeAtividade;

	//bi-directional many-to-one association to OpeCentro1
	@ManyToOne
	@JoinColumn(name="ope_centro1_id")
	private OpeCentro1 opeCentro11;

	//bi-directional many-to-one association to OpeCentro1
	@ManyToOne
	@JoinColumn(name="ope_centro1_id_dest_pri", nullable=false)
	private OpeCentro1 opeCentro12;

	//bi-directional many-to-one association to OpeCentro1
	@ManyToOne
	@JoinColumn(name="ope_centro1_id_dest_sec")
	private OpeCentro1 opeCentro13;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id")
	private OpeCentro2 opeCentro21;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id_dest_pri")
	private OpeCentro2 opeCentro22;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id_dest_sec")
	private OpeCentro2 opeCentro23;

	//bi-directional many-to-one association to OpeCompart
	@ManyToOne
	@JoinColumn(name="ope_compart_id_pri")
	private OpeCompart opeCompart1;

	//bi-directional many-to-one association to OpeCompart
	@ManyToOne
	@JoinColumn(name="ope_compart_id_sec")
	private OpeCompart opeCompart2;

	//bi-directional many-to-one association to OpePeriodo
	@ManyToOne
	@JoinColumn(name="ope_periodo_id_desc_pri")
	private OpePeriodo opePeriodo1;

	//bi-directional many-to-one association to OpePeriodo
	@ManyToOne
	@JoinColumn(name="ope_periodo_id_desc_sec")
	private OpePeriodo opePeriodo2;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentroDest() {
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

	public BigDecimal getQnt() {
		return this.qnt;
	}

	public void setQnt(BigDecimal qnt) {
		this.qnt = qnt;
	}

	public String getTipoEs() {
		return this.tipoEs;
	}

	public void setTipoEs(String tipoEs) {
		this.tipoEs = tipoEs;
	}

	public BigDecimal getValor() {
		return this.valor;
	}

	public void setValor(BigDecimal valor) {
		this.valor = valor;
	}

	public FinPagrec getFinPagrec() {
		return this.finPagrec;
	}

	public void setFinPagrec(FinPagrec finPagrec) {
		this.finPagrec = finPagrec;
	}

	public FinPagrecBanco getFinPagrecBanco() {
		return this.finPagrecBanco;
	}

	public void setFinPagrecBanco(FinPagrecBanco finPagrecBanco) {
		this.finPagrecBanco = finPagrecBanco;
	}

	public MovItemserv getMovItemserv() {
		return this.movItemserv;
	}

	public void setMovItemserv(MovItemserv movItemserv) {
		this.movItemserv = movItemserv;
	}

	public OpeAtividade getOpeAtividade() {
		return this.opeAtividade;
	}

	public void setOpeAtividade(OpeAtividade opeAtividade) {
		this.opeAtividade = opeAtividade;
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

	public OpeCentro1 getOpeCentro13() {
		return this.opeCentro13;
	}

	public void setOpeCentro13(OpeCentro1 opeCentro13) {
		this.opeCentro13 = opeCentro13;
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

	public OpeCentro2 getOpeCentro23() {
		return this.opeCentro23;
	}

	public void setOpeCentro23(OpeCentro2 opeCentro23) {
		this.opeCentro23 = opeCentro23;
	}

	public OpeCompart getOpeCompart1() {
		return this.opeCompart1;
	}

	public void setOpeCompart1(OpeCompart opeCompart1) {
		this.opeCompart1 = opeCompart1;
	}

	public OpeCompart getOpeCompart2() {
		return this.opeCompart2;
	}

	public void setOpeCompart2(OpeCompart opeCompart2) {
		this.opeCompart2 = opeCompart2;
	}

	public OpePeriodo getOpePeriodo1() {
		return this.opePeriodo1;
	}

	public void setOpePeriodo1(OpePeriodo opePeriodo1) {
		this.opePeriodo1 = opePeriodo1;
	}

	public OpePeriodo getOpePeriodo2() {
		return this.opePeriodo2;
	}

	public void setOpePeriodo2(OpePeriodo opePeriodo2) {
		this.opePeriodo2 = opePeriodo2;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}