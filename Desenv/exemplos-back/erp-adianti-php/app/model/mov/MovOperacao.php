<?php

class MovOperacao extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'mov_operacao';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_numeracao;
    private $mov_tipo;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('sigla_mov_operacao');
        parent::addAttribute('mov_tipo_id');
        parent::addAttribute('ger_numeracao_id');
        parent::addAttribute('finalidade_doc');
    }

    public function get_ger_numeracao()
    {
        if (empty($this->ger_numeracao)) {
            $this->ger_numeracao = new GerNumeracao($this->ger_numeracao_id);
        }
        return $this->ger_numeracao;
    }

    public function get_mov_tipo()
    {
        if (empty($this->mov_tipo)) {
            $this->mov_tipo = new MovTipo($this->mov_tipo_id);
        }
        return $this->mov_tipo;
    }

}

?>