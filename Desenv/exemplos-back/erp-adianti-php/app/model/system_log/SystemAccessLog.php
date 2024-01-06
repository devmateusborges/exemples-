<?php
use Adianti\Registry\TSession;

//TODO CORE
class SystemAccessLog extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
    
    const TABLENAME = 'system_access_log';
    const PRIMARYKEY= 'id';
    const IDPOLICY =  'max'; // {max, serial}
    
    
    /**
     * Constructor method
     */
    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('sessionid');
        parent::addAttribute('login');
        parent::addAttribute('login_time');
        parent::addAttribute('logout_time');
        parent::addAttribute('unit_id');
    }

    /**
     * Register login
     */
    public static function registerLogin()
    {
        TTransaction::open(TSession::getValue('pConn'));        
        $object = new self;
        $object->login = TSession::getValue('login');
        if (empty(session_id()))
        {
            $object->sessionid = json_encode($_REQUEST);
        }
        else{
            $object->sessionid = session_id();
        }
        $object->login_time = date("Y-m-d H:i:s");
        $object->unit_id = TSession::getValue('userunitid');
        $object->store();
        TTransaction::close();
    }
    
    /**
     * Register logout
     */
    public static function registerLogout()
    {
        TTransaction::open(TSession::getValue('pConn'));
        // get logs by session id
        $logs = self::where('unit_id', '=',TSession::getValue('userunitid') )->where('sessionid', '=', session_id())->load();
        if (count($logs)>0)
        {
            $log = $logs[0];
            if ($log instanceof SystemAccessLog);
            {
                $log->logout_time = date("Y-m-d H:i:s");
            }
            $log->store();
        }
        TTransaction::close();
    }
    
    /**
     *
     */
    public static function getStatsByDay()
    {
        TTransaction::open(TSession::getValue('pConn'));
        // get logs by session id
        $logs = self::where('login_time', '>=', date('Y-m-01'))
                    ->where('login_time', '<=', date('Y-m-t'))
                    ->where('unit_id', '=', TSession::getValue('userunitid'))
                    ->load();
        $accesses = array();
        
        if (count($logs)>0)
        {
            $accesses = array();
            foreach ($logs as $log)
            {
                $day = substr($log->login_time,8,2);
                if (isset($accesses[$day]))
                {
                    $accesses[$day] ++;
                }
                else
                {
                    $accesses[$day] = 1;
                }
            }
        }
        
        TTransaction::close();
        return $accesses;
    }
}
