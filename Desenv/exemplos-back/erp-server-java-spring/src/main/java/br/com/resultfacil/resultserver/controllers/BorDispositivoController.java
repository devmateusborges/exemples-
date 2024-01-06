package br.com.resultfacil.resultserver.controllers;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.resultfacil.resultserver.services.BorDispositivoService;
import br.com.resultfacil.resultserver.services.base.BaseService;
import br.com.resultfacil.resultserver.controllers.base.BaseController;
import br.com.resultfacil.resultserver.models.BorDispositivo;
import br.com.resultfacil.resultserver.models.BorDispositivoDTO;


@RestController
@RequestMapping(path = "/bor/bordispositivo",produces = MediaType.APPLICATION_JSON_VALUE)
public class BorDispositivoController implements  BaseController<BorDispositivo,BorDispositivoDTO,String>{

    @Autowired
    private BorDispositivoService service;

    @Override
    public BaseService<BorDispositivo, BorDispositivoDTO, String> getService() {
        return service;
    }



 
	
}