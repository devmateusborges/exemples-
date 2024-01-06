<?php

class FisNcm extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;

    const TABLENAME = 'fis_ncm';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $fis_ibpt;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('nr_ncm');
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('data_validade');
    }

    public function get_fis_ibpt()
    {
        if (empty($this->fis_ibpt)) {
            $this->fis_ibpt = FisNcm::find($this->id)->filterMany('FisIbpt')->where('ger_uf_id', '=', '1')->load()[0];
        }
        return $this->fis_ibpt;
    }

}

?>