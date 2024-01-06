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
@Table(name="ope_centro2_area")
@NamedQuery(name="OpeCentro2Area.findAll", query="SELECT o FROM OpeCentro2Area o")
public class OpeCentro2Area implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="alt_z", length=100)
	private String altZ;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(name="bloco_col", length=100)
	private String blocoCol;

	@Temporal(TemporalType.DATE)
	@Column(name="data_emerg")
	private Date dataEmerg;

	@Temporal(TemporalType.DATE)
	@Column(name="data_fin_col")
	private Date dataFinCol;

	@Temporal(TemporalType.DATE)
	@Column(name="data_fin_plan")
	private Date dataFinPlan;

	@Temporal(TemporalType.DATE)
	@Column(name="data_florada_1")
	private Date dataFlorada1;

	@Temporal(TemporalType.DATE)
	@Column(name="data_ini_col")
	private Date dataIniCol;

	@Temporal(TemporalType.DATE)
	@Column(name="data_ini_plan")
	private Date dataIniPlan;

	@Temporal(TemporalType.DATE)
	@Column(name="data_ult_col")
	private Date dataUltCol;

	@Temporal(TemporalType.DATE)
	@Column(name="data_ult_plan")
	private Date dataUltPlan;

	@Column(name="lat_x", length=100)
	private String latX;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="long_y", length=100)
	private String longY;

	@Column(length=250)
	private String observacao;

	@Column(name="qnt_area_improd", nullable=false, precision=18, scale=6)
	private BigDecimal qntAreaImprod;

	@Column(name="qnt_area_prod", nullable=false, precision=18, scale=6)
	private BigDecimal qntAreaProd;

	@Column(name="qnt_plantas_estande", precision=18, scale=6)
	private BigDecimal qntPlantasEstande;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id", nullable=false)
	private GerItemserv gerItemserv1;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id_ult")
	private GerItemserv gerItemserv2;

	//bi-directional many-to-one association to GerItemservVar
	@ManyToOne
	@JoinColumn(name="ger_itemserv_var_id")
	private GerItemservVar gerItemservVar1;

	//bi-directional many-to-one association to GerItemservVar
	@ManyToOne
	@JoinColumn(name="ger_itemserv_var_id_ult")
	private GerItemservVar gerItemservVar2;

	//bi-directional many-to-one association to GerUmedida
	@ManyToOne
	@JoinColumn(name="ger_umedida_id", nullable=false)
	private GerUmedida gerUmedida;

	//bi-directional many-to-one association to OpeAtividadeSistema
	@ManyToOne
	@JoinColumn(name="ope_atividade_sistema_id_col")
	private OpeAtividadeSistema opeAtividadeSistema1;

	//bi-directional many-to-one association to OpeAtividadeSistema
	@ManyToOne
	@JoinColumn(name="ope_atividade_sistema_id_cult")
	private OpeAtividadeSistema opeAtividadeSistema2;

	//bi-directional many-to-one association to OpeAtividadeSistema
	@ManyToOne
	@JoinColumn(name="ope_atividade_sistema_id_plan")
	private OpeAtividadeSistema opeAtividadeSistema3;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id", nullable=false)
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeEspac
	@ManyToOne
	@JoinColumn(name="ope_espac_id")
	private OpeEspac opeEspac;

	//bi-directional many-to-one association to OpeEstagio
	@ManyToOne
	@JoinColumn(name="ope_estagio_id")
	private OpeEstagio opeEstagio;

	//bi-directional many-to-one association to OpePeriodo
	@ManyToOne
	@JoinColumn(name="ope_periodo_id")
	private OpePeriodo opePeriodo;

	//bi-directional many-to-one association to OpeTipoSolo
	@ManyToOne
	@JoinColumn(name="ope_tipo_solo_id")
	private OpeTipoSolo opeTipoSolo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCentro2MapaCoord
	@OneToMany(mappedBy="opeCentro2Area")
	private List<OpeCentro2MapaCoord> opeCentro2MapaCoords;

	//bi-directional many-to-one association to OpeCentro2MapaGeometria
	@OneToMany(mappedBy="opeCentro2Area")
	private List<OpeCentro2MapaGeometria> opeCentro2MapaGeometrias;

	public OpeCentro2Area() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getAltZ() {
		return this.altZ;
	}

	public void setAltZ(String altZ) {
		this.altZ = altZ;
	}

	public String getAtivo() {
		return this.ativo;
	}

	public void setAtivo(String ativo) {
		this.ativo = ativo;
	}

	public String getBlocoCol() {
		return this.blocoCol;
	}

	public void setBlocoCol(String blocoCol) {
		this.blocoCol = blocoCol;
	}

	public Date getDataEmerg() {
		return this.dataEmerg;
	}

	public void setDataEmerg(Date dataEmerg) {
		this.dataEmerg = dataEmerg;
	}

	public Date getDataFinCol() {
		return this.dataFinCol;
	}

	public void setDataFinCol(Date dataFinCol) {
		this.dataFinCol = dataFinCol;
	}

	public Date getDataFinPlan() {
		return this.dataFinPlan;
	}

	public void setDataFinPlan(Date dataFinPlan) {
		this.dataFinPlan = dataFinPlan;
	}

	public Date getDataFlorada1() {
		return this.dataFlorada1;
	}

	public void setDataFlorada1(Date dataFlorada1) {
		this.dataFlorada1 = dataFlorada1;
	}

	public Date getDataIniCol() {
		return this.dataIniCol;
	}

	public void setDataIniCol(Date dataIniCol) {
		this.dataIniCol = dataIniCol;
	}

	public Date getDataIniPlan() {
		return this.dataIniPlan;
	}

	public void setDataIniPlan(Date dataIniPlan) {
		this.dataIniPlan = dataIniPlan;
	}

	public Date getDataUltCol() {
		return this.dataUltCol;
	}

	public void setDataUltCol(Date dataUltCol) {
		this.dataUltCol = dataUltCol;
	}

	public Date getDataUltPlan() {
		return this.dataUltPlan;
	}

	public void setDataUltPlan(Date dataUltPlan) {
		this.dataUltPlan = dataUltPlan;
	}

	public String getLatX() {
		return this.latX;
	}

	public void setLatX(String latX) {
		this.latX = latX;
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

	public String getLongY() {
		return this.longY;
	}

	public void setLongY(String longY) {
		this.longY = longY;
	}

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public BigDecimal getQntAreaImprod() {
		return this.qntAreaImprod;
	}

	public void setQntAreaImprod(BigDecimal qntAreaImprod) {
		this.qntAreaImprod = qntAreaImprod;
	}

	public BigDecimal getQntAreaProd() {
		return this.qntAreaProd;
	}

	public void setQntAreaProd(BigDecimal qntAreaProd) {
		this.qntAreaProd = qntAreaProd;
	}

	public BigDecimal getQntPlantasEstande() {
		return this.qntPlantasEstande;
	}

	public void setQntPlantasEstande(BigDecimal qntPlantasEstande) {
		this.qntPlantasEstande = qntPlantasEstande;
	}

	public GerItemserv getGerItemserv1() {
		return this.gerItemserv1;
	}

	public void setGerItemserv1(GerItemserv gerItemserv1) {
		this.gerItemserv1 = gerItemserv1;
	}

	public GerItemserv getGerItemserv2() {
		return this.gerItemserv2;
	}

	public void setGerItemserv2(GerItemserv gerItemserv2) {
		this.gerItemserv2 = gerItemserv2;
	}

	public GerItemservVar getGerItemservVar1() {
		return this.gerItemservVar1;
	}

	public void setGerItemservVar1(GerItemservVar gerItemservVar1) {
		this.gerItemservVar1 = gerItemservVar1;
	}

	public GerItemservVar getGerItemservVar2() {
		return this.gerItemservVar2;
	}

	public void setGerItemservVar2(GerItemservVar gerItemservVar2) {
		this.gerItemservVar2 = gerItemservVar2;
	}

	public GerUmedida getGerUmedida() {
		return this.gerUmedida;
	}

	public void setGerUmedida(GerUmedida gerUmedida) {
		this.gerUmedida = gerUmedida;
	}

	public OpeAtividadeSistema getOpeAtividadeSistema1() {
		return this.opeAtividadeSistema1;
	}

	public void setOpeAtividadeSistema1(OpeAtividadeSistema opeAtividadeSistema1) {
		this.opeAtividadeSistema1 = opeAtividadeSistema1;
	}

	public OpeAtividadeSistema getOpeAtividadeSistema2() {
		return this.opeAtividadeSistema2;
	}

	public void setOpeAtividadeSistema2(OpeAtividadeSistema opeAtividadeSistema2) {
		this.opeAtividadeSistema2 = opeAtividadeSistema2;
	}

	public OpeAtividadeSistema getOpeAtividadeSistema3() {
		return this.opeAtividadeSistema3;
	}

	public void setOpeAtividadeSistema3(OpeAtividadeSistema opeAtividadeSistema3) {
		this.opeAtividadeSistema3 = opeAtividadeSistema3;
	}

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
	}

	public OpeEspac getOpeEspac() {
		return this.opeEspac;
	}

	public void setOpeEspac(OpeEspac opeEspac) {
		this.opeEspac = opeEspac;
	}

	public OpeEstagio getOpeEstagio() {
		return this.opeEstagio;
	}

	public void setOpeEstagio(OpeEstagio opeEstagio) {
		this.opeEstagio = opeEstagio;
	}

	public OpePeriodo getOpePeriodo() {
		return this.opePeriodo;
	}

	public void setOpePeriodo(OpePeriodo opePeriodo) {
		this.opePeriodo = opePeriodo;
	}

	public OpeTipoSolo getOpeTipoSolo() {
		return this.opeTipoSolo;
	}

	public void setOpeTipoSolo(OpeTipoSolo opeTipoSolo) {
		this.opeTipoSolo = opeTipoSolo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCentro2MapaCoord> getOpeCentro2MapaCoords() {
		return this.opeCentro2MapaCoords;
	}

	public void setOpeCentro2MapaCoords(List<OpeCentro2MapaCoord> opeCentro2MapaCoords) {
		this.opeCentro2MapaCoords = opeCentro2MapaCoords;
	}

	public OpeCentro2MapaCoord addOpeCentro2MapaCoord(OpeCentro2MapaCoord opeCentro2MapaCoord) {
		getOpeCentro2MapaCoords().add(opeCentro2MapaCoord);
		opeCentro2MapaCoord.setOpeCentro2Area(this);

		return opeCentro2MapaCoord;
	}

	public OpeCentro2MapaCoord removeOpeCentro2MapaCoord(OpeCentro2MapaCoord opeCentro2MapaCoord) {
		getOpeCentro2MapaCoords().remove(opeCentro2MapaCoord);
		opeCentro2MapaCoord.setOpeCentro2Area(null);

		return opeCentro2MapaCoord;
	}

	public List<OpeCentro2MapaGeometria> getOpeCentro2MapaGeometrias() {
		return this.opeCentro2MapaGeometrias;
	}

	public void setOpeCentro2MapaGeometrias(List<OpeCentro2MapaGeometria> opeCentro2MapaGeometrias) {
		this.opeCentro2MapaGeometrias = opeCentro2MapaGeometrias;
	}

	public OpeCentro2MapaGeometria addOpeCentro2MapaGeometria(OpeCentro2MapaGeometria opeCentro2MapaGeometria) {
		getOpeCentro2MapaGeometrias().add(opeCentro2MapaGeometria);
		opeCentro2MapaGeometria.setOpeCentro2Area(this);

		return opeCentro2MapaGeometria;
	}

	public OpeCentro2MapaGeometria removeOpeCentro2MapaGeometria(OpeCentro2MapaGeometria opeCentro2MapaGeometria) {
		getOpeCentro2MapaGeometrias().remove(opeCentro2MapaGeometria);
		opeCentro2MapaGeometria.setOpeCentro2Area(null);

		return opeCentro2MapaGeometria;
	}

}