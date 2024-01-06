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
@Table(name="ger_per")
@NamedQuery(name="GerPer.findAll", query="SELECT g FROM GerPer g")
public class GerPer implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=50)
	private String id;

	@Column(name="ano_nome", length=50)
	private String anoNome;

	@Column(name="bimestre_nome", length=50)
	private String bimestreNome;

	@Temporal(TemporalType.DATE)
	@Column(name="data_ano_inicial")
	private Date dataAnoInicial;

	@Temporal(TemporalType.DATE)
	@Column(name="data_bimestre_inicial")
	private Date dataBimestreInicial;

	@Temporal(TemporalType.DATE)
	@Column(name="data_dia_inicial")
	private Date dataDiaInicial;

	@Temporal(TemporalType.DATE)
	@Column(name="data_mes_inicial")
	private Date dataMesInicial;

	@Temporal(TemporalType.DATE)
	@Column(name="data_quadrimestre_inicial")
	private Date dataQuadrimestreInicial;

	@Temporal(TemporalType.DATE)
	@Column(name="data_quinzena_inicial")
	private Date dataQuinzenaInicial;

	@Temporal(TemporalType.DATE)
	@Column(name="data_semana_inicial")
	private Date dataSemanaInicial;

	@Temporal(TemporalType.DATE)
	@Column(name="data_semestre_inicial")
	private Date dataSemestreInicial;

	@Temporal(TemporalType.DATE)
	@Column(name="data_trimestre_inicial")
	private Date dataTrimestreInicial;

	@Column(name="dia_nome", length=50)
	private String diaNome;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="mes_nome", length=50)
	private String mesNome;

	@Column(name="quadrimestre_nome", length=50)
	private String quadrimestreNome;

	@Column(name="quinzena_nome", length=50)
	private String quinzenaNome;

	@Column(name="semana_nome", length=50)
	private String semanaNome;

	@Column(name="semestre_nome", length=50)
	private String semestreNome;

	@Column(name="trimestre_nome", length=50)
	private String trimestreNome;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to IndVrAno
	@OneToMany(mappedBy="gerPer")
	private List<IndVrAno> indVrAnos;

	//bi-directional many-to-one association to IndVrBimestre
	@OneToMany(mappedBy="gerPer")
	private List<IndVrBimestre> indVrBimestres;

	//bi-directional many-to-one association to IndVrDia
	@OneToMany(mappedBy="gerPer")
	private List<IndVrDia> indVrDias;

	//bi-directional many-to-one association to IndVrMe
	@OneToMany(mappedBy="gerPer")
	private List<IndVrMes> indVrMes;

	//bi-directional many-to-one association to IndVrQuadrimestre
	@OneToMany(mappedBy="gerPer")
	private List<IndVrQuadrimestre> indVrQuadrimestres;

	//bi-directional many-to-one association to IndVrQuinzena
	@OneToMany(mappedBy="gerPer")
	private List<IndVrQuinzena> indVrQuinzenas;

	//bi-directional many-to-one association to IndVrSemana
	@OneToMany(mappedBy="gerPer")
	private List<IndVrSemana> indVrSemanas;

	//bi-directional many-to-one association to IndVrSemestre
	@OneToMany(mappedBy="gerPer")
	private List<IndVrSemestre> indVrSemestres;

	//bi-directional many-to-one association to IndVrTrimestre
	@OneToMany(mappedBy="gerPer")
	private List<IndVrTrimestre> indVrTrimestres;

	public GerPer() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getAnoNome() {
		return this.anoNome;
	}

	public void setAnoNome(String anoNome) {
		this.anoNome = anoNome;
	}

	public String getBimestreNome() {
		return this.bimestreNome;
	}

	public void setBimestreNome(String bimestreNome) {
		this.bimestreNome = bimestreNome;
	}

	public Date getDataAnoInicial() {
		return this.dataAnoInicial;
	}

	public void setDataAnoInicial(Date dataAnoInicial) {
		this.dataAnoInicial = dataAnoInicial;
	}

	public Date getDataBimestreInicial() {
		return this.dataBimestreInicial;
	}

	public void setDataBimestreInicial(Date dataBimestreInicial) {
		this.dataBimestreInicial = dataBimestreInicial;
	}

	public Date getDataDiaInicial() {
		return this.dataDiaInicial;
	}

	public void setDataDiaInicial(Date dataDiaInicial) {
		this.dataDiaInicial = dataDiaInicial;
	}

	public Date getDataMesInicial() {
		return this.dataMesInicial;
	}

	public void setDataMesInicial(Date dataMesInicial) {
		this.dataMesInicial = dataMesInicial;
	}

	public Date getDataQuadrimestreInicial() {
		return this.dataQuadrimestreInicial;
	}

	public void setDataQuadrimestreInicial(Date dataQuadrimestreInicial) {
		this.dataQuadrimestreInicial = dataQuadrimestreInicial;
	}

	public Date getDataQuinzenaInicial() {
		return this.dataQuinzenaInicial;
	}

	public void setDataQuinzenaInicial(Date dataQuinzenaInicial) {
		this.dataQuinzenaInicial = dataQuinzenaInicial;
	}

	public Date getDataSemanaInicial() {
		return this.dataSemanaInicial;
	}

	public void setDataSemanaInicial(Date dataSemanaInicial) {
		this.dataSemanaInicial = dataSemanaInicial;
	}

	public Date getDataSemestreInicial() {
		return this.dataSemestreInicial;
	}

	public void setDataSemestreInicial(Date dataSemestreInicial) {
		this.dataSemestreInicial = dataSemestreInicial;
	}

	public Date getDataTrimestreInicial() {
		return this.dataTrimestreInicial;
	}

	public void setDataTrimestreInicial(Date dataTrimestreInicial) {
		this.dataTrimestreInicial = dataTrimestreInicial;
	}

	public String getDiaNome() {
		return this.diaNome;
	}

	public void setDiaNome(String diaNome) {
		this.diaNome = diaNome;
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

	public String getMesNome() {
		return this.mesNome;
	}

	public void setMesNome(String mesNome) {
		this.mesNome = mesNome;
	}

	public String getQuadrimestreNome() {
		return this.quadrimestreNome;
	}

	public void setQuadrimestreNome(String quadrimestreNome) {
		this.quadrimestreNome = quadrimestreNome;
	}

	public String getQuinzenaNome() {
		return this.quinzenaNome;
	}

	public void setQuinzenaNome(String quinzenaNome) {
		this.quinzenaNome = quinzenaNome;
	}

	public String getSemanaNome() {
		return this.semanaNome;
	}

	public void setSemanaNome(String semanaNome) {
		this.semanaNome = semanaNome;
	}

	public String getSemestreNome() {
		return this.semestreNome;
	}

	public void setSemestreNome(String semestreNome) {
		this.semestreNome = semestreNome;
	}

	public String getTrimestreNome() {
		return this.trimestreNome;
	}

	public void setTrimestreNome(String trimestreNome) {
		this.trimestreNome = trimestreNome;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<IndVrAno> getIndVrAnos() {
		return this.indVrAnos;
	}

	public void setIndVrAnos(List<IndVrAno> indVrAnos) {
		this.indVrAnos = indVrAnos;
	}

	public IndVrAno addIndVrAno(IndVrAno indVrAno) {
		getIndVrAnos().add(indVrAno);
		indVrAno.setGerPer(this);

		return indVrAno;
	}

	public IndVrAno removeIndVrAno(IndVrAno indVrAno) {
		getIndVrAnos().remove(indVrAno);
		indVrAno.setGerPer(null);

		return indVrAno;
	}

	public List<IndVrBimestre> getIndVrBimestres() {
		return this.indVrBimestres;
	}

	public void setIndVrBimestres(List<IndVrBimestre> indVrBimestres) {
		this.indVrBimestres = indVrBimestres;
	}

	public IndVrBimestre addIndVrBimestre(IndVrBimestre indVrBimestre) {
		getIndVrBimestres().add(indVrBimestre);
		indVrBimestre.setGerPer(this);

		return indVrBimestre;
	}

	public IndVrBimestre removeIndVrBimestre(IndVrBimestre indVrBimestre) {
		getIndVrBimestres().remove(indVrBimestre);
		indVrBimestre.setGerPer(null);

		return indVrBimestre;
	}

	public List<IndVrDia> getIndVrDias() {
		return this.indVrDias;
	}

	public void setIndVrDias(List<IndVrDia> indVrDias) {
		this.indVrDias = indVrDias;
	}

	public IndVrDia addIndVrDia(IndVrDia indVrDia) {
		getIndVrDias().add(indVrDia);
		indVrDia.setGerPer(this);

		return indVrDia;
	}

	public IndVrDia removeIndVrDia(IndVrDia indVrDia) {
		getIndVrDias().remove(indVrDia);
		indVrDia.setGerPer(null);

		return indVrDia;
	}

	public List<IndVrMes> getIndVrMes() {
		return this.indVrMes;
	}

	public void setIndVrMes(List<IndVrMes> indVrMes) {
		this.indVrMes = indVrMes;
	}

	public IndVrMes addIndVrMe(IndVrMes indVrMe) {
		getIndVrMes().add(indVrMe);
		indVrMe.setGerPer(this);

		return indVrMe;
	}

	public IndVrMes removeIndVrMe(IndVrMes indVrMe) {
		getIndVrMes().remove(indVrMe);
		indVrMe.setGerPer(null);

		return indVrMe;
	}

	public List<IndVrQuadrimestre> getIndVrQuadrimestres() {
		return this.indVrQuadrimestres;
	}

	public void setIndVrQuadrimestres(List<IndVrQuadrimestre> indVrQuadrimestres) {
		this.indVrQuadrimestres = indVrQuadrimestres;
	}

	public IndVrQuadrimestre addIndVrQuadrimestre(IndVrQuadrimestre indVrQuadrimestre) {
		getIndVrQuadrimestres().add(indVrQuadrimestre);
		indVrQuadrimestre.setGerPer(this);

		return indVrQuadrimestre;
	}

	public IndVrQuadrimestre removeIndVrQuadrimestre(IndVrQuadrimestre indVrQuadrimestre) {
		getIndVrQuadrimestres().remove(indVrQuadrimestre);
		indVrQuadrimestre.setGerPer(null);

		return indVrQuadrimestre;
	}

	public List<IndVrQuinzena> getIndVrQuinzenas() {
		return this.indVrQuinzenas;
	}

	public void setIndVrQuinzenas(List<IndVrQuinzena> indVrQuinzenas) {
		this.indVrQuinzenas = indVrQuinzenas;
	}

	public IndVrQuinzena addIndVrQuinzena(IndVrQuinzena indVrQuinzena) {
		getIndVrQuinzenas().add(indVrQuinzena);
		indVrQuinzena.setGerPer(this);

		return indVrQuinzena;
	}

	public IndVrQuinzena removeIndVrQuinzena(IndVrQuinzena indVrQuinzena) {
		getIndVrQuinzenas().remove(indVrQuinzena);
		indVrQuinzena.setGerPer(null);

		return indVrQuinzena;
	}

	public List<IndVrSemana> getIndVrSemanas() {
		return this.indVrSemanas;
	}

	public void setIndVrSemanas(List<IndVrSemana> indVrSemanas) {
		this.indVrSemanas = indVrSemanas;
	}

	public IndVrSemana addIndVrSemana(IndVrSemana indVrSemana) {
		getIndVrSemanas().add(indVrSemana);
		indVrSemana.setGerPer(this);

		return indVrSemana;
	}

	public IndVrSemana removeIndVrSemana(IndVrSemana indVrSemana) {
		getIndVrSemanas().remove(indVrSemana);
		indVrSemana.setGerPer(null);

		return indVrSemana;
	}

	public List<IndVrSemestre> getIndVrSemestres() {
		return this.indVrSemestres;
	}

	public void setIndVrSemestres(List<IndVrSemestre> indVrSemestres) {
		this.indVrSemestres = indVrSemestres;
	}

	public IndVrSemestre addIndVrSemestre(IndVrSemestre indVrSemestre) {
		getIndVrSemestres().add(indVrSemestre);
		indVrSemestre.setGerPer(this);

		return indVrSemestre;
	}

	public IndVrSemestre removeIndVrSemestre(IndVrSemestre indVrSemestre) {
		getIndVrSemestres().remove(indVrSemestre);
		indVrSemestre.setGerPer(null);

		return indVrSemestre;
	}

	public List<IndVrTrimestre> getIndVrTrimestres() {
		return this.indVrTrimestres;
	}

	public void setIndVrTrimestres(List<IndVrTrimestre> indVrTrimestres) {
		this.indVrTrimestres = indVrTrimestres;
	}

	public IndVrTrimestre addIndVrTrimestre(IndVrTrimestre indVrTrimestre) {
		getIndVrTrimestres().add(indVrTrimestre);
		indVrTrimestre.setGerPer(this);

		return indVrTrimestre;
	}

	public IndVrTrimestre removeIndVrTrimestre(IndVrTrimestre indVrTrimestre) {
		getIndVrTrimestres().remove(indVrTrimestre);
		indVrTrimestre.setGerPer(null);

		return indVrTrimestre;
	}

}