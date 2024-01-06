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
@Table(name="fis_tributo")
@NamedQuery(name="FisTributo.findAll", query="SELECT f FROM FisTributo f")
public class FisTributo implements Serializable {
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

	@Column(name="nr_tributo", nullable=false, length=50)
	private String nrTributo;

	//bi-directional many-to-one association to FisTributacao
	@OneToMany(mappedBy="fisTributo")
	private List<FisTributacao> fisTributacaos;

	public FisTributo() {
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

	public String getNrTributo() {
		return this.nrTributo;
	}

	public void setNrTributo(String nrTributo) {
		this.nrTributo = nrTributo;
	}

	public List<FisTributacao> getFisTributacaos() {
		return this.fisTributacaos;
	}

	public void setFisTributacaos(List<FisTributacao> fisTributacaos) {
		this.fisTributacaos = fisTributacaos;
	}

	public FisTributacao addFisTributacao(FisTributacao fisTributacao) {
		getFisTributacaos().add(fisTributacao);
		fisTributacao.setFisTributo(this);

		return fisTributacao;
	}

	public FisTributacao removeFisTributacao(FisTributacao fisTributacao) {
		getFisTributacaos().remove(fisTributacao);
		fisTributacao.setFisTributo(null);

		return fisTributacao;
	}

}