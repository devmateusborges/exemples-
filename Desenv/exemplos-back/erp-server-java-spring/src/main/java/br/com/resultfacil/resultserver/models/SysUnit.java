package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

import br.com.resultfacil.resultserver.models.base.BaseModel;
import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="sys_unit")
@NamedQuery(name="SysUnit.findAll", query="SELECT s FROM SysUnit s")
public class SysUnit extends BaseModel  {



	@NotNull
	@NotBlank
	@Column(name="connection_name", length=50)
	private String connectionName;

	@Column(name="img_logo")
	private byte[] imgLogo;

	@NotNull
	@NotBlank
	@Column(nullable=false, length=100)
	private String name;
	@NotNull
	@NotBlank
	@Column(name="sigla_unit", nullable=false, length=100)
	private String siglaUnit;


	
}