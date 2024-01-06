<?php
require_once 'init.php';

class TApplication extends AdiantiCoreApplication
{
    public static function run($debug = FALSE)
    {
        new TSession;
        
        if ($_REQUEST)
        {
            $ini    = AdiantiApplicationConfig::get();
            $class  = isset($_REQUEST['class']) ? $_REQUEST['class'] : '';
            $public = in_array($class, $ini['permission']['public_classes']);
            
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

            //TODO: Colocar unit_token

            if (TSession::getValue('logged')) // logged
            {
                $programs = (array) TSession::getValue('programs'); // programs with permission
                $programs = array_merge($programs, self::getDefaultPermissions());
                
                if( isset($programs[$class]) OR $public )
                {
                    parent::run($debug);
                }
                else
                {
                    new TMessage('error', _t('Permission denied') );
                }
            }
            else if ($class == 'LoginForm' OR $public )
            {
                parent::run($debug);
            }
            else
            {
                new TMessage('error', _t('Permission denied'), new TAction(array('LoginForm','onLogout')) );
            }
        }
    }
    
    /**
     * Return default programs for logged users
     */
    public static function getDefaultPermissions()
    {
        return array('Adianti\Base\TStandardSeek' => TRUE,
                     'LoginForm' => TRUE,
                     'AdiantiMultiSearchService' => TRUE,
                     'AdiantiUploaderService' => TRUE,
                     'AdiantiAutocompleteService' => TRUE,
                     'EmptyPage' => TRUE,
                     'MessageList' => TRUE,
                     'SystemDocumentUploaderService' => TRUE,
                     'NotificationList' => TRUE,
                     'SearchBox' => TRUE,
                     'SearchInputBox' => TRUE,
                     'SystemPageService' => TRUE,
                     'SystemPageBatchUpdate' => TRUE,
                     'SystemPermissionUpdate' => TRUE,
                     'SystemMenuUpdate' => TRUE);
    } 
}

TApplication::run(TRUE);
