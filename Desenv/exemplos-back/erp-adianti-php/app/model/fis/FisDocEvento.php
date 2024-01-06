<?php

class FisDocEvento extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'fis_doc_evento';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('fis_doc_id');
        parent::addAttribute('xml_retorno');
        parent::addAttribute('tipo_evento');
        parent::addAttribute('nr_protocolo');
        parent::addAttribute('qnt_evento');
        parent::addAttribute('descricao_evento');
    }

}

?>