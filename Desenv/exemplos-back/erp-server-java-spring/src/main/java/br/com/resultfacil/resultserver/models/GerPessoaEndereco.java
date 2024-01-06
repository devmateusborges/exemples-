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
@Table(name="ger_pessoa_endereco")
@NamedQuery(name="GerPessoaEndereco.findAll", query="SELECT g FROM GerPessoaEndereco g")
public class GerPessoaEndereco implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(length=100)
	private String contato;

	@Column(length=100)
	private String email;

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

	@Column(length=100)
	private String fone;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(nullable=false, length=1)
	private String padrao;

	@Column(nullable=false, length=1)
	private String tipo;

	//bi-directional many-to-one association to FisTributacao
	@OneToMany(mappedBy="gerPessoaEndereco")
	private List<FisTributacao> fisTributacaos;

	//bi-directional many-to-one association to GerCidade
	@ManyToOne
	@JoinColumn(name="end_ger_cidade_id", nullable=false)
	private GerCidade gerCidade;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="ger_pessoa_id", nullable=false)
	private GerPessoa gerPessoa;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="gerPessoaEndereco1")
	private List<Mov> movs1;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="gerPessoaEndereco2")
	private List<Mov> movs2;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="gerPessoaEndereco3")
	private List<Mov> movs3;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="gerPessoaEndereco4")
	private List<Mov> movs4;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="gerPessoaEndereco5")
	private List<Mov> movs5;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="gerPessoaEndereco6")
	private List<Mov> movs6;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="gerPessoaEndereco7")
	private List<Mov> movs7;

	//bi-directional many-to-one association to MovCotacao
	@OneToMany(mappedBy="gerPessoaEndereco")
	private List<MovCotacao> movCotacaos;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoaEndereco1")
	private List<MovCotacaoAnal> movCotacaoAnals1;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoaEndereco2")
	private List<MovCotacaoAnal> movCotacaoAnals2;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoaEndereco3")
	private List<MovCotacaoAnal> movCotacaoAnals3;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoaEndereco4")
	private List<MovCotacaoAnal> movCotacaoAnals4;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoaEndereco5")
	private List<MovCotacaoAnal> movCotacaoAnals5;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoaEndereco6")
	private List<MovCotacaoAnal> movCotacaoAnals6;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoaEndereco7")
	private List<MovCotacaoAnal> movCotacaoAnals7;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoaEndereco8")
	private List<MovCotacaoAnal> movCotacaoAnals8;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoaEndereco9")
	private List<MovCotacaoAnal> movCotacaoAnals9;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="gerPessoaEndereco10")
	private List<MovCotacaoAnal> movCotacaoAnals10;

	//bi-directional many-to-one association to MovFrete
	@OneToMany(mappedBy="gerPessoaEndereco1")
	private List<MovFrete> movFretes1;

	//bi-directional many-to-one association to MovFrete
	@OneToMany(mappedBy="gerPessoaEndereco2")
	private List<MovFrete> movFretes2;

	//bi-directional many-to-one association to OpeCentro2
	@OneToMany(mappedBy="gerPessoaEndereco")
	private List<OpeCentro2> opeCentro2s;

	//bi-directional many-to-one association to OpeCentro2Ord
	@OneToMany(mappedBy="gerPessoaEndereco")
	private List<OpeCentro2Ord> opeCentro2Ords;

	//bi-directional many-to-one association to OpeCentro2OrdRec
	@OneToMany(mappedBy="gerPessoaEndereco")
	private List<OpeCentro2OrdRec> opeCentro2OrdRecs;

	//bi-directional many-to-one association to OpeOcorCompartMov
	@OneToMany(mappedBy="gerPessoaEndereco")
	private List<OpeOcorCompartMov> opeOcorCompartMovs;

	//bi-directional many-to-one association to OpeOcorMov
	@OneToMany(mappedBy="gerPessoaEndereco")
	private List<OpeOcorMov> opeOcorMovs;

	public GerPessoaEndereco() {
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

	public String getContato() {
		return this.contato;
	}

	public void setContato(String contato) {
		this.contato = contato;
	}

	public String getEmail() {
		return this.email;
	}

	public void setEmail(String email) {
		this.email = email;
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

	public String getFone() {
		return this.fone;
	}

	public void setFone(String fone) {
		this.fone = fone;
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

	public String getPadrao() {
		return this.padrao;
	}

	public void setPadrao(String padrao) {
		this.padrao = padrao;
	}

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public List<FisTributacao> getFisTributacaos() {
		return this.fisTributacaos;
	}

	public void setFisTributacaos(List<FisTributacao> fisTributacaos) {
		this.fisTributacaos = fisTributacaos;
	}

	public FisTributacao addFisTributacao(FisTributacao fisTributacao) {
		getFisTributacaos().add(fisTributacao);
		fisTributacao.setGerPessoaEndereco(this);

		return fisTributacao;
	}

	public FisTributacao removeFisTributacao(FisTributacao fisTributacao) {
		getFisTributacaos().remove(fisTributacao);
		fisTributacao.setGerPessoaEndereco(null);

		return fisTributacao;
	}

	public GerCidade getGerCidade() {
		return this.gerCidade;
	}

	public void setGerCidade(GerCidade gerCidade) {
		this.gerCidade = gerCidade;
	}

	public GerPessoa getGerPessoa() {
		return this.gerPessoa;
	}

	public void setGerPessoa(GerPessoa gerPessoa) {
		this.gerPessoa = gerPessoa;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<Mov> getMovs1() {
		return this.movs1;
	}

	public void setMovs1(List<Mov> movs1) {
		this.movs1 = movs1;
	}

	public Mov addMovs1(Mov movs1) {
		getMovs1().add(movs1);
		movs1.setGerPessoaEndereco1(this);

		return movs1;
	}

	public Mov removeMovs1(Mov movs1) {
		getMovs1().remove(movs1);
		movs1.setGerPessoaEndereco1(null);

		return movs1;
	}

	public List<Mov> getMovs2() {
		return this.movs2;
	}

	public void setMovs2(List<Mov> movs2) {
		this.movs2 = movs2;
	}

	public Mov addMovs2(Mov movs2) {
		getMovs2().add(movs2);
		movs2.setGerPessoaEndereco2(this);

		return movs2;
	}

	public Mov removeMovs2(Mov movs2) {
		getMovs2().remove(movs2);
		movs2.setGerPessoaEndereco2(null);

		return movs2;
	}

	public List<Mov> getMovs3() {
		return this.movs3;
	}

	public void setMovs3(List<Mov> movs3) {
		this.movs3 = movs3;
	}

	public Mov addMovs3(Mov movs3) {
		getMovs3().add(movs3);
		movs3.setGerPessoaEndereco3(this);

		return movs3;
	}

	public Mov removeMovs3(Mov movs3) {
		getMovs3().remove(movs3);
		movs3.setGerPessoaEndereco3(null);

		return movs3;
	}

	public List<Mov> getMovs4() {
		return this.movs4;
	}

	public void setMovs4(List<Mov> movs4) {
		this.movs4 = movs4;
	}

	public Mov addMovs4(Mov movs4) {
		getMovs4().add(movs4);
		movs4.setGerPessoaEndereco4(this);

		return movs4;
	}

	public Mov removeMovs4(Mov movs4) {
		getMovs4().remove(movs4);
		movs4.setGerPessoaEndereco4(null);

		return movs4;
	}

	public List<Mov> getMovs5() {
		return this.movs5;
	}

	public void setMovs5(List<Mov> movs5) {
		this.movs5 = movs5;
	}

	public Mov addMovs5(Mov movs5) {
		getMovs5().add(movs5);
		movs5.setGerPessoaEndereco5(this);

		return movs5;
	}

	public Mov removeMovs5(Mov movs5) {
		getMovs5().remove(movs5);
		movs5.setGerPessoaEndereco5(null);

		return movs5;
	}

	public List<Mov> getMovs6() {
		return this.movs6;
	}

	public void setMovs6(List<Mov> movs6) {
		this.movs6 = movs6;
	}

	public Mov addMovs6(Mov movs6) {
		getMovs6().add(movs6);
		movs6.setGerPessoaEndereco6(this);

		return movs6;
	}

	public Mov removeMovs6(Mov movs6) {
		getMovs6().remove(movs6);
		movs6.setGerPessoaEndereco6(null);

		return movs6;
	}

	public List<Mov> getMovs7() {
		return this.movs7;
	}

	public void setMovs7(List<Mov> movs7) {
		this.movs7 = movs7;
	}

	public Mov addMovs7(Mov movs7) {
		getMovs7().add(movs7);
		movs7.setGerPessoaEndereco7(this);

		return movs7;
	}

	public Mov removeMovs7(Mov movs7) {
		getMovs7().remove(movs7);
		movs7.setGerPessoaEndereco7(null);

		return movs7;
	}

	public List<MovCotacao> getMovCotacaos() {
		return this.movCotacaos;
	}

	public void setMovCotacaos(List<MovCotacao> movCotacaos) {
		this.movCotacaos = movCotacaos;
	}

	public MovCotacao addMovCotacao(MovCotacao movCotacao) {
		getMovCotacaos().add(movCotacao);
		movCotacao.setGerPessoaEndereco(this);

		return movCotacao;
	}

	public MovCotacao removeMovCotacao(MovCotacao movCotacao) {
		getMovCotacaos().remove(movCotacao);
		movCotacao.setGerPessoaEndereco(null);

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
		movCotacaoAnals1.setGerPessoaEndereco1(this);

		return movCotacaoAnals1;
	}

	public MovCotacaoAnal removeMovCotacaoAnals1(MovCotacaoAnal movCotacaoAnals1) {
		getMovCotacaoAnals1().remove(movCotacaoAnals1);
		movCotacaoAnals1.setGerPessoaEndereco1(null);

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
		movCotacaoAnals2.setGerPessoaEndereco2(this);

		return movCotacaoAnals2;
	}

	public MovCotacaoAnal removeMovCotacaoAnals2(MovCotacaoAnal movCotacaoAnals2) {
		getMovCotacaoAnals2().remove(movCotacaoAnals2);
		movCotacaoAnals2.setGerPessoaEndereco2(null);

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
		movCotacaoAnals3.setGerPessoaEndereco3(this);

		return movCotacaoAnals3;
	}

	public MovCotacaoAnal removeMovCotacaoAnals3(MovCotacaoAnal movCotacaoAnals3) {
		getMovCotacaoAnals3().remove(movCotacaoAnals3);
		movCotacaoAnals3.setGerPessoaEndereco3(null);

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
		movCotacaoAnals4.setGerPessoaEndereco4(this);

		return movCotacaoAnals4;
	}

	public MovCotacaoAnal removeMovCotacaoAnals4(MovCotacaoAnal movCotacaoAnals4) {
		getMovCotacaoAnals4().remove(movCotacaoAnals4);
		movCotacaoAnals4.setGerPessoaEndereco4(null);

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
		movCotacaoAnals5.setGerPessoaEndereco5(this);

		return movCotacaoAnals5;
	}

	public MovCotacaoAnal removeMovCotacaoAnals5(MovCotacaoAnal movCotacaoAnals5) {
		getMovCotacaoAnals5().remove(movCotacaoAnals5);
		movCotacaoAnals5.setGerPessoaEndereco5(null);

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
		movCotacaoAnals6.setGerPessoaEndereco6(this);

		return movCotacaoAnals6;
	}

	public MovCotacaoAnal removeMovCotacaoAnals6(MovCotacaoAnal movCotacaoAnals6) {
		getMovCotacaoAnals6().remove(movCotacaoAnals6);
		movCotacaoAnals6.setGerPessoaEndereco6(null);

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
		movCotacaoAnals7.setGerPessoaEndereco7(this);

		return movCotacaoAnals7;
	}

	public MovCotacaoAnal removeMovCotacaoAnals7(MovCotacaoAnal movCotacaoAnals7) {
		getMovCotacaoAnals7().remove(movCotacaoAnals7);
		movCotacaoAnals7.setGerPessoaEndereco7(null);

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
		movCotacaoAnals8.setGerPessoaEndereco8(this);

		return movCotacaoAnals8;
	}

	public MovCotacaoAnal removeMovCotacaoAnals8(MovCotacaoAnal movCotacaoAnals8) {
		getMovCotacaoAnals8().remove(movCotacaoAnals8);
		movCotacaoAnals8.setGerPessoaEndereco8(null);

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
		movCotacaoAnals9.setGerPessoaEndereco9(this);

		return movCotacaoAnals9;
	}

	public MovCotacaoAnal removeMovCotacaoAnals9(MovCotacaoAnal movCotacaoAnals9) {
		getMovCotacaoAnals9().remove(movCotacaoAnals9);
		movCotacaoAnals9.setGerPessoaEndereco9(null);

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
		movCotacaoAnals10.setGerPessoaEndereco10(this);

		return movCotacaoAnals10;
	}

	public MovCotacaoAnal removeMovCotacaoAnals10(MovCotacaoAnal movCotacaoAnals10) {
		getMovCotacaoAnals10().remove(movCotacaoAnals10);
		movCotacaoAnals10.setGerPessoaEndereco10(null);

		return movCotacaoAnals10;
	}

	public List<MovFrete> getMovFretes1() {
		return this.movFretes1;
	}

	public void setMovFretes1(List<MovFrete> movFretes1) {
		this.movFretes1 = movFretes1;
	}

	public MovFrete addMovFretes1(MovFrete movFretes1) {
		getMovFretes1().add(movFretes1);
		movFretes1.setGerPessoaEndereco1(this);

		return movFretes1;
	}

	public MovFrete removeMovFretes1(MovFrete movFretes1) {
		getMovFretes1().remove(movFretes1);
		movFretes1.setGerPessoaEndereco1(null);

		return movFretes1;
	}

	public List<MovFrete> getMovFretes2() {
		return this.movFretes2;
	}

	public void setMovFretes2(List<MovFrete> movFretes2) {
		this.movFretes2 = movFretes2;
	}

	public MovFrete addMovFretes2(MovFrete movFretes2) {
		getMovFretes2().add(movFretes2);
		movFretes2.setGerPessoaEndereco2(this);

		return movFretes2;
	}

	public MovFrete removeMovFretes2(MovFrete movFretes2) {
		getMovFretes2().remove(movFretes2);
		movFretes2.setGerPessoaEndereco2(null);

		return movFretes2;
	}

	public List<OpeCentro2> getOpeCentro2s() {
		return this.opeCentro2s;
	}

	public void setOpeCentro2s(List<OpeCentro2> opeCentro2s) {
		this.opeCentro2s = opeCentro2s;
	}

	public OpeCentro2 addOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().add(opeCentro2);
		opeCentro2.setGerPessoaEndereco(this);

		return opeCentro2;
	}

	public OpeCentro2 removeOpeCentro2(OpeCentro2 opeCentro2) {
		getOpeCentro2s().remove(opeCentro2);
		opeCentro2.setGerPessoaEndereco(null);

		return opeCentro2;
	}

	public List<OpeCentro2Ord> getOpeCentro2Ords() {
		return this.opeCentro2Ords;
	}

	public void setOpeCentro2Ords(List<OpeCentro2Ord> opeCentro2Ords) {
		this.opeCentro2Ords = opeCentro2Ords;
	}

	public OpeCentro2Ord addOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().add(opeCentro2Ord);
		opeCentro2Ord.setGerPessoaEndereco(this);

		return opeCentro2Ord;
	}

	public OpeCentro2Ord removeOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().remove(opeCentro2Ord);
		opeCentro2Ord.setGerPessoaEndereco(null);

		return opeCentro2Ord;
	}

	public List<OpeCentro2OrdRec> getOpeCentro2OrdRecs() {
		return this.opeCentro2OrdRecs;
	}

	public void setOpeCentro2OrdRecs(List<OpeCentro2OrdRec> opeCentro2OrdRecs) {
		this.opeCentro2OrdRecs = opeCentro2OrdRecs;
	}

	public OpeCentro2OrdRec addOpeCentro2OrdRec(OpeCentro2OrdRec opeCentro2OrdRec) {
		getOpeCentro2OrdRecs().add(opeCentro2OrdRec);
		opeCentro2OrdRec.setGerPessoaEndereco(this);

		return opeCentro2OrdRec;
	}

	public OpeCentro2OrdRec removeOpeCentro2OrdRec(OpeCentro2OrdRec opeCentro2OrdRec) {
		getOpeCentro2OrdRecs().remove(opeCentro2OrdRec);
		opeCentro2OrdRec.setGerPessoaEndereco(null);

		return opeCentro2OrdRec;
	}

	public List<OpeOcorCompartMov> getOpeOcorCompartMovs() {
		return this.opeOcorCompartMovs;
	}

	public void setOpeOcorCompartMovs(List<OpeOcorCompartMov> opeOcorCompartMovs) {
		this.opeOcorCompartMovs = opeOcorCompartMovs;
	}

	public OpeOcorCompartMov addOpeOcorCompartMov(OpeOcorCompartMov opeOcorCompartMov) {
		getOpeOcorCompartMovs().add(opeOcorCompartMov);
		opeOcorCompartMov.setGerPessoaEndereco(this);

		return opeOcorCompartMov;
	}

	public OpeOcorCompartMov removeOpeOcorCompartMov(OpeOcorCompartMov opeOcorCompartMov) {
		getOpeOcorCompartMovs().remove(opeOcorCompartMov);
		opeOcorCompartMov.setGerPessoaEndereco(null);

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
		opeOcorMov.setGerPessoaEndereco(this);

		return opeOcorMov;
	}

	public OpeOcorMov removeOpeOcorMov(OpeOcorMov opeOcorMov) {
		getOpeOcorMovs().remove(opeOcorMov);
		opeOcorMov.setGerPessoaEndereco(null);

		return opeOcorMov;
	}

}