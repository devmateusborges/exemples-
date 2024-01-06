<?php

class MovStatus extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
 
    const TABLENAME = 'mov_status';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('sigla_mov_status');
        parent::addAttribute('tipo_status');
    }

}

?>