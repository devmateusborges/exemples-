package br.com.resultfacil.resultserver.securities;

import br.com.resultfacil.resultserver.models.SysUserDTO;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.oauth2.core.user.OAuth2User;

import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.Map;

public class UserPrincipal implements OAuth2User, UserDetails {

  private String id;
  private String email;
  private String name;
  private String login;
  private String password;
  private Collection<? extends GrantedAuthority> authorities;
  private Map<String, Object> attributes;


  public UserPrincipal(String id, String email, String name,String login, String password,
      Collection<? extends GrantedAuthority> authorities) {
    this.id = id;
    this.email = email;
    this.name = name;
    this.login = login;
    this.password = password;
    this.authorities = authorities;
  }

  public UserPrincipal(SysUserDTO sysUserDTO) {
    this.id = sysUserDTO.getId();
    this.email = sysUserDTO.getEmail();
    this.name = sysUserDTO.getName();
    this.login = sysUserDTO.getLogin();
    this.password = sysUserDTO.getPassword();
  }

  public UserPrincipal(SysUserDTO sysUserDTO, Map<String, Object> attributes) {
      this.id = sysUserDTO.getId();
      this.email = sysUserDTO.getEmail();
      this.name = sysUserDTO.getName();
      this.login = sysUserDTO.getLogin();
      this.password = sysUserDTO.getPassword();
      
      //Buscar banco authorities
      Collection<? extends GrantedAuthority> authorities = Collections.singletonList(new SimpleGrantedAuthority("ROLE_USER"));
      this.setAuthorities(authorities);
      this.setAttributes(attributes);
  }

  @Override
  public Map<String, Object> getAttributes() {
    return attributes;
  }

  public void setAttributes(Map<String, Object> attributes) {
    this.attributes = attributes;
  }

  public void setAuthorities(Collection<? extends GrantedAuthority> authorities) {
    this.authorities = authorities;
  }

  @Override
  public Collection<? extends GrantedAuthority> getAuthorities() {
    return authorities;
  }

  @Override
  public String getName() {
    return this.name;
  }

  public String getId() {
    return this.id;
  }

  public String getLogin() {
    return this.login;
  }

  @Override
  public String getPassword() {
    return this.password;
  }

  @Override
  public String getUsername() {
    return this.login;
  }

  @Override
  public boolean isAccountNonExpired() {
    return true;
  }

  @Override
  public boolean isAccountNonLocked() {
    return true;
  }

  @Override
  public boolean isCredentialsNonExpired() {
    return true;
  }

  @Override
  public boolean isEnabled() {
    return true;
  }
}