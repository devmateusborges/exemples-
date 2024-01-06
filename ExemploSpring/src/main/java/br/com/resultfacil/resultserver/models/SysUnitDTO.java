package br.com.resultfacil.resultserver.models;

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
public class SysUnitDTO  extends BaseModelDTO {
	

	@NotNull
	@NotBlank
	private String connectionName;

	private byte[] imgLogo;
	
	@NotNull
	@NotBlank
	private String name;
	
	@NotNull
	@NotBlank
	private String siglaUnit;

	
}