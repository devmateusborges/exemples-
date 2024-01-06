<?php
use Adianti\Registry\TSession;

class SystemEmailLog extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'system_unit_id';
 
    const TABLENAME = 'system_email_log';
    const PRIMARYKEY= 'id';
    const IDPOLICY =  'max'; // {max, serial}
    
    
    /**
     * Constructor method
     */
    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);

        parent::addAttribute('system_unit_id');
        parent::addAttribute('type_in_out');
        parent::addAttribute('security_user');
        parent::addAttribute('security_pwd');
        parent::addAttribute('security_host');
        parent::addAttribute('security_port');
        parent::addAttribute('security_type');
        parent::addAttribute('date_log');
        parent::addAttribute('date_send');
        parent::addAttribute('email_from');
        parent::addAttribute('subject');
        parent::addAttribute('body');
        parent::addAttribute('error_message');
        parent::addAttribute('email_reply');
        parent::addAttribute('email_to');
        parent::addAttribute('login');
        parent::addAttribute('body_type');

    }

   
}
