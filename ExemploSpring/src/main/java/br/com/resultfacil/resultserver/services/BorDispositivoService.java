package br.com.resultfacil.resultserver.services;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Service;

import br.com.resultfacil.resultserver.exceptions.EntityNotFoundException;
import br.com.resultfacil.resultserver.models.BorDispositivo;
import br.com.resultfacil.resultserver.models.BorDispositivoDTO;
import br.com.resultfacil.resultserver.models.SysUnitID;
import br.com.resultfacil.resultserver.repositories.BorDispositivoRepository;
import br.com.resultfacil.resultserver.repositories.SysUnitRepository;
import br.com.resultfacil.resultserver.services.base.BaseService;

@Service
public class BorDispositivoService implements  BaseService<BorDispositivo,BorDispositivoDTO,String>{

    @Autowired
    private BorDispositivoRepository repository;
    
    @Autowired
    private SysUnitRepository repositorySysUnit;

    @Override
    public JpaRepository<BorDispositivo, String> getBaseRepository() {
        
        return repository;
    }

    @Override
    public BorDispositivo getDTOToModel(BorDispositivoDTO dto) {
            BorDispositivo entity  = new BorDispositivo();
    
            entity.setId(dto.getId());
            entity.setLogDateIns(dto.getLogDateIns());
            entity.setLogDateUpd(dto.getLogDateUpd());
            entity.setLogUserIns(dto.getLogUserIns());
            entity.setLogUserUpd(dto.getLogUserUpd());
            entity.setAtivo(dto.getAtivo());
            entity.setNome(dto.getNome());
            entity.setNumeroSerie(dto.getNumeroSerie());
            entity.setTipo(dto.getTipo());
            entity.setOpeCentro2Equip(dto.getOpeCentro2Equip());
            entity.setOpeCentro2Pessoa(dto.getOpeCentro2Pessoa());
            entity.setSysUnit(repositorySysUnit.findById(dto.getSysUnit().getId()).orElseThrow(() -> new EntityNotFoundException(SysUnitID.class.getName())));
            return entity;
    
    }

    @Override
    public BorDispositivoDTO getModelToDTO(BorDispositivo model) {
            BorDispositivoDTO dto  = new BorDispositivoDTO();
    
            dto.setId(model.getId());
            dto.setLogDateIns(model.getLogDateIns());
            dto.setLogDateUpd(model.getLogDateUpd());
            dto.setLogUserIns(model.getLogUserIns());
            dto.setLogUserUpd(model.getLogUserUpd());
            dto.setAtivo(model.getAtivo());
            dto.setNome(model.getNome());
            dto.setNumeroSerie(model.getNumeroSerie());
            dto.setTipo(model.getTipo());
            dto.setOpeCentro2Equip(model.getOpeCentro2Equip());
            dto.setOpeCentro2Pessoa(model.getOpeCentro2Pessoa());
            dto.setSysUnit(new SysUnitID(model.getSysUnit().getId()));
            return dto;
    
    }    



    
}
