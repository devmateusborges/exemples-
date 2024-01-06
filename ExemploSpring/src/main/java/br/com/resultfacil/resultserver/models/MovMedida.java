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
@Table(name="mov_medida")
@NamedQuery(name="MovMedida.findAll", query="SELECT m FROM MovMedida m")
public class MovMedida implements Serializable {
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
	private String marca;

	@Column(name="nr_volume", precision=18, scale=6)
	private BigDecimal nrVolume;

	@Column(name="peso_bruto", precision=18, scale=6)
	private BigDecimal pesoBruto;

	@Column(name="peso_liquido", precision=18, scale=6)
	private BigDecimal pesoLiquido;

	@Column(name="qnt_medida", nullable=false, precision=18, scale=6)
	private BigDecimal qntMedida;

	@Column(name="tipo_medida", nullable=false, length=50)
	private String tipoMedida;

	//bi-directional many-to-one association to GerUmedida
	@ManyToOne
	@JoinColumn(name="ger_umedida_id", nullable=false)
	private GerUmedida gerUmedida;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id", nullable=false)
	private Mov mov;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public MovMedida() {
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

	public String getMarca() {
		return this.marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public BigDecimal getNrVolume() {
		return this.nrVolume;
	}

	public void setNrVolume(BigDecimal nrVolume) {
		this.nrVolume = nrVolume;
	}

	public BigDecimal getPesoBruto() {
		return this.pesoBruto;
	}

	public void setPesoBruto(BigDecimal pesoBruto) {
		this.pesoBruto = pesoBruto;
	}

	public BigDecimal getPesoLiquido() {
		return this.pesoLiquido;
	}

	public void setPesoLiquido(BigDecimal pesoLiquido) {
		this.pesoLiquido = pesoLiquido;
	}

	public BigDecimal getQntMedida() {
		return this.qntMedida;
	}

	public void setQntMedida(BigDecimal qntMedida) {
		this.qntMedida = qntMedida;
	}

	public String getTipoMedida() {
		return this.tipoMedida;
	}

	public void setTipoMedida(String tipoMedida) {
		this.tipoMedida = tipoMedida;
	}

	public GerUmedida getGerUmedida() {
		return this.gerUmedida;
	}

	public void setGerUmedida(GerUmedida gerUmedida) {
		this.gerUmedida = gerUmedida;
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