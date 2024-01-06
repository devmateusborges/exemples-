<?php

class MovFrete extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    const UNITFIELD = 'unit_id';


    const TABLENAME = 'mov_frete';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ope_centro2_equip;
    private $ger_pessoa_endereco_condutor;
    private $ger_pessoa_endereco_transp;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('id');
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('ope_centro2_id_equip');
        parent::addAttribute('ger_pessoa_endereco_id_condutor');
        parent::addAttribute('ger_pessoa_endereco_id_transp');
        parent::addAttribute('valor_frete');
        parent::addAttribute('adic_frete_vase_cal_icms');
        parent::addAttribute('valor_base_calc');
        parent::addAttribute('perc_aliquota');
        parent::addAttribute('valor_imposto');
        parent::addAttribute('valor_pis');
        parent::addAttribute('valor_confis');
    }

    public function get_ope_centro2_equip()
    {
        if (empty($this->ope_centro2_equip)) {
            $this->ope_centro2_equip = new OpeCentro2Equip($this->ope_centro2_id_equip);
        }
        return $this->ope_centro2_equip;
    }

    public function get_ger_pessoa_endereco_condutor()
    {
        if (empty($this->ger_pessoa_endereco_condutor)) {
            $this->ger_pessoa_endereco_condutor = new GerPessoaEndereco($this->ger_pessoa_endereco_id_condutor);
        }
        return $this->ger_pessoa_endereco_condutor;
    }

    public function get_ger_pessoa_endereco_transp()
    {
        if (empty($this->ger_pessoa_endereco_transp)) {
            $this->ger_pessoa_endereco_transp = new GerPessoaEndereco($this->ger_pessoa_endereco_id_transp);
        }
        return $this->ger_pessoa_endereco_transp;
    }

}

?>