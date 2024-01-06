<?php

class FinPagRec extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'fin_pagrec';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max';

    private $fin_pagrec_parc;
    private $fin_doc_tipo;
    private $fin_cond_pagrec;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('id');
        parent::addAttribute('fin_cond_pagrec_id');
        parent::addAttribute('numero_parc_total');
        parent::addAttribute('tipo_es');
        parent::addAttribute('fin_pagrec_tipo_id');
        parent::addAttribute('numero_doc_pagrec');
        parent::addAttribute('ger_pessoa_id');
        parent::addAttribute('ger_pessoa_id_pagrec');
        parent::addAttribute('observacao');
        parent::addAttribute('data_mov');
        parent::addAttribute('valor_pagrec');
        parent::addAttribute('ope_centro_rat_tipo_id');
        parent::addAttribute('ger_empresa_id');
        parent::addAttribute('fin_doc_tipo_id');
    }

    public function get_fin_pagrec_parc()
    {
        if (empty($this->fin_pagrec_parc)) {
            $this->fin_pagrec_parc = FinPagRec::find($this->id)->hasMany('FinPagRecOrigem');
        }
        return $this->fin_pagrec_parc;
    }

    public function get_fin_doc_tipo()
    {
        if (empty($this->fin_doc_tipo)) {
            $this->fin_doc_tipo = new FinDocTipo($this->fin_doc_tipo_id);
        }
        return $this->fin_doc_tipo;
    }

    public function get_fin_cond_pagrec()
    {
        if (empty($this->fin_cond_pagrec)) {
            $this->fin_cond_pagrec = new FinCondPagRec($this->fin_cond_pagrec_id);
        }
        return $this->fin_cond_pagrec;
    }

}

?>