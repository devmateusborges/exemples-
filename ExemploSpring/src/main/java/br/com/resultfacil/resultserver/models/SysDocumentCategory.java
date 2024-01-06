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
@Table(name="sys_document_category")
@NamedQuery(name="SysDocumentCategory.findAll", query="SELECT s FROM SysDocumentCategory s")
public class SysDocumentCategory implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@CreationTimestamp
@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(length=2147483647)
	private String name;

	//bi-directional many-to-one association to SysDocument
	@OneToMany(mappedBy="sysDocumentCategory")
	private List<SysDocument> sysDocuments;

	public SysDocumentCategory() {
	}

	public String getId() {
		return this.id;
	}

	public void setId(String id) {
		this.id = id;
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

	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public List<SysDocument> getSysDocuments() {
		return this.sysDocuments;
	}

	public void setSysDocuments(List<SysDocument> sysDocuments) {
		this.sysDocuments = sysDocuments;
	}

	public SysDocument addSysDocument(SysDocument sysDocument) {
		getSysDocuments().add(sysDocument);
		sysDocument.setSysDocumentCategory(this);

		return sysDocument;
	}

	public SysDocument removeSysDocument(SysDocument sysDocument) {
		getSysDocuments().remove(sysDocument);
		sysDocument.setSysDocumentCategory(null);

		return sysDocument;
	}

}