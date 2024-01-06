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
@Table(name="ger_marca")
@NamedQuery(name="GerMarca.findAll", query="SELECT g FROM GerMarca g")
public class GerMarca implements Serializable {
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

	@Column(name="unit_id", nullable=false, length=36)
	private String unitId;

	//bi-directional many-to-one association to GerMarcaModelo
	@OneToMany(mappedBy="gerMarca")
	private List<GerMarcaModelo> gerMarcaModelos;

	//bi-directional many-to-one association to GerMarcaPessoa
	@OneToMany(mappedBy="gerMarca")
	private List<GerMarcaPessoa> gerMarcaPessoas;

	public GerMarca() {
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

	public String getUnitId() {
		return this.unitId;
	}

	public void setUnitId(String unitId) {
		this.unitId = unitId;
	}

	public List<GerMarcaModelo> getGerMarcaModelos() {
		return this.gerMarcaModelos;
	}

	public void setGerMarcaModelos(List<GerMarcaModelo> gerMarcaModelos) {
		this.gerMarcaModelos = gerMarcaModelos;
	}

	public GerMarcaModelo addGerMarcaModelo(GerMarcaModelo gerMarcaModelo) {
		getGerMarcaModelos().add(gerMarcaModelo);
		gerMarcaModelo.setGerMarca(this);

		return gerMarcaModelo;
	}

	public GerMarcaModelo removeGerMarcaModelo(GerMarcaModelo gerMarcaModelo) {
		getGerMarcaModelos().remove(gerMarcaModelo);
		gerMarcaModelo.setGerMarca(null);

		return gerMarcaModelo;
	}

	public List<GerMarcaPessoa> getGerMarcaPessoas() {
		return this.gerMarcaPessoas;
	}

	public void setGerMarcaPessoas(List<GerMarcaPessoa> gerMarcaPessoas) {
		this.gerMarcaPessoas = gerMarcaPessoas;
	}

	public GerMarcaPessoa addGerMarcaPessoa(GerMarcaPessoa gerMarcaPessoa) {
		getGerMarcaPessoas().add(gerMarcaPessoa);
		gerMarcaPessoa.setGerMarca(this);

		return gerMarcaPessoa;
	}

	public GerMarcaPessoa removeGerMarcaPessoa(GerMarcaPessoa gerMarcaPessoa) {
		getGerMarcaPessoas().remove(gerMarcaPessoa);
		gerMarcaPessoa.setGerMarca(null);

		return gerMarcaPessoa;
	}

}