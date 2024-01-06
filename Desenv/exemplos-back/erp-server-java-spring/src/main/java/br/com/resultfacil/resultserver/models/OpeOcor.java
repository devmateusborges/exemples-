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
@Table(name="ope_ocor")
@NamedQuery(name="OpeOcor.findAll", query="SELECT o FROM OpeOcor o")
public class OpeOcor implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(nullable=false, length=50)
	private String icon;

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

	@Column(name="sigla_ocor", nullable=false, length=50)
	private String siglaOcor;

	@Column(nullable=false, length=1)
	private String tipo;

	@Column(name="tipo_lanc", nullable=false, length=1)
	private String tipoLanc;

	//bi-directional many-to-one association to GerUmedida
	@ManyToOne
	@JoinColumn(name="ger_umedida_id", nullable=false)
	private GerUmedida gerUmedida;

	//bi-directional many-to-one association to OpeOcorGrupo
	@ManyToOne
	@JoinColumn(name="ope_ocor_grupo_id", nullable=false)
	private OpeOcorGrupo opeOcorGrupo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeOcorMovDet
	@OneToMany(mappedBy="opeOcor")
	private List<OpeOcorMovDet> opeOcorMovDets;

	//bi-directional many-to-one association to OpeOcorPrev
	@OneToMany(mappedBy="opeOcor")
	private List<OpeOcorPrev> opeOcorPrevs;

	//bi-directional many-to-one association to SysDocument
	@OneToMany(mappedBy="opeOcor")
	private List<SysDocument> sysDocuments;

	public OpeOcor() {
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

	public String getIcon() {
		return this.icon;
	}

	public void setIcon(String icon) {
		this.icon = icon;
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

	public String getSiglaOcor() {
		return this.siglaOcor;
	}

	public void setSiglaOcor(String siglaOcor) {
		this.siglaOcor = siglaOcor;
	}

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public String getTipoLanc() {
		return this.tipoLanc;
	}

	public void setTipoLanc(String tipoLanc) {
		this.tipoLanc = tipoLanc;
	}

	public GerUmedida getGerUmedida() {
		return this.gerUmedida;
	}

	public void setGerUmedida(GerUmedida gerUmedida) {
		this.gerUmedida = gerUmedida;
	}

	public OpeOcorGrupo getOpeOcorGrupo() {
		return this.opeOcorGrupo;
	}

	public void setOpeOcorGrupo(OpeOcorGrupo opeOcorGrupo) {
		this.opeOcorGrupo = opeOcorGrupo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeOcorMovDet> getOpeOcorMovDets() {
		return this.opeOcorMovDets;
	}

	public void setOpeOcorMovDets(List<OpeOcorMovDet> opeOcorMovDets) {
		this.opeOcorMovDets = opeOcorMovDets;
	}

	public OpeOcorMovDet addOpeOcorMovDet(OpeOcorMovDet opeOcorMovDet) {
		getOpeOcorMovDets().add(opeOcorMovDet);
		opeOcorMovDet.setOpeOcor(this);

		return opeOcorMovDet;
	}

	public OpeOcorMovDet removeOpeOcorMovDet(OpeOcorMovDet opeOcorMovDet) {
		getOpeOcorMovDets().remove(opeOcorMovDet);
		opeOcorMovDet.setOpeOcor(null);

		return opeOcorMovDet;
	}

	public List<OpeOcorPrev> getOpeOcorPrevs() {
		return this.opeOcorPrevs;
	}

	public void setOpeOcorPrevs(List<OpeOcorPrev> opeOcorPrevs) {
		this.opeOcorPrevs = opeOcorPrevs;
	}

	public OpeOcorPrev addOpeOcorPrev(OpeOcorPrev opeOcorPrev) {
		getOpeOcorPrevs().add(opeOcorPrev);
		opeOcorPrev.setOpeOcor(this);

		return opeOcorPrev;
	}

	public OpeOcorPrev removeOpeOcorPrev(OpeOcorPrev opeOcorPrev) {
		getOpeOcorPrevs().remove(opeOcorPrev);
		opeOcorPrev.setOpeOcor(null);

		return opeOcorPrev;
	}

	public List<SysDocument> getSysDocuments() {
		return this.sysDocuments;
	}

	public void setSysDocuments(List<SysDocument> sysDocuments) {
		this.sysDocuments = sysDocuments;
	}

	public SysDocument addSysDocument(SysDocument sysDocument) {
		getSysDocuments().add(sysDocument);
		sysDocument.setOpeOcor(this);

		return sysDocument;
	}

	public SysDocument removeSysDocument(SysDocument sysDocument) {
		getSysDocuments().remove(sysDocument);
		sysDocument.setOpeOcor(null);

		return sysDocument;
	}

}