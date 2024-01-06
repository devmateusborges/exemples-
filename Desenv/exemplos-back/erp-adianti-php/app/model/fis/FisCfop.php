<?php

class FisCfop extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;

    const TABLENAME = 'fis_cfop';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('nr_cfop');
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('data_validade');
    }

    public static function findCfop($cfop)
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('nr_cfop', '=', $cfop));
        $repository = new TRepository('FisCfop');
        $cfop = $repository->load($criteria);
        return $cfop[0];
    }

}

?>