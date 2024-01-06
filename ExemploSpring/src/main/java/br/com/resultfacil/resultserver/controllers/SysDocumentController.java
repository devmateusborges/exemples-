package br.com.resultfacil.resultserver.controllers;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.resultfacil.resultserver.services.SysDocumentService;
import br.com.resultfacil.resultserver.services.base.BaseService;
import br.com.resultfacil.resultserver.controllers.base.BaseController;
import br.com.resultfacil.resultserver.models.SysDocument;
import br.com.resultfacil.resultserver.models.SysDocumentDTO;


@RestController
@RequestMapping(path = "/sys/sysdocument",produces = MediaType.APPLICATION_JSON_VALUE)
public class SysDocumentController implements  BaseController<SysDocument,SysDocumentDTO,String>{

    @Autowired
    private SysDocumentService service;

    @Override
    public BaseService<SysDocument, SysDocumentDTO, String> getService() {
        return service;
    }



 
	
}