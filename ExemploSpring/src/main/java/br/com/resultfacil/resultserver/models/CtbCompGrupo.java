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
@Table(name="ctb_comp_grupo")
@NamedQuery(name="CtbCompGrupo.findAll", query="SELECT c FROM CtbCompGrupo c")
public class CtbCompGrupo implements Serializable {
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

	@Column(name="sigla_comp_grupo", nullable=false, length=50)
	private String siglaCompGrupo;

	//bi-directional many-to-one association to CtbComp
	@OneToMany(mappedBy="ctbCompGrupo")
	private List<CtbComp> ctbComps;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public CtbCompGrupo() {
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

	public String getSiglaCompGrupo() {
		return this.siglaCompGrupo;
	}

	public void setSiglaCompGrupo(String siglaCompGrupo) {
		this.siglaCompGrupo = siglaCompGrupo;
	}

	public List<CtbComp> getCtbComps() {
		return this.ctbComps;
	}

	public void setCtbComps(List<CtbComp> ctbComps) {
		this.ctbComps = ctbComps;
	}

	public CtbComp addCtbComp(CtbComp ctbComp) {
		getCtbComps().add(ctbComp);
		ctbComp.setCtbCompGrupo(this);

		return ctbComp;
	}

	public CtbComp removeCtbComp(CtbComp ctbComp) {
		getCtbComps().remove(ctbComp);
		ctbComp.setCtbCompGrupo(null);

		return ctbComp;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}