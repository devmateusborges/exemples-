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
@Table(name="ope_compart_subgrupo")
@NamedQuery(name="OpeCompartSubgrupo.findAll", query="SELECT o FROM OpeCompartSubgrupo o")
public class OpeCompartSubgrupo implements Serializable {
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

	@Column(name="sigla_compart_subgrupo", nullable=false, length=50)
	private String siglaCompartSubgrupo;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="opeCompartSubgrupo")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to OpeCompart
	@OneToMany(mappedBy="opeCompartSubgrupo")
	private List<OpeCompart> opeComparts;

	//bi-directional many-to-one association to OpeCompartGrupo
	@ManyToOne
	@JoinColumn(name="ope_compart_grupo_id", nullable=false)
	private OpeCompartGrupo opeCompartGrupo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCompartSubgrupo() {
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

	public String getSiglaCompartSubgrupo() {
		return this.siglaCompartSubgrupo;
	}

	public void setSiglaCompartSubgrupo(String siglaCompartSubgrupo) {
		this.siglaCompartSubgrupo = siglaCompartSubgrupo;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setOpeCompartSubgrupo(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setOpeCompartSubgrupo(null);

		return opeCentroConfig;
	}

	public List<OpeCompart> getOpeComparts() {
		return this.opeComparts;
	}

	public void setOpeComparts(List<OpeCompart> opeComparts) {
		this.opeComparts = opeComparts;
	}

	public OpeCompart addOpeCompart(OpeCompart opeCompart) {
		getOpeComparts().add(opeCompart);
		opeCompart.setOpeCompartSubgrupo(this);

		return opeCompart;
	}

	public OpeCompart removeOpeCompart(OpeCompart opeCompart) {
		getOpeComparts().remove(opeCompart);
		opeCompart.setOpeCompartSubgrupo(null);

		return opeCompart;
	}

	public OpeCompartGrupo getOpeCompartGrupo() {
		return this.opeCompartGrupo;
	}

	public void setOpeCompartGrupo(OpeCompartGrupo opeCompartGrupo) {
		this.opeCompartGrupo = opeCompartGrupo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}