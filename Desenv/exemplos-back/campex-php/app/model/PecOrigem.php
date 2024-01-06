<?php

class PecOrigem extends TRecord
{
    const TABLENAME  = 'pec_origem';
    const PRIMARYKEY = 'id';
    const IDPOLICY   =  'uuid'; // {max, serial}

    private $system_unit;

    

    use SystemChangeLogTrait;
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
     * Method getPecAnimals
     */
    public function getPecAnimals()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('pec_origem_id', '=', $this->id));
        return PecAnimal::getObjects( $criteria );
    }

    public function set_pec_animal_system_unit_to_string($pec_animal_system_unit_to_string)
    {
        if(is_array($pec_animal_system_unit_to_string))
        {
            $values = SystemUnit::where('id', 'in', $pec_animal_system_unit_to_string)->getIndexedArray('name', 'name');
            $this->pec_animal_system_unit_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_animal_system_unit_to_string = $pec_animal_system_unit_to_string;
        }

        $this->vdata['pec_animal_system_unit_to_string'] = $this->pec_animal_system_unit_to_string;
    }

    public function get_pec_animal_system_unit_to_string()
    {
        if(!empty($this->pec_animal_system_unit_to_string))
        {
            return $this->pec_animal_system_unit_to_string;
        }
    
        $values = PecAnimal::where('pec_origem_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
        return implode(', ', $values);
    }

    public function set_pec_animal_pec_raca_to_string($pec_animal_pec_raca_to_string)
    {
        if(is_array($pec_animal_pec_raca_to_string))
        {
            $values = PecRaca::where('id', 'in', $pec_animal_pec_raca_to_string)->getIndexedArray('descricao', 'descricao');
            $this->pec_animal_pec_raca_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_animal_pec_raca_to_string = $pec_animal_pec_raca_to_string;
        }

        $this->vdata['pec_animal_pec_raca_to_string'] = $this->pec_animal_pec_raca_to_string;
    }

    public function get_pec_animal_pec_raca_to_string()
    {
        if(!empty($this->pec_animal_pec_raca_to_string))
        {
            return $this->pec_animal_pec_raca_to_string;
        }
    
        $values = PecAnimal::where('pec_origem_id', '=', $this->id)->getIndexedArray('pec_raca_id','{pec_raca->descricao}');
        return implode(', ', $values);
    }

    public function set_pec_animal_pec_pelagem_to_string($pec_animal_pec_pelagem_to_string)
    {
        if(is_array($pec_animal_pec_pelagem_to_string))
        {
            $values = PecPelagem::where('id', 'in', $pec_animal_pec_pelagem_to_string)->getIndexedArray('id', 'id');
            $this->pec_animal_pec_pelagem_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_animal_pec_pelagem_to_string = $pec_animal_pec_pelagem_to_string;
        }

        $this->vdata['pec_animal_pec_pelagem_to_string'] = $this->pec_animal_pec_pelagem_to_string;
    }

    public function get_pec_animal_pec_pelagem_to_string()
    {
        if(!empty($this->pec_animal_pec_pelagem_to_string))
        {
            return $this->pec_animal_pec_pelagem_to_string;
        }
    
        $values = PecAnimal::where('pec_origem_id', '=', $this->id)->getIndexedArray('pec_pelagem_id','{pec_pelagem->id}');
        return implode(', ', $values);
    }

    public function set_pec_animal_pec_categoria_to_string($pec_animal_pec_categoria_to_string)
    {
        if(is_array($pec_animal_pec_categoria_to_string))
        {
            $values = PecCategoria::where('id', 'in', $pec_animal_pec_categoria_to_string)->getIndexedArray('descricao', 'descricao');
            $this->pec_animal_pec_categoria_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_animal_pec_categoria_to_string = $pec_animal_pec_categoria_to_string;
        }

        $this->vdata['pec_animal_pec_categoria_to_string'] = $this->pec_animal_pec_categoria_to_string;
    }

    public function get_pec_animal_pec_categoria_to_string()
    {
        if(!empty($this->pec_animal_pec_categoria_to_string))
        {
            return $this->pec_animal_pec_categoria_to_string;
        }
    
        $values = PecAnimal::where('pec_origem_id', '=', $this->id)->getIndexedArray('pec_categoria_id','{pec_categoria->descricao}');
        return implode(', ', $values);
    }

    public function set_pec_animal_pec_brinco_to_string($pec_animal_pec_brinco_to_string)
    {
        if(is_array($pec_animal_pec_brinco_to_string))
        {
            $values = PecBrinco::where('id', 'in', $pec_animal_pec_brinco_to_string)->getIndexedArray('codigo', 'codigo');
            $this->pec_animal_pec_brinco_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_animal_pec_brinco_to_string = $pec_animal_pec_brinco_to_string;
        }

        $this->vdata['pec_animal_pec_brinco_to_string'] = $this->pec_animal_pec_brinco_to_string;
    }

    public function get_pec_animal_pec_brinco_to_string()
    {
        if(!empty($this->pec_animal_pec_brinco_to_string))
        {
            return $this->pec_animal_pec_brinco_to_string;
        }
    
        $values = PecAnimal::where('pec_origem_id', '=', $this->id)->getIndexedArray('pec_brinco_id','{pec_brinco->codigo}');
        return implode(', ', $values);
    }

    public function set_pec_animal_pec_sisbov_to_string($pec_animal_pec_sisbov_to_string)
    {
        if(is_array($pec_animal_pec_sisbov_to_string))
        {
            $values = PecSisbov::where('id', 'in', $pec_animal_pec_sisbov_to_string)->getIndexedArray('id', 'id');
            $this->pec_animal_pec_sisbov_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_animal_pec_sisbov_to_string = $pec_animal_pec_sisbov_to_string;
        }

        $this->vdata['pec_animal_pec_sisbov_to_string'] = $this->pec_animal_pec_sisbov_to_string;
    }

    public function get_pec_animal_pec_sisbov_to_string()
    {
        if(!empty($this->pec_animal_pec_sisbov_to_string))
        {
            return $this->pec_animal_pec_sisbov_to_string;
        }
    
        $values = PecAnimal::where('pec_origem_id', '=', $this->id)->getIndexedArray('pec_sisbov_id','{pec_sisbov->id}');
        return implode(', ', $values);
    }

    public function set_pec_animal_pec_lote_to_string($pec_animal_pec_lote_to_string)
    {
        if(is_array($pec_animal_pec_lote_to_string))
        {
            $values = PecLote::where('id', 'in', $pec_animal_pec_lote_to_string)->getIndexedArray('descricao', 'descricao');
            $this->pec_animal_pec_lote_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_animal_pec_lote_to_string = $pec_animal_pec_lote_to_string;
        }

        $this->vdata['pec_animal_pec_lote_to_string'] = $this->pec_animal_pec_lote_to_string;
    }

    public function get_pec_animal_pec_lote_to_string()
    {
        if(!empty($this->pec_animal_pec_lote_to_string))
        {
            return $this->pec_animal_pec_lote_to_string;
        }
    
        $values = PecAnimal::where('pec_origem_id', '=', $this->id)->getIndexedArray('pec_lote_id','{pec_lote->descricao}');
        return implode(', ', $values);
    }

    public function set_pec_animal_pec_origem_to_string($pec_animal_pec_origem_to_string)
    {
        if(is_array($pec_animal_pec_origem_to_string))
        {
            $values = PecOrigem::where('id', 'in', $pec_animal_pec_origem_to_string)->getIndexedArray('descricao', 'descricao');
            $this->pec_animal_pec_origem_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_animal_pec_origem_to_string = $pec_animal_pec_origem_to_string;
        }

        $this->vdata['pec_animal_pec_origem_to_string'] = $this->pec_animal_pec_origem_to_string;
    }

    public function get_pec_animal_pec_origem_to_string()
    {
        if(!empty($this->pec_animal_pec_origem_to_string))
        {
            return $this->pec_animal_pec_origem_to_string;
        }
    
        $values = PecAnimal::where('pec_origem_id', '=', $this->id)->getIndexedArray('pec_origem_id','{pec_origem->descricao}');
        return implode(', ', $values);
    }

    
}

