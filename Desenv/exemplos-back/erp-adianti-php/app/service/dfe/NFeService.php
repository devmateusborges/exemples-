<?php

use NFePHP\DA\NFe\Danfe;
use NFePHP\NFe\Complements;
use NFePHP\NFe\Make;

class NFeService extends BaseService
{

    function __construct()
    {
        if (method_exists($this, $_REQUEST['action'])) {
            call_user_func(array(
                $this,
                $_REQUEST['action']
            ));
        }
    }

    private function buscaDados($movimento)
    {
        $this->movimento = new Mov($movimento);

        $this->config = array(
            "atualizacao" => date('Y-m-d h:i:s'),
            "tpAmb" => $this->movimento->fis_doc_tipo->ambiente,
            "razaosocial" => $this->movimento->ger_empresa->razao_social,
            "cnpj" => $this->movimento->ger_empresa->doc_cnpj, // PRECISA SER VÁLIDO
            "ie" => $this->movimento->ger_empresa->doc_ie, // PRECISA SER VÁLIDO
            "siglaUF" => $this->movimento->ger_empresa->end_ger_cidade->ger_uf->sigla_uf,
            "schemes" => self::C_NFE_SCHEMES,
            "versao" => self::C_NFE_VERSAO,
            "tokenIBPT" => "",
            "CSC" => "",
            "CSCid" => "",
            "aProxyConf" => array(
                "proxyIp" => "",
                "proxyPort" => "",
                "proxyUser" => "",
                "proxyPass" => ""
            ),
            "cert" => array(
                "data" => $this->movimento->ger_empresa->fis_certificado->certificado,
                "senha" => $this->movimento->ger_empresa->fis_certificado->senha
            )
        );
        $this->path = sprintf('./files/%s', $this->config['cnpj']);
        @mkdir(sprintf('%s/pdf', $this->path), 0777, true);
        @mkdir(sprintf('%s/xml', $this->path), 0777, true);
    }

    public function geraDanfe()
    {
        try {
            TTransaction::open(TSession::getValue('pConn'));
            $this->danfe($_REQUEST['id']);
        } catch (\Exception $e) {
            echo $e->getMessage();
        } finally {
            TTransaction::close();
        }
    }

    private function danfe($movimento)
    {
        $this->buscaDados($movimento);
        $danfe = new Danfe($this->movimento->fis_doc->xml_protocolado, 'P', 'A4', '', 'I');
        $danfe->montaDANFE();
        $pdf = $danfe->render();
        file_put_contents(sprintf('%s/pdf/%s.pdf', $this->path, $this->movimento->fis_doc->chave), $pdf);
        header('Content-Type: application/pdf');
        echo $pdf;
    }

    public function envia()
    {
        try {
            TTransaction::open(TSession::getValue('pConn'));

            $this->buscaDados($_REQUEST['id']);
            $this->geraDocumentoFiscal();

            $xml = $this->montaXML();
            $tools = new NFePHP\NFe\Tools(json_encode($this->config), NFePHP\Common\Certificate::readPfx(base64_decode($this->config['cert']['data']), $this->config['cert']['senha']));
            $tools->model($this->movimento->fis_doc->fis_doc_tipo->modelo);
            // assinando xml
            $xmlAssinado = $tools->signNFe($xml); // O conteúdo do XML assinado fica armazenado na variável $xmlAssinado
            // enviando xml para a sefaz
            $idLote = str_pad(100, 15, '0', STR_PAD_LEFT); // Identificador do lote
            $resp = $tools->sefazEnviaLote([$xmlAssinado], $idLote);
            // convertendo o $resp que é uma string em um object para poder acessar suas propriedades
            $st = new NFePHP\NFe\Common\Standardize();
            $std = $st->toStd($resp);
            if ($std->cStat != 103) {
                //erro registrar e voltar
                echo "[$std->cStat] $std->xMotivo";
            } else {
                $recibo = $std->infRec->nRec; // Vamos usar a variável $recibo para consultar o status da nota
                $protocolo = $tools->sefazConsultaRecibo($recibo);
                $st = new NFePHP\NFe\Common\Standardize();
                $std = $st->toStd($protocolo);
                $chaveAcesso = $std->protNFe->infProt->chNFe;
                // grava em disco
                file_put_contents(sprintf('%s/xml/%s.xml', $this->path, $chaveAcesso), $xmlAssinado);
                if ($std->protNFe->infProt->cStat == 100) {
                    // protocoloca o xml e salva em arquivo
                    $xmlProtocolado = Complements::toAuthorize($xmlAssinado, $protocolo);
                    file_put_contents(sprintf('%s/xml/%s.xml', $this->path, $chaveAcesso), $xmlProtocolado);
                    // Extrai o XML de Autorização
                    $doc = new DOMDocument('1.0', 'utf-8');
                    $doc->loadXML($protocolo, LIBXML_NOBLANKS | LIBXML_NOEMPTYTAG);
                    $infProt = $doc->getElementsByTagName('infProt')->item(0);
                    // atualiza o fisdoc com os dados da autorização
                    $fisDoc = new FisDoc();
                    $fisDoc->id = $this->movimento->fis_doc->id;
                    $fisDoc->unit_id = $this->movimento->fis_doc->unit_id;
                    $fisDoc->xml_assinado = $xmlAssinado;
                    $fisDoc->xml_protocolado = $xmlProtocolado;
                    $fisDoc->data_autorizado = date("Y-m-d H:i:s", strtotime($std->protNFe->infProt->dhRecbto));
                    $fisDoc->store();
                    // insere o evento de autorização da nota
                    $fisDocEvento = new FisDocEvento();
                    $fisDocEvento->unit_id = $this->movimento->fis_doc->unit_id;
                    $fisDocEvento->fis_doc_id = $this->movimento->fis_doc->id;
                    $fisDocEvento->xml_retorno = $doc->saveXML($infProt);
                    $fisDocEvento->tipo_evento = 1; // autorização
                    $fisDocEvento->nr_protocolo = $std->protNFe->infProt->nProt;
                    $fisDocEvento->qnt_evento = 1;
                    $fisDocEvento->descricao_evento = self::C_EVENTO_AUTORIZACAO;
                    $fisDocEvento->store();
                    // imprime a danfe
                    $this->danfe($this->movimento->id);
                } else {
                    echo sprintf("%s - %s", $std->protNFe->infProt->cStat, $std->protNFe->infProt->xMotivo);
                }
            }
        } catch (\Exception $e) {
            echo $e->getMessage();
        } finally {
            TTransaction::close();
        }
    }

