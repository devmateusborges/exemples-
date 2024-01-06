<?php

class GerItemServ extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'ger_itemserv';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $fis_ncm;
    private $fis_nbs;
    private $ger_umedida;
    private $fis_cest;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('referencia1');
        parent::addAttribute('referencia2');
        parent::addAttribute('referencia3');
        parent::addAttribute('ger_itemserv_subgrupo_id');
        parent::addAttribute('fis_ncm_id');
        parent::addAttribute('fis_nbs_id');
        parent::addAttribute('ger_umedida_id');
        parent::addAttribute('tipo');
        parent::addAttribute('tipo_comp');
        parent::addAttribute('origem_fiscal');
        parent::addAttribute('fis_cest_id');
    }

    public function get_fis_ncm()
    {
        if (empty($this->fis_ncm)) {
            $this->fis_ncm = new FisNcm($this->fis_ncm_id);
        }
        return $this->fis_ncm;
    }

    public function get_fis_nbs()
    {
        if (empty($this->fis_nbs)) {
            $this->fis_nbs = new FisNbs($this->fis_nbs_id);
        }
        return $this->fis_nbs;
    }

    public function get_ger_umedida()
    {
        if (empty($this->ger_umedida)) {
            $this->ger_umedida = new GerUmedida($this->ger_umedida_id);
        }
        return $this->ger_umedida;
    }

    public function get_fis_cest()
    {
        if (empty($this->fis_cest)) {
            $this->fis_cest = new FisCest($this->fis_cest_id);
        }
        return $this->fis_cest;
    }

}

?>