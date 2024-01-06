<?php

class FisDoc extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'fis_doc';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $fis_doc_tipo;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('data_emissao');
        parent::addAttribute('chave');
        parent::addAttribute('numero');
        parent::addAttribute('serie');
        parent::addAttribute('fis_doc_tipo_id');
        parent::addAttribute('numero_ini');
        parent::addAttribute('numero_fin');
        parent::addAttribute('data_autorizado');
        parent::addAttribute('data_cancelado');
        parent::addAttribute('data_encerrado');
        parent::addAttribute('xml_assinado');
        parent::addAttribute('xml_protocolado');
        parent::addAttribute('ambiente');
        parent::addAttribute('tipo_emissao');
        parent::addAttribute('status_sefaz');
        parent::addAttribute('ger_empresa_id');
    }

    public function get_fis_doc_tipo()
    {
        if (empty($this->fis_doc_tipo)) {
            $this->fis_doc_tipo = new FisDocTipo($this->fis_doc_tipo_id);
        }
        return $this->fis_doc_tipo;
    }

    public function getEvento($evento)
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('fis_doc_id', '=', $this->id));
        $criteria->add(new TFilter('tipo_evento', '=', $evento));
        $criteria->setProperty('order', 'id desc');
        $repository = new TRepository('FisDocEvento');
        $fisDocEvento = $repository->load($criteria);
        return $fisDocEvento[0];
    }

}

?>