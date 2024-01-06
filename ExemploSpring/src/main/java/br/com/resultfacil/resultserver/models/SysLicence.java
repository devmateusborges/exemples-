package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.sql.Timestamp;
import java.util.List;



import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="sys_licence")
@NamedQuery(name="SysLicence.findAll", query="SELECT s FROM SysLicence s")
public class SysLicence implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="chamado_id", nullable=false, length=100)
	private String chamadoId;

	@Column(length=100)
	private String doc;

	@Column(name="end_bairro", length=100)
	private String endBairro;

	@Column(name="end_cidade", length=100)
	private String endCidade;

	@Column(name="end_logradouro", length=100)
	private String endLogradouro;

	@Column(name="end_numero", length=100)
	private String endNumero;

	@Column(name="end_pais", length=100)
	private String endPais;

	@Column(name="end_uf", length=100)
	private String endUf;

	@Column(name="log_date_ins", nullable=false)
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="nome_solicitante", nullable=false, length=100)
	private String nomeSolicitante;

	@Column(nullable=false, length=2)
	private String status;

	@Column(name="status_data", nullable=false)
	private Timestamp statusData;

	@Column(name="status_observacao", nullable=false, length=250)
	private String statusObservacao;

	@Column(name="sys_version", length=50)
	private String sysVersion;

	@Column(name="tipo_doc", nullable=false, length=100)
	private String tipoDoc;

	//bi-directional many-to-one association to Sy
	@ManyToOne
	@JoinColumn(name="sys_id", nullable=false)
	private Sys sys;

	//bi-directional many-to-one association to SysPlan
	@ManyToOne
	@JoinColumn(name="sys_plan_id", nullable=false)
	private SysPlan sysPlan;

	//bi-directional many-to-one association to SysUser
	@ManyToOne
	@JoinColumn(name="sys_user_id")
	private SysUser sysUser;

	//bi-directional many-to-one association to SysLicenceDevice
	@OneToMany(mappedBy="sysLicence")
	private List<SysLicenceDevice> sysLicenceDevices;

	//bi-directional many-to-one association to SysRestrictionLicence
	@OneToMany(mappedBy="sysLicence")
	private List<SysRestrictionLicence> sysRestrictionLicences;

	public SysLicence() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getChamadoId() {
		return this.chamadoId;
	}

	public void setChamadoId(String chamadoId) {
		this.chamadoId = chamadoId;
	}

	public String getDoc() {
		return this.doc;
	}

	public void setDoc(String doc) {
		this.doc = doc;
	}

	public String getEndBairro() {
		return this.endBairro;
	}

	public void setEndBairro(String endBairro) {
		this.endBairro = endBairro;
	}

	public String getEndCidade() {
		return this.endCidade;
	}

	public void setEndCidade(String endCidade) {
		this.endCidade = endCidade;
	}

	public String getEndLogradouro() {
		return this.endLogradouro;
	}

	public void setEndLogradouro(String endLogradouro) {
		this.endLogradouro = endLogradouro;
	}

	public String getEndNumero() {
		return this.endNumero;
	}

	public void setEndNumero(String endNumero) {
		this.endNumero = endNumero;
	}

	public String getEndPais() {
		return this.endPais;
	}

	public void setEndPais(String endPais) {
		this.endPais = endPais;
	}

	public String getEndUf() {
		return this.endUf;
	}

	public void setEndUf(String endUf) {
		this.endUf = endUf;
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

	public String getNomeSolicitante() {
		return this.nomeSolicitante;
	}

	public void setNomeSolicitante(String nomeSolicitante) {
		this.nomeSolicitante = nomeSolicitante;
	}

	public String getStatus() {
		return this.status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public Timestamp getStatusData() {
		return this.statusData;
	}

	public void setStatusData(Timestamp statusData) {
		this.statusData = statusData;
	}

	public String getStatusObservacao() {
		return this.statusObservacao;
	}

	public void setStatusObservacao(String statusObservacao) {
		this.statusObservacao = statusObservacao;
	}

	public String getSysVersion() {
		return this.sysVersion;
	}

	public void setSysVersion(String sysVersion) {
		this.sysVersion = sysVersion;
	}

	public String getTipoDoc() {
		return this.tipoDoc;
	}

	public void setTipoDoc(String tipoDoc) {
		this.tipoDoc = tipoDoc;
	}

	public Sys getSys() {
		return this.sys;
	}

	public void setSys(Sys sys) {
		this.sys = sys;
	}

	public SysPlan getSysPlan() {
		return this.sysPlan;
	}

	public void setSysPlan(SysPlan sysPlan) {
		this.sysPlan = sysPlan;
	}

	public SysUser getSysUser() {
		return this.sysUser;
	}

	public void setSysUser(SysUser sysUser) {
		this.sysUser = sysUser;
	}

	public List<SysLicenceDevice> getSysLicenceDevices() {
		return this.sysLicenceDevices;
	}

	public void setSysLicenceDevices(List<SysLicenceDevice> sysLicenceDevices) {
		this.sysLicenceDevices = sysLicenceDevices;
	}

	public SysLicenceDevice addSysLicenceDevice(SysLicenceDevice sysLicenceDevice) {
		getSysLicenceDevices().add(sysLicenceDevice);
		sysLicenceDevice.setSysLicence(this);

		return sysLicenceDevice;
	}

	public SysLicenceDevice removeSysLicenceDevice(SysLicenceDevice sysLicenceDevice) {
		getSysLicenceDevices().remove(sysLicenceDevice);
		sysLicenceDevice.setSysLicence(null);

		return sysLicenceDevice;
	}

	public List<SysRestrictionLicence> getSysRestrictionLicences() {
		return this.sysRestrictionLicences;
	}

	public void setSysRestrictionLicences(List<SysRestrictionLicence> sysRestrictionLicences) {
		this.sysRestrictionLicences = sysRestrictionLicences;
	}

	public SysRestrictionLicence addSysRestrictionLicence(SysRestrictionLicence sysRestrictionLicence) {
		getSysRestrictionLicences().add(sysRestrictionLicence);
		sysRestrictionLicence.setSysLicence(this);

		return sysRestrictionLicence;
	}

	public SysRestrictionLicence removeSysRestrictionLicence(SysRestrictionLicence sysRestrictionLicence) {
		getSysRestrictionLicences().remove(sysRestrictionLicence);
		sysRestrictionLicence.setSysLicence(null);

		return sysRestrictionLicence;
	}

}