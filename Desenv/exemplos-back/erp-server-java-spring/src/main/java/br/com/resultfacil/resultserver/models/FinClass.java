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
@Table(name="fin_class")
@NamedQuery(name="FinClass.findAll", query="SELECT f FROM FinClass f")
public class FinClass implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(name="fixo_variavel", nullable=false, length=1)
	private String fixoVariavel;

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

	@Column(name="sigla_class", length=15)
	private String siglaClass;

	@Column(name="tipo_es", nullable=false, length=1)
	private String tipoEs;

	@Column(name="tipo_fluxo", nullable=false, length=2)
	private String tipoFluxo;

	@Column(name="tipo_prev", length=1)
	private String tipoPrev;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FinClassAgrupGrupo
	@OneToMany(mappedBy="finClass")
	private List<FinClassAgrupGrupo> finClassAgrupGrupos;

	//bi-directional many-to-one association to FinPagrecClass
	@OneToMany(mappedBy="finClass")
	private List<FinPagrecClass> finPagrecClasses;

	//bi-directional many-to-one association to FinPagrecPrev
	@OneToMany(mappedBy="finClass")
	private List<FinPagrecPrev> finPagrecPrevs;

	public FinClass() {
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

	public String getFixoVariavel() {
		return this.fixoVariavel;
	}

	public void setFixoVariavel(String fixoVariavel) {
		this.fixoVariavel = fixoVariavel;
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

	public String getSiglaClass() {
		return this.siglaClass;
	}

	public void setSiglaClass(String siglaClass) {
		this.siglaClass = siglaClass;
	}

	public String getTipoEs() {
		return this.tipoEs;
	}

	public void setTipoEs(String tipoEs) {
		this.tipoEs = tipoEs;
	}

	public String getTipoFluxo() {
		return this.tipoFluxo;
	}

	public void setTipoFluxo(String tipoFluxo) {
		this.tipoFluxo = tipoFluxo;
	}

	public String getTipoPrev() {
		return this.tipoPrev;
	}

	public void setTipoPrev(String tipoPrev) {
		this.tipoPrev = tipoPrev;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<FinClassAgrupGrupo> getFinClassAgrupGrupos() {
		return this.finClassAgrupGrupos;
	}

	public void setFinClassAgrupGrupos(List<FinClassAgrupGrupo> finClassAgrupGrupos) {
		this.finClassAgrupGrupos = finClassAgrupGrupos;
	}

	public FinClassAgrupGrupo addFinClassAgrupGrupo(FinClassAgrupGrupo finClassAgrupGrupo) {
		getFinClassAgrupGrupos().add(finClassAgrupGrupo);
		finClassAgrupGrupo.setFinClass(this);

		return finClassAgrupGrupo;
	}

	public FinClassAgrupGrupo removeFinClassAgrupGrupo(FinClassAgrupGrupo finClassAgrupGrupo) {
		getFinClassAgrupGrupos().remove(finClassAgrupGrupo);
		finClassAgrupGrupo.setFinClass(null);

		return finClassAgrupGrupo;
	}

	public List<FinPagrecClass> getFinPagrecClasses() {
		return this.finPagrecClasses;
	}

	public void setFinPagrecClasses(List<FinPagrecClass> finPagrecClasses) {
		this.finPagrecClasses = finPagrecClasses;
	}

	public FinPagrecClass addFinPagrecClass(FinPagrecClass finPagrecClass) {
		getFinPagrecClasses().add(finPagrecClass);
		finPagrecClass.setFinClass(this);

		return finPagrecClass;
	}

	public FinPagrecClass removeFinPagrecClass(FinPagrecClass finPagrecClass) {
		getFinPagrecClasses().remove(finPagrecClass);
		finPagrecClass.setFinClass(null);

		return finPagrecClass;
	}

	public List<FinPagrecPrev> getFinPagrecPrevs() {
		return this.finPagrecPrevs;
	}

	public void setFinPagrecPrevs(List<FinPagrecPrev> finPagrecPrevs) {
		this.finPagrecPrevs = finPagrecPrevs;
	}

	public FinPagrecPrev addFinPagrecPrev(FinPagrecPrev finPagrecPrev) {
		getFinPagrecPrevs().add(finPagrecPrev);
		finPagrecPrev.setFinClass(this);

		return finPagrecPrev;
	}

	public FinPagrecPrev removeFinPagrecPrev(FinPagrecPrev finPagrecPrev) {
		getFinPagrecPrevs().remove(finPagrecPrev);
		finPagrecPrev.setFinClass(null);

		return finPagrecPrev;
	}

}