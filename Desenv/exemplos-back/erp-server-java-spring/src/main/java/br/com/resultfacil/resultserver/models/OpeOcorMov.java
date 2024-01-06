package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.util.Date;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_ocor_mov")
@NamedQuery(name="OpeOcorMov.findAll", query="SELECT o FROM OpeOcorMov o")
public class OpeOcorMov implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_mov", nullable=false)
	private Date dataMov;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(nullable=false, length=50)
	private String numero;

	@Column(length=250)
	private String observacao;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_exec", nullable=false)
	private GerPessoaEndereco gerPessoaEndereco;

	//bi-directional many-to-one association to OpeOcorTipo
	@ManyToOne
	@JoinColumn(name="ope_ocor_tipo_id", nullable=false)
	private OpeOcorTipo opeOcorTipo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeOcorMovDest
	@OneToMany(mappedBy="opeOcorMov")
	private List<OpeOcorMovDest> opeOcorMovDests;

	//bi-directional many-to-one association to OpeOcorMovDet
	@OneToMany(mappedBy="opeOcorMov")
	private List<OpeOcorMovDet> opeOcorMovDets;

	public OpeOcorMov() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataMov() {
		return this.dataMov;
	}

	public void setDataMov(Date dataMov) {
		this.dataMov = dataMov;
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

	public String getNumero() {
		return this.numero;
	}

	public void setNumero(String numero) {
		this.numero = numero;
	}

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public GerPessoaEndereco getGerPessoaEndereco() {
		return this.gerPessoaEndereco;
	}

	public void setGerPessoaEndereco(GerPessoaEndereco gerPessoaEndereco) {
		this.gerPessoaEndereco = gerPessoaEndereco;
	}

	public OpeOcorTipo getOpeOcorTipo() {
		return this.opeOcorTipo;
	}

	public void setOpeOcorTipo(OpeOcorTipo opeOcorTipo) {
		this.opeOcorTipo = opeOcorTipo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeOcorMovDest> getOpeOcorMovDests() {
		return this.opeOcorMovDests;
	}

	public void setOpeOcorMovDests(List<OpeOcorMovDest> opeOcorMovDests) {
		this.opeOcorMovDests = opeOcorMovDests;
	}

	public OpeOcorMovDest addOpeOcorMovDest(OpeOcorMovDest opeOcorMovDest) {
		getOpeOcorMovDests().add(opeOcorMovDest);
		opeOcorMovDest.setOpeOcorMov(this);

		return opeOcorMovDest;
	}

	public OpeOcorMovDest removeOpeOcorMovDest(OpeOcorMovDest opeOcorMovDest) {
		getOpeOcorMovDests().remove(opeOcorMovDest);
		opeOcorMovDest.setOpeOcorMov(null);

		return opeOcorMovDest;
	}

	public List<OpeOcorMovDet> getOpeOcorMovDets() {
		return this.opeOcorMovDets;
	}

	public void setOpeOcorMovDets(List<OpeOcorMovDet> opeOcorMovDets) {
		this.opeOcorMovDets = opeOcorMovDets;
	}

	public OpeOcorMovDet addOpeOcorMovDet(OpeOcorMovDet opeOcorMovDet) {
		getOpeOcorMovDets().add(opeOcorMovDet);
		opeOcorMovDet.setOpeOcorMov(this);

		return opeOcorMovDet;
	}

	public OpeOcorMovDet removeOpeOcorMovDet(OpeOcorMovDet opeOcorMovDet) {
		getOpeOcorMovDets().remove(opeOcorMovDet);
		opeOcorMovDet.setOpeOcorMov(null);

		return opeOcorMovDet;
	}

}