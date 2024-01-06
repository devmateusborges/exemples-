package br.com.resultfacil.resultserver.configs;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import br.com.resultfacil.resultserver.properties.StorageProperties;

import br.com.resultfacil.resultserver.properties.StorageProperties.TypeProvider;
import br.com.resultfacil.resultserver.utils.storage.FileLocalStorageService;
import br.com.resultfacil.resultserver.utils.storage.FileS3StorageService;
import br.com.resultfacil.resultserver.utils.storage.FileStorageService;

import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;

@Configuration
public class StorageConfig {

    @Autowired
    private StorageProperties storageProperties;

    @Bean
    @ConditionalOnProperty(name = "app.storage.type-provider", havingValue = "s3")
    public AmazonS3 s3() {
        BasicAWSCredentials credentials = new BasicAWSCredentials(
                storageProperties.getS3().getAcessKey(),
                storageProperties.getS3().getSecretKey());

        return AmazonS3ClientBuilder.standard()
                .withCredentials(new AWSStaticCredentialsProvider(credentials))
                .withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration(storageProperties.getS3().getEndPoint(), storageProperties.getS3().getRegion()))
                .build();
    }

    @Bean
    public FileStorageService fileStorageService() {
        if (TypeProvider.S3.equals(storageProperties.getTypeProvider())) {
            return new FileS3StorageService();
        } else {
            return new FileLocalStorageService();
        }
    }

}
