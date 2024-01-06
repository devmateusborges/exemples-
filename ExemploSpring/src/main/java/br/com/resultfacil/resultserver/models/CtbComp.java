package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ctb_comp")
@NamedQuery(name="CtbComp.findAll", query="SELECT c FROM CtbComp c")
public class CtbComp implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(name="ctb_comp_id_calc_orig", length=36)
	private String ctbCompIdCalcOrig;

	@Column(name="fator_calc_origem", precision=18, scale=6)
	private BigDecimal fatorCalcOrigem;

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

	@Column(name="sigla_comp", nullable=false, length=50)
	private String siglaComp;

	//bi-directional many-to-one association to CtbCompGrupo
	@ManyToOne
	@JoinColumn(name="ctb_comp_grupo_id", nullable=false)
	private CtbCompGrupo ctbCompGrupo;

	//bi-directional many-to-one association to GerUmedida
	@ManyToOne
	@JoinColumn(name="ger_umedida_id", nullable=false)
	private GerUmedida gerUmedida;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to CtbLancDet
	@OneToMany(mappedBy="ctbComp")
	private List<CtbLancDet> ctbLancDets;

	//bi-directional many-to-one association to GerItemserv
	@OneToMany(mappedBy="ctbComp")
	private List<GerItemserv> gerItemservs;

	//bi-directional many-to-one association to OpeCentro1
	@OneToMany(mappedBy="ctbComp")
	private List<OpeCentro1> opeCentro1s;

	//bi-directional many-to-one association to OpeCentro2
	@OneToMany(mappedBy="ctbComp")
	private List<OpeCentro2> opeCentro2s;

	//bi-directional many-to-one association to OpeCentro2OrdItemserv
	@OneToMany(mappedBy="ctbComp")
	private List<OpeCentro2OrdItemserv> opeCentro2OrdItemservs;

	//bi-directional many-to-one association to OpeCentro2OrdRec
	@OneToMany(mappedBy="ctbComp1")
	private List<OpeCentro2OrdRec> opeCentro2OrdRecs1;

	//bi-directional many-to-one association to OpeCentro2OrdRec
	@OneToMany(mappedBy="ctbComp2")
	private List<OpeCentro2OrdRec> opeCentro2OrdRecs2;

	//bi-directional many-to-one association to OpeCentroPrevDest
	@OneToMany(mappedBy="ctbComp")
	private List<OpeCentroPrevDest> opeCentroPrevDests;

	//bi-directional many-to-one association to OpeCentroRendFator
	@OneToMany(mappedBy="ctbComp")
	private List<OpeCentroRendFator> opeCentroRendFators;

	//bi-directional many-to-one association to OpeCentroSubgrupo
	@OneToMany(mappedBy="ctbComp")
	private List<OpeCentroSubgrupo> opeCentroSubgrupos;

	public CtbComp() {
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

	public String getCtbCompIdCalcOrig() {
		return this.ctbCompIdCalcOrig;
	}

	public void setCtbCompIdCalcOrig(String ctbCompIdCalcOrig) {
		this.ctbCompIdCalcOrig = ctbCompIdCalcOrig;
	}

	public BigDecimal getFatorCalcOrigem() {
		return this.fatorCalcOrigem;
	}

	public void setFatorCalcOrigem(BigDecimal fatorCalcOrigem) {
		this.fatorCalcOrigem = fatorCalcOrigem;
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

	public String getSiglaComp() {
		return this.siglaComp;
	}

	public void setSiglaComp(String siglaComp) {
		this.siglaComp = siglaComp;
	}

	public CtbCompGrupo getCtbCompGrupo() {
		return this.ctbCompGrupo;
	}

	public void setCtbCompGrupo(CtbCompGrupo ctbCompGrupo) {
		this.ctbCompGrupo = ctbCompGrupo;
	}

	public GerUmedida getGerUmedida() {
		return this.gerUmedida;
	}

	public void setGerUmedida(GerUmedida gerUmedida) {
		this.gerUmedida = gerUmedida;
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
		ctbLancDet.setCtbComp(this);

		return ctbLancDet;
	}

	public CtbLancDet removeCtbLancDet(CtbLancDet ctbLancDet) {
		getCtbLancDets().remove(ctbLancDet);
		ctbLancDet.setCtbComp(null);

		return ctbLancDet;
	}

	public List<GerItemserv> getGerItemservs() {
		return this.gerItemservs;
	}

	public void setGerItemservs(List<GerItemserv> gerItemservs) {
		this.gerItemservs = gerItemservs;
	}

	public GerItemserv addGerItemserv(GerItemserv gerItemserv) {
		getGerItemservs().add(gerItemserv);
		gerItemserv.setCtbComp(this);

		return gerItemserv;
	}

	public GerItemserv removeGerItemserv(GerItemserv gerItemserv) {
		getGerItemservs().remove(gerItemserv);
		gerItemserv.setCtbComp(null);

		return gerItemserv;
	}

	public List<OpeCentro1> getOpeCentro1s() {
		return this.opeCentro1s;
	}

	public void setOpeCentro1s(List<OpeCentro1> opeCentro1s) {
		this.opeCentro1s = opeCentro1s;
	}

	public OpeCentro1 addOpeCentro1(OpeCentro1 opeCentro1) {
		getOpeCentro1s().add(opeCentro1);
		opeCentro1.setCtbComp(this);

		return opeCentro1;
	}

	public OpeCentro1 removeOpeCentro1(OpeCentro1 opeCentro1) {
		getOpeCentro1s().remove(opeCentro1);
		opeCentro1.setCtbComp(null);

		return opeCentro1;
	}

	public List<OpeCentro2> getOpeCentro2s() {
		return this.opeCentro2s;
	}

	public void setOpeCentro2s(List<OpeCentro2> opeCentro2s) {
		this.opeCentro2s = opeCentro2s;
	}

	public OpeCentro2 addOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().add(opeCentro2);
		opeCentro2.setCtbComp(this);

		return opeCentro2;
	}

	public OpeCentro2 removeOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().remove(opeCentro2);
		opeCentro2.setCtbComp(null);

		return opeCentro2;
	}

	public List<OpeCentro2OrdItemserv> getOpeCentro2OrdItemservs() {
		return this.opeCentro2OrdItemservs;
	}

	public void setOpeCentro2OrdItemservs(List<OpeCentro2OrdItemserv> opeCentro2OrdItemservs) {
		this.opeCentro2OrdItemservs = opeCentro2OrdItemservs;
	}

	public OpeCentro2OrdItemserv addOpeCentro2OrdItemserv(OpeCentro2OrdItemserv opeCentro2OrdItemserv) {
		getOpeCentro2OrdItemservs().add(opeCentro2OrdItemserv);
		opeCentro2OrdItemserv.setCtbComp(this);

		return opeCentro2OrdItemserv;
	}

	public OpeCentro2OrdItemserv removeOpeCentro2OrdItemserv(OpeCentro2OrdItemserv opeCentro2OrdItemserv) {
		getOpeCentro2OrdItemservs().remove(opeCentro2OrdItemserv);
		opeCentro2OrdItemserv.setCtbComp(null);

		return opeCentro2OrdItemserv;
	}

	public List<OpeCentro2OrdRec> getOpeCentro2OrdRecs1() {
		return this.opeCentro2OrdRecs1;
	}

	public void setOpeCentro2OrdRecs1(List<OpeCentro2OrdRec> opeCentro2OrdRecs1) {
		this.opeCentro2OrdRecs1 = opeCentro2OrdRecs1;
	}

	public OpeCentro2OrdRec addOpeCentro2OrdRecs1(OpeCentro2OrdRec opeCentro2OrdRecs1) {
		getOpeCentro2OrdRecs1().add(opeCentro2OrdRecs1);
		opeCentro2OrdRecs1.setCtbComp1(this);

		return opeCentro2OrdRecs1;
	}

	public OpeCentro2OrdRec removeOpeCentro2OrdRecs1(OpeCentro2OrdRec opeCentro2OrdRecs1) {
		getOpeCentro2OrdRecs1().remove(opeCentro2OrdRecs1);
		opeCentro2OrdRecs1.setCtbComp1(null);

		return opeCentro2OrdRecs1;
	}

	public List<OpeCentro2OrdRec> getOpeCentro2OrdRecs2() {
		return this.opeCentro2OrdRecs2;
	}

	public void setOpeCentro2OrdRecs2(List<OpeCentro2OrdRec> opeCentro2OrdRecs2) {
		this.opeCentro2OrdRecs2 = opeCentro2OrdRecs2;
	}

	public OpeCentro2OrdRec addOpeCentro2OrdRecs2(OpeCentro2OrdRec opeCentro2OrdRecs2) {
		getOpeCentro2OrdRecs2().add(opeCentro2OrdRecs2);
		opeCentro2OrdRecs2.setCtbComp2(this);

		return opeCentro2OrdRecs2;
	}

	public OpeCentro2OrdRec removeOpeCentro2OrdRecs2(OpeCentro2OrdRec opeCentro2OrdRecs2) {
		getOpeCentro2OrdRecs2().remove(opeCentro2OrdRecs2);
		opeCentro2OrdRecs2.setCtbComp2(null);

		return opeCentro2OrdRecs2;
	}

	public List<OpeCentroPrevDest> getOpeCentroPrevDests() {
		return this.opeCentroPrevDests;
	}

	public void setOpeCentroPrevDests(List<OpeCentroPrevDest> opeCentroPrevDests) {
		this.opeCentroPrevDests = opeCentroPrevDests;
	}

	public OpeCentroPrevDest addOpeCentroPrevDest(OpeCentroPrevDest opeCentroPrevDest) {
		getOpeCentroPrevDests().add(opeCentroPrevDest);
		opeCentroPrevDest.setCtbComp(this);

		return opeCentroPrevDest;
	}

	public OpeCentroPrevDest removeOpeCentroPrevDest(OpeCentroPrevDest opeCentroPrevDest) {
		getOpeCentroPrevDests().remove(opeCentroPrevDest);
		opeCentroPrevDest.setCtbComp(null);

		return opeCentroPrevDest;
	}

	public List<OpeCentroRendFator> getOpeCentroRendFators() {
		return this.opeCentroRendFators;
	}

	public void setOpeCentroRendFators(List<OpeCentroRendFator> opeCentroRendFators) {
		this.opeCentroRendFators = opeCentroRendFators;
	}

	public OpeCentroRendFator addOpeCentroRendFator(OpeCentroRendFator opeCentroRendFator) {
		getOpeCentroRendFators().add(opeCentroRendFator);
		opeCentroRendFator.setCtbComp(this);

		return opeCentroRendFator;
	}

	public OpeCentroRendFator removeOpeCentroRendFator(OpeCentroRendFator opeCentroRendFator) {
		getOpeCentroRendFators().remove(opeCentroRendFator);
		opeCentroRendFator.setCtbComp(null);

		return opeCentroRendFator;
	}

	public List<OpeCentroSubgrupo> getOpeCentroSubgrupos() {
		return this.opeCentroSubgrupos;
	}

	public void setOpeCentroSubgrupos(List<OpeCentroSubgrupo> opeCentroSubgrupos) {
		this.opeCentroSubgrupos = opeCentroSubgrupos;
	}

	public OpeCentroSubgrupo addOpeCentroSubgrupo(OpeCentroSubgrupo opeCentroSubgrupo) {
		getOpeCentroSubgrupos().add(opeCentroSubgrupo);
		opeCentroSubgrupo.setCtbComp(this);

		return opeCentroSubgrupo;
	}

	public OpeCentroSubgrupo removeOpeCentroSubgrupo(OpeCentroSubgrupo opeCentroSubgrupo) {
		getOpeCentroSubgrupos().remove(opeCentroSubgrupo);
		opeCentroSubgrupo.setCtbComp(null);

		return opeCentroSubgrupo;
	}

}