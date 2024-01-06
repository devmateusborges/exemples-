package br.com.resultfacil.resultserver.properties;


import java.nio.file.Path;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;


import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Component
@ConfigurationProperties("app.storage")
public class StorageProperties {

	private Local local = new Local();
	private S3 s3 = new S3();
	private TypeProvider typeProvider = TypeProvider.LOCAL;
	
	public enum TypeProvider {
		
		LOCAL, S3
		
	}
	
	@Getter
	@Setter
	public class Local {
		
		private Path directoryFiles;
		
	}
	
	@Getter
	@Setter
	public class S3 {
		
		private String acessKey;
		private String secretKey;
		private String endPoint;
		private String bucket;
		private String region;
		private String directoryFiles;
		
	}
	
}