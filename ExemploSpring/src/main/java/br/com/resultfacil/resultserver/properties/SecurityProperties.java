package br.com.resultfacil.resultserver.properties;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Component
@ConfigurationProperties(prefix = "app")
public class SecurityProperties {
    private final Auth auth = new Auth();
    private final Cors cors = new Cors();

    @Getter
	@Setter
    public static class Auth {
        private String tokenSecret;
        private long tokenExpirationMsec;
    }

    @Getter
	@Setter
    public static class Cors {
        private String allowedOrigins;
    }
}
