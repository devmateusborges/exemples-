<?php

class FisIbpt extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;

    const TABLENAME = 'fis_ibpt';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('data_validade_ini');
        parent::addAttribute('data_validade_fin');
        parent::addAttribute('fis_nbs_id');
        parent::addAttribute('fis_ncm_id');
        parent::addAttribute('ger_uf_id');
        parent::addAttribute('perc_nacional');
        parent::addAttribute('perc_importado');
        parent::addAttribute('perc_municipal');
    }

}

?>