<?php

class MovCondutor extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
 
    const TABLENAME = 'mov_condutor';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_pessoa_condutor;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('ger_pessoa_id_condutor');
    }

    public function get_ger_pessoa_condutor()
    {
        if (empty($this->ger_pessoa_condutor)) {
            $this->ger_pessoa_condutor = new GerPessoa($this->ger_pessoa_id_condutor);
        }
        return $this->ger_pessoa_condutor;
    }

}

?>