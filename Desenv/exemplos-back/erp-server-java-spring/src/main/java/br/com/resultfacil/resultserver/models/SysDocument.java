package br.com.resultfacil.resultserver.models;

import javax.persistence.*;
import javax.validation.Valid;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

import br.com.resultfacil.resultserver.models.base.BaseModel;

import java.io.InputStream;
import java.time.OffsetDateTime;
import java.util.List;


import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="sys_document")
@NamedQuery(name="SysDocument.findAll", query="SELECT s FROM SysDocument s")
public class SysDocument extends BaseModel  {



	@Column(name="archive_date")
	private OffsetDateTime archiveDate;

	@NotNull
	@NotBlank
	@Column(length=2147483647)
	private String description;
	
	@NotNull
	@NotBlank
	@Column(length=2147483647)
	private String filename;
	
	@NotNull
	@NotBlank
	@Column(name="content_type")
	private String contentType;

	@Transient
	private InputStream inputStream;	

	@NotNull
	@Column(name="submission_date")
	private OffsetDateTime submissionDate;
	
	@NotNull
	@NotBlank
	@Column(length=2147483647)
	private String title;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="crm_mov_id")
	private CrmMov crmMov;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="fin_pagrec_id")
	private FinPagrec finPagrec;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="ger_pessoa_id")
	private GerPessoa gerPessoa;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="mov_id")
	private Mov mov;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="ope_centro1_id")
	private OpeCentro1 opeCentro1;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="ope_centro2_id")
	private OpeCentro2 opeCentro2;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="ope_centro2_ord_id")
	private OpeCentro2Ord opeCentro2Ord;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="ope_compart_id")
	private OpeCompart opeCompart;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="ope_compart_ocor_id")
	private OpeCompartOcor opeCompartOcor;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="ope_ocor_id")
	private OpeOcor opeOcor;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="category_id")
	private SysDocumentCategory sysDocumentCategory;

	@Valid
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="sys_user_id")
	private SysUser sysUser;

	@OneToMany(mappedBy="sysDocument",fetch = FetchType.LAZY)
	private List<SysDocumentGroup> sysDocumentGroups;

	@OneToMany(mappedBy="sysDocument",fetch = FetchType.LAZY)
	private List<SysDocumentUser> sysDocumentUsers;

}