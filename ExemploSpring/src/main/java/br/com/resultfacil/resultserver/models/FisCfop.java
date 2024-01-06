package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.util.Date;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="fis_cfop")
@NamedQuery(name="FisCfop.findAll", query="SELECT f FROM FisCfop f")
public class FisCfop implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Temporal(TemporalType.DATE)
	@Column(name="data_validade", nullable=false)
	private Date dataValidade;

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

	@Column(name="nr_cfop", nullable=false, length=50)
	private String nrCfop;

	//bi-directional many-to-one association to MovItemserv
	@OneToMany(mappedBy="fisCfop")
	private List<MovItemserv> movItemservs;

	public FisCfop() {
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

	public Date getDataValidade() {
		return this.dataValidade;
	}

	public void setDataValidade(Date dataValidade) {
		this.dataValidade = dataValidade;
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

	public String getNrCfop() {
		return this.nrCfop;
	}

	public void setNrCfop(String nrCfop) {
		this.nrCfop = nrCfop;
	}

	public List<MovItemserv> getMovItemservs() {
		return this.movItemservs;
	}

	public void setMovItemservs(List<MovItemserv> movItemservs) {
		this.movItemservs = movItemservs;
	}

	public MovItemserv addMovItemserv(MovItemserv movItemserv) {
		getMovItemservs().add(movItemserv);
		movItemserv.setFisCfop(this);

		return movItemserv;
	}

	public MovItemserv removeMovItemserv(MovItemserv movItemserv) {
		getMovItemservs().remove(movItemserv);
		movItemserv.setFisCfop(null);

		return movItemserv;
	}

}