package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="mov_pedagio")
@NamedQuery(name="MovPedagio.findAll", query="SELECT m FROM MovPedagio m")
public class MovPedagio implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="nr_comprovante", length=50)
	private String nrComprovante;

	@Column(name="valor_pedagio", nullable=false, precision=18, scale=6)
	private BigDecimal valorPedagio;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="ger_pessoa_id_emp_pedagio", nullable=false)
	private GerPessoa gerPessoa1;

	//bi-directional many-to-one association to GerPessoa
	@ManyToOne
	@JoinColumn(name="ger_pessoa_id_responsavel", nullable=false)
	private GerPessoa gerPessoa2;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id", nullable=false)
	private Mov mov;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public MovPedagio() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
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

	public String getNrComprovante() {
		return this.nrComprovante;
	}

	public void setNrComprovante(String nrComprovante) {
		this.nrComprovante = nrComprovante;
	}

	public BigDecimal getValorPedagio() {
		return this.valorPedagio;
	}

	public void setValorPedagio(BigDecimal valorPedagio) {
		this.valorPedagio = valorPedagio;
	}

	public GerPessoa getGerPessoa1() {
		return this.gerPessoa1;
	}

	public void setGerPessoa1(GerPessoa gerPessoa1) {
		this.gerPessoa1 = gerPessoa1;
	}

	public GerPessoa getGerPessoa2() {
		return this.gerPessoa2;
	}

	public void setGerPessoa2(GerPessoa gerPessoa2) {
		this.gerPessoa2 = gerPessoa2;
	}

	public Mov getMov() {
		return this.mov;
	}

	public void setMov(Mov mov) {
		this.mov = mov;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}