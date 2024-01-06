package br.com.resultfacil.resultserver.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Service;

import br.com.resultfacil.resultserver.models.SysUnit;
import br.com.resultfacil.resultserver.models.SysUnitDTO;
import br.com.resultfacil.resultserver.repositories.SysUnitRepository;
import br.com.resultfacil.resultserver.services.base.BaseService;

@Service
public class SysUnitService implements BaseService<SysUnit, SysUnitDTO, String> {

    @Autowired
    private SysUnitRepository repository;

    @Override
    public JpaRepository<SysUnit, String> getBaseRepository() {

        return repository;
    }

    @Override
    public SysUnit getDTOToModel(SysUnitDTO dto) {
        SysUnit entity = new SysUnit();
        entity.setId(dto.getId());
        entity.setLogDateIns(dto.getLogDateIns());
        entity.setLogDateUpd(dto.getLogDateUpd());
        entity.setLogUserIns(dto.getLogUserIns());
        entity.setLogUserUpd(dto.getLogUserUpd());
        entity.setConnectionName(dto.getConnectionName());
        entity.setName(dto.getName());
        entity.setSiglaUnit(dto.getSiglaUnit());
        return entity;
    }

    @Override
    public SysUnitDTO getModelToDTO(SysUnit entity) {
        SysUnitDTO dto = new SysUnitDTO();
        dto.setId(entity.getId());
        dto.setLogDateIns(entity.getLogDateIns());
        dto.setLogDateUpd(entity.getLogDateUpd());
        dto.setLogUserIns(entity.getLogUserIns());
        dto.setLogUserUpd(entity.getLogUserUpd());
        dto.setConnectionName(entity.getConnectionName());
        dto.setName(entity.getName());
        dto.setSiglaUnit(entity.getSiglaUnit());
        return dto;
    }    

}
