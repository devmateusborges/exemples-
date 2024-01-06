<?php

class OpeCentro2Equip extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'ope_centro2_equip';
    const PRIMARYKEY = 'ope_centro2_id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_cidade;
    private $ope_centro2;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('ope_centro2_id');
        parent::addAttribute('tipo_rodado');
        parent::addAttribute('tipo_carroceria');
        parent::addAttribute('ger_cidade_id');
        parent::addAttribute('placa');
        parent::addAttribute('renavam');
        parent::addAttribute('tara');
        parent::addAttribute('capacidade_kg');
        parent::addAttribute('capacidade_m3');
        parent::addAttribute('potencia');
        parent::addAttribute('nr_chassi');
        parent::addAttribute('nr_serie');
        parent::addAttribute('liberado_abastec');
        parent::addAttribute('largura');
        parent::addAttribute('altura');
        parent::addAttribute('nr_registro_estadual');
        parent::addAttribute('tipo_tracao');
        parent::addAttribute('tipo_transp_auto_carga');
    }

    public function get_ger_cidade()
    {
        if (empty($this->ger_cidade)) {
            $this->ger_cidade = new GerCidade($this->ger_cidade_id);
        }
        return $this->ger_cidade;
    }

    public function get_ope_centro2()
    {
        if (empty($this->ope_centro2)) {
            $this->ope_centro2 = new OpeCentro2($this->ope_centro2_id);
        }
        return $this->ope_centro2;
    }

}

?>