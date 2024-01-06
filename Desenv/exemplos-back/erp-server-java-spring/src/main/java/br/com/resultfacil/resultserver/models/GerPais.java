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
@Table(name="ger_pais")
@NamedQuery(name="GerPais.findAll", query="SELECT g FROM GerPais g")
public class GerPais implements Serializable {
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

	@Column(name="nr_pais", nullable=false, length=50)
	private String nrPais;

	@Column(name="sigla_pais", length=50)
	private String siglaPais;

	//bi-directional many-to-one association to GerUf
	@OneToMany(mappedBy="gerPai")
	private List<GerUf> gerUfs;

	public GerPais() {
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

	public String getNrPais() {
		return this.nrPais;
	}

	public void setNrPais(String nrPais) {
		this.nrPais = nrPais;
	}

	public String getSiglaPais() {
		return this.siglaPais;
	}

	public void setSiglaPais(String siglaPais) {
		this.siglaPais = siglaPais;
	}

	public List<GerUf> getGerUfs() {
		return this.gerUfs;
	}

	public void setGerUfs(List<GerUf> gerUfs) {
		this.gerUfs = gerUfs;
	}

	public GerUf addGerUf(GerUf gerUf) {
		getGerUfs().add(gerUf);
		gerUf.setGerPai(this);

		return gerUf;
	}

	public GerUf removeGerUf(GerUf gerUf) {
		getGerUfs().remove(gerUf);
		gerUf.setGerPai(null);

		return gerUf;
	}

}