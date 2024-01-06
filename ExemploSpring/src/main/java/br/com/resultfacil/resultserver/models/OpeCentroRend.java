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
@Table(name="ope_centro_rend")
@NamedQuery(name="OpeCentroRend.findAll", query="SELECT o FROM OpeCentroRend o")
public class OpeCentroRend implements Serializable {
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

	@Column(length=250)
	private String observacao;

	//bi-directional many-to-one association to OpeAtividade
	@ManyToOne
	@JoinColumn(name="ope_atividade_id", nullable=false)
	private OpeAtividade opeAtividade;

	//bi-directional many-to-one association to OpeCentroVersao
	@ManyToOne
	@JoinColumn(name="ope_centro_versao_id", nullable=false)
	private OpeCentroVersao opeCentroVersao;

	//bi-directional many-to-one association to SysUnit
	@ManyToOne
	@JoinColumn(name="unit_id", nullable=false)
	private SysUnit sysUnit;

	//bi-directional many-to-one association to OpeCentroRendFator
	@OneToMany(mappedBy="opeCentroRend")
	private List<OpeCentroRendFator> opeCentroRendFators;

	public OpeCentroRend() {
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

	public String getObservacao() {
		return this.observacao;
	}

	public void setObservacao(String observacao) {
		this.observacao = observacao;
	}

	public OpeAtividade getOpeAtividade() {
		return this.opeAtividade;
	}

	public void setOpeAtividade(OpeAtividade opeAtividade) {
		this.opeAtividade = opeAtividade;
	}

	public OpeCentroVersao getOpeCentroVersao() {
		return this.opeCentroVersao;
	}

	public void setOpeCentroVersao(OpeCentroVersao opeCentroVersao) {
		this.opeCentroVersao = opeCentroVersao;
	}

	public SysUnit getSysUnit() {
		return this.sysUnit;
	}

	public void setSysUnit(SysUnit sysUnit) {
		this.sysUnit = sysUnit;
	}

	public List<OpeCentroRendFator> getOpeCentroRendFators() {
		return this.opeCentroRendFators;
	}

	public void setOpeCentroRendFators(List<OpeCentroRendFator> opeCentroRendFators) {
		this.opeCentroRendFators = opeCentroRendFators;
	}

	public OpeCentroRendFator addOpeCentroRendFator(OpeCentroRendFator opeCentroRendFator) {
		getOpeCentroRendFators().add(opeCentroRendFator);
		opeCentroRendFator.setOpeCentroRend(this);

		return opeCentroRendFator;
	}

	public OpeCentroRendFator removeOpeCentroRendFator(OpeCentroRendFator opeCentroRendFator) {
		getOpeCentroRendFators().remove(opeCentroRendFator);
		opeCentroRendFator.setOpeCentroRend(null);

		return opeCentroRendFator;
	}

}