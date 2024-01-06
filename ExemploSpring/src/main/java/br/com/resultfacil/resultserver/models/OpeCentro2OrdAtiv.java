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
@Table(name="ope_centro2_ord_ativ")
@NamedQuery(name="OpeCentro2OrdAtiv.findAll", query="SELECT o FROM OpeCentro2OrdAtiv o")
public class OpeCentro2OrdAtiv implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

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

	@Column(name="observacao_externa", length=250)
	private String observacaoExterna;

	@Column(name="observacao_interna", length=250)
	private String observacaoInterna;

	@Column(name="ordem_exec", nullable=false, length=3)
	private String ordemExec;

	@Column(name="tipo_executor", nullable=false, length=1)
	private String tipoExecutor;

	//bi-directional many-to-one association to OpeAtividade
	@ManyToOne
	@JoinColumn(name="ope_atividade_id", nullable=false)
	private OpeAtividade opeAtividade;

	//bi-directional many-to-one association to OpeCentro2Ord
	@ManyToOne
	@JoinColumn(name="ope_centro2_ord_id", nullable=false)
	private OpeCentro2Ord opeCentro2Ord;

	//bi-directional many-to-one association to OpeFrenteTrabalho
	@ManyToOne
	@JoinColumn(name="ope_frente_trabalho_id")
	private OpeFrenteTrabalho opeFrenteTrabalho;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCentro2OrdItemserv
	@OneToMany(mappedBy="opeCentro2OrdAtiv")
	private List<OpeCentro2OrdItemserv> opeCentro2OrdItemservs;

	//bi-directional many-to-one association to OpeCentro2OrdRec
	@OneToMany(mappedBy="opeCentro2OrdAtiv")
	private List<OpeCentro2OrdRec> opeCentro2OrdRecs;

	public OpeCentro2OrdAtiv() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
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

	public String getOrdemExec() {
		return this.ordemExec;
	}

	public void setOrdemExec(String ordemExec) {
		this.ordemExec = ordemExec;
	}

	public String getTipoExecutor() {
		return this.tipoExecutor;
	}

	public void setTipoExecutor(String tipoExecutor) {
		this.tipoExecutor = tipoExecutor;
	}

	public OpeAtividade getOpeAtividade() {
		return this.opeAtividade;
	}

	public void setOpeAtividade(OpeAtividade opeAtividade) {
		this.opeAtividade = opeAtividade;
	}

	public OpeCentro2Ord getOpeCentro2Ord() {
		return this.opeCentro2Ord;
	}

	public void setOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		this.opeCentro2Ord = opeCentro2Ord;
	}

	public OpeFrenteTrabalho getOpeFrenteTrabalho() {
		return this.opeFrenteTrabalho;
	}

	public void setOpeFrenteTrabalho(OpeFrenteTrabalho opeFrenteTrabalho) {
		this.opeFrenteTrabalho = opeFrenteTrabalho;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCentro2OrdItemserv> getOpeCentro2OrdItemservs() {
		return this.opeCentro2OrdItemservs;
	}

	public void setOpeCentro2OrdItemservs(List<OpeCentro2OrdItemserv> opeCentro2OrdItemservs) {
		this.opeCentro2OrdItemservs = opeCentro2OrdItemservs;
	}

	public OpeCentro2OrdItemserv addOpeCentro2OrdItemserv(OpeCentro2OrdItemserv opeCentro2OrdItemserv) {
		getOpeCentro2OrdItemservs().add(opeCentro2OrdItemserv);
		opeCentro2OrdItemserv.setOpeCentro2OrdAtiv(this);

		return opeCentro2OrdItemserv;
	}

	public OpeCentro2OrdItemserv removeOpeCentro2OrdItemserv(OpeCentro2OrdItemserv opeCentro2OrdItemserv) {
		getOpeCentro2OrdItemservs().remove(opeCentro2OrdItemserv);
		opeCentro2OrdItemserv.setOpeCentro2OrdAtiv(null);

		return opeCentro2OrdItemserv;
	}

	public List<OpeCentro2OrdRec> getOpeCentro2OrdRecs() {
		return this.opeCentro2OrdRecs;
	}

	public void setOpeCentro2OrdRecs(List<OpeCentro2OrdRec> opeCentro2OrdRecs) {
		this.opeCentro2OrdRecs = opeCentro2OrdRecs;
	}

	public OpeCentro2OrdRec addOpeCentro2OrdRec(OpeCentro2OrdRec opeCentro2OrdRec) {
		getOpeCentro2OrdRecs().add(opeCentro2OrdRec);
		opeCentro2OrdRec.setOpeCentro2OrdAtiv(this);

		return opeCentro2OrdRec;
	}

	public OpeCentro2OrdRec removeOpeCentro2OrdRec(OpeCentro2OrdRec opeCentro2OrdRec) {
		getOpeCentro2OrdRecs().remove(opeCentro2OrdRec);
		opeCentro2OrdRec.setOpeCentro2OrdAtiv(null);

		return opeCentro2OrdRec;
	}

}