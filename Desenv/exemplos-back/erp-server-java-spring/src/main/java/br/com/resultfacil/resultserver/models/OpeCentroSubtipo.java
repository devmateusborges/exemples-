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
@Table(name="ope_centro_subtipo")
@NamedQuery(name="OpeCentroSubtipo.findAll", query="SELECT o FROM OpeCentroSubtipo o")
public class OpeCentroSubtipo implements Serializable {
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

	@Column(nullable=false, length=100)
	private String nome;

	@Column(name="tipo_destinacao", length=1)
	private String tipoDestinacao;

	//bi-directional many-to-one association to OpeCentro1
	@OneToMany(mappedBy="opeCentroSubtipo")
	private List<OpeCentro1> opeCentro1s;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="opeCentroSubtipo")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to OpeCentroGrupo
	@OneToMany(mappedBy="opeCentroSubtipo")
	private List<OpeCentroGrupo> opeCentroGrupos;

	//bi-directional many-to-one association to OpeCentroRatFator
	@OneToMany(mappedBy="opeCentroSubtipo")
	private List<OpeCentroRatFator> opeCentroRatFators;

	//bi-directional many-to-one association to OpeCentroTipo
	@ManyToOne
	@JoinColumn(name="ope_centro_tipo_id", nullable=false)
	private OpeCentroTipo opeCentroTipo;

	public OpeCentroSubtipo() {
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

	public String getNome() {
		return this.nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getTipoDestinacao() {
		return this.tipoDestinacao;
	}

	public void setTipoDestinacao(String tipoDestinacao) {
		this.tipoDestinacao = tipoDestinacao;
	}

	public List<OpeCentro1> getOpeCentro1s() {
		return this.opeCentro1s;
	}

	public void setOpeCentro1s(List<OpeCentro1> opeCentro1s) {
		this.opeCentro1s = opeCentro1s;
	}

	public OpeCentro1 addOpeCentro1(OpeCentro1 opeCentro1) {
		getOpeCentro1s().add(opeCentro1);
		opeCentro1.setOpeCentroSubtipo(this);

		return opeCentro1;
	}

	public OpeCentro1 removeOpeCentro1(OpeCentro1 opeCentro1) {
		getOpeCentro1s().remove(opeCentro1);
		opeCentro1.setOpeCentroSubtipo(null);

		return opeCentro1;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setOpeCentroSubtipo(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setOpeCentroSubtipo(null);

		return opeCentroConfig;
	}

	public List<OpeCentroGrupo> getOpeCentroGrupos() {
		return this.opeCentroGrupos;
	}

	public void setOpeCentroGrupos(List<OpeCentroGrupo> opeCentroGrupos) {
		this.opeCentroGrupos = opeCentroGrupos;
	}

	public OpeCentroGrupo addOpeCentroGrupo(OpeCentroGrupo opeCentroGrupo) {
		getOpeCentroGrupos().add(opeCentroGrupo);
		opeCentroGrupo.setOpeCentroSubtipo(this);

		return opeCentroGrupo;
	}

	public OpeCentroGrupo removeOpeCentroGrupo(OpeCentroGrupo opeCentroGrupo) {
		getOpeCentroGrupos().remove(opeCentroGrupo);
		opeCentroGrupo.setOpeCentroSubtipo(null);

		return opeCentroGrupo;
	}

	public List<OpeCentroRatFator> getOpeCentroRatFators() {
		return this.opeCentroRatFators;
	}

	public void setOpeCentroRatFators(List<OpeCentroRatFator> opeCentroRatFators) {
		this.opeCentroRatFators = opeCentroRatFators;
	}

	public OpeCentroRatFator addOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().add(opeCentroRatFator);
		opeCentroRatFator.setOpeCentroSubtipo(this);

		return opeCentroRatFator;
	}

	public OpeCentroRatFator removeOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().remove(opeCentroRatFator);
		opeCentroRatFator.setOpeCentroSubtipo(null);

		return opeCentroRatFator;
	}

	public OpeCentroTipo getOpeCentroTipo() {
		return this.opeCentroTipo;
	}

	public void setOpeCentroTipo(OpeCentroTipo opeCentroTipo) {
		this.opeCentroTipo = opeCentroTipo;
	}

}