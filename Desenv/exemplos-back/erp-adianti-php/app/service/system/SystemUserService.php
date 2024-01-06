<?php

class SystemUserService
{

    public function Registration($param)
    {
        try {
            $ini = AdiantiApplicationConfig::get();
            if ($ini['permission']['user_register'] !== '1') {
                throw new Exception(_t('The user registration is disabled'));
            }

            TTransaction::open(TSession::getValue('pConn'));

            if (empty($param['login'])) {
                throw new Exception(TAdiantiCoreTranslator::translate('The field ^1 is required', _t('Login')));
            }

            if (empty($param['name'])) {
                throw new Exception(TAdiantiCoreTranslator::translate('The field ^1 is required', _t('Name')));
            }

            if (empty($param['email'])) {
                throw new Exception(TAdiantiCoreTranslator::translate('The field ^1 is required', _t('Email')));
            }

            if (empty($param['password'])) {
                throw new Exception(TAdiantiCoreTranslator::translate('The field ^1 is required', _t('Password')));
            }

            if (empty($param['repassword'])) {
                throw new Exception(TAdiantiCoreTranslator::translate('The field ^1 is required', _t('Password confirmation')));
            }

            if (SystemUser::newFromLogin($param['login']) instanceof SystemUser) {
                throw new Exception(_t('An user with this login is already registered'));
            }

            if (SystemUser::newFromEmail($param['email']) instanceof SystemUser) {
                throw new Exception(_t('An user with this e-mail is already registered'));
            }

            if ($param['password'] !== $param['repassword']) {
                throw new Exception(_t('The passwords do not match'));
            }

            $object = new SystemUser;
            $object->active = 'N';
            $object->active_message = 'Ativação enviada para seu email, verifique sua caixa de email';
            $object->system = 'N';
            $object->fromArray($param);
            $object->login = strtolower($object->login);
            $object->password = md5($object->password);
            $object->frontpage_id = $ini['permission']['default_screen'];
            $object->clearParts();
            $object->store();

            //Adiciona Grupos para novos clientes cadastrados
            $default_groups = explode(',', $ini['permission']['default_groups']);

            if (count($default_groups) > 0) {
                foreach ($default_groups as $group_id) {
                    $object->addSystemUserGroup(new SystemGroup($group_id));
                }
            }

            //Adiciona Units MODELO para novos clientes cadastrados
            $default_units = explode(',', $ini['permission']['default_units']);

            if (count($default_units) > 0) {
                foreach ($default_units as $unit_id) {
                    $object->addSystemUserUnit(new SystemUnit($unit_id));
                }
            }

            //Adiciona Programa Boas Vindas para novos clientes cadastrados
            $default_programs = explode(',', $ini['permission']['default_screen']);

            if (count($default_programs) > 0) {
                foreach ($default_programs as $program_id) {
                    $object->addSystemUserProgram(new SystemProgram($program_id));
                }
            }

            TTransaction::close(); // close the transaction

            $vEmailWelcome = self::EmailWelcome($param);
            if ($vEmailWelcome !== 'OK') {
                throw new Exception($vEmailWelcome);
            } else {
                return 'OK';
            }
        } catch (Exception $e) {
            return $e->getMessage();
            TTransaction::rollback();
        }
    }


    public function RequestNewPassword($param)
    {

        try {

            TTransaction::open(TSession::getValue('pConn'));

            $login = $param['login'];
            $user  = SystemUser::newFromLogin($login);

            //Gera JwtToken 
            $jwt  = SystemJwtTokenService::TokenGeneration($login, 24);

            if ($user instanceof SystemUser) {
                if ($user->active == 'N') {
                    throw new Exception(_t('Inactive user'));
                } else {

                    $referer = $_SERVER['HTTP_REFERER'];
                    $url = substr($referer, 0, strpos($referer, 'index.php'));
                    $url .= 'index.php?class=SystemPasswordResetForm&method=onLoad&jwt=' . $jwt;

                    $replaces = [];
                    $replaces['name'] = $user->name;
                    $replaces['link'] = $url;
                    $replaces['application_name'] = APPLICATION_NAME;
                    $replaces['application_version'] = APPLICATION_VERSION;
                    $replaces['title'] = 'AGROBOT - Comunicado';
                    $replaces['direitos_reservados'] = 'AGROBOT ' . date('Y') . ' - Direitos Reservados';
                    $html = new THtmlRenderer('app/resources/system_reset_password.html');
                    $html->enableSection('main', $replaces);

                    $vMailLogId = MailService::StoreEmail($login, TSession::getValue('userunitid'), 'OU', $user->email, _t('Password reset'), $html->getContents(), 'html');
                    $vMailServiceSend = MailService::SendStoreEmail($vMailLogId);
                    if ($vMailServiceSend !== 'OK') {
                        throw new Exception($vMailServiceSend);
                    } else {
                        return 'OK';
                    }
                }
            } else {
                throw new Exception(_t('User not found'));
            }
        } catch (Exception $e) {
            return $e->getMessage();
            TTransaction::rollback();
        }
    }

