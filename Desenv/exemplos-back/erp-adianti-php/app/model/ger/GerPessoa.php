<?php

class GerPessoa extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'ger_pessoa';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('nome');
        parent::addAttribute('razao_social');
        parent::addAttribute('ativo');
        parent::addAttribute('doc_cnpj');
        parent::addAttribute('doc_cpf');
        parent::addAttribute('doc_ie');
        parent::addAttribute('doc_im');
        parent::addAttribute('doc_cnae');
        parent::addAttribute('data_abertura');
        parent::addAttribute('doc_junta');
        parent::addAttribute('fis_regime');
        parent::addAttribute('fone_1');
        parent::addAttribute('fone_2');
        parent::addAttribute('fone_3');
        parent::addAttribute('contato_1');
        parent::addAttribute('contato_2');
        parent::addAttribute('contato_3');
        parent::addAttribute('contrib_icms');
        parent::addAttribute('nr_rntrc');
    }


    public function get_ger_pessoa_endereco()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('ger_pessoa_id', '=', $this->id));
        return GerPessoaEndereco::getObjects($criteria);
    }

    public function get_ger_pessoa_conta_banco()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('ger_pessoa_id', '=', $this->id));
        return GerPessoaContaBanco::getObjects($criteria);
    }

    public static function findCNPJ($cnpj)
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('doc_cnpj', '=', $cnpj));
        $repository = new TRepository('GerPessoa');
        $pessoa = $repository->load($criteria);
        return $pessoa[0];
    }

    public static function findCPF($cpf)
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('doc_cpf', '=', $cpf));
        $repository = new TRepository('GerPessoa');
        $pessoa = $repository->load($criteria);
        return $pessoa[0];
    }

}

?>