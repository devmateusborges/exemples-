<?php

class PecAnimal extends TRecord
{
    const TABLENAME  = 'pec_animal';
    const PRIMARYKEY = 'id';
    const IDPOLICY   =  'uuid'; // {max, serial}

    private $pec_raca;
    private $pec_pelagem;
    private $system_unit;
    private $pec_categoria;
    private $pec_brinco;
    private $pec_sisbov;
    private $pec_lote;
    private $pec_origem;

    

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
        parent::addAttribute('dt_entrada');
        parent::addAttribute('status');
        parent::addAttribute('dt_nascimento');
        parent::addAttribute('observacao');
        parent::addAttribute('pec_raca_id');
        parent::addAttribute('pec_pelagem_id');
        parent::addAttribute('pec_categoria_id');
        parent::addAttribute('pec_brinco_id');
        parent::addAttribute('pec_sisbov_id');
        parent::addAttribute('pec_animal_id_pai');
        parent::addAttribute('pec_animal_id_mae');
        parent::addAttribute('pec_lote_id');
        parent::addAttribute('pec_origem_id');
        parent::addAttribute('rgn');
        parent::addAttribute('rgd');
        parent::addAttribute('dt_desmama');
        parent::addAttribute('vr_custo_entrada');
        parent::addAttribute('vr_custo_kg');
        parent::addAttribute('vr_custos_extra');
        parent::addAttribute('codigo_rastreio');
            
    }

    /**
     * Method set_pec_raca
     * Sample of usage: $var->pec_raca = $object;
     * @param $object Instance of PecRaca
     */
    public function set_pec_raca(PecRaca $object)
    {
        $this->pec_raca = $object;
        $this->pec_raca_id = $object->id;
    }

    /**
     * Method get_pec_raca
     * Sample of usage: $var->pec_raca->attribute;
     * @returns PecRaca instance
     */
    public function get_pec_raca()
    {
    
        // loads the associated object
        if (empty($this->pec_raca))
            $this->pec_raca = new PecRaca($this->pec_raca_id);
    
        // returns the associated object
        return $this->pec_raca;
    }
    /**
     * Method set_pec_pelagem
     * Sample of usage: $var->pec_pelagem = $object;
     * @param $object Instance of PecPelagem
     */
    public function set_pec_pelagem(PecPelagem $object)
    {
        $this->pec_pelagem = $object;
        $this->pec_pelagem_id = $object->id;
    }

    /**
     * Method get_pec_pelagem
     * Sample of usage: $var->pec_pelagem->attribute;
     * @returns PecPelagem instance
     */
    public function get_pec_pelagem()
    {
    
        // loads the associated object
        if (empty($this->pec_pelagem))
            $this->pec_pelagem = new PecPelagem($this->pec_pelagem_id);
    
        // returns the associated object
        return $this->pec_pelagem;
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
     * Method set_pec_categoria
     * Sample of usage: $var->pec_categoria = $object;
     * @param $object Instance of PecCategoria
     */
    public function set_pec_categoria(PecCategoria $object)
    {
        $this->pec_categoria = $object;
        $this->pec_categoria_id = $object->id;
    }

    /**
     * Method get_pec_categoria
     * Sample of usage: $var->pec_categoria->attribute;
     * @returns PecCategoria instance
     */
    public function get_pec_categoria()
    {
    
        // loads the associated object
        if (empty($this->pec_categoria))
            $this->pec_categoria = new PecCategoria($this->pec_categoria_id);
    
        // returns the associated object
        return $this->pec_categoria;
    }
    /**
     * Method set_pec_brinco
     * Sample of usage: $var->pec_brinco = $object;
     * @param $object Instance of PecBrinco
     */
    public function set_pec_brinco(PecBrinco $object)
    {
        $this->pec_brinco = $object;
        $this->pec_brinco_id = $object->id;
    }

    /**
     * Method get_pec_brinco
     * Sample of usage: $var->pec_brinco->attribute;
     * @returns PecBrinco instance
     */
    public function get_pec_brinco()
    {
    
        // loads the associated object
        if (empty($this->pec_brinco))
            $this->pec_brinco = new PecBrinco($this->pec_brinco_id);
    
        // returns the associated object
        return $this->pec_brinco;
    }
    /**
     * Method set_pec_sisbov
     * Sample of usage: $var->pec_sisbov = $object;
     * @param $object Instance of PecSisbov
     */
    public function set_pec_sisbov(PecSisbov $object)
    {
        $this->pec_sisbov = $object;
        $this->pec_sisbov_id = $object->id;
    }

    /**
     * Method get_pec_sisbov
     * Sample of usage: $var->pec_sisbov->attribute;
     * @returns PecSisbov instance
     */
    public function get_pec_sisbov()
    {
    
        // loads the associated object
        if (empty($this->pec_sisbov))
            $this->pec_sisbov = new PecSisbov($this->pec_sisbov_id);
    
        // returns the associated object
        return $this->pec_sisbov;
    }
    /**
     * Method set_pec_lote
     * Sample of usage: $var->pec_lote = $object;
     * @param $object Instance of PecLote
     */
    public function set_pec_lote(PecLote $object)
    {
        $this->pec_lote = $object;
        $this->pec_lote_id = $object->id;
    }

    /**
     * Method get_pec_lote
     * Sample of usage: $var->pec_lote->attribute;
     * @returns PecLote instance
     */
    public function get_pec_lote()
    {
    
        // loads the associated object
        if (empty($this->pec_lote))
            $this->pec_lote = new PecLote($this->pec_lote_id);
    
        // returns the associated object
        return $this->pec_lote;
    }
    /**
     * Method set_pec_origem
     * Sample of usage: $var->pec_origem = $object;
     * @param $object Instance of PecOrigem
     */
    public function set_pec_origem(PecOrigem $object)
    {
        $this->pec_origem = $object;
        $this->pec_origem_id = $object->id;
    }

    /**
     * Method get_pec_origem
     * Sample of usage: $var->pec_origem->attribute;
     * @returns PecOrigem instance
     */
    public function get_pec_origem()
    {
    
        // loads the associated object
        if (empty($this->pec_origem))
            $this->pec_origem = new PecOrigem($this->pec_origem_id);
    
        // returns the associated object
        return $this->pec_origem;
    }

    
}

