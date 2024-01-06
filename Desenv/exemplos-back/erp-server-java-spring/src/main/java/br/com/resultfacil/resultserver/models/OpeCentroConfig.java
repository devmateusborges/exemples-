package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.sql.Timestamp;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="ope_centro_config")
@NamedQuery(name="OpeCentroConfig.findAll", query="SELECT o FROM OpeCentroConfig o")
public class OpeCentroConfig implements Serializable {
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

	@Column(length=250)
	private String observacao;

	@Column(name="tipo_regra", nullable=false, length=1)
	private String tipoRegra;

	//bi-directional many-to-one association to GerEmpresa
	@ManyToOne
	@JoinColumn(name="ger_empresa_id")
	private GerEmpresa gerEmpresa;

	//bi-directional many-to-one association to GerItemserv
	@ManyToOne
	@JoinColumn(name="ger_itemserv_id")
	private GerItemserv gerItemserv;

	//bi-directional many-to-one association to GerItemservGrupo
	@ManyToOne
	@JoinColumn(name="ger_itemserv_grupo_id")
	private GerItemservGrupo gerItemservGrupo;

	//bi-directional many-to-one association to GerItemservSubgrupo
	@ManyToOne
	@JoinColumn(name="ger_itemserv_subgrupo_id")
	private GerItemservSubgrupo gerItemservSubgrupo;

	//bi-directional many-to-one association to MovOperacao
	@ManyToOne
	@JoinColumn(name="mov_operacao_id")
	private MovOperacao movOperacao;

	//bi-directional many-to-one association to OpeAtividade
	@ManyToOne
	@JoinColumn(name="ope_atividade_id")
	private OpeAtividade opeAtividade;

	//bi-directional many-to-one association to OpeCentro1
	@ManyToOne
	@JoinColumn(name="ope_centro1_id")
	private OpeCentro1 opeCentro1;

	//bi-directional many-to-one association to OpeCentro2
	@ManyToOne
	@JoinColumn(name="ope_centro2_id")
	private OpeCentro2 opeCentro2;

	//bi-directional many-to-one association to OpeCentro2OrdTipo
	@ManyToOne
	@JoinColumn(name="ope_centro2_ord_tipo_id")
	private OpeCentro2OrdTipo opeCentro2OrdTipo;

	//bi-directional many-to-one association to OpeCentroGrupo
	@ManyToOne
	@JoinColumn(name="ope_centro_grupo_id")
	private OpeCentroGrupo opeCentroGrupo;

	//bi-directional many-to-one association to OpeCentroSubgrupo
	@ManyToOne
	@JoinColumn(name="ope_centro_subgrupo_id")
	private OpeCentroSubgrupo opeCentroSubgrupo;

	//bi-directional many-to-one association to OpeCentroSubtipo
	@ManyToOne
	@JoinColumn(name="ope_centro_subtipo_id")
	private OpeCentroSubtipo opeCentroSubtipo;

	//bi-directional many-to-one association to OpeCentroTipo
	@ManyToOne
	@JoinColumn(name="ope_centro_tipo_id")
	private OpeCentroTipo opeCentroTipo;

	//bi-directional many-to-one association to OpeCompart
	@ManyToOne
	@JoinColumn(name="ope_compart_id")
	private OpeCompart opeCompart;

	//bi-directional many-to-one association to OpeCompartGrupo
	@ManyToOne
	@JoinColumn(name="ope_compart_grupo_id")
	private OpeCompartGrupo opeCompartGrupo;

	//bi-directional many-to-one association to OpeCompartSubgrupo
	@ManyToOne
	@JoinColumn(name="ope_compart_subgrupo_id")
	private OpeCompartSubgrupo opeCompartSubgrupo;

