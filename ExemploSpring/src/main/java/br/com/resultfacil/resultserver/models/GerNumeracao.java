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
@Table(name="ger_numeracao")
@NamedQuery(name="GerNumeracao.findAll", query="SELECT g FROM GerNumeracao g")
public class GerNumeracao implements Serializable {
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

	@Column(nullable=false, length=3)
	private String serie;

	@Column(name="ultimo_nr", nullable=false)
	private Integer ultimoNr;

	//bi-directional many-to-one association to FinDocTipo
	@OneToMany(mappedBy="gerNumeracao")
	private List<FinDocTipo> finDocTipos;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to MovOperacao
	@OneToMany(mappedBy="gerNumeracao")
	private List<MovOperacao> movOperacaos;

	public GerNumeracao() {
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

	public String getSerie() {
		return this.serie;
	}

	public void setSerie(String serie) {
		this.serie = serie;
	}

	public Integer getUltimoNr() {
		return this.ultimoNr;
	}

	public void setUltimoNr(Integer ultimoNr) {
		this.ultimoNr = ultimoNr;
	}

	public List<FinDocTipo> getFinDocTipos() {
		return this.finDocTipos;
	}

	public void setFinDocTipos(List<FinDocTipo> finDocTipos) {
		this.finDocTipos = finDocTipos;
	}

	public FinDocTipo addFinDocTipo(FinDocTipo finDocTipo) {
		getFinDocTipos().add(finDocTipo);
		finDocTipo.setGerNumeracao(this);

		return finDocTipo;
	}

	public FinDocTipo removeFinDocTipo(FinDocTipo finDocTipo) {
		getFinDocTipos().remove(finDocTipo);
		finDocTipo.setGerNumeracao(null);

		return finDocTipo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<MovOperacao> getMovOperacaos() {
		return this.movOperacaos;
	}

	public void setMovOperacaos(List<MovOperacao> movOperacaos) {
		this.movOperacaos = movOperacaos;
	}

	public MovOperacao addMovOperacao(MovOperacao movOperacao) {
		getMovOperacaos().add(movOperacao);
		movOperacao.setGerNumeracao(this);

		return movOperacao;
	}

	public MovOperacao removeMovOperacao(MovOperacao movOperacao) {
		getMovOperacaos().remove(movOperacao);
		movOperacao.setGerNumeracao(null);

		return movOperacao;
	}

}