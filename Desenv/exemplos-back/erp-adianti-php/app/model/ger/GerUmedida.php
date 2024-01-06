<?php

class GerUmedida extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;

    const TABLENAME = 'ger_umedida';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('sigla_umedida');
        parent::addAttribute('nr_umedida');
    }

    public static function findSigla($sigla)
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('sigla_umedida', '=', $sigla));
        $repository = new TRepository('GerUmedida');
        $unidade = $repository->load($criteria);
        return $unidade[0];
    }

}

?>