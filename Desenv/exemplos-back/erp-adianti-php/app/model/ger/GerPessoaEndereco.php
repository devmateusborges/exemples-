<?php

class GerPessoaEndereco extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'ger_pessoa_endereco';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_pessoa;
    private $end_ger_cidade;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('ger_pessoa_id');
        parent::addAttribute('ativo');
        parent::addAttribute('tipo');
        parent::addAttribute('padrao');
        parent::addAttribute('end_logradouro');
        parent::addAttribute('end_logradouro_nr');
        parent::addAttribute('end_bairro');
        parent::addAttribute('end_complemento');
        parent::addAttribute('end_cep');
        parent::addAttribute('end_ger_cidade_id');
        parent::addAttribute('fone');
        parent::addAttribute('email');
        parent::addAttribute('contato');
    }

    public function get_ger_pessoa()
    {
        if (empty($this->ger_pessoa)) {
            $this->ger_pessoa = new GerPessoa($this->ger_pessoa_id);
        }
        return $this->ger_pessoa;
    }

    public function set_ger_pessoa(GerPessoa $object)
    {
        $this->ger_pessoa = $object;
        $this->ger_pessoa_id = $object->id;
    }

    public function get_end_ger_cidade()
    {
        if (empty($this->end_ger_cidade)) {
            $this->end_ger_cidade = new GerCidade($this->end_ger_cidade_id);
        }
        return $this->end_ger_cidade;
    }

    public function set_end_ger_cidade(GerCidade $object)
    {
        $this->end_ger_cidade = $object;
        $this->end_ger_cidade_id = $object->id;
    }

    public static function findEndereco($id_cliente, $rua, $numero, $cep)
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('ger_pessoa_id', '=', $id_cliente));
        $criteria->add(new TFilter('end_logradouro', '=', $rua));
        $criteria->add(new TFilter('end_logradouro_nr', '=', $numero));
        $criteria->add(new TFilter('end_cep', '=', $cep));
        $repository = new TRepository('GerPessoaEndereco');
        $pessoaEndereco = $repository->load($criteria);
        return $pessoaEndereco[0];
    }
}
