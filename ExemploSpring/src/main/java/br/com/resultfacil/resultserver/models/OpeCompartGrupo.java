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
@Table(name="ope_compart_grupo")
@NamedQuery(name="OpeCompartGrupo.findAll", query="SELECT o FROM OpeCompartGrupo o")
public class OpeCompartGrupo implements Serializable {
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

	@Column(name="sigla_compart_grupo", nullable=false, length=50)
	private String siglaCompartGrupo;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="opeCompartGrupo")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCompartSubgrupo
	@OneToMany(mappedBy="opeCompartGrupo")
	private List<OpeCompartSubgrupo> opeCompartSubgrupos;

	public OpeCompartGrupo() {
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

	public String getSiglaCompartGrupo() {
		return this.siglaCompartGrupo;
	}

	public void setSiglaCompartGrupo(String siglaCompartGrupo) {
		this.siglaCompartGrupo = siglaCompartGrupo;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setOpeCompartGrupo(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setOpeCompartGrupo(null);

		return opeCentroConfig;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCompartSubgrupo> getOpeCompartSubgrupos() {
		return this.opeCompartSubgrupos;
	}

	public void setOpeCompartSubgrupos(List<OpeCompartSubgrupo> opeCompartSubgrupos) {
		this.opeCompartSubgrupos = opeCompartSubgrupos;
	}

	public OpeCompartSubgrupo addOpeCompartSubgrupo(OpeCompartSubgrupo opeCompartSubgrupo) {
		getOpeCompartSubgrupos().add(opeCompartSubgrupo);
		opeCompartSubgrupo.setOpeCompartGrupo(this);

		return opeCompartSubgrupo;
	}

	public OpeCompartSubgrupo removeOpeCompartSubgrupo(OpeCompartSubgrupo opeCompartSubgrupo) {
		getOpeCompartSubgrupos().remove(opeCompartSubgrupo);
		opeCompartSubgrupo.setOpeCompartGrupo(null);

		return opeCompartSubgrupo;
	}

}