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
@Table(name="fin_cond_pagrec")
@NamedQuery(name="FinCondPagrec.findAll", query="SELECT f FROM FinCondPagrec f")
public class FinCondPagrec implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(name="considera_feriado", nullable=false, length=1)
	private String consideraFeriado;

	@Column(name="considera_final_sem", nullable=false, length=1)
	private String consideraFinalSem;

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

	@Column(name="qnt_dia_ini", nullable=false)
	private Integer qntDiaIni;

	@Column(name="sigla_cond_pagamento", nullable=false, length=50)
	private String siglaCondPagamento;

	@Column(name="tipo_prazo", length=1)
	private String tipoPrazo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FinCondPagrecConfig
	@OneToMany(mappedBy="finCondPagrec")
	private List<FinCondPagrecConfig> finCondPagrecConfigs;

	//bi-directional many-to-one association to FinPagrec
	@OneToMany(mappedBy="finCondPagrec")
	private List<FinPagrec> finPagrecs;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="finCondPagrec")
	private List<Mov> movs;

	//bi-directional many-to-one association to MovCotacao
	@OneToMany(mappedBy="finCondPagrec")
	private List<MovCotacao> movCotacaos;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="finCondPagrec1")
	private List<MovCotacaoAnal> movCotacaoAnals1;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="finCondPagrec2")
	private List<MovCotacaoAnal> movCotacaoAnals2;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="finCondPagrec3")
	private List<MovCotacaoAnal> movCotacaoAnals3;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="finCondPagrec4")
	private List<MovCotacaoAnal> movCotacaoAnals4;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="finCondPagrec5")
	private List<MovCotacaoAnal> movCotacaoAnals5;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="finCondPagrec6")
	private List<MovCotacaoAnal> movCotacaoAnals6;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="finCondPagrec7")
	private List<MovCotacaoAnal> movCotacaoAnals7;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="finCondPagrec8")
	private List<MovCotacaoAnal> movCotacaoAnals8;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="finCondPagrec9")
	private List<MovCotacaoAnal> movCotacaoAnals9;

	//bi-directional many-to-one association to MovCotacaoAnal
	@OneToMany(mappedBy="finCondPagrec10")
	private List<MovCotacaoAnal> movCotacaoAnals10;

	public FinCondPagrec() {
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

	public String getConsideraFeriado() {
		return this.consideraFeriado;
	}

	public void setConsideraFeriado(String consideraFeriado) {
		this.consideraFeriado = consideraFeriado;
	}

	public String getConsideraFinalSem() {
		return this.consideraFinalSem;
	}

	public void setConsideraFinalSem(String consideraFinalSem) {
		this.consideraFinalSem = consideraFinalSem;
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

	public Integer getQntDiaIni() {
		return this.qntDiaIni;
	}

	public void setQntDiaIni(Integer qntDiaIni) {
		this.qntDiaIni = qntDiaIni;
	}

	public String getSiglaCondPagamento() {
		return this.siglaCondPagamento;
	}

	public void setSiglaCondPagamento(String siglaCondPagamento) {
		this.siglaCondPagamento = siglaCondPagamento;
	}

	public String getTipoPrazo() {
		return this.tipoPrazo;
	}

	public void setTipoPrazo(String tipoPrazo) {
		this.tipoPrazo = tipoPrazo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<FinCondPagrecConfig> getFinCondPagrecConfigs() {
		return this.finCondPagrecConfigs;
	}

	public void setFinCondPagrecConfigs(List<FinCondPagrecConfig> finCondPagrecConfigs) {
		this.finCondPagrecConfigs = finCondPagrecConfigs;
	}

	public FinCondPagrecConfig addFinCondPagrecConfig(FinCondPagrecConfig finCondPagrecConfig) {
		getFinCondPagrecConfigs().add(finCondPagrecConfig);
		finCondPagrecConfig.setFinCondPagrec(this);

		return finCondPagrecConfig;
	}

	public FinCondPagrecConfig removeFinCondPagrecConfig(FinCondPagrecConfig finCondPagrecConfig) {
		getFinCondPagrecConfigs().remove(finCondPagrecConfig);
		finCondPagrecConfig.setFinCondPagrec(null);

		return finCondPagrecConfig;
	}

	public List<FinPagrec> getFinPagrecs() {
		return this.finPagrecs;
	}

	public void setFinPagrecs(List<FinPagrec> finPagrecs) {
		this.finPagrecs = finPagrecs;
	}

	public FinPagrec addFinPagrec(FinPagrec finPagrec) {
		getFinPagrecs().add(finPagrec);
		finPagrec.setFinCondPagrec(this);

		return finPagrec;
	}

	public FinPagrec removeFinPagrec(FinPagrec finPagrec) {
		getFinPagrecs().remove(finPagrec);
		finPagrec.setFinCondPagrec(null);

		return finPagrec;
	}

	public List<Mov> getMovs() {
		return this.movs;
	}

	public void setMovs(List<Mov> movs) {
		this.movs = movs;
	}

	public Mov addMov(Mov mov) {
		getMovs().add(mov);
		mov.setFinCondPagrec(this);

		return mov;
	}

	public Mov removeMov(Mov mov) {
		getMovs().remove(mov);
		mov.setFinCondPagrec(null);

		return mov;
	}

	public List<MovCotacao> getMovCotacaos() {
		return this.movCotacaos;
	}

	public void setMovCotacaos(List<MovCotacao> movCotacaos) {
		this.movCotacaos = movCotacaos;
	}

	public MovCotacao addMovCotacao(MovCotacao movCotacao) {
		getMovCotacaos().add(movCotacao);
		movCotacao.setFinCondPagrec(this);

		return movCotacao;
	}

	public MovCotacao removeMovCotacao(MovCotacao movCotacao) {
		getMovCotacaos().remove(movCotacao);
		movCotacao.setFinCondPagrec(null);

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
		movCotacaoAnals1.setFinCondPagrec1(this);

		return movCotacaoAnals1;
	}

	public MovCotacaoAnal removeMovCotacaoAnals1(MovCotacaoAnal movCotacaoAnals1) {
		getMovCotacaoAnals1().remove(movCotacaoAnals1);
		movCotacaoAnals1.setFinCondPagrec1(null);

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
		movCotacaoAnals2.setFinCondPagrec2(this);

		return movCotacaoAnals2;
	}

	public MovCotacaoAnal removeMovCotacaoAnals2(MovCotacaoAnal movCotacaoAnals2) {
		getMovCotacaoAnals2().remove(movCotacaoAnals2);
		movCotacaoAnals2.setFinCondPagrec2(null);

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
		movCotacaoAnals3.setFinCondPagrec3(this);

		return movCotacaoAnals3;
	}

	public MovCotacaoAnal removeMovCotacaoAnals3(MovCotacaoAnal movCotacaoAnals3) {
		getMovCotacaoAnals3().remove(movCotacaoAnals3);
		movCotacaoAnals3.setFinCondPagrec3(null);

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
		movCotacaoAnals4.setFinCondPagrec4(this);

		return movCotacaoAnals4;
	}

	public MovCotacaoAnal removeMovCotacaoAnals4(MovCotacaoAnal movCotacaoAnals4) {
		getMovCotacaoAnals4().remove(movCotacaoAnals4);
		movCotacaoAnals4.setFinCondPagrec4(null);

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
		movCotacaoAnals5.setFinCondPagrec5(this);

		return movCotacaoAnals5;
	}

	public MovCotacaoAnal removeMovCotacaoAnals5(MovCotacaoAnal movCotacaoAnals5) {
		getMovCotacaoAnals5().remove(movCotacaoAnals5);
		movCotacaoAnals5.setFinCondPagrec5(null);

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
		movCotacaoAnals6.setFinCondPagrec6(this);

		return movCotacaoAnals6;
	}

	public MovCotacaoAnal removeMovCotacaoAnals6(MovCotacaoAnal movCotacaoAnals6) {
		getMovCotacaoAnals6().remove(movCotacaoAnals6);
		movCotacaoAnals6.setFinCondPagrec6(null);

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
		movCotacaoAnals7.setFinCondPagrec7(this);

		return movCotacaoAnals7;
	}

	public MovCotacaoAnal removeMovCotacaoAnals7(MovCotacaoAnal movCotacaoAnals7) {
		getMovCotacaoAnals7().remove(movCotacaoAnals7);
		movCotacaoAnals7.setFinCondPagrec7(null);

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
		movCotacaoAnals8.setFinCondPagrec8(this);

		return movCotacaoAnals8;
	}

	public MovCotacaoAnal removeMovCotacaoAnals8(MovCotacaoAnal movCotacaoAnals8) {
		getMovCotacaoAnals8().remove(movCotacaoAnals8);
		movCotacaoAnals8.setFinCondPagrec8(null);

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
		movCotacaoAnals9.setFinCondPagrec9(this);

		return movCotacaoAnals9;
	}

	public MovCotacaoAnal removeMovCotacaoAnals9(MovCotacaoAnal movCotacaoAnals9) {
		getMovCotacaoAnals9().remove(movCotacaoAnals9);
		movCotacaoAnals9.setFinCondPagrec9(null);

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
		movCotacaoAnals10.setFinCondPagrec10(this);

		return movCotacaoAnals10;
	}

	public MovCotacaoAnal removeMovCotacaoAnals10(MovCotacaoAnal movCotacaoAnals10) {
		getMovCotacaoAnals10().remove(movCotacaoAnals10);
		movCotacaoAnals10.setFinCondPagrec10(null);

		return movCotacaoAnals10;
	}

}