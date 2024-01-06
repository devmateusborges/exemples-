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
@Table(name="ope_ocor_grupo")
@NamedQuery(name="OpeOcorGrupo.findAll", query="SELECT o FROM OpeOcorGrupo o")
public class OpeOcorGrupo implements Serializable {
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

	@Column(name="sigla_ocor_grupo", nullable=false, length=50)
	private String siglaOcorGrupo;

	//bi-directional many-to-one association to OpeOcor
	@OneToMany(mappedBy="opeOcorGrupo")
	private List<OpeOcor> opeOcors;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeOcorGrupo() {
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

	public String getSiglaOcorGrupo() {
		return this.siglaOcorGrupo;
	}

	public void setSiglaOcorGrupo(String siglaOcorGrupo) {
		this.siglaOcorGrupo = siglaOcorGrupo;
	}

	public List<OpeOcor> getOpeOcors() {
		return this.opeOcors;
	}

	public void setOpeOcors(List<OpeOcor> opeOcors) {
		this.opeOcors = opeOcors;
	}

	public OpeOcor addOpeOcor(OpeOcor opeOcor) {
		getOpeOcors().add(opeOcor);
		opeOcor.setOpeOcorGrupo(this);

		return opeOcor;
	}

	public OpeOcor removeOpeOcor(OpeOcor opeOcor) {
		getOpeOcors().remove(opeOcor);
		opeOcor.setOpeOcorGrupo(null);

		return opeOcor;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}