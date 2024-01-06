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
@Table(name="fin_class_grupo")
@NamedQuery(name="FinClassGrupo.findAll", query="SELECT f FROM FinClassGrupo f")
public class FinClassGrupo implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(nullable=false, length=50)
	private String estrutura;

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

	@Column(name="sigla_class_grupo", length=255)
	private String siglaClassGrupo;

	//bi-directional many-to-one association to FinClassAgrupGrupo
	@OneToMany(mappedBy="finClassGrupo")
	private List<FinClassAgrupGrupo> finClassAgrupGrupos;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public FinClassGrupo() {
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

	public String getEstrutura() {
		return this.estrutura;
	}

	public void setEstrutura(String estrutura) {
		this.estrutura = estrutura;
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

	public String getSiglaClassGrupo() {
		return this.siglaClassGrupo;
	}

	public void setSiglaClassGrupo(String siglaClassGrupo) {
		this.siglaClassGrupo = siglaClassGrupo;
	}

	public List<FinClassAgrupGrupo> getFinClassAgrupGrupos() {
		return this.finClassAgrupGrupos;
	}

	public void setFinClassAgrupGrupos(List<FinClassAgrupGrupo> finClassAgrupGrupos) {
		this.finClassAgrupGrupos = finClassAgrupGrupos;
	}

	public FinClassAgrupGrupo addFinClassAgrupGrupo(FinClassAgrupGrupo finClassAgrupGrupo) {
		getFinClassAgrupGrupos().add(finClassAgrupGrupo);
		finClassAgrupGrupo.setFinClassGrupo(this);

		return finClassAgrupGrupo;
	}

	public FinClassAgrupGrupo removeFinClassAgrupGrupo(FinClassAgrupGrupo finClassAgrupGrupo) {
		getFinClassAgrupGrupos().remove(finClassAgrupGrupo);
		finClassAgrupGrupo.setFinClassGrupo(null);

		return finClassAgrupGrupo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}