	//bi-directional many-to-one association to OpeEstagio
	@ManyToOne
	@JoinColumn(name="ope_estagio_id")
	private OpeEstagio opeEstagio;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	public OpeCentroConfig() {
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

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public String getTipoRegra() {
		return this.tipoRegra;
	}

	public void setTipoRegra(String tipoRegra) {
		this.tipoRegra = tipoRegra;
	}

	public GerEmpresa getGerEmpresa() {
		return this.gerEmpresa;
	}

	public void setGerEmpresa(GerEmpresa gerEmpresa) {
		this.gerEmpresa = gerEmpresa;
	}

	public GerItemserv getGerItemserv() {
		return this.gerItemserv;
	}

	public void setGerItemserv(GerItemserv gerItemserv) {
		this.gerItemserv = gerItemserv;
	}

	public GerItemservGrupo getGerItemservGrupo() {
		return this.gerItemservGrupo;
	}

	public void setGerItemservGrupo(GerItemservGrupo gerItemservGrupo) {
		this.gerItemservGrupo = gerItemservGrupo;
	}

	public GerItemservSubgrupo getGerItemservSubgrupo() {
		return this.gerItemservSubgrupo;
	}

	public void setGerItemservSubgrupo(GerItemservSubgrupo gerItemservSubgrupo) {
		this.gerItemservSubgrupo = gerItemservSubgrupo;
	}

	public MovOperacao getMovOperacao() {
		return this.movOperacao;
	}

	public void setMovOperacao(MovOperacao movOperacao) {
		this.movOperacao = movOperacao;
	}

	public OpeAtividade getOpeAtividade() {
		return this.opeAtividade;
	}

	public void setOpeAtividade(OpeAtividade opeAtividade) {
		this.opeAtividade = opeAtividade;
	}

	public OpeCentro1 getOpeCentro1() {
		return this.opeCentro1;
	}

	public void setOpeCentro1(OpeCentro1 opeCentro1) {
		this.opeCentro1 = opeCentro1;
	}

	public OpeCentro2 getOpeCentro2() {
		return this.opeCentro2;
	}

	public void setOpeCentro2(OpeCentro2 opeCentro2) {
		this.opeCentro2 = opeCentro2;
	}

	public OpeCentro2OrdTipo getOpeCentro2OrdTipo() {
		return this.opeCentro2OrdTipo;
	}

	public void setOpeCentro2OrdTipo(OpeCentro2OrdTipo opeCentro2OrdTipo) {
		this.opeCentro2OrdTipo = opeCentro2OrdTipo;
	}

	public OpeCentroGrupo getOpeCentroGrupo() {
		return this.opeCentroGrupo;
	}

	public void setOpeCentroGrupo(OpeCentroGrupo opeCentroGrupo) {
		this.opeCentroGrupo = opeCentroGrupo;
	}

	public OpeCentroSubgrupo getOpeCentroSubgrupo() {
		return this.opeCentroSubgrupo;
	}

	public void setOpeCentroSubgrupo(OpeCentroSubgrupo opeCentroSubgrupo) {
		this.opeCentroSubgrupo = opeCentroSubgrupo;
	}

	public OpeCentroSubtipo getOpeCentroSubtipo() {
		return this.opeCentroSubtipo;
	}

	public void setOpeCentroSubtipo(OpeCentroSubtipo opeCentroSubtipo) {
		this.opeCentroSubtipo = opeCentroSubtipo;
	}

	public OpeCentroTipo getOpeCentroTipo() {
		return this.opeCentroTipo;
	}

	public void setOpeCentroTipo(OpeCentroTipo opeCentroTipo) {
		this.opeCentroTipo = opeCentroTipo;
	}

	public OpeCompart getOpeCompart() {
		return this.opeCompart;
	}

	public void setOpeCompart(OpeCompart opeCompart) {
		this.opeCompart = opeCompart;
	}

	public OpeCompartGrupo getOpeCompartGrupo() {
		return this.opeCompartGrupo;
	}

	public void setOpeCompartGrupo(OpeCompartGrupo opeCompartGrupo) {
		this.opeCompartGrupo = opeCompartGrupo;
	}

	public OpeCompartSubgrupo getOpeCompartSubgrupo() {
		return this.opeCompartSubgrupo;
	}

	public void setOpeCompartSubgrupo(OpeCompartSubgrupo opeCompartSubgrupo) {
		this.opeCompartSubgrupo = opeCompartSubgrupo;
	}

	public OpeEstagio getOpeEstagio() {
		return this.opeEstagio;
	}

	public void setOpeEstagio(OpeEstagio opeEstagio) {
		this.opeEstagio = opeEstagio;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

}