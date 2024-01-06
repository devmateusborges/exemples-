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
@Table(name="ger_cidade")
@NamedQuery(name="GerCidade.findAll", query="SELECT g FROM GerCidade g")
public class GerCidade implements Serializable {
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

	@Column(name="nr_cidade", nullable=false, length=50)
	private String nrCidade;

	//bi-directional many-to-one association to GerUf
	@ManyToOne
	@JoinColumn(name="ger_uf_id", nullable=false)
	private GerUf gerUf;

	//bi-directional many-to-one association to GerEmpresa
	@OneToMany(mappedBy="gerCidade")
	private List<GerEmpresa> gerEmpresas;

	//bi-directional many-to-one association to GerPessoaEndereco
	@OneToMany(mappedBy="gerCidade")
	private List<GerPessoaEndereco> gerPessoaEnderecos;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="gerCidade1")
	private List<Mov> movs1;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="gerCidade2")
	private List<Mov> movs2;

	//bi-directional many-to-one association to MovEntrega
	@OneToMany(mappedBy="gerCidade")
	private List<MovEntrega> movEntregas;

	//bi-directional many-to-one association to MovPercurso
	@OneToMany(mappedBy="gerCidade")
	private List<MovPercurso> movPercursos;

	//bi-directional many-to-one association to OpeCentro2Equip
	@OneToMany(mappedBy="gerCidade")
	private List<OpeCentro2Equip> opeCentro2Equips;

	public GerCidade() {
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

	public String getNrCidade() {
		return this.nrCidade;
	}

	public void setNrCidade(String nrCidade) {
		this.nrCidade = nrCidade;
	}

	public GerUf getGerUf() {
		return this.gerUf;
	}

	public void setGerUf(GerUf gerUf) {
		this.gerUf = gerUf;
	}

	public List<GerEmpresa> getGerEmpresas() {
		return this.gerEmpresas;
	}

	public void setGerEmpresas(List<GerEmpresa> gerEmpresas) {
		this.gerEmpresas = gerEmpresas;
	}

	public GerEmpresa addGerEmpresa(GerEmpresa gerEmpresa) {
		getGerEmpresas().add(gerEmpresa);
		gerEmpresa.setGerCidade(this);

		return gerEmpresa;
	}

	public GerEmpresa removeGerEmpresa(GerEmpresa gerEmpresa) {
		getGerEmpresas().remove(gerEmpresa);
		gerEmpresa.setGerCidade(null);

		return gerEmpresa;
	}

	public List<GerPessoaEndereco> getGerPessoaEnderecos() {
		return this.gerPessoaEnderecos;
	}

	public void setGerPessoaEnderecos(List<GerPessoaEndereco> gerPessoaEnderecos) {
		this.gerPessoaEnderecos = gerPessoaEnderecos;
	}

	public GerPessoaEndereco addGerPessoaEndereco(GerPessoaEndereco gerPessoaEndereco) {
		getGerPessoaEnderecos().add(gerPessoaEndereco);
		gerPessoaEndereco.setGerCidade(this);

		return gerPessoaEndereco;
	}

	public GerPessoaEndereco removeGerPessoaEndereco(GerPessoaEndereco gerPessoaEndereco) {
		getGerPessoaEnderecos().remove(gerPessoaEndereco);
		gerPessoaEndereco.setGerCidade(null);

		return gerPessoaEndereco;
	}

	public List<Mov> getMovs1() {
		return this.movs1;
	}

	public void setMovs1(List<Mov> movs1) {
		this.movs1 = movs1;
	}

	public Mov addMovs1(Mov movs1) {
		getMovs1().add(movs1);
		movs1.setGerCidade1(this);

		return movs1;
	}

	public Mov removeMovs1(Mov movs1) {
		getMovs1().remove(movs1);
		movs1.setGerCidade1(null);

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
		movs2.setGerCidade2(this);

		return movs2;
	}

	public Mov removeMovs2(Mov movs2) {
		getMovs2().remove(movs2);
		movs2.setGerCidade2(null);

		return movs2;
	}

	public List<MovEntrega> getMovEntregas() {
		return this.movEntregas;
	}

	public void setMovEntregas(List<MovEntrega> movEntregas) {
		this.movEntregas = movEntregas;
	}

	public MovEntrega addMovEntrega(MovEntrega movEntrega) {
		getMovEntregas().add(movEntrega);
		movEntrega.setGerCidade(this);

		return movEntrega;
	}

	public MovEntrega removeMovEntrega(MovEntrega movEntrega) {
		getMovEntregas().remove(movEntrega);
		movEntrega.setGerCidade(null);

		return movEntrega;
	}

	public List<MovPercurso> getMovPercursos() {
		return this.movPercursos;
	}

	public void setMovPercursos(List<MovPercurso> movPercursos) {
		this.movPercursos = movPercursos;
	}

	public MovPercurso addMovPercurso(MovPercurso movPercurso) {
		getMovPercursos().add(movPercurso);
		movPercurso.setGerCidade(this);

		return movPercurso;
	}

	public MovPercurso removeMovPercurso(MovPercurso movPercurso) {
		getMovPercursos().remove(movPercurso);
		movPercurso.setGerCidade(null);

		return movPercurso;
	}

	public List<OpeCentro2Equip> getOpeCentro2Equips() {
		return this.opeCentro2Equips;
	}

	public void setOpeCentro2Equips(List<OpeCentro2Equip> opeCentro2Equips) {
		this.opeCentro2Equips = opeCentro2Equips;
	}

	public OpeCentro2Equip addOpeCentro2Equip(OpeCentro2Equip opeCentro2Equip) {
		getOpeCentro2Equips().add(opeCentro2Equip);
		opeCentro2Equip.setGerCidade(this);

		return opeCentro2Equip;
	}

	public OpeCentro2Equip removeOpeCentro2Equip(OpeCentro2Equip opeCentro2Equip) {
		getOpeCentro2Equips().remove(opeCentro2Equip);
		opeCentro2Equip.setGerCidade(null);

		return opeCentro2Equip;
	}

}