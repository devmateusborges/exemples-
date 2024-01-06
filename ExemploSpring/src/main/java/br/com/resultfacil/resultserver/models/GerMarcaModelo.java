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
@Table(name="ger_marca_modelo")
@NamedQuery(name="GerMarcaModelo.findAll", query="SELECT g FROM GerMarcaModelo g")
public class GerMarcaModelo implements Serializable {
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

	//bi-directional many-to-one association to GerMarca
	@ManyToOne
	@JoinColumn(name="ger_marca_id", nullable=false)
	private GerMarca gerMarca;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCentro2
	@OneToMany(mappedBy="gerMarcaModelo")
	private List<OpeCentro2> opeCentro2s;

	//bi-directional many-to-one association to OpeCentro2MovMedia
	@OneToMany(mappedBy="gerMarcaModelo")
	private List<OpeCentro2MovMedia> opeCentro2MovMedias;

	public GerMarcaModelo() {
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

	public GerMarca getGerMarca() {
		return this.gerMarca;
	}

	public void setGerMarca(GerMarca gerMarca) {
		this.gerMarca = gerMarca;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCentro2> getOpeCentro2s() {
		return this.opeCentro2s;
	}

	public void setOpeCentro2s(List<OpeCentro2> opeCentro2s) {
		this.opeCentro2s = opeCentro2s;
	}

	public OpeCentro2 addOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().add(opeCentro2);
		opeCentro2.setGerMarcaModelo(this);

		return opeCentro2;
	}

	public OpeCentro2 removeOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().remove(opeCentro2);
		opeCentro2.setGerMarcaModelo(null);

		return opeCentro2;
	}

	public List<OpeCentro2MovMedia> getOpeCentro2MovMedias() {
		return this.opeCentro2MovMedias;
	}

	public void setOpeCentro2MovMedias(List<OpeCentro2MovMedia> opeCentro2MovMedias) {
		this.opeCentro2MovMedias = opeCentro2MovMedias;
	}

	public OpeCentro2MovMedia addOpeCentro2MovMedia(OpeCentro2MovMedia opeCentro2MovMedia) {
		getOpeCentro2MovMedias().add(opeCentro2MovMedia);
		opeCentro2MovMedia.setGerMarcaModelo(this);

		return opeCentro2MovMedia;
	}

	public OpeCentro2MovMedia removeOpeCentro2MovMedia(OpeCentro2MovMedia opeCentro2MovMedia) {
		getOpeCentro2MovMedias().remove(opeCentro2MovMedia);
		opeCentro2MovMedia.setGerMarcaModelo(null);

		return opeCentro2MovMedia;
	}

}