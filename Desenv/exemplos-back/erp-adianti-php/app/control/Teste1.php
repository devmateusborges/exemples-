<?php

class Teste1 extends TPage
{
   
    public function __construct()
    {
        parent::__construct();

        //$nfe = new NFeService();
        $importacao = new ImportacaoXMLService();
        $importacao->importa();
      
    }


}
