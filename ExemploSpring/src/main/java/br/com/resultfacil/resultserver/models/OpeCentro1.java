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
@Table(name="ope_centro1")
@NamedQuery(name="OpeCentro1.findAll", query="SELECT o FROM OpeCentro1 o")
public class OpeCentro1 implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

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

	@Column(nullable=false, length=100)
	private String nome;

	@Column(length=250)
	private String observacao;

	@Column(name="sigla_centro1", nullable=false, length=50)
	private String siglaCentro1;

	//bi-directional many-to-one association to FinPagrecPrevDest
	@OneToMany(mappedBy="opeCentro11")
	private List<FinPagrecPrevDest> finPagrecPrevDests1;

	//bi-directional many-to-one association to FinPagrecPrevDest
	@OneToMany(mappedBy="opeCentro12")
	private List<FinPagrecPrevDest> finPagrecPrevDests2;

	//bi-directional many-to-one association to CtbComp
	@ManyToOne
	@JoinColumn(name="ctb_comp_id")
	private CtbComp ctbComp;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="ger_pessoa_id", nullable=false)
	private GerPessoa gerPessoa;

	//bi-directional many-to-one association to OpeCentroSubtipo
	@ManyToOne
	@JoinColumn(name="ope_centro_subtipo_id", nullable=false)
	private OpeCentroSubtipo opeCentroSubtipo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCentro2
	@OneToMany(mappedBy="opeCentro1")
	private List<OpeCentro2> opeCentro2s;

	//bi-directional many-to-one association to OpeCentro2OrdRec
	@OneToMany(mappedBy="opeCentro11")
	private List<OpeCentro2OrdRec> opeCentro2OrdRecs1;

	//bi-directional many-to-one association to OpeCentro2OrdRec
	@OneToMany(mappedBy="opeCentro12")
	private List<OpeCentro2OrdRec> opeCentro2OrdRecs2;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="opeCentro1")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="opeCentro11")
	private List<OpeCentroDest> opeCentroDests1;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="opeCentro12")
	private List<OpeCentroDest> opeCentroDests2;

	//bi-directional many-to-one association to OpeCentroDest
	@OneToMany(mappedBy="opeCentro13")
	private List<OpeCentroDest> opeCentroDests3;

	//bi-directional many-to-one association to OpeCentroPrevDest
	@OneToMany(mappedBy="opeCentro1")
	private List<OpeCentroPrevDest> opeCentroPrevDests;

	//bi-directional many-to-one association to OpeCentroRatFator
	@OneToMany(mappedBy="opeCentro1")
	private List<OpeCentroRatFator> opeCentroRatFators;

	//bi-directional many-to-one association to SysDocument
	@OneToMany(mappedBy="opeCentro1")
	private List<SysDocument> sysDocuments;

	public OpeCentro1() {
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

	public String getSiglaCentro1() {
		return this.siglaCentro1;
	}

	public void setSiglaCentro1(String siglaCentro1) {
		this.siglaCentro1 = siglaCentro1;
	}

	public List<FinPagrecPrevDest> getFinPagrecPrevDests1() {
		return this.finPagrecPrevDests1;
	}

	public void setFinPagrecPrevDests1(List<FinPagrecPrevDest> finPagrecPrevDests1) {
		this.finPagrecPrevDests1 = finPagrecPrevDests1;
	}

	public FinPagrecPrevDest addFinPagrecPrevDests1(FinPagrecPrevDest finPagrecPrevDests1) {
		getFinPagrecPrevDests1().add(finPagrecPrevDests1);
		finPagrecPrevDests1.setOpeCentro11(this);

		return finPagrecPrevDests1;
	}

	public FinPagrecPrevDest removeFinPagrecPrevDests1(FinPagrecPrevDest finPagrecPrevDests1) {
		getFinPagrecPrevDests1().remove(finPagrecPrevDests1);
		finPagrecPrevDests1.setOpeCentro11(null);

		return finPagrecPrevDests1;
	}

	public List<FinPagrecPrevDest> getFinPagrecPrevDests2() {
		return this.finPagrecPrevDests2;
	}

	public void setFinPagrecPrevDests2(List<FinPagrecPrevDest> finPagrecPrevDests2) {
		this.finPagrecPrevDests2 = finPagrecPrevDests2;
	}

	public FinPagrecPrevDest addFinPagrecPrevDests2(FinPagrecPrevDest finPagrecPrevDests2) {
		getFinPagrecPrevDests2().add(finPagrecPrevDests2);
		finPagrecPrevDests2.setOpeCentro12(this);

		return finPagrecPrevDests2;
	}

	public FinPagrecPrevDest removeFinPagrecPrevDests2(FinPagrecPrevDest finPagrecPrevDests2) {
		getFinPagrecPrevDests2().remove(finPagrecPrevDests2);
		finPagrecPrevDests2.setOpeCentro12(null);

		return finPagrecPrevDests2;
	}

	public CtbComp getCtbComp() {
		return this.ctbComp;
	}

	public void setCtbComp(CtbComp ctbComp) {
		this.ctbComp = ctbComp;
	}

	public GerPessoa getGerPessoa() {
		return this.gerPessoa;
	}

	public void setGerPessoa(GerPessoa gerPessoa) {
		this.gerPessoa = gerPessoa;
	}

	public OpeCentroSubtipo getOpeCentroSubtipo() {
		return this.opeCentroSubtipo;
	}

	public void setOpeCentroSubtipo(OpeCentroSubtipo opeCentroSubtipo) {
		this.opeCentroSubtipo = opeCentroSubtipo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCentro2> getOpeCentro2s() {
		return this.opeCentro2s;
	}

	public void setOpeCentro2s(List<OpeCentro2> opeCentro2s) {
		this.opeCentro2s = opeCentro2s;
	}

	public OpeCentro2 addOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().add(opeCentro2);
		opeCentro2.setOpeCentro1(this);

		return opeCentro2;
	}

	public OpeCentro2 removeOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().remove(opeCentro2);
		opeCentro2.setOpeCentro1(null);

		return opeCentro2;
	}

	public List<OpeCentro2OrdRec> getOpeCentro2OrdRecs1() {
		return this.opeCentro2OrdRecs1;
	}

	public void setOpeCentro2OrdRecs1(List<OpeCentro2OrdRec> opeCentro2OrdRecs1) {
		this.opeCentro2OrdRecs1 = opeCentro2OrdRecs1;
	}

	public OpeCentro2OrdRec addOpeCentro2OrdRecs1(OpeCentro2OrdRec opeCentro2OrdRecs1) {
		getOpeCentro2OrdRecs1().add(opeCentro2OrdRecs1);
		opeCentro2OrdRecs1.setOpeCentro11(this);

		return opeCentro2OrdRecs1;
	}

	public OpeCentro2OrdRec removeOpeCentro2OrdRecs1(OpeCentro2OrdRec opeCentro2OrdRecs1) {
		getOpeCentro2OrdRecs1().remove(opeCentro2OrdRecs1);
		opeCentro2OrdRecs1.setOpeCentro11(null);

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
		opeCentro2OrdRecs2.setOpeCentro12(this);

		return opeCentro2OrdRecs2;
	}

	public OpeCentro2OrdRec removeOpeCentro2OrdRecs2(OpeCentro2OrdRec opeCentro2OrdRecs2) {
		getOpeCentro2OrdRecs2().remove(opeCentro2OrdRecs2);
		opeCentro2OrdRecs2.setOpeCentro12(null);

		return opeCentro2OrdRecs2;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setOpeCentro1(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setOpeCentro1(null);

		return opeCentroConfig;
	}

	public List<OpeCentroDest> getOpeCentroDests1() {
		return this.opeCentroDests1;
	}

	public void setOpeCentroDests1(List<OpeCentroDest> opeCentroDests1) {
		this.opeCentroDests1 = opeCentroDests1;
	}

	public OpeCentroDest addOpeCentroDests1(OpeCentroDest opeCentroDests1) {
		getOpeCentroDests1().add(opeCentroDests1);
		opeCentroDests1.setOpeCentro11(this);

		return opeCentroDests1;
	}

	public OpeCentroDest removeOpeCentroDests1(OpeCentroDest opeCentroDests1) {
		getOpeCentroDests1().remove(opeCentroDests1);
		opeCentroDests1.setOpeCentro11(null);

		return opeCentroDests1;
	}

	public List<OpeCentroDest> getOpeCentroDests2() {
		return this.opeCentroDests2;
	}

	public void setOpeCentroDests2(List<OpeCentroDest> opeCentroDests2) {
		this.opeCentroDests2 = opeCentroDests2;
	}

	public OpeCentroDest addOpeCentroDests2(OpeCentroDest opeCentroDests2) {
		getOpeCentroDests2().add(opeCentroDests2);
		opeCentroDests2.setOpeCentro12(this);

		return opeCentroDests2;
	}

	public OpeCentroDest removeOpeCentroDests2(OpeCentroDest opeCentroDests2) {
		getOpeCentroDests2().remove(opeCentroDests2);
		opeCentroDests2.setOpeCentro12(null);

		return opeCentroDests2;
	}

	public List<OpeCentroDest> getOpeCentroDests3() {
		return this.opeCentroDests3;
	}

	public void setOpeCentroDests3(List<OpeCentroDest> opeCentroDests3) {
		this.opeCentroDests3 = opeCentroDests3;
	}

	public OpeCentroDest addOpeCentroDests3(OpeCentroDest opeCentroDests3) {
		getOpeCentroDests3().add(opeCentroDests3);
		opeCentroDests3.setOpeCentro13(this);

		return opeCentroDests3;
	}

	public OpeCentroDest removeOpeCentroDests3(OpeCentroDest opeCentroDests3) {
		getOpeCentroDests3().remove(opeCentroDests3);
		opeCentroDests3.setOpeCentro13(null);

		return opeCentroDests3;
	}

	public List<OpeCentroPrevDest> getOpeCentroPrevDests() {
		return this.opeCentroPrevDests;
	}

	public void setOpeCentroPrevDests(List<OpeCentroPrevDest> opeCentroPrevDests) {
		this.opeCentroPrevDests = opeCentroPrevDests;
	}

	public OpeCentroPrevDest addOpeCentroPrevDest(OpeCentroPrevDest opeCentroPrevDest) {
		getOpeCentroPrevDests().add(opeCentroPrevDest);
		opeCentroPrevDest.setOpeCentro1(this);

		return opeCentroPrevDest;
	}

	public OpeCentroPrevDest removeOpeCentroPrevDest(OpeCentroPrevDest opeCentroPrevDest) {
		getOpeCentroPrevDests().remove(opeCentroPrevDest);
		opeCentroPrevDest.setOpeCentro1(null);

		return opeCentroPrevDest;
	}

	public List<OpeCentroRatFator> getOpeCentroRatFators() {
		return this.opeCentroRatFators;
	}

	public void setOpeCentroRatFators(List<OpeCentroRatFator> opeCentroRatFators) {
		this.opeCentroRatFators = opeCentroRatFators;
	}

	public OpeCentroRatFator addOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().add(opeCentroRatFator);
		opeCentroRatFator.setOpeCentro1(this);

		return opeCentroRatFator;
	}

	public OpeCentroRatFator removeOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().remove(opeCentroRatFator);
		opeCentroRatFator.setOpeCentro1(null);

		return opeCentroRatFator;
	}

	public List<SysDocument> getSysDocuments() {
		return this.sysDocuments;
	}

	public void setSysDocuments(List<SysDocument> sysDocuments) {
		this.sysDocuments = sysDocuments;
	}

	public SysDocument addSysDocument(SysDocument sysDocument) {
		getSysDocuments().add(sysDocument);
		sysDocument.setOpeCentro1(this);

		return sysDocument;
	}

	public SysDocument removeSysDocument(SysDocument sysDocument) {
		getSysDocuments().remove(sysDocument);
		sysDocument.setOpeCentro1(null);

		return sysDocument;
	}

}