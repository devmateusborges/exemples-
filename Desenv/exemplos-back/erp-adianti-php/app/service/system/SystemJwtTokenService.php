<?php
use \Firebase\JWT\JWT;

class SystemJwtTokenService
{

    public static function TokenGeneration($login,$hours,$method)
    {
        $ini = AdiantiApplicationConfig::get();

        if ($ini['permission']['reset_password'] !== '1') {
            throw new Exception(_t('The password reset is disabled'));
        }

        if (empty($ini['general']['seed']) or $ini['general']['seed'] == 's8dkld83kf73kf094') {
            throw new Exception(_t('A new seed is required in the application.ini for security reasons'));
        }

        $key = APPLICATION_NAME . $ini['general']['seed'];
                    
        $token = array(
            "user" => $login,
            "method" => $method,
            "expires" => strtotime("+ ".$hours." hours")
        );
        
        return JWT::encode($token, $key);

    }


    public static function TokenDecode($token)
    {
        $ini = AdiantiApplicationConfig::get();

        if (empty($ini['general']['seed']) OR $ini['general']['seed'] == 's8dkld83kf73kf094')
        {
            throw new Exception(_t('A new seed is required in the application.ini for security reasons'));
        }
        
        $key = APPLICATION_NAME . $ini['general']['seed'];
        
        return (array) JWT::decode($token, $key, array('HS256'));

    }    
}
