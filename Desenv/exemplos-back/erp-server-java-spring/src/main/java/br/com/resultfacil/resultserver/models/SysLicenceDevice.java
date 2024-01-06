package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;
import java.sql.Timestamp;



import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="sys_licence_device")
@NamedQuery(name="SysLicenceDevice.findAll", query="SELECT s FROM SysLicenceDevice s")
public class SysLicenceDevice implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="log_date_ins", nullable=false)
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", nullable=false, length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="sigla_device", nullable=false, length=100)
	private String siglaDevice;

	//bi-directional many-to-one association to SysLicence
	@ManyToOne
	@JoinColumn(name="sys_licence_id", nullable=false)
	private SysLicence sysLicence;

	public SysLicenceDevice() {
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

	public String getSiglaDevice() {
		return this.siglaDevice;
	}

	public void setSiglaDevice(String siglaDevice) {
		this.siglaDevice = siglaDevice;
	}

	public SysLicence getSysLicence() {
		return this.sysLicence;
	}

	public void setSysLicence(SysLicence sysLicence) {
		this.sysLicence = sysLicence;
	}

}