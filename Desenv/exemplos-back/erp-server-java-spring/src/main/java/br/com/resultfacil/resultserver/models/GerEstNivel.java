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
@Table(name="ger_est_nivel")
@NamedQuery(name="GerEstNivel.findAll", query="SELECT g FROM GerEstNivel g")
public class GerEstNivel implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=1)
	private String ativo;

	@Column(name="bloq_mov_pedido", length=1)
	private String bloqMovPedido;

	@Column(name="bloq_mov_solic", length=1)
	private String bloqMovSolic;

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

	@Column(length=250)
	private String observacao;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to MovEstNivel
	@OneToMany(mappedBy="gerEstNivel")
	private List<MovEstNivel> movEstNivels;

	public GerEstNivel() {
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

	public String getBloqMovPedido() {
		return this.bloqMovPedido;
	}

	public void setBloqMovPedido(String bloqMovPedido) {
		this.bloqMovPedido = bloqMovPedido;
	}

	public String getBloqMovSolic() {
		return this.bloqMovSolic;
	}

	public void setBloqMovSolic(String bloqMovSolic) {
		this.bloqMovSolic = bloqMovSolic;
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

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<MovEstNivel> getMovEstNivels() {
		return this.movEstNivels;
	}

	public void setMovEstNivels(List<MovEstNivel> movEstNivels) {
		this.movEstNivels = movEstNivels;
	}

	public MovEstNivel addMovEstNivel(MovEstNivel movEstNivel) {
		getMovEstNivels().add(movEstNivel);
		movEstNivel.setGerEstNivel(this);

		return movEstNivel;
	}

	public MovEstNivel removeMovEstNivel(MovEstNivel movEstNivel) {
		getMovEstNivels().remove(movEstNivel);
		movEstNivel.setGerEstNivel(null);

		return movEstNivel;
	}

}