<?php

use NFePHP\Common\Keys;

class BaseService
{

    protected $config;

    protected $movimento;

    protected $path;

    const C_TRIBUTO_ICMS = 1;

    const C_TRIBUTO_IPI = 2;

    const C_TRIBUTO_IR = 3;

    const C_TRIBUTO_ST = 5;

    const C_TRIBUTO_INSS = 6;

    const C_TRIBUTO_CSLL = 7;

    const C_TRIBUTO_PIS = 9;

    const C_VERSAO_APP = '1.0.0b';

    const C_SEM_GTIN = 'SEM GTIN';

    const C_TRIBUTO_COFINS = 10;

    const C_EVENTO_AUTORIZACAO = 'Autorização';

    const C_EVENTO_CANCELAMENTO = 'Cancelamento';

    const C_EVENTO_INUTILIZACAO = 'Inutilização';

    const C_EVENTO_ENCERRAMENTO = 'Encerramento';

    const C_NFE_VERSAO = '4.00';

    const C_NFE_SCHEMES = 'PL_009_V4';

    const C_CTE_VERSAO = '3.00';

    const C_CTE_VERSAO_MODAL = '3.00';

    const C_CTE_SCHEMES = 'PL_CTe_300';

    const C_CTE_HOM = 'CT-E EMITIDO EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL';

    const C_MDFE_VERSAO = '3.00';

    const C_MDFE_SCHEMES = 'PL_MDFe_300';

    const C_MDFE_VERSAO_MODAL = '3.00';

    protected function geraDocumentoFiscal()
    {
        if ($this->movimento->fis_doc == null) {
            $numero = intval($this->movimento->mov_operacao->ger_numeracao->ultimo_nr) + 1;
            $modelo = $this->movimento->fis_doc_tipo->modelo;
            $serie = $this->movimento->mov_operacao->ger_numeracao->serie;
            // gera a chave de acesso
            $chave = Keys::build(
                $this->movimento->ger_empresa->end_ger_cidade->ger_uf->nr_uf,
                date("y"),
                date("m"),
                $this->movimento->ger_empresa->doc_cnpj,
                $modelo,
                $serie,
                $numero,
                $tpEmis = 1 // 1 - Normal; 2 - Contingencia
            );
            // cria o fis_doc
            $fisDoc = new FisDoc();
            $fisDoc->unit_id = $this->movimento->unit_id;
            $fisDoc->mov_id = $this->movimento->id;
            $fisDoc->ger_empresa_id = $this->movimento->ger_empresa_id;
            $fisDoc->data_emissao = date("Y-m-d");
            $fisDoc->chave = $chave;
            $fisDoc->numero = $numero;
            $fisDoc->serie = $serie;
            $fisDoc->fis_doc_tipo_id = $this->movimento->fis_doc_tipo->id;
            $fisDoc->ambiente = $this->movimento->fis_doc_tipo->ambiente;
            $fisDoc->tipo_emissao = $tpEmis;
            $fisDoc->store();
            // atualiza o ultimo numero utilizado
            $gerNumeracao = new GerNumeracao();
            $gerNumeracao->id = $this->movimento->mov_operacao->ger_numeracao->id;
            $gerNumeracao->unit_id = $this->movimento->mov_operacao->ger_numeracao->unit_id;
            $gerNumeracao->ultimo_nr = $numero;
            $gerNumeracao->store();
        }
    }

}