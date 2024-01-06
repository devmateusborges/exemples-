<?php

class ImportacaoXMLService
{

    private $doc;

    private function carregaXML()
    {
        $file = file_get_contents('./files/exemplos_nf_xml/NFA_Avulsa_GO.xml');

        $this->doc = new DOMDocument('1.0', 'utf-8');
        $this->doc->loadXML($file);
    }

    private function pSimpleGetValue($theObj, $keyName, $itemNum = 0)
    {
        return $theObj->getElementsByTagName($keyName)->item($itemNum)->nodeValue;
    }

    public function importa()
    {

        try {
            TTransaction::open(TSession::getValue('pConn'));

            $this->carregaXML();
            $gerEmpresa = new GerEmpresa(1); // @todo

            $infNFe = $this->doc->getElementsByTagName('infNFe')->item(0);
            $ide = $this->doc->getElementsByTagName('ide')->item(0);
            $emit = $this->doc->getElementsByTagName('emit')->item(0);
            $det = $this->doc->getElementsByTagName('det');
            $total = $this->doc->getElementsByTagName('total')->item(0);
            $transp = $this->doc->getElementsByTagName('transp')->item(0);

            $gerPessoaEmitente = new GerPessoa();
            if (!empty($emit->getElementsByTagName('CNPJ')->item(0)->nodeValue)) {
                $pessoaEmitente = $gerPessoaEmitente::findCNPJ($this->pSimpleGetValue($emit, 'CNPJ'));
            } else {
                $pessoaEmitente = $gerPessoaEmitente::findCPF($this->pSimpleGetValue($emit, 'CPF'));
            }
            if ($pessoaEmitente != null) {
                $gerPessoaEmitente->id = $pessoaEmitente->id;
            }
            $gerPessoaEmitente->unit_id = 1;
            $gerPessoaEmitente->nome = $this->pSimpleGetValue($emit, 'xNome');
            $gerPessoaEmitente->razao_social = $this->pSimpleGetValue($emit, 'xNome');
            $gerPessoaEmitente->ativo = 'S';
            $gerPessoaEmitente->contrib_icms = '1'; //contribuinte de icms
            if (!empty($emit->getElementsByTagName('CNPJ')->item(0)->nodeValue)) {
                $gerPessoaEmitente->doc_cnpj = $this->pSimpleGetValue($emit, 'CNPJ');
            } else {
                $gerPessoaEmitente->doc_cpf = $this->pSimpleGetValue($emit, 'CPF');
            }
            $gerPessoaEmitente->doc_ie = $this->pSimpleGetValue($emit, 'IE');
            $gerPessoaEmitente->fis_regime = $this->pSimpleGetValue($emit, 'CRT');
            $gerPessoaEmitente->fone = $this->pSimpleGetValue($emit, 'fone');
            $encontrouCliente = (intval($gerPessoaEmitente->id) > 0);
            $gerPessoaEmitente->store();

            $gerPessoaEmitenteEndereco = new GerPessoaEndereco();
            if ($encontrouCliente) {
                $pessoaEmitenteEndereco = $gerPessoaEmitenteEndereco::findEndereco(
                    $gerPessoaEmitente->id,
                    $this->pSimpleGetValue($emit, 'xLgr'),
                    $this->pSimpleGetValue($emit, 'nro'),
                    $this->pSimpleGetValue($emit, 'CEP')
                );
            } else {
                $pessoaEmitenteEndereco = new GerPessoaEndereco();
                $pessoaEmitenteEndereco->unit_id = 1;
                $pessoaEmitenteEndereco->ger_pessoa_id = $gerPessoaEmitente->id;
                $pessoaEmitenteEndereco->ativo = 'S';
                $pessoaEmitenteEndereco->padrao = 'S';
                $pessoaEmitenteEndereco->end_logradouro = $this->pSimpleGetValue($emit, 'xLgr');
                $pessoaEmitenteEndereco->end_logradouro_nr = $this->pSimpleGetValue($emit, 'nro');
                $pessoaEmitenteEndereco->end_bairro = $this->pSimpleGetValue($emit, 'xBairro');
                $pessoaEmitenteEndereco->end_complemento = $this->pSimpleGetValue($emit, 'xBairro');
                $pessoaEmitenteEndereco->end_cep = $this->pSimpleGetValue($emit, 'CEP');
                $cidade = new GerCidade();
                $cidade = $cidade::findIBGE($this->pSimpleGetValue($emit, 'cMun'));
                $pessoaEmitenteEndereco->end_ger_cidade_id = $cidade->id;
                $pessoaEmitenteEndereco->store();
            }

            $movimento = new Mov();
            $movimento->unit_id = 1;
            $movimento->nr_externo = $this->pSimpleGetValue($ide, 'nNF');
            $movimento->ger_pessoa_id = $gerPessoaEmitente->id;
            $movimento->ger_pessoa_endereco_id_fiscal = $pessoaEmitenteEndereco->id;
            $movimento->ger_pessoa_endereco_id_entrega = $pessoaEmitenteEndereco->id; // @todo
            $movimento->mov_operacao_id = 10;
            $movimento->fin_cond_pagrec_id = 1; // @todo
            $movimento->data_mov = date("Y-m-d", strtotime($this->pSimpleGetValue($ide, 'dhEmi')));
            $movimento->numero_mov = $this->pSimpleGetValue($ide, 'nNF');
            $movimento->data_emissao = date("Y-m-d", strtotime($this->pSimpleGetValue($ide, 'dhEmi')));
            $movimento->mov_tipo_id = 4;
            $movimento->fis_doc_tipo_id = 1; // @todo
            $movimento->serie_mov = $this->pSimpleGetValue($ide, 'serie');
            //$movimento->mov_status_id = 1; // @todo
            $movimento->valor_total = $this->pSimpleGetValue($total, 'vNF');
            $movimento->ger_empresa_id = 1; // @todo
            $movimento->tipo_frete = $this->pSimpleGetValue($transp, 'modFrete');
            $movimento->store();

            foreach ($det as $key => $item) {
                $imposto = $item->getElementsByTagName('imposto')->item(0);
                $gerItemServPessoa = new GerItemServPessoa();
                $itemServ = $gerItemServPessoa::findItemExt(
                    $pessoaEmitente->id,
                    $this->pSimpleGetValue($item, 'cProd')
                );
                $movItemServ = new MovItemServ();
                $movItemServ->unit_id = 1;
                $movItemServ->mov_id = $movimento->id;
                if ($itemServ == null) {
                    $movItemServ->ger_itemserv_id = 1; // @todo produto padrão
                } else {
                    $movItemServ->ger_itemserv_id = $itemServ->ger_itemserv->id;
                }
                $gerUnidadeMedida = new GerUmedida();
                $sigla = $this->pSimpleGetValue($item, 'uCom');
                $gerUnidadeMedida = $gerUnidadeMedida::findSigla($sigla);
                if ($gerUnidadeMedida == null) {
                    throw new Exception("Unidade de medida '$sigla' não cadastrada.");
                }
                $movItemServ->qnt_orig = $this->pSimpleGetValue($item, 'qCom');
                $movItemServ->qnt_devolvida = 0; // @todo
                $movItemServ->valor_unit_orig = $this->pSimpleGetValue($item, 'vUnCom');
                $movItemServ->ger_umedida_conv_id_conv = $gerUnidadeMedida->id;
                $movItemServ->qnt_conv = $this->pSimpleGetValue($item, 'qCom');
                $movItemServ->valor_unit_conv = $this->pSimpleGetValue($item, 'vUnCom');
                $movItemServ->valor_bruto = $this->pSimpleGetValue($item, 'vProd');
                $movItemServ->valor_desconto = number_format($this->pSimpleGetValue($item, 'vDesc'), 2, '.', '');
                $movItemServ->valor_acrecimo = 0; // @todo
                $movItemServ->valor_outros = number_format($this->pSimpleGetValue($item, 'vOutros'), 2, '.', '');
                $movItemServ->valor_frete = number_format($this->pSimpleGetValue($item, 'vFrete'), 2, '.', '');
                $movItemServ->valor_seguro = number_format($this->pSimpleGetValue($item, 'vSeg'), 2, '.', '');
                $movItemServ->valor_liquido = $movItemServ->valor_bruto + $movItemServ->valor_outros + $movItemServ->valor_frete + $movItemServ->valor_seguro - $movItemServ->valor_desconto;
                $movItemServ->valor_tributo_retido = 0; // @todo

                $fisCfop = new FisCfop();
                $cfop = $this->pSimpleGetValue($item, 'CFOP');
                $fisCfop = $fisCfop::findCfop($cfop);
                if ($fisCfop == null) {
                    throw new Exception("CFOP '$cfop' não cadastrado.");
                }
                $movItemServ->fis_cfop_id = $fisCfop->id;
                $movItemServ->store();

                $fisTributacao = new FisTributacao();
                $impostosItem = $fisTributacao::processaImpostos(
                    $this->doc->saveXML($imposto),
                    $key + 1,
                    $gerEmpresa->fis_regime
                );
                // grava a tributação do item
                foreach ($impostosItem['impostos'] as $imposto) {
                    if ($imposto->CST == null) {
                        continue;
                    }
                    $fisTributo = new FisTributo();
                    $tributo = $fisTributo::findTributo($imposto->tributo);

                    $fisTributacao = new FisTributacao();
                    $fisTributacao->mov_id = $movimento->id;
                    $fisTributacao->mov_itemserv_id = $movItemServ->id;
                    $fisTributacao->fis_tributo_id = $tributo->id;
                    $fisTributacao->cst = $imposto->CST;
                    $fisTributacao->modalidade_base_calc = '1'; // @todo
                    $fisTributacao->valor_base_calc = number_format($imposto->valorBaseCalculo, 2, '.', '');
                    $fisTributacao->perc_aliquota = number_format($imposto->percencualAliquota, 2, '.', '');
                    $fisTributacao->valor_imposto = number_format($imposto->valorImposto, 2, '.', '');
                    $fisTributacao->valor_base_calc_isento = 0;
                    $fisTributacao->perc_aliquota_isento = 0;
                    $fisTributacao->valor_imposto_insento = 0;
                    $fisTributacao->valor_base_calc_st = number_format($imposto->valorReducaoBaseCalculo, 2, '.', '');
                    $fisTributacao->margem_agregada_st = number_format($imposto->percentualMargemValorAgregado, 2, '.', '');
                    $fisTributacao->perc_aliquota_st = number_format($imposto->percentualST, 2, '.', '');
                    $fisTributacao->valor_imposto_st = number_format($imposto->valorST, 2, '.', '');
                    $fisTributacao->perc_reducao_base_calc = number_format($imposto->percentualReducaoBaseCalculo, 2, '.', '');
                    $fisTributacao->valor_imposto_operacao = 0;
                    $fisTributacao->valor_imposto_diferido = 0;
                    $fisTributacao->perc_credito_sn = 0;
                    $fisTributacao->valor_credito_sn = 0;
                    $fisTributacao->valor_base_calc_fcp = 0;
                    $fisTributacao->perc_aliquota_fcp = 0;
                    $fisTributacao->valor_imposto_fcp = 0;
                    $fisTributacao->valor_base_calc_fcp_st = number_format($imposto->valorBaseCalculoFCPST, 2, '.', '');
                    $fisTributacao->perc_aliquota_fcp_st = number_format($imposto->percencualAliquotaFCPST, 2, '.', '');
                    $fisTributacao->valor_imposto_fcp_st = number_format($imposto->valorFCPST, 2, '.', '');
                    $fisTributacao->store();
                }
            }
            // cria o fis_doc
            $fisDoc = new FisDoc();
            $fisDoc->unit_id = 1;
            $fisDoc->mov_id = $movimento->id;
            $fisDoc->ger_empresa_id = $movimento->ger_empresa_id;
            $fisDoc->data_emissao = date("Y-m-d", strtotime($this->pSimpleGetValue($ide, 'dhEmi')));
            $fisDoc->chave = str_replace('NFe', '', $infNFe->getAttribute("Id"));
            $fisDoc->numero = $this->pSimpleGetValue($ide, 'nNF');
            $fisDoc->serie = $this->pSimpleGetValue($ide, 'serie');
            $fisDoc->fis_doc_tipo_id = $movimento->fis_doc_tipo->id;
            $fisDoc->ambiente = $this->pSimpleGetValue($ide, 'tpAmb');
            $fisDoc->tipo_emissao = $this->pSimpleGetValue($ide, 'tpEmis');
            $fisDoc->store();

            echo "sucesso";
            TTransaction::close();
        } catch (Exception $e) {
            echo $e->getMessage();
        }

    }

}