    private function montaXML()
    {
        $make = new Make();

        $infNFe = new stdClass();
        $infNFe->versao = self::C_NFE_VERSAO; //versão do layout
        $infNFe->Id = $this->movimento->fis_doc->chave;//se o Id de 44 digitos não for passado será gerado automaticamente
        $infNFe->pk_nItem = null; //deixe essa variavel sempre como NULL
        $make->taginfNFe($infNFe);

        $ide = new stdClass();
        $ide->cUF = $this->movimento->ger_empresa->end_ger_cidade->ger_uf->nr_uf;
        $ide->cNF = substr($this->movimento->fis_doc->chave, 35, 8);
        $ide->natOp = $this->movimento->mov_itemserv[0]->fis_cfop->nome;
        $ide->mod = $this->movimento->fis_doc->fis_doc_tipo->modelo;
        $ide->serie = $this->movimento->fis_doc->serie;
        $ide->nNF = $this->movimento->fis_doc->numero;
        $ide->dhEmi = date("Y-m-d\TH:i:sP", strtotime($this->movimento->data_mov));
        $ide->dhSaiEnt = date("Y-m-d\TH:i:sP", strtotime($this->movimento->data_mov));
        $ide->tpNF = (in_array($this->movimento->mov_operacao->mov_tipo->tipo_interno, array('NF01', 'NF02'))) ? 2 : 1;
        $ide->idDest = ($this->movimento->ger_empresa->end_ger_cidade->ger_uf->sigla_uf == $this->movimento->ger_pessoa_endereco_fiscal->end_ger_cidade->ger_uf->sigla_uf) ? 1 : 2; // 1- mesmo estado 2-interestadual
        $ide->cMunFG = $this->movimento->ger_empresa->end_ger_cidade->nr_cidade;
        $ide->tpImp = 1;
        $ide->tpEmis = $this->movimento->fis_doc->tipo_emissao;
        $ide->cDV = substr($this->movimento->fis_doc->chave, 43);
        $ide->tpAmb = $this->movimento->fis_doc->ambiente;
        $ide->finNFe = $this->movimento->mov_operacao->finalidade_doc;
        $ide->indFinal = 1;
        $ide->indPres = 1;
        $ide->procEmi = 0;
        $ide->verProc = self::C_VERSAO_APP;
        $ide->dhCont = null;
        $ide->xJust = null;
        $make->tagide($ide);

        if ($this->movimento->mov_operacao->finalidade_doc == 4) {
            $origem = new Mov($this->movimento->mov_origem->mov_id_origem);

            $refNFe = new stdClass();
            $refNFe->refNFe = $origem->fis_doc->chave;
            $make->tagrefNFe($refNFe);
        }

        if ($this->movimento->mov_operacao->mov_tipo->tipo_interno == 'NF08') {
            $origem = new Mov($this->movimento->mov_origem->mov_id_origem);

            $refNFP = new stdClass(); // @todo
            $refNFP->cUF = '';
            $refNFP->AAMM = '';
            $refNFP->CNPJ = '';
            $refNFP->CPF = '';
            $refNFP->IE = '';
            $refNFP->mod = '';
            $refNFP->serie = '';
            $refNFP->nNF = '';
            $make->tagrefNFP($refNFP);
        }

        $emit = new stdClass();
        $emit->xNome = $this->movimento->ger_empresa->razao_social;
        $emit->xFant = $this->movimento->ger_empresa->nome;
        $emit->IE = soNumeros($this->movimento->ger_empresa->doc_ie);
        $emit->IEST = '';
        $emit->IM = soNumeros($this->movimento->ger_empresa->doc_im);
        $emit->CNAE = $this->movimento->ger_empresa->doc_cnae; //opcional
        $emit->CRT = $this->movimento->ger_empresa->fis_regime; //simples nacional 1 ou 2  ou normal = 3
        $emit->CNPJ = soNumeros($this->movimento->ger_empresa->doc_cnpj);
        $make->tagemit($emit);

        $enderEmit = new stdClass();
        $enderEmit->xLgr = $this->movimento->ger_empresa->end_logradouro;
        $enderEmit->nro = $this->movimento->ger_empresa->end_logradouro_nr;
        $enderEmit->xCpl = $this->movimento->ger_empresa->end_complemento;
        $enderEmit->xBairro = $this->movimento->ger_empresa->end_bairro;
        $enderEmit->cMun = $this->movimento->ger_empresa->end_ger_cidade->nr_cidade;
        $enderEmit->xMun = $this->movimento->ger_empresa->end_ger_cidade->nome;
        $enderEmit->UF = $this->movimento->ger_empresa->end_ger_cidade->ger_uf->sigla_uf;
        $enderEmit->CEP = soNumeros($this->movimento->ger_empresa->end_cep);
        $enderEmit->cPais = $this->movimento->ger_empresa->end_ger_cidade->ger_uf->ger_pais->nr_pais; //BRASIL
        $enderEmit->xPais = $this->movimento->ger_empresa->end_ger_cidade->ger_uf->ger_pais->nome;
        $enderEmit->fone = $this->movimento->ger_empresa->fone_1; //tem que retirar ( -
        $make->tagenderEmit($enderEmit);

        $dest = new stdClass();
        $dest->xNome = $this->movimento->ger_pessoa->nome;
        $dest->CNPJ = soNumeros($this->movimento->ger_pessoa->doc_cnpj); //indicar apenas um CNPJ ou CPF ou idEstrangeiro
        $dest->CPF = soNumeros($this->movimento->ger_pessoa->doc_cpf);
        $dest->indIEDest = $this->movimento->ger_pessoa->contrib_icms;  //1 icms 2 isento
        $dest->IE = soNumeros($this->movimento->ger_pessoa->doc_ie);
        $dest->ISUF = '';
        $dest->IM = soNumeros($this->movimento->ger_pessoa->doc_im); //inscricao municipal opcional
        $dest->idEstrangeiro = '';  //para brasileiro deixa vazio
        $make->tagdest($dest);

        $enderDest = new stdClass();
        $enderDest->xLgr = $this->movimento->ger_pessoa_endereco_fiscal->end_logradouro;
        $enderDest->nro = $this->movimento->ger_pessoa_endereco_fiscal->end_logradouro_nr;
        $enderDest->xCpl = $this->movimento->ger_pessoa_endereco_fiscal->end_complemento;
        $enderDest->xBairro = $this->movimento->ger_pessoa_endereco_fiscal->end_bairro;
        $enderDest->cMun = $this->movimento->ger_pessoa_endereco_fiscal->end_ger_cidade->nr_cidade;
        $enderDest->xMun = $this->movimento->ger_pessoa_endereco_fiscal->end_ger_cidade->nome;
        $enderDest->UF = $this->movimento->ger_pessoa_endereco_fiscal->end_ger_cidade->ger_uf->sigla_uf;
        $enderDest->CEP = soNumeros($this->movimento->ger_pessoa_endereco_fiscal->end_cep);
        $enderDest->cPais = $this->movimento->ger_pessoa_endereco_fiscal->end_ger_cidade->ger_uf->ger_pais->nr_pais;
        $enderDest->xPais = $this->movimento->ger_pessoa_endereco_fiscal->end_ger_cidade->ger_uf->ger_pais->nome;
        $enderDest->fone = $this->movimento->ger_pessoa_endereco_fiscal->fone;
        $make->tagenderDest($enderDest);

        if (intval($this->movimento->ger_pessoa_endereco_id_entrega) > 0) {
            // entrega
            $entrega = new stdClass();
            $entrega->xNome = $this->movimento->ger_pessoa_endereco_entrega->ger_pessoa->nome;
            $entrega->CNPJ = soNumeros($this->movimento->ger_pessoa_endereco_entrega->ger_pessoa->doc_cnpj);
            $entrega->CPF = soNumeros($this->movimento->ger_pessoa_endereco_entrega->ger_pessoa->doc_cpf);
            $entrega->IE = soNumeros($this->movimento->ger_pessoa->doc_ie);
            $entrega->xLgr = $this->movimento->ger_pessoa_endereco_entrega->end_logradouro;
            $entrega->nro = $this->movimento->ger_pessoa_endereco_entrega->end_logradouro_nr;
            $entrega->xCpl = $this->movimento->ger_pessoa_endereco_entrega->end_complemento;
            $entrega->xBairro = $this->movimento->ger_pessoa_endereco_entrega->end_bairro;
            $entrega->cMun = $this->movimento->ger_pessoa_endereco_entrega->end_ger_cidade->nr_cidade;
            $entrega->xMun = $this->movimento->ger_pessoa_endereco_entrega->end_ger_cidade->nome;
            $entrega->UF = $this->movimento->ger_pessoa_endereco_entrega->end_ger_cidade->ger_uf->sigla_uf;
            $entrega->CEP = soNumeros($this->movimento->ger_pessoa_endereco_entrega->end_cep);
            $entrega->cPais = $this->movimento->ger_pessoa_endereco_entrega->end_ger_cidade->ger_uf->ger_pais->nr_pais;
            $entrega->xPais = $this->movimento->ger_pessoa_endereco_entrega->end_ger_cidade->ger_uf->ger_pais->nome;
            $entrega->fone = $this->movimento->ger_pessoa_endereco_entrega->fone;
            $entrega->email = $this->movimento->ger_pessoa_endereco_entrega->email;
            $make->tagentrega($entrega);
        }

        $totais = array();
        foreach ($this->movimento->mov_itemserv as $key => $item) {
            $prod = new stdClass();
            $prod->item = $key + 1; //item da NFe
            $prod->cProd = $item->ger_itemserv->referencia1;
            $prod->cEAN = self::C_SEM_GTIN; // quando nao tem CEAN c envia a palavra 'SEM GTIN'
            $prod->xProd = $item->ger_itemserv->nome;
            $prod->NCM = $item->ger_itemserv->fis_ncm->nr_ncm;
            $prod->EXTIPI = '';
            $prod->CFOP = $item->fis_cfop->nr_cfop;
            $prod->uCom = $item->ger_itemserv->ger_umedida->sigla_umedida;
            $prod->qCom = number_format($item->qnt_conv, 4, '.', ''); //PRECISA FORMATAR 4 CASAS
            $prod->vUnCom = number_format($item->valor_unit_orig, 10, '.', '');
            $prod->vProd = number_format($item->valor_bruto, 2, '.', ''); //QCOM X VUNCOM 2 CASAS DEPOIS DA VIRGULA
            $prod->cEANTrib = self::C_SEM_GTIN;
            $prod->uTrib = $item->ger_itemserv->ger_umedida->sigla_umedida;
            $prod->qTrib = number_format($item->qnt_conv, 4, '.', '');
            $prod->vUnTrib = number_format($item->valor_unit_orig, 10, '.', '');
            $prod->vFrete = number_format($item->valor_frete, 2, '.', ''); // se for 0.000 então mandar '', se for > 0.00 enviar o valor
            if (floatval($prod->vFrete) == 0) {
                $prod->vFrete = null;
            }
            $prod->vSeg = number_format($item->valor_seguro, 2, '.', ''); // se for 0.000 então mandar '', se for > 0.00 enviar o valor
            if (floatval($prod->vSeg) == 0) {
                $prod->vSeg = null;
            }
            $prod->vDesc = number_format($item->valor_desconto, 2, '.', ''); // se for 0.000 então mandar '', se for > 0.00 enviar o valor
            if (floatval($prod->vDesc) == 0) {
                $prod->vDesc = null;
            }
            $prod->vOutro = number_format($item->valor_outros, 2, '.', ''); // se for 0.000 então mandar '', se for > 0.00 enviar o valor
            if (floatval($prod->vOutro) == 0) {
                $prod->vOutro = null;
            }
            $prod->indTot = 1; //NOTA VAI SAIR ZERADA SEM INCLUIR O VALOR DE UM BRINDE.
            $make->tagprod($prod);

            $totais['vprod'] += $prod->vProd;
            $totais['vfrete'] += $prod->vFrete;
            $totais['vseg'] += $prod->vSeg;
            $totais['vdesc'] += $prod->vDesc;
            $totais['voutro'] += $prod->vOutro;

            if (FisTributacao::retornaImposto($item->fis_tributacao, [self::C_TRIBUTO_ST])) {
                $cest = new stdClass();  //coloca esta parte somente se o produto tiver CEST
                $cest->item = $key + 1; //item da NFe
                $cest->CEST = $item->ger_itemserv->fis_cest->nr_cest;
                $cest->indEscala = 'S'; //incluido no layout 4.00 Somente para industria
                $cest->CNPJFab = ''; //incluido no layout 4.00 somente para industria
                $make->tagCEST($cest);
            }

            $imposto = new stdClass();
            $imposto->item = $key + 1; //item da NFe
            $imposto->vTotTrib = $prod->vProd * ($item->ger_itemserv->fis_ncm->fis_ibpt->perc_municipal / 100);
            if (in_array($item->ger_itemserv->origem_fiscal, [0, 3, 4, 5, 8])) {
                $imposto->vTotTrib += $prod->vProd * ($item->ger_itemserv->fis_ncm->fis_ibpt->perc_nacional / 100);
            } else {
                $imposto->vTotTrib += $prod->vProd * ($item->ger_itemserv->fis_ncm->fis_ibpt->perc_importado / 100);
            }
            $imposto->vTotTrib = number_format($imposto->vTotTrib, 2, '.', '');
            $make->tagimposto($imposto);

            $totais['vtottrib'] += $imposto->vTotTrib;

            $impostoICMS = FisTributacao::retornaImposto($item->fis_tributacao, [self::C_TRIBUTO_ICMS, self::C_TRIBUTO_ST]);

            $icms = new stdClass();
            $icms->item = $key + 1; //item da NFe
            $icms->orig = $item->ger_itemserv->origem_fiscal;
            if ($emit->CRT == 3) {
                $icms->CST = $impostoICMS->cst;
                $icms->modBC = $impostoICMS->modalidade_base_calc;
                $icms->pRedBC = number_format($impostoICMS->perc_reducao_base_calc, 13, 2);
                $icms->vBC = number_format($impostoICMS->valor_base_calc, 13, 2);
                $icms->pICMS = number_format($impostoICMS->perc_aliquota, 13, 2);
                $icms->vICMS = number_format($impostoICMS->valor_imposto, 13, 2);
                $icms->vICMSDeson = number_format($impostoICMS->valor_icms_desonerado, 13, 2);
                $icms->motDesICMS = $impostoICMS->motivo_icms_desonerado;
                $icms->modBCST = $impostoICMS->mod_base_calc_st;
                $icms->pMVAST = number_format($impostoICMS->margem_agregada_st, 13, 2);
                $icms->pRedBCST = number_format($impostoICMS->perc_red_base_calc, 13, 2);
                $icms->vBCST = number_format($impostoICMS->valor_base_calc_st, 13, 2);
                $icms->pICMSST = number_format($impostoICMS->perc_aliquota_st, 13, 2);
                $icms->vICMSST = number_format($impostoICMS->valor_imposto_st, 13, 2);
                $icms->pDif = '33.33';
                $icms->vICMSDif = number_format($impostoICMS->valor_imposto_diferido, 13, 2);
                $icms->vICMSOp = number_format($impostoICMS->valor_imposto_operacao, 13, 2);
                $icms->pFCP = number_format($impostoICMS->perc_fundo_comb_pob, 13, 2);
                $icms->vFCP = number_format($impostoICMS->valor_fundo_comb_pob, 13, 2);
                $icms->vBCFCP = number_format($impostoICMS->valor_base_calc_fundo_comb_pob, 13, 2);
                $icms->vBCFCPST = number_format($impostoICMS->valor_base_calc_st_fundo_comb_pob, 13, 2);
                $icms->pFCPST = number_format($impostoICMS->perc_st_fundo_comb_pob, 13, 2);
                $icms->vFCPST = number_format($impostoICMS->valor_st_fundo_comb_pob, 13, 2);
                $icms->vBCSTRet = number_format($impostoICMS->valor_base_calc_st_ret, 13, 2);
                $icms->pST = number_format($impostoICMS->perc_aliquota_st, 13, 2);
                $icms->vICMSSTRet = number_format($impostoICMS->valor_icms_st_ret, 13, 2);
                $icms->vBCFCPSTRet = number_format($impostoICMS->valor_base_calc_fundo_comb_pob_st_ret, 13, 2);
                $icms->pFCPSTRet = number_format($impostoICMS->perc_aliquota_fundo_comb_pob_st_ret, 13, 2);
                $icms->vFCPSTRet = number_format($impostoICMS->valor_fundo_comb_pob_st_ret, 13, 2);
                $icms->pRedBCEfet = number_format($impostoICMS->perc_aliquota_red_base_calc_efetiva, 13, 2);
                $icms->vBCEfet = number_format($impostoICMS->valor_base_calc_efetiva, 13, 2);
                $icms->pICMSEfet = number_format($impostoICMS->perc_aliquota_icms_efetiva, 13, 2);
                $icms->vICMSEfet = number_format($impostoICMS->valor_icms_efetiva, 13, 2);
                $icms->vICMSSubstituto = number_format($impostoICMS->valor_icms_substituto, 13, 2);
                $make->tagICMS($icms);
            } else {
                $icms->CSOSN = $impostoICMS->cst;
                $icms->pCredSN = number_format($impostoICMS->perc_aliquota_credito, 13, 2);
                $icms->vCredICMSSN = number_format($impostoICMS->valor_credito_icms, 13, 2);
                $icms->modBCST = $impostoICMS->mod_base_calc_st;
                $icms->pMVAST = number_format($impostoICMS->margem_agregada_st, 13, 2);
                $icms->pRedBCST = number_format($impostoICMS->perc_red_base_calc, 13, 2);
                $icms->vBCST = number_format($impostoICMS->valor_base_calc_st, 13, 2);
                $icms->pICMSST = number_format($impostoICMS->perc_aliquota_st, 13, 2);
                $icms->vICMSST = number_format($impostoICMS->valor_imposto_st, 13, 2);
                $icms->vBCFCPST = number_format($impostoICMS->valor_base_calc_st_fundo_comb_pob, 13, 2);
                $icms->pFCPST = number_format($impostoICMS->perc_st_fundo_comb_pob, 13, 2);
                $icms->vFCPST = number_format($impostoICMS->valor_st_fundo_comb_pob, 13, 2);
                $icms->vBCSTRet = number_format($impostoICMS->valor_base_calc_st_ret, 13, 2);
                $icms->pST = number_format($impostoICMS->perc_aliquota_st, 13, 2);
                $icms->vICMSSTRet = number_format($impostoICMS->valor_icms_st_ret, 13, 2);
                $icms->vBCFCPSTRet = number_format($impostoICMS->valor_base_calc_fundo_comb_pob_st_ret, 13, 2);
                $icms->pFCPSTRet = number_format($impostoICMS->perc_aliquota_fundo_comb_pob_st_ret, 13, 2);
                $icms->vFCPSTRet = number_format($impostoICMS->valor_fundo_comb_pob_st_ret, 13, 2);
                $icms->modBC = $impostoICMS->modalidade_base_calc;
                $icms->vBC = number_format($impostoICMS->valor_base_calc, 13, 2);
                $icms->pRedBC = number_format($impostoICMS->perc_reducao_base_calc, 13, 2);
                $icms->pICMS = number_format($impostoICMS->perc_aliquota, 13, 2);
                $icms->vICMS = number_format($impostoICMS->valor_imposto, 13, 2);
                $icms->pRedBCEfet = number_format($impostoICMS->perc_aliquota_red_base_calc_efetiva, 13, 2);
                $icms->vBCEfet = number_format($impostoICMS->valor_base_calc_efetiva, 13, 2);
                $icms->pICMSEfet = number_format($impostoICMS->perc_aliquota_icms_efetiva, 13, 2);
                $icms->vICMSEfet = number_format($impostoICMS->valor_icms_efetiva, 13, 2);
                $icms->vICMSSubstituto = number_format($impostoICMS->valor_icms_substituto, 13, 2);
                $make->tagICMSSN($icms);
            }
            $totais['vbcicms'] += $icms->vBC;
            $totais['vicms'] += $icms->vICMS;
            $totais['vbcicmsst'] += $icms->vBCST;
            $totais['vicmsst'] += $icms->vICMSST;

            $impostoPIS = FisTributacao::retornaImposto($item->fis_tributacao, [self::C_TRIBUTO_PIS]);
            $pis = new stdClass();
            $pis->item = $key + 1; //item da NFe
            $pis->CST = '49';
            if (in_array($this->movimento->mov_operacao->mov_tipo->tipo_interno, array('NF01', 'NF02'))) {
                $pis->CST = '99';
            }
            if ($impostoPIS !== false) {
                $pis->CST = $impostoPIS->cst;
            }
            $pis->vBC = number_format($impostoPIS->valor_base_calc, 2, '.', '');
            $pis->pPIS = number_format($impostoPIS->perc_aliquota, 4, '.', '');
            $pis->vPIS = number_format($impostoPIS->valor_imposto, 2, '.', '');
            $make->tagPIS($pis);
            $totais['vpis'] += $pis->vPIS;

            $impostoCOFINS = FisTributacao::retornaImposto($item->fis_tributacao, [self::C_TRIBUTO_COFINS]);
            $cofins = new stdClass();
            $cofins->item = $key + 1; //item da NFe
            $cofins->CST = '49';
            if (in_array($this->movimento->mov_operacao->mov_tipo->tipo_interno, array('NF01', 'NF02'))) {
                $cofins->CST = '99';
            }
            if ($impostoCOFINS !== false) {
                $cofins->CST = $impostoCOFINS->cst;
            }
            $cofins->vBC = number_format($impostoCOFINS->valor_base_calc, 2, '.', '');
            $cofins->pCOFINS = number_format($impostoCOFINS->perc_aliquota, 4, '.', '');
            $cofins->vCOFINS = number_format($impostoCOFINS->valor_imposto, 2, '.', '');
            $make->tagCOFINS($cofins);
            $totais['vconfins'] += $cofins->vCOFINS;
        }

        $icmstot = new stdClass();
        $icmstot->vBC = number_format($totais['vbcicms'], 2, '.', '');
        $icmstot->vICMS = number_format($totais['vicms'], 2, '.', '');
        $icmstot->vICMSDeson = '0.00';
        $icmstot->vFCP = '0.00';
        $icmstot->vBCST = number_format($totais['vbcicmsst'], 2, '.', '');
        $icmstot->vST = number_format($totais['vicmsst'], 2, '.', '');
        $icmstot->vFCPST = '0.00';
        $icmstot->vFCPSTRet = '0.00';
        $icmstot->vProd = number_format($totais['vprod'], 2, '.', ''); // SOMA DO VALOR DOS PRODUTOS
        $icmstot->vFrete = number_format($totais['vfrete'], 2, '.', ''); //SOMA DOS FRETES
        $icmstot->vSeg = number_format($totais['vseg'], 2, '.', ''); //SEGURO
        $icmstot->vDesc = number_format($totais['vdesc'], 2, '.', ''); //DESCONTO
        $icmstot->vII = '0.00';
        $icmstot->vIPI = '0.00';
        $icmstot->vIPIDevol = '0.00';
        $icmstot->vPIS = number_format($totais['vpis'], 2, '.', '');
        $icmstot->vCOFINS = number_format($totais['vconfins'], 2, '.', '');
        $icmstot->vOutro = number_format($totais['voutro'], 2, '.', ''); //ACRESCIMOS
        $icmstot->vNF = number_format($icmstot->vProd + $icmstot->vST + $icmstot->vFrete + $icmstot->vSeg + $icmstot->vOutro - $icmstot->vDesc, 2, '.', '');  // LIQUIDO => VPROD + VFRETE + VSEG - VDESC + VOUTRO
        $icmstot->vTotTrib = number_format($totais['vtottrib'], 2, '.', '');
        $make->tagICMSTot($icmstot);

        //transporte para destinatario
        $transp = new stdClass();
        //0=Por conta do emitente; 1=Por conta do destinatário/remetente; 2=Por conta de terceiros; 9=Sem frete. (V2.0)
        $transp->modFrete = $this->movimento->tipo_frete;
        $make->tagtransp($transp);


        $frete = $this->movimento->mov_frete;
        if ($frete != null) {
            //OPCIONAL DADOS DA TRANSPORTADORA
            $transporta = new stdClass();
            $transporta->xNome = $frete->ger_pessoa_endereco_transp->ger_pessoa->nome;
            $transporta->IE = soNumeros($frete->ger_pessoa_endereco_transp->ger_pessoa->doc_ie);
            $transporta->xEnder = $frete->ger_pessoa_endereco_transp->end_logradouro;
            $transporta->xMun = $frete->ger_pessoa_endereco_transp->end_ger_cidade->nome;
            $transporta->UF = $frete->ger_pessoa_endereco_transp->end_ger_cidade->ger_uf->sigla_uf;
            $transporta->CNPJ = soNumeros($frete->ger_pessoa_endereco_transp->ger_pessoa->doc_cnpj);//só pode haver um ou CNPJ ou CPF, se um deles é especificado o outro deverá ser null
            $transporta->CPF = soNumeros($frete->ger_pessoa_endereco_transp->ger_pessoa->doc_cpf);
            $make->tagtransporta($transporta);

            $veicTransp = new stdClass();
            $veicTransp->placa = $frete->ope_centro2_equip->placa;
            $veicTransp->UF = $frete->ope_centro2_equip->ger_cidade->ger_uf->sigla_uf;
            $veicTransp->RNTC = soNumeros($frete->ope_centro2_equip->nr_registro_estadual);
            $make->tagveicTransp($veicTransp);

            // reboques
            $reboques = $this->movimento->mov_reboque;
            foreach ($reboques as $reboque) {
                $rebo = new stdClass();
                $rebo->placa = $reboque->ope_centro2_equip->placa;
                $rebo->UF = $reboque->ope_centro2_equip->ger_cidade->ger_uf->sigla_uf;
                $rebo->RNTC = soNumeros($reboque->ope_centro2_equip->nr_registro_estadual);
                $make->tagreboque($rebo);
            }
        }

        $medidas = $this->movimento->mov_medida;
        foreach ($medidas as $key => $medida) {
            $vol = new stdClass();
            $vol->item = $key + 1;
            $vol->qVol = $medida->qnt_medida;
            $vol->esp = $medida->ger_umedida->nome;
            $vol->marca = $medida->marca;
            $vol->nVol = $medida->nr_volume;
            $vol->pesoL = number_format($medida->peso_liquido, 13, 2);
            $vol->pesoB = number_format($medida->peso_bruto, 13, 2);
            $make->tagvol($vol);
        }

        $pag = new stdClass();
        $pag->vTroco = null; //incluso no layout 4.00, obrigatório informar para NFCe (65)
        $make->tagpag($pag);

        if ($this->movimento->mov_operacao->finalidade_doc == 4) {

            $detPag = new stdClass();
            $detPag->tPag = '90'; //01=Dinheiro 02=Cheque 03=Cartão de Crédito 04=Cartão de Débito 05=Crédito Loja 10=Vale Alimentação 11=Vale Refeição 12=Vale Presente 13=Vale Combustível 14=Fatura 99=Outros
            $detPag->vPag = '0.00'; //Obs: deve ser informado o valor pago pelo cliente
            $make->tagdetPag($detPag);
        } else {

            $detPag = new stdClass();
            $detPag->tPag = $this->movimento->fin_pagrec_origem->fin_pagrec->fin_doc_tipo->nr_nfe; //01=Dinheiro 02=Cheque 03=Cartão de Crédito 04=Cartão de Débito 05=Crédito Loja 10=Vale Alimentação 11=Vale Refeição 12=Vale Presente 13=Vale Combustível 14=Fatura 99=Outros
            $detPag->vPag = $this->movimento->fin_pagrec_origem->fin_pagrec->valor_pagrec; //Obs: deve ser informado o valor pago pelo cliente
            $detPag->tpIntegra = null; //incluso na NT 2015/002
            $detPag->indPag = $this->movimento->fin_pagrec_origem->fin_pagrec->fin_cond_pagrec->tipo_prazo; //0= Pagamento à Vista 1= Pagamento à Prazo
            $make->tagdetPag($detPag);

            if ($detPag->indPag == 1) {
                $fat = new stdClass();
                $fat->nFat = $this->movimento->fin_pagrec_origem->fin_pagrec->numero_doc_pagrec;
                $fat->vOrig = $this->movimento->fin_pagrec_origem->fin_pagrec->valor_pagrec;
                $fat->vDesc = null;
                $fat->vLiq = $this->movimento->fin_pagrec_origem->fin_pagrec->valor_pagrec;
                $make->tagfat($fat);

                $duplicatas = $this->movimento->fin_pagrec_origem->fin_pagrec->fin_pagrec_parc;
                foreach ($duplicatas as $duplicata) {
                    $dup = new stdClass();
                    $dup->nDup = $duplicata->numero_parc;
                    $dup->dVenc = $duplicata->data_vencimento;
                    $dup->vDup = $duplicata->valor_pagrec;
                    $make->tagdup($dup);
                }
            }
        }

        $infAdic = new stdClass();
        $infAdic->infAdFisco = $this->movimento->observacao_fiscal;
        $infAdic->infCpl = 'informacoes complementares'; //todo ver depois
        $make->taginfAdic($infAdic);

        if ($this->movimento->mov_operacao->mov_tipo->tipo_interno == 'NF07') {
            // exportação
            $exporta = new stdClass();
            $dup->UFSaidaPais = $duplicata->valor_pagrec;
            $dup->xLocExporta = $duplicata->valor_pagrec;
            $dup->xLocDespacho = $duplicata->valor_pagrec;
            $make->tagexporta($exporta);
        }

        //todo o eduardo vai ver com mais calma
        $infRespTec = new stdClass();
        $infRespTec->CNPJ = soNumeros('00994539000103');
        $infRespTec->xContato = 'Mardel Cardoso';
        $infRespTec->email = 'mardel@arenaplan.com.br';
        $infRespTec->fone = soNumeros('11987918980');
        $make->taginfRespTec($infRespTec);

        $make->montaNFe();

        return $make->getXML();
    }

