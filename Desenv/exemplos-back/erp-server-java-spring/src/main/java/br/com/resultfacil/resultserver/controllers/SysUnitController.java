package br.com.resultfacil.resultserver.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.resultfacil.resultserver.services.SysUnitService;
import br.com.resultfacil.resultserver.services.base.BaseService;
import br.com.resultfacil.resultserver.controllers.base.BaseController;
import br.com.resultfacil.resultserver.models.SysUnit;
import br.com.resultfacil.resultserver.models.SysUnitDTO;


@RestController
@RequestMapping(path = "/sys/sysunit",produces = MediaType.APPLICATION_JSON_VALUE)
public class SysUnitController implements  BaseController<SysUnit,SysUnitDTO,String>{

    @Autowired
    private SysUnitService service;

    @Override
    public BaseService<SysUnit, SysUnitDTO, String> getService() {
        return service;
    }

 
	
}