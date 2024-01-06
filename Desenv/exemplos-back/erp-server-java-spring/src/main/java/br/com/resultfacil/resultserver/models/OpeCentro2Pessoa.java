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
@Table(name="ope_centro2_pessoa")
@NamedQuery(name="OpeCentro2Pessoa.findAll", query="SELECT o FROM OpeCentro2Pessoa o")
public class OpeCentro2Pessoa implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="pto_idenf", length=50)
	private String ptoIdenf;

	@Column(name="pto_idenf_tipo", length=1)
	private String ptoIdenfTipo;

	//bi-directional many-to-one association to BorDispositivo
	@OneToMany(mappedBy="opeCentro2Pessoa")
	private List<BorDispositivo> borDispositivos;

	//bi-directional many-to-one association to OpeCentro2Ord
	@OneToMany(mappedBy="opeCentro2Pessoa")
	private List<OpeCentro2Ord> opeCentro2Ords;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id", nullable=false)
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeFrenteTrabalho
	@ManyToOne
	@JoinColumn(name="ope_frente_trabalho_id")
	private OpeFrenteTrabalho opeFrenteTrabalho;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentro2Pessoa() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
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

	public String getPtoIdenf() {
		return this.ptoIdenf;
	}

	public void setPtoIdenf(String ptoIdenf) {
		this.ptoIdenf = ptoIdenf;
	}

	public String getPtoIdenfTipo() {
		return this.ptoIdenfTipo;
	}

	public void setPtoIdenfTipo(String ptoIdenfTipo) {
		this.ptoIdenfTipo = ptoIdenfTipo;
	}

	public List<BorDispositivo> getBorDispositivos() {
		return this.borDispositivos;
	}

	public void setBorDispositivos(List<BorDispositivo> borDispositivos) {
		this.borDispositivos = borDispositivos;
	}

	public BorDispositivo addBorDispositivo(BorDispositivo borDispositivo) {
		getBorDispositivos().add(borDispositivo);
		borDispositivo.setOpeCentro2Pessoa(this);

		return borDispositivo;
	}

	public BorDispositivo removeBorDispositivo(BorDispositivo borDispositivo) {
		getBorDispositivos().remove(borDispositivo);
		borDispositivo.setOpeCentro2Pessoa(null);

		return borDispositivo;
	}

	public List<OpeCentro2Ord> getOpeCentro2Ords() {
		return this.opeCentro2Ords;
	}

	public void setOpeCentro2Ords(List<OpeCentro2Ord> opeCentro2Ords) {
		this.opeCentro2Ords = opeCentro2Ords;
	}

	public OpeCentro2Ord addOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().add(opeCentro2Ord);
		opeCentro2Ord.setOpeCentro2Pessoa(this);

		return opeCentro2Ord;
	}

	public OpeCentro2Ord removeOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().remove(opeCentro2Ord);
		opeCentro2Ord.setOpeCentro2Pessoa(null);

		return opeCentro2Ord;
	}

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
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

}