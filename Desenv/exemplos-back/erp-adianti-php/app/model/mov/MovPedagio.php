<?php

class MovPedagio extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
 
    const TABLENAME = 'mov_pedagio';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_pessoa_pedagio;
    private $ger_pessoa_responsavel;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('ger_pessoa_id_emp_pedagio');
        parent::addAttribute('ger_pessoa_id_responsavel');
        parent::addAttribute('valor_pedagio');
        parent::addAttribute('nr_comprovante');
    }

    public function get_ger_pessoa_pedagio()
    {
        if (empty($this->ger_pessoa_pedagio)) {
            $this->ger_pessoa_pedagio = new GerPessoa($this->ger_pessoa_id_emp_pedagio);
        }
        return $this->ger_pessoa_pedagio;
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