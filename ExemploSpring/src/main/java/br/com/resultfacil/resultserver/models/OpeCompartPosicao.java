package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_compart_posicao")
@NamedQuery(name="OpeCompartPosicao.findAll", query="SELECT o FROM OpeCompartPosicao o")
public class OpeCompartPosicao implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(name="banda_montagem", nullable=false, length=1)
	private String bandaMontagem;

	@Column(name="lado_montagem", nullable=false, length=1)
	private String ladoMontagem;

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

	@Column(name="numero_eixo", nullable=false)
	private Integer numeroEixo;

	@Column(nullable=false, length=1)
	private String posicao;

	@Column(name="sigla_compart_posicao", nullable=false, length=50)
	private String siglaCompartPosicao;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCompartPosicao() {
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

	public String getBandaMontagem() {
		return this.bandaMontagem;
	}

	public void setBandaMontagem(String bandaMontagem) {
		this.bandaMontagem = bandaMontagem;
	}

	public String getLadoMontagem() {
		return this.ladoMontagem;
	}

	public void setLadoMontagem(String ladoMontagem) {
		this.ladoMontagem = ladoMontagem;
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

	public Integer getNumeroEixo() {
		return this.numeroEixo;
	}

	public void setNumeroEixo(Integer numeroEixo) {
		this.numeroEixo = numeroEixo;
	}

	public String getPosicao() {
		return this.posicao;
	}

	public void setPosicao(String posicao) {
		this.posicao = posicao;
	}

	public String getSiglaCompartPosicao() {
		return this.siglaCompartPosicao;
	}

	public void setSiglaCompartPosicao(String siglaCompartPosicao) {
		this.siglaCompartPosicao = siglaCompartPosicao;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}