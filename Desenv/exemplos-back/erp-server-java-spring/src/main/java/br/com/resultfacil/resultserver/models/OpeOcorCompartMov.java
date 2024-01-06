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
@Table(name="ope_ocor_compart_mov")
@NamedQuery(name="OpeOcorCompartMov.findAll", query="SELECT o FROM OpeOcorCompartMov o")
public class OpeOcorCompartMov implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_mov")
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

	@Column(length=50)
	private String numero;

	@Column(length=250)
	private String observacao;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id")
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to GerPessoaEndereco
	@ManyToOne
	@JoinColumn(name="ger_pessoa_endereco_id_exec")
	private GerPessoaEndereco gerPessoaEndereco;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeOcorCompartMovDet
	@OneToMany(mappedBy="opeOcorCompartMov")
	private List<OpeOcorCompartMovDet> opeOcorCompartMovDets;

	public OpeOcorCompartMov() {
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
		opeOcorCompartMovDet.setOpeOcorCompartMov(this);

		return opeOcorCompartMovDet;
	}

	public OpeOcorCompartMovDet removeOpeOcorCompartMovDet(OpeOcorCompartMovDet opeOcorCompartMovDet) {
		getOpeOcorCompartMovDets().remove(opeOcorCompartMovDet);
		opeOcorCompartMovDet.setOpeOcorCompartMov(null);

		return opeOcorCompartMovDet;
	}

}