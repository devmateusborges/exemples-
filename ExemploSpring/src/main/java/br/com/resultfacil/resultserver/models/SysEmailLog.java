package br.com.resultfacil.resultserver.models;

import java.io.Serializable;
import javax.persistence.*;



import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@EqualsAndHashCode(onlyExplicitlyIncluded = true, callSuper = false)
@Entity
@Table(name="sys_email_log")
@NamedQuery(name="SysEmailLog.findAll", query="SELECT s FROM SysEmailLog s")
public class SysEmailLog implements Serializable {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	public SysEmailLog() {
	}

}