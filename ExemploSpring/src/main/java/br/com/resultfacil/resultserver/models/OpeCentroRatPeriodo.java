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
@Table(name="ope_centro_rat_periodo")
@NamedQuery(name="OpeCentroRatPeriodo.findAll", query="SELECT o FROM OpeCentroRatPeriodo o")
public class OpeCentroRatPeriodo implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_ini", nullable=false)
	private Date dataIni;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="tipo_rp", length=1)
	private String tipoRp;

	//bi-directional many-to-one association to OpeCentroRatFator
	@OneToMany(mappedBy="opeCentroRatPeriodo")
	private List<OpeCentroRatFator> opeCentroRatFators;

	//bi-directional many-to-one association to OpeCentroRatTipo
	@ManyToOne
	@JoinColumn(name="ope_centro_rat_tipo_id", nullable=false)
	private OpeCentroRatTipo opeCentroRatTipo;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentroRatPeriodo() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataIni() {
		return this.dataIni;
	}

	public void setDataIni(Date dataIni) {
		this.dataIni = dataIni;
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

	public String getTipoRp() {
		return this.tipoRp;
	}

	public void setTipoRp(String tipoRp) {
		this.tipoRp = tipoRp;
	}

	public List<OpeCentroRatFator> getOpeCentroRatFators() {
		return this.opeCentroRatFators;
	}

	public void setOpeCentroRatFators(List<OpeCentroRatFator> opeCentroRatFators) {
		this.opeCentroRatFators = opeCentroRatFators;
	}

	public OpeCentroRatFator addOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().add(opeCentroRatFator);
		opeCentroRatFator.setOpeCentroRatPeriodo(this);

		return opeCentroRatFator;
	}

	public OpeCentroRatFator removeOpeCentroRatFator(OpeCentroRatFator opeCentroRatFator) {
		getOpeCentroRatFators().remove(opeCentroRatFator);
		opeCentroRatFator.setOpeCentroRatPeriodo(null);

		return opeCentroRatFator;
	}

	public OpeCentroRatTipo getOpeCentroRatTipo() {
		return this.opeCentroRatTipo;
	}

	public void setOpeCentroRatTipo(OpeCentroRatTipo opeCentroRatTipo) {
		this.opeCentroRatTipo = opeCentroRatTipo;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}