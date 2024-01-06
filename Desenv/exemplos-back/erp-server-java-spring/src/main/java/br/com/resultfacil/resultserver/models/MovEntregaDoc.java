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
@Table(name="mov_entrega_doc")
@NamedQuery(name="MovEntregaDoc.findAll", query="SELECT m FROM MovEntregaDoc m")
public class MovEntregaDoc implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="chave_documento", length=50)
	private String chaveDocumento;

	@Temporal(TemporalType.DATE)
	@Column(name="data_emissao")
	private Date dataEmissao;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="modelo_documento", length=2)
	private String modeloDocumento;

	@Column(name="nr_documento", length=50)
	private String nrDocumento;

	@Column(name="serie_documento", length=3)
	private String serieDocumento;

	@Column(name="subserie_documento", length=2)
	private String subserieDocumento;

	@Column(name="valor_total", precision=18, scale=6)
	private BigDecimal valorTotal;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id")
	private Mov mov1;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id_interno")
	private Mov mov2;

	//bi-directional many-to-one association to MovEntrega
	@ManyToOne
	@JoinColumn(name="mov_entrega_id")
	private MovEntrega movEntrega;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public MovEntregaDoc() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getChaveDocumento() {
		return this.chaveDocumento;
	}

	public void setChaveDocumento(String chaveDocumento) {
		this.chaveDocumento = chaveDocumento;
	}

	public Date getDataEmissao() {
		return this.dataEmissao;
	}

	public void setDataEmissao(Date dataEmissao) {
		this.dataEmissao = dataEmissao;
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

	public String getModeloDocumento() {
		return this.modeloDocumento;
	}

	public void setModeloDocumento(String modeloDocumento) {
		this.modeloDocumento = modeloDocumento;
	}

	public String getNrDocumento() {
		return this.nrDocumento;
	}

	public void setNrDocumento(String nrDocumento) {
		this.nrDocumento = nrDocumento;
	}

	public String getSerieDocumento() {
		return this.serieDocumento;
	}

	public void setSerieDocumento(String serieDocumento) {
		this.serieDocumento = serieDocumento;
	}

	public String getSubserieDocumento() {
		return this.subserieDocumento;
	}

	public void setSubserieDocumento(String subserieDocumento) {
		this.subserieDocumento = subserieDocumento;
	}

	public BigDecimal getValorTotal() {
		return this.valorTotal;
	}

	public void setValorTotal(BigDecimal valorTotal) {
		this.valorTotal = valorTotal;
	}

	public Mov getMov1() {
		return this.mov1;
	}

	public void setMov1(Mov mov1) {
		this.mov1 = mov1;
	}

	public Mov getMov2() {
		return this.mov2;
	}

	public void setMov2(Mov mov2) {
		this.mov2 = mov2;
	}

	public MovEntrega getMovEntrega() {
		return this.movEntrega;
	}

	public void setMovEntrega(MovEntrega movEntrega) {
		this.movEntrega = movEntrega;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}