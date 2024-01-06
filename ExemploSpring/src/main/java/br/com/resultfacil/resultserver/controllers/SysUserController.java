package br.com.resultfacil.resultserver.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.resultfacil.resultserver.services.SysUserService;
import br.com.resultfacil.resultserver.services.base.BaseService;
import br.com.resultfacil.resultserver.controllers.base.BaseController;
import br.com.resultfacil.resultserver.exceptions.OAuth2AuthenticationProcessingException;
import br.com.resultfacil.resultserver.models.SysUser;
import br.com.resultfacil.resultserver.models.SysUserDTO;
import br.com.resultfacil.resultserver.securities.CurrentUser;
import br.com.resultfacil.resultserver.securities.UserPrincipal;

@RestController
@RequestMapping(path = "/sys/sysuser", produces = MediaType.APPLICATION_JSON_VALUE)
public class SysUserController implements BaseController<SysUser, SysUserDTO, String> {

    @Autowired
    private SysUserService service;

    @Override
    public BaseService<SysUser, SysUserDTO, String> getService() {
        return service;
    }

    @GetMapping("/me")
    //@PreAuthorize("hasRole('USER')")
    public SysUserDTO getCurrentUser(@CurrentUser UserPrincipal userPrincipal)  {
        SysUserDTO sysUserDTO = service.findById(userPrincipal.getId());
        return sysUserDTO;
        
    }

}