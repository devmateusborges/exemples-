package br.com.resultfacil.resultserver;
import java.util.TimeZone;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;

import br.com.resultfacil.resultserver.properties.AppProperties;

@SpringBootApplication
@EnableConfigurationProperties(AppProperties.class)
public class ResultServerApplication {

	public static void main(String[] args) {
		TimeZone.setDefault(TimeZone.getTimeZone("UTC"));
		SpringApplication.run(ResultServerApplication.class, args);
	}

}
