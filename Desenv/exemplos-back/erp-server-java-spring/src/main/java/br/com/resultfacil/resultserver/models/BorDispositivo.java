package br.com.resultfacil.resultserver.models;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQuery;
import javax.persistence.Table;
import javax.validation.Valid;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

import br.com.resultfacil.resultserver.models.base.BaseModel;
import lombok.Data;
import lombok.EqualsAndHashCode;


@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name = "bor_dispositivo")
@NamedQuery(name = "BorDispositivo.findAll", query = "SELECT b FROM BorDispositivo b")
public class BorDispositivo extends BaseModel  {
	

	@NotNull
	@NotBlank
	@Column(length = 1)
	private String ativo;

	@NotNull
	@NotBlank
	@Column(length = 100)
	private String nome;

	@NotNull
	@NotBlank
	@Column(name = "numero_serie", nullable = false, length = 50)
	private String numeroSerie;
	
	@NotNull
	@NotBlank
	@Column(length = 1)
	private String tipo;

	@ManyToOne
	@JoinColumn(name = "ope_centro2_equip_id")
	private OpeCentro2Equip opeCentro2Equip;

	@Valid
	@ManyToOne
	@JoinColumn(name = "ope_centro2_pessoa_id")
	private OpeCentro2Pessoa opeCentro2Pessoa;

	@Valid
	@NotNull
	@ManyToOne(fetch = FetchType.EAGER)
	@JoinColumn(name = "unit_id", nullable = false)
	private SysUnit sysUnit;


}