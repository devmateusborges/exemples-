package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="fis_doc_evento")
@NamedQuery(name="FisDocEvento.findAll", query="SELECT f FROM FisDocEvento f")
public class FisDocEvento implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="descricao_evento", length=2147483647)
	private String descricaoEvento;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="nr_protocolo", nullable=false, length=50)
	private String nrProtocolo;

	@Column(name="pdf_retorno", length=2147483647)
	private String pdfRetorno;

	@Column(name="qnt_evento")
	private Integer qntEvento;

	@Column(name="tipo_evento", nullable=false)
	private Integer tipoEvento;

	@Column(name="xml_retorno", nullable=false, length=2147483647)
	private String xmlRetorno;

	//bi-directional many-to-one association to FisDoc
	@ManyToOne
	@JoinColumn(name="fis_doc_id", nullable=false)
	private FisDoc fisDoc;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public FisDocEvento() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getDescricaoEvento() {
		return this.descricaoEvento;
	}

	public void setDescricaoEvento(String descricaoEvento) {
		this.descricaoEvento = descricaoEvento;
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

	public String getNrProtocolo() {
		return this.nrProtocolo;
	}

	public void setNrProtocolo(String nrProtocolo) {
		this.nrProtocolo = nrProtocolo;
	}

	public String getPdfRetorno() {
		return this.pdfRetorno;
	}

	public void setPdfRetorno(String pdfRetorno) {
		this.pdfRetorno = pdfRetorno;
	}

	public Integer getQntEvento() {
		return this.qntEvento;
	}

	public void setQntEvento(Integer qntEvento) {
		this.qntEvento = qntEvento;
	}

	public Integer getTipoEvento() {
		return this.tipoEvento;
	}

	public void setTipoEvento(Integer tipoEvento) {
		this.tipoEvento = tipoEvento;
	}

	public String getXmlRetorno() {
		return this.xmlRetorno;
	}

	public void setXmlRetorno(String xmlRetorno) {
		this.xmlRetorno = xmlRetorno;
	}

	public FisDoc getFisDoc() {
		return this.fisDoc;
	}

	public void setFisDoc(FisDoc fisDoc) {
		this.fisDoc = fisDoc;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}