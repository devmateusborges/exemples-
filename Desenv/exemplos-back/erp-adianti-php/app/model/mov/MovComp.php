<?php

class MovComp extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
 
    const TABLENAME = 'mov_comp';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('nome_comp');
        parent::addAttribute('qnt_comp');
    }

}

?>