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
@Table(name="mov_operacao")
@NamedQuery(name="MovOperacao.findAll", query="SELECT m FROM MovOperacao m")
public class MovOperacao implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(length=2147483647)
	private String configuracao;

	@Column(name="finalidade_doc", nullable=false)
	private Integer finalidadeDoc;

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

	@Column(name="sigla_mov_operacao", nullable=false, length=50)
	private String siglaMovOperacao;

	@Column(name="tipo_es", length=1)
	private String tipoEs;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="movOperacao")
	private List<Mov> movs;

	//bi-directional many-to-one association to GerNumeracao
	@ManyToOne
	@JoinColumn(name="ger_numeracao_id", nullable=false)
	private GerNumeracao gerNumeracao;

	//bi-directional many-to-one association to MovTipo
	@ManyToOne
	@JoinColumn(name="mov_tipo_id", nullable=false)
	private MovTipo movTipo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to MovOperacaoStatus
	@OneToMany(mappedBy="movOperacao1")
	private List<MovOperacaoStatus> movOperacaoStatuses1;

	//bi-directional many-to-one association to MovOperacaoStatus
	@OneToMany(mappedBy="movOperacao2")
	private List<MovOperacaoStatus> movOperacaoStatuses2;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="movOperacao")
	private List<OpeCentroConfig> opeCentroConfigs;

	public MovOperacao() {
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

	public String getConfiguracao() {
		return this.configuracao;
	}

	public void setConfiguracao(String configuracao) {
		this.configuracao = configuracao;
	}

	public Integer getFinalidadeDoc() {
		return this.finalidadeDoc;
	}

	public void setFinalidadeDoc(Integer finalidadeDoc) {
		this.finalidadeDoc = finalidadeDoc;
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

	public String getSiglaMovOperacao() {
		return this.siglaMovOperacao;
	}

	public void setSiglaMovOperacao(String siglaMovOperacao) {
		this.siglaMovOperacao = siglaMovOperacao;
	}

	public String getTipoEs() {
		return this.tipoEs;
	}

	public void setTipoEs(String tipoEs) {
		this.tipoEs = tipoEs;
	}

	public List<Mov> getMovs() {
		return this.movs;
	}

	public void setMovs(List<Mov> movs) {
		this.movs = movs;
	}

	public Mov addMov(Mov mov) {
		getMovs().add(mov);
		mov.setMovOperacao(this);

		return mov;
	}

	public Mov removeMov(Mov mov) {
		getMovs().remove(mov);
		mov.setMovOperacao(null);

		return mov;
	}

	public GerNumeracao getGerNumeracao() {
		return this.gerNumeracao;
	}

	public void setGerNumeracao(GerNumeracao gerNumeracao) {
		this.gerNumeracao = gerNumeracao;
	}

	public MovTipo getMovTipo() {
		return this.movTipo;
	}

	public void setMovTipo(MovTipo movTipo) {
		this.movTipo = movTipo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<MovOperacaoStatus> getMovOperacaoStatuses1() {
		return this.movOperacaoStatuses1;
	}

	public void setMovOperacaoStatuses1(List<MovOperacaoStatus> movOperacaoStatuses1) {
		this.movOperacaoStatuses1 = movOperacaoStatuses1;
	}

	public MovOperacaoStatus addMovOperacaoStatuses1(MovOperacaoStatus movOperacaoStatuses1) {
		getMovOperacaoStatuses1().add(movOperacaoStatuses1);
		movOperacaoStatuses1.setMovOperacao1(this);

		return movOperacaoStatuses1;
	}

	public MovOperacaoStatus removeMovOperacaoStatuses1(MovOperacaoStatus movOperacaoStatuses1) {
		getMovOperacaoStatuses1().remove(movOperacaoStatuses1);
		movOperacaoStatuses1.setMovOperacao1(null);

		return movOperacaoStatuses1;
	}

	public List<MovOperacaoStatus> getMovOperacaoStatuses2() {
		return this.movOperacaoStatuses2;
	}

	public void setMovOperacaoStatuses2(List<MovOperacaoStatus> movOperacaoStatuses2) {
		this.movOperacaoStatuses2 = movOperacaoStatuses2;
	}

	public MovOperacaoStatus addMovOperacaoStatuses2(MovOperacaoStatus movOperacaoStatuses2) {
		getMovOperacaoStatuses2().add(movOperacaoStatuses2);
		movOperacaoStatuses2.setMovOperacao2(this);

		return movOperacaoStatuses2;
	}

	public MovOperacaoStatus removeMovOperacaoStatuses2(MovOperacaoStatus movOperacaoStatuses2) {
		getMovOperacaoStatuses2().remove(movOperacaoStatuses2);
		movOperacaoStatuses2.setMovOperacao2(null);

		return movOperacaoStatuses2;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setMovOperacao(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setMovOperacao(null);

		return opeCentroConfig;
	}

}