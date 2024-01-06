package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.util.Date;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_periodo")
@NamedQuery(name="OpePeriodo.findAll", query="SELECT o FROM OpePeriodo o")
public class OpePeriodo implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Temporal(TemporalType.DATE)
	@Column(name="data_fin", nullable=false)
	private Date dataFin;

	@Temporal(TemporalType.DATE)
	@Column(name="data_ini", nullable=false)
	private Date dataIni;

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

	@Column(name="sigla_periodo", nullable=false, length=50)
	private String siglaPeriodo;

	//bi-directional many-to-one association to OpeCentro2Area
	@OneToMany(mappedBy="opePeriodo")
	private List<OpeCentro2Area> opeCentro2Areas;

	//bi-directional many-to-one association to OpeCentro2Ord
	@OneToMany(mappedBy="opePeriodo")
	private List<OpeCentro2Ord> opeCentro2Ords;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="opePeriodo1")
	private List<OpeCentroDest> opeCentroDests1;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="opePeriodo2")
	private List<OpeCentroDest> opeCentroDests2;

	//bi-directional many-to-one association to OpeCentroPrev
	@OneToMany(mappedBy="opePeriodo")
	private List<OpeCentroPrev> opeCentroPrevs;

	//bi-directional many-to-one association to OpeCentroRatFator
	@OneToMany(mappedBy="opePeriodo")
	private List<OpeCentroRatFator> opeCentroRatFators;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpePeriodo() {
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

	public Date getDataFin() {
		return this.dataFin;
	}

	public void setDataFin(Date dataFin) {
		this.dataFin = dataFin;
	}

	public Date getDataIni() {
		return this.dataIni;
	}

	public void setDataIni(Date dataIni) {
		this.dataIni = dataIni;
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

	public String getSiglaPeriodo() {
		return this.siglaPeriodo;
	}

	public void setSiglaPeriodo(String siglaPeriodo) {
		this.siglaPeriodo = siglaPeriodo;
	}

	public List<OpeCentro2Area> getOpeCentro2Areas() {
		return this.opeCentro2Areas;
	}

	public void setOpeCentro2Areas(List<OpeCentro2Area> opeCentro2Areas) {
		this.opeCentro2Areas = opeCentro2Areas;
	}

	public OpeCentro2Area addOpeCentro2Area(OpeCentro2Area opeCentro2Area) {
		getOpeCentro2Areas().add(opeCentro2Area);
		opeCentro2Area.setOpePeriodo(this);

		return opeCentro2Area;
	}

	public OpeCentro2Area removeOpeCentro2Area(OpeCentro2Area opeCentro2Area) {
		getOpeCentro2Areas().remove(opeCentro2Area);
		opeCentro2Area.setOpePeriodo(null);

		return opeCentro2Area;
	}

	public List<OpeCentro2Ord> getOpeCentro2Ords() {
		return this.opeCentro2Ords;
	}

	public void setOpeCentro2Ords(List<OpeCentro2Ord> opeCentro2Ords) {
		this.opeCentro2Ords = opeCentro2Ords;
	}

	public OpeCentro2Ord addOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().add(opeCentro2Ord);
		opeCentro2Ord.setOpePeriodo(this);

		return opeCentro2Ord;
	}

	public OpeCentro2Ord removeOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().remove(opeCentro2Ord);
		opeCentro2Ord.setOpePeriodo(null);

		return opeCentro2Ord;
	}

	public List<OpeCentroDest> getOpeCentroDests1() {
		return this.opeCentroDests1;
	}

	public void setOpeCentroDests1(List<OpeCentroDest> opeCentroDests1) {
		this.opeCentroDests1 = opeCentroDests1;
	}

	public OpeCentroDest addOpeCentroDests1(OpeCentroDest opeCentroDests1) {
		getOpeCentroDests1().add(opeCentroDests1);
		opeCentroDests1.setOpePeriodo1(this);

		return opeCentroDests1;
	}

	public OpeCentroDest removeOpeCentroDests1(OpeCentroDest opeCentroDests1) {
		getOpeCentroDests1().remove(opeCentroDests1);
		opeCentroDests1.setOpePeriodo1(null);

		return opeCentroDests1;
	}

	public List<OpeCentroDest> getOpeCentroDests2() {
		return this.opeCentroDests2;
	}

	public void setOpeCentroDests2(List<OpeCentroDest> opeCentroDests2) {
		this.opeCentroDests2 = opeCentroDests2;
	}

	public OpeCentroDest addOpeCentroDests2(OpeCentroDest opeCentroDests2) {
		getOpeCentroDests2().add(opeCentroDests2);
		opeCentroDests2.setOpePeriodo2(this);

		return opeCentroDests2;
	}

	public OpeCentroDest removeOpeCentroDests2(OpeCentroDest opeCentroDests2) {
		getOpeCentroDests2().remove(opeCentroDests2);
		opeCentroDests2.setOpePeriodo2(null);

		return opeCentroDests2;
	}

	public List<OpeCentroPrev> getOpeCentroPrevs() {
		return this.opeCentroPrevs;
	}

	public void setOpeCentroPrevs(List<OpeCentroPrev> opeCentroPrevs) {
		this.opeCentroPrevs = opeCentroPrevs;
	}

	public OpeCentroPrev addOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().add(opeCentroPrev);
		opeCentroPrev.setOpePeriodo(this);

		return opeCentroPrev;
	}

	public OpeCentroPrev removeOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().remove(opeCentroPrev);
		opeCentroPrev.setOpePeriodo(null);

		return opeCentroPrev;
	}

	public List<OpeCentroRatFator> getOpeCentroRatFators() {
		return this.opeCentroRatFators;
	}

	public void setOpeCentroRatFators(List<OpeCentroRatFator> opeCentroRatFators) {
		this.opeCentroRatFators = opeCentroRatFators;
	}

	public OpeCentroRatFator addOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().add(opeCentroRatFator);
		opeCentroRatFator.setOpePeriodo(this);

		return opeCentroRatFator;
	}

	public OpeCentroRatFator removeOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().remove(opeCentroRatFator);
		opeCentroRatFator.setOpePeriodo(null);

		return opeCentroRatFator;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}