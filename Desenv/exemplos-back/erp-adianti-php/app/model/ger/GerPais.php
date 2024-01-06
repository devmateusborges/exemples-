<?php

class GerPais extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    
    const TABLENAME = 'ger_pais';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('id');
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('nr_pais');
    }

}

?>