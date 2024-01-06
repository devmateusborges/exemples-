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
@Table(name="ger_processo_bloq")
@NamedQuery(name="GerProcessoBloq.findAll", query="SELECT g FROM GerProcessoBloq g")
public class GerProcessoBloq implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Temporal(TemporalType.DATE)
	@Column(name="data_lib_final")
	private Date dataLibFinal;

	@Temporal(TemporalType.DATE)
	@Column(name="data_lib_inicial")
	private Date dataLibInicial;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(nullable=false, length=250)
	private String observacao;

	@Column(name="tipo_processo", nullable=false, length=50)
	private String tipoProcesso;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id", nullable=false)
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to GerProcessoBloqUser
	@OneToMany(mappedBy="gerProcessoBloq")
	private List<GerProcessoBloqUser> gerProcessoBloqUsers;

	public GerProcessoBloq() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Date getDataLibFinal() {
		return this.dataLibFinal;
	}

	public void setDataLibFinal(Date dataLibFinal) {
		this.dataLibFinal = dataLibFinal;
	}

	public Date getDataLibInicial() {
		return this.dataLibInicial;
	}

	public void setDataLibInicial(Date dataLibInicial) {
		this.dataLibInicial = dataLibInicial;
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

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public String getTipoProcesso() {
		return this.tipoProcesso;
	}

	public void setTipoProcesso(String tipoProcesso) {
		this.tipoProcesso = tipoProcesso;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<GerProcessoBloqUser> getGerProcessoBloqUsers() {
		return this.gerProcessoBloqUsers;
	}

	public void setGerProcessoBloqUsers(List<GerProcessoBloqUser> gerProcessoBloqUsers) {
		this.gerProcessoBloqUsers = gerProcessoBloqUsers;
	}

	public GerProcessoBloqUser addGerProcessoBloqUser(GerProcessoBloqUser gerProcessoBloqUser) {
		getGerProcessoBloqUsers().add(gerProcessoBloqUser);
		gerProcessoBloqUser.setGerProcessoBloq(this);

		return gerProcessoBloqUser;
	}

	public GerProcessoBloqUser removeGerProcessoBloqUser(GerProcessoBloqUser gerProcessoBloqUser) {
		getGerProcessoBloqUsers().remove(gerProcessoBloqUser);
		gerProcessoBloqUser.setGerProcessoBloq(null);

		return gerProcessoBloqUser;
	}

}