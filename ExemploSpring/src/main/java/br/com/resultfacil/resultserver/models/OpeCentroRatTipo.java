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
@Table(name="ope_centro_rat_tipo")
@NamedQuery(name="OpeCentroRatTipo.findAll", query="SELECT o FROM OpeCentroRatTipo o")
public class OpeCentroRatTipo implements Serializable {
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

	@Column(length=250)
	private String observacao;

	@Column(name="sigla_centro_rat_tipo", length=50)
	private String siglaCentroRatTipo;

	@Column(name="tipo_apur", nullable=false, length=1)
	private String tipoApur;

	@Column(name="tipo_ps", nullable=false, length=1)
	private String tipoPs;

	//bi-directional many-to-one association to FinPagrec
	@OneToMany(mappedBy="opeCentroRatTipo")
	private List<FinPagrec> finPagrecs;

	//bi-directional many-to-one association to OpeCentro2
	@OneToMany(mappedBy="opeCentroRatTipo")
	private List<OpeCentro2> opeCentro2s;

	//bi-directional many-to-one association to OpeCentroRatPeriodo
	@OneToMany(mappedBy="opeCentroRatTipo")
	private List<OpeCentroRatPeriodo> opeCentroRatPeriodos;

	//bi-directional many-to-one association to OpeCentroVersao
	@ManyToOne
	@JoinColumn(name="ope_centro_versao_id")
	private OpeCentroVersao opeCentroVersao;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentroRatTipo() {
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

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public String getSiglaCentroRatTipo() {
		return this.siglaCentroRatTipo;
	}

	public void setSiglaCentroRatTipo(String siglaCentroRatTipo) {
		this.siglaCentroRatTipo = siglaCentroRatTipo;
	}

	public String getTipoApur() {
		return this.tipoApur;
	}

	public void setTipoApur(String tipoApur) {
		this.tipoApur = tipoApur;
	}

	public String getTipoPs() {
		return this.tipoPs;
	}

	public void setTipoPs(String tipoPs) {
		this.tipoPs = tipoPs;
	}

	public List<FinPagrec> getFinPagrecs() {
		return this.finPagrecs;
	}

	public void setFinPagrecs(List<FinPagrec> finPagrecs) {
		this.finPagrecs = finPagrecs;
	}

	public FinPagrec addFinPagrec(FinPagrec finPagrec) {
		getFinPagrecs().add(finPagrec);
		finPagrec.setOpeCentroRatTipo(this);

		return finPagrec;
	}

	public FinPagrec removeFinPagrec(FinPagrec finPagrec) {
		getFinPagrecs().remove(finPagrec);
		finPagrec.setOpeCentroRatTipo(null);

		return finPagrec;
	}

	public List<OpeCentro2> getOpeCentro2s() {
		return this.opeCentro2s;
	}

	public void setOpeCentro2s(List<OpeCentro2> opeCentro2s) {
		this.opeCentro2s = opeCentro2s;
	}

	public OpeCentro2 addOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().add(opeCentro2);
		opeCentro2.setOpeCentroRatTipo(this);

		return opeCentro2;
	}

	public OpeCentro2 removeOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().remove(opeCentro2);
		opeCentro2.setOpeCentroRatTipo(null);

		return opeCentro2;
	}

	public List<OpeCentroRatPeriodo> getOpeCentroRatPeriodos() {
		return this.opeCentroRatPeriodos;
	}

	public void setOpeCentroRatPeriodos(List<OpeCentroRatPeriodo> opeCentroRatPeriodos) {
		this.opeCentroRatPeriodos = opeCentroRatPeriodos;
	}

	public OpeCentroRatPeriodo addOpeCentroRatPeriodo(OpeCentroRatPeriodo opeCentroRatPeriodo) {
		getOpeCentroRatPeriodos().add(opeCentroRatPeriodo);
		opeCentroRatPeriodo.setOpeCentroRatTipo(this);

		return opeCentroRatPeriodo;
	}

	public OpeCentroRatPeriodo removeOpeCentroRatPeriodo(OpeCentroRatPeriodo opeCentroRatPeriodo) {
		getOpeCentroRatPeriodos().remove(opeCentroRatPeriodo);
		opeCentroRatPeriodo.setOpeCentroRatTipo(null);

		return opeCentroRatPeriodo;
	}

	public OpeCentroVersao getOpeCentroVersao() {
		return this.opeCentroVersao;
	}

	public void setOpeCentroVersao(OpeCentroVersao opeCentroVersao) {
		this.opeCentroVersao = opeCentroVersao;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}