<?php

class GerItemServPessoa extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;

    const TABLENAME = 'ger_itemserv_pessoa';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_itemserv;
    private $ger_pessoa;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('id');
        parent::addAttribute('ger_itemserv_id');
        parent::addAttribute('ger_pessoa_id');
        parent::addAttribute('cod_itemserv_ext');
    }

    public function get_ger_itemserv()
    {
        if (empty($this->ger_itemserv)) {
            $this->ger_itemserv = new GerItemServ($this->ger_itemserv_id);
        }
        return $this->ger_itemserv;
    }

    public function get_ger_pessoa()
    {
        if (empty($this->ger_pessoa)) {
            $this->ger_pessoa = new GerPessoa($this->ger_pessoa_id);
        }
        return $this->ger_pessoa;
    }

    public static function findItemExt($pessoa, $codExterno)
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('ger_pessoa_id', '=', $pessoa));
        $criteria->add(new TFilter('cod_itemserv_ext', '=', $codExterno));
        $repository = new TRepository('GerItemServPessoa');
        $item = $repository->load($criteria);
        return $item[0];
    }

}

?>