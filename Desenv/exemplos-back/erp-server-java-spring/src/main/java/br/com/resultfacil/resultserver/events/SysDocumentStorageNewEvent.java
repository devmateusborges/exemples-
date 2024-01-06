package br.com.resultfacil.resultserver.events;

import org.springframework.context.ApplicationEvent;

import br.com.resultfacil.resultserver.models.SysDocument;
import lombok.Getter;

@Getter
public class SysDocumentStorageNewEvent extends ApplicationEvent {
	public SysDocument sysDocument;
	public String oldFileName;
	
	public SysDocumentStorageNewEvent(Object source, SysDocument sysDocument, String oldFileName) {
		super(source);
		this.sysDocument = sysDocument;
		this.oldFileName = oldFileName;
	}

}