    public function ResetPassword($param)
    {

        try {
            if (empty($param['password1'])) {
                throw new Exception('Senha vazia');
            }

            if ($param['password1'] !== $param['password2']) {
                throw new Exception(_t('The passwords do not match'));
            }

            //Decode Token
            $token = SystemJwtTokenService::TokenDecode($param['jwt']);

            $login = $token['user'];
            $expires = $token['expires'];

            if ($expires < strtotime('now')) {
                throw new Exception('Token expired. This operation is not allowed');
            }

            TTransaction::open(TSession::getValue('pConn'));
            $user  = SystemUser::newFromLogin($login);

            if ($user instanceof SystemUser) {
                if ($user->active == 'N') {
                    throw new Exception(_t('Inactive user'));
                } else {
                    $user->password = md5($param['password1']);
                    $user->store();
                    TTransaction::close();
                    return 'OK';
                }
            }
            TTransaction::close();
        } catch (Exception $e) {
            return $e->getMessage();
            TTransaction::rollback();
        }
    }


    public function EmailWelcome($param)
    {

        try {

            TTransaction::open(TSession::getValue('pConn'));

            $login = $param['login'];
            $user  = SystemUser::newFromLogin($login);

            //Gera JwtToken 
            $jwt  = SystemJwtTokenService::TokenGeneration($login, 24);

            if ($user instanceof SystemUser) {
                //Email de welcome desativado
                if ($user->active == 'N') {
                    $referer = $_SERVER['HTTP_REFERER'];
                    $url = substr($referer, 0, strpos($referer, 'index.php'));
                    $url .= 'index.php?class=LoginForm&method=onActiveUserWelcome&jwt=' . $jwt;

                    $replaces = [];
                    $replaces['name'] = $user->name;
                    $replaces['link'] = $url;
                    $replaces['application_name'] = APPLICATION_NAME;
                    $replaces['application_version'] = APPLICATION_VERSION;
                    $replaces['title'] = 'AGROBOT - Seja Bem Vindo';
                    $replaces['direitos_reservados'] = 'AGROBOT ' . date('Y') . ' - Direitos Reservados';
                    $html = new THtmlRenderer('app/resources/system_user_welcome.html');
                    $html->enableSection('main', $replaces);

                    $vMailLogId = MailService::StoreEmail($login, TSession::getValue('userunitid'), 'OU', $user->email, _t('Welcome to our Platform'),          $html->getContents(), 'html');
                    $vMailServiceSend = MailService::SendStoreEmail($vMailLogId);

                    if ($vMailServiceSend !== 'OK') {
                        TTransaction::close();
                        throw new Exception($vMailServiceSend);
                    } else {
                        TTransaction::close();
                        return 'OK';
                    }
                }
            } else {
                throw new Exception(_t('User not found'));
            }
        } catch (Exception $e) {
            TTransaction::close();
            return $e->getMessage();
        }
    }

    public function ActiveUserWelcome($param)
    {
        try {
            //Decode Token
            $token = SystemJwtTokenService::TokenDecode($param['jwt']);

            $login = $token['user'];
            $expires = $token['expires'];

            if ($expires < strtotime('now')) {
                throw new Exception('Token expired. This operation is not allowed');
            }

            TTransaction::open(TSession::getValue('pConn'));
            $user  = SystemUser::newFromLogin($login);

            if ($user instanceof SystemUser) {
                if ($user->active == 'N') {
                    $user->active = 'Y';
                    $user->active_message = '';
                    $user->store();
                    TTransaction::close();
                    return 'OK';
                } else {
                    throw new Exception(_t('User is already active'));
                }
            }
            TTransaction::close();
        } catch (Exception $e) {
            return $e->getMessage();
            TTransaction::rollback();
        }
    }
}
