package br.com.resultfacil.resultserver.models;

import java.time.OffsetDateTime;
import java.util.List;

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
public class SysDocumentDTO extends BaseModelDTO {

	private OffsetDateTime archiveDate;

	@NotNull
	@NotBlank
	private String description;
	
	@NotNull
	@NotBlank
	private String filename;

	@NotNull
	@NotBlank
	private String contentType;
	
	@NotNull
	@NotBlank	
	private String file64;	
	
	@NotNull
	private OffsetDateTime submissionDate;
	
	@NotNull
	@NotBlank
	private String title;

	/*
	@Valid
	private CrmMov crmMov;

	@Valid
	private FinPagrec finPagrec;

	@Valid
	private GerPessoa gerPessoa;

	@Valid
	private Mov mov;

	@Valid
	private OpeCentro1 opeCentro1;

	@Valid
	private OpeCentro2 opeCentro2;

	@Valid
	private OpeCentro2Ord opeCentro2Ord;

	@Valid
	private OpeCompart opeCompart;

	@Valid
	private OpeCompartOcor opeCompartOcor;

	@Valid
	private OpeOcor opeOcor;

	@Valid
	private SysDocumentCategory sysDocumentCategory;

	@Valid
	private SysUser sysUser;

	private List<SysDocumentGroup> sysDocumentGroups;

	private List<SysDocumentUser> sysDocumentUsers;
	*/

}