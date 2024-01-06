<?php

class FinPagRecParc extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'fin_pagrec_parc';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max';

    private $fin_doc_tipo;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('id');
        parent::addAttribute('numero_parc');
        parent::addAttribute('fin_pagrec_id');
        parent::addAttribute('fin_doc_tipo_id');
        parent::addAttribute('valor_pagrec');
        parent::addAttribute('valor_juro');
        parent::addAttribute('valor_desconto');
        parent::addAttribute('valor_multa');
    }

    public function get_fin_doc_tipo()
    {
        if (empty($this->fin_doc_tipo)) {
            $this->fin_doc_tipo = new FinDocTipo($this->fin_doc_tipo_id);
        }
        return $this->fin_doc_tipo;
    }

}

?>