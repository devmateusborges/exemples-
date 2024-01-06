<?php

class MovEntrega extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
  
    const TABLENAME = 'mov_entrega';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_cidade;
    private $mov_entregas_doc;

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

    public function get_mov_entregas_doc()
    {
        if (empty($this->mov_entregas_doc)) {
            $this->mov_entregas_doc = MovEntregaDoc::find($this->id)->hasMany('MovEntregaDoc');
        }
        return $this->mov_entregas_doc;
    }

}

?>