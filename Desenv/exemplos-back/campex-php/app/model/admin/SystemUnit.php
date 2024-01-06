<?php

class SystemUnit extends TRecord
{
    const TABLENAME  = 'system_unit';
    const PRIMARYKEY = 'id';
    const IDPOLICY   =  'max'; // {max, serial}

    

    /**
     * Constructor method
     */
    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('name');
        parent::addAttribute('connection_name');
            
    }

    /**
     * Method getPecAnimals
     */
    public function getPecAnimals()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('system_unit_id', '=', $this->id));
        return PecAnimal::getObjects( $criteria );
    }
    /**
     * Method getPecRacas
     */
    public function getPecRacas()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('system_unit_id', '=', $this->id));
        return PecRaca::getObjects( $criteria );
    }
    /**
     * Method getPecEspecies
     */
    public function getPecEspecies()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('system_unit_id', '=', $this->id));
        return PecEspecie::getObjects( $criteria );
    }
    /**
     * Method getPecPelagems
     */
    public function getPecPelagems()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('system_unit_id', '=', $this->id));
        return PecPelagem::getObjects( $criteria );
    }
    /**
     * Method getPecCategorias
     */
    public function getPecCategorias()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('system_unit_id', '=', $this->id));
        return PecCategoria::getObjects( $criteria );
    }
    /**
     * Method getPecOrigems
     */
    public function getPecOrigems()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('system_unit_id', '=', $this->id));
        return PecOrigem::getObjects( $criteria );
    }
    /**
     * Method getPecBrincos
     */
    public function getPecBrincos()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('system_unit_id', '=', $this->id));
        return PecBrinco::getObjects( $criteria );
    }
    /**
     * Method getAdmCcustos
     */
    public function getAdmCcustos()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('system_unit_id', '=', $this->id));
        return AdmCcusto::getObjects( $criteria );
    }
    /**
     * Method getPecFinalidades
     */
    public function getPecFinalidades()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('system_unit_id', '=', $this->id));
        return PecFinalidade::getObjects( $criteria );
    }
    /**
     * Method getPecLotes
     */
    public function getPecLotes()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('system_unit_id', '=', $this->id));
        return PecLote::getObjects( $criteria );
    }
    /**
     * Method getPecSisbovs
     */
    public function getPecSisbovs()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('system_unit_id', '=', $this->id));
        return PecSisbov::getObjects( $criteria );
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
    
        $values = PecAnimal::where('system_unit_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
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
    
        $values = PecAnimal::where('system_unit_id', '=', $this->id)->getIndexedArray('pec_raca_id','{pec_raca->descricao}');
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
    
        $values = PecAnimal::where('system_unit_id', '=', $this->id)->getIndexedArray('pec_pelagem_id','{pec_pelagem->id}');
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
    
        $values = PecAnimal::where('system_unit_id', '=', $this->id)->getIndexedArray('pec_categoria_id','{pec_categoria->descricao}');
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
    
        $values = PecAnimal::where('system_unit_id', '=', $this->id)->getIndexedArray('pec_brinco_id','{pec_brinco->codigo}');
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
    
        $values = PecAnimal::where('system_unit_id', '=', $this->id)->getIndexedArray('pec_sisbov_id','{pec_sisbov->id}');
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
    
        $values = PecAnimal::where('system_unit_id', '=', $this->id)->getIndexedArray('pec_lote_id','{pec_lote->descricao}');
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
    
        $values = PecAnimal::where('system_unit_id', '=', $this->id)->getIndexedArray('pec_origem_id','{pec_origem->descricao}');
        return implode(', ', $values);
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
    
        $values = PecRaca::where('system_unit_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
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
    
        $values = PecRaca::where('system_unit_id', '=', $this->id)->getIndexedArray('pec_especie_id','{pec_especie->descricao}');
        return implode(', ', $values);
    }

    public function set_pec_especie_system_unit_to_string($pec_especie_system_unit_to_string)
    {
        if(is_array($pec_especie_system_unit_to_string))
        {
            $values = SystemUnit::where('id', 'in', $pec_especie_system_unit_to_string)->getIndexedArray('name', 'name');
            $this->pec_especie_system_unit_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_especie_system_unit_to_string = $pec_especie_system_unit_to_string;
        }

        $this->vdata['pec_especie_system_unit_to_string'] = $this->pec_especie_system_unit_to_string;
    }

    public function get_pec_especie_system_unit_to_string()
    {
        if(!empty($this->pec_especie_system_unit_to_string))
        {
            return $this->pec_especie_system_unit_to_string;
        }
    
        $values = PecEspecie::where('system_unit_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
        return implode(', ', $values);
    }

    public function set_pec_pelagem_system_unit_to_string($pec_pelagem_system_unit_to_string)
    {
        if(is_array($pec_pelagem_system_unit_to_string))
        {
            $values = SystemUnit::where('id', 'in', $pec_pelagem_system_unit_to_string)->getIndexedArray('name', 'name');
            $this->pec_pelagem_system_unit_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_pelagem_system_unit_to_string = $pec_pelagem_system_unit_to_string;
        }

        $this->vdata['pec_pelagem_system_unit_to_string'] = $this->pec_pelagem_system_unit_to_string;
    }

    public function get_pec_pelagem_system_unit_to_string()
    {
        if(!empty($this->pec_pelagem_system_unit_to_string))
        {
            return $this->pec_pelagem_system_unit_to_string;
        }
    
        $values = PecPelagem::where('system_unit_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
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
    
        $values = PecCategoria::where('system_unit_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
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
    
        $values = PecCategoria::where('system_unit_id', '=', $this->id)->getIndexedArray('pec_especie_id','{pec_especie->descricao}');
        return implode(', ', $values);
    }

    public function set_pec_origem_system_unit_to_string($pec_origem_system_unit_to_string)
    {
        if(is_array($pec_origem_system_unit_to_string))
        {
            $values = SystemUnit::where('id', 'in', $pec_origem_system_unit_to_string)->getIndexedArray('name', 'name');
            $this->pec_origem_system_unit_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_origem_system_unit_to_string = $pec_origem_system_unit_to_string;
        }

        $this->vdata['pec_origem_system_unit_to_string'] = $this->pec_origem_system_unit_to_string;
    }

    public function get_pec_origem_system_unit_to_string()
    {
        if(!empty($this->pec_origem_system_unit_to_string))
        {
            return $this->pec_origem_system_unit_to_string;
        }
    
        $values = PecOrigem::where('system_unit_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
        return implode(', ', $values);
    }

    public function set_pec_brinco_system_unit_to_string($pec_brinco_system_unit_to_string)
    {
        if(is_array($pec_brinco_system_unit_to_string))
        {
            $values = SystemUnit::where('id', 'in', $pec_brinco_system_unit_to_string)->getIndexedArray('name', 'name');
            $this->pec_brinco_system_unit_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_brinco_system_unit_to_string = $pec_brinco_system_unit_to_string;
        }

        $this->vdata['pec_brinco_system_unit_to_string'] = $this->pec_brinco_system_unit_to_string;
    }

    public function get_pec_brinco_system_unit_to_string()
    {
        if(!empty($this->pec_brinco_system_unit_to_string))
        {
            return $this->pec_brinco_system_unit_to_string;
        }
    
        $values = PecBrinco::where('system_unit_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
        return implode(', ', $values);
    }

    public function set_adm_ccusto_system_unit_to_string($adm_ccusto_system_unit_to_string)
    {
        if(is_array($adm_ccusto_system_unit_to_string))
        {
            $values = SystemUnit::where('id', 'in', $adm_ccusto_system_unit_to_string)->getIndexedArray('name', 'name');
            $this->adm_ccusto_system_unit_to_string = implode(', ', $values);
        }
        else
        {
            $this->adm_ccusto_system_unit_to_string = $adm_ccusto_system_unit_to_string;
        }

        $this->vdata['adm_ccusto_system_unit_to_string'] = $this->adm_ccusto_system_unit_to_string;
    }

    public function get_adm_ccusto_system_unit_to_string()
    {
        if(!empty($this->adm_ccusto_system_unit_to_string))
        {
            return $this->adm_ccusto_system_unit_to_string;
        }
    
        $values = AdmCcusto::where('system_unit_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
        return implode(', ', $values);
    }

    public function set_pec_finalidade_system_unit_to_string($pec_finalidade_system_unit_to_string)
    {
        if(is_array($pec_finalidade_system_unit_to_string))
        {
            $values = SystemUnit::where('id', 'in', $pec_finalidade_system_unit_to_string)->getIndexedArray('name', 'name');
            $this->pec_finalidade_system_unit_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_finalidade_system_unit_to_string = $pec_finalidade_system_unit_to_string;
        }

        $this->vdata['pec_finalidade_system_unit_to_string'] = $this->pec_finalidade_system_unit_to_string;
    }

    public function get_pec_finalidade_system_unit_to_string()
    {
        if(!empty($this->pec_finalidade_system_unit_to_string))
        {
            return $this->pec_finalidade_system_unit_to_string;
        }
    
        $values = PecFinalidade::where('system_unit_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
        return implode(', ', $values);
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
    
        $values = PecLote::where('system_unit_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
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
    
        $values = PecLote::where('system_unit_id', '=', $this->id)->getIndexedArray('pec_finalidade_id','{pec_finalidade->descricao}');
        return implode(', ', $values);
    }

    public function set_pec_sisbov_system_unit_to_string($pec_sisbov_system_unit_to_string)
    {
        if(is_array($pec_sisbov_system_unit_to_string))
        {
            $values = SystemUnit::where('id', 'in', $pec_sisbov_system_unit_to_string)->getIndexedArray('name', 'name');
            $this->pec_sisbov_system_unit_to_string = implode(', ', $values);
        }
        else
        {
            $this->pec_sisbov_system_unit_to_string = $pec_sisbov_system_unit_to_string;
        }

        $this->vdata['pec_sisbov_system_unit_to_string'] = $this->pec_sisbov_system_unit_to_string;
    }

    public function get_pec_sisbov_system_unit_to_string()
    {
        if(!empty($this->pec_sisbov_system_unit_to_string))
        {
            return $this->pec_sisbov_system_unit_to_string;
        }
    
        $values = PecSisbov::where('system_unit_id', '=', $this->id)->getIndexedArray('system_unit_id','{system_unit->name}');
        return implode(', ', $values);
    }

    
}