    public function cancela()
    {
        try {
            TTransaction::open(TSession::getValue('pConn'));

            $this->buscaDados($_REQUEST['id']);

            $justificativa = 'teste de cancelamento';

            $tools = new NFePHP\NFe\Tools(json_encode($this->config), NFePHP\Common\Certificate::readPfx(base64_decode($this->config['cert']['data']), $this->config['cert']['senha']));
            $tools->model($this->movimento->fis_doc->fis_doc_tipo->modelo);

            $docEvento = $this->movimento->fis_doc->getEvento(1);

            // cancela a nfe
            $resp = $tools->sefazCancela($this->movimento->fis_doc->chave, $justificativa, $docEvento->nr_protocolo);
            $st = new NFePHP\NFe\Common\Standardize();
            $std = $st->toStd($resp);
            if ($std->retEvento->infEvento->cStat == 135) {
                // protocoloca o xml e salva em arquivo
                // Extrai o XML de Cancelamento
                $doc = new DOMDocument('1.0', 'utf-8');
                $doc->loadXML($resp, LIBXML_NOBLANKS | LIBXML_NOEMPTYTAG);
                $retEvento = $doc->getElementsByTagName('retEvento')->item(0);
                $infEvento = $retEvento->getElementsByTagName('infEvento')->item(0);
                // atualiza o fisdoc com os dados da autorização
                $fisDoc = new FisDoc();
                $fisDoc->id = $this->movimento->fis_doc->id;
                $fisDoc->unit_id = $this->movimento->fis_doc->unit_id;
                $fisDoc->data_cancelado = date("Y-m-d H:i:s", strtotime($std->retEvento->infEvento->dhRegEvento));
                $fisDoc->store();
                // insere o evento de cancelamento da nota
                $fisDocEvento = new FisDocEvento();
                $fisDocEvento->unit_id = $this->movimento->fis_doc->unit_id;
                $fisDocEvento->fis_doc_id = $this->movimento->fis_doc->id;
                $fisDocEvento->xml_retorno = $doc->saveXML($infEvento);
                $fisDocEvento->tipo_evento = 2; // cancelamento
                $fisDocEvento->nr_protocolo = $std->retEvento->infEvento->nProt;
                $fisDocEvento->qnt_evento = 1;
                $fisDocEvento->descricao_evento = self::C_EVENTO_CANCELAMENTO;
                $fisDocEvento->store();
            }
            echo sprintf("%s - %s", $std->retEvento->infEvento->cStat, $std->retEvento->infEvento->xMotivo);
        } catch (Exception $e) {
            echo $e->getMessage();
        } finally {
            TTransaction::close();
        }
    }

