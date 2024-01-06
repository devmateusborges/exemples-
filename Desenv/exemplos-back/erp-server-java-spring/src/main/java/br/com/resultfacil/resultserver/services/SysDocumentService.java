package br.com.resultfacil.resultserver.services;


import java.io.ByteArrayInputStream;
import java.util.Base64;

import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Service;

import br.com.resultfacil.resultserver.events.SysDocumentStorageDelEvent;
import br.com.resultfacil.resultserver.events.SysDocumentStorageNewEvent;
import br.com.resultfacil.resultserver.models.SysDocument;
import br.com.resultfacil.resultserver.models.SysDocumentDTO;
import br.com.resultfacil.resultserver.repositories.SysDocumentRepository;
import br.com.resultfacil.resultserver.services.base.BaseService;
import br.com.resultfacil.resultserver.utils.ConstUtil;
import br.com.resultfacil.resultserver.utils.storage.FileStorageService;
import br.com.resultfacil.resultserver.utils.storage.FileStorageService.FileDow;

@Service
public class SysDocumentService implements  BaseService<SysDocument,SysDocumentDTO,String>{

    @Autowired
    private ApplicationEventPublisher applicationEventPublisher;
    
    @Autowired
    private SysDocumentRepository repository;
    
    @Autowired
    private FileStorageService fileStorageService;
    

    @Override
    public JpaRepository<SysDocument, String> getBaseRepository() {
        
        return repository;
    }

    @Override
    public SysDocument getDTOToModel(SysDocumentDTO dto) {
            SysDocument entity  = new SysDocument();
    
            entity.setId(dto.getId());
            entity.setLogDateIns(dto.getLogDateIns());
            entity.setLogDateUpd(dto.getLogDateUpd());
            entity.setLogUserIns(dto.getLogUserIns());
            entity.setLogUserUpd(dto.getLogUserUpd());
            entity.setArchiveDate(dto.getArchiveDate());
            entity.setDescription(dto.getDescription());
            entity.setFilename(dto.getFilename());
            entity.setContentType(dto.getContentType());
            entity.setSubmissionDate(dto.getSubmissionDate());
            if (!dto.getFile64().equals(ConstUtil.APP_NOT_UPDATE)) {
                entity.setInputStream(new ByteArrayInputStream(Base64.getDecoder().decode(dto.getFile64())));
            } else {
                entity.setInputStream(null);
            }
            entity.setTitle(dto.getTitle());

            return entity;
    
    }

    @Override
    public SysDocumentDTO getModelToDTO(SysDocument model) {
            SysDocumentDTO dto  = new SysDocumentDTO();
    
            dto.setId(model.getId());
            dto.setLogDateIns(model.getLogDateIns());
            dto.setLogDateUpd(model.getLogDateUpd());
            dto.setLogUserIns(model.getLogUserIns());
            dto.setLogUserUpd(model.getLogUserUpd());
            dto.setArchiveDate(model.getArchiveDate());
            dto.setDescription(model.getDescription());
            dto.setFilename(model.getFilename());
            dto.setContentType(model.getContentType());
            dto.setSubmissionDate(model.getSubmissionDate());
            dto.setTitle(model.getTitle());
            return dto;
    
    }    

    @Transactional
    @Override
    public SysDocumentDTO save(SysDocumentDTO dto) {
        String oldFileName = "";
        SysDocument modelSave = getBaseRepository().findById(dto.id).orElse(null);
        
        if (!dto.getFile64().equals(ConstUtil.APP_NOT_UPDATE)) {
            dto.setFilename(fileStorageService.generateFileName(dto.getFilename())); 
        }

        if (modelSave != null) {
            oldFileName = modelSave.getFilename();
        }
        
        modelSave = this.getDTOToModel(dto);
        
        
        
        SysDocumentStorageNewEvent sysDocumentStorageNewEvent = new SysDocumentStorageNewEvent(modelSave, modelSave,oldFileName);
        applicationEventPublisher.publishEvent(sysDocumentStorageNewEvent);
        SysDocumentDTO dtoSave = BaseService.super.save(dto);
        return dtoSave;
    }    
    

    @Transactional
    @Override
    public void delete(String id) {
        SysDocument modelSave = getBaseRepository().findById(id).get();
        SysDocumentStorageDelEvent sysDocumentStorageDelEvent = new SysDocumentStorageDelEvent(modelSave, modelSave);
        applicationEventPublisher.publishEvent(sysDocumentStorageDelEvent);
        getBaseRepository().deleteById(id);
    }    


    public FileDow getFileById(String id) {
        SysDocument modelSave = getBaseRepository().findById(id).get();
        return fileStorageService.dowFile(modelSave.getFilename());
    }    


    
}
