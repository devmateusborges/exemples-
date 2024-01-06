package br.com.resultfacil.resultserver.repositories.base;

import org.springframework.data.jpa.repository.JpaRepository;

import br.com.resultfacil.resultserver.models.base.BaseModel;


public interface BaseRepository<T extends BaseModel,ID> extends JpaRepository<T, ID> {

}