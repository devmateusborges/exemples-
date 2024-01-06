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
@Table(name="ope_centro_grupo")
@NamedQuery(name="OpeCentroGrupo.findAll", query="SELECT o FROM OpeCentroGrupo o")
public class OpeCentroGrupo implements Serializable {
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

	@Column(name="sigla_centro_grupo", nullable=false, length=50)
	private String siglaCentroGrupo;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="opeCentroGrupo")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to OpeCentroSubtipo
	@ManyToOne
	@JoinColumn(name="ope_centro_subtipo_id", nullable=false)
	private OpeCentroSubtipo opeCentroSubtipo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCentroSubgrupo
	@OneToMany(mappedBy="opeCentroGrupo")
	private List<OpeCentroSubgrupo> opeCentroSubgrupos;

	public OpeCentroGrupo() {
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

	public String getSiglaCentroGrupo() {
		return this.siglaCentroGrupo;
	}

	public void setSiglaCentroGrupo(String siglaCentroGrupo) {
		this.siglaCentroGrupo = siglaCentroGrupo;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setOpeCentroGrupo(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setOpeCentroGrupo(null);

		return opeCentroConfig;
	}

	public OpeCentroSubtipo getOpeCentroSubtipo() {
		return this.opeCentroSubtipo;
	}

	public void setOpeCentroSubtipo(OpeCentroSubtipo opeCentroSubtipo) {
		this.opeCentroSubtipo = opeCentroSubtipo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCentroSubgrupo> getOpeCentroSubgrupos() {
		return this.opeCentroSubgrupos;
	}

	public void setOpeCentroSubgrupos(List<OpeCentroSubgrupo> opeCentroSubgrupos) {
		this.opeCentroSubgrupos = opeCentroSubgrupos;
	}

	public OpeCentroSubgrupo addOpeCentroSubgrupo(OpeCentroSubgrupo opeCentroSubgrupo) {
		getOpeCentroSubgrupos().add(opeCentroSubgrupo);
		opeCentroSubgrupo.setOpeCentroGrupo(this);

		return opeCentroSubgrupo;
	}

	public OpeCentroSubgrupo removeOpeCentroSubgrupo(OpeCentroSubgrupo opeCentroSubgrupo) {
		getOpeCentroSubgrupos().remove(opeCentroSubgrupo);
		opeCentroSubgrupo.setOpeCentroGrupo(null);

		return opeCentroSubgrupo;
	}

}