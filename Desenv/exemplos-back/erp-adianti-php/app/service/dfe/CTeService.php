<?php

use NFePHP\CTe\Complements;

class CTeService extends BaseService
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
            "schemes" => self::C_CTE_SCHEMES,
            "versao" => self::C_CTE_VERSAO,
            "tokenIBPT" => "",
            "cert" => array(
                "data" => $this->movimento->ger_empresa->fis_certificado->certificado,
                "senha" => $this->movimento->ger_empresa->fis_certificado->senha
            )
        );
        $this->path = sprintf('./files/%s', $this->config['cnpj']);
        @mkdir(sprintf('%s/pdf', $this->path), 0777, true);
        @mkdir(sprintf('%s/xml', $this->path), 0777, true);
    }

    public function geraDacte()
    {
        try {
            TTransaction::open(TSession::getValue('pConn'));
            $this->dacte($_REQUEST['id']);
        } catch (\Exception $e) {
            echo $e->getMessage();
        } finally {
            TTransaction::close();
        }
    }

    private function dacte($movimento)
    {
        $this->buscaDados($movimento);
        if ($this->movimento->fis_doc->fis_doc_tipo->modelo == 57) {
            $danfe = new Dacte($this->movimento->fis_doc->xml_protocolado, 'P', 'A4', '', 'I');
            $danfe->montaDACTe();
            $pdf = $danfe->render();
        } else {
            $danfe = new DacteOSV3($this->movimento->fis_doc->xml_protocolado, 'P', 'A4', '', 'I');
            $danfe->montaDACTe();
            $pdf = $danfe->render();
        }
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
            $tools = new NFePHP\CTe\Tools(json_encode($this->config), NFePHP\Common\Certificate::readPfx(base64_decode($this->config['cert']['data']), $this->config['cert']['senha']));
            $tools->model($this->movimento->fis_doc->fis_doc_tipo->modelo);
            // assinando xml
            $xmlAssinado = $tools->signCTe($xml); // O conteúdo do XML assinado fica armazenado na variável $xmlAssinado
            // enviando xml para a sefaz
            $idLote = str_pad(100, 15, '0', STR_PAD_LEFT); // Identificador do lote
            $resp = $tools->sefazEnviaLote([$xmlAssinado], $idLote);
            // convertendo o $resp que é uma string em um object para poder acessar suas propriedades
            $st = new NFePHP\CTe\Common\Standardize();
            $std = $st->toStd($resp);
            if ($this->movimento->fis_doc->fis_doc_tipo->modelo == 57) {
                if ($std->cStat != 103) {
                    //erro registrar e voltar
                    echo "[$std->cStat] $std->xMotivo";
                } else {
                    $recibo = $std->infRec->nRec; // Vamos usar a variável $recibo para consultar o status do cte
                    $protocolo = $tools->sefazConsultaRecibo($recibo);
                    $st = new NFePHP\CTe\Common\Standardize();
                    $std = $st->toStd($protocolo);
                    $chaveAcesso = $std->protCTe->infProt->chNFe;
                    // grava em disco
                    file_put_contents(sprintf('%s/xml/%s.xml', $this->path, $chaveAcesso), $xmlAssinado);
                    if ($std->protCTe->infProt->cStat == 100) {
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
                        $fisDoc->data_autorizado = date("Y-m-d H:i:s", strtotime($std->protCTe->infProt->dhRecbto));
                        $fisDoc->store();
                        // insere o evento de autorização do cte
                        $fisDocEvento = new FisDocEvento();
                        $fisDocEvento->unit_id = $this->movimento->fis_doc->unit_id;
                        $fisDocEvento->fis_doc_id = $this->movimento->fis_doc->id;
                        $fisDocEvento->xml_retorno = $doc->saveXML($infProt);
                        $fisDocEvento->tipo_evento = 1; // autorização
                        $fisDocEvento->nr_protocolo = $std->protCTe->infProt->nProt;
                        $fisDocEvento->qnt_evento = 1;
                        $fisDocEvento->descricao_evento = self::C_EVENTO_AUTORIZACAO;
                        $fisDocEvento->store();
                        // imprime a danfe
                        $this->dacte($this->movimento->id);
                    } else {
                        echo sprintf("%s - %s", $std->protCTe->infProt->cStat, $std->protCTe->infProt->xMotivo);
                    }
                }
            } else {
                $chaveAcesso = $std->retCTeOS->protCTe->infProt->chNFe;
                // grava em disco
                file_put_contents(sprintf('%s/xml/%s.xml', $this->path, $chaveAcesso), $xmlAssinado);
                if ($std->retCTeOS->protCTe->infProt->cStat == 100) {
                    // protocoloca o xml e salva em arquivo
                    $xmlProtocolado = Complements::toAuthorize($xmlAssinado, $resp);
                    file_put_contents(sprintf('%s/xml/%s.xml', $this->path, $chaveAcesso), $xmlProtocolado);
                    // Extrai o XML de Autorização
                    $doc = new DOMDocument('1.0', 'utf-8');
                    $doc->loadXML($resp, LIBXML_NOBLANKS | LIBXML_NOEMPTYTAG);
                    $infProt = $doc->getElementsByTagName('infProt')->item(0);
                    // atualiza o fisdoc com os dados da autorização
                    $fisDoc = new FisDoc();
                    $fisDoc->id = $this->movimento->fis_doc->id;
                    $fisDoc->unit_id = $this->movimento->fis_doc->unit_id;
                    $fisDoc->xml_assinado = $xmlAssinado;
                    $fisDoc->xml_protocolado = $xmlProtocolado;
                    $fisDoc->data_autorizado = date("Y-m-d H:i:s", strtotime($std->retCTeOS->protCTe->infProt->dhRecbto));
                    $fisDoc->store();
                    // insere o evento de autorização do cte
                    $fisDocEvento = new FisDocEvento();
                    $fisDocEvento->unit_id = $this->movimento->fis_doc->unit_id;
                    $fisDocEvento->fis_doc_id = $this->movimento->fis_doc->id;
                    $fisDocEvento->xml_retorno = $doc->saveXML($infProt);
                    $fisDocEvento->tipo_evento = 1; // autorização
                    $fisDocEvento->nr_protocolo = $std->retCTeOS->protCTe->infProt->nProt;
                    $fisDocEvento->qnt_evento = 1;
                    $fisDocEvento->descricao_evento = self::C_EVENTO_AUTORIZACAO;
                    $fisDocEvento->store();
                    // imprime a danfe
                    $this->dacte($this->movimento->id);
                } else {
                    echo sprintf("%s - %s", $std->retCTeOS->protCTe->infProt->cStat, $std->retCTeOS->protCTe->infProt->xMotivo);
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
        $make = new \NFePHP\CTe\MakeCTe(false);

        $make->taginfCTe(
            self::C_CTE_VERSAO
        );

        $ide = new stdClass();
        $ide->cUF = $this->movimento->ger_empresa->end_ger_cidade->ger_uf->nr_uf;
        $ide->cCT = substr($this->movimento->fis_doc->chave, 35, 8);
        $ide->CFOP = $this->movimento->mov_itemserv[0]->fis_cfop->nr_cfop;
        $ide->natOp = $this->movimento->mov_itemserv[0]->fis_cfop->nome;
        $ide->mod = $this->movimento->fis_doc->fis_doc_tipo->modelo;
        $ide->serie = $this->movimento->fis_doc->serie;
        $ide->nCT = $this->movimento->fis_doc->numero;
        $ide->dhEmi = date("Y-m-d\TH:i:sP", strtotime($this->movimento->data_mov));
        $ide->tpImp = 1; // 1 retrato; 2 paisagem
        $ide->tpEmis = $this->movimento->fis_doc->tipo_emissao;
        $ide->cDV = substr($this->movimento->fis_doc->chave, 43);
        $ide->tpAmb = $this->movimento->fis_doc->ambiente;
        $ide->tpCTe = $this->movimento->mov_operacao->finalidade_doc;
        $ide->procEmi = 0;
        $ide->verProc = self::C_VERSAO_APP; // versao do seu sistema
        $ide->indGlobalizado = ''; // modelo 57
        $ide->cMunEnv = $this->movimento->ger_empresa->end_ger_cidade->nr_cidade;
        $ide->xMunEnv = $this->movimento->ger_empresa->end_ger_cidade->nome;
        $ide->UFEnv = $this->movimento->ger_empresa->end_ger_cidade->ger_uf->sigla_uf;
        $ide->modal = $this->movimento->tipo_modal_carga;
        $ide->tpServ = $this->movimento->tipo_serv_frete;
        $ide->cMunIni = $this->movimento->ger_cidade_carreg->nr_cidade;
        $ide->xMunIni = $this->movimento->ger_cidade_carreg->nome;
        $ide->UFIni = $this->movimento->ger_cidade_carreg->ger_uf->sigla_uf;
        $ide->cMunFim = $this->movimento->ger_cidade_descarreg->nr_cidade;
        $ide->xMunFim = $this->movimento->ger_cidade_descarreg->nome;
        $ide->UFFim = $this->movimento->ger_cidade_descarreg->ger_uf->sigla_uf;
        $ide->retira = "0";  //TODO
        $ide->xDetRetira = "";

        // Busca os dados do Tomador
        $tomador_ctr = $this->movimento->ger_pessoa;
        $enderecotoma_ctr = $this->movimento->ger_pessoa_endereco_fiscal;
        if ($this->movimento->fis_doc->fis_doc_tipo->modelo == 57) {
            if (intval($this->movimento->tipo_tomador_serv_frete) == 0) {
                $tomador_ctr = $this->movimento->ger_pessoa_endereco_reme->ger_pessoa;
                $enderecotoma_ctr = $this->movimento->ger_pessoa_endereco_reme;
            } else if (intval($this->movimento->tipo_tomador_serv_frete) == 1) {
                $tomador_ctr = $this->movimento->ger_pessoa_endereco_expe->ger_pessoa;
                $enderecotoma_ctr = $this->movimento->ger_pessoa_endereco_expe;
            } else if (intval($this->movimento->tipo_tomador_serv_frete) == 2) {
                $tomador_ctr = $this->movimento->ger_pessoa_endereco_rece->ger_pessoa;
                $enderecotoma_ctr = $this->movimento->ger_pessoa_endereco_rece;
            } else if (intval($this->movimento->tipo_tomador_serv_frete) == 3) {
                $tomador_ctr = $this->movimento->ger_pessoa_endereco_dest->ger_pessoa;
                $enderecotoma_ctr = $this->movimento->ger_pessoa_endereco_dest;
            }
        }

        $indIEToma = "1";
        if (intval($tomador_ctr->contrib_icms) == 2) {
            $indIEToma = "2";
            if (in_array($tomador_ctr->end_ger_cidade->ger_uf->sigla_uf, array("AM", "BA", "CE", "GO", "MG", "MS", "MT", "PE", "RN", "SE", "SP"))) {
                $indIEToma = "9";
            }
        } else if (intval($tomador_ctr->contrib_icms) == 9) {
            $indIEToma = "9";
        }

        $ide->indIEToma = $indIEToma;
        $ide->dhCont = '';
        $ide->xJust = '';
        $make->tagide(
            $cUF = $ide->cUF,
            $cCT = $ide->cCT,
            $CFOP = $ide->CFOP,
            $natOp = $ide->natOp,
            $mod = $ide->mod,
            $serie = $ide->serie,
            $nCT = $ide->nCT,
            $dhEmi = $ide->dhEmi,
            $tpImp = $ide->tpImp,
            $tpEmis = $ide->tpEmis,
            $cDV = $ide->cDV,
            $tpAmb = $ide->tpAmb,
            $tpCTe = $ide->tpCTe,
            $procEmi = $ide->procEmi,
            $verProc = $ide->verProc,
            $indGlobalizado = $ide->indGlobalizado,
            $cMunEnv = $ide->cMunEnv,
            $xMunEnv = $ide->xMunEnv,
            $UFEnv = $ide->UFEnv,
            $modal = $ide->modal,
            $tpServ = $ide->tpServ,
            $cMunIni = $ide->cMunIni,
            $xMunIni = $ide->xMunIni,
            $UFIni = $ide->UFIni,
            $cMunFim = $ide->cMunFim,
            $xMunFim = $ide->xMunFim,
            $UFFim = $ide->UFFim,
            $retira = $ide->retira,
            $xDetRetira = $ide->xDetRetira,
            $indIEToma = $ide->indIEToma,
            $dhCont = $ide->dhCont,
            $xJust = $ide->xJust
        );

        if ($this->movimento->fis_doc->fis_doc_tipo->modelo == 67) {
            $percursos = $this->movimento->mov_percurso;
            foreach ($percursos as $percurso) {
                $infPercurso = new stdClass();
                $infPercurso->UFPer = $percurso->ger_cidade->ger_uf->sigla_uf;
                $make->taginfPercurso($infPercurso);
            }
        }

        if ($this->movimento->fis_doc->fis_doc_tipo->modelo == 57) {
            if (intval($this->movimento->tipo_tomador_serv_frete) != 4) {
                $toma3 = new stdClass();
                $toma3->toma = $this->movimento->tipo_tomador_serv_frete;
                $make->tagTomador3(
                    $toma3->toma
                );
            } else {
                $toma4 = new stdClass();
                $toma4->toma = 4;
                $toma4->CNPJ = soNumeros($tomador_ctr->doc_cnpj);
                $toma4->CPF = soNumeros($tomador_ctr->doc_cpf);
                $toma4->IE = soNumeros($tomador_ctr->doc_ie);
                $toma4->xNome = $tomador_ctr->razao_social;
                $toma4->xFant = $tomador_ctr->nome;
                $toma4->fone = soNumeros($tomador_ctr->fone_1);
                $toma4->email = '';
                $make->tagTomador4(
                    $cnpj = $toma4->CNPJ,
                    $cpf = $toma4->CPF,
                    $ie = $toma4->IE,
                    $xNome = $toma4->xNome,
                    $xFant = $toma4->xFant,
                    $fone = $toma4->fone,
                    $email = $toma4->email
                );

                $enderToma4 = new stdClass();
                $enderToma4->xLgr = $enderecotoma_ctr->end_logradouro;
                $enderToma4->nro = $tomador_ctr->end_logradouro_nr;
                $enderToma4->xCpl = $tomador_ctr->end_complemento;
                $enderToma4->xBairro = $tomador_ctr->end_bairro;
                $enderToma4->cMun = $tomador_ctr->end_ger_cidade->nr_cidade;
                $enderToma4->xMun = $tomador_ctr->end_ger_cidade->nome;
                $enderToma4->CEP = soNumeros($tomador_ctr->end_ger_cidade->ger_uf->sigla_uf);
                $enderToma4->UF = $tomador_ctr->end_cep;
                $enderToma4->cPais = $tomador_ctr->end_ger_cidade->ger_uf->ger_pais->nr_pais;
                $enderToma4->xPais = $tomador_ctr->end_ger_cidade->ger_uf->ger_pais->nome;
                $make->tagEndertomador4(
                    $xLgr = $enderToma4->xLgr,
                    $nro = $enderToma4->nro,
                    $xCpl = $enderToma4->xCpl,
                    $xBairro = $enderToma4->xBairro,
                    $cMun = $enderToma4->cMun,
                    $xMun = $enderToma4->xMun,
                    $cep = $enderToma4->CEP,
                    $siglaUF = $enderToma4->UF,
                    $cPais = $enderToma4->cPais,
                    $xPais = $enderToma4->xPais
                );
            }
        } else {
            $tomador = new stdClass();
            $tomador->CNPJ = soNumeros($tomador_ctr->doc_cnpj);
            $tomador->CPF = soNumeros($tomador_ctr->doc_cpf);
            $tomador->IE = soNumeros($tomador_ctr->doc_ie);
            $tomador->xNome = $tomador_ctr->razao_social;
            $tomador->xFant = $tomador_ctr->nome;
            $tomador->fone = soNumeros($tomador_ctr->fone_1);
            $tomador->email = $enderecotoma_ctr->email;
            $make->tagTomador(
                $cnpj = $tomador->CNPJ,
                $cpf = $tomador->CPF,
                $ie = $tomador->IE,
                $xNome = $tomador->xNome,
                $xFant = $tomador->xFant,
                $fone = $tomador->fone,
                $email = $tomador->email
            );

            $enderToma = new stdClass();
            $enderToma->xLgr = $enderecotoma_ctr->end_logradouro;
            $enderToma->nro = $enderecotoma_ctr->end_logradouro_nr;
            $enderToma->xCpl = $enderecotoma_ctr->end_complemento;
            $enderToma->xBairro = $enderecotoma_ctr->end_bairro;
            $enderToma->cMun = $enderecotoma_ctr->end_ger_cidade->nr_cidade;
            $enderToma->xMun = $enderecotoma_ctr->end_ger_cidade->nome;
            $enderToma->CEP = soNumeros($enderecotoma_ctr->end_cep);
            $enderToma->UF = $enderecotoma_ctr->end_ger_cidade->ger_uf->sigla_uf;
            $enderToma->cPais = $enderecotoma_ctr->end_ger_cidade->ger_uf->ger_pais->nr_pais;
            $enderToma->xPais = $enderecotoma_ctr->end_ger_cidade->ger_uf->ger_pais->nome;
            $make->tagEndertomador(
                $xLgr = $enderToma->xLgr,
                $nro = $enderToma->nro,
                $xCpl = $enderToma->xCpl,
                $xBairro = $enderToma->xBairro,
                $cMun = $enderToma->cMun,
                $xMun = $enderToma->xMun,
                $cep = $enderToma->CEP,
                $siglaUF = $enderToma->UF,
                $cPais = $enderToma->cPais,
                $xPais = $enderToma->xPais
            );
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

        if ($this->movimento->fis_doc->fis_doc_tipo->modelo == 57) {
            $rem = new stdClass();
            $rem->CPF = soNumeros($this->movimento->ger_pessoa_endereco_reme->ger_pessoa->doc_cpf);
            $rem->CNPJ = soNumeros($this->movimento->ger_pessoa_endereco_reme->ger_pessoa->doc_cnpj);
            $rem->IE = soNumeros($this->movimento->ger_pessoa_endereco_reme->ger_pessoa->doc_ie);
            $rem->xNome = $this->movimento->ger_pessoa_endereco_reme->ger_pessoa->razao_social;
            if ($this->movimento->fis_doc->ambiente == 2) {
                $rem->xNome = self::C_CTE_HOM;
            }
            $rem->xFant = $this->movimento->ger_pessoa_endereco_reme->ger_pessoa->nome;
            $rem->fone = soNumeros($this->movimento->ger_pessoa_endereco_reme->ger_pessoa->fone_1);
            $rem->email = '';
            $make->tagrem(
                $cnpj = $rem->CNPJ,
                $cpf = $rem->CPF,
                $ie = $rem->IE,
                $xNome = $rem->xNome,
                $xFant = $rem->xFant,
                $fone = $rem->fone,
                $email = $rem->email
            );

            $enderReme = new stdClass();
            $enderReme->xLgr = $this->movimento->ger_pessoa_endereco_reme->end_logradouro;
            $enderReme->nro = $this->movimento->ger_pessoa_endereco_reme->end_logradouro_nr;
            $enderReme->xCpl = $this->movimento->ger_pessoa_endereco_reme->end_complemento;
            $enderReme->xBairro = $this->movimento->ger_pessoa_endereco_reme->end_bairro;
            $enderReme->cMun = $this->movimento->ger_pessoa_endereco_reme->end_ger_cidade->nr_cidade;
            $enderReme->xMun = $this->movimento->ger_pessoa_endereco_reme->end_ger_cidade->nome;
            $enderReme->CEP = soNumeros($this->movimento->ger_pessoa_endereco_reme->end_cep);
            $enderReme->UF = $this->movimento->ger_pessoa_endereco_reme->end_ger_cidade->ger_uf->sigla_uf;
            $enderReme->cPais = $this->movimento->ger_pessoa_endereco_reme->end_ger_cidade->ger_uf->ger_pais->nr_pais;
            $enderReme->xPais = $this->movimento->ger_pessoa_endereco_reme->end_ger_cidade->ger_uf->ger_pais->nome;
            $make->tagEnderRem(
                $xLgr = $enderReme->xLgr,
                $nro = $enderReme->nro,
                $xCpl = $enderReme->xCpl,
                $xBairro = $enderReme->xBairro,
                $cMun = $enderReme->cMun,
                $xMun = $enderReme->xMun,
                $cep = $enderReme->CEP,
                $siglaUF = $enderReme->UF,
                $cPais = $enderReme->cPais,
                $xPais = $enderReme->xPais
            );

            $dest = new stdClass();
            $dest->xNome = $this->movimento->ger_pessoa_endereco_dest->ger_pessoa->nome;
            if ($this->movimento->fis_doc->ambiente == 2) {
                $dest->xNome = self::C_CTE_HOM;
            }
            $dest->CNPJ = soNumeros($this->movimento->ger_pessoa_endereco_dest->ger_pessoa->doc_cnpj);
            $dest->CPF = soNumeros($this->movimento->ger_pessoa_endereco_dest->ger_pessoa->doc_cpf);
            $dest->IE = soNumeros($this->movimento->ger_pessoa_endereco_dest->ger_pessoa->doc_ie);
            $dest->ISUF = '';
            $dest->fone = soNumeros($this->movimento->ger_pessoa_endereco_dest->ger_pessoa->fone_1);
            $make->tagdest(
                $cnpj = $dest->CNPJ,
                $cpf = $dest->CPF,
                $ie = $dest->IE,
                $xNome = $dest->xNome,
                $fone = $dest->fone,
                $isUF = $dest->ISUF,
                $email = ''
            );

            $enderDest = new stdClass();
            $enderDest->xLgr = $this->movimento->ger_pessoa_endereco_dest->end_logradouro;
            $enderDest->nro = $this->movimento->ger_pessoa_endereco_dest->end_logradouro_nr;
            $enderDest->xCpl = $this->movimento->ger_pessoa_endereco_dest->end_complemento;
            $enderDest->xBairro = $this->movimento->ger_pessoa_endereco_dest->end_bairro;
            $enderDest->cMun = $this->movimento->ger_pessoa_endereco_dest->end_ger_cidade->nr_cidade;
            $enderDest->xMun = $this->movimento->ger_pessoa_endereco_dest->end_ger_cidade->nome;
            $enderDest->UF = $this->movimento->ger_pessoa_endereco_dest->end_ger_cidade->ger_uf->sigla_uf;
            $enderDest->CEP = soNumeros($this->movimento->ger_pessoa_endereco_dest->end_cep);
            $enderDest->cPais = $this->movimento->ger_pessoa_endereco_dest->end_ger_cidade->ger_uf->ger_pais->nr_pais;
            $enderDest->xPais = $this->movimento->ger_pessoa_endereco_dest->end_ger_cidade->ger_uf->ger_pais->nome;
            $make->tagEnderDest(
                $xLgr = $enderDest->xLgr,
                $nro = $enderDest->nro,
                $xCpl = $enderDest->xCpl,
                $xBairro = $enderDest->xBairro,
                $cMun = $enderDest->cMun,
                $xMun = $enderDest->xMun,
                $cep = $enderDest->CEP,
                $siglaUF = $enderDest->UF,
                $cPais = $enderDest->cPais,
                $xPais = $enderDest->xPais
            );

            if (intval($this->movimento->ger_pessoa_endereco_id_expe) > 0) {
                $exped = new stdClass();
                $exped->xNome = $this->movimento->ger_pessoa_endereco_expe->ger_pessoa->nome;
                if ($this->movimento->fis_doc->ambiente == 2) {
                    $exped->xNome = self::C_CTE_HOM;
                }
                $exped->CNPJ = soNumeros($this->movimento->ger_pessoa_endereco_expe->ger_pessoa->doc_cnpj);
                $exped->CPF = soNumeros($this->movimento->ger_pessoa_endereco_expe->ger_pessoa->doc_cpf);
                $exped->fone = soNumeros($this->movimento->ger_pessoa_endereco_expe->ger_pessoa->fone_1);
                $exped->IE = soNumeros($this->movimento->ger_pessoa_endereco_expe->ger_pessoa->doc_ie);
                $exped->email = '';
                $make->tagexped(
                    $cnpj = $exped->CNPJ,
                    $cpf = $exped->CPF,
                    $ie = $exped->IE,
                    $xNome = $exped->xNome,
                    $fone = $exped->fone
                );

                $enderExped = new stdClass();
                $enderExped->xLgr = $this->movimento->ger_pessoa_endereco_expe->end_logradouro;
                $enderExped->nro = $this->movimento->ger_pessoa_endereco_expe->end_logradouro_nr;
                $enderExped->xCpl = $this->movimento->ger_pessoa_endereco_expe->end_complemento;
                $enderExped->xBairro = $this->movimento->ger_pessoa_endereco_expe->end_bairro;
                $enderExped->cMun = $this->movimento->ger_pessoa_endereco_expe->end_ger_cidade->nr_cidade;
                $enderExped->xMun = $this->movimento->ger_pessoa_endereco_expe->end_ger_cidade->nome;
                $enderExped->CEP = soNumeros($this->movimento->ger_pessoa_endereco_expe->end_cep);
                $enderExped->UF = $this->movimento->ger_pessoa_endereco_expe->end_ger_cidade->ger_uf->sigla_uf;
                $enderExped->cPais = $this->movimento->ger_pessoa_endereco_expe->end_ger_cidade->ger_uf->ger_pais->nr_pais;
                $enderExped->xPais = $this->movimento->ger_pessoa_endereco_expe->end_ger_cidade->ger_uf->ger_pais->nome;
                $make->tagenderExped(
                    $xLgr = $enderExped->xLgr,
                    $nro = $enderExped->nro,
                    $xCpl = $enderExped->xCpl,
                    $xBairro = $enderExped->xBairro,
                    $cMun = $enderExped->cMun,
                    $xMun = $enderExped->xMun,
                    $cep = $enderExped->CEP,
                    $siglaUF = $enderExped->UF,
                    $cPais = $enderExped->cPais,
                    $xPais = $enderExped->xPais
                );
            }

            if (intval($this->movimento->ger_pessoa_endereco_id_rece) > 0) {
                $receb = new stdClass();
                $receb->xNome = $this->movimento->ger_pessoa_endereco_rece->ger_pessoa->nome;
                if ($this->movimento->fis_doc->ambiente == 2) {
                    $receb->xNome = self::C_CTE_HOM;
                }
                $receb->CNPJ = soNumeros($this->movimento->ger_pessoa_endereco_rece->ger_pessoa->doc_cnpj);
                $receb->CPF = soNumeros($this->movimento->ger_pessoa_endereco_rece->ger_pessoa->doc_cpf);
                $receb->fone = soNumeros($this->movimento->ger_pessoa_endereco_rece->ger_pessoa->fone_1);
                $receb->IE = soNumeros($this->movimento->ger_pessoa_endereco_rece->ger_pessoa->doc_ie);
                $receb->email = '';
                $make->tagreceb(
                    $cnpj = $receb->CNPJ,
                    $cpf = $receb->CPF,
                    $ie = $receb->IE,
                    $xNome = $receb->xNome,
                    $fone = $receb->fone,
                    $email = $receb->email
                );

                $enderReceb = new stdClass();
                $enderReceb->xLgr = $this->movimento->ger_pessoa_endereco_rece->end_logradouro;
                $enderReceb->nro = $this->movimento->ger_pessoa_endereco_rece->end_logradouro_nr;
                $enderReceb->xCpl = $this->movimento->ger_pessoa_endereco_rece->end_complemento;
                $enderReceb->xBairro = $this->movimento->ger_pessoa_endereco_rece->end_bairro;
                $enderReceb->cMun = $this->movimento->ger_pessoa_endereco_rece->end_ger_cidade->nr_cidade;
                $enderReceb->xMun = $this->movimento->ger_pessoa_endereco_rece->end_ger_cidade->nome;
                $enderReceb->CEP = soNumeros($this->movimento->ger_pessoa_endereco_rece->end_cep);
                $enderReceb->UF = $this->movimento->ger_pessoa_endereco_rece->end_ger_cidade->ger_uf->sigla_uf;
                $enderReceb->cPais = $this->movimento->ger_pessoa_endereco_rece->end_ger_cidade->ger_uf->ger_pais->nr_pais;
                $enderReceb->xPais = $this->movimento->ger_pessoa_endereco_rece->end_ger_cidade->ger_uf->ger_pais->nome;
                $make->tagenderReceb(
                    $xLgr = $enderReceb->xLgr,
                    $nro = $enderReceb->nro,
                    $xCpl = $enderReceb->xCpl,
                    $xBairro = $enderReceb->xBairro,
                    $cMun = $enderReceb->cMun,
                    $xMun = $enderReceb->xMun,
                    $cep = $enderReceb->CEP,
                    $siglaUF = $enderReceb->UF,
                    $cPais = $enderReceb->cPais,
                    $xPais = $enderReceb->xPais
                );
            }

        }

        $vPrest = new stdClass();
        $vPrest->vTPrest = number_format($this->movimento->valor_item_frete_total, 2, '.', '');
        $vPrest->vRec = number_format($this->movimento->valor_financeiro_total, 2, '.', '');
        $make->tagvPrest(
            $vTPrest = $vPrest->vTPrest,
            $vRec = $vPrest->vRec
        );

        $complementos = $this->movimento->mov_comp;
        foreach ($complementos as $complemento) {
            $Comp = new stdClass();
            $Comp->xNome = $complemento->nome_comp;
            $Comp->vComp = number_format($complemento->qnt_comp, 2, '.', '');
            $make->tagComp(
                $xNome = $Comp->xNome,
                $vComp = $Comp->vComp
            );
        }

        $produto = '';
        foreach ($this->movimento->mov_itemserv as $key => $item) {
            $produto = $item->ger_itemserv->nome;
            if (in_array($item->ger_itemserv->origem_fiscal, [0, 3, 4, 5, 8])) {
                $vTotTrib = $item->valor_bruto * ($item->ger_itemserv->fis_nbs->fis_ibpt->perc_nacional / 100);
            } else {
                $vTotTrib = $item->valor_bruto * ($item->ger_itemserv->fis_nbs->fis_ibpt->perc_importado / 100);
            }
            $vTotTrib = number_format($vTotTrib, 2, '.', '');
            $make->tagImposto(
                $vTotTrib
            );
            if ($emit->CRT == 3) {
                $impostoICMS = FisTributacao::retornaImposto($item->fis_tributacao, [self::C_TRIBUTO_ICMS, self::C_TRIBUTO_ST]);
                $icms = new stdClass();
                $icms->cst = $impostoICMS->cst;
                $icms->vBC = number_format($impostoICMS->valor_base_calc, 13, 2);
                $icms->pICMS = number_format($impostoICMS->perc_aliquota, 13, 2);
                $icms->vICMS = number_format($impostoICMS->valor_imposto, 13, 2);
                $icms->pRedBC = number_format($impostoICMS->perc_reducao_base_calc, 13, 2);
                $icms->vBCSTRet = number_format(0, 13, 2);
                $icms->vICMSSTRet = number_format(0, 13, 2);
                $icms->pICMSSTRet = number_format(0, 13, 2);
                $icms->vCred = number_format(0, 13, 2);
                if ($this->movimento->ger_cidade_carreg->ger_uf->sigla_uf != $this->movimento->ger_empresa->end_ger_cidade->ger_uf->sigla_uf) {
                    $make->tagICMSOutraUF(
                        $pRedBCOutraUF = $icms->pRedBC,
                        $vBCOutraUF = $icms->vBC,
                        $pICMSOutraUF = $icms->pICMS,
                        $vICMSOutraUF = $icms->vICMS
                    );
                } else {
                    $make->tagicms(
                        $cst = $icms->cst,
                        $vBC = $icms->vBC,
                        $pICMS = $icms->pICMS,
                        $vICMS = $icms->vICMS,
                        $pRedBC = $icms->pRedBC,
                        $vBCSTRet = $icms->vBCSTRet,
                        $vICMSSTRet = $icms->vICMSSTRet,
                        $pICMSSTRet = $icms->pICMSSTRet,
                        $vCred = $icms->vCred
                    );
                }
            } else {
                $make->tagICMSSN();
            }

            if ($this->movimento->fis_doc->fis_doc_tipo->modelo == 67) {
                $impostoPIS = FisTributacao::retornaImposto($item->fis_tributacao, [self::C_TRIBUTO_PIS]);
                $impostoCOFINS = FisTributacao::retornaImposto($item->fis_tributacao, [self::C_TRIBUTO_COFINS]);
                $impostoIR = FisTributacao::retornaImposto($item->fis_tributacao, [self::C_TRIBUTO_IR]);
                $impostoINSS = FisTributacao::retornaImposto($item->fis_tributacao, [self::C_TRIBUTO_INSS]);
                $impostoCSLL = FisTributacao::retornaImposto($item->fis_tributacao, [self::C_TRIBUTO_CSLL]);

                $infTribFed = new stdClass();
                $infTribFed->vPIS = number_format($impostoPIS->valor_imposto, 2, '.', '');
                $infTribFed->vCOFINS = number_format($impostoCOFINS->valor_imposto, 2, '.', '');
                $infTribFed->vIR = number_format($impostoIR->valor_imposto, 2, '.', '');
                $infTribFed->vINSS = number_format($impostoINSS->valor_imposto, 2, '.', '');
                $infTribFed->vCSLL = number_format($impostoCSLL->valor_imposto, 2, '.', '');
                $make->taginfTribFed(
                    $vPIS = $infTribFed->vPIS,
                    $vCOFINS = $infTribFed->vCOFINS,
                    $vIR = $infTribFed->vIR,
                    $vINSS = $infTribFed->vINSS,
                    $vCSLL = $infTribFed->vCSLL
                );
            }
        }

        if (intval($this->movimento->mov_operacao->finalidade_doc) == 0) { // Normal
            $make->tagCteNormal(
                $vCarga = number_format($this->movimento->valor_item_frete_total, 2, '.', ''),
                $proPred = $produto,
                $xOutCat = '',
                $xDescServ = $produto
            );

            $cargas = $this->movimento->mov_medida;
            foreach ($cargas as $carga) {
                $infQ = new stdClass();
                $infQ->cUnid = $carga->ger_umedida->nr_umedida;
                $infQ->xNome = $carga->tipo_medida;
                $infQ->qCarga = number_format($carga->qnt_medida, 4, '.', '');
                $make->taginfQ(
                    $cUnid = $infQ->cUnid,
                    $tpMed = $infQ->xNome,
                    $qCarga = $infQ->qCarga
                );
            }

            if ($this->movimento->fis_doc->fis_doc_tipo->modelo == 67) {
                $seguros = $this->movimento->mov_seguradora;
                foreach ($seguros as $seguro) {
                    $seg = new stdClass();
                    $seg->respSeg = $seguro->tipo_responsavel;
                    $seg->xSeg = $seguro->ger_pessoa_seguradora->nome;
                    $seg->nApol = $seguro->nr_apolice;
                    $make->tagSeg(
                        $respSeg = $seg->respSeg,
                        $xSeg = $seg->xSeg,
                        $nApol = $seg->nApol
                    );
                }
            }

            $notas = $this->movimento->mov_entrega_doc;
            if (count($notas) > 0) {
                foreach ($notas as $nota) {
                    if ($nota->modelo_documento == 55) {
                        $infNFe = new stdClass();
                        $infNFe->chave = $nota->chave_documento;
                        $make->tagNFeRef(
                            $chave = $infNFe->chave
                        );
                    } else {
                        $infDocRef = new stdClass();
                        $infDocRef->nDoc = $nota->nr_documento;
                        $infDocRef->serie = $nota->serie_documento;
                        $infDocRef->subserie = $nota->subserie_documento;
                        $infDocRef->dEmi = date("Y-m-d", strtotime($nota->data_emissao));
                        $infDocRef->vDoc = number_format($nota->valor_total, 2, '.', '');
                        $make->tagDocRef(
                            $nDoc = $infDocRef->nDoc,
                            $serie = $infDocRef->serie,
                            $subserie = $infDocRef->subserie,
                            $dEmi = $infDocRef->dEmi,
                            $vDoc = $infDocRef->vDoc
                        );
                    }
                }
            } else {
                $infOutros = new stdClass();
                $infOutros->tpDoc = "99";
                $make->taginfOutros(
                    $tpDoc = $infOutros->tpDoc,
                    $descOutros = '',
                    $nDoc = '',
                    $dEmi = '',
                    $vDocFisc = '',
                    $dPrev = ''
                );
            }

            // duplicatas
            $duplicatas = $this->movimento->fin_pagrec_origem->fin_pagrec->fin_pagrec_parc;
            // não estao aceitando duplicadas ainda

            if (intval($this->movimento->tipo_modal_carga) == 1) {
                $infModal = new stdClass();
                $infModal->versaoModal = self::C_CTE_VERSAO_MODAL;
                $make->tagInfModal(
                    $modal = $this->movimento->tipo_modal_carga,
                    $versaoModal = $infModal->versaoModal
                );

                if ($this->movimento->fis_doc->fis_doc_tipo->modelo == 57) {
                    $rodo = new stdClass();
                    $rodo->RNTRC = $this->movimento->ger_empresa->doc_rntrc;
                    $make->tagrodo(
                        $RNTRC = $rodo->RNTRC
                    );
                } else if (intval($this->movimento->tipo_serv_frete) != 7) { // Transporte de Valores
                    if (intval($this->movimento->tipo_serv_frete) == 6) { // Transporte de Pessoas
                        $rodoOS = new stdClass();
                        if ($this->movimento->ger_cidade_carreg->ger_uf->sigla_uf != $this->movimento->ger_cidade_descarreg->ger_uf->sigla_uf) { // Operacao Interestadual
                            $rodoOS->TAF = soNumeros($this->movimento->taf);
                        } else {
                            $rodoOS->NroRegEstadual = soNumeros($this->movimento->ope_centro2_veiculo->ope_centro2_equip->nr_registro_estadual);
                        }
                        $make->tagrodoOS(
                            $TAF = strval($rodoOS->TAF),
                            $NroRegEstadual = strval($rodoOS->NroRegEstadual)
                        );

                        $infFretamento = new stdClass();
                        $infFretamento->tpFretamento = $this->movimento->tipo_fretamento;
                        $infFretamento->dhViagem = date("Y-m-d\TH:i:sP", strtotime($this->movimento->data_entrada_saida));
                        $make->taginfFretamento(
                            $tpFretamento = $infFretamento->tpFretamento,
                            $dhViagem = $infFretamento->dhViagem
                        );
                    }

                    $frete = $this->movimento->mov_frete;
                    if ($frete != null) {
                        $veic = new stdClass();
                        $veic->cInt = $frete->ope_centro2_equip->id;
                        $veic->RENAVAM = $frete->ope_centro2_equip->renavam;
                        $veic->placa = $frete->ope_centro2_equip->placa;
                        $veic->tara = floatval($frete->ope_centro2_equip->tara);
                        $veic->capKG = floatval($frete->ope_centro2_equip->capacidade_kg);
                        $veic->capM3 = floatval($frete->ope_centro2_equip->capacidade_m3);
                        $veic->tpProp = $frete->ope_centro2_equip->ope_centro2->tipo_prop;
                        $veic->tpVeic = $frete->ope_centro2_equip->tipo_tracao;
                        $veic->tpRod = $frete->ope_centro2_equip->tipo_rodado;
                        $veic->tpCar = $frete->ope_centro2_equip->tipo_carroceria;
                        $veic->UF = $frete->ope_centro2_equip->ger_cidade->ger_uf->sigla_uf;

                        $veic->CNPJ = soNumeros($frete->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->doc_cnpj);
                        $veic->CPF = soNumeros($frete->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->doc_cpf);
                        $veic->RNTRC = soNumeros($frete->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->nr_rntrc);
                        $veic->xNome = $frete->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->nome;
                        $veic->IE = soNumeros($frete->ope_centro2_equip->ope_centro2->ger_pessoa_endereco->ger_pessoa->doc_ie);
                        $veic->propUF = $frete->ope_centro2_equip->ger_pessoa_endereco->ger_cidade->ger_uf->sigla_uf;
                        $veic->tpPropProp = $frete->ope_centro2_equip->tipo_transp_auto_carga;
                        $make->tagveic(
                            $RENAVAM = $veic->RENAVAM,
                            $placa = $veic->placa,
                            $UF = $veic->UF
                        );
                    }
                }
            }
        } else if (intval($this->movimento->mov_operacao->finalidade_doc) == 1) { // Complemento de Valores
            $origem = new Mov($this->movimento->mov_origem->mov_id_origem);

            $infCteAnu = new stdClass();
            $infCteAnu->chCTe = $origem->fis_doc->chave;
            $infCteAnu->data = date("Y-m-d", strtotime($this->movimento->data_anulacao));
            $make->taginfCteAnu(
                $chCte = $infCteAnu->chCTe,
                $dEmi = $infCteAnu->data
            );
        } else if (intval($this->movimento->mov_operacao->finalidade_doc) == 2) { // Anulação de Valores
            $origem = new Mov($this->movimento->mov_origem->mov_id_origem);

            $infCteComp = new stdClass();
            $infCteComp->chCTe = $origem->fis_doc->chave;
            $make->taginfCTeComp(
                $chCTe = $infCteComp->chCTe
            );
        }

        if ($this->movimento->fis_doc->fis_doc_tipo->modelo == 57 and $this->movimento->tipo_serv_frete > 0) {
            $origem = new Mov($this->movimento->mov_origem->mov_id_origem);

            $emiDocAnt = new stdClass();
            $emiDocAnt->CNPJ = soNumeros($origem->ger_pessoa_endereco_fiscal->ger_pessoa->doc_cnpj);
            $emiDocAnt->CPF = soNumeros($origem->ger_pessoa_endereco_fiscal->ger_pessoa->doc_cpf);
            $emiDocAnt->IE = soNumeros($origem->ger_pessoa_endereco_fiscal->ger_pessoa->doc_ie);
            $emiDocAnt->UF = $origem->ger_pessoa_endereco_fiscal->end_ger_cidade->ger_uf->sigla_uf;
            $emiDocAnt->xNome = $origem->ger_pessoa_endereco_fiscal->ger_pessoa->nome;
            $make->tagemiDocAnt(
                $cnpj = $emiDocAnt->CNPJ,
                $cpf = $emiDocAnt->CPF,
                $ie = $emiDocAnt->IE,
                $uf = $emiDocAnt->UF,
                $xNome = $emiDocAnt->xNome
            );

            foreach ($this->movimento->mov_entrega_doc_ant as $docAnt) {
                $idDocAntEle = new stdClass();
                $idDocAntEle->chCTe = $docAnt->chave_documento;
                $make->tagDocAntEle(
                    $chCTe = $idDocAntEle->chCTe
                );
            }
        }

        if ($this->movimento->observacao_transp != '' or $this->movimento->observacao_serv != '') {
            $compl = new stdClass();
            $compl->xCaracAd = $this->movimento->observacao_transp;
            $compl->xCaracSer = $this->movimento->observacao_serv;
            $make->tagcompl(
                $xCaracAd = $compl->xCaracAd,
                $xCaracSer = $compl->xCaracSer,
                $xEmi = '',
                $origCalc = '',
                $destCalc = '',
                $xObs = ''
            );
        }

        /*
        $infRespTec = new stdClass();
        $infRespTec->CNPJ = '00994539000103';
        $infRespTec->xContato = 'Mardel Cardoso';
        $infRespTec->email = 'mardel@arenaplan.com.br';
        $infRespTec->fone = '11987918980';
        $make->taginfRespTec($infRespTec);
        */

        $make->montaCTe();
        return $make->getXML();
    }

    public function cancela()
    {
        try {
            TTransaction::open(TSession::getValue('pConn'));

            $this->buscaDados($_REQUEST['id']);

            $justificativa = 'teste de cancelamento';

            $tools = new NFePHP\CTe\Tools(json_encode($this->config), NFePHP\Common\Certificate::readPfx(base64_decode($this->config['cert']['data']), $this->config['cert']['senha']));
            $tools->model($this->movimento->fis_doc->fis_doc_tipo->modelo);

            $docEvento = $this->movimento->fis_doc->getEvento(1);

            // cancela a nfe
            $resp = $tools->sefazCancela($this->movimento->fis_doc->chave, $justificativa, $docEvento->nr_protocolo);
            $st = new NFePHP\CTe\Common\Standardize();
            $std = $st->toStd($resp);
            if ($std->infEvento->cStat == 135) {
                // Extrai o XML de Cancelamento
                $doc = new DOMDocument('1.0', 'utf-8');
                $doc->loadXML($resp, LIBXML_NOBLANKS | LIBXML_NOEMPTYTAG);
                $retEvento = $doc->getElementsByTagName('retEventoCTe')->item(0);
                $infEvento = $retEvento->getElementsByTagName('infEvento')->item(0);
                // atualiza o fisdoc com os dados da autorização
                $fisDoc = new FisDoc();
                $fisDoc->id = $this->movimento->fis_doc->id;
                $fisDoc->unit_id = $this->movimento->fis_doc->unit_id;
                $fisDoc->data_cancelado = date("Y-m-d H:i:s", strtotime($std->infEvento->dhRegEvento));
                $fisDoc->store();
                // insere o evento de cancelamento do cte
                $fisDocEvento = new FisDocEvento();
                $fisDocEvento->unit_id = $this->movimento->fis_doc->unit_id;
                $fisDocEvento->fis_doc_id = $this->movimento->fis_doc->id;
                $fisDocEvento->xml_retorno = $doc->saveXML($infEvento);
                $fisDocEvento->tipo_evento = 2; // cancelamento
                $fisDocEvento->nr_protocolo = $std->infEvento->nProt;
                $fisDocEvento->qnt_evento = 1;
                $fisDocEvento->descricao_evento = self::C_EVENTO_CANCELAMENTO;
                $fisDocEvento->store();
            }
            echo sprintf("%s - %s", $std->infEvento->cStat, $std->infEvento->xMotivo);
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
                "schemes" => self::C_CTE_SCHEMES,
                "versao" => self::C_CTE_VERSAO,
                "tokenIBPT" => "",
                "cert" => array(
                    "data" => $empresa->fis_certificado->certificado,
                    "senha" => $empresa->fis_certificado->senha
                )
            );

            $tools = new NFePHP\CTe\Tools(json_encode($this->config), NFePHP\Common\Certificate::readPfx(base64_decode($this->config['cert']['data']), $this->config['cert']['senha']));
            $tools->model($docTipo->modelo);
            // inutiliza a nfe
            $resp = $tools->sefazInutiliza($serie, $inicio, $final, $justificativa);
            $st = new NFePHP\CTe\Common\Standardize();
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
                // insere o evento de inutilização do cte
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

    public function cce()
    {
        try {
            TTransaction::open(TSession::getValue('pConn'));

            $this->buscaDados($_REQUEST['id']);

            $justificativa = 'correcao do numero do endereco para 2'; //TODO Passa parametro no metodo
            $correcoes = array(
                array(
                    'grupoAlterado' => 'ide',
                    'campoAlterado' => 'natOp',
                    'valorAlterado' => 'OUTRA NATUREZA'
                )
            );

            $tools = new NFePHP\CTe\Tools(json_encode($this->config), NFePHP\Common\Certificate::readPfx(base64_decode($this->config['cert']['data']), $this->config['cert']['senha']));
            $tools->model($this->movimento->fis_doc->fis_doc_tipo->modelo);

            $docEvento = $this->movimento->fis_doc->getEvento(4);
            $sequenciaEvento = intval($docEvento->qnt_evento) + 1;

            // cartao de correcao da nfe
            $resp = $tools->sefazCCe($this->movimento->fis_doc->chave, $correcoes, $sequenciaEvento);
            $st = new NFePHP\CTe\Common\Standardize();
            $std = $st->toStd($resp);
            if ($std->infEvento->cStat == 135) {
                // Extrai o XML da Carta de Correção
                $doc = new DOMDocument('1.0', 'utf-8');
                $doc->loadXML($resp, LIBXML_NOBLANKS | LIBXML_NOEMPTYTAG);
                $retEvento = $doc->getElementsByTagName('retEventoCTe');
                foreach ($retEvento as $key => $evento) {
                    $infEvento = $evento->getElementsByTagName('infEvento')->item(0);
                    if (in_array(intval($infEvento->getElementsByTagName('cStat')->item(0)->nodeValue), array(
                        135
                    ))) {
                        break;
                    }
                }
                file_put_contents(sprintf('%s/xml/%s-cce.xml', $this->path, $this->movimento->fis_doc->chave), $resp);
                // insere o evento de cancelamento do cte
                $fisDocEvento = new FisDocEvento();
                $fisDocEvento->unit_id = $this->movimento->fis_doc->unit_id;
                $fisDocEvento->fis_doc_id = $this->movimento->fis_doc->id;
                $fisDocEvento->xml_retorno = $doc->saveXML($infEvento);
                $fisDocEvento->tipo_evento = 4; // carta de correção
                $fisDocEvento->nr_protocolo = $std->infEvento->nProt;
                $fisDocEvento->qnt_evento = $sequenciaEvento;
                $fisDocEvento->descricao_evento = $justificativa;
                $fisDocEvento->store();
            }
            echo sprintf("%s - %s", $std->infEvento->cStat, $std->infEvento->xMotivo);
        } catch (Exception $e) {
            echo $e->getMessage();
        } finally {
            TTransaction::close();
        }
    }

}

?>