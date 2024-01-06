<?php

class FisTributo extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;

    const TABLENAME = 'fis_tributo';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('nr_tributo');
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
    }

    public static function findTributo($tributo)
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('nr_tributo', '=', $tributo));
        $repository = new TRepository('FisTributo');
        $tributo = $repository->load($criteria);
        return $tributo[0];
    }

}

?>