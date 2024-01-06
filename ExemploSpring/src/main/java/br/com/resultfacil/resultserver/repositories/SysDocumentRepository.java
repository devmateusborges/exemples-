package br.com.resultfacil.resultserver.repositories;

import org.springframework.stereotype.Repository;
import br.com.resultfacil.resultserver.models.SysDocument;
import br.com.resultfacil.resultserver.repositories.base.BaseRepository;

@Repository
public interface SysDocumentRepository extends BaseRepository<SysDocument,String> {

}
