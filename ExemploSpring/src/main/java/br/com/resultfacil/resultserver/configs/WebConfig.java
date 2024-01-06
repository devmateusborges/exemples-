package br.com.resultfacil.resultserver.configs;

import javax.servlet.Filter;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.filter.ShallowEtagHeaderFilter;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import br.com.resultfacil.resultserver.properties.AppProperties;

@Configuration
public class WebConfig implements WebMvcConfigurer {
	
	
}
