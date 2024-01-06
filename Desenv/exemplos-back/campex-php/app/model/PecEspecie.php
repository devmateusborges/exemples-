<?php

class PecEspecie extends TRecord
{
    const TABLENAME  = 'pec_especie';
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
        parent::addAttribute('observacao');
        parent::addAttribute('tempo_gestacao');
        parent::addAttribute('primeira_cobertura');
        parent::addAttribute('diagnostico_apos_cobertura');
        parent::addAttribute('proximo_cruzamento');
        parent::addAttribute('tempo_lactacao');
        parent::addAttribute('idade_desmama');
        parent::addAttribute('nomenclatura_filhote');
            
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
     * Method getPecRacas
     */
    public function getPecRacas()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('pec_especie_id', '=', $this->id));
        return PecRaca::getObjects( $criteria );
    }
    /**
     * Method getPecCategorias
     */
    public function getPecCategorias()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('pec_especie_id', '=', $this->id));
        return PecCategoria::getObjects( $criteria );
    }

    public function set_pec_raca_system_unit_to_string($pec_raca_system_unit_to_string)
    {
        if(is_array($pec_raca_system_unit_to_string))
        {
            $values = SystemUnit::where('id', 'in', $pec_raca_system_unit_to_string)->getIndexedArray('name', 'name');
            $this->pec_raca_system_unit_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_raca_system_unit_to_string = $pec_raca_system_unit_to_string;
        }

        $this->vdata['pec_raca_system_unit_to_string'] = $this->pec_raca_system_unit_to_string;
    }

    public function get_pec_raca_system_unit_to_string()
    {
        if(!empty($this->pec_raca_system_unit_to_string))
        {
            return $this->pec_raca_system_unit_to_string;
        }
    
        $values = PecRaca::where('pec_especie_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
        return implode(', ', $values);
    }

    public function set_pec_raca_pec_especie_to_string($pec_raca_pec_especie_to_string)
    {
        if(is_array($pec_raca_pec_especie_to_string))
        {
            $values = PecEspecie::where('id', 'in', $pec_raca_pec_especie_to_string)->getIndexedArray('descricao', 'descricao');
            $this->pec_raca_pec_especie_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_raca_pec_especie_to_string = $pec_raca_pec_especie_to_string;
        }

        $this->vdata['pec_raca_pec_especie_to_string'] = $this->pec_raca_pec_especie_to_string;
    }

    public function get_pec_raca_pec_especie_to_string()
    {
        if(!empty($this->pec_raca_pec_especie_to_string))
        {
            return $this->pec_raca_pec_especie_to_string;
        }
    
        $values = PecRaca::where('pec_especie_id', '=', $this->id)->getIndexedArray('pec_especie_id','{pec_especie->descricao}');
        return implode(', ', $values);
    }

    public function set_pec_categoria_system_unit_to_string($pec_categoria_system_unit_to_string)
    {
        if(is_array($pec_categoria_system_unit_to_string))
        {
            $values = SystemUnit::where('id', 'in', $pec_categoria_system_unit_to_string)->getIndexedArray('name', 'name');
            $this->pec_categoria_system_unit_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_categoria_system_unit_to_string = $pec_categoria_system_unit_to_string;
        }

        $this->vdata['pec_categoria_system_unit_to_string'] = $this->pec_categoria_system_unit_to_string;
    }

    public function get_pec_categoria_system_unit_to_string()
    {
        if(!empty($this->pec_categoria_system_unit_to_string))
        {
            return $this->pec_categoria_system_unit_to_string;
        }
    
        $values = PecCategoria::where('pec_especie_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
        return implode(', ', $values);
    }

    public function set_pec_categoria_pec_especie_to_string($pec_categoria_pec_especie_to_string)
    {
        if(is_array($pec_categoria_pec_especie_to_string))
        {
            $values = PecEspecie::where('id', 'in', $pec_categoria_pec_especie_to_string)->getIndexedArray('descricao', 'descricao');
            $this->pec_categoria_pec_especie_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_categoria_pec_especie_to_string = $pec_categoria_pec_especie_to_string;
        }

        $this->vdata['pec_categoria_pec_especie_to_string'] = $this->pec_categoria_pec_especie_to_string;
    }

    public function get_pec_categoria_pec_especie_to_string()
    {
        if(!empty($this->pec_categoria_pec_especie_to_string))
        {
            return $this->pec_categoria_pec_especie_to_string;
        }
    
        $values = PecCategoria::where('pec_especie_id', '=', $this->id)->getIndexedArray('pec_especie_id','{pec_especie->descricao}');
        return implode(', ', $values);
    }

    
}

