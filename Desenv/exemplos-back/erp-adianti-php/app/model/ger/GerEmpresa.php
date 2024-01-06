<?php

class GerEmpresa extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'ger_empresa';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $end_ger_cidade;
    private $fis_certificado;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('nome');
        parent::addAttribute('razao_social');
        parent::addAttribute('ativo');
        parent::addAttribute('sigla_empresa');
        parent::addAttribute('doc_cnpj');
        parent::addAttribute('doc_cpf');
        parent::addAttribute('doc_ie');
        parent::addAttribute('doc_im');
        parent::addAttribute('doc_cnae');
        parent::addAttribute('data_abertura');
        parent::addAttribute('doc_junta');
        parent::addAttribute('fis_regime');
        parent::addAttribute('fis_contador_nome');
        parent::addAttribute('fis_contador_crc');
        parent::addAttribute('fis_contador_cpf');
        parent::addAttribute('fis_contador_crc_seq');
        parent::addAttribute('fis_contador_crc_org_exp');
        parent::addAttribute('data_validade_a3');
        parent::addAttribute('data_validade_a1');
        parent::addAttribute('end_logradouro');
        parent::addAttribute('end_logradouro_nr');
        parent::addAttribute('end_bairro');
        parent::addAttribute('end_complemento');
        parent::addAttribute('end_cep');
        parent::addAttribute('end_ger_cidade_id');
        parent::addAttribute('fone_1');
        parent::addAttribute('fone_2');
        parent::addAttribute('fone_3');
        parent::addAttribute('contato_1');
        parent::addAttribute('contato_2');
        parent::addAttribute('contato_3');
        parent::addAttribute('email_1');
        parent::addAttribute('doc_rntrc');
        parent::addAttribute('fis_certificado_id');
    }

    public function get_end_ger_cidade()
    {
        if (empty($this->end_ger_cidade)) {
            $this->end_ger_cidade = new GerCidade($this->end_ger_cidade_id);
        }
        return $this->end_ger_cidade;
    }

    public function get_fis_certificado()
    {
        if (empty($this->fis_certificado)) {
            $this->fis_certificado = new FisCertificado($this->fis_certificado_id);
        }
        return $this->fis_certificado;
    }

}

?>