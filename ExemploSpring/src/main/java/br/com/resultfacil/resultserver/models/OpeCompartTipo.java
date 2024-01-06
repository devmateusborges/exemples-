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
@Table(name="ope_compart_tipo")
@NamedQuery(name="OpeCompartTipo.findAll", query="SELECT o FROM OpeCompartTipo o")
public class OpeCompartTipo implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(nullable=false, length=100)
	private String nome;

	@Column(name="qnt_lonas", nullable=false, precision=18, scale=3)
	private BigDecimal qntLonas;

	@Column(name="qnt_sulco_max", precision=18, scale=3)
	private BigDecimal qntSulcoMax;

	@Column(name="qnt_sulco_min", nullable=false, precision=18, scale=3)
	private BigDecimal qntSulcoMin;

	@Column(name="sigla_compart_tipo", nullable=false, length=50)
	private String siglaCompartTipo;

	@Column(name="tipo_compart", nullable=false, length=1)
	private String tipoCompart;

	//bi-directional many-to-one association to OpeCompartMedida
	@ManyToOne
	@JoinColumn(name="ope_compart_medida_id", nullable=false)
	private OpeCompartMedida opeCompartMedida;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCompartTipo() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getAtivo() {
		return this.ativo;
	}

	public void setAtivo(String ativo) {
		this.ativo = ativo;
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

	public String getNome() {
		return this.nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public BigDecimal getQntLonas() {
		return this.qntLonas;
	}

	public void setQntLonas(BigDecimal qntLonas) {
		this.qntLonas = qntLonas;
	}

	public BigDecimal getQntSulcoMax() {
		return this.qntSulcoMax;
	}

	public void setQntSulcoMax(BigDecimal qntSulcoMax) {
		this.qntSulcoMax = qntSulcoMax;
	}

	public BigDecimal getQntSulcoMin() {
		return this.qntSulcoMin;
	}

	public void setQntSulcoMin(BigDecimal qntSulcoMin) {
		this.qntSulcoMin = qntSulcoMin;
	}

	public String getSiglaCompartTipo() {
		return this.siglaCompartTipo;
	}

	public void setSiglaCompartTipo(String siglaCompartTipo) {
		this.siglaCompartTipo = siglaCompartTipo;
	}

	public String getTipoCompart() {
		return this.tipoCompart;
	}

	public void setTipoCompart(String tipoCompart) {
		this.tipoCompart = tipoCompart;
	}

	public OpeCompartMedida getOpeCompartMedida() {
		return this.opeCompartMedida;
	}

	public void setOpeCompartMedida(OpeCompartMedida opeCompartMedida) {
		this.opeCompartMedida = opeCompartMedida;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}