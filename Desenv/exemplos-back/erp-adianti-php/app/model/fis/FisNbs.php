<?php

class FisNbs extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    
    const TABLENAME = 'fis_nbs';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('nr_nbs');
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('data_validade');
    }

}

?>