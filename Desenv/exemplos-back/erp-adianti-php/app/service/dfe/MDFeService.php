<?php

use NFePHP\DA\MDFe\Damdfe;

class MDFeService extends BaseService
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
            "schemes" => self::C_MDFE_SCHEMES,
            "versao" => self::C_MDFE_VERSAO,
            "tokenIBPT" => "",
            "pathXmlUrlFileMDFe" => "mdfe_ws1.xml",
            "certPfxName" => sprintf('%s.pfx', $this->movimento->ger_empresa->doc_cnpj),
            "certPassword" => $this->movimento->ger_empresa->fis_certificado->senha
        );
        $this->path = sprintf('./files/%s', $this->config['cnpj']);
        @mkdir(sprintf('%s/pdf', $this->path), 0777, true);
        @mkdir(sprintf('%s/xml', $this->path), 0777, true);
        $this->config['pathCertsFiles'] = sprintf("%s/certs", $this->path);
        @mkdir($this->config['pathCertsFiles'], 0777, true);
        file_put_contents(sprintf("%s/%s", $this->config['pathCertsFiles'], $this->config['certPfxName']), $this->movimento->ger_empresa->fis_certificado->certificado);
    }

    public function geraDamdfe()
    {
        try {
            TTransaction::open(TSession::getValue('pConn'));
            $this->damdfe($_REQUEST['id']);
        } catch (\Exception $e) {
            echo $e->getMessage();
        } finally {
            TTransaction::close();
        }
    }

    private function damdfe($movimento)
    {
        $this->buscaDados($movimento);
        $damdfe = new Damdfe($this->movimento->fis_doc->xml_protocolado, 'P', 'A4', '', 'S');
        $pdf = $damdfe->printMDFe('', 'S');
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
            $tools = new NFePHP\MDFe\Tools(json_encode($this->config));
            // assinando xml
            $xmlAssinado = $tools->assina($xml); // O conteúdo do XML assinado fica armazenado na variável $xmlAssinado
            // enviando xml para a sefaz
            $idLote = str_pad(100, 15, '0', STR_PAD_LEFT); // Identificador do lote
            $retornoLote = array();
            $tools->sefazEnviaLote($xmlAssinado, '', $idLote, $retornoLote);
            // convertendo o $resp que é uma string em um object para poder acessar suas propriedades
            if ($retornoLote['cStat'] != 103) {
                //erro registrar e voltar
                echo $retornoLote['cStat'] . " " . $retornoLote['xMotivo'];
            } else {
                $recibo = $retornoLote['nRec']; // Vamos usar a variável $recibo para consultar o status da mdfe
                sleep(3);
                $retorno = array();
                $protocolo = $tools->sefazConsultaRecibo($recibo, '', $retorno);
                $chaveAcesso = $retorno['aProt']['chMDFe'];
                // grava em disco
                file_put_contents(sprintf('%s/xml/%s.xml', $this->path, $chaveAcesso), $xmlAssinado);
                if ($retorno['aProt']['cStat'] == 100) {
                    // protocoloca o xml e salva em arquivo
                    $xmlProtocolado = $tools->addProtocolo($xmlAssinado, $protocolo);
                    file_put_contents(sprintf('%s/xml/%s.xml', $this->path, $chaveAcesso), $xmlProtocolado);
                    // Extrai o XML de Autorização
                    $doc = new \DOMDocument('1.0', 'utf-8');
                    $doc->loadXML($protocolo, LIBXML_NOBLANKS | LIBXML_NOEMPTYTAG);
                    $infProt = $doc->getElementsByTagName('infProt')->item(0);
                    // atualiza o fisdoc com os dados da autorização
                    $fisDoc = new FisDoc();
                    $fisDoc->id = $this->movimento->fis_doc->id;
                    $fisDoc->unit_id = $this->movimento->fis_doc->unit_id;
                    $fisDoc->xml_assinado = $xmlAssinado;
                    $fisDoc->xml_protocolado = $xmlProtocolado;
                    $fisDoc->data_autorizado = date("Y-m-d H:i:s", strtotime($retorno['aProt']['dhRecbto']));
                    $fisDoc->store();
                    // insere o evento de autorização da mdfe
                    $fisDocEvento = new FisDocEvento();
                    $fisDocEvento->unit_id = $this->movimento->fis_doc->unit_id;
                    $fisDocEvento->fis_doc_id = $this->movimento->fis_doc->id;
                    $fisDocEvento->xml_retorno = $doc->saveXML($infProt);
                    $fisDocEvento->tipo_evento = 1; // autorização
                    $fisDocEvento->nr_protocolo = $retorno['aProt']['nProt'];
                    $fisDocEvento->qnt_evento = 1;
                    $fisDocEvento->descricao_evento = self::C_EVENTO_AUTORIZACAO;
                    $fisDocEvento->store();
                    // imprime a damdfe
                    $this->damdfe($this->movimento->id);
                } else {
                    echo sprintf("%s - %s", $retorno['aProt']['cStat'], $retorno['aProt']['xMotivo']);
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
        $make = new \NFePHP\MDFe\MakeMDFe(false);

        $make->taginfMDFe(
            $this->movimento->fis_doc->chave,
            self::C_MDFE_VERSAO
        );

        $make->tagide(
            $cUF = $this->movimento->ger_empresa->end_ger_cidade->ger_uf->nr_uf,
            $tpAmb = $this->movimento->fis_doc->ambiente,
            $tpEmit = $this->movimento->tipo_emissao_carga,
            $tpTransp = $this->movimento->tipo_transportador_carga,
            $mod = $this->movimento->fis_doc->fis_doc_tipo->modelo,
            $serie = $this->movimento->fis_doc->serie,
            $nMDF = $this->movimento->fis_doc->numero,
            $cMDF = substr($this->movimento->fis_doc->chave, 35, 8),
            $cDV = substr($this->movimento->fis_doc->chave, 43),
            $modal = $this->movimento->tipo_modal_carga,
            $dhEmi = date("Y-m-d\TH:i:sP", strtotime($this->movimento->data_mov)),
            $tpEmis = $this->movimento->fis_doc->tipo_emissao,
            $procEmi = '0',
            $verProc = self::C_VERSAO_APP,
            $ufIni = $this->movimento->ger_cidade_carreg->ger_uf->sigla_uf,
            $ufFim = $this->movimento->ger_cidade_descarreg->ger_uf->sigla_uf
        );

        $make->tagInfMunCarrega(
            $cMunCarrega = $this->movimento->ger_cidade_carreg->nr_cidade,
            $xMunCarrega = $this->movimento->ger_cidade_carreg->nome
        );

        $percursos = $this->movimento->mov_percurso;
        foreach ($percursos as $percurso) {
            $infPercurso = new stdClass();
            $infPercurso->UFPer = $percurso->ger_cidade->ger_uf->sigla_uf;
            $make->taginfPercurso($infPercurso);
        }

        $emit = new stdClass();
        $emit->CNPJ = soNumeros($this->movimento->ger_empresa->doc_cnpj);
        $emit->IE = soNumeros($this->movimento->ger_empresa->doc_ie);
        $emit->xNome = $this->movimento->ger_empresa->razao_social;
        $emit->xFant = $this->movimento->ger_empresa->nome;
        $make->tagemit(
            $cnpj = $emit->CNPJ,
            $ie = $emit->IE,
            $xNome = $emit->xNome,
            $xFant = $emit->xFant
        );

        $enderEmit = new stdClass();
        $enderEmit->xLgr = $this->movimento->ger_empresa->end_logradouro;
        $enderEmit->nro = $this->movimento->ger_empresa->end_logradouro_nr;
        $enderEmit->xCpl = $this->movimento->ger_empresa->end_complemento;
        $enderEmit->xBairro = $this->movimento->ger_empresa->end_bairro;
        $enderEmit->cMun = $this->movimento->ger_empresa->end_ger_cidade->nr_cidade;
        $enderEmit->xMun = $this->movimento->ger_empresa->end_ger_cidade->nome;
        $enderEmit->CEP = soNumeros($this->movimento->ger_empresa->end_cep);
        $enderEmit->UF = $this->movimento->ger_empresa->end_ger_cidade->ger_uf->sigla_uf;
        $enderEmit->fone = soNumeros($this->movimento->ger_empresa->fone_1);
        $make->tagenderEmit(
            $xLgr = $enderEmit->xLgr,
            $nro = $enderEmit->nro,
            $xCpl = $enderEmit->xCpl,
            $xBairro = $enderEmit->xBairro,
            $cMun = $enderEmit->cMun,
            $xMun = $enderEmit->xMun,
            $cep = $enderEmit->CEP,
            $siglaUF = $enderEmit->UF,
            $fone = $enderEmit->fone
        );

        $make->taginfModal(
            $versaoModal = self::C_MDFE_VERSAO_MODAL
        );

        $make->tagANTT(
            $rntrc = soNumeros($this->movimento->ger_empresa->doc_rntrc)
        );

        $contratantes = $this->movimento->mov_tomador;
        foreach ($contratantes as $contratante) {
            $make->tagContratante(
                $CPF = soNumeros($contratante->ger_pessoa_responsavel->doc_cpf),
                $CNPJ = soNumeros($contratante->ger_pessoa_responsavel->doc_cnpj)
            );
        }

        $frete = $this->movimento->mov_frete;
        if ($frete != null) {
            $veic = new stdClass();
            $veic->cInt = $frete->ope_centro2_equip->id;
            $veic->placa = $frete->ope_centro2_equip->placa;
            $veic->RENAVAM = $frete->ope_centro2_equip->renavam;
            $veic->tara = floatval($frete->ope_centro2_equip->tara);
            $veic->capKG = floatval($frete->ope_centro2_equip->capacidade_kg);
            $veic->capM3 = floatval($frete->ope_centro2_equip->capacidade_m3);
            $veic->tpRod = $frete->ope_centro2_equip->tipo_rodado;
            $veic->tpCar = $frete->ope_centro2_equip->tipo_carroceria;
            $veic->UF = $frete->ope_centro2_equip->ger_cidade->ger_uf->sigla_uf;

            $prop = new stdClass();
            $prop->CNPJ = soNumeros($frete->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->doc_cnpj);
            $prop->CPF = soNumeros($frete->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->doc_cpf);
            $prop->RNTRC = soNumeros($frete->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->nr_rntrc);
            $prop->xNome = $frete->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->nome;
            $prop->IE = soNumeros($frete->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->doc_ie);
            $prop->UFprop = $frete->ope_centro2_equip->ger_pessoa_endereco->ger_cidade->ger_uf->sigla_uf;
            $prop->tpProp = $frete->ope_centro2_equip->tipo_transp_auto_carga;

            $make->tagVeicTracao(
                $cInt = $veic->cInt,
                $placa = $veic->placa,
                $renavam = $veic->RENAVAM,
                $tara = $veic->tara,
                $capKG = $veic->capKG,
                $capM3 = $veic->capM3,
                $CPF = $prop->CPF,
                $CNPJ = $prop->CNPJ,
                $propRNTRC = $prop->RNTRC,
                $xNome = $prop->xNome,
                $IE = $prop->IE,
                $UFprop = $prop->UFprop,
                $tpProp = $prop->tpProp,
                $tpRod = $veic->tpRod,
                $tpCar = $veic->tpCar,
                $UF = $veic->UF
            );

            $reboques = $this->movimento->mov_reboque;
            foreach ($reboques as $reboque) {
                $veic = new stdClass();
                $veic->cInt = $reboque->ope_centro2_equip->id;
                $veic->placa = $reboque->ope_centro2_equip->placa;
                $veic->RENAVAM = $reboque->ope_centro2_equip->renavam;
                $veic->tara = floatval($reboque->ope_centro2_equip->tara);
                $veic->capKG = floatval($reboque->ope_centro2_equip->capacidade_kg);
                $veic->capM3 = floatval($reboque->ope_centro2_equip->capacidade_m3);
                $veic->tpRod = $reboque->ope_centro2_equip->tipo_rodado;
                $veic->tpCar = $reboque->ope_centro2_equip->tipo_carroceria;
                $veic->UF = $reboque->ope_centro2_equip->ger_cidade->ger_uf->sigla_uf;

                $prop = new stdClass();
                $prop->CNPJ = soNumeros($reboque->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->doc_cnpj);
                $prop->CPF = soNumeros($reboque->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->doc_cpf);
                $prop->RNTRC = soNumeros($reboque->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->nr_rntrc);
                $prop->xNome = $reboque->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->nome;
                $prop->IE = soNumeros($reboque->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->doc_ie);
                $prop->UFprop = $reboque->ope_centro2_equip->ger_pessoa_endereco->ger_cidade->ger_uf->sigla_uf;
                $prop->tpProp = $reboque->ope_centro2_equip->tipo_transp_auto_carga;

                $make->tagVeicReboque(
                    $cInt = $veic->cInt,
                    $placa = $veic->placa,
                    $renavam = $veic->RENAVAM,
                    $tara = $veic->tara,
                    $capKG = $veic->capKG,
                    $capM3 = $veic->capM3,
                    $CPF = $prop->CPF,
                    $CNPJ = $prop->CNPJ,
                    $propRNTRC = $prop->RNTRC,
                    $xNome = $prop->xNome,
                    $IE = $prop->IE,
                    $UFprop = $prop->UFprop,
                    $tpProp = $prop->tpProp,
                    $tpCar = $veic->tpCar,
                    $UF = $veic->UF
                );
            }

            $condutores = $this->movimento->mov_condutor;
            foreach ($condutores as $condutor) {
                $make->tagCondutor(
                    $xNome = $condutor->ger_pessoa_condutor->none,
                    $cpf = soNumeros($condutor->ger_pessoa_condutor->CPF)
                );
            }
        }

        $qNFe = 0;
        $qCTe = 0;
        $entregas = $this->movimento->mov_entrega;
        foreach ($entregas as $key => $entrega) {
            $make->tagInfMunDescarga(
                $nItem = $key,
                $cMunDescarga = $entrega->ger_cidade->nr_cidade,
                $xMunDescarga = $entrega->ger_cidade->nome
            );
            $documentos = $entrega->mov_entregas_doc;
            foreach ($documentos as $documento) {
                if ($documento->modelo_documento == 55) {
                    $make->tagInfNFe(
                        $nItem = $key,
                        $chNFe = $documento->chave_documento,
                        $segCodBarra = ''
                    );
                    $qNFe++;
                } else {
                    $make->tagInfCTe(
                        $nItem = $key,
                        $chCTe = $documento->chave_documento,
                        $segCodBarra = ''
                    );
                    $qCTe++;
                }
            }
        }

        if ($qNFe == 0) {
            $qNFe = '';
        }
        if ($qCTe == 0) {
            $qCTe = '';
        }
        $make->tagTot(
            $qCTe,
            $qNFe,
            $qMDFe = '',
            $vCarga = number_format($this->movimento->valor_carga, 2, '.', ''),
            $cUnid = $this->movimento->tipo_umedida_carga,
            $qCarga = number_format($this->movimento->qnt_carga, 2, '.', '')
        );

        $seguros = $this->movimento->mov_seguradora;
        foreach ($seguros as $seguro) {
            $make->tagSeg(
                $respSeg = $seguro->tipo_responsavel,
                $CNPJ = soNumeros($seguro->ger_pessoa_responsavel->doc_cnpj),
                $CPF = soNumeros($seguro->ger_pessoa_responsavel->doc_cpf),
                $xSeg = $seguro->ger_pessoa_seguradora->nome,
                $CNPJSeg = soNumeros($seguro->ger_pessoa_seguradora->doc_cnpj),
                $nApol = $seguro->nr_apolice,
                $nAver = $seguro->nr_averbacao
            );
        }
        //TODO TESTAR EM HOMO
        /*
        $infRespTec = new stdClass();
        $infRespTec->CNPJ = '00994539000103';
        $infRespTec->xContato = 'Mardel Cardoso';
        $infRespTec->email = 'mardel@arenaplan.com.br';
        $infRespTec->fone = '11987918980';
        $make->taginfRespTec($infRespTec);
        */

        $make->montaMDFe();
        return $make->getXML();
    }

    public function cancela()
    {
        try {
            TTransaction::open(TSession::getValue('pConn'));

            $this->buscaDados($_REQUEST['id']);

            $justificativa = 'teste de cancelamento';

            $tools = new NFePHP\MDFe\Tools(json_encode($this->config));

            $docEvento = $this->movimento->fis_doc->getEvento(1);

            // cancela a mdfe
            $aRetorno = array();
            $resp = $tools->sefazCancela(
                $this->movimento->fis_doc->chave,
                '',
                '',
                $docEvento->nr_protocolo,
                $justificativa,
                $aRetorno
            );
            if ($aRetorno['cStat'] == 135) {
                // Extrai o XML de Cancelamento
                $doc = new \DOMDocument('1.0', 'utf-8');
                $doc->loadXML($resp, LIBXML_NOBLANKS | LIBXML_NOEMPTYTAG);
                $retEvento = $doc->getElementsByTagName('retEventoMDFe')->item(0);
                $infEvento = $retEvento->getElementsByTagName('infEvento')->item(0);
                // atualiza o fisdoc com os dados de cancelamento
                $fisDoc = new FisDoc();
                $fisDoc->id = $this->movimento->fis_doc->id;
                $fisDoc->unit_id = $this->movimento->fis_doc->unit_id;
                $fisDoc->data_cancelado = date("Y-m-d H:i:s", strtotime($aRetorno['aEvent']['dhRegEvento']));
                $fisDoc->store();
                // insere o evento de cancelamento da mdfe
                $fisDocEvento = new FisDocEvento();
                $fisDocEvento->unit_id = $this->movimento->fis_doc->unit_id;
                $fisDocEvento->fis_doc_id = $this->movimento->fis_doc->id;
                $fisDocEvento->xml_retorno = $doc->saveXML($infEvento);
                $fisDocEvento->tipo_evento = 2; // cancelamento
                $fisDocEvento->nr_protocolo = $aRetorno['aEvent']['nProt'];
                $fisDocEvento->qnt_evento = 1;
                $fisDocEvento->descricao_evento = self::C_EVENTO_CANCELAMENTO;
                $fisDocEvento->store();
            }
            echo sprintf("%s - %s", $aRetorno['aEvent']['cStat'], $aRetorno['aEvent']['xMotivo']);
        } catch (Exception $e) {
            echo $e->getMessage();
        } finally {
            TTransaction::close();
        }
    }

    public function encerra()
    {
        try {
            TTransaction::open(TSession::getValue('pConn'));

            $this->buscaDados($_REQUEST['id']);

            $tools = new NFePHP\MDFe\Tools(json_encode($this->config));

            $docEvento = $this->movimento->fis_doc->getEvento(1);

            // encerra a mdfe
            $aRetorno = array();
            $resp = $tools->sefazEncerra(
                $this->movimento->fis_doc->chave,
                '',
                '',
                $docEvento->nr_protocolo,
                $this->movimento->ger_empresa->end_ger_cidade->ger_uf->nr_uf,
                $this->movimento->ger_empresa->end_ger_cidade->nr_cidade,
                $aRetorno
            );
            if ($aRetorno['aEvent']['cStat'] == 135) {
                // Extrai o XML de Encerramento
                $doc = new \DOMDocument('1.0', 'utf-8');
                $doc->loadXML($resp, LIBXML_NOBLANKS | LIBXML_NOEMPTYTAG);
                $retEvento = $doc->getElementsByTagName('retEventoMDFe')->item(0);
                $infEvento = $retEvento->getElementsByTagName('infEvento')->item(0);
                // atualiza o fisdoc com os dados de encerramento
                $fisDoc = new FisDoc();
                $fisDoc->id = $this->movimento->fis_doc->id;
                $fisDoc->unit_id = $this->movimento->fis_doc->unit_id;
                $fisDoc->data_encerrado = date("Y-m-d H:i:s", strtotime($aRetorno['aEvent']['dhRegEvento']));
                $fisDoc->store();
                // insere o evento de encerramento da mdfe
                $fisDocEvento = new FisDocEvento();
                $fisDocEvento->unit_id = $this->movimento->fis_doc->unit_id;
                $fisDocEvento->fis_doc_id = $this->movimento->fis_doc->id;
                $fisDocEvento->xml_retorno = $doc->saveXML($infEvento);
                $fisDocEvento->tipo_evento = 5; // encerramento
                $fisDocEvento->nr_protocolo = $aRetorno['aEvent']['nProt'];
                $fisDocEvento->qnt_evento = 1;
                $fisDocEvento->descricao_evento = self::C_EVENTO_ENCERRAMENTO;
                $fisDocEvento->store();
            }
            echo sprintf("%s - %s", $aRetorno['aEvent']['cStat'], $aRetorno['aEvent']['xMotivo']);
        } catch (Exception $e) {
            echo $e->getMessage();
        } finally {
            TTransaction::close();
        }
    }

}

?>