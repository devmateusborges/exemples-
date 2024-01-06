package br.com.resultfacil.resultserver.controllers.base;
import java.util.List;

import javax.validation.Valid;


import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import br.com.resultfacil.resultserver.services.base.BaseService;



public interface BaseController<T,DTO,ID>{


    BaseService<T,DTO,ID> getService();


    @GetMapping(value = "/{id}")
    default ResponseEntity<DTO> findById(@PathVariable ID id){
        DTO obj = getService().findById(id);
        return ResponseEntity.ok(obj);
    }

    @GetMapping
    default ResponseEntity<List<DTO>> findAll(){
        List<DTO> list = getService().findAll();
        return ResponseEntity.ok(list);
    }

    @DeleteMapping("/{id}")	
	default ResponseEntity<String> delete(@PathVariable("id") ID id) {
		getService().delete(id);
		return ResponseEntity.noContent().build();
		
	}

    @PostMapping	
	default ResponseEntity<DTO> save(@RequestBody @Valid  DTO obj) {
        DTO objSave = getService().save(obj);
		return ResponseEntity.ok(objSave);
		
	}
	
}