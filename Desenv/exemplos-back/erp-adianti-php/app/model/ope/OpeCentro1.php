<?php

class OpeCentro1 extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
    
    const TABLENAME = 'ope_centro1';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_pessoa;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('ativo');
        parent::addAttribute('sigla_centro1');
        parent::addAttribute('ger_pessoa_id');
        parent::addAttribute('ope_centro_subtipo_id');
        parent::addAttribute('observacao');
    }

    public function get_ger_pessoa()
    {
        if (empty($this->ger_pessoa)) {
            $this->ger_pessoa = new GerPessoa($this->ger_pessoa_id);
        }
        return $this->ger_pessoa;
    }

}

?>