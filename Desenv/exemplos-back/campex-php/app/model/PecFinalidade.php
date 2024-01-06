<?php

class PecFinalidade extends TRecord
{
    const TABLENAME  = 'pec_finalidade';
    const PRIMARYKEY = 'id';
    const IDPOLICY   =  'uuid'; // {max, serial}

    private $system_unit;

    

    /**
     * Constructor method
     */
    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('system_unit_id');
        parent::addAttribute('codigo');
        parent::addAttribute('descricao');
            
    }

    /**
     * Method set_system_unit
     * Sample of usage: $var->system_unit = $object;
     * @param $object Instance of SystemUnit
     */
    public function set_system_unit(SystemUnit $object)
    {
        $this->system_unit = $object;
        $this->system_unit_id = $object->id;
    }

    /**
     * Method get_system_unit
     * Sample of usage: $var->system_unit->attribute;
     * @returns SystemUnit instance
     */
    public function get_system_unit()
    {
    
        // loads the associated object
        if (empty($this->system_unit))
            $this->system_unit = new SystemUnit($this->system_unit_id);
    
        // returns the associated object
        return $this->system_unit;
    }

    /**
     * Method getPecLotes
     */
    public function getPecLotes()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('pec_finalidade_id', '=', $this->id));
        return PecLote::getObjects( $criteria );
    }

    public function set_pec_lote_system_unit_to_string($pec_lote_system_unit_to_string)
    {
        if(is_array($pec_lote_system_unit_to_string))
        {
            $values = SystemUnit::where('id', 'in', $pec_lote_system_unit_to_string)->getIndexedArray('name', 'name');
            $this->pec_lote_system_unit_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_lote_system_unit_to_string = $pec_lote_system_unit_to_string;
        }

        $this->vdata['pec_lote_system_unit_to_string'] = $this->pec_lote_system_unit_to_string;
    }

    public function get_pec_lote_system_unit_to_string()
    {
        if(!empty($this->pec_lote_system_unit_to_string))
        {
            return $this->pec_lote_system_unit_to_string;
        }
    
        $values = PecLote::where('pec_finalidade_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
        return implode(', ', $values);
    }

    public function set_pec_lote_pec_finalidade_to_string($pec_lote_pec_finalidade_to_string)
    {
        if(is_array($pec_lote_pec_finalidade_to_string))
        {
            $values = PecFinalidade::where('id', 'in', $pec_lote_pec_finalidade_to_string)->getIndexedArray('descricao', 'descricao');
            $this->pec_lote_pec_finalidade_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_lote_pec_finalidade_to_string = $pec_lote_pec_finalidade_to_string;
        }

        $this->vdata['pec_lote_pec_finalidade_to_string'] = $this->pec_lote_pec_finalidade_to_string;
    }

    public function get_pec_lote_pec_finalidade_to_string()
    {
        if(!empty($this->pec_lote_pec_finalidade_to_string))
        {
            return $this->pec_lote_pec_finalidade_to_string;
        }
    
        $values = PecLote::where('pec_finalidade_id', '=', $this->id)->getIndexedArray('pec_finalidade_id','{pec_finalidade->descricao}');
        return implode(', ', $values);
    }

    
}

