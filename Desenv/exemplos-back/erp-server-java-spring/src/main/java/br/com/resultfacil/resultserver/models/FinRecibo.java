package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.math.BigDecimal;
import java.util.Date;
import java.sql.Timestamp;
import java.util.List;


import org.hibernate.annotations.CreationTimestamp;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="fin_recibo")
@NamedQuery(name="FinRecibo.findAll", query="SELECT f FROM FinRecibo f")
public class FinRecibo implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(nullable=false, length=2147483647)
	private String conteudo;

	@Temporal(TemporalType.DATE)
	@Column(name="data_recibo")
	private Date dataRecibo;

	@Column(name="ger_pessoa_endereco_id", length=36)
	private String gerPessoaEnderecoId;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="nome_pessoa", length=100)
	private String nomePessoa;

	@Column(name="nr_doc_pessoa", length=50)
	private String nrDocPessoa;

	@Column(nullable=false, length=2)
	private String status;

	@Column(name="status_observacao", length=250)
	private String statusObservacao;

	@Column(name="tipo_doc_pessoa", length=50)
	private String tipoDocPessoa;

	@Column(name="unit_id", nullable=false, length=36)
	private String unitId;

	@Column(nullable=false, precision=18, scale=2)
	private BigDecimal valor;

	//bi-directional many-to-one association to FinPagrecOrigem
	@OneToMany(mappedBy="finRecibo")
	private List<FinPagrecOrigem> finPagrecOrigems;

	public FinRecibo() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getConteudo() {
		return this.conteudo;
	}

	public void setConteudo(String conteudo) {
		this.conteudo = conteudo;
	}

	public Date getDataRecibo() {
		return this.dataRecibo;
	}

	public void setDataRecibo(Date dataRecibo) {
		this.dataRecibo = dataRecibo;
	}

	public String getGerPessoaEnderecoId() {
		return this.gerPessoaEnderecoId;
	}

	public void setGerPessoaEnderecoId(String gerPessoaEnderecoId) {
		this.gerPessoaEnderecoId = gerPessoaEnderecoId;
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

	public String getNomePessoa() {
		return this.nomePessoa;
	}

	public void setNomePessoa(String nomePessoa) {
		this.nomePessoa = nomePessoa;
	}

	public String getNrDocPessoa() {
		return this.nrDocPessoa;
	}

	public void setNrDocPessoa(String nrDocPessoa) {
		this.nrDocPessoa = nrDocPessoa;
	}

	public String getStatus() {
		return this.status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public String getStatusObservacao() {
		return this.statusObservacao;
	}

	public void setStatusObservacao(String statusObservacao) {
		this.statusObservacao = statusObservacao;
	}

	public String getTipoDocPessoa() {
		return this.tipoDocPessoa;
	}

	public void setTipoDocPessoa(String tipoDocPessoa) {
		this.tipoDocPessoa = tipoDocPessoa;
	}

	public String getUnitId() {
		return this.unitId;
	}

	public void setUnitId(String unitId) {
		this.unitId = unitId;
	}

	public BigDecimal getValor() {
		return this.valor;
	}

	public void setValor(BigDecimal valor) {
		this.valor = valor;
	}

	public List<FinPagrecOrigem> getFinPagrecOrigems() {
		return this.finPagrecOrigems;
	}

	public void setFinPagrecOrigems(List<FinPagrecOrigem> finPagrecOrigems) {
		this.finPagrecOrigems = finPagrecOrigems;
	}

	public FinPagrecOrigem addFinPagrecOrigem(FinPagrecOrigem finPagrecOrigem) {
		getFinPagrecOrigems().add(finPagrecOrigem);
		finPagrecOrigem.setFinRecibo(this);

		return finPagrecOrigem;
	}

	public FinPagrecOrigem removeFinPagrecOrigem(FinPagrecOrigem finPagrecOrigem) {
		getFinPagrecOrigems().remove(finPagrecOrigem);
		finPagrecOrigem.setFinRecibo(null);

		return finPagrecOrigem;
	}

}