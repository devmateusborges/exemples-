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
@Table(name="ope_ocor_tipo")
@NamedQuery(name="OpeOcorTipo.findAll", query="SELECT o FROM OpeOcorTipo o")
public class OpeOcorTipo implements Serializable {
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

	@Column(name="obrig_ope_compart", nullable=false, length=1)
	private String obrigOpeCompart;

	@Column(name="sigla_ocor_tipo", nullable=false, length=50)
	private String siglaOcorTipo;

	@Column(nullable=false, length=1)
	private String tipo;

	//bi-directional many-to-one association to OpeOcorMov
	@OneToMany(mappedBy="opeOcorTipo")
	private List<OpeOcorMov> opeOcorMovs;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeOcorTipo() {
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

	public String getObrigOpeCompart() {
		return this.obrigOpeCompart;
	}

	public void setObrigOpeCompart(String obrigOpeCompart) {
		this.obrigOpeCompart = obrigOpeCompart;
	}

	public String getSiglaOcorTipo() {
		return this.siglaOcorTipo;
	}

	public void setSiglaOcorTipo(String siglaOcorTipo) {
		this.siglaOcorTipo = siglaOcorTipo;
	}

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public List<OpeOcorMov> getOpeOcorMovs() {
		return this.opeOcorMovs;
	}

	public void setOpeOcorMovs(List<OpeOcorMov> opeOcorMovs) {
		this.opeOcorMovs = opeOcorMovs;
	}

	public OpeOcorMov addOpeOcorMov(OpeOcorMov opeOcorMov) {
		getOpeOcorMovs().add(opeOcorMov);
		opeOcorMov.setOpeOcorTipo(this);

		return opeOcorMov;
	}

	public OpeOcorMov removeOpeOcorMov(OpeOcorMov opeOcorMov) {
		getOpeOcorMovs().remove(opeOcorMov);
		opeOcorMov.setOpeOcorTipo(null);

		return opeOcorMov;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}