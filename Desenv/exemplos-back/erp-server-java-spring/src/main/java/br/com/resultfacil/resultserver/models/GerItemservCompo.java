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
@Table(name="ger_itemserv_compos")
@NamedQuery(name="GerItemservCompo.findAll", query="SELECT g FROM GerItemservCompo g")
public class GerItemservCompo implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(name="fator_mult", nullable=false, precision=18, scale=6)
	private BigDecimal fatorMult;

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
	private String observacao;

	@Column(nullable=false, length=50)
	private String ordem;

	@Column(name="qnt_altura", precision=18, scale=6)
	private BigDecimal qntAltura;

	@Column(name="qnt_compos", nullable=false, precision=18, scale=6)
	private BigDecimal qntCompos;

	@Column(name="qnt_comprimento", precision=18, scale=6)
	private BigDecimal qntComprimento;

	@Column(name="qnt_largura", precision=18, scale=6)
	private BigDecimal qntLargura;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id_de", nullable=false)
	private GerItemserv gerItemserv1;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id_para", nullable=false)
	private GerItemserv gerItemserv2;

	//bi-directional many-to-one association to GerItemservComposTipo
	@ManyToOne
	@JoinColumn(name="ger_itemserv_compos_tipo_id", nullable=false)
	private GerItemservComposTipo gerItemservComposTipo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public GerItemservCompo() {
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

	public BigDecimal getFatorMult() {
		return this.fatorMult;
	}

	public void setFatorMult(BigDecimal fatorMult) {
		this.fatorMult = fatorMult;
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

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public String getOrdem() {
		return this.ordem;
	}

	public void setOrdem(String ordem) {
		this.ordem = ordem;
	}

	public BigDecimal getQntAltura() {
		return this.qntAltura;
	}

	public void setQntAltura(BigDecimal qntAltura) {
		this.qntAltura = qntAltura;
	}

	public BigDecimal getQntCompos() {
		return this.qntCompos;
	}

	public void setQntCompos(BigDecimal qntCompos) {
		this.qntCompos = qntCompos;
	}

	public BigDecimal getQntComprimento() {
		return this.qntComprimento;
	}

	public void setQntComprimento(BigDecimal qntComprimento) {
		this.qntComprimento = qntComprimento;
	}

	public BigDecimal getQntLargura() {
		return this.qntLargura;
	}

	public void setQntLargura(BigDecimal qntLargura) {
		this.qntLargura = qntLargura;
	}

	public GerItemserv getGerItemserv1() {
		return this.gerItemserv1;
	}

	public void setGerItemserv1(GerItemserv gerItemserv1) {
		this.gerItemserv1 = gerItemserv1;
	}

	public GerItemserv getGerItemserv2() {
		return this.gerItemserv2;
	}

	public void setGerItemserv2(GerItemserv gerItemserv2) {
		this.gerItemserv2 = gerItemserv2;
	}

	public GerItemservComposTipo getGerItemservComposTipo() {
		return this.gerItemservComposTipo;
	}

	public void setGerItemservComposTipo(GerItemservComposTipo gerItemservComposTipo) {
		this.gerItemservComposTipo = gerItemservComposTipo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}