package br.com.resultfacil.resultserver.services.base;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import javax.validation.Valid;
import javax.validation.Validator;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.validation.beanvalidation.SpringValidatorAdapter;


public interface BaseService<T,DTO,ID> {


     
    JpaRepository<T, ID> getBaseRepository();

    T getDTOToModel(DTO dto);
    DTO getModelToDTO(T t);

    default public DTO findById(ID id) {
        Optional<T> result = getBaseRepository().findById(id);
        return this.getModelToDTO(result.get());
    }


    default public List<DTO> findAll() {
        List<T> list = getBaseRepository().findAll();
        return list.stream().map(x -> this.getModelToDTO(x)).collect(Collectors.toList());
    }

    @Transactional
	default public void delete(ID id) {
        getBaseRepository().deleteById(id);
	}
    
    @Transactional
    default public DTO save(@Valid DTO dto) {
        
        T entity = this.getDTOToModel(dto);
        
        T result = getBaseRepository().save(entity);
        return this.getModelToDTO(result);
	}


   


}