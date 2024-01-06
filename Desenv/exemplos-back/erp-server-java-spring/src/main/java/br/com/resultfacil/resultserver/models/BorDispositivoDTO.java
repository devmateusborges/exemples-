package br.com.resultfacil.resultserver.models;

import javax.validation.Valid;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

import br.com.resultfacil.resultserver.models.base.BaseModelDTO;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Setter
@Getter
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class BorDispositivoDTO extends BaseModelDTO {


	@NotNull
	@NotBlank
	private String ativo;

	@NotNull
	@NotBlank
	private String nome;
	
	@NotNull
	@NotBlank
	private String numeroSerie;
	
	@NotNull
	@NotBlank
	private String tipo;
	
	@Valid
	private OpeCentro2Equip opeCentro2Equip;
	
	@Valid
	private OpeCentro2Pessoa opeCentro2Pessoa;
	
	@Valid
	@NotNull
	private SysUnitID sysUnit;


	

}