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
@Table(name="sys_process_log")
@NamedQuery(name="SysProcessLog.findAll", query="SELECT s FROM SysProcessLog s")
public class SysProcessLog implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@Column(name="date_fin_process")
	private Timestamp dateFinProcess;

	@Column(name="date_ini_process", nullable=false)
	private Timestamp dateIniProcess;
	
	@CreationTimestamp
	@Column(name="log_date_ins")
	private Timestamp logDateIns;

	@Column(name="log_date_upd")
	private Timestamp logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;

	@Column(name="param_process", nullable=false, length=2147483647)
	private String paramProcess;

	@Column(nullable=false, length=1)
	private String reversed;

	@Column(name="type_process", nullable=false, length=50)
	private String typeProcess;

	@OneToMany(mappedBy="sysProcessLog")
	private List<CtbLancDet> ctbLancDets;

	@OneToMany(mappedBy="sysProcessLog")
	private List<FinPagrec> finPagrecs;

	@OneToMany(mappedBy="sysProcessLog")
	private List<FinPagrecBancoExtrato> finPagrecBancoExtratos;

	@OneToMany(mappedBy="sysProcessLog")
	private List<FinPagrecBancoTransf> finPagrecBancoTransfs;

	@OneToMany(mappedBy="sysProcessLog")
	private List<FinPagrecPrev> finPagrecPrevs;

	@OneToMany(mappedBy="sysProcessLog")
	private List<OpeCentro2Ord> opeCentro2Ords;

	@OneToMany(mappedBy="sysProcessLog")
	private List<OpeCentroPrev> opeCentroPrevs;

	@OneToMany(mappedBy="sysProcessLog")
	private List<OpeCentroPrevDest> opeCentroPrevDests;

	@OneToMany(mappedBy="sysProcessLog")
	private List<PtoMarcacao> ptoMarcacaos;

	@ManyToOne
	@JoinColumn(name="unit_id")
	private SysUnit sysUnit;

	@ManyToOne
	@JoinColumn(name="sys_user_id", nullable=false)
	private SysUser sysUser;


}