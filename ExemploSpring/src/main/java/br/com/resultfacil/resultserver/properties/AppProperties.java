package br.com.resultfacil.resultserver.properties;

import java.util.ArrayList;
import java.util.List;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Component
@ConfigurationProperties(prefix = "app")
public class AppProperties {
    private final Auth auth = new Auth();
    private final Cors cors = new Cors();
    private final OAuth2 oauth2 = new OAuth2();

    @Getter
	@Setter
    public static class Auth {
        private String tokenSecret;
        private long tokenExpirationMsec;
    }

    @Getter
	@Setter
    public static class Cors {
        private String[] allowedOrigins;
    }

    @Getter
	@Setter
    public static class OAuth2 {
        private List<String> authorizedRedirectUris = new ArrayList<>();

        public OAuth2 authorizedRedirectUris(List<String> authorizedRedirectUris) {
            this.authorizedRedirectUris = authorizedRedirectUris;
            return this;
        }
    }    
}
