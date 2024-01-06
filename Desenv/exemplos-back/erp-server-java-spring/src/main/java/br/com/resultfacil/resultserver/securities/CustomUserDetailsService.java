package  br.com.resultfacil.resultserver.securities;

import br.com.resultfacil.resultserver.exceptions.EntityNotFoundException;
import br.com.resultfacil.resultserver.models.SysUser;
import br.com.resultfacil.resultserver.models.SysUserDTO;
import br.com.resultfacil.resultserver.services.SysUserService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

import org.springframework.transaction.annotation.Transactional;


@Service
public class CustomUserDetailsService implements UserDetailsService {
  
  @Autowired
  SysUserService sysUserService;

  @Override
  @Transactional
  public UserDetails loadUserByUsername(String login) throws UsernameNotFoundException{
    
    SysUserDTO user = sysUserService.getByLogin(login);
    
    Optional<SysUserDTO> userAux = Optional.ofNullable(user);
    
    return userAux.map(UserPrincipal::new).orElse(null);

  }

  @Transactional
  public UserDetails loadUserById(String id) {

    SysUserDTO userDTO = sysUserService.findById(id);

    UserPrincipal userPrincipal = new UserPrincipal(userDTO);
    
    return (UserDetails) userPrincipal;

  }
  
}