package br.com.resultfacil.resultserver.models;

import javax.persistence.*;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

import br.com.resultfacil.resultserver.enums.AuthProviderEnum;
import br.com.resultfacil.resultserver.models.base.BaseModel;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="sys_user")
@NamedQuery(name="SysUser.findAll", query="SELECT s FROM SysUser s")
public class SysUser extends BaseModel  {


	@NotNull
	@NotBlank	
	@Column(nullable=false, length=1)
	private String active;

	@Column(name="active_message", length=2147483647)
	private String activeMessage;
	
	@NotNull
	@NotBlank
	@Column(length=1)
	private String admin;

	@NotNull
	@NotBlank
	@Column(length=1)
	private String chat;

	@Column(length=50)
	private String document;
	
	@NotNull
	@NotBlank
	@Column(nullable=false, length=100)
	private String email;

	@Column(name="frontpage_id", length=36)
	private String frontpageId;
	
	@NotNull
	@NotBlank
	@Column(nullable=false, length=100)
	private String login;

	@Column(name="login_ext", length=100)
	private String loginExt;

	@NotNull
	@NotBlank
	@Column(nullable=false, length=100)
	private String name;
	
	@NotNull
	@NotBlank
	@Column(length=1)
	private String origem;

	@NotNull
	@NotBlank
	@Column(nullable=false, length=100)
	private String password;

	@Column(length=50)
	private String phone;
	
	@NotNull
    @Enumerated(EnumType.STRING)
	@Column(name="provider", length=50)
	private AuthProviderEnum  provider;
	
	@Column(name="provider_code",length=50)
	private String providerCode;
	
	@NotNull
	@NotBlank
	@Column(name="email_verified", length=1)
	private String emailVerified;

	@Column(name="image_url",length=1000)
	private String imageUrl;	
}