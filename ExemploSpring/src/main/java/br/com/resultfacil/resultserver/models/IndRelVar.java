package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ind_rel_var")
@NamedQuery(name="IndRelVar.findAll", query="SELECT i FROM IndRelVar i")
public class IndRelVar implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(precision=18, scale=2)
	private BigDecimal largura;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="ordem_padrao", nullable=false)
	private Integer ordemPadrao;

	@Column(name="var_agrupavel", nullable=false, length=1)
	private String varAgrupavel;

	@Column(name="var_nome_descritivo", nullable=false, length=50)
	private String varNomeDescritivo;

	@Column(name="var_nome_tecnico", nullable=false, length=50)
	private String varNomeTecnico;

	@Column(name="var_nome_tecnico_prefixo", length=50)
	private String varNomeTecnicoPrefixo;

	@Column(length=1)
	private String visivel;

	//bi-directional many-to-one association to IndRel
	@ManyToOne
	@JoinColumn(name="ind_rel_id", nullable=false)
	private IndRel indRel;

	public IndRelVar() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public BigDecimal getLargura() {
		return this.largura;
	}

	public void setLargura(BigDecimal largura) {
		this.largura = largura;
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

	public Integer getOrdemPadrao() {
		return this.ordemPadrao;
	}

	public void setOrdemPadrao(Integer ordemPadrao) {
		this.ordemPadrao = ordemPadrao;
	}

	public String getVarAgrupavel() {
		return this.varAgrupavel;
	}

	public void setVarAgrupavel(String varAgrupavel) {
		this.varAgrupavel = varAgrupavel;
	}

	public String getVarNomeDescritivo() {
		return this.varNomeDescritivo;
	}

	public void setVarNomeDescritivo(String varNomeDescritivo) {
		this.varNomeDescritivo = varNomeDescritivo;
	}

	public String getVarNomeTecnico() {
		return this.varNomeTecnico;
	}

	public void setVarNomeTecnico(String varNomeTecnico) {
		this.varNomeTecnico = varNomeTecnico;
	}

	public String getVarNomeTecnicoPrefixo() {
		return this.varNomeTecnicoPrefixo;
	}

	public void setVarNomeTecnicoPrefixo(String varNomeTecnicoPrefixo) {
		this.varNomeTecnicoPrefixo = varNomeTecnicoPrefixo;
	}

	public String getVisivel() {
		return this.visivel;
	}

	public void setVisivel(String visivel) {
		this.visivel = visivel;
	}

	public IndRel getIndRel() {
		return this.indRel;
	}

	public void setIndRel(IndRel indRel) {
		this.indRel = indRel;
	}

}