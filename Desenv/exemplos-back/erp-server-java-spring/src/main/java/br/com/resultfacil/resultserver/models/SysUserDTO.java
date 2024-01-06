package br.com.resultfacil.resultserver.models;


import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

import br.com.resultfacil.resultserver.enums.AuthProviderEnum;
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
public class SysUserDTO extends BaseModelDTO  {


	@NotNull
	@NotBlank
	@Builder.Default
	private String active = "S";

	private String activeMessage;
	
	@NotNull
	@NotBlank
	@Builder.Default
	private String admin = "N";

	@NotNull
	@NotBlank
	@Builder.Default
	private String chat = "N";

	private String document;
	
	@NotNull
	@NotBlank
	private String email;

	private String frontpageId;
	
	@NotNull
	@NotBlank
	private String login;

	private String loginExt;

	@NotNull
	@NotBlank
	private String name;
	
	@NotNull
	@NotBlank
	@Builder.Default
	private String origem = "1";

	@NotNull
	@NotBlank
	@Builder.Default
	private String password = "$2a$12$Kgg6NcAqRD59EF0r2ccRuOHP1PYVbjSv68YnSA6qQ4gWm7lGDtFqC";

	private String phone;

	@NotNull
	@Builder.Default
	private AuthProviderEnum  provider = AuthProviderEnum.local;
	
	private String providerCode;
	
	@NotNull
	@NotBlank
	@Builder.Default
	private String emailVerified = "N";	

	private String imageUrl;

}