    public function inutiliza($serie, $inicio, $final, $justificativa)
    {
        try {
            TTransaction::open(TSession::getValue('pConn'));

            $empresa = new GerEmpresa(1);
            $docTipo = new FisDocTipo(1);

            $this->config = array(
                "atualizacao" => date('Y-m-d h:i:s'),
                "tpAmb" => $docTipo->ambiente,
                "razaosocial" => $empresa->razao_social,
                "cnpj" => $empresa->doc_cnpj, // PRECISA SER VÁLIDO
                "ie" => $empresa->doc_ie, // PRECISA SER VÁLIDO
                "siglaUF" => $empresa->end_ger_cidade->ger_uf->sigla_uf,
                "schemes" => self::C_NFE_SCHEMES,
                "versao" => self::C_NFE_VERSAO,
                "tokenIBPT" => "",
                "CSC" => "",
                "CSCid" => "",
                "aProxyConf" => array(
                    "proxyIp" => "",
                    "proxyPort" => "",
                    "proxyUser" => "",
                    "proxyPass" => ""
                ),
                "cert" => array(
                    "data" => $empresa->fis_certificado->certificado,
                    "senha" => $empresa->fis_certificado->senha
                )
            );

            $tools = new NFePHP\NFe\Tools(json_encode($this->config), NFePHP\Common\Certificate::readPfx(base64_decode($this->config['cert']['data']), $this->config['cert']['senha']));
            $tools->model($docTipo->modelo);
            // inutiliza a nfe
            $resp = $tools->sefazInutiliza($serie, $inicio, $final, $justificativa);
            $st = new NFePHP\NFe\Common\Standardize();
            $std = $st->toStd($resp);
            if ($std->infInut->cStat == 102) {
                // Extrai o XML de Inutilização
                $doc = new DOMDocument('1.0', 'utf-8');
                $doc->loadXML($resp, LIBXML_NOBLANKS | LIBXML_NOEMPTYTAG);
                $infInut = $doc->getElementsByTagName('infInut')->item(0);
                file_put_contents(sprintf('%s/xml/serie-%s-inicio-%s-final-%s-inut.xml', $this->path, $serie, $inicio, $final), $resp);
                // cria o fis_doc
                $fisDoc = new FisDoc();
                $fisDoc->unit_id = $empresa->unit_id;
                $fisDoc->mov_id = null;
                $fisDoc->data_emissao = date("Y-m-d");
                $fisDoc->numero = $inicio;
                $fisDoc->serie = $serie;
                $fisDoc->numero_ini = $inicio;
                $fisDoc->numero_fin = $final;
                $fisDoc->fis_doc_tipo_id = $docTipo->id;
                $fisDoc->ambiente = $docTipo->ambiente;
                $fisDoc->tipo_emissao = 1;
                $fisDoc->store();
                // insere o evento de inutilização da nota
                $fisDocEvento = new FisDocEvento();
                $fisDocEvento->unit_id = $empresa->unit_id;
                $fisDocEvento->fis_doc_id = $fisDoc->id;
                $fisDocEvento->xml_retorno = $doc->saveXML($infInut);
                $fisDocEvento->tipo_evento = 3; // inutilização
                $fisDocEvento->nr_protocolo = $std->infInut->nProt;
                $fisDocEvento->qnt_evento = 1;
                $fisDocEvento->descricao_evento = self::C_EVENTO_INUTILIZACAO;
                $fisDocEvento->store();
            }
            echo sprintf("%s - %s", $std->infInut->cStat, $std->infInut->xMotivo);
        } catch (Exception $e) {
            echo $e->getMessage();
        } finally {
            TTransaction::close();
        }
    }

