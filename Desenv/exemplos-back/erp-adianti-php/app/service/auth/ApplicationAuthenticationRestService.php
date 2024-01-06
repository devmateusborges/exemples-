<?php
use \Firebase\JWT\JWT;

class ApplicationAuthenticationRestService
{
    public static function getToken($param)
    {
      
        
        $pConn  = isset($_REQUEST['pConn']) ? $_REQUEST['pConn'] : '';
        if(empty($pConn))
        {
          $pConn = TSession::getValue('pConn');
          if(empty($pConn))
          {
             die('<h1>'.'Conexão ['.$pConn.'] inválida'.'</h1>');
          }
          
        }
        else
        {
          TSession::setValue('pConn',$pConn);
        }
     

        $pUnitId  = isset($_REQUEST['pUnitId']) ? $_REQUEST['pUnitId'] : '';
        if(empty($pUnitId))
        {
          $pUnitId = TSession::getValue('pUnitId');
          if(empty($pUnitId))
          {
             die('<h1>'.'Unidade ['.$pUnitId.'] inválida'.'</h1>');
          }
        }
        else
        {
            TTransaction::open($pConn);
            $unitObj = new SystemUnit($pUnitId);
            TTransaction::close();
            if (isset( $unitObj)) {
              TSession::setValue('pUnitId',$pUnitId);
            }
        }        
        
      
     
        $user = ApplicationAuthenticationService::authenticate($param['login'], $param['password']);
      
        $ini = AdiantiApplicationConfig::get();
        $key = APPLICATION_NAME . $ini['general']['seed'];
        
        if (empty($ini['general']['seed']))
        {
            throw new Exception('Application seed not defined');
        }
       
        $token = array(
            "user" => $param['login'],
            "userid" => $user->id,
            "username" => $user->name,
            "usermail" => $user->email,
            "expires" => strtotime("+ 3 hours"),
            "unitid" => $pUnitId
        );
        
        return JWT::encode($token, $key);
    }
}
