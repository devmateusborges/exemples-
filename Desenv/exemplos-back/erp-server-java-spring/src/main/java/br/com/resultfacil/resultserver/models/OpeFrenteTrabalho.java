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
@Table(name="ope_frente_trabalho")
@NamedQuery(name="OpeFrenteTrabalho.findAll", query="SELECT o FROM OpeFrenteTrabalho o")
public class OpeFrenteTrabalho implements Serializable {
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

	@Column(name="sigla_frente_trabalho", length=50)
	private String siglaFrenteTrabalho;

	//bi-directional many-to-one association to OpeCentro2Equip
	@OneToMany(mappedBy="opeFrenteTrabalho")
	private List<OpeCentro2Equip> opeCentro2Equips;

	//bi-directional many-to-one association to OpeCentro2Ord
	@OneToMany(mappedBy="opeFrenteTrabalho")
	private List<OpeCentro2Ord> opeCentro2Ords;

	//bi-directional many-to-one association to OpeCentro2OrdAtiv
	@OneToMany(mappedBy="opeFrenteTrabalho")
	private List<OpeCentro2OrdAtiv> opeCentro2OrdAtivs;

	//bi-directional many-to-one association to OpeCentro2ParamPer
	@OneToMany(mappedBy="opeFrenteTrabalho")
	private List<OpeCentro2ParamPer> opeCentro2ParamPers;

	//bi-directional many-to-one association to OpeCentro2Pessoa
	@OneToMany(mappedBy="opeFrenteTrabalho")
	private List<OpeCentro2Pessoa> opeCentro2Pessoas;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeFrenteTrabalho() {
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

	public String getSiglaFrenteTrabalho() {
		return this.siglaFrenteTrabalho;
	}

	public void setSiglaFrenteTrabalho(String siglaFrenteTrabalho) {
		this.siglaFrenteTrabalho = siglaFrenteTrabalho;
	}

	public List<OpeCentro2Equip> getOpeCentro2Equips() {
		return this.opeCentro2Equips;
	}

	public void setOpeCentro2Equips(List<OpeCentro2Equip> opeCentro2Equips) {
		this.opeCentro2Equips = opeCentro2Equips;
	}

	public OpeCentro2Equip addOpeCentro2Equip(OpeCentro2Equip opeCentro2Equip) {
		getOpeCentro2Equips().add(opeCentro2Equip);
		opeCentro2Equip.setOpeFrenteTrabalho(this);

		return opeCentro2Equip;
	}

	public OpeCentro2Equip removeOpeCentro2Equip(OpeCentro2Equip opeCentro2Equip) {
		getOpeCentro2Equips().remove(opeCentro2Equip);
		opeCentro2Equip.setOpeFrenteTrabalho(null);

		return opeCentro2Equip;
	}

	public List<OpeCentro2Ord> getOpeCentro2Ords() {
		return this.opeCentro2Ords;
	}

	public void setOpeCentro2Ords(List<OpeCentro2Ord> opeCentro2Ords) {
		this.opeCentro2Ords = opeCentro2Ords;
	}

	public OpeCentro2Ord addOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().add(opeCentro2Ord);
		opeCentro2Ord.setOpeFrenteTrabalho(this);

		return opeCentro2Ord;
	}

	public OpeCentro2Ord removeOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().remove(opeCentro2Ord);
		opeCentro2Ord.setOpeFrenteTrabalho(null);

		return opeCentro2Ord;
	}

	public List<OpeCentro2OrdAtiv> getOpeCentro2OrdAtivs() {
		return this.opeCentro2OrdAtivs;
	}

	public void setOpeCentro2OrdAtivs(List<OpeCentro2OrdAtiv> opeCentro2OrdAtivs) {
		this.opeCentro2OrdAtivs = opeCentro2OrdAtivs;
	}

	public OpeCentro2OrdAtiv addOpeCentro2OrdAtiv(OpeCentro2OrdAtiv opeCentro2OrdAtiv) {
		getOpeCentro2OrdAtivs().add(opeCentro2OrdAtiv);
		opeCentro2OrdAtiv.setOpeFrenteTrabalho(this);

		return opeCentro2OrdAtiv;
	}

	public OpeCentro2OrdAtiv removeOpeCentro2OrdAtiv(OpeCentro2OrdAtiv opeCentro2OrdAtiv) {
		getOpeCentro2OrdAtivs().remove(opeCentro2OrdAtiv);
		opeCentro2OrdAtiv.setOpeFrenteTrabalho(null);

		return opeCentro2OrdAtiv;
	}

	public List<OpeCentro2ParamPer> getOpeCentro2ParamPers() {
		return this.opeCentro2ParamPers;
	}

	public void setOpeCentro2ParamPers(List<OpeCentro2ParamPer> opeCentro2ParamPers) {
		this.opeCentro2ParamPers = opeCentro2ParamPers;
	}

	public OpeCentro2ParamPer addOpeCentro2ParamPer(OpeCentro2ParamPer opeCentro2ParamPer) {
		getOpeCentro2ParamPers().add(opeCentro2ParamPer);
		opeCentro2ParamPer.setOpeFrenteTrabalho(this);

		return opeCentro2ParamPer;
	}

	public OpeCentro2ParamPer removeOpeCentro2ParamPer(OpeCentro2ParamPer opeCentro2ParamPer) {
		getOpeCentro2ParamPers().remove(opeCentro2ParamPer);
		opeCentro2ParamPer.setOpeFrenteTrabalho(null);

		return opeCentro2ParamPer;
	}

	public List<OpeCentro2Pessoa> getOpeCentro2Pessoas() {
		return this.opeCentro2Pessoas;
	}

	public void setOpeCentro2Pessoas(List<OpeCentro2Pessoa> opeCentro2Pessoas) {
		this.opeCentro2Pessoas = opeCentro2Pessoas;
	}

	public OpeCentro2Pessoa addOpeCentro2Pessoa(OpeCentro2Pessoa opeCentro2Pessoa) {
		getOpeCentro2Pessoas().add(opeCentro2Pessoa);
		opeCentro2Pessoa.setOpeFrenteTrabalho(this);

		return opeCentro2Pessoa;
	}

	public OpeCentro2Pessoa removeOpeCentro2Pessoa(OpeCentro2Pessoa opeCentro2Pessoa) {
		getOpeCentro2Pessoas().remove(opeCentro2Pessoa);
		opeCentro2Pessoa.setOpeFrenteTrabalho(null);

		return opeCentro2Pessoa;
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

}