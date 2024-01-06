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
@Table(name="ger_umedida")
@NamedQuery(name="GerUmedida.findAll", query="SELECT g FROM GerUmedida g")
public class GerUmedida implements Serializable {
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

	@Column(name="nr_umedida", length=50)
	private String nrUmedida;

	@Column(name="sigla_umedida", nullable=false, length=50)
	private String siglaUmedida;

	//bi-directional many-to-one association to CtbComp
	@OneToMany(mappedBy="gerUmedida")
	private List<CtbComp> ctbComps;

	//bi-directional many-to-one association to GerItemserv
	@OneToMany(mappedBy="gerUmedida")
	private List<GerItemserv> gerItemservs;

	//bi-directional many-to-one association to GerUmedidaConv
	@OneToMany(mappedBy="gerUmedida1")
	private List<GerUmedidaConv> gerUmedidaConvs1;

	//bi-directional many-to-one association to GerUmedidaConv
	@OneToMany(mappedBy="gerUmedida2")
	private List<GerUmedidaConv> gerUmedidaConvs2;

	//bi-directional many-to-one association to Ind
	@OneToMany(mappedBy="gerUmedida")
	private List<Ind> inds;

	//bi-directional many-to-one association to MovItemserv
	@OneToMany(mappedBy="gerUmedida")
	private List<MovItemserv> movItemservs;

	//bi-directional many-to-one association to MovMedida
	@OneToMany(mappedBy="gerUmedida")
	private List<MovMedida> movMedidas;

	//bi-directional many-to-one association to OpeAtividade
	@OneToMany(mappedBy="gerUmedida")
	private List<OpeAtividade> opeAtividades;

	//bi-directional many-to-one association to OpeCentro2
	@OneToMany(mappedBy="gerUmedida")
	private List<OpeCentro2> opeCentro2s;

	//bi-directional many-to-one association to OpeCentro2Area
	@OneToMany(mappedBy="gerUmedida")
	private List<OpeCentro2Area> opeCentro2Areas;

	//bi-directional many-to-one association to OpeCentro2OrdDest
	@OneToMany(mappedBy="gerUmedida")
	private List<OpeCentro2OrdDest> opeCentro2OrdDests;

	//bi-directional many-to-one association to OpeOcor
	@OneToMany(mappedBy="gerUmedida")
	private List<OpeOcor> opeOcors;

	public GerUmedida() {
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

	public String getNrUmedida() {
		return this.nrUmedida;
	}

	public void setNrUmedida(String nrUmedida) {
		this.nrUmedida = nrUmedida;
	}

	public String getSiglaUmedida() {
		return this.siglaUmedida;
	}

	public void setSiglaUmedida(String siglaUmedida) {
		this.siglaUmedida = siglaUmedida;
	}

	public List<CtbComp> getCtbComps() {
		return this.ctbComps;
	}

	public void setCtbComps(List<CtbComp> ctbComps) {
		this.ctbComps = ctbComps;
	}

	public CtbComp addCtbComp(CtbComp ctbComp) {
		getCtbComps().add(ctbComp);
		ctbComp.setGerUmedida(this);

		return ctbComp;
	}

	public CtbComp removeCtbComp(CtbComp ctbComp) {
		getCtbComps().remove(ctbComp);
		ctbComp.setGerUmedida(null);

		return ctbComp;
	}

	public List<GerItemserv> getGerItemservs() {
		return this.gerItemservs;
	}

	public void setGerItemservs(List<GerItemserv> gerItemservs) {
		this.gerItemservs = gerItemservs;
	}

	public GerItemserv addGerItemserv(GerItemserv gerItemserv) {
		getGerItemservs().add(gerItemserv);
		gerItemserv.setGerUmedida(this);

		return gerItemserv;
	}

	public GerItemserv removeGerItemserv(GerItemserv gerItemserv) {
		getGerItemservs().remove(gerItemserv);
		gerItemserv.setGerUmedida(null);

		return gerItemserv;
	}

	public List<GerUmedidaConv> getGerUmedidaConvs1() {
		return this.gerUmedidaConvs1;
	}

	public void setGerUmedidaConvs1(List<GerUmedidaConv> gerUmedidaConvs1) {
		this.gerUmedidaConvs1 = gerUmedidaConvs1;
	}

	public GerUmedidaConv addGerUmedidaConvs1(GerUmedidaConv gerUmedidaConvs1) {
		getGerUmedidaConvs1().add(gerUmedidaConvs1);
		gerUmedidaConvs1.setGerUmedida1(this);

		return gerUmedidaConvs1;
	}

	public GerUmedidaConv removeGerUmedidaConvs1(GerUmedidaConv gerUmedidaConvs1) {
		getGerUmedidaConvs1().remove(gerUmedidaConvs1);
		gerUmedidaConvs1.setGerUmedida1(null);

		return gerUmedidaConvs1;
	}

	public List<GerUmedidaConv> getGerUmedidaConvs2() {
		return this.gerUmedidaConvs2;
	}

	public void setGerUmedidaConvs2(List<GerUmedidaConv> gerUmedidaConvs2) {
		this.gerUmedidaConvs2 = gerUmedidaConvs2;
	}

	public GerUmedidaConv addGerUmedidaConvs2(GerUmedidaConv gerUmedidaConvs2) {
		getGerUmedidaConvs2().add(gerUmedidaConvs2);
		gerUmedidaConvs2.setGerUmedida2(this);

		return gerUmedidaConvs2;
	}

	public GerUmedidaConv removeGerUmedidaConvs2(GerUmedidaConv gerUmedidaConvs2) {
		getGerUmedidaConvs2().remove(gerUmedidaConvs2);
		gerUmedidaConvs2.setGerUmedida2(null);

		return gerUmedidaConvs2;
	}

	public List<Ind> getInds() {
		return this.inds;
	}

	public void setInds(List<Ind> inds) {
		this.inds = inds;
	}

	public Ind addInd(Ind ind) {
		getInds().add(ind);
		ind.setGerUmedida(this);

		return ind;
	}

	public Ind removeInd(Ind ind) {
		getInds().remove(ind);
		ind.setGerUmedida(null);

		return ind;
	}

	public List<MovItemserv> getMovItemservs() {
		return this.movItemservs;
	}

	public void setMovItemservs(List<MovItemserv> movItemservs) {
		this.movItemservs = movItemservs;
	}

	public MovItemserv addMovItemserv(MovItemserv movItemserv) {
		getMovItemservs().add(movItemserv);
		movItemserv.setGerUmedida(this);

		return movItemserv;
	}

	public MovItemserv removeMovItemserv(MovItemserv movItemserv) {
		getMovItemservs().remove(movItemserv);
		movItemserv.setGerUmedida(null);

		return movItemserv;
	}

	public List<MovMedida> getMovMedidas() {
		return this.movMedidas;
	}

	public void setMovMedidas(List<MovMedida> movMedidas) {
		this.movMedidas = movMedidas;
	}

	public MovMedida addMovMedida(MovMedida movMedida) {
		getMovMedidas().add(movMedida);
		movMedida.setGerUmedida(this);

		return movMedida;
	}

	public MovMedida removeMovMedida(MovMedida movMedida) {
		getMovMedidas().remove(movMedida);
		movMedida.setGerUmedida(null);

		return movMedida;
	}

	public List<OpeAtividade> getOpeAtividades() {
		return this.opeAtividades;
	}

	public void setOpeAtividades(List<OpeAtividade> opeAtividades) {
		this.opeAtividades = opeAtividades;
	}

	public OpeAtividade addOpeAtividade(OpeAtividade opeAtividade) {
		getOpeAtividades().add(opeAtividade);
		opeAtividade.setGerUmedida(this);

		return opeAtividade;
	}

	public OpeAtividade removeOpeAtividade(OpeAtividade opeAtividade) {
		getOpeAtividades().remove(opeAtividade);
		opeAtividade.setGerUmedida(null);

		return opeAtividade;
	}

	public List<OpeCentro2> getOpeCentro2s() {
		return this.opeCentro2s;
	}

	public void setOpeCentro2s(List<OpeCentro2> opeCentro2s) {
		this.opeCentro2s = opeCentro2s;
	}

	public OpeCentro2 addOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().add(opeCentro2);
		opeCentro2.setGerUmedida(this);

		return opeCentro2;
	}

