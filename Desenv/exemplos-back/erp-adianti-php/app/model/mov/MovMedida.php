<?php

class MovMedida extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
 
    const TABLENAME = 'mov_medida';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_umedida;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('ger_umedida_id');
        parent::addAttribute('tipo_medida');
        parent::addAttribute('qnt_medida');
    }

    public function get_ger_umedida()
    {
        if (empty($this->ger_umedida)) {
            $this->ger_umedida = new GerUmedida($this->ger_umedida_id);
        }
        return $this->ger_umedida;
    }

}

?>