<?php

class MovSeguradora extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
 
    const TABLENAME = 'mov_seguradora';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_pessoa_responsavel;
    private $ger_pessoa_seguradora;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('ger_pessoa_id_responsavel');
        parent::addAttribute('ger_pessoa_id_seguradora');
        parent::addAttribute('nr_apolice');
        parent::addAttribute('nr_averbacao');
        parent::addAttribute('tipo_responsavel');
    }

    public function get_ger_pessoa_responsavel()
    {
        if (empty($this->ger_pessoa_responsavel)) {
            $this->ger_pessoa_responsavel = new GerPessoa($this->ger_pessoa_id_responsavel);
        }
        return $this->ger_pessoa_responsavel;
    }

    public function get_ger_pessoa_seguradora()
    {
        if (empty($this->ger_pessoa_seguradora)) {
            $this->ger_pessoa_seguradora = new GerPessoa($this->ger_pessoa_id_seguradora);
        }
        return $this->ger_pessoa_seguradora;
    }

}

?>