	public OpeCentro2 removeOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().remove(opeCentro2);
		opeCentro2.setGerUmedida(null);

		return opeCentro2;
	}

	public List<OpeCentro2Area> getOpeCentro2Areas() {
		return this.opeCentro2Areas;
	}

	public void setOpeCentro2Areas(List<OpeCentro2Area> opeCentro2Areas) {
		this.opeCentro2Areas = opeCentro2Areas;
	}

	public OpeCentro2Area addOpeCentro2Area(OpeCentro2Area opeCentro2Area) {
		getOpeCentro2Areas().add(opeCentro2Area);
		opeCentro2Area.setGerUmedida(this);

		return opeCentro2Area;
	}

	public OpeCentro2Area removeOpeCentro2Area(OpeCentro2Area opeCentro2Area) {
		getOpeCentro2Areas().remove(opeCentro2Area);
		opeCentro2Area.setGerUmedida(null);

		return opeCentro2Area;
	}

	public List<OpeCentro2OrdDest> getOpeCentro2OrdDests() {
		return this.opeCentro2OrdDests;
	}

	public void setOpeCentro2OrdDests(List<OpeCentro2OrdDest> opeCentro2OrdDests) {
		this.opeCentro2OrdDests = opeCentro2OrdDests;
	}

	public OpeCentro2OrdDest addOpeCentro2OrdDest(OpeCentro2OrdDest opeCentro2OrdDest) {
		getOpeCentro2OrdDests().add(opeCentro2OrdDest);
		opeCentro2OrdDest.setGerUmedida(this);

		return opeCentro2OrdDest;
	}

	public OpeCentro2OrdDest removeOpeCentro2OrdDest(OpeCentro2OrdDest opeCentro2OrdDest) {
		getOpeCentro2OrdDests().remove(opeCentro2OrdDest);
		opeCentro2OrdDest.setGerUmedida(null);

		return opeCentro2OrdDest;
	}

	public List<OpeOcor> getOpeOcors() {
		return this.opeOcors;
	}

	public void setOpeOcors(List<OpeOcor> opeOcors) {
		this.opeOcors = opeOcors;
	}

	public OpeOcor addOpeOcor(OpeOcor opeOcor) {
		getOpeOcors().add(opeOcor);
		opeOcor.setGerUmedida(this);

		return opeOcor;
	}

	public OpeOcor removeOpeOcor(OpeOcor opeOcor) {
		getOpeOcors().remove(opeOcor);
		opeOcor.setGerUmedida(null);

		return opeOcor;
	}

}