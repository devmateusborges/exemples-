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
@Table(name="ope_centro2_ord")
@NamedQuery(name="OpeCentro2Ord.findAll", query="SELECT o FROM OpeCentro2Ord o")
public class OpeCentro2Ord implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_fin_exec", nullable=false)
	private Date dataFinExec;

	@Temporal(TemporalType.DATE)
	@Column(name="data_fin_exec_prev")
	private Date dataFinExecPrev;

	@Temporal(TemporalType.DATE)
	@Column(name="data_ini_exec", nullable=false)
	private Date dataIniExec;

	@Temporal(TemporalType.DATE)
	@Column(name="data_ini_exec_prev")
	private Date dataIniExecPrev;

	@Temporal(TemporalType.DATE)
	@Column(name="data_status", nullable=false)
	private Date dataStatus;

	@Temporal(TemporalType.DATE)
	@Column(name="data_valid")
	private Date dataValid;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="numero_ord", length=50)
	private String numeroOrd;

	@Column(name="observacao_externa", length=250)
	private String observacaoExterna;

	@Column(name="observacao_interna", length=250)
	private String observacaoInterna;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_exec")
	private GerPessoaEndereco gerPessoaEndereco;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id", nullable=false)
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeCentro2OrdStatus
	@ManyToOne
	@JoinColumn(name="ope_centro2_ord_status_id", nullable=false)
	private OpeCentro2OrdStatus opeCentro2OrdStatus;

	//bi-directional many-to-one association to OpeCentro2OrdTipo
	@ManyToOne
	@JoinColumn(name="ope_centro2_ord_tipo_id", nullable=false)
	private OpeCentro2OrdTipo opeCentro2OrdTipo;

	//bi-directional many-to-one association to OpeCentro2Pessoa
	@ManyToOne
	@JoinColumn(name="ope_centro2_pessoa_id_solic")
	private OpeCentro2Pessoa opeCentro2Pessoa;

	//bi-directional many-to-one association to OpeCentroVersao
	@ManyToOne
	@JoinColumn(name="ope_centro_versao_id")
	private OpeCentroVersao opeCentroVersao;

	//bi-directional many-to-one association to OpeFrenteTrabalho
	@ManyToOne
	@JoinColumn(name="ope_frente_trabalho_id")
	private OpeFrenteTrabalho opeFrenteTrabalho;

	//bi-directional many-to-one association to OpePeriodo
	@ManyToOne
	@JoinColumn(name="ope_periodo_id", nullable=false)
	private OpePeriodo opePeriodo;

	//bi-directional many-to-one association to SysProcessLog
	@ManyToOne
	@JoinColumn(name="process_id")
	private SysProcessLog sysProcessLog;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCentro2OrdAtiv
	@OneToMany(mappedBy="opeCentro2Ord")
	private List<OpeCentro2OrdAtiv> opeCentro2OrdAtivs;

	//bi-directional many-to-one association to OpeCentro2OrdDest
	@OneToMany(mappedBy="opeCentro2Ord")
	private List<OpeCentro2OrdDest> opeCentro2OrdDests;

	//bi-directional many-to-one association to SysDocument
	@OneToMany(mappedBy="opeCentro2Ord")
	private List<SysDocument> sysDocuments;

	public OpeCentro2Ord() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataFinExec() {
		return this.dataFinExec;
	}

	public void setDataFinExec(Date dataFinExec) {
		this.dataFinExec = dataFinExec;
	}

	public Date getDataFinExecPrev() {
		return this.dataFinExecPrev;
	}

	public void setDataFinExecPrev(Date dataFinExecPrev) {
		this.dataFinExecPrev = dataFinExecPrev;
	}

	public Date getDataIniExec() {
		return this.dataIniExec;
	}

	public void setDataIniExec(Date dataIniExec) {
		this.dataIniExec = dataIniExec;
	}

	public Date getDataIniExecPrev() {
		return this.dataIniExecPrev;
	}

	public void setDataIniExecPrev(Date dataIniExecPrev) {
		this.dataIniExecPrev = dataIniExecPrev;
	}

	public Date getDataStatus() {
		return this.dataStatus;
	}

	public void setDataStatus(Date dataStatus) {
		this.dataStatus = dataStatus;
	}

	public Date getDataValid() {
		return this.dataValid;
	}

	public void setDataValid(Date dataValid) {
		this.dataValid = dataValid;
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

	public String getNumeroOrd() {
		return this.numeroOrd;
	}

	public void setNumeroOrd(String numeroOrd) {
		this.numeroOrd = numeroOrd;
	}

	public String getObservacaoExterna() {
		return this.observacaoExterna;
	}

	public void setObservacaoExterna(String observacaoExterna) {
		this.observacaoExterna = observacaoExterna;
	}

	public String getObservacaoInterna() {
		return this.observacaoInterna;
	}

	public void setObservacaoInterna(String observacaoInterna) {
		this.observacaoInterna = observacaoInterna;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public GerPessoaEndereco getGerPessoaEndereco() {
		return this.gerPessoaEndereco;
	}

	public void setGerPessoaEndereco(GerPessoaEndereco gerPessoaEndereco) {
		this.gerPessoaEndereco = gerPessoaEndereco;
	}

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
	}

	public OpeCentro2OrdStatus getOpeCentro2OrdStatus() {
		return this.opeCentro2OrdStatus;
	}

	public void setOpeCentro2OrdStatus(OpeCentro2OrdStatus opeCentro2OrdStatus) {
		this.opeCentro2OrdStatus = opeCentro2OrdStatus;
	}

	public OpeCentro2OrdTipo getOpeCentro2OrdTipo() {
		return this.opeCentro2OrdTipo;
	}

	public void setOpeCentro2OrdTipo(OpeCentro2OrdTipo opeCentro2OrdTipo) {
		this.opeCentro2OrdTipo = opeCentro2OrdTipo;
	}

	public OpeCentro2Pessoa getOpeCentro2Pessoa() {
		return this.opeCentro2Pessoa;
	}

	public void setOpeCentro2Pessoa(OpeCentro2Pessoa opeCentro2Pessoa) {
		this.opeCentro2Pessoa = opeCentro2Pessoa;
	}

	public OpeCentroVersao getOpeCentroVersao() {
		return this.opeCentroVersao;
	}

	public void setOpeCentroVersao(OpeCentroVersao opeCentroVersao) {
		this.opeCentroVersao = opeCentroVersao;
	}

	public OpeFrenteTrabalho getOpeFrenteTrabalho() {
		return this.opeFrenteTrabalho;
	}

	public void setOpeFrenteTrabalho(OpeFrenteTrabalho opeFrenteTrabalho) {
		this.opeFrenteTrabalho = opeFrenteTrabalho;
	}

	public OpePeriodo getOpePeriodo() {
		return this.opePeriodo;
	}

	public void setOpePeriodo(OpePeriodo opePeriodo) {
		this.opePeriodo = opePeriodo;
	}

	public SysProcessLog getSysProcessLog() {
		return this.sysProcessLog;
	}

	public void setSysProcessLog(SysProcessLog sysProcessLog) {
		this.sysProcessLog = sysProcessLog;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCentro2OrdAtiv> getOpeCentro2OrdAtivs() {
		return this.opeCentro2OrdAtivs;
	}

	public void setOpeCentro2OrdAtivs(List<OpeCentro2OrdAtiv> opeCentro2OrdAtivs) {
		this.opeCentro2OrdAtivs = opeCentro2OrdAtivs;
	}

	public OpeCentro2OrdAtiv addOpeCentro2OrdAtiv(OpeCentro2OrdAtiv opeCentro2OrdAtiv) {
		getOpeCentro2OrdAtivs().add(opeCentro2OrdAtiv);
		opeCentro2OrdAtiv.setOpeCentro2Ord(this);

		return opeCentro2OrdAtiv;
	}

	public OpeCentro2OrdAtiv removeOpeCentro2OrdAtiv(OpeCentro2OrdAtiv opeCentro2OrdAtiv) {
		getOpeCentro2OrdAtivs().remove(opeCentro2OrdAtiv);
		opeCentro2OrdAtiv.setOpeCentro2Ord(null);

		return opeCentro2OrdAtiv;
	}

	public List<OpeCentro2OrdDest> getOpeCentro2OrdDests() {
		return this.opeCentro2OrdDests;
	}

	public void setOpeCentro2OrdDests(List<OpeCentro2OrdDest> opeCentro2OrdDests) {
		this.opeCentro2OrdDests = opeCentro2OrdDests;
	}

	public OpeCentro2OrdDest addOpeCentro2OrdDest(OpeCentro2OrdDest opeCentro2OrdDest) {
		getOpeCentro2OrdDests().add(opeCentro2OrdDest);
		opeCentro2OrdDest.setOpeCentro2Ord(this);

		return opeCentro2OrdDest;
	}

	public OpeCentro2OrdDest removeOpeCentro2OrdDest(OpeCentro2OrdDest opeCentro2OrdDest) {
		getOpeCentro2OrdDests().remove(opeCentro2OrdDest);
		opeCentro2OrdDest.setOpeCentro2Ord(null);

		return opeCentro2OrdDest;
	}

	public List<SysDocument> getSysDocuments() {
		return this.sysDocuments;
	}

	public void setSysDocuments(List<SysDocument> sysDocuments) {
		this.sysDocuments = sysDocuments;
	}

	public SysDocument addSysDocument(SysDocument sysDocument) {
		getSysDocuments().add(sysDocument);
		sysDocument.setOpeCentro2Ord(this);

		return sysDocument;
	}

	public SysDocument removeSysDocument(SysDocument sysDocument) {
		getSysDocuments().remove(sysDocument);
		sysDocument.setOpeCentro2Ord(null);

		return sysDocument;
	}

}