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
@Table(name="mov_status")
@NamedQuery(name="MovStatus.findAll", query="SELECT m FROM MovStatus m")
public class MovStatus implements Serializable {
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

	@Column(name="sigla_mov_status", nullable=false, length=50)
	private String siglaMovStatus;

	@Column(name="tipo_status", nullable=false, length=1)
	private String tipoStatus;

	//bi-directional many-to-one association to Mov
	@OneToMany(mappedBy="movStatus")
	private List<Mov> movs;

	//bi-directional many-to-one association to MovOperacaoStatus
	@OneToMany(mappedBy="movStatus1")
	private List<MovOperacaoStatus> movOperacaoStatuses1;

	//bi-directional many-to-one association to MovOperacaoStatus
	@OneToMany(mappedBy="movStatus2")
	private List<MovOperacaoStatus> movOperacaoStatuses2;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public MovStatus() {
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

	public String getSiglaMovStatus() {
		return this.siglaMovStatus;
	}

	public void setSiglaMovStatus(String siglaMovStatus) {
		this.siglaMovStatus = siglaMovStatus;
	}

	public String getTipoStatus() {
		return this.tipoStatus;
	}

	public void setTipoStatus(String tipoStatus) {
		this.tipoStatus = tipoStatus;
	}

	public List<Mov> getMovs() {
		return this.movs;
	}

	public void setMovs(List<Mov> movs) {
		this.movs = movs;
	}

	public Mov addMov(Mov mov) {
		getMovs().add(mov);
		mov.setMovStatus(this);

		return mov;
	}

	public Mov removeMov(Mov mov) {
		getMovs().remove(mov);
		mov.setMovStatus(null);

		return mov;
	}

	public List<MovOperacaoStatus> getMovOperacaoStatuses1() {
		return this.movOperacaoStatuses1;
	}

	public void setMovOperacaoStatuses1(List<MovOperacaoStatus> movOperacaoStatuses1) {
		this.movOperacaoStatuses1 = movOperacaoStatuses1;
	}

	public MovOperacaoStatus addMovOperacaoStatuses1(MovOperacaoStatus movOperacaoStatuses1) {
		getMovOperacaoStatuses1().add(movOperacaoStatuses1);
		movOperacaoStatuses1.setMovStatus1(this);

		return movOperacaoStatuses1;
	}

	public MovOperacaoStatus removeMovOperacaoStatuses1(MovOperacaoStatus movOperacaoStatuses1) {
		getMovOperacaoStatuses1().remove(movOperacaoStatuses1);
		movOperacaoStatuses1.setMovStatus1(null);

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
		movOperacaoStatuses2.setMovStatus2(this);

		return movOperacaoStatuses2;
	}

	public MovOperacaoStatus removeMovOperacaoStatuses2(MovOperacaoStatus movOperacaoStatuses2) {
		getMovOperacaoStatuses2().remove(movOperacaoStatuses2);
		movOperacaoStatuses2.setMovStatus2(null);

		return movOperacaoStatuses2;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}