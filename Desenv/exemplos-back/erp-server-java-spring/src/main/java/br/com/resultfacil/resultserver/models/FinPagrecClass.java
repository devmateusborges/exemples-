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
@Table(name="fin_pagrec_class")
@NamedQuery(name="FinPagrecClass.findAll", query="SELECT f FROM FinPagrecClass f")
public class FinPagrecClass implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_valid")
	private Date dataValid;

	@Column(name="fator_rat", nullable=false, precision=18, scale=6)
	private BigDecimal fatorRat;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="perc_rat", nullable=false, precision=18, scale=6)
	private BigDecimal percRat;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor;

	//bi-directional many-to-one association to FinClass
	@ManyToOne
	@JoinColumn(name="fin_class_id", nullable=false)
	private FinClass finClass;

	//bi-directional many-to-one association to FinPagrec
	@ManyToOne
	@JoinColumn(name="fin_pagrec_id")
	private FinPagrec finPagrec;

	//bi-directional many-to-one association to FinPagrecBanco
	@ManyToOne
	@JoinColumn(name="fin_pagrec_banco_id")
	private FinPagrecBanco finPagrecBanco;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public FinPagrecClass() {
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

	public BigDecimal getFatorRat() {
		return this.fatorRat;
	}

	public void setFatorRat(BigDecimal fatorRat) {
		this.fatorRat = fatorRat;
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

	public BigDecimal getPercRat() {
		return this.percRat;
	}

	public void setPercRat(BigDecimal percRat) {
		this.percRat = percRat;
	}

	public BigDecimal getValor() {
		return this.valor;
	}

	public void setValor(BigDecimal valor) {
		this.valor = valor;
	}

	public FinClass getFinClass() {
		return this.finClass;
	}

	public void setFinClass(FinClass finClass) {
		this.finClass = finClass;
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

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}