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
@Table(name="ger_pessoa")
@NamedQuery(name="GerPessoa.findAll", query="SELECT g FROM GerPessoa g")
public class GerPessoa implements Serializable {
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

	@Column(name="contrib_icms", nullable=false)
	private Integer contribIcms;

	@Column(name="data_abertura", length=50)
	private String dataAbertura;

	@Temporal(TemporalType.DATE)
	@Column(name="data_valid")
	private Date dataValid;

	@Column(name="doc_cnae", length=50)
	private String docCnae;

	@Column(name="doc_cnpj", length=50)
	private String docCnpj;

	@Column(name="doc_cpf", length=50)
	private String docCpf;

	@Column(name="doc_crc", length=50)
	private String docCrc;

	@Column(name="doc_crc_org_exp", length=50)
	private String docCrcOrgExp;

	@Column(name="doc_crc_seq", length=50)
	private String docCrcSeq;

	@Column(name="doc_ie", length=50)
	private String docIe;

	@Column(name="doc_im", length=50)
	private String docIm;

	@Column(name="doc_junta", length=50)
	private String docJunta;

	@Column(name="doc_rg", length=50)
	private String docRg;

	@Column(name="doc_rg_org_exp", length=50)
	private String docRgOrgExp;

	@Column(name="doc_taf", length=50)
	private String docTaf;

	@Column(name="fis_regime", length=50)
	private String fisRegime;

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

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(nullable=false, length=100)
	private String nome;

	@Column(name="nr_registro_est_cte", length=50)
	private String nrRegistroEstCte;

	@Column(name="nr_rntrc", length=8)
	private String nrRntrc;

	@Column(name="razao_social", nullable=false, length=100)
	private String razaoSocial;

	@Column(name="sigla_pes", length=50)
	private String siglaPes;

	//bi-directional many-to-one association to FinPagrec
	@OneToMany(mappedBy="gerPessoa1")
	private List<FinPagrec> finPagrecs1;

	//bi-directional many-to-one association to FinPagrec
	@OneToMany(mappedBy="gerPessoa2")
	private List<FinPagrec> finPagrecs2;

	//bi-directional many-to-one association to FinPagrecPrev
	@OneToMany(mappedBy="gerPessoa")
	private List<FinPagrecPrev> finPagrecPrevs;

	//bi-directional many-to-one association to GerEmpresaPessoa
	@OneToMany(mappedBy="gerPessoa")
	private List<GerEmpresaPessoa> gerEmpresaPessoas;

	//bi-directional many-to-one association to GerItemservPessoa
	@OneToMany(mappedBy="gerPessoa")
	private List<GerItemservPessoa> gerItemservPessoas;

	//bi-directional many-to-one association to GerMarcaPessoa
	@OneToMany(mappedBy="gerPessoa")
	private List<GerMarcaPessoa> gerMarcaPessoas;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to GerPessoaContaBanco
	@OneToMany(mappedBy="gerPessoa")
	private List<GerPessoaContaBanco> gerPessoaContaBancos;

