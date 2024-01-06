<?php

class Teste3 extends TPage
{
   
    public function __construct()
    {
        parent::__construct();

        $importacao = new ImportacaoXMLService();
        $importacao->importa();
    }


}
