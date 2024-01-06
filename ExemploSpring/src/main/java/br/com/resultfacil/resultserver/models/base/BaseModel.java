package br.com.resultfacil.resultserver.models.base;

import java.io.Serializable;
import javax.persistence.*;

import java.time.OffsetDateTime;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;
import org.springframework.data.domain.AbstractAggregateRoot;

import lombok.Data;
import lombok.EqualsAndHashCode;

@Data
@MappedSuperclass
public class BaseModel extends AbstractAggregateRoot<BaseModel> implements Serializable  {
	private static final long serialVersionUID = 1L;

	@EqualsAndHashCode.Include
	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	@Column(unique=true, nullable=false, length=36)
	private String id;

	@CreationTimestamp
	@Column(name="log_date_ins")
	private OffsetDateTime  logDateIns;
	
	@UpdateTimestamp
	@Column(name="log_date_upd")
	private OffsetDateTime  logDateUpd;

	@Column(name="log_user_ins", length=100)
	private String logUserIns;

	@Column(name="log_user_upd", length=100)
	private String logUserUpd;


}