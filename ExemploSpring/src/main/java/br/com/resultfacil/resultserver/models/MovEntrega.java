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
@Table(name="mov_entrega")
@NamedQuery(name="MovEntrega.findAll", query="SELECT m FROM MovEntrega m")
public class MovEntrega implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	//bi-directional many-to-one association to GerCidade
	@ManyToOne
	@JoinColumn(name="ger_cidade_id")
	private GerCidade gerCidade;

	//bi-directional many-to-one association to Mov
	@ManyToOne
	@JoinColumn(name="mov_id", nullable=false)
	private Mov mov;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to MovEntregaDoc
	@OneToMany(mappedBy="movEntrega")
	private List<MovEntregaDoc> movEntregaDocs;

	public MovEntrega() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
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

	public GerCidade getGerCidade() {
		return this.gerCidade;
	}

	public void setGerCidade(GerCidade gerCidade) {
		this.gerCidade = gerCidade;
	}

	public Mov getMov() {
		return this.mov;
	}

	public void setMov(Mov mov) {
		this.mov = mov;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<MovEntregaDoc> getMovEntregaDocs() {
		return this.movEntregaDocs;
	}

	public void setMovEntregaDocs(List<MovEntregaDoc> movEntregaDocs) {
		this.movEntregaDocs = movEntregaDocs;
	}

	public MovEntregaDoc addMovEntregaDoc(MovEntregaDoc movEntregaDoc) {
		getMovEntregaDocs().add(movEntregaDoc);
		movEntregaDoc.setMovEntrega(this);

		return movEntregaDoc;
	}

	public MovEntregaDoc removeMovEntregaDoc(MovEntregaDoc movEntregaDoc) {
		getMovEntregaDocs().remove(movEntregaDoc);
		movEntregaDoc.setMovEntrega(null);

		return movEntregaDoc;
	}

}