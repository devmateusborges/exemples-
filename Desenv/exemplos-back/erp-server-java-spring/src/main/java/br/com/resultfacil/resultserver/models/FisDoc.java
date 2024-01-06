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
@Table(name="fis_doc")
@NamedQuery(name="FisDoc.findAll", query="SELECT f FROM FisDoc f")
public class FisDoc implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false)
	private Integer ambiente;

	@Column(length=50)
	private String chave;

	@Column(name="data_autorizado")
	private Timestamp dataAutorizado;

	@Column(name="data_cancelado")
	private Timestamp dataCancelado;

	@Column(name="data_emissao", nullable=false)
	private Timestamp dataEmissao;

	@Column(name="data_encerrado")
	private Timestamp dataEncerrado;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=2147483647)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(nullable=false)
	private Integer numero;

	@Column(name="numero_fin")
	private Integer numeroFin;

	@Column(name="numero_ini")
	private Integer numeroIni;

	@Column(name="numero_pre")
	private Integer numeroPre;

	@Column(name="pdf_emitido", length=2147483647)
	private String pdfEmitido;

	@Column(nullable=false, length=3)
	private String serie;

	@Column(name="serie_pre", length=3)
	private String seriePre;

	@Column(name="status_sefaz")
	private Integer statusSefaz;

	@Column(name="tipo_emissao", nullable=false)
	private Integer tipoEmissao;

	@Column(name="xml_assinado", length=2147483647)
	private String xmlAssinado;

	@Column(name="xml_protocolado", length=2147483647)
	private String xmlProtocolado;

	//bi-directional many-to-one association to FisDocTipo
	@ManyToOne
	@JoinColumn(name="fis_doc_tipo_id", nullable=false)
	private FisDocTipo fisDocTipo;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id")
	private Mov mov;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to FisDocEvento
	@OneToMany(mappedBy="fisDoc")
	private List<FisDocEvento> fisDocEventos;

	public FisDoc() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Integer getAmbiente() {
		return this.ambiente;
	}

	public void setAmbiente(Integer ambiente) {
		this.ambiente = ambiente;
	}

	public String getChave() {
		return this.chave;
	}

	public void setChave(String chave) {
		this.chave = chave;
	}

	public Timestamp getDataAutorizado() {
		return this.dataAutorizado;
	}

	public void setDataAutorizado(Timestamp dataAutorizado) {
		this.dataAutorizado = dataAutorizado;
	}

	public Timestamp getDataCancelado() {
		return this.dataCancelado;
	}

	public void setDataCancelado(Timestamp dataCancelado) {
		this.dataCancelado = dataCancelado;
	}

	public Timestamp getDataEmissao() {
		return this.dataEmissao;
	}

	public void setDataEmissao(Timestamp dataEmissao) {
		this.dataEmissao = dataEmissao;
	}

	public Timestamp getDataEncerrado() {
		return this.dataEncerrado;
	}

	public void setDataEncerrado(Timestamp dataEncerrado) {
		this.dataEncerrado = dataEncerrado;
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

	public Integer getNumero() {
		return this.numero;
	}

	public void setNumero(Integer numero) {
		this.numero = numero;
	}

	public Integer getNumeroFin() {
		return this.numeroFin;
	}

	public void setNumeroFin(Integer numeroFin) {
		this.numeroFin = numeroFin;
	}

	public Integer getNumeroIni() {
		return this.numeroIni;
	}

	public void setNumeroIni(Integer numeroIni) {
		this.numeroIni = numeroIni;
	}

	public Integer getNumeroPre() {
		return this.numeroPre;
	}

	public void setNumeroPre(Integer numeroPre) {
		this.numeroPre = numeroPre;
	}

	public String getPdfEmitido() {
		return this.pdfEmitido;
	}

	public void setPdfEmitido(String pdfEmitido) {
		this.pdfEmitido = pdfEmitido;
	}

	public String getSerie() {
		return this.serie;
	}

	public void setSerie(String serie) {
		this.serie = serie;
	}

	public String getSeriePre() {
		return this.seriePre;
	}

	public void setSeriePre(String seriePre) {
		this.seriePre = seriePre;
	}

	public Integer getStatusSefaz() {
		return this.statusSefaz;
	}

	public void setStatusSefaz(Integer statusSefaz) {
		this.statusSefaz = statusSefaz;
	}

	public Integer getTipoEmissao() {
		return this.tipoEmissao;
	}

	public void setTipoEmissao(Integer tipoEmissao) {
		this.tipoEmissao = tipoEmissao;
	}

	public String getXmlAssinado() {
		return this.xmlAssinado;
	}

	public void setXmlAssinado(String xmlAssinado) {
		this.xmlAssinado = xmlAssinado;
	}

	public String getXmlProtocolado() {
		return this.xmlProtocolado;
	}

	public void setXmlProtocolado(String xmlProtocolado) {
		this.xmlProtocolado = xmlProtocolado;
	}

	public FisDocTipo getFisDocTipo() {
		return this.fisDocTipo;
	}

	public void setFisDocTipo(FisDocTipo fisDocTipo) {
		this.fisDocTipo = fisDocTipo;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
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

	public List<FisDocEvento> getFisDocEventos() {
		return this.fisDocEventos;
	}

	public void setFisDocEventos(List<FisDocEvento> fisDocEventos) {
		this.fisDocEventos = fisDocEventos;
	}

	public FisDocEvento addFisDocEvento(FisDocEvento fisDocEvento) {
		getFisDocEventos().add(fisDocEvento);
		fisDocEvento.setFisDoc(this);

		return fisDocEvento;
	}

	public FisDocEvento removeFisDocEvento(FisDocEvento fisDocEvento) {
		getFisDocEventos().remove(fisDocEvento);
		fisDocEvento.setFisDoc(null);

		return fisDocEvento;
	}

}