    // apenas para modelo 55
    public function cce()
    {
        try {
            TTransaction::open(TSession::getValue('pConn'));

            $this->buscaDados($_REQUEST['id']);

            $justificativa = 'correcao do numero do endereco para 2';

            $tools = new NFePHP\NFe\Tools(json_encode($this->config), NFePHP\Common\Certificate::readPfx(base64_decode($this->config['cert']['data']), $this->config['cert']['senha']));
            $tools->model($this->movimento->fis_doc->fis_doc_tipo->modelo);

            $docEvento = $this->movimento->fis_doc->getEvento(4);
            $sequenciaEvento = intval($docEvento->qnt_evento) + 1;

            // cartao de correcao da nfe
            $resp = $tools->sefazCCe($this->movimento->fis_doc->chave, $justificativa, $sequenciaEvento);
            $st = new NFePHP\NFe\Common\Standardize();
            $std = $st->toStd($resp);
            if ($std->retEvento->infEvento->cStat == 135) {
                // Extrai o XML da Carta de Correção
                $doc = new DOMDocument('1.0', 'utf-8');
                $doc->loadXML($resp, LIBXML_NOBLANKS | LIBXML_NOEMPTYTAG);
                $retEvento = $doc->getElementsByTagName('retEvento');
                foreach ($retEvento as $key => $evento) {
                    $infEvento = $evento->getElementsByTagName('infEvento')->item(0);
                    if (in_array(intval($infEvento->getElementsByTagName('cStat')->item(0)->nodeValue), array(
                        135
                    ))) {
                        break;
                    }
                }
                file_put_contents(sprintf('%s/xml/%s-cce.xml', $this->path, $this->movimento->fis_doc->chave), $resp);
                // insere o evento de cancelamento da nota
                $fisDocEvento = new FisDocEvento();
                $fisDocEvento->unit_id = $this->movimento->fis_doc->unit_id;
                $fisDocEvento->fis_doc_id = $this->movimento->fis_doc->id;
                $fisDocEvento->xml_retorno = $doc->saveXML($infEvento);
                $fisDocEvento->tipo_evento = 4; // carta de correção
                $fisDocEvento->nr_protocolo = $std->retEvento->infEvento->nProt;
                $fisDocEvento->qnt_evento = $sequenciaEvento;
                $fisDocEvento->descricao_evento = $justificativa;
                $fisDocEvento->store();
            }
            echo sprintf("%s - %s", $std->retEvento->infEvento->cStat, $std->retEvento->infEvento->xMotivo);
        } catch (Exception $e) {
            echo $e->getMessage();
        } finally {
            TTransaction::close();
        }
    }

}

?>