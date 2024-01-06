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
@Table(name="ope_compart_ocor")
@NamedQuery(name="OpeCompartOcor.findAll", query="SELECT o FROM OpeCompartOcor o")
public class OpeCompartOcor implements Serializable {
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

	@Column(name="sigla_compart_ocor", nullable=false, length=50)
	private String siglaCompartOcor;

	@Column(name="tipo_ocor", nullable=false, length=1)
	private String tipoOcor;

	//bi-directional many-to-one association to OpeCompartStatus
	@ManyToOne
	@JoinColumn(name="ope_compart_status_id", nullable=false)
	private OpeCompartStatus opeCompartStatus;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeOcorCompartMovDet
	@OneToMany(mappedBy="opeCompartOcor")
	private List<OpeOcorCompartMovDet> opeOcorCompartMovDets;

	//bi-directional many-to-one association to SysDocument
	@OneToMany(mappedBy="opeCompartOcor")
	private List<SysDocument> sysDocuments;

	public OpeCompartOcor() {
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

	public String getSiglaCompartOcor() {
		return this.siglaCompartOcor;
	}

	public void setSiglaCompartOcor(String siglaCompartOcor) {
		this.siglaCompartOcor = siglaCompartOcor;
	}

	public String getTipoOcor() {
		return this.tipoOcor;
	}

	public void setTipoOcor(String tipoOcor) {
		this.tipoOcor = tipoOcor;
	}

	public OpeCompartStatus getOpeCompartStatus() {
		return this.opeCompartStatus;
	}

	public void setOpeCompartStatus(OpeCompartStatus opeCompartStatus) {
		this.opeCompartStatus = opeCompartStatus;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeOcorCompartMovDet> getOpeOcorCompartMovDets() {
		return this.opeOcorCompartMovDets;
	}

	public void setOpeOcorCompartMovDets(List<OpeOcorCompartMovDet> opeOcorCompartMovDets) {
		this.opeOcorCompartMovDets = opeOcorCompartMovDets;
	}

	public OpeOcorCompartMovDet addOpeOcorCompartMovDet(OpeOcorCompartMovDet opeOcorCompartMovDet) {
		getOpeOcorCompartMovDets().add(opeOcorCompartMovDet);
		opeOcorCompartMovDet.setOpeCompartOcor(this);

		return opeOcorCompartMovDet;
	}

	public OpeOcorCompartMovDet removeOpeOcorCompartMovDet(OpeOcorCompartMovDet opeOcorCompartMovDet) {
		getOpeOcorCompartMovDets().remove(opeOcorCompartMovDet);
		opeOcorCompartMovDet.setOpeCompartOcor(null);

		return opeOcorCompartMovDet;
	}

	public List<SysDocument> getSysDocuments() {
		return this.sysDocuments;
	}

	public void setSysDocuments(List<SysDocument> sysDocuments) {
		this.sysDocuments = sysDocuments;
	}

	public SysDocument addSysDocument(SysDocument sysDocument) {
		getSysDocuments().add(sysDocument);
		sysDocument.setOpeCompartOcor(this);

		return sysDocument;
	}

	public SysDocument removeSysDocument(SysDocument sysDocument) {
		getSysDocuments().remove(sysDocument);
		sysDocument.setOpeCompartOcor(null);

		return sysDocument;
	}

}