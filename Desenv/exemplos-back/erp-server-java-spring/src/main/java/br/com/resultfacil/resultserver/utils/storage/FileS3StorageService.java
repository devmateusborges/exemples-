package br.com.resultfacil.resultserver.utils.storage;

import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.model.CannedAccessControlList;
import com.amazonaws.services.s3.model.DeleteObjectRequest;
import com.amazonaws.services.s3.model.ObjectMetadata;
import com.amazonaws.services.s3.model.PutObjectRequest;

import org.springframework.beans.factory.annotation.Autowired;

import br.com.resultfacil.resultserver.exceptions.StorageException;
import br.com.resultfacil.resultserver.properties.StorageProperties;

public class FileS3StorageService implements FileStorageService {

    @Autowired
	private AmazonS3 amazonS3;
	
	@Autowired
	private StorageProperties storageProperties;
    
    @Override
    public FileDow dowFile(String fileName) {
        // TODO FileS3StorageService > FileDow
        return null;
    }

    @Override
    public void upfile(FileNew fileNew) {
        try {
			String fileStoragePath = getFileStoragePath(fileNew.getFileName());
			
			ObjectMetadata objectMetadata = new ObjectMetadata();
			objectMetadata.setContentType(fileNew.getContentType());
			
			PutObjectRequest putObjectRequest = new PutObjectRequest(
					storageProperties.getS3().getBucket(),
					fileStoragePath,
					fileNew.getInputStream(),
					objectMetadata)
				.withCannedAcl(CannedAccessControlList.PublicRead);
			
			amazonS3.putObject(putObjectRequest);
		} catch (Exception e) {
			throw new StorageException("Não foi possível enviar arquivo para Nuvem", e);
		}
        
    }

    @Override
    public void delFile(String fileName) {
        try {
			String fileStoragePath = getFileStoragePath(fileName);

			DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest(
					storageProperties.getS3().getBucket(), fileStoragePath);

			amazonS3.deleteObject(deleteObjectRequest);
		} catch (Exception e) {
			throw new StorageException("Não foi possível excluir arquivo na Nuvem", e);
		}
        
    }
    
    private String getFileStoragePath(String fileName) {
		return String.format("%s/%s", storageProperties.getS3().getDirectoryFiles(), fileName);
	}
}
