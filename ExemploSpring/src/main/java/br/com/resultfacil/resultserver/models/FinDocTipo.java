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
@Table(name="fin_doc_tipo")
@NamedQuery(name="FinDocTipo.findAll", query="SELECT f FROM FinDocTipo f")
public class FinDocTipo implements Serializable {
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

	@Column(name="nr_doc", length=50)
	private String nrDoc;

	//bi-directional many-to-one association to GerNumeracao
	@ManyToOne
	@JoinColumn(name="ger_numeracao_id")
	private GerNumeracao gerNumeracao;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FinPagrec
	@OneToMany(mappedBy="finDocTipo")
	private List<FinPagrec> finPagrecs;

	//bi-directional many-to-one association to FinPagrecBaixa
	@OneToMany(mappedBy="finDocTipo")
	private List<FinPagrecBaixa> finPagrecBaixas;

	//bi-directional many-to-one association to FinPagrecParc
	@OneToMany(mappedBy="finDocTipo")
	private List<FinPagrecParc> finPagrecParcs;

	public FinDocTipo() {
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

	public String getNrDoc() {
		return this.nrDoc;
	}

	public void setNrDoc(String nrDoc) {
		this.nrDoc = nrDoc;
	}

	public GerNumeracao getGerNumeracao() {
		return this.gerNumeracao;
	}

	public void setGerNumeracao(GerNumeracao gerNumeracao) {
		this.gerNumeracao = gerNumeracao;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<FinPagrec> getFinPagrecs() {
		return this.finPagrecs;
	}

	public void setFinPagrecs(List<FinPagrec> finPagrecs) {
		this.finPagrecs = finPagrecs;
	}

	public FinPagrec addFinPagrec(FinPagrec finPagrec) {
		getFinPagrecs().add(finPagrec);
		finPagrec.setFinDocTipo(this);

		return finPagrec;
	}

	public FinPagrec removeFinPagrec(FinPagrec finPagrec) {
		getFinPagrecs().remove(finPagrec);
		finPagrec.setFinDocTipo(null);

		return finPagrec;
	}

	public List<FinPagrecBaixa> getFinPagrecBaixas() {
		return this.finPagrecBaixas;
	}

	public void setFinPagrecBaixas(List<FinPagrecBaixa> finPagrecBaixas) {
		this.finPagrecBaixas = finPagrecBaixas;
	}

	public FinPagrecBaixa addFinPagrecBaixa(FinPagrecBaixa finPagrecBaixa) {
		getFinPagrecBaixas().add(finPagrecBaixa);
		finPagrecBaixa.setFinDocTipo(this);

		return finPagrecBaixa;
	}

	public FinPagrecBaixa removeFinPagrecBaixa(FinPagrecBaixa finPagrecBaixa) {
		getFinPagrecBaixas().remove(finPagrecBaixa);
		finPagrecBaixa.setFinDocTipo(null);

		return finPagrecBaixa;
	}

	public List<FinPagrecParc> getFinPagrecParcs() {
		return this.finPagrecParcs;
	}

	public void setFinPagrecParcs(List<FinPagrecParc> finPagrecParcs) {
		this.finPagrecParcs = finPagrecParcs;
	}

	public FinPagrecParc addFinPagrecParc(FinPagrecParc finPagrecParc) {
		getFinPagrecParcs().add(finPagrecParc);
		finPagrecParc.setFinDocTipo(this);

		return finPagrecParc;
	}

	public FinPagrecParc removeFinPagrecParc(FinPagrecParc finPagrecParc) {
		getFinPagrecParcs().remove(finPagrecParc);
		finPagrecParc.setFinDocTipo(null);

		return finPagrecParc;
	}

}