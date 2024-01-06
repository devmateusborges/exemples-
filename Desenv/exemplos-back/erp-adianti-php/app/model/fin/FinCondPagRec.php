<?php

class FinCondPagRec extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'fin_cond_pagrec';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max';

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('id');
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('sigla_cond_pagamento');
        parent::addAttribute('considera_feriado');
        parent::addAttribute('considera_final_sem');
        parent::addAttribute('qnt_dia_ini');
        parent::addAttribute('observacao');
        parent::addAttribute('tipo_prazo');
    }

}

?>