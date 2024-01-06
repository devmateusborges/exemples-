package br.com.resultfacil.resultserver.events;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;
import org.springframework.transaction.event.TransactionPhase;
import org.springframework.transaction.event.TransactionalEventListener;

import br.com.resultfacil.resultserver.models.SysDocument;
import br.com.resultfacil.resultserver.utils.storage.FileStorageService;
import br.com.resultfacil.resultserver.utils.storage.FileStorageService.FileNew;

@Component
public class SysDocumentStorageListener {

	@Autowired
	private FileStorageService fileStorageService;

	@TransactionalEventListener(fallbackExecution = true, phase = TransactionPhase.AFTER_COMMIT)
	public void storageNewListener(SysDocumentStorageNewEvent event) {
		System.out.println(">>>SysDocumentStorageListener>storageNewListener");
		if (event.getSysDocument().getInputStream() != null)  {

			SysDocument sysDocument = event.getSysDocument();
			FileNew fileNew = FileNew.builder()
			.contentType(sysDocument.getContentType())
			.fileName(sysDocument.getFilename())
			.inputStream(sysDocument.getInputStream())
			.build();
			
			fileStorageService.repFile(event.getOldFileName(),fileNew);
		};

	}
	@TransactionalEventListener(fallbackExecution = true, phase = TransactionPhase.AFTER_COMMIT)
	public void storageDelListener(SysDocumentStorageDelEvent event) {
		System.out.println(">>>SysDocumentStorageListener>storageDelListener");
		SysDocument sysDocument = event.getSysDocument();

		fileStorageService.delFile(sysDocument.getFilename());

	}

}