<?php

class BorDispositivo extends TRecord
{
    const TABLENAME  = 'bor_dispositivo';
    const PRIMARYKEY = 'id';
    const IDPOLICY   =  'serial'; // {max, serial}
    
    
    
    /**
     * Constructor method
     */
    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('nome');
        parent::addAttribute('numero_serie');
        parent::addAttribute('ativo');
        parent::addAttribute('unit_id');
    }
}

