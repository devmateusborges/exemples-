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
@Table(name="ctb_lanc")
@NamedQuery(name="CtbLanc.findAll", query="SELECT c FROM CtbLanc c")
public class CtbLanc implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_lanc", nullable=false)
	private Date dataLanc;

	@Column(nullable=false, length=250)
	private String historico;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", nullable=false, length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="numero_lanc", nullable=false, length=50)
	private String numeroLanc;

	@Column(nullable=false, length=2)
	private String status;

	@Column(name="status_observacao", length=250)
	private String statusObservacao;

	//bi-directional many-to-one association to CtbHistorico
	@ManyToOne
	@JoinColumn(name="ctb_historico_id", nullable=false)
	private CtbHistorico ctbHistorico;

	//bi-directional many-to-one association to CtbLote
	@ManyToOne
	@JoinColumn(name="ctb_lote_id", nullable=false)
	private CtbLote ctbLote;

	//bi-directional many-to-one association to CtbVersao
	@ManyToOne
	@JoinColumn(name="ctb_versao_id")
	private CtbVersao ctbVersao;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to CtbLancDet
	@OneToMany(mappedBy="ctbLanc")
	private List<CtbLancDet> ctbLancDets;

	public CtbLanc() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataLanc() {
		return this.dataLanc;
	}

	public void setDataLanc(Date dataLanc) {
		this.dataLanc = dataLanc;
	}

	public String getHistorico() {
		return this.historico;
	}

	public void setHistorico(String historico) {
		this.historico = historico;
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

	public String getNumeroLanc() {
		return this.numeroLanc;
	}

	public void setNumeroLanc(String numeroLanc) {
		this.numeroLanc = numeroLanc;
	}

	public String getStatus() {
		return this.status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public String getStatusObservacao() {
		return this.statusObservacao;
	}

	public void setStatusObservacao(String statusObservacao) {
		this.statusObservacao = statusObservacao;
	}

	public CtbHistorico getCtbHistorico() {
		return this.ctbHistorico;
	}

	public void setCtbHistorico(CtbHistorico ctbHistorico) {
		this.ctbHistorico = ctbHistorico;
	}

	public CtbLote getCtbLote() {
		return this.ctbLote;
	}

	public void setCtbLote(CtbLote ctbLote) {
		this.ctbLote = ctbLote;
	}

	public CtbVersao getCtbVersao() {
		return this.ctbVersao;
	}

	public void setCtbVersao(CtbVersao ctbVersao) {
		this.ctbVersao = ctbVersao;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<CtbLancDet> getCtbLancDets() {
		return this.ctbLancDets;
	}

	public void setCtbLancDets(List<CtbLancDet> ctbLancDets) {
		this.ctbLancDets = ctbLancDets;
	}

	public CtbLancDet addCtbLancDet(CtbLancDet ctbLancDet) {
		getCtbLancDets().add(ctbLancDet);
		ctbLancDet.setCtbLanc(this);

		return ctbLancDet;
	}

	public CtbLancDet removeCtbLancDet(CtbLancDet ctbLancDet) {
		getCtbLancDets().remove(ctbLancDet);
		ctbLancDet.setCtbLanc(null);

		return ctbLancDet;
	}

}