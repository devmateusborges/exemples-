package br.com.resultfacil.resultserver.utils.storage;



import java.nio.file.Files;
import java.nio.file.Path;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.util.FileCopyUtils;

import br.com.resultfacil.resultserver.exceptions.StorageException;
import br.com.resultfacil.resultserver.properties.StorageProperties;

public class FileLocalStorageService implements FileStorageService {

	@Autowired
	private StorageProperties storageProperties;
	
	@Override
	public FileDow dowFile(String fileName) {
		try {
			Path fileStoragePath = getFileStoragePath(fileName);

			FileDow fileDow = FileDow.builder()
					.inputStream(Files.newInputStream(fileStoragePath))
					.build();
			
			return fileDow;
		} catch (Exception e) {
			throw new StorageException("Não foi possível baixar o arquivo", e);
		}
	}
	
	@Override
	public void upfile(FileNew fileNew) {
		try {
			Path fileStoragePath = getFileStoragePath(fileNew.getFileName());
			
			FileCopyUtils.copy(fileNew.getInputStream(), 
					Files.newOutputStream(fileStoragePath));
		} catch (Exception e) {
			throw new StorageException("Não foi possível salvar o arquivo", e);
		}
	}
	
	@Override
	public void delFile(String fileName) {
		try {
			Path fileStoragePath = getFileStoragePath(fileName);
			
			Files.deleteIfExists(fileStoragePath);
		} catch (Exception e) {
			throw new StorageException("Não foi possível excluir arquivo", e);
		}
	}

	private Path getFileStoragePath(String fileName) {
		return storageProperties.getLocal().getDirectoryFiles()
				.resolve(Path.of(fileName));
	}

}