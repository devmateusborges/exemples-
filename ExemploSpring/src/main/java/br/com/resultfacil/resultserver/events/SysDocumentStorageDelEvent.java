package br.com.resultfacil.resultserver.events;

import org.springframework.context.ApplicationEvent;

import br.com.resultfacil.resultserver.models.SysDocument;
import lombok.Getter;

@Getter
public class SysDocumentStorageDelEvent extends ApplicationEvent {
	public SysDocument sysDocument;
	
	public SysDocumentStorageDelEvent(Object source, SysDocument sysDocument) {
		super(source);
		this.sysDocument = sysDocument;
	}

}
