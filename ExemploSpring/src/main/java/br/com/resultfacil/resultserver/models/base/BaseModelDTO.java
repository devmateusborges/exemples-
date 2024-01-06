package br.com.resultfacil.resultserver.models.base;

import java.time.OffsetDateTime;

import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
public class BaseModelDTO  {

	public String id;

	public OffsetDateTime  logDateIns;
	
	public OffsetDateTime  logDateUpd;
	
	public String logUserIns;

	public String logUserUpd;
	

}