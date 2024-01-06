<?php

class FinPagRecOrigem extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
    
    const TABLENAME = 'fin_pagrec_origem';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max';

    private $fin_pagrec;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('id');
        parent::addAttribute('fin_pagrec_id');
        parent::addAttribute('fin_pagrec_id_origem');
        parent::addAttribute('fin_pagrec_parc_id');
        parent::addAttribute('fin_pagrec_parc_id_origem');
        parent::addAttribute('tipo');
        parent::addAttribute('mov_id');
    }

    public function get_fin_pagrec()
    {
        if (empty($this->fin_pagrec)) {
            $this->fin_pagrec = FinPagRecOrigem::find($this->fin_pagrec_id)->hasMany('FinPagRec');
        }
        return $this->fin_pagrec;
    }

}

?>