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
@Table(name="ind_vr_quadrimestre")
@NamedQuery(name="IndVrQuadrimestre.findAll", query="SELECT i FROM IndVrQuadrimestre i")
public class IndVrQuadrimestre implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="aprovado_exibicao", nullable=false, length=1)
	private String aprovadoExibicao;

	@Column(nullable=false, length=100)
	private String atributo;

	@Column(name="ind_id", nullable=false, length=36)
	private String indId;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="valor_meta", nullable=false, precision=18, scale=6)
	private BigDecimal valorMeta;

	@Column(name="valor_real", nullable=false, precision=18, scale=6)
	private BigDecimal valorReal;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to GerPer
	@ManyToOne
	@JoinColumn(name="ger_per_id", nullable=false)
	private GerPer gerPer;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public IndVrQuadrimestre() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getAprovadoExibicao() {
		return this.aprovadoExibicao;
	}

	public void setAprovadoExibicao(String aprovadoExibicao) {
		this.aprovadoExibicao = aprovadoExibicao;
	}

	public String getAtributo() {
		return this.atributo;
	}

	public void setAtributo(String atributo) {
		this.atributo = atributo;
	}

	public String getIndId() {
		return this.indId;
	}

	public void setIndId(String indId) {
		this.indId = indId;
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

	public BigDecimal getValorMeta() {
		return this.valorMeta;
	}

	public void setValorMeta(BigDecimal valorMeta) {
		this.valorMeta = valorMeta;
	}

	public BigDecimal getValorReal() {
		return this.valorReal;
	}

	public void setValorReal(BigDecimal valorReal) {
		this.valorReal = valorReal;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public GerPer getGerPer() {
		return this.gerPer;
	}

	public void setGerPer(GerPer gerPer) {
		this.gerPer = gerPer;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}