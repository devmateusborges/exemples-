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
@Table(name="ope_centro_tipo")
@NamedQuery(name="OpeCentroTipo.findAll", query="SELECT o FROM OpeCentroTipo o")
public class OpeCentroTipo implements Serializable {
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

	@Column(name="tipo_es", nullable=false, length=1)
	private String tipoEs;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="opeCentroTipo")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to OpeCentroSubtipo
	@OneToMany(mappedBy="opeCentroTipo")
	private List<OpeCentroSubtipo> opeCentroSubtipos;

	public OpeCentroTipo() {
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

	public String getTipoEs() {
		return this.tipoEs;
	}

	public void setTipoEs(String tipoEs) {
		this.tipoEs = tipoEs;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setOpeCentroTipo(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setOpeCentroTipo(null);

		return opeCentroConfig;
	}

	public List<OpeCentroSubtipo> getOpeCentroSubtipos() {
		return this.opeCentroSubtipos;
	}

	public void setOpeCentroSubtipos(List<OpeCentroSubtipo> opeCentroSubtipos) {
		this.opeCentroSubtipos = opeCentroSubtipos;
	}

	public OpeCentroSubtipo addOpeCentroSubtipo(OpeCentroSubtipo opeCentroSubtipo) {
		getOpeCentroSubtipos().add(opeCentroSubtipo);
		opeCentroSubtipo.setOpeCentroTipo(this);

		return opeCentroSubtipo;
	}

	public OpeCentroSubtipo removeOpeCentroSubtipo(OpeCentroSubtipo opeCentroSubtipo) {
		getOpeCentroSubtipos().remove(opeCentroSubtipo);
		opeCentroSubtipo.setOpeCentroTipo(null);

		return opeCentroSubtipo;
	}

}