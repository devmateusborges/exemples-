<?php

class GerUf extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;

    const TABLENAME = 'ger_uf';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_pais;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('nr_uf');
        parent::addAttribute('ger_pais_id');
    }

    public function get_ger_pais()
    {
        if (empty($this->ger_pais)) {
            $this->ger_pais = new GerPais($this->ger_pais_id);
        }
        return $this->ger_pais;
    }

}

?>