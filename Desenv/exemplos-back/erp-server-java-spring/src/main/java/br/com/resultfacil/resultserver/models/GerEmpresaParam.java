package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.util.Date;
import java.sql.Timestamp;

import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ger_empresa_param")
@NamedQuery(name="GerEmpresaParam.findAll", query="SELECT g FROM GerEmpresaParam g")
public class GerEmpresaParam implements Serializable {
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

	@Column(nullable=false, length=250)
	private String observacao;

	@Column(name="sigla_param", nullable=false, length=50)
	private String siglaParam;

	@Column(name="unit_id", nullable=false, length=36)
	private String unitId;

	@Temporal(TemporalType.DATE)
	@Column(name="valor_dt", nullable=false)
	private Date valorDt;

	@Column(name="valor_nm", nullable=false, precision=18, scale=6)
	private BigDecimal valorNm;

	@Column(name="valor_tx", nullable=false, length=250)
	private String valorTx;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	public GerEmpresaParam() {
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

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public String getSiglaParam() {
		return this.siglaParam;
	}

	public void setSiglaParam(String siglaParam) {
		this.siglaParam = siglaParam;
	}

	public String getUnitId() {
		return this.unitId;
	}

	public void setUnitId(String unitId) {
		this.unitId = unitId;
	}

	public Date getValorDt() {
		return this.valorDt;
	}

	public void setValorDt(Date valorDt) {
		this.valorDt = valorDt;
	}

	public BigDecimal getValorNm() {
		return this.valorNm;
	}

	public void setValorNm(BigDecimal valorNm) {
		this.valorNm = valorNm;
	}

	public String getValorTx() {
		return this.valorTx;
	}

	public void setValorTx(String valorTx) {
		this.valorTx = valorTx;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

}