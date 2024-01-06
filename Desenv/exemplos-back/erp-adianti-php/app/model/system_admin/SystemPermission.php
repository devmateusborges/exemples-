<?php

class SystemPermission
{
    public static function checkPermission($action)
    {
        $ini    = AdiantiApplicationConfig::get();
        
        $programs = TSession::getValue('programs');
        $public = $ini['permission']['public_classes'];
        
        return ( (isset($programs[$action]) AND $programs[$action]) OR
                 in_array($action, $public) );
    } 
}
