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
@Table(name="ger_itemserv_compos_tipo")
@NamedQuery(name="GerItemservComposTipo.findAll", query="SELECT g FROM GerItemservComposTipo g")
public class GerItemservComposTipo implements Serializable {
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

	@Column(name="unit_id", nullable=false, length=36)
	private String unitId;

	//bi-directional many-to-one association to GerItemservCompo
	@OneToMany(mappedBy="gerItemservComposTipo")
	private List<GerItemservCompo> gerItemservCompos;

	public GerItemservComposTipo() {
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

	public String getUnitId() {
		return this.unitId;
	}

	public void setUnitId(String unitId) {
		this.unitId = unitId;
	}

	public List<GerItemservCompo> getGerItemservCompos() {
		return this.gerItemservCompos;
	}

	public void setGerItemservCompos(List<GerItemservCompo> gerItemservCompos) {
		this.gerItemservCompos = gerItemservCompos;
	}

	public GerItemservCompo addGerItemservCompo(GerItemservCompo gerItemservCompo) {
		getGerItemservCompos().add(gerItemservCompo);
		gerItemservCompo.setGerItemservComposTipo(this);

		return gerItemservCompo;
	}

	public GerItemservCompo removeGerItemservCompo(GerItemservCompo gerItemservCompo) {
		getGerItemservCompos().remove(gerItemservCompo);
		gerItemservCompo.setGerItemservComposTipo(null);

		return gerItemservCompo;
	}

}