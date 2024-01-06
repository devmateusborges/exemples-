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
@Table(name="fin_tipo_variacao")
@NamedQuery(name="FinTipoVariacao.findAll", query="SELECT f FROM FinTipoVariacao f")
public class FinTipoVariacao implements Serializable {
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

	@Column(nullable=false, length=1)
	private String tipo;

	@Column(name="valor_positivo", nullable=false, length=1)
	private String valorPositivo;

	//bi-directional many-to-one association to FinPagrecBaixaVar
	@OneToMany(mappedBy="finTipoVariacao")
	private List<FinPagrecBaixaVar> finPagrecBaixaVars;

	//bi-directional many-to-one association to FinPagrecParcVar
	@OneToMany(mappedBy="finTipoVariacao")
	private List<FinPagrecParcVar> finPagrecParcVars;

	//bi-directional many-to-one association to FinPagrecPrevVar
	@OneToMany(mappedBy="finTipoVariacao")
	private List<FinPagrecPrevVar> finPagrecPrevVars;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public FinTipoVariacao() {
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

	public String getTipo() {
		return this.tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public String getValorPositivo() {
		return this.valorPositivo;
	}

	public void setValorPositivo(String valorPositivo) {
		this.valorPositivo = valorPositivo;
	}

	public List<FinPagrecBaixaVar> getFinPagrecBaixaVars() {
		return this.finPagrecBaixaVars;
	}

	public void setFinPagrecBaixaVars(List<FinPagrecBaixaVar> finPagrecBaixaVars) {
		this.finPagrecBaixaVars = finPagrecBaixaVars;
	}

	public FinPagrecBaixaVar addFinPagrecBaixaVar(FinPagrecBaixaVar finPagrecBaixaVar) {
		getFinPagrecBaixaVars().add(finPagrecBaixaVar);
		finPagrecBaixaVar.setFinTipoVariacao(this);

		return finPagrecBaixaVar;
	}

	public FinPagrecBaixaVar removeFinPagrecBaixaVar(FinPagrecBaixaVar finPagrecBaixaVar) {
		getFinPagrecBaixaVars().remove(finPagrecBaixaVar);
		finPagrecBaixaVar.setFinTipoVariacao(null);

		return finPagrecBaixaVar;
	}

	public List<FinPagrecParcVar> getFinPagrecParcVars() {
		return this.finPagrecParcVars;
	}

	public void setFinPagrecParcVars(List<FinPagrecParcVar> finPagrecParcVars) {
		this.finPagrecParcVars = finPagrecParcVars;
	}

	public FinPagrecParcVar addFinPagrecParcVar(FinPagrecParcVar finPagrecParcVar) {
		getFinPagrecParcVars().add(finPagrecParcVar);
		finPagrecParcVar.setFinTipoVariacao(this);

		return finPagrecParcVar;
	}

	public FinPagrecParcVar removeFinPagrecParcVar(FinPagrecParcVar finPagrecParcVar) {
		getFinPagrecParcVars().remove(finPagrecParcVar);
		finPagrecParcVar.setFinTipoVariacao(null);

		return finPagrecParcVar;
	}

	public List<FinPagrecPrevVar> getFinPagrecPrevVars() {
		return this.finPagrecPrevVars;
	}

	public void setFinPagrecPrevVars(List<FinPagrecPrevVar> finPagrecPrevVars) {
		this.finPagrecPrevVars = finPagrecPrevVars;
	}

	public FinPagrecPrevVar addFinPagrecPrevVar(FinPagrecPrevVar finPagrecPrevVar) {
		getFinPagrecPrevVars().add(finPagrecPrevVar);
		finPagrecPrevVar.setFinTipoVariacao(this);

		return finPagrecPrevVar;
	}

	public FinPagrecPrevVar removeFinPagrecPrevVar(FinPagrecPrevVar finPagrecPrevVar) {
		getFinPagrecPrevVars().remove(finPagrecPrevVar);
		finPagrecPrevVar.setFinTipoVariacao(null);

		return finPagrecPrevVar;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}