	//bi-directional many-to-one association to GerPessoaEndereco
	@OneToMany(mappedBy="gerPessoa")
	private List<GerPessoaEndereco> gerPessoaEnderecos;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="gerPessoa")
	private List<Mov> movs;

	//bi-directional many-to-one association to MovCiot
	@OneToMany(mappedBy="gerPessoa")
	private List<MovCiot> movCiots;

	//bi-directional many-to-one association to MovCondutor
	@OneToMany(mappedBy="gerPessoa")
	private List<MovCondutor> movCondutors;

	//bi-directional many-to-one association to MovCotacao
	@OneToMany(mappedBy="gerPessoa")
	private List<MovCotacao> movCotacaos;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoa1")
	private List<MovCotacaoAnal> movCotacaoAnals1;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoa2")
	private List<MovCotacaoAnal> movCotacaoAnals2;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoa3")
	private List<MovCotacaoAnal> movCotacaoAnals3;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoa4")
	private List<MovCotacaoAnal> movCotacaoAnals4;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoa5")
	private List<MovCotacaoAnal> movCotacaoAnals5;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoa6")
	private List<MovCotacaoAnal> movCotacaoAnals6;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoa7")
	private List<MovCotacaoAnal> movCotacaoAnals7;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoa8")
	private List<MovCotacaoAnal> movCotacaoAnals8;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoa9")
	private List<MovCotacaoAnal> movCotacaoAnals9;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoa10")
	private List<MovCotacaoAnal> movCotacaoAnals10;

	//bi-directional many-to-one association to MovPedagio
	@OneToMany(mappedBy="gerPessoa1")
	private List<MovPedagio> movPedagios1;

	//bi-directional many-to-one association to MovPedagio
	@OneToMany(mappedBy="gerPessoa2")
	private List<MovPedagio> movPedagios2;

	//bi-directional many-to-one association to MovSeguradora
	@OneToMany(mappedBy="gerPessoa1")
	private List<MovSeguradora> movSeguradoras1;

	//bi-directional many-to-one association to MovSeguradora
	@OneToMany(mappedBy="gerPessoa2")
	private List<MovSeguradora> movSeguradoras2;

	//bi-directional many-to-one association to MovTomador
	@OneToMany(mappedBy="gerPessoa")
	private List<MovTomador> movTomadors;

	//bi-directional many-to-one association to OpeCentro1
	@OneToMany(mappedBy="gerPessoa")
	private List<OpeCentro1> opeCentro1s;

	//bi-directional many-to-one association to SysDocument
	@OneToMany(mappedBy="gerPessoa")
	private List<SysDocument> sysDocuments;

	public GerPessoa() {
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

	public Integer getContribIcms() {
		return this.contribIcms;
	}

	public void setContribIcms(Integer contribIcms) {
		this.contribIcms = contribIcms;
	}

	public String getDataAbertura() {
		return this.dataAbertura;
	}

	public void setDataAbertura(String dataAbertura) {
		this.dataAbertura = dataAbertura;
	}

	public Date getDataValid() {
		return this.dataValid;
	}

	public void setDataValid(Date dataValid) {
		this.dataValid = dataValid;
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

	public String getDocCrc() {
		return this.docCrc;
	}

	public void setDocCrc(String docCrc) {
		this.docCrc = docCrc;
	}

	public String getDocCrcOrgExp() {
		return this.docCrcOrgExp;
	}

	public void setDocCrcOrgExp(String docCrcOrgExp) {
		this.docCrcOrgExp = docCrcOrgExp;
	}

	public String getDocCrcSeq() {
		return this.docCrcSeq;
	}

	public void setDocCrcSeq(String docCrcSeq) {
		this.docCrcSeq = docCrcSeq;
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

	public String getDocRg() {
		return this.docRg;
	}

	public void setDocRg(String docRg) {
		this.docRg = docRg;
	}

	public String getDocRgOrgExp() {
		return this.docRgOrgExp;
	}

	public void setDocRgOrgExp(String docRgOrgExp) {
		this.docRgOrgExp = docRgOrgExp;
	}

	public String getDocTaf() {
		return this.docTaf;
	}

	public void setDocTaf(String docTaf) {
		this.docTaf = docTaf;
	}

	public String getFisRegime() {
		return this.fisRegime;
	}

	public void setFisRegime(String fisRegime) {
		this.fisRegime = fisRegime;
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

	public String getNrRegistroEstCte() {
		return this.nrRegistroEstCte;
	}

	public void setNrRegistroEstCte(String nrRegistroEstCte) {
		this.nrRegistroEstCte = nrRegistroEstCte;
	}

	public String getNrRntrc() {
		return this.nrRntrc;
	}

	public void setNrRntrc(String nrRntrc) {
		this.nrRntrc = nrRntrc;
	}

	public String getRazaoSocial() {
		return this.razaoSocial;
	}

	public void setRazaoSocial(String razaoSocial) {
		this.razaoSocial = razaoSocial;
	}

	public String getSiglaPes() {
		return this.siglaPes;
	}

	public void setSiglaPes(String siglaPes) {
		this.siglaPes = siglaPes;
	}

	public List<FinPagrec> getFinPagrecs1() {
		return this.finPagrecs1;
	}

	public void setFinPagrecs1(List<FinPagrec> finPagrecs1) {
		this.finPagrecs1 = finPagrecs1;
	}

	public FinPagrec addFinPagrecs1(FinPagrec finPagrecs1) {
		getFinPagrecs1().add(finPagrecs1);
		finPagrecs1.setGerPessoa1(this);

		return finPagrecs1;
	}

	public FinPagrec removeFinPagrecs1(FinPagrec finPagrecs1) {
		getFinPagrecs1().remove(finPagrecs1);
		finPagrecs1.setGerPessoa1(null);

		return finPagrecs1;
	}

	public List<FinPagrec> getFinPagrecs2() {
		return this.finPagrecs2;
	}

	public void setFinPagrecs2(List<FinPagrec> finPagrecs2) {
		this.finPagrecs2 = finPagrecs2;
	}

	public FinPagrec addFinPagrecs2(FinPagrec finPagrecs2) {
		getFinPagrecs2().add(finPagrecs2);
		finPagrecs2.setGerPessoa2(this);

		return finPagrecs2;
	}

	public FinPagrec removeFinPagrecs2(FinPagrec finPagrecs2) {
		getFinPagrecs2().remove(finPagrecs2);
		finPagrecs2.setGerPessoa2(null);

		return finPagrecs2;
	}

	public List<FinPagrecPrev> getFinPagrecPrevs() {
		return this.finPagrecPrevs;
	}

	public void setFinPagrecPrevs(List<FinPagrecPrev> finPagrecPrevs) {
		this.finPagrecPrevs = finPagrecPrevs;
	}

	public FinPagrecPrev addFinPagrecPrev(FinPagrecPrev finPagrecPrev) {
		getFinPagrecPrevs().add(finPagrecPrev);
		finPagrecPrev.setGerPessoa(this);

		return finPagrecPrev;
	}

	public FinPagrecPrev removeFinPagrecPrev(FinPagrecPrev finPagrecPrev) {
		getFinPagrecPrevs().remove(finPagrecPrev);
		finPagrecPrev.setGerPessoa(null);

		return finPagrecPrev;
	}

	public List<GerEmpresaPessoa> getGerEmpresaPessoas() {
		return this.gerEmpresaPessoas;
	}

	public void setGerEmpresaPessoas(List<GerEmpresaPessoa> gerEmpresaPessoas) {
		this.gerEmpresaPessoas = gerEmpresaPessoas;
	}

	public GerEmpresaPessoa addGerEmpresaPessoa(GerEmpresaPessoa gerEmpresaPessoa) {
		getGerEmpresaPessoas().add(gerEmpresaPessoa);
		gerEmpresaPessoa.setGerPessoa(this);

		return gerEmpresaPessoa;
	}

	public GerEmpresaPessoa removeGerEmpresaPessoa(GerEmpresaPessoa gerEmpresaPessoa) {
		getGerEmpresaPessoas().remove(gerEmpresaPessoa);
		gerEmpresaPessoa.setGerPessoa(null);

		return gerEmpresaPessoa;
	}

	public List<GerItemservPessoa> getGerItemservPessoas() {
		return this.gerItemservPessoas;
	}

	public void setGerItemservPessoas(List<GerItemservPessoa> gerItemservPessoas) {
		this.gerItemservPessoas = gerItemservPessoas;
	}

	public GerItemservPessoa addGerItemservPessoa(GerItemservPessoa gerItemservPessoa) {
		getGerItemservPessoas().add(gerItemservPessoa);
		gerItemservPessoa.setGerPessoa(this);

		return gerItemservPessoa;
	}

	public GerItemservPessoa removeGerItemservPessoa(GerItemservPessoa gerItemservPessoa) {
		getGerItemservPessoas().remove(gerItemservPessoa);
		gerItemservPessoa.setGerPessoa(null);

		return gerItemservPessoa;
	}

	public List<GerMarcaPessoa> getGerMarcaPessoas() {
		return this.gerMarcaPessoas;
	}

	public void setGerMarcaPessoas(List<GerMarcaPessoa> gerMarcaPessoas) {
		this.gerMarcaPessoas = gerMarcaPessoas;
	}

	public GerMarcaPessoa addGerMarcaPessoa(GerMarcaPessoa gerMarcaPessoa) {
		getGerMarcaPessoas().add(gerMarcaPessoa);
		gerMarcaPessoa.setGerPessoa(this);

		return gerMarcaPessoa;
	}

	public GerMarcaPessoa removeGerMarcaPessoa(GerMarcaPessoa gerMarcaPessoa) {
		getGerMarcaPessoas().remove(gerMarcaPessoa);
		gerMarcaPessoa.setGerPessoa(null);

		return gerMarcaPessoa;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<GerPessoaContaBanco> getGerPessoaContaBancos() {
		return this.gerPessoaContaBancos;
	}

	public void setGerPessoaContaBancos(List<GerPessoaContaBanco> gerPessoaContaBancos) {
		this.gerPessoaContaBancos = gerPessoaContaBancos;
	}

	public GerPessoaContaBanco addGerPessoaContaBanco(GerPessoaContaBanco gerPessoaContaBanco) {
		getGerPessoaContaBancos().add(gerPessoaContaBanco);
		gerPessoaContaBanco.setGerPessoa(this);

		return gerPessoaContaBanco;
	}

	public GerPessoaContaBanco removeGerPessoaContaBanco(GerPessoaContaBanco gerPessoaContaBanco) {
		getGerPessoaContaBancos().remove(gerPessoaContaBanco);
		gerPessoaContaBanco.setGerPessoa(null);

		return gerPessoaContaBanco;
	}

	public List<GerPessoaEndereco> getGerPessoaEnderecos() {
		return this.gerPessoaEnderecos;
	}

	public void setGerPessoaEnderecos(List<GerPessoaEndereco> gerPessoaEnderecos) {
		this.gerPessoaEnderecos = gerPessoaEnderecos;
	}

	public GerPessoaEndereco addGerPessoaEndereco(GerPessoaEndereco gerPessoaEndereco) {
		getGerPessoaEnderecos().add(gerPessoaEndereco);
		gerPessoaEndereco.setGerPessoa(this);

		return gerPessoaEndereco;
	}

	public GerPessoaEndereco removeGerPessoaEndereco(GerPessoaEndereco gerPessoaEndereco) {
		getGerPessoaEnderecos().remove(gerPessoaEndereco);
		gerPessoaEndereco.setGerPessoa(null);

		return gerPessoaEndereco;
	}

	public List<Mov> getMovs() {
		return this.movs;
	}

	public void setMovs(List<Mov> movs) {
		this.movs = movs;
	}

	public Mov addMov(Mov mov) {
		getMovs().add(mov);
		mov.setGerPessoa(this);

		return mov;
	}

	public Mov removeMov(Mov mov) {
		getMovs().remove(mov);
		mov.setGerPessoa(null);

		return mov;
	}

	public List<MovCiot> getMovCiots() {
		return this.movCiots;
	}

	public void setMovCiots(List<MovCiot> movCiots) {
		this.movCiots = movCiots;
	}

	public MovCiot addMovCiot(MovCiot movCiot) {
		getMovCiots().add(movCiot);
		movCiot.setGerPessoa(this);

		return movCiot;
	}

	public MovCiot removeMovCiot(MovCiot movCiot) {
		getMovCiots().remove(movCiot);
		movCiot.setGerPessoa(null);

		return movCiot;
	}

	public List<MovCondutor> getMovCondutors() {
		return this.movCondutors;
	}

	public void setMovCondutors(List<MovCondutor> movCondutors) {
		this.movCondutors = movCondutors;
	}

	public MovCondutor addMovCondutor(MovCondutor movCondutor) {
		getMovCondutors().add(movCondutor);
		movCondutor.setGerPessoa(this);

		return movCondutor;
	}

	public MovCondutor removeMovCondutor(MovCondutor movCondutor) {
		getMovCondutors().remove(movCondutor);
		movCondutor.setGerPessoa(null);

		return movCondutor;
	}

	public List<MovCotacao> getMovCotacaos() {
		return this.movCotacaos;
	}

	public void setMovCotacaos(List<MovCotacao> movCotacaos) {
		this.movCotacaos = movCotacaos;
	}

	public MovCotacao addMovCotacao(MovCotacao movCotacao) {
		getMovCotacaos().add(movCotacao);
		movCotacao.setGerPessoa(this);

		return movCotacao;
	}

	public MovCotacao removeMovCotacao(MovCotacao movCotacao) {
		getMovCotacaos().remove(movCotacao);
		movCotacao.setGerPessoa(null);

		return movCotacao;
	}

	public List<MovCotacaoAnal> getMovCotacaoAnals1() {
		return this.movCotacaoAnals1;
	}

	public void setMovCotacaoAnals1(List<MovCotacaoAnal> movCotacaoAnals1) {
		this.movCotacaoAnals1 = movCotacaoAnals1;
	}

	public MovCotacaoAnal addMovCotacaoAnals1(MovCotacaoAnal movCotacaoAnals1) {
		getMovCotacaoAnals1().add(movCotacaoAnals1);
		movCotacaoAnals1.setGerPessoa1(this);

		return movCotacaoAnals1;
	}

	public MovCotacaoAnal removeMovCotacaoAnals1(MovCotacaoAnal movCotacaoAnals1) {
		getMovCotacaoAnals1().remove(movCotacaoAnals1);
		movCotacaoAnals1.setGerPessoa1(null);

		return movCotacaoAnals1;
	}

	public List<MovCotacaoAnal> getMovCotacaoAnals2() {
		return this.movCotacaoAnals2;
	}

	public void setMovCotacaoAnals2(List<MovCotacaoAnal> movCotacaoAnals2) {
		this.movCotacaoAnals2 = movCotacaoAnals2;
	}

	public MovCotacaoAnal addMovCotacaoAnals2(MovCotacaoAnal movCotacaoAnals2) {
		getMovCotacaoAnals2().add(movCotacaoAnals2);
		movCotacaoAnals2.setGerPessoa2(this);

		return movCotacaoAnals2;
	}

	public MovCotacaoAnal removeMovCotacaoAnals2(MovCotacaoAnal movCotacaoAnals2) {
		getMovCotacaoAnals2().remove(movCotacaoAnals2);
		movCotacaoAnals2.setGerPessoa2(null);

		return movCotacaoAnals2;
	}

	public List<MovCotacaoAnal> getMovCotacaoAnals3() {
		return this.movCotacaoAnals3;
	}

	public void setMovCotacaoAnals3(List<MovCotacaoAnal> movCotacaoAnals3) {
		this.movCotacaoAnals3 = movCotacaoAnals3;
	}

	public MovCotacaoAnal addMovCotacaoAnals3(MovCotacaoAnal movCotacaoAnals3) {
		getMovCotacaoAnals3().add(movCotacaoAnals3);
		movCotacaoAnals3.setGerPessoa3(this);

		return movCotacaoAnals3;
	}

	public MovCotacaoAnal removeMovCotacaoAnals3(MovCotacaoAnal movCotacaoAnals3) {
		getMovCotacaoAnals3().remove(movCotacaoAnals3);
		movCotacaoAnals3.setGerPessoa3(null);

		return movCotacaoAnals3;
	}

	public List<MovCotacaoAnal> getMovCotacaoAnals4() {
		return this.movCotacaoAnals4;
	}

	public void setMovCotacaoAnals4(List<MovCotacaoAnal> movCotacaoAnals4) {
		this.movCotacaoAnals4 = movCotacaoAnals4;
	}

	public MovCotacaoAnal addMovCotacaoAnals4(MovCotacaoAnal movCotacaoAnals4) {
		getMovCotacaoAnals4().add(movCotacaoAnals4);
		movCotacaoAnals4.setGerPessoa4(this);

		return movCotacaoAnals4;
	}

	public MovCotacaoAnal removeMovCotacaoAnals4(MovCotacaoAnal movCotacaoAnals4) {
		getMovCotacaoAnals4().remove(movCotacaoAnals4);
		movCotacaoAnals4.setGerPessoa4(null);

		return movCotacaoAnals4;
	}

	public List<MovCotacaoAnal> getMovCotacaoAnals5() {
		return this.movCotacaoAnals5;
	}

	public void setMovCotacaoAnals5(List<MovCotacaoAnal> movCotacaoAnals5) {
		this.movCotacaoAnals5 = movCotacaoAnals5;
	}

	public MovCotacaoAnal addMovCotacaoAnals5(MovCotacaoAnal movCotacaoAnals5) {
		getMovCotacaoAnals5().add(movCotacaoAnals5);
		movCotacaoAnals5.setGerPessoa5(this);

		return movCotacaoAnals5;
	}

	public MovCotacaoAnal removeMovCotacaoAnals5(MovCotacaoAnal movCotacaoAnals5) {
		getMovCotacaoAnals5().remove(movCotacaoAnals5);
		movCotacaoAnals5.setGerPessoa5(null);

		return movCotacaoAnals5;
	}

	public List<MovCotacaoAnal> getMovCotacaoAnals6() {
		return this.movCotacaoAnals6;
	}

	public void setMovCotacaoAnals6(List<MovCotacaoAnal> movCotacaoAnals6) {
		this.movCotacaoAnals6 = movCotacaoAnals6;
	}

	public MovCotacaoAnal addMovCotacaoAnals6(MovCotacaoAnal movCotacaoAnals6) {
		getMovCotacaoAnals6().add(movCotacaoAnals6);
		movCotacaoAnals6.setGerPessoa6(this);

		return movCotacaoAnals6;
	}

	public MovCotacaoAnal removeMovCotacaoAnals6(MovCotacaoAnal movCotacaoAnals6) {
		getMovCotacaoAnals6().remove(movCotacaoAnals6);
		movCotacaoAnals6.setGerPessoa6(null);

		return movCotacaoAnals6;
	}

	public List<MovCotacaoAnal> getMovCotacaoAnals7() {
		return this.movCotacaoAnals7;
	}

	public void setMovCotacaoAnals7(List<MovCotacaoAnal> movCotacaoAnals7) {
		this.movCotacaoAnals7 = movCotacaoAnals7;
	}

	public MovCotacaoAnal addMovCotacaoAnals7(MovCotacaoAnal movCotacaoAnals7) {
		getMovCotacaoAnals7().add(movCotacaoAnals7);
		movCotacaoAnals7.setGerPessoa7(this);

		return movCotacaoAnals7;
	}

	public MovCotacaoAnal removeMovCotacaoAnals7(MovCotacaoAnal movCotacaoAnals7) {
		getMovCotacaoAnals7().remove(movCotacaoAnals7);
		movCotacaoAnals7.setGerPessoa7(null);

		return movCotacaoAnals7;
	}

	public List<MovCotacaoAnal> getMovCotacaoAnals8() {
		return this.movCotacaoAnals8;
	}

	public void setMovCotacaoAnals8(List<MovCotacaoAnal> movCotacaoAnals8) {
		this.movCotacaoAnals8 = movCotacaoAnals8;
	}

	public MovCotacaoAnal addMovCotacaoAnals8(MovCotacaoAnal movCotacaoAnals8) {
		getMovCotacaoAnals8().add(movCotacaoAnals8);
		movCotacaoAnals8.setGerPessoa8(this);

		return movCotacaoAnals8;
	}

	public MovCotacaoAnal removeMovCotacaoAnals8(MovCotacaoAnal movCotacaoAnals8) {
		getMovCotacaoAnals8().remove(movCotacaoAnals8);
		movCotacaoAnals8.setGerPessoa8(null);

		return movCotacaoAnals8;
	}

	public List<MovCotacaoAnal> getMovCotacaoAnals9() {
		return this.movCotacaoAnals9;
	}

	public void setMovCotacaoAnals9(List<MovCotacaoAnal> movCotacaoAnals9) {
		this.movCotacaoAnals9 = movCotacaoAnals9;
	}

	public MovCotacaoAnal addMovCotacaoAnals9(MovCotacaoAnal movCotacaoAnals9) {
		getMovCotacaoAnals9().add(movCotacaoAnals9);
		movCotacaoAnals9.setGerPessoa9(this);

		return movCotacaoAnals9;
	}

	public MovCotacaoAnal removeMovCotacaoAnals9(MovCotacaoAnal movCotacaoAnals9) {
		getMovCotacaoAnals9().remove(movCotacaoAnals9);
		movCotacaoAnals9.setGerPessoa9(null);

		return movCotacaoAnals9;
	}

	public List<MovCotacaoAnal> getMovCotacaoAnals10() {
		return this.movCotacaoAnals10;
	}

	public void setMovCotacaoAnals10(List<MovCotacaoAnal> movCotacaoAnals10) {
		this.movCotacaoAnals10 = movCotacaoAnals10;
	}

	public MovCotacaoAnal addMovCotacaoAnals10(MovCotacaoAnal movCotacaoAnals10) {
		getMovCotacaoAnals10().add(movCotacaoAnals10);
		movCotacaoAnals10.setGerPessoa10(this);

		return movCotacaoAnals10;
	}

	public MovCotacaoAnal removeMovCotacaoAnals10(MovCotacaoAnal movCotacaoAnals10) {
		getMovCotacaoAnals10().remove(movCotacaoAnals10);
		movCotacaoAnals10.setGerPessoa10(null);

		return movCotacaoAnals10;
	}

	public List<MovPedagio> getMovPedagios1() {
		return this.movPedagios1;
	}

	public void setMovPedagios1(List<MovPedagio> movPedagios1) {
		this.movPedagios1 = movPedagios1;
	}

	public MovPedagio addMovPedagios1(MovPedagio movPedagios1) {
		getMovPedagios1().add(movPedagios1);
		movPedagios1.setGerPessoa1(this);

		return movPedagios1;
	}

	public MovPedagio removeMovPedagios1(MovPedagio movPedagios1) {
		getMovPedagios1().remove(movPedagios1);
		movPedagios1.setGerPessoa1(null);

		return movPedagios1;
	}

	public List<MovPedagio> getMovPedagios2() {
		return this.movPedagios2;
	}

	public void setMovPedagios2(List<MovPedagio> movPedagios2) {
		this.movPedagios2 = movPedagios2;
	}

	public MovPedagio addMovPedagios2(MovPedagio movPedagios2) {
		getMovPedagios2().add(movPedagios2);
		movPedagios2.setGerPessoa2(this);

		return movPedagios2;
	}

	public MovPedagio removeMovPedagios2(MovPedagio movPedagios2) {
		getMovPedagios2().remove(movPedagios2);
		movPedagios2.setGerPessoa2(null);

		return movPedagios2;
	}

	public List<MovSeguradora> getMovSeguradoras1() {
		return this.movSeguradoras1;
	}

	public void setMovSeguradoras1(List<MovSeguradora> movSeguradoras1) {
		this.movSeguradoras1 = movSeguradoras1;
	}

	public MovSeguradora addMovSeguradoras1(MovSeguradora movSeguradoras1) {
		getMovSeguradoras1().add(movSeguradoras1);
		movSeguradoras1.setGerPessoa1(this);

		return movSeguradoras1;
	}

	public MovSeguradora removeMovSeguradoras1(MovSeguradora movSeguradoras1) {
		getMovSeguradoras1().remove(movSeguradoras1);
		movSeguradoras1.setGerPessoa1(null);

		return movSeguradoras1;
	}

	public List<MovSeguradora> getMovSeguradoras2() {
		return this.movSeguradoras2;
	}

	public void setMovSeguradoras2(List<MovSeguradora> movSeguradoras2) {
		this.movSeguradoras2 = movSeguradoras2;
	}

	public MovSeguradora addMovSeguradoras2(MovSeguradora movSeguradoras2) {
		getMovSeguradoras2().add(movSeguradoras2);
		movSeguradoras2.setGerPessoa2(this);

		return movSeguradoras2;
	}

	public MovSeguradora removeMovSeguradoras2(MovSeguradora movSeguradoras2) {
		getMovSeguradoras2().remove(movSeguradoras2);
		movSeguradoras2.setGerPessoa2(null);

		return movSeguradoras2;
	}

	public List<MovTomador> getMovTomadors() {
		return this.movTomadors;
	}

	public void setMovTomadors(List<MovTomador> movTomadors) {
		this.movTomadors = movTomadors;
	}

	public MovTomador addMovTomador(MovTomador movTomador) {
		getMovTomadors().add(movTomador);
		movTomador.setGerPessoa(this);

		return movTomador;
	}

	public MovTomador removeMovTomador(MovTomador movTomador) {
		getMovTomadors().remove(movTomador);
		movTomador.setGerPessoa(null);

		return movTomador;
	}

	public List<OpeCentro1> getOpeCentro1s() {
		return this.opeCentro1s;
	}

	public void setOpeCentro1s(List<OpeCentro1> opeCentro1s) {
		this.opeCentro1s = opeCentro1s;
	}

	public OpeCentro1 addOpeCentro1(OpeCentro1 opeCentro1) {
		getOpeCentro1s().add(opeCentro1);
		opeCentro1.setGerPessoa(this);

		return opeCentro1;
	}

	public OpeCentro1 removeOpeCentro1(OpeCentro1 opeCentro1) {
		getOpeCentro1s().remove(opeCentro1);
		opeCentro1.setGerPessoa(null);

		return opeCentro1;
	}

	public List<SysDocument> getSysDocuments() {
		return this.sysDocuments;
	}

	public void setSysDocuments(List<SysDocument> sysDocuments) {
		this.sysDocuments = sysDocuments;
	}

	public SysDocument addSysDocument(SysDocument sysDocument) {
		getSysDocuments().add(sysDocument);
		sysDocument.setGerPessoa(this);

		return sysDocument;
	}

	public SysDocument removeSysDocument(SysDocument sysDocument) {
		getSysDocuments().remove(sysDocument);
		sysDocument.setGerPessoa(null);

		return sysDocument;
	}

}