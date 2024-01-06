package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.util.Date;
import java.sql.Timestamp;
import java.util.List;

import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_centro2_equip")
@NamedQuery(name="OpeCentro2Equip.findAll", query="SELECT o FROM OpeCentro2Equip o")
public class OpeCentro2Equip implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(precision=18, scale=6)
	private BigDecimal altura;

	@Column(name="capacidade_kg", precision=18, scale=6)
	private BigDecimal capacidadeKg;

	@Column(name="capacidade_m3", precision=18, scale=6)
	private BigDecimal capacidadeM3;

	@Temporal(TemporalType.DATE)
	@Column(name="data_venc_imposto")
	private Date dataVencImposto;

	@Temporal(TemporalType.DATE)
	@Column(name="data_venc_licenciamento")
	private Date dataVencLicenciamento;

	@Column(precision=18, scale=6)
	private BigDecimal largura;

	@Column(name="liberado_abastec", nullable=false, length=1)
	private String liberadoAbastec;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="nr_chassi", length=100)
	private String nrChassi;

	@Column(name="nr_registro_estadual", length=50)
	private String nrRegistroEstadual;

	@Column(name="nr_serie", length=100)
	private String nrSerie;

	@Column(length=100)
	private String placa;

	@Column(length=100)
	private String potencia;

	@Column(length=100)
	private String renavam;

	@Column(precision=18, scale=6)
	private BigDecimal tara;

	@Column(name="tipo_carroceria", nullable=false, length=100)
	private String tipoCarroceria;

	@Column(name="tipo_rodado", nullable=false, length=100)
	private String tipoRodado;

	@Column(name="tipo_tracao")
	private Integer tipoTracao;

	@Column(name="tipo_transp_auto_carga")
	private Integer tipoTranspAutoCarga;

	//bi-directional many-to-one association to BorDispositivo
	@OneToMany(mappedBy="opeCentro2Equip")
	private List<BorDispositivo> borDispositivos;

	//bi-directional many-to-one association to MovFrete
	@OneToMany(mappedBy="opeCentro2Equip")
	private List<MovFrete> movFretes;

	//bi-directional many-to-one association to MovReboque
	@OneToMany(mappedBy="opeCentro2Equip")
	private List<MovReboque> movReboques;

	//bi-directional many-to-one association to GerCidade
	@ManyToOne
	@JoinColumn(name="ger_cidade_id", nullable=false)
	private GerCidade gerCidade;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id", nullable=false)
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeFrenteTrabalho
	@ManyToOne
	@JoinColumn(name="ope_frente_trabalho_id")
	private OpeFrenteTrabalho opeFrenteTrabalho;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentro2Equip() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public BigDecimal getAltura() {
		return this.altura;
	}

	public void setAltura(BigDecimal altura) {
		this.altura = altura;
	}

	public BigDecimal getCapacidadeKg() {
		return this.capacidadeKg;
	}

	public void setCapacidadeKg(BigDecimal capacidadeKg) {
		this.capacidadeKg = capacidadeKg;
	}

	public BigDecimal getCapacidadeM3() {
		return this.capacidadeM3;
	}

	public void setCapacidadeM3(BigDecimal capacidadeM3) {
		this.capacidadeM3 = capacidadeM3;
	}

	public Date getDataVencImposto() {
		return this.dataVencImposto;
	}

	public void setDataVencImposto(Date dataVencImposto) {
		this.dataVencImposto = dataVencImposto;
	}

	public Date getDataVencLicenciamento() {
		return this.dataVencLicenciamento;
	}

	public void setDataVencLicenciamento(Date dataVencLicenciamento) {
		this.dataVencLicenciamento = dataVencLicenciamento;
	}

	public BigDecimal getLargura() {
		return this.largura;
	}

	public void setLargura(BigDecimal largura) {
		this.largura = largura;
	}

	public String getLiberadoAbastec() {
		return this.liberadoAbastec;
	}

	public void setLiberadoAbastec(String liberadoAbastec) {
		this.liberadoAbastec = liberadoAbastec;
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

	public String getNrChassi() {
		return this.nrChassi;
	}

	public void setNrChassi(String nrChassi) {
		this.nrChassi = nrChassi;
	}

	public String getNrRegistroEstadual() {
		return this.nrRegistroEstadual;
	}

	public void setNrRegistroEstadual(String nrRegistroEstadual) {
		this.nrRegistroEstadual = nrRegistroEstadual;
	}

	public String getNrSerie() {
		return this.nrSerie;
	}

	public void setNrSerie(String nrSerie) {
		this.nrSerie = nrSerie;
	}

	public String getPlaca() {
		return this.placa;
	}

	public void setPlaca(String placa) {
		this.placa = placa;
	}

	public String getPotencia() {
		return this.potencia;
	}

	public void setPotencia(String potencia) {
		this.potencia = potencia;
	}

	public String getRenavam() {
		return this.renavam;
	}

	public void setRenavam(String renavam) {
		this.renavam = renavam;
	}

	public BigDecimal getTara() {
		return this.tara;
	}

	public void setTara(BigDecimal tara) {
		this.tara = tara;
	}

	public String getTipoCarroceria() {
		return this.tipoCarroceria;
	}

	public void setTipoCarroceria(String tipoCarroceria) {
		this.tipoCarroceria = tipoCarroceria;
	}

	public String getTipoRodado() {
		return this.tipoRodado;
	}

	public void setTipoRodado(String tipoRodado) {
		this.tipoRodado = tipoRodado;
	}

	public Integer getTipoTracao() {
		return this.tipoTracao;
	}

	public void setTipoTracao(Integer tipoTracao) {
		this.tipoTracao = tipoTracao;
	}

	public Integer getTipoTranspAutoCarga() {
		return this.tipoTranspAutoCarga;
	}

	public void setTipoTranspAutoCarga(Integer tipoTranspAutoCarga) {
		this.tipoTranspAutoCarga = tipoTranspAutoCarga;
	}

	public List<BorDispositivo> getBorDispositivos() {
		return this.borDispositivos;
	}

	public void setBorDispositivos(List<BorDispositivo> borDispositivos) {
		this.borDispositivos = borDispositivos;
	}

	public BorDispositivo addBorDispositivo(BorDispositivo borDispositivo) {
		getBorDispositivos().add(borDispositivo);
		borDispositivo.setOpeCentro2Equip(this);

		return borDispositivo;
	}

	public BorDispositivo removeBorDispositivo(BorDispositivo borDispositivo) {
		getBorDispositivos().remove(borDispositivo);
		borDispositivo.setOpeCentro2Equip(null);

		return borDispositivo;
	}

	public List<MovFrete> getMovFretes() {
		return this.movFretes;
	}

	public void setMovFretes(List<MovFrete> movFretes) {
		this.movFretes = movFretes;
	}

	public MovFrete addMovFrete(MovFrete movFrete) {
		getMovFretes().add(movFrete);
		movFrete.setOpeCentro2Equip(this);

		return movFrete;
	}

	public MovFrete removeMovFrete(MovFrete movFrete) {
		getMovFretes().remove(movFrete);
		movFrete.setOpeCentro2Equip(null);

		return movFrete;
	}

	public List<MovReboque> getMovReboques() {
		return this.movReboques;
	}

	public void setMovReboques(List<MovReboque> movReboques) {
		this.movReboques = movReboques;
	}

	public MovReboque addMovReboque(MovReboque movReboque) {
		getMovReboques().add(movReboque);
		movReboque.setOpeCentro2Equip(this);

		return movReboque;
	}

	public MovReboque removeMovReboque(MovReboque movReboque) {
		getMovReboques().remove(movReboque);
		movReboque.setOpeCentro2Equip(null);

		return movReboque;
	}

	public GerCidade getGerCidade() {
		return this.gerCidade;
	}

	public void setGerCidade(GerCidade gerCidade) {
		this.gerCidade = gerCidade;
	}

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
	}

	public OpeFrenteTrabalho getOpeFrenteTrabalho() {
		return this.opeFrenteTrabalho;
	}

	public void setOpeFrenteTrabalho(OpeFrenteTrabalho opeFrenteTrabalho) {
		this.opeFrenteTrabalho = opeFrenteTrabalho;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}