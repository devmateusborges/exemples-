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
@Table(name="fin_pagrec_tipo")
@NamedQuery(name="FinPagrecTipo.findAll", query="SELECT f FROM FinPagrecTipo f")
public class FinPagrecTipo implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="aceita_entrada", nullable=false, length=1)
	private String aceitaEntrada;

	@Column(name="aceita_saida", nullable=false, length=1)
	private String aceitaSaida;

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

	//bi-directional many-to-one association to FinPagrec
	@OneToMany(mappedBy="finPagrecTipo")
	private List<FinPagrec> finPagrecs;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public FinPagrecTipo() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getAceitaEntrada() {
		return this.aceitaEntrada;
	}

	public void setAceitaEntrada(String aceitaEntrada) {
		this.aceitaEntrada = aceitaEntrada;
	}

	public String getAceitaSaida() {
		return this.aceitaSaida;
	}

	public void setAceitaSaida(String aceitaSaida) {
		this.aceitaSaida = aceitaSaida;
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

	public List<FinPagrec> getFinPagrecs() {
		return this.finPagrecs;
	}

	public void setFinPagrecs(List<FinPagrec> finPagrecs) {
		this.finPagrecs = finPagrecs;
	}

	public FinPagrec addFinPagrec(FinPagrec finPagrec) {
		getFinPagrecs().add(finPagrec);
		finPagrec.setFinPagrecTipo(this);

		return finPagrec;
	}

	public FinPagrec removeFinPagrec(FinPagrec finPagrec) {
		getFinPagrecs().remove(finPagrec);
		finPagrec.setFinPagrecTipo(null);

		return finPagrec;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}