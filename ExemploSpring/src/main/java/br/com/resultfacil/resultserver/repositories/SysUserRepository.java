package br.com.resultfacil.resultserver.repositories;

import java.util.List;

import org.springframework.stereotype.Repository;
import br.com.resultfacil.resultserver.models.SysUser;
import br.com.resultfacil.resultserver.repositories.base.BaseRepository;

@Repository
public interface SysUserRepository extends BaseRepository<SysUser,String> {

    
    List<SysUser> findByLogin(String login);
    

}
