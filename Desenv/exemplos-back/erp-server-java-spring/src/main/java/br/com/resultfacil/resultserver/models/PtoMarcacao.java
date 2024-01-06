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
@Table(name="pto_marcacao")
@NamedQuery(name="PtoMarcacao.findAll", query="SELECT p FROM PtoMarcacao p")
public class PtoMarcacao implements Serializable {
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

	@Column(name="marc_ano")
	private Integer marcAno;

	@Column(name="marc_data")
	private Timestamp marcData;

	@Column(name="marc_dia")
	private Integer marcDia;

	@Column(name="marc_hora")
	private Integer marcHora;

	@Column(name="marc_mes")
	private Integer marcMes;

	@Column(name="marc_minuto")
	private Integer marcMinuto;

	//bi-directional many-to-one association to PtoMedidor
	@ManyToOne
	@JoinColumn(name="pto_medidor_id")
	private PtoMedidor ptoMedidor;

	//bi-directional many-to-one association to SysProcessLog
	@ManyToOne
	@JoinColumn(name="process_id")
	private SysProcessLog sysProcessLog;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public PtoMarcacao() {
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

	public Integer getMarcAno() {
		return this.marcAno;
	}

	public void setMarcAno(Integer marcAno) {
		this.marcAno = marcAno;
	}

	public Timestamp getMarcData() {
		return this.marcData;
	}

	public void setMarcData(Timestamp marcData) {
		this.marcData = marcData;
	}

	public Integer getMarcDia() {
		return this.marcDia;
	}

	public void setMarcDia(Integer marcDia) {
		this.marcDia = marcDia;
	}

	public Integer getMarcHora() {
		return this.marcHora;
	}

	public void setMarcHora(Integer marcHora) {
		this.marcHora = marcHora;
	}

	public Integer getMarcMes() {
		return this.marcMes;
	}

	public void setMarcMes(Integer marcMes) {
		this.marcMes = marcMes;
	}

	public Integer getMarcMinuto() {
		return this.marcMinuto;
	}

	public void setMarcMinuto(Integer marcMinuto) {
		this.marcMinuto = marcMinuto;
	}

	public PtoMedidor getPtoMedidor() {
		return this.ptoMedidor;
	}

	public void setPtoMedidor(PtoMedidor ptoMedidor) {
		this.ptoMedidor = ptoMedidor;
	}

	public SysProcessLog getSysProcessLog() {
		return this.sysProcessLog;
	}

	public void setSysProcessLog(SysProcessLog sysProcessLog) {
		this.sysProcessLog = sysProcessLog;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}