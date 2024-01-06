<?php

class MovPercurso extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
 
    const TABLENAME = 'mov_percurso';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_cidade;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('ger_cidade_id');
    }

    public function get_ger_cidade()
    {
        if (empty($this->ger_cidade)) {
            $this->ger_cidade = new GerCidade($this->ger_cidade_id);
        }
        return $this->ger_cidade;
    }

}

?>