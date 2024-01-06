<?php

class SystemUserProgram extends TRecord
{
    const TABLENAME = 'system_user_program';
    const PRIMARYKEY= 'id';
    const IDPOLICY =  'max'; // {max, serial}
    
    public function __construct($id = NULL)
    {
        parent::__construct($id);
        parent::addAttribute('system_user_id');
        parent::addAttribute('system_program_id');
    }
}
