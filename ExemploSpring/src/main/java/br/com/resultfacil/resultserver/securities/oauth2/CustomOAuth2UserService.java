package br.com.resultfacil.resultserver.securities.oauth2;

import br.com.resultfacil.resultserver.exceptions.OAuth2AuthenticationProcessingException;
import br.com.resultfacil.resultserver.models.SysUserDTO;
import br.com.resultfacil.resultserver.enums.AuthProviderEnum;
import br.com.resultfacil.resultserver.securities.UserPrincipal;
import br.com.resultfacil.resultserver.securities.oauth2.userinfo.OAuth2UserInfo;
import br.com.resultfacil.resultserver.securities.oauth2.userinfo.OAuth2UserInfoFactory;
import br.com.resultfacil.resultserver.services.SysUserService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.oauth2.client.userinfo.DefaultOAuth2UserService;
import org.springframework.security.oauth2.client.userinfo.OAuth2UserRequest;
import org.springframework.security.oauth2.core.OAuth2AuthenticationException;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Service;
import org.apache.commons.lang.*;


@Service
public class CustomOAuth2UserService extends DefaultOAuth2UserService {

    @Autowired
    private SysUserService sysUserService;

    @Override
    public OAuth2User loadUser(OAuth2UserRequest oAuth2UserRequest) throws OAuth2AuthenticationException {
        OAuth2User oAuth2User = super.loadUser(oAuth2UserRequest);

        try {
            return processOAuth2User(oAuth2UserRequest, oAuth2User);
        } catch (AuthenticationException ex) {
            throw ex;
        } catch (Exception ex) {

            throw ex;
        }
    }

    private OAuth2User processOAuth2User(OAuth2UserRequest oAuth2UserRequest, OAuth2User oAuth2User) {

        OAuth2UserInfo oAuth2UserInfo = OAuth2UserInfoFactory.getOAuth2UserInfo(
                oAuth2UserRequest.getClientRegistration().getRegistrationId(), oAuth2User.getAttributes());

        if (StringUtils.isEmpty(oAuth2UserInfo.getEmail())) {
            throw new OAuth2AuthenticationProcessingException("Email not found from OAuth2 provider");
        }

        SysUserDTO sysUserDTO = sysUserService.getByLogin(oAuth2UserInfo.getLogin());

        if (sysUserDTO != null) {
            if (!sysUserDTO.getProvider()
                    .equals(AuthProviderEnum.valueOf(oAuth2UserRequest.getClientRegistration().getRegistrationId()))) {
                throw new OAuth2AuthenticationProcessingException("Looks like you're signed up with " +
                        sysUserDTO.getProvider() + " account. Please use your " + sysUserDTO.getProvider() +
                        " account to login.");
            }
            sysUserDTO = loginUpdate(sysUserDTO, oAuth2UserInfo);
        } else {
            sysUserDTO = loginRegister(oAuth2UserRequest, oAuth2UserInfo);
        }

        UserPrincipal userPrincipal = new UserPrincipal(sysUserDTO, oAuth2User.getAttributes());

        return (OAuth2User) userPrincipal;
    }

    private SysUserDTO loginRegister(OAuth2UserRequest oAuth2UserRequest, OAuth2UserInfo oAuth2UserInfo) {
        try {

            SysUserDTO sysUserDTO = new SysUserDTO();

            sysUserDTO.setProvider(
                    AuthProviderEnum.valueOf(oAuth2UserRequest.getClientRegistration().getRegistrationId()));
            sysUserDTO.setProviderCode(oAuth2UserInfo.getId());
            sysUserDTO.setName(oAuth2UserInfo.getName());
            sysUserDTO.setEmail(oAuth2UserInfo.getEmail());
            sysUserDTO.setLogin(oAuth2UserInfo.getLogin());
            sysUserDTO.setImageUrl(oAuth2UserInfo.getImageUrl());

            return sysUserService.save(sysUserDTO);

        } catch (Exception ex) {

            throw ex;
        }
    }

    private SysUserDTO loginUpdate(SysUserDTO existingUser, OAuth2UserInfo oAuth2UserInfo) {
        try {
            existingUser.setName(oAuth2UserInfo.getName());
            existingUser.setEmail(oAuth2UserInfo.getEmail());
            existingUser.setImageUrl(oAuth2UserInfo.getImageUrl());
            return sysUserService.save(existingUser);
        } catch (Exception ex) {

            throw ex;
        }
    }

}