<?php

class GerPessoaContaBanco extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
    
    const TABLENAME = 'ger_pessoa_conta_banco';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; 

    private $ger_pessoa;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);

        parent::addAttribute('unit_id');
        parent::addAttribute('ger_pessoa_id');
        parent::addAttribute('fin_banco_id');
        parent::addAttribute('agencia');
        parent::addAttribute('conta');
        parent::addAttribute('observacao');

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


}

?>