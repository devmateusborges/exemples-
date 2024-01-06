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
@Table(name="mov_tipo")
@NamedQuery(name="MovTipo.findAll", query="SELECT m FROM MovTipo m")
public class MovTipo implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(length=2147483647)
	private String configuracao;

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

	@Column(name="sigla_mov_tipo", nullable=false, length=50)
	private String siglaMovTipo;

	@Column(name="tipo_mov", nullable=false, length=10)
	private String tipoMov;

	//bi-directional many-to-one association to MovOperacao
	@OneToMany(mappedBy="movTipo")
	private List<MovOperacao> movOperacaos;

	public MovTipo() {
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

	public String getConfiguracao() {
		return this.configuracao;
	}

	public void setConfiguracao(String configuracao) {
		this.configuracao = configuracao;
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

	public String getSiglaMovTipo() {
		return this.siglaMovTipo;
	}

	public void setSiglaMovTipo(String siglaMovTipo) {
		this.siglaMovTipo = siglaMovTipo;
	}

	public String getTipoMov() {
		return this.tipoMov;
	}

	public void setTipoMov(String tipoMov) {
		this.tipoMov = tipoMov;
	}

	public List<MovOperacao> getMovOperacaos() {
		return this.movOperacaos;
	}

	public void setMovOperacaos(List<MovOperacao> movOperacaos) {
		this.movOperacaos = movOperacaos;
	}

	public MovOperacao addMovOperacao(MovOperacao movOperacao) {
		getMovOperacaos().add(movOperacao);
		movOperacao.setMovTipo(this);

		return movOperacao;
	}

	public MovOperacao removeMovOperacao(MovOperacao movOperacao) {
		getMovOperacaos().remove(movOperacao);
		movOperacao.setMovTipo(null);

		return movOperacao;
	}

}