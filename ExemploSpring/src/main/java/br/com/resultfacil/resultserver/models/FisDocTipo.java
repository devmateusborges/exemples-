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
@Table(name="fis_doc_tipo")
@NamedQuery(name="FisDocTipo.findAll", query="SELECT f FROM FisDocTipo f")
public class FisDocTipo implements Serializable {
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

	@Column(nullable=false, length=50)
	private String modelo;

	@Column(nullable=false, length=100)
	private String nome;

	//bi-directional many-to-one association to FisDoc
	@OneToMany(mappedBy="fisDocTipo")
	private List<FisDoc> fisDocs;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="fisDocTipo")
	private List<Mov> movs;

	public FisDocTipo() {
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

	public String getModelo() {
		return this.modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
	}

	public String getNome() {
		return this.nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public List<FisDoc> getFisDocs() {
		return this.fisDocs;
	}

	public void setFisDocs(List<FisDoc> fisDocs) {
		this.fisDocs = fisDocs;
	}

	public FisDoc addFisDoc(FisDoc fisDoc) {
		getFisDocs().add(fisDoc);
		fisDoc.setFisDocTipo(this);

		return fisDoc;
	}

	public FisDoc removeFisDoc(FisDoc fisDoc) {
		getFisDocs().remove(fisDoc);
		fisDoc.setFisDocTipo(null);

		return fisDoc;
	}

	public List<Mov> getMovs() {
		return this.movs;
	}

	public void setMovs(List<Mov> movs) {
		this.movs = movs;
	}

	public Mov addMov(Mov mov) {
		getMovs().add(mov);
		mov.setFisDocTipo(this);

		return mov;
	}

	public Mov removeMov(Mov mov) {
		getMovs().remove(mov);
		mov.setFisDocTipo(null);

		return mov;
	}

}