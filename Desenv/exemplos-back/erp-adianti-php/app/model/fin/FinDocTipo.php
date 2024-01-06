<?php

class FinDocTipo extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'fin_pagrec_tipo';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max';

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('id');
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('aceita_entrada');
        parent::addAttribute('aceita_saida');
    }

}

?>