<?php

class MovReboque extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'mov_reboque';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ope_centro2_equip;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('id');
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('ope_centro2_id_equip');
    }

    public function get_ope_centro2_equip()
    {
        if (empty($this->ope_centro2_equip)) {
            $this->ope_centro2_equip = new OpeCentro2Equip($this->ope_centro2_id_equip);
        }
        return $this->ope_centro2_equip;
    }

}

?>