package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ind")
@NamedQuery(name="Ind.findAll", query="SELECT i FROM Ind i")
public class Ind implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="acumular_ano", length=1)
	private String acumularAno;

	@Column(name="acumular_bimestre", length=1)
	private String acumularBimestre;

	@Column(name="acumular_mes", length=1)
	private String acumularMes;

	@Column(name="acumular_quadrimestre", length=1)
	private String acumularQuadrimestre;

	@Column(name="acumular_quinzena", length=1)
	private String acumularQuinzena;

	@Column(name="acumular_semana", length=1)
	private String acumularSemana;

	@Column(name="acumular_semestre", length=1)
	private String acumularSemestre;

	@Column(name="acumular_trimestre", length=1)
	private String acumularTrimestre;

	@Column(name="campo_ordenacao", length=50)
	private String campoOrdenacao;

	@Column(name="casas_dec")
	private Integer casasDec;

	@Column(name="exibir_ano", length=1)
	private String exibirAno;

	@Column(name="exibir_bimestre", length=1)
	private String exibirBimestre;

	@Column(name="exibir_dia", length=1)
	private String exibirDia;

	@Column(name="exibir_media_meta", length=1)
	private String exibirMediaMeta;

	@Column(name="exibir_media_real", length=1)
	private String exibirMediaReal;

	@Column(name="exibir_mes", length=1)
	private String exibirMes;

	@Column(name="exibir_quadrimestre", length=1)
	private String exibirQuadrimestre;

	@Column(name="exibir_quinzena", length=1)
	private String exibirQuinzena;

	@Column(name="exibir_semana", length=1)
	private String exibirSemana;

	@Column(name="exibir_semestre", length=1)
	private String exibirSemestre;

	@Column(name="exibir_trimestre", length=1)
	private String exibirTrimestre;

	@Column(name="grafico_tipo_atributo")
	private Integer graficoTipoAtributo;

	@Column(name="grafico_tipo_ind")
	private Integer graficoTipoInd;

	@Column(name="grafico_valor_vazio_zero", length=1)
	private String graficoValorVazioZero;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="metodo_ordenacao")
	private Integer metodoOrdenacao;

	@Column(length=100)
	private String nome;

	@Column(name="sigla_ind", length=50)
	private String siglaInd;

	@Column(name="tipo_acumulo")
	private Integer tipoAcumulo;

	@Column(name="totalizador_atributo")
	private Integer totalizadorAtributo;

	//bi-directional many-to-one association to GerUmedida
	@ManyToOne
	@JoinColumn(name="ger_umedida_id")
	private GerUmedida gerUmedida;

	//bi-directional many-to-one association to Ind
	@ManyToOne
	@JoinColumn(name="ind_id_ponderacao")
	private Ind ind;

	//bi-directional many-to-one association to Ind
	@OneToMany(mappedBy="ind")
	private List<Ind> inds;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to IndRelac
	@OneToMany(mappedBy="ind1")
	private List<IndRelac> indRelacs1;

	//bi-directional many-to-one association to IndRelac
	@OneToMany(mappedBy="ind2")
	private List<IndRelac> indRelacs2;

	public Ind() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getAcumularAno() {
		return this.acumularAno;
	}

	public void setAcumularAno(String acumularAno) {
		this.acumularAno = acumularAno;
	}

	public String getAcumularBimestre() {
		return this.acumularBimestre;
	}

	public void setAcumularBimestre(String acumularBimestre) {
		this.acumularBimestre = acumularBimestre;
	}

	public String getAcumularMes() {
		return this.acumularMes;
	}

	public void setAcumularMes(String acumularMes) {
		this.acumularMes = acumularMes;
	}

	public String getAcumularQuadrimestre() {
		return this.acumularQuadrimestre;
	}

	public void setAcumularQuadrimestre(String acumularQuadrimestre) {
		this.acumularQuadrimestre = acumularQuadrimestre;
	}

	public String getAcumularQuinzena() {
		return this.acumularQuinzena;
	}

	public void setAcumularQuinzena(String acumularQuinzena) {
		this.acumularQuinzena = acumularQuinzena;
	}

	public String getAcumularSemana() {
		return this.acumularSemana;
	}

	public void setAcumularSemana(String acumularSemana) {
		this.acumularSemana = acumularSemana;
	}

	public String getAcumularSemestre() {
		return this.acumularSemestre;
	}

	public void setAcumularSemestre(String acumularSemestre) {
		this.acumularSemestre = acumularSemestre;
	}

	public String getAcumularTrimestre() {
		return this.acumularTrimestre;
	}

	public void setAcumularTrimestre(String acumularTrimestre) {
		this.acumularTrimestre = acumularTrimestre;
	}

	public String getCampoOrdenacao() {
		return this.campoOrdenacao;
	}

	public void setCampoOrdenacao(String campoOrdenacao) {
		this.campoOrdenacao = campoOrdenacao;
	}

	public Integer getCasasDec() {
		return this.casasDec;
	}

	public void setCasasDec(Integer casasDec) {
		this.casasDec = casasDec;
	}

	public String getExibirAno() {
		return this.exibirAno;
	}

	public void setExibirAno(String exibirAno) {
		this.exibirAno = exibirAno;
	}

	public String getExibirBimestre() {
		return this.exibirBimestre;
	}

	public void setExibirBimestre(String exibirBimestre) {
		this.exibirBimestre = exibirBimestre;
	}

	public String getExibirDia() {
		return this.exibirDia;
	}

	public void setExibirDia(String exibirDia) {
		this.exibirDia = exibirDia;
	}

	public String getExibirMediaMeta() {
		return this.exibirMediaMeta;
	}

	public void setExibirMediaMeta(String exibirMediaMeta) {
		this.exibirMediaMeta = exibirMediaMeta;
	}

	public String getExibirMediaReal() {
		return this.exibirMediaReal;
	}

	public void setExibirMediaReal(String exibirMediaReal) {
		this.exibirMediaReal = exibirMediaReal;
	}

	public String getExibirMes() {
		return this.exibirMes;
	}

	public void setExibirMes(String exibirMes) {
		this.exibirMes = exibirMes;
	}

	public String getExibirQuadrimestre() {
		return this.exibirQuadrimestre;
	}

	public void setExibirQuadrimestre(String exibirQuadrimestre) {
		this.exibirQuadrimestre = exibirQuadrimestre;
	}

	public String getExibirQuinzena() {
		return this.exibirQuinzena;
	}

	public void setExibirQuinzena(String exibirQuinzena) {
		this.exibirQuinzena = exibirQuinzena;
	}

	public String getExibirSemana() {
		return this.exibirSemana;
	}

	public void setExibirSemana(String exibirSemana) {
		this.exibirSemana = exibirSemana;
	}

	public String getExibirSemestre() {
		return this.exibirSemestre;
	}

	public void setExibirSemestre(String exibirSemestre) {
		this.exibirSemestre = exibirSemestre;
	}

	public String getExibirTrimestre() {
		return this.exibirTrimestre;
	}

	public void setExibirTrimestre(String exibirTrimestre) {
		this.exibirTrimestre = exibirTrimestre;
	}

	public Integer getGraficoTipoAtributo() {
		return this.graficoTipoAtributo;
	}

	public void setGraficoTipoAtributo(Integer graficoTipoAtributo) {
		this.graficoTipoAtributo = graficoTipoAtributo;
	}

	public Integer getGraficoTipoInd() {
		return this.graficoTipoInd;
	}

	public void setGraficoTipoInd(Integer graficoTipoInd) {
		this.graficoTipoInd = graficoTipoInd;
	}

	public String getGraficoValorVazioZero() {
		return this.graficoValorVazioZero;
	}

	public void setGraficoValorVazioZero(String graficoValorVazioZero) {
		this.graficoValorVazioZero = graficoValorVazioZero;
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

	public Integer getMetodoOrdenacao() {
		return this.metodoOrdenacao;
	}

	public void setMetodoOrdenacao(Integer metodoOrdenacao) {
		this.metodoOrdenacao = metodoOrdenacao;
	}

	public String getNome() {
		return this.nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getSiglaInd() {
		return this.siglaInd;
	}

	public void setSiglaInd(String siglaInd) {
		this.siglaInd = siglaInd;
	}

	public Integer getTipoAcumulo() {
		return this.tipoAcumulo;
	}

	public void setTipoAcumulo(Integer tipoAcumulo) {
		this.tipoAcumulo = tipoAcumulo;
	}

	public Integer getTotalizadorAtributo() {
		return this.totalizadorAtributo;
	}

	public void setTotalizadorAtributo(Integer totalizadorAtributo) {
		this.totalizadorAtributo = totalizadorAtributo;
	}

	public GerUmedida getGerUmedida() {
		return this.gerUmedida;
	}

	public void setGerUmedida(GerUmedida gerUmedida) {
		this.gerUmedida = gerUmedida;
	}

	public Ind getInd() {
		return this.ind;
	}

	public void setInd(Ind ind) {
		this.ind = ind;
	}

	public List<Ind> getInds() {
		return this.inds;
	}

	public void setInds(List<Ind> inds) {
		this.inds = inds;
	}

	public Ind addInd(Ind ind) {
		getInds().add(ind);
		ind.setInd(this);

		return ind;
	}

	public Ind removeInd(Ind ind) {
		getInds().remove(ind);
		ind.setInd(null);

		return ind;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<IndRelac> getIndRelacs1() {
		return this.indRelacs1;
	}

	public void setIndRelacs1(List<IndRelac> indRelacs1) {
		this.indRelacs1 = indRelacs1;
	}

	public IndRelac addIndRelacs1(IndRelac indRelacs1) {
		getIndRelacs1().add(indRelacs1);
		indRelacs1.setInd1(this);

		return indRelacs1;
	}

	public IndRelac removeIndRelacs1(IndRelac indRelacs1) {
		getIndRelacs1().remove(indRelacs1);
		indRelacs1.setInd1(null);

		return indRelacs1;
	}

	public List<IndRelac> getIndRelacs2() {
		return this.indRelacs2;
	}

	public void setIndRelacs2(List<IndRelac> indRelacs2) {
		this.indRelacs2 = indRelacs2;
	}

	public IndRelac addIndRelacs2(IndRelac indRelacs2) {
		getIndRelacs2().add(indRelacs2);
		indRelacs2.setInd2(this);

		return indRelacs2;
	}

	public IndRelac removeIndRelacs2(IndRelac indRelacs2) {
		getIndRelacs2().remove(indRelacs2);
		indRelacs2.setInd2(null);

		return indRelacs2;
	}

}