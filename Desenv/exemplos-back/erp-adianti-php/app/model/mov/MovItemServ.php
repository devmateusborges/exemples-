<?php

class MovItemServ extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
 
    const TABLENAME = 'mov_itemserv';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_itemserv;
    private $fis_tributacao;
    private $fis_cfop;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('ger_itemserv_id');
        parent::addAttribute('fis_cfop_id');
        parent::addAttribute('qnt_orig');
        parent::addAttribute('valor_unit_orig');
        parent::addAttribute('ger_umedida_conv_id_conv');
        parent::addAttribute('qnt_conv');
        parent::addAttribute('valor_unit_conv');
        parent::addAttribute('valor_bruto');
        parent::addAttribute('valor_desconto');
        parent::addAttribute('valor_acrecimo');
        parent::addAttribute('valor_outros');
        parent::addAttribute('valor_liquido');
        parent::addAttribute('qnt_devolvida');
        parent::addAttribute('valor_frete');
        parent::addAttribute('valor_seguro');
        parent::addAttribute('observacao');
        parent::addAttribute('valor_tributo_retido');
    }

    public function get_ger_itemserv()
    {
        if (empty($this->ger_itemserv)) {
            $this->ger_itemserv = new GerItemServ($this->ger_itemserv_id);
        }
        return $this->ger_itemserv;
    }

    public function get_fis_tributacao()
    {
        if (empty($this->fis_tributacao)) {
            $this->fis_tributacao = MovItemServ::find($this->id)->hasMany('FisTributacao', 'mov_itemserv_id');
        }
        return $this->fis_tributacao;
    }

    public function get_fis_cfop()
    {
        if (empty($this->fis_cfop)) {
            $this->fis_cfop = new FisCfop($this->fis_cfop_id);
        }
        return $this->fis_cfop;
    }

}

?>