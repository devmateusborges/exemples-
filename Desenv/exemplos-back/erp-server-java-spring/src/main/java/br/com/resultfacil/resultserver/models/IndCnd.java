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
@Table(name="ind_cnd")
@NamedQuery(name="IndCnd.findAll", query="SELECT i FROM IndCnd i")
public class IndCnd implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(length=1)
	private String ativo;

	@Column(name="config_cnd", length=2147483647)
	private String configCnd;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(length=250)
	private String nome;

	@Column(length=2)
	private String tipo;

	//bi-directional many-to-one association to IndFtd
	@OneToMany(mappedBy="indCnd")
	private List<IndFtd> indFtds;

	public IndCnd() {
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

	public String getConfigCnd() {
		return this.configCnd;
	}

	public void setConfigCnd(String configCnd) {
		this.configCnd = configCnd;
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

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public List<IndFtd> getIndFtds() {
		return this.indFtds;
	}

	public void setIndFtds(List<IndFtd> indFtds) {
		this.indFtds = indFtds;
	}

	public IndFtd addIndFtd(IndFtd indFtd) {
		getIndFtds().add(indFtd);
		indFtd.setIndCnd(this);

		return indFtd;
	}

	public IndFtd removeIndFtd(IndFtd indFtd) {
		getIndFtds().remove(indFtd);
		indFtd.setIndCnd(null);

		return indFtd;
	}

}