package br.com.resultfacil.resultserver.configs;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.BeanIds;

import br.com.resultfacil.resultserver.properties.AppProperties;
import br.com.resultfacil.resultserver.securities.CustomUserDetailsService;
import br.com.resultfacil.resultserver.securities.RestAuthenticationEntryPoint;
import br.com.resultfacil.resultserver.securities.TokenAuthenticationFilter;
import br.com.resultfacil.resultserver.securities.oauth2.CustomOAuth2UserService;
import br.com.resultfacil.resultserver.securities.oauth2.HttpCookieOAuth2AuthorizationRequestRepository;
import br.com.resultfacil.resultserver.securities.oauth2.OAuth2AuthenticationFailureHandler;
import br.com.resultfacil.resultserver.securities.oauth2.OAuth2AuthenticationSuccessHandler;
import org.springframework.web.cors.CorsConfiguration;

import java.util.Arrays;
import java.util.List;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
@EnableGlobalMethodSecurity(
        securedEnabled = true,
        jsr250Enabled = true,
        prePostEnabled = true
)
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {

  @Autowired
  private AppProperties appProperties;

  @Autowired
  private CustomUserDetailsService customUserDetailsService;

  @Autowired
  private CustomOAuth2UserService customOAuth2UserService;

  @Autowired
  private OAuth2AuthenticationSuccessHandler oAuth2AuthenticationSuccessHandler;

  @Autowired
  private OAuth2AuthenticationFailureHandler oAuth2AuthenticationFailureHandler;

  @Autowired
  private HttpCookieOAuth2AuthorizationRequestRepository httpCookieOAuth2AuthorizationRequestRepository;
  
  @Bean
  public TokenAuthenticationFilter tokenAuthenticationFilter() {
    return new TokenAuthenticationFilter();
  }

  @Bean
  public HttpCookieOAuth2AuthorizationRequestRepository cookieAuthorizationRequestRepository() {
      return new HttpCookieOAuth2AuthorizationRequestRepository();
  }

  @Override
  public void configure(AuthenticationManagerBuilder authenticationManagerBuilder) throws Exception {
      authenticationManagerBuilder
              .userDetailsService(customUserDetailsService)
              .passwordEncoder(passwordEncoder());
  }

  @Bean
  public PasswordEncoder passwordEncoder() {
      return new BCryptPasswordEncoder();
  }

  @Bean(BeanIds.AUTHENTICATION_MANAGER)
  @Override
  protected AuthenticationManager authenticationManager() throws Exception {
    return super.authenticationManager();
  }

  @Override
  protected void configure(HttpSecurity http) throws Exception {

    CorsConfiguration corsConfiguration = new CorsConfiguration();
    corsConfiguration.setAllowedHeaders(Arrays.asList("*"));
    corsConfiguration.setAllowedOrigins(Arrays.asList(appProperties.getCors().getAllowedOrigins()));
    corsConfiguration.setAllowedMethods(Arrays.asList("GET", "POST", "PUT", "DELETE", "PUT","OPTIONS","PATCH", "DELETE"));
    corsConfiguration.setAllowCredentials(true);
    corsConfiguration.setExposedHeaders(Arrays.asList("Authorization"));

      http
      .cors().configurationSource(request -> corsConfiguration)
          .and()
      .sessionManagement()
          .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
          .and()
      .csrf()
          .disable()
      .formLogin()
          .disable()
      .httpBasic()
          .disable()
      .authorizeRequests()
          .antMatchers("/",
              "/error",
              "/favicon.ico",
              "/**/*.png",
              "/**/*.gif",
              "/**/*.svg",
              "/**/*.jpg",
              "/**/*.html",
              "/**/*.css",
              "/**/*.js")
              .permitAll()
          .antMatchers("/auth/**", "/oauth2/**")
              .permitAll()
          .anyRequest()
              .authenticated()
          .and()
      .exceptionHandling()
          .authenticationEntryPoint(new RestAuthenticationEntryPoint())
          .and()          
      .oauth2Login()
          .authorizationEndpoint()
              .baseUri("/oauth2/authorize")
              .authorizationRequestRepository(cookieAuthorizationRequestRepository())
              .and()
          .redirectionEndpoint()
              .baseUri("/oauth2/callback/*")
              .and()
          .userInfoEndpoint()
              .userService(customOAuth2UserService)
              .and()
          .successHandler(oAuth2AuthenticationSuccessHandler)
          .failureHandler(oAuth2AuthenticationFailureHandler);

  // Add our custom Token based authentication filter
  http.addFilterBefore(tokenAuthenticationFilter(), UsernamePasswordAuthenticationFilter.class);
  }



  @Override
  protected UserDetailsService userDetailsService() {
    return customUserDetailsService;
  }
}