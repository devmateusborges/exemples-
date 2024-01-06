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
@Table(name="ope_centro2_ord_tipo")
@NamedQuery(name="OpeCentro2OrdTipo.findAll", query="SELECT o FROM OpeCentro2OrdTipo o")
public class OpeCentro2OrdTipo implements Serializable {
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

	@Column(name="sigla_ord_tipo", nullable=false, length=50)
	private String siglaOrdTipo;

	@Column(name="valida_itemserv_i", length=1)
	private String validaItemservI;

	@Column(name="valida_itemserv_s", length=1)
	private String validaItemservS;

	@Column(name="valida_prev_itemserv", length=1)
	private String validaPrevItemserv;

	@Column(name="valida_prev_rec", length=1)
	private String validaPrevRec;

	@Column(name="valida_rec_equip", length=1)
	private String validaRecEquip;

	@Column(name="valida_rec_pessoa", length=1)
	private String validaRecPessoa;

	@Column(name="valida_regra_config", length=1)
	private String validaRegraConfig;

	@Column(name="valida_saldo_area_aberta", length=1)
	private String validaSaldoAreaAberta;

	@Column(name="valida_tipo_executor", length=2)
	private String validaTipoExecutor;

	@Column(name="valida_tipo_prop_rec_equip", length=2)
	private String validaTipoPropRecEquip;

	@Column(name="valida_tipo_prop_rec_pessoa", length=2)
	private String validaTipoPropRecPessoa;

	//bi-directional many-to-one association to OpeCentro2Ord
	@OneToMany(mappedBy="opeCentro2OrdTipo")
	private List<OpeCentro2Ord> opeCentro2Ords;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCentroConfig
	@OneToMany(mappedBy="opeCentro2OrdTipo")
	private List<OpeCentroConfig> opeCentroConfigs;

	//bi-directional many-to-one association to OpeCentroPrev
	@OneToMany(mappedBy="opeCentro2OrdTipo")
	private List<OpeCentroPrev> opeCentroPrevs;

	public OpeCentro2OrdTipo() {
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

	public String getSiglaOrdTipo() {
		return this.siglaOrdTipo;
	}

	public void setSiglaOrdTipo(String siglaOrdTipo) {
		this.siglaOrdTipo = siglaOrdTipo;
	}

	public String getValidaItemservI() {
		return this.validaItemservI;
	}

	public void setValidaItemservI(String validaItemservI) {
		this.validaItemservI = validaItemservI;
	}

	public String getValidaItemservS() {
		return this.validaItemservS;
	}

	public void setValidaItemservS(String validaItemservS) {
		this.validaItemservS = validaItemservS;
	}

	public String getValidaPrevItemserv() {
		return this.validaPrevItemserv;
	}

	public void setValidaPrevItemserv(String validaPrevItemserv) {
		this.validaPrevItemserv = validaPrevItemserv;
	}

	public String getValidaPrevRec() {
		return this.validaPrevRec;
	}

	public void setValidaPrevRec(String validaPrevRec) {
		this.validaPrevRec = validaPrevRec;
	}

	public String getValidaRecEquip() {
		return this.validaRecEquip;
	}

	public void setValidaRecEquip(String validaRecEquip) {
		this.validaRecEquip = validaRecEquip;
	}

	public String getValidaRecPessoa() {
		return this.validaRecPessoa;
	}

	public void setValidaRecPessoa(String validaRecPessoa) {
		this.validaRecPessoa = validaRecPessoa;
	}

	public String getValidaRegraConfig() {
		return this.validaRegraConfig;
	}

	public void setValidaRegraConfig(String validaRegraConfig) {
		this.validaRegraConfig = validaRegraConfig;
	}

	public String getValidaSaldoAreaAberta() {
		return this.validaSaldoAreaAberta;
	}

	public void setValidaSaldoAreaAberta(String validaSaldoAreaAberta) {
		this.validaSaldoAreaAberta = validaSaldoAreaAberta;
	}

	public String getValidaTipoExecutor() {
		return this.validaTipoExecutor;
	}

	public void setValidaTipoExecutor(String validaTipoExecutor) {
		this.validaTipoExecutor = validaTipoExecutor;
	}

	public String getValidaTipoPropRecEquip() {
		return this.validaTipoPropRecEquip;
	}

	public void setValidaTipoPropRecEquip(String validaTipoPropRecEquip) {
		this.validaTipoPropRecEquip = validaTipoPropRecEquip;
	}

	public String getValidaTipoPropRecPessoa() {
		return this.validaTipoPropRecPessoa;
	}

	public void setValidaTipoPropRecPessoa(String validaTipoPropRecPessoa) {
		this.validaTipoPropRecPessoa = validaTipoPropRecPessoa;
	}

	public List<OpeCentro2Ord> getOpeCentro2Ords() {
		return this.opeCentro2Ords;
	}

	public void setOpeCentro2Ords(List<OpeCentro2Ord> opeCentro2Ords) {
		this.opeCentro2Ords = opeCentro2Ords;
	}

	public OpeCentro2Ord addOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().add(opeCentro2Ord);
		opeCentro2Ord.setOpeCentro2OrdTipo(this);

		return opeCentro2Ord;
	}

	public OpeCentro2Ord removeOpeCentro2Ord(OpeCentro2Ord opeCentro2Ord) {
		getOpeCentro2Ords().remove(opeCentro2Ord);
		opeCentro2Ord.setOpeCentro2OrdTipo(null);

		return opeCentro2Ord;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCentroConfig> getOpeCentroConfigs() {
		return this.opeCentroConfigs;
	}

	public void setOpeCentroConfigs(List<OpeCentroConfig> opeCentroConfigs) {
		this.opeCentroConfigs = opeCentroConfigs;
	}

	public OpeCentroConfig addOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().add(opeCentroConfig);
		opeCentroConfig.setOpeCentro2OrdTipo(this);

		return opeCentroConfig;
	}

	public OpeCentroConfig removeOpeCentroConfig(OpeCentroConfig opeCentroConfig) {
		getOpeCentroConfigs().remove(opeCentroConfig);
		opeCentroConfig.setOpeCentro2OrdTipo(null);

		return opeCentroConfig;
	}

	public List<OpeCentroPrev> getOpeCentroPrevs() {
		return this.opeCentroPrevs;
	}

	public void setOpeCentroPrevs(List<OpeCentroPrev> opeCentroPrevs) {
		this.opeCentroPrevs = opeCentroPrevs;
	}

	public OpeCentroPrev addOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().add(opeCentroPrev);
		opeCentroPrev.setOpeCentro2OrdTipo(this);

		return opeCentroPrev;
	}

	public OpeCentroPrev removeOpeCentroPrev(OpeCentroPrev opeCentroPrev) {
		getOpeCentroPrevs().remove(opeCentroPrev);
		opeCentroPrev.setOpeCentro2OrdTipo(null);

		return opeCentroPrev;
	}

}