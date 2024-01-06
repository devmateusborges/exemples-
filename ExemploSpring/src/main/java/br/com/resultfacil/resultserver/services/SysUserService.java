package br.com.resultfacil.resultserver.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Service;

import br.com.resultfacil.resultserver.models.SysUser;
import br.com.resultfacil.resultserver.models.SysUserDTO;
import br.com.resultfacil.resultserver.repositories.SysUserRepository;
import br.com.resultfacil.resultserver.services.base.BaseService;

@Service
public class SysUserService implements BaseService<SysUser, SysUserDTO, String> {

    @Autowired
    private SysUserRepository repository;

    @Override
    public JpaRepository<SysUser, String> getBaseRepository() {

        return repository;
    }

    @Override
    public SysUser getDTOToModel(SysUserDTO dto) {
        SysUser entity = new SysUser();
        entity.setId(dto.getId());
        entity.setLogDateIns(dto.getLogDateIns());
        entity.setLogDateUpd(dto.getLogDateUpd());
        entity.setLogUserIns(dto.getLogUserIns());
        entity.setLogUserUpd(dto.getLogUserUpd());
        entity.setActive(dto.getActive());
        entity.setActiveMessage(dto.getActiveMessage());
        entity.setAdmin(dto.getAdmin());
        entity.setChat(dto.getChat());
        entity.setDocument(dto.getDocument());
        entity.setEmail(dto.getEmail());
        entity.setFrontpageId(dto.getFrontpageId());
        entity.setLogin(dto.getLogin());
        entity.setLoginExt(dto.getLoginExt());
        entity.setName(dto.getName());
        entity.setOrigem(dto.getOrigem());
        entity.setPassword(dto.getPassword());
        entity.setPhone(dto.getPhone());
        entity.setProvider(dto.getProvider());
        entity.setProviderCode(dto.getProviderCode());
        entity.setEmailVerified(dto.getEmailVerified());
        entity.setImageUrl(dto.getImageUrl());
        return entity;
    }

    @Override
    public SysUserDTO getModelToDTO(SysUser entity) {
        SysUserDTO dto = new SysUserDTO();
        dto.setId(entity.getId());
        dto.setLogDateIns(entity.getLogDateIns());
        dto.setLogDateUpd(entity.getLogDateUpd());
        dto.setLogUserIns(entity.getLogUserIns());
        dto.setLogUserUpd(entity.getLogUserUpd());
        dto.setActive(entity.getActive());
        dto.setActiveMessage(entity.getActiveMessage());
        dto.setAdmin(entity.getAdmin());
        dto.setChat(entity.getChat());
        dto.setDocument(entity.getDocument());
        dto.setEmail(entity.getEmail());
        dto.setFrontpageId(entity.getFrontpageId());
        dto.setLogin(entity.getLogin());
        dto.setLoginExt(entity.getLoginExt());
        dto.setName(entity.getName());
        dto.setOrigem(entity.getOrigem());
        dto.setPassword(entity.getPassword());
        dto.setPhone(entity.getPhone());
        dto.setProvider(entity.getProvider());
        dto.setProviderCode(entity.getProviderCode());
        dto.setEmailVerified(entity.getEmailVerified());        
        dto.setImageUrl(entity.getImageUrl());       
        return dto;
    }    


    public SysUserDTO getByLogin(String login) {
        List<SysUser> user = repository.findByLogin(login);
        if (!user.isEmpty()) {
            return this.getModelToDTO(user.get(0));
        } else {
            return null;
        }
    }    



}
