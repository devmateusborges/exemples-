<?php

class MovEntregaDoc extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
 
    const TABLENAME = 'mov_entrega_doc';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('mov_entrega_id');
        parent::addAttribute('valor_total');
        parent::addAttribute('mov_id_interno');
        parent::addAttribute('chave_documento');
        parent::addAttribute('modelo_documento');
        parent::addAttribute('serie_documento');
        parent::addAttribute('nr_documento');
        parent::addAttribute('subserie_documento');
        parent::addAttribute('data_emissao');
    }

}

?>