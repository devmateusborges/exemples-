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
@Table(name="ger_empresa")
@NamedQuery(name="GerEmpresa.findAll", query="SELECT g FROM GerEmpresa g")
public class GerEmpresa implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(name="contato_1", length=100)
	private String contato1;

	@Column(name="contato_2", length=100)
	private String contato2;

	@Column(name="contato_3", length=100)
	private String contato3;

	@Temporal(TemporalType.DATE)
	@Column(name="data_abertura")
	private Date dataAbertura;

	@Temporal(TemporalType.DATE)
	@Column(name="data_validade_a1")
	private Date dataValidadeA1;

	@Temporal(TemporalType.DATE)
	@Column(name="data_validade_a3")
	private Date dataValidadeA3;

	@Column(name="doc_cnae", length=50)
	private String docCnae;

	@Column(name="doc_cnpj", length=50)
	private String docCnpj;

	@Column(name="doc_cpf", length=50)
	private String docCpf;

	@Column(name="doc_ie", length=50)
	private String docIe;

	@Column(name="doc_im", length=50)
	private String docIm;

	@Column(name="doc_junta", length=50)
	private String docJunta;

	@Column(name="doc_rntrc", length=100)
	private String docRntrc;

	@Column(name="email_1", length=255)
	private String email1;

	@Column(name="end_bairro", length=100)
	private String endBairro;

	@Column(name="end_cep", length=100)
	private String endCep;

	@Column(name="end_complemento", length=100)
	private String endComplemento;

	@Column(name="end_logradouro", length=100)
	private String endLogradouro;

	@Column(name="end_logradouro_nr", length=10)
	private String endLogradouroNr;

	@Column(name="fis_dfe_ambiente", length=1)
	private String fisDfeAmbiente;

	@Column(name="fis_dfe_api_token", length=2147483647)
	private String fisDfeApiToken;

	@Column(name="fis_incent_cultura", length=1)
	private String fisIncentCultura;

	@Column(name="fis_incent_fiscal_nfs", length=1)
	private String fisIncentFiscalNfs;

	@Column(name="fis_provedor_nfs", length=1)
	private String fisProvedorNfs;

	@Column(name="fis_regime", length=50)
	private String fisRegime;

	@Column(name="fis_regime_trib_nfs", length=1)
	private String fisRegimeTribNfs;

	@Column(name="fone_1", length=100)
	private String fone1;

	@Column(name="fone_2", length=100)
	private String fone2;

	@Column(name="fone_3", length=100)
	private String fone3;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=255)
	private String logUserIns;

	@Column(name="log_user_upd", length=255)
	private String logUserUpd;

	@Column(nullable=false, length=100)
	private String nome;

	@Column(name="razao_social", nullable=false, length=100)
	private String razaoSocial;

	@Column(name="sigla_empresa", nullable=false, length=50)
	private String siglaEmpresa;

	//bi-directional many-to-one association to CtbLanc
	@OneToMany(mappedBy="gerEmpresa")
	private List<CtbLanc> ctbLancs;

	//bi-directional many-to-one association to FinConta
	@OneToMany(mappedBy="gerEmpresa")
	private List<FinConta> finContas;

	//bi-directional many-to-one association to FinLote
	@OneToMany(mappedBy="gerEmpresa")
	private List<FinLote> finLotes;

	//bi-directional many-to-one association to FinPagrec
	@OneToMany(mappedBy="gerEmpresa")
	private List<FinPagrec> finPagrecs;

	//bi-directional many-to-one association to FinPagrecBanco
	@OneToMany(mappedBy="gerEmpresa")
	private List<FinPagrecBanco> finPagrecBancos;

	//bi-directional many-to-one association to FinPagrecBancoTransf
	@OneToMany(mappedBy="gerEmpresa")
	private List<FinPagrecBancoTransf> finPagrecBancoTransfs;

	//bi-directional many-to-one association to FinPagrecPrev
	@OneToMany(mappedBy="gerEmpresa")
	private List<FinPagrecPrev> finPagrecPrevs;

	//bi-directional many-to-one association to FisDoc
	@OneToMany(mappedBy="gerEmpresa")
	private List<FisDoc> fisDocs;

	//bi-directional many-to-one association to FisCertificado
	@ManyToOne
	@JoinColumn(name="fis_certificado_id")
	private FisCertificado fisCertificado;

	//bi-directional many-to-one association to GerCidade
	@ManyToOne
	@JoinColumn(name="end_ger_cidade_id", nullable=false)
	private GerCidade gerCidade;

	//bi-directional many-to-one association to GerEmpresaGrupo
	@ManyToOne
	@JoinColumn(name="ger_empresa_grupo_id")
	private GerEmpresaGrupo gerEmpresaGrupo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to GerEmpresaParam
	@OneToMany(mappedBy="gerEmpresa")
	private List<GerEmpresaParam> gerEmpresaParams;

	//bi-directional many-to-one association to GerEmpresaPessoa
	@OneToMany(mappedBy="gerEmpresa")
	private List<GerEmpresaPessoa> gerEmpresaPessoas;

	//bi-directional many-to-one association to GerProcessoBloq
	@OneToMany(mappedBy="gerEmpresa")
	private List<GerProcessoBloq> gerProcessoBloqs;

	//bi-directional many-to-one association to IndVrAno
	@OneToMany(mappedBy="gerEmpresa")
	private List<IndVrAno> indVrAnos;

	//bi-directional many-to-one association to IndVrBimestre
	@OneToMany(mappedBy="gerEmpresa")
	private List<IndVrBimestre> indVrBimestres;

	//bi-directional many-to-one association to IndVrDia
	@OneToMany(mappedBy="gerEmpresa")
	private List<IndVrDia> indVrDias;

	//bi-directional many-to-one association to IndVrMe
	@OneToMany(mappedBy="gerEmpresa")
	private List<IndVrMes> indVrMes;

	//bi-directional many-to-one association to IndVrQuadrimestre
	@OneToMany(mappedBy="gerEmpresa")
	private List<IndVrQuadrimestre> indVrQuadrimestres;

	//bi-directional many-to-one association to IndVrQuinzena
	@OneToMany(mappedBy="gerEmpresa")
	private List<IndVrQuinzena> indVrQuinzenas;

	//bi-directional many-to-one association to IndVrSemana
	@OneToMany(mappedBy="gerEmpresa")
	private List<IndVrSemana> indVrSemanas;

	//bi-directional many-to-one association to IndVrSemestre
	@OneToMany(mappedBy="gerEmpresa")
	private List<IndVrSemestre> indVrSemestres;

	//bi-directional many-to-one association to IndVrTrimestre
	@OneToMany(mappedBy="gerEmpresa")
	private List<IndVrTrimestre> indVrTrimestres;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="gerEmpresa")
	private List<Mov> movs;

	//bi-directional many-to-one association to OpeCentro2Ord
	@OneToMany(mappedBy="gerEmpresa")
	private List<OpeCentro2Ord> opeCentro2Ords;

	//bi-directional many-to-one association to OpeCentro2ParamPer
	@OneToMany(mappedBy="gerEmpresa")
	private List<OpeCentro2ParamPer> opeCentro2ParamPers;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="gerEmpresa")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to OpeCentroPrev
	@OneToMany(mappedBy="gerEmpresa")
	private List<OpeCentroPrev> opeCentroPrevs;

	//bi-directional many-to-one association to OpeCentroRatFator
	@OneToMany(mappedBy="gerEmpresa")
	private List<OpeCentroRatFator> opeCentroRatFators;

	//bi-directional many-to-one association to OpeFrenteTrabalho
	@OneToMany(mappedBy="gerEmpresa")
	private List<OpeFrenteTrabalho> opeFrenteTrabalhos;

	//bi-directional many-to-one association to OpeOcorCompartMov
	@OneToMany(mappedBy="gerEmpresa")
	private List<OpeOcorCompartMov> opeOcorCompartMovs;

	//bi-directional many-to-one association to OpeOcorMov
	@OneToMany(mappedBy="gerEmpresa")
	private List<OpeOcorMov> opeOcorMovs;

	public GerEmpresa() {
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

	public String getContato1() {
		return this.contato1;
	}

	public void setContato1(String contato1) {
		this.contato1 = contato1;
	}

	public String getContato2() {
		return this.contato2;
	}

	public void setContato2(String contato2) {
		this.contato2 = contato2;
	}

	public String getContato3() {
		return this.contato3;
	}

	public void setContato3(String contato3) {
		this.contato3 = contato3;
	}

	public Date getDataAbertura() {
		return this.dataAbertura;
	}

	public void setDataAbertura(Date dataAbertura) {
		this.dataAbertura = dataAbertura;
	}

	public Date getDataValidadeA1() {
		return this.dataValidadeA1;
	}

	public void setDataValidadeA1(Date dataValidadeA1) {
		this.dataValidadeA1 = dataValidadeA1;
	}

	public Date getDataValidadeA3() {
		return this.dataValidadeA3;
	}

	public void setDataValidadeA3(Date dataValidadeA3) {
		this.dataValidadeA3 = dataValidadeA3;
	}

	public String getDocCnae() {
		return this.docCnae;
	}

	public void setDocCnae(String docCnae) {
		this.docCnae = docCnae;
	}

	public String getDocCnpj() {
		return this.docCnpj;
	}

	public void setDocCnpj(String docCnpj) {
		this.docCnpj = docCnpj;
	}

	public String getDocCpf() {
		return this.docCpf;
	}

	public void setDocCpf(String docCpf) {
		this.docCpf = docCpf;
	}

	public String getDocIe() {
		return this.docIe;
	}

	public void setDocIe(String docIe) {
		this.docIe = docIe;
	}

	public String getDocIm() {
		return this.docIm;
	}

	public void setDocIm(String docIm) {
		this.docIm = docIm;
	}

	public String getDocJunta() {
		return this.docJunta;
	}

	public void setDocJunta(String docJunta) {
		this.docJunta = docJunta;
	}

	public String getDocRntrc() {
		return this.docRntrc;
	}

	public void setDocRntrc(String docRntrc) {
		this.docRntrc = docRntrc;
	}

	public String getEmail1() {
		return this.email1;
	}

	public void setEmail1(String email1) {
		this.email1 = email1;
	}

	public String getEndBairro() {
		return this.endBairro;
	}

	public void setEndBairro(String endBairro) {
		this.endBairro = endBairro;
	}

	public String getEndCep() {
		return this.endCep;
	}

	public void setEndCep(String endCep) {
		this.endCep = endCep;
	}

	public String getEndComplemento() {
		return this.endComplemento;
	}

	public void setEndComplemento(String endComplemento) {
		this.endComplemento = endComplemento;
	}

	public String getEndLogradouro() {
		return this.endLogradouro;
	}

	public void setEndLogradouro(String endLogradouro) {
		this.endLogradouro = endLogradouro;
	}

	public String getEndLogradouroNr() {
		return this.endLogradouroNr;
	}

	public void setEndLogradouroNr(String endLogradouroNr) {
		this.endLogradouroNr = endLogradouroNr;
	}

	public String getFisDfeAmbiente() {
		return this.fisDfeAmbiente;
	}

	public void setFisDfeAmbiente(String fisDfeAmbiente) {
		this.fisDfeAmbiente = fisDfeAmbiente;
	}

	public String getFisDfeApiToken() {
		return this.fisDfeApiToken;
	}

	public void setFisDfeApiToken(String fisDfeApiToken) {
		this.fisDfeApiToken = fisDfeApiToken;
	}

	public String getFisIncentCultura() {
		return this.fisIncentCultura;
	}

	public void setFisIncentCultura(String fisIncentCultura) {
		this.fisIncentCultura = fisIncentCultura;
	}

	public String getFisIncentFiscalNfs() {
		return this.fisIncentFiscalNfs;
	}

	public void setFisIncentFiscalNfs(String fisIncentFiscalNfs) {
		this.fisIncentFiscalNfs = fisIncentFiscalNfs;
	}

	public String getFisProvedorNfs() {
		return this.fisProvedorNfs;
	}

	public void setFisProvedorNfs(String fisProvedorNfs) {
		this.fisProvedorNfs = fisProvedorNfs;
	}

	public String getFisRegime() {
		return this.fisRegime;
	}

	public void setFisRegime(String fisRegime) {
		this.fisRegime = fisRegime;
	}

	public String getFisRegimeTribNfs() {
		return this.fisRegimeTribNfs;
	}

	public void setFisRegimeTribNfs(String fisRegimeTribNfs) {
		this.fisRegimeTribNfs = fisRegimeTribNfs;
	}

	public String getFone1() {
		return this.fone1;
	}

	public void setFone1(String fone1) {
		this.fone1 = fone1;
	}

	public String getFone2() {
		return this.fone2;
	}

	public void setFone2(String fone2) {
		this.fone2 = fone2;
	}

	public String getFone3() {
		return this.fone3;
	}

	public void setFone3(String fone3) {
		this.fone3 = fone3;
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

	public String getRazaoSocial() {
		return this.razaoSocial;
	}

	public void setRazaoSocial(String razaoSocial) {
		this.razaoSocial = razaoSocial;
	}

	public String getSiglaEmpresa() {
		return this.siglaEmpresa;
	}

	public void setSiglaEmpresa(String siglaEmpresa) {
		this.siglaEmpresa = siglaEmpresa;
	}

	public List<CtbLanc> getCtbLancs() {
		return this.ctbLancs;
	}

	public void setCtbLancs(List<CtbLanc> ctbLancs) {
		this.ctbLancs = ctbLancs;
	}

	public CtbLanc addCtbLanc(CtbLanc ctbLanc) {
		getCtbLancs().add(ctbLanc);
		ctbLanc.setGerEmpresa(this);

		return ctbLanc;
	}

	public CtbLanc removeCtbLanc(CtbLanc ctbLanc) {
		getCtbLancs().remove(ctbLanc);
		ctbLanc.setGerEmpresa(null);

		return ctbLanc;
	}

	public List<FinConta> getFinContas() {
		return this.finContas;
	}

	public void setFinContas(List<FinConta> finContas) {
		this.finContas = finContas;
	}

	public FinConta addFinConta(FinConta finConta) {
		getFinContas().add(finConta);
		finConta.setGerEmpresa(this);

		return finConta;
	}

	public FinConta removeFinConta(FinConta finConta) {
		getFinContas().remove(finConta);
		finConta.setGerEmpresa(null);

		return finConta;
	}

	public List<FinLote> getFinLotes() {
		return this.finLotes;
	}

	public void setFinLotes(List<FinLote> finLotes) {
		this.finLotes = finLotes;
	}

	public FinLote addFinLote(FinLote finLote) {
		getFinLotes().add(finLote);
		finLote.setGerEmpresa(this);

		return finLote;
	}

	public FinLote removeFinLote(FinLote finLote) {
		getFinLotes().remove(finLote);
		finLote.setGerEmpresa(null);

		return finLote;
	}

	public List<FinPagrec> getFinPagrecs() {
		return this.finPagrecs;
	}

	public void setFinPagrecs(List<FinPagrec> finPagrecs) {
		this.finPagrecs = finPagrecs;
	}

	public FinPagrec addFinPagrec(FinPagrec finPagrec) {
		getFinPagrecs().add(finPagrec);
		finPagrec.setGerEmpresa(this);

		return finPagrec;
	}

	public FinPagrec removeFinPagrec(FinPagrec finPagrec) {
		getFinPagrecs().remove(finPagrec);
		finPagrec.setGerEmpresa(null);

		return finPagrec;
	}

	public List<FinPagrecBanco> getFinPagrecBancos() {
		return this.finPagrecBancos;
	}

	public void setFinPagrecBancos(List<FinPagrecBanco> finPagrecBancos) {
		this.finPagrecBancos = finPagrecBancos;
	}

	public FinPagrecBanco addFinPagrecBanco(FinPagrecBanco finPagrecBanco) {
		getFinPagrecBancos().add(finPagrecBanco);
		finPagrecBanco.setGerEmpresa(this);

		return finPagrecBanco;
	}

	public FinPagrecBanco removeFinPagrecBanco(FinPagrecBanco finPagrecBanco) {
		getFinPagrecBancos().remove(finPagrecBanco);
		finPagrecBanco.setGerEmpresa(null);

		return finPagrecBanco;
	}

	public List<FinPagrecBancoTransf> getFinPagrecBancoTransfs() {
		return this.finPagrecBancoTransfs;
	}

	public void setFinPagrecBancoTransfs(List<FinPagrecBancoTransf> finPagrecBancoTransfs) {
		this.finPagrecBancoTransfs = finPagrecBancoTransfs;
	}

	public FinPagrecBancoTransf addFinPagrecBancoTransf(FinPagrecBancoTransf finPagrecBancoTransf) {
		getFinPagrecBancoTransfs().add(finPagrecBancoTransf);
		finPagrecBancoTransf.setGerEmpresa(this);

		return finPagrecBancoTransf;
	}

	public FinPagrecBancoTransf removeFinPagrecBancoTransf(FinPagrecBancoTransf finPagrecBancoTransf) {
		getFinPagrecBancoTransfs().remove(finPagrecBancoTransf);
		finPagrecBancoTransf.setGerEmpresa(null);

		return finPagrecBancoTransf;
	}

	public List<FinPagrecPrev> getFinPagrecPrevs() {
		return this.finPagrecPrevs;
	}

	public void setFinPagrecPrevs(List<FinPagrecPrev> finPagrecPrevs) {
		this.finPagrecPrevs = finPagrecPrevs;
	}

	public FinPagrecPrev addFinPagrecPrev(FinPagrecPrev finPagrecPrev) {
		getFinPagrecPrevs().add(finPagrecPrev);
		finPagrecPrev.setGerEmpresa(this);

		return finPagrecPrev;
	}

	public FinPagrecPrev removeFinPagrecPrev(FinPagrecPrev finPagrecPrev) {
		getFinPagrecPrevs().remove(finPagrecPrev);
		finPagrecPrev.setGerEmpresa(null);

		return finPagrecPrev;
	}

	public List<FisDoc> getFisDocs() {
		return this.fisDocs;
	}

	public void setFisDocs(List<FisDoc> fisDocs) {
		this.fisDocs = fisDocs;
	}

	public FisDoc addFisDoc(FisDoc fisDoc) {
		getFisDocs().add(fisDoc);
		fisDoc.setGerEmpresa(this);

		return fisDoc;
	}

	public FisDoc removeFisDoc(FisDoc fisDoc) {
		getFisDocs().remove(fisDoc);
		fisDoc.setGerEmpresa(null);

		return fisDoc;
	}

	public FisCertificado getFisCertificado() {
		return this.fisCertificado;
	}

	public void setFisCertificado(FisCertificado fisCertificado) {
		this.fisCertificado = fisCertificado;
	}

	public GerCidade getGerCidade() {
		return this.gerCidade;
	}

	public void setGerCidade(GerCidade gerCidade) {
		this.gerCidade = gerCidade;
	}

	public GerEmpresaGrupo getGerEmpresaGrupo() {
		return this.gerEmpresaGrupo;
	}

	public void setGerEmpresaGrupo(GerEmpresaGrupo gerEmpresaGrupo) {
		this.gerEmpresaGrupo = gerEmpresaGrupo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<GerEmpresaParam> getGerEmpresaParams() {
		return this.gerEmpresaParams;
	}

	public void setGerEmpresaParams(List<GerEmpresaParam> gerEmpresaParams) {
		this.gerEmpresaParams = gerEmpresaParams;
	}

	public GerEmpresaParam addGerEmpresaParam(GerEmpresaParam gerEmpresaParam) {
		getGerEmpresaParams().add(gerEmpresaParam);
		gerEmpresaParam.setGerEmpresa(this);

		return gerEmpresaParam;
	}

	public GerEmpresaParam removeGerEmpresaParam(GerEmpresaParam gerEmpresaParam) {
		getGerEmpresaParams().remove(gerEmpresaParam);
		gerEmpresaParam.setGerEmpresa(null);

		return gerEmpresaParam;
	}

	public List<GerEmpresaPessoa> getGerEmpresaPessoas() {
		return this.gerEmpresaPessoas;
	}

	public void setGerEmpresaPessoas(List<GerEmpresaPessoa> gerEmpresaPessoas) {
		this.gerEmpresaPessoas = gerEmpresaPessoas;
	}

	public GerEmpresaPessoa addGerEmpresaPessoa(GerEmpresaPessoa gerEmpresaPessoa) {
		getGerEmpresaPessoas().add(gerEmpresaPessoa);
		gerEmpresaPessoa.setGerEmpresa(this);

		return gerEmpresaPessoa;
	}

	public GerEmpresaPessoa removeGerEmpresaPessoa(GerEmpresaPessoa gerEmpresaPessoa) {
		getGerEmpresaPessoas().remove(gerEmpresaPessoa);
		gerEmpresaPessoa.setGerEmpresa(null);

		return gerEmpresaPessoa;
	}

	public List<GerProcessoBloq> getGerProcessoBloqs() {
		return this.gerProcessoBloqs;
	}

	public void setGerProcessoBloqs(List<GerProcessoBloq> gerProcessoBloqs) {
		this.gerProcessoBloqs = gerProcessoBloqs;
	}

	public GerProcessoBloq addGerProcessoBloq(GerProcessoBloq gerProcessoBloq) {
		getGerProcessoBloqs().add(gerProcessoBloq);
		gerProcessoBloq.setGerEmpresa(this);

		return gerProcessoBloq;
	}

	public GerProcessoBloq removeGerProcessoBloq(GerProcessoBloq gerProcessoBloq) {
		getGerProcessoBloqs().remove(gerProcessoBloq);
		gerProcessoBloq.setGerEmpresa(null);

		return gerProcessoBloq;
	}

	public List<IndVrAno> getIndVrAnos() {
		return this.indVrAnos;
	}

	public void setIndVrAnos(List<IndVrAno> indVrAnos) {
		this.indVrAnos = indVrAnos;
	}

	public IndVrAno addIndVrAno(IndVrAno indVrAno) {
		getIndVrAnos().add(indVrAno);
		indVrAno.setGerEmpresa(this);

		return indVrAno;
	}

	public IndVrAno removeIndVrAno(IndVrAno indVrAno) {
		getIndVrAnos().remove(indVrAno);
		indVrAno.setGerEmpresa(null);

		return indVrAno;
	}

	public List<IndVrBimestre> getIndVrBimestres() {
		return this.indVrBimestres;
	}

	public void setIndVrBimestres(List<IndVrBimestre> indVrBimestres) {
		this.indVrBimestres = indVrBimestres;
	}

	public IndVrBimestre addIndVrBimestre(IndVrBimestre indVrBimestre) {
		getIndVrBimestres().add(indVrBimestre);
		indVrBimestre.setGerEmpresa(this);

		return indVrBimestre;
	}

	public IndVrBimestre removeIndVrBimestre(IndVrBimestre indVrBimestre) {
		getIndVrBimestres().remove(indVrBimestre);
		indVrBimestre.setGerEmpresa(null);

		return indVrBimestre;
	}

	public List<IndVrDia> getIndVrDias() {
		return this.indVrDias;
	}

	public void setIndVrDias(List<IndVrDia> indVrDias) {
		this.indVrDias = indVrDias;
	}

	public IndVrDia addIndVrDia(IndVrDia indVrDia) {
		getIndVrDias().add(indVrDia);
		indVrDia.setGerEmpresa(this);

		return indVrDia;
	}

	public IndVrDia removeIndVrDia(IndVrDia indVrDia) {
		getIndVrDias().remove(indVrDia);
		indVrDia.setGerEmpresa(null);

		return indVrDia;
	}

	public List<IndVrMes> getIndVrMes() {
		return this.indVrMes;
	}

	public void setIndVrMes(List<IndVrMes> indVrMes) {
		this.indVrMes = indVrMes;
	}

	public IndVrMes addIndVrMe(IndVrMes indVrMe) {
		getIndVrMes().add(indVrMe);
		indVrMe.setGerEmpresa(this);

		return indVrMe;
	}

	public IndVrMes removeIndVrMe(IndVrMes indVrMe) {
		getIndVrMes().remove(indVrMe);
		indVrMe.setGerEmpresa(null);

		return indVrMe;
	}

	public List<IndVrQuadrimestre> getIndVrQuadrimestres() {
		return this.indVrQuadrimestres;
	}

	public void setIndVrQuadrimestres(List<IndVrQuadrimestre> indVrQuadrimestres) {
		this.indVrQuadrimestres = indVrQuadrimestres;
	}

	public IndVrQuadrimestre addIndVrQuadrimestre(IndVrQuadrimestre indVrQuadrimestre) {
		getIndVrQuadrimestres().add(indVrQuadrimestre);
		indVrQuadrimestre.setGerEmpresa(this);

		return indVrQuadrimestre;
	}

	public IndVrQuadrimestre removeIndVrQuadrimestre(IndVrQuadrimestre indVrQuadrimestre) {
		getIndVrQuadrimestres().remove(indVrQuadrimestre);
		indVrQuadrimestre.setGerEmpresa(null);

		return indVrQuadrimestre;
	}

	public List<IndVrQuinzena> getIndVrQuinzenas() {
		return this.indVrQuinzenas;
	}

	public void setIndVrQuinzenas(List<IndVrQuinzena> indVrQuinzenas) {
		this.indVrQuinzenas = indVrQuinzenas;
	}

	public IndVrQuinzena addIndVrQuinzena(IndVrQuinzena indVrQuinzena) {
		getIndVrQuinzenas().add(indVrQuinzena);
		indVrQuinzena.setGerEmpresa(this);

		return indVrQuinzena;
	}

	public IndVrQuinzena removeIndVrQuinzena(IndVrQuinzena indVrQuinzena) {
		getIndVrQuinzenas().remove(indVrQuinzena);
		indVrQuinzena.setGerEmpresa(null);

		return indVrQuinzena;
	}

	public List<IndVrSemana> getIndVrSemanas() {
		return this.indVrSemanas;
	}

	public void setIndVrSemanas(List<IndVrSemana> indVrSemanas) {
		this.indVrSemanas = indVrSemanas;
	}

	public IndVrSemana addIndVrSemana(IndVrSemana indVrSemana) {
		getIndVrSemanas().add(indVrSemana);
		indVrSemana.setGerEmpresa(this);

		return indVrSemana;
	}

	public IndVrSemana removeIndVrSemana(IndVrSemana indVrSemana) {
		getIndVrSemanas().remove(indVrSemana);
		indVrSemana.setGerEmpresa(null);

		return indVrSemana;
	}

	public List<IndVrSemestre> getIndVrSemestres() {
		return this.indVrSemestres;
	}

	public void setIndVrSemestres(List<IndVrSemestre> indVrSemestres) {
		this.indVrSemestres = indVrSemestres;
	}

	public IndVrSemestre addIndVrSemestre(IndVrSemestre indVrSemestre) {
		getIndVrSemestres().add(indVrSemestre);
		indVrSemestre.setGerEmpresa(this);

		return indVrSemestre;
	}

	public IndVrSemestre removeIndVrSemestre(IndVrSemestre indVrSemestre) {
		getIndVrSemestres().remove(indVrSemestre);
		indVrSemestre.setGerEmpresa(null);

		return indVrSemestre;
	}

	public List<IndVrTrimestre> getIndVrTrimestres() {
		return this.indVrTrimestres;
	}

	public void setIndVrTrimestres(List<IndVrTrimestre> indVrTrimestres) {
		this.indVrTrimestres = indVrTrimestres;
	}

	public IndVrTrimestre addIndVrTrimestre(IndVrTrimestre indVrTrimestre) {
		getIndVrTrimestres().add(indVrTrimestre);
		indVrTrimestre.setGerEmpresa(this);

		return indVrTrimestre;
	}

	public IndVrTrimestre removeIndVrTrimestre(IndVrTrimestre indVrTrimestre) {
		getIndVrTrimestres().remove(indVrTrimestre);
		indVrTrimestre.setGerEmpresa(null);

		return indVrTrimestre;
	}

	public List<Mov> getMovs() {
		return this.movs;
	}

	public void setMovs(List<Mov> movs) {
		this.movs = movs;
	}

	public Mov addMov(Mov mov) {
		getMovs().add(mov);
		mov.setGerEmpresa(this);

		return mov;
	}

	public Mov removeMov(Mov mov) {
		getMovs().remove(mov);
		mov.setGerEmpresa(null);

		return mov;
	}

	public List<OpeCentro2Ord> getOpeCentro2Ords() {
		return this.opeCentro2Ords;
	}

	public void setOpeCentro2Ords(List<OpeCentro2Ord> opeCentro2Ords) {
		this.opeCentro2Ords = opeCentro2Ords;
	}

	public OpeCentro2Ord addOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().add(opeCentro2Ord);
		opeCentro2Ord.setGerEmpresa(this);

		return opeCentro2Ord;
	}

	public OpeCentro2Ord removeOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().remove(opeCentro2Ord);
		opeCentro2Ord.setGerEmpresa(null);

		return opeCentro2Ord;
	}

	public List<OpeCentro2ParamPer> getOpeCentro2ParamPers() {
		return this.opeCentro2ParamPers;
	}

	public void setOpeCentro2ParamPers(List<OpeCentro2ParamPer> opeCentro2ParamPers) {
		this.opeCentro2ParamPers = opeCentro2ParamPers;
	}

	public OpeCentro2ParamPer addOpeCentro2ParamPer(OpeCentro2ParamPer opeCentro2ParamPer) {
		getOpeCentro2ParamPers().add(opeCentro2ParamPer);
		opeCentro2ParamPer.setGerEmpresa(this);

		return opeCentro2ParamPer;
	}

	public OpeCentro2ParamPer removeOpeCentro2ParamPer(OpeCentro2ParamPer opeCentro2ParamPer) {
		getOpeCentro2ParamPers().remove(opeCentro2ParamPer);
		opeCentro2ParamPer.setGerEmpresa(null);

		return opeCentro2ParamPer;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setGerEmpresa(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setGerEmpresa(null);

		return opeCentroConfig;
	}

	public List<OpeCentroPrev> getOpeCentroPrevs() {
		return this.opeCentroPrevs;
	}

	public void setOpeCentroPrevs(List<OpeCentroPrev> opeCentroPrevs) {
		this.opeCentroPrevs = opeCentroPrevs;
	}

	public OpeCentroPrev addOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().add(opeCentroPrev);
		opeCentroPrev.setGerEmpresa(this);

		return opeCentroPrev;
	}

	public OpeCentroPrev removeOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().remove(opeCentroPrev);
		opeCentroPrev.setGerEmpresa(null);

		return opeCentroPrev;
	}

	public List<OpeCentroRatFator> getOpeCentroRatFators() {
		return this.opeCentroRatFators;
	}

	public void setOpeCentroRatFators(List<OpeCentroRatFator> opeCentroRatFators) {
		this.opeCentroRatFators = opeCentroRatFators;
	}

	public OpeCentroRatFator addOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().add(opeCentroRatFator);
		opeCentroRatFator.setGerEmpresa(this);

		return opeCentroRatFator;
	}

	public OpeCentroRatFator removeOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().remove(opeCentroRatFator);
		opeCentroRatFator.setGerEmpresa(null);

		return opeCentroRatFator;
	}

	public List<OpeFrenteTrabalho> getOpeFrenteTrabalhos() {
		return this.opeFrenteTrabalhos;
	}

	public void setOpeFrenteTrabalhos(List<OpeFrenteTrabalho> opeFrenteTrabalhos) {
		this.opeFrenteTrabalhos = opeFrenteTrabalhos;
	}

	public OpeFrenteTrabalho addOpeFrenteTrabalho(OpeFrenteTrabalho opeFrenteTrabalho) {
		getOpeFrenteTrabalhos().add(opeFrenteTrabalho);
		opeFrenteTrabalho.setGerEmpresa(this);

		return opeFrenteTrabalho;
	}

	public OpeFrenteTrabalho removeOpeFrenteTrabalho(OpeFrenteTrabalho opeFrenteTrabalho) {
		getOpeFrenteTrabalhos().remove(opeFrenteTrabalho);
		opeFrenteTrabalho.setGerEmpresa(null);

		return opeFrenteTrabalho;
	}

	public List<OpeOcorCompartMov> getOpeOcorCompartMovs() {
		return this.opeOcorCompartMovs;
	}

	public void setOpeOcorCompartMovs(List<OpeOcorCompartMov> opeOcorCompartMovs) {
		this.opeOcorCompartMovs = opeOcorCompartMovs;
	}

	public OpeOcorCompartMov addOpeOcorCompartMov(OpeOcorCompartMov opeOcorCompartMov) {
		getOpeOcorCompartMovs().add(opeOcorCompartMov);
		opeOcorCompartMov.setGerEmpresa(this);

		return opeOcorCompartMov;
	}

	public OpeOcorCompartMov removeOpeOcorCompartMov(OpeOcorCompartMov opeOcorCompartMov) {
		getOpeOcorCompartMovs().remove(opeOcorCompartMov);
		opeOcorCompartMov.setGerEmpresa(null);

		return opeOcorCompartMov;
	}

	public List<OpeOcorMov> getOpeOcorMovs() {
		return this.opeOcorMovs;
	}

	public void setOpeOcorMovs(List<OpeOcorMov> opeOcorMovs) {
		this.opeOcorMovs = opeOcorMovs;
	}

	public OpeOcorMov addOpeOcorMov(OpeOcorMov opeOcorMov) {
		getOpeOcorMovs().add(opeOcorMov);
		opeOcorMov.setGerEmpresa(this);

		return opeOcorMov;
	}

	public OpeOcorMov removeOpeOcorMov(OpeOcorMov opeOcorMov) {
		getOpeOcorMovs().remove(opeOcorMov);
		opeOcorMov.setGerEmpresa(null);

		return opeOcorMov;
	}

}