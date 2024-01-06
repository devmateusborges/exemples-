package br.com.resultfacil.resultserver.repositories;

import org.springframework.stereotype.Repository;
import br.com.resultfacil.resultserver.models.SysUnit;
import br.com.resultfacil.resultserver.repositories.base.BaseRepository;

@Repository
public interface SysUnitRepository extends BaseRepository<SysUnit,String> {

}
