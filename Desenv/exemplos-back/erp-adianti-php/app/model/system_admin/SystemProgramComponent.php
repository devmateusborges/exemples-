<?php

class SystemProgramComponent extends TRecord
{
    const TABLENAME  = 'system_program_component';
    const PRIMARYKEY = 'id';
    const IDPOLICY   = 'max'; // {max, serial}
    
    public function __construct($id = NULL)
    {
        parent::__construct($id);
        parent::addAttribute('system_program_id');
        parent::addAttribute('component_element');
        parent::addAttribute('title');
        parent::addAttribute('content');
        parent::addAttribute('order_view');
        parent::addAttribute('tab_name');
        parent::addAttribute('col_name');
        parent::addAttribute('link_video');
        parent::addAttribute('link_manual');
    }
    
    
}
