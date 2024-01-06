<?php

class MovTomador extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'mov_tomador';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_pessoa_responsavel;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('ger_pessoa_id_responsavel');
    }

    public function get_ger_pessoa_responsavel()
    {
        if (empty($this->ger_pessoa_responsavel)) {
            $this->ger_pessoa_responsavel = new GerPessoa($this->ger_pessoa_id_responsavel);
        }
        return $this->ger_pessoa_responsavel;
    }

}

?>