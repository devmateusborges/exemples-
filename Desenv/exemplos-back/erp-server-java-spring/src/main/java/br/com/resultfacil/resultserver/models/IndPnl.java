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
@Table(name="ind_pnl")
@NamedQuery(name="IndPnl.findAll", query="SELECT i FROM IndPnl i")
public class IndPnl implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(length=50)
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

	@Column(length=250)
	private String nome;

	@Column(length=1)
	private String tipo;

	//bi-directional many-to-one association to IndPnlRelacRel
	@OneToMany(mappedBy="indPnl")
	private List<IndPnlRelacRel> indPnlRelacRels;

	//bi-directional many-to-one association to SysUserIndPnl
	@OneToMany(mappedBy="indPnl")
	private List<SysUserIndPnl> sysUserIndPnls;

	public IndPnl() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
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

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public List<IndPnlRelacRel> getIndPnlRelacRels() {
		return this.indPnlRelacRels;
	}

	public void setIndPnlRelacRels(List<IndPnlRelacRel> indPnlRelacRels) {
		this.indPnlRelacRels = indPnlRelacRels;
	}

	public IndPnlRelacRel addIndPnlRelacRel(IndPnlRelacRel indPnlRelacRel) {
		getIndPnlRelacRels().add(indPnlRelacRel);
		indPnlRelacRel.setIndPnl(this);

		return indPnlRelacRel;
	}

	public IndPnlRelacRel removeIndPnlRelacRel(IndPnlRelacRel indPnlRelacRel) {
		getIndPnlRelacRels().remove(indPnlRelacRel);
		indPnlRelacRel.setIndPnl(null);

		return indPnlRelacRel;
	}

	public List<SysUserIndPnl> getSysUserIndPnls() {
		return this.sysUserIndPnls;
	}

	public void setSysUserIndPnls(List<SysUserIndPnl> sysUserIndPnls) {
		this.sysUserIndPnls = sysUserIndPnls;
	}

	public SysUserIndPnl addSysUserIndPnl(SysUserIndPnl sysUserIndPnl) {
		getSysUserIndPnls().add(sysUserIndPnl);
		sysUserIndPnl.setIndPnl(this);

		return sysUserIndPnl;
	}

	public SysUserIndPnl removeSysUserIndPnl(SysUserIndPnl sysUserIndPnl) {
		getSysUserIndPnls().remove(sysUserIndPnl);
		sysUserIndPnl.setIndPnl(null);

		return sysUserIndPnl;
	}

}