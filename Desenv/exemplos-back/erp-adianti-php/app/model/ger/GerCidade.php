<?php

class GerCidade extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    
    const TABLENAME = 'ger_cidade';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_uf;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('ativo');
        parent::addAttribute('nr_cidade');
        parent::addAttribute('ger_uf_id');
    }

    public function get_ger_uf()
    {
        if (empty($this->ger_uf)) {
            $this->ger_uf = new GerUf($this->ger_uf_id);
        }
        return $this->ger_uf;
    }

    public static function findIBGE($ibge)
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('nr_cidade', '=', $ibge));
        $repository = new TRepository('GerCidade');
        $cidade = $repository->load($criteria);
        return $cidade[0];
    }

}

?>