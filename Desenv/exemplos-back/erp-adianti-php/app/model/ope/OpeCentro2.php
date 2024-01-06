<?php

class OpeCentro2 extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'ope_centro2';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ope_centro1;
    private $ger_pessoa_endereco;
    private $ope_centro2_equip;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('nome');
        parent::addAttribute('ativo');
        parent::addAttribute('sigla_centro2');
        parent::addAttribute('ope_centro1_id');
        parent::addAttribute('ope_centro_subgrupo_id');
        parent::addAttribute('utiliza_compart');
        parent::addAttribute('observacao');
        parent::addAttribute('ope_centro_rat_tipo_id');
        parent::addAttribute('ger_marca_modelo_id');
        parent::addAttribute('tipo_prop');
        parent::addAttribute('ger_pessoa_endereco_id');
    }

    public function get_ope_centro1()
    {
        if (empty($this->ope_centro1)) {
            $this->ope_centro1 = new OpeCentro1($this->ope_centro1_id);
        }
        return $this->ope_centro1;
    }

    public function get_ope_centro2_equip()
    {
        if (empty($this->ope_centro2_equip)) {
            $criteria = new TCriteria;
            $criteria->add(new TFilter('ope_centro2_id', '=', $this->id));
            $repository = new TRepository('OpeCentro2Equip');
            $this->ope_centro2_equip = $repository->load($criteria)[0];
        }
        return $this->ope_centro2_equip;
    }

    public function get_ger_pessoa_endereco()
    {
        if (empty($this->ger_pessoa_endereco)) {
            $this->ger_pessoa_endereco = new GerPessoaEndereco($this->ger_pessoa_endereco_id);
        }
        return $this->ger_pessoa_endereco;
    }

}

?>