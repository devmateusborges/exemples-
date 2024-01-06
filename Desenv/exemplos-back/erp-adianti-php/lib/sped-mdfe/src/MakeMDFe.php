<?php

namespace NFePHP\MDFe;

/**
 * Classe a construção do xml do Manifesto Eletrônico de Documentos Fiscais (MDF-e)
 * NOTA: Esta classe foi construida conforme estabelecido no
 * Manual de Orientação do Contribuinte
 * Padrões Técnicos de Comunicação do Manifesto Eletrônico de Documentos Fiscais
 * versão 1.00 de Junho de 2012
 *
 * @author    Roberto L. Machado <linux.rlm at gmail dot com>
 * @package   nfephp-org/sped-mdfe
 * @name      Make .php
 * @copyright 2009-2016 NFePHP
 * @license   http://www.gnu.org/licenses/lesser.html LGPL v3
 * @link      http://github.com/nfephp-org/sped-mdfe for the canonical source repository
 * @category  Library
 */
class MakeMDFe
{

    /**
     * erros
     * Matriz contendo os erros reportados pelas tags obrigatórias
     * e sem conteúdo
     * @var array
     */
    public $erros = array();
    /**
     * xml
     * String com o xml da NFe montado
     * @var string
     */
    public $xml = '';
    /**
     * dom
     * Variável onde será montado o xml do documento fiscal
     * @var \NFePHP\Common\Dom\Dom
     */
    public $dom;
    /**
     * versao
     * numero da versão do xml da MDFe
     *
     * @var string
     */
    public $versao = '3.00';
    /**
     * mod
     * modelo da MDFe 58
     *
     * @var integer
     */
    public $mod = '58';
    /**
     * chave da MDFe
     *
     * @var string
     */
    public $chMDFe = '';

    //propriedades privadas utilizadas internamente pela classe
    private $MDFe = ''; //DOMNode
    private $modal = ''; //DOMNode
    private $infMDFe = ''; //DOMNode
    private $ide = ''; //DOMNode
    private $emit = ''; //DOMNode
    private $enderEmit = ''; //DOMNode
    private $infModal = ''; //DOMNode
    private $infANTT = ''; //DOMNode
    private $tot = ''; //DOMNode
    private $infAdic = ''; //DOMNode
    private $rodo = ''; //DOMNode
    private $veicPrincipal = ''; //DOMNode
    private $aereo = ''; //DOMNode
    private $trem = ''; //DOMNode
    private $aqua = ''; //DOMNode
    // Arrays
    private $aInfMunCarrega = array(); //array de DOMNode
    private $aInfPercurso = array(); //array de DOMNode
    private $aInfMunDescarga = array(); //array de DOMNode
    private $aInfCTe = array(); //array de DOMNode
    private $aInfCT = array(); //array de DOMNode
    private $aInfNFe = array(); //array de DOMNode
    private $aInfNF = array(); //array de DOMNode
    private $aCIOT = array(); //array de DOMNode
    private $aLacres = array(); //array de DOMNode
    private $aCondutor = array(); //array de DOMNode
    private $aReboque = array(); //array de DOMNode
    private $aDisp = array(); //array de DOMNode
    private $aContratante = array(); //array de DOMNode
    private $aVag = array(); //array de DOMNode
    private $aInfTermCarreg = array(); //array de DOMNode
    private $aInfTermDescarreg = array(); //array de DOMNode
    private $aInfEmbComb = array(); //array de DOMNode
    private $aCountDoc = array(); //contador de documentos fiscais
    private $aSeg = array(); //array de DOMNodes

    public function __construct($formatOutput = true, $preserveWhiteSpace = false)
    {
        $this->dom = new \DOMDocument('1.0', 'UTF-8');
        $this->dom->formatOutput = $formatOutput;
        $this->dom->preserveWhiteSpace = $preserveWhiteSpace;
    }

    /**
     * getXML
     * retorna o xml da CTe que foi montado
     * @return string
     */
    public function getXML()
    {
        return $this->xml;
    }

    /**
     *
     * @return boolean
     */
    public function montaMDFe()
    {
        if (count($this->erros) > 0) {
            return false;
        }
        //cria a tag raiz da MDFe
        $this->zTagMDFe();
        //monta a tag ide com as tags adicionais
        $this->zTagIde();
        //tag ide [4]
        $this->zAppChild($this->infMDFe, $this->ide, 'Falta tag "infMDFe"');
        //tag enderemit [30]
        $this->zAppChild($this->emit, $this->enderEmit, 'Falta tag "emit"');
        //tag emit [25]
        $this->zAppChild($this->infMDFe, $this->emit, 'Falta tag "infMDFe"');
        //tag infModal [41]
        if ($this->modal == '1') {
            $this->zTagRodo();
        } else if ($this->modal == '2') {
            $this->zTagAereo();
        } else if ($this->modal == '3') {
            $this->zTagAqua();
        } else {
            $this->zTagFerrov();
        }
        $this->zAppChild($this->infMDFe, $this->infModal, 'Falta tag "infMDFe"');
        //tag indDoc [44]
        $this->zTagInfDoc();
        // tag seg [118]
        foreach ($this->aSeg as $seg) {
            $this->zAppChild($this->infMDFe, $seg, 'Falta tag "infMDFe"');
        }
        //tag tot [68]
        $this->zAppChild($this->infMDFe, $this->tot, 'Falta tag "infMDFe"');
        //tag lacres [76]
        $this->zTagLacres();
        //tag infAdic [78]
        $this->zAppChild($this->infMDFe, $this->infAdic, 'Falta tag "infMDFe"');
        //[1] tag infCte (1 A01)
        $this->zAppChild($this->MDFe, $this->infMDFe, 'Falta tag "CTe"');
        //[0] tag CTe
        $this->zAppChild($this->dom, $this->MDFe, 'Falta DOMDocument');
        //convert DOMDocument para string
        $this->xml = $this->dom->saveXML();
        return true;
    }


    /**
     * taginfMDFe
     * Informações da MDFe 1 pai MDFe
     * tag MDFe/infMDFe
     *
     * @param string $chave
     * @param string $versao
     * @return DOMElement
     */
    public function taginfMDFe($chave = '', $versao = '')
    {
        $this->infMDFe = $this->dom->createElement("infMDFe");
        $this->infMDFe->setAttribute("Id", 'MDFe' . $chave);
        $this->infMDFe->setAttribute("versao", $versao);
        $this->versao = $versao;
        $this->chMDFe = $chave;
        return $this->infMDFe;
    }

    /**
     * tgaide
     * Informações de identificação da MDFe 4 pai 1
     * tag MDFe/infMDFe/ide
     *
     * @param string $cUF
     * @param string $tpAmb
     * @param string $tpEmit
     * @param string $tpTransp
     * @param string $mod
     * @param string $serie
     * @param string $nMDF
     * @param string $cMDF
     * @param string $cDV
     * @param string $modal
     * @param string $dhEmi
     * @param string $tpEmis
     * @param string $procEmi
     * @param string $verProc
     * @param string $ufIni
     * @param string $ufFim
     * @return DOMElement
     */
    public function tagide(
        $cUF = '',
        $tpAmb = '',
        $tpEmit = '',
        $tpTransp = '',
        $mod = '58',
        $serie = '',
        $nMDF = '',
        $cMDF = '',
        $cDV = '',
        $modal = '',
        $dhEmi = '',
        $tpEmis = '',
        $procEmi = '',
        $verProc = '',
        $ufIni = '',
        $ufFim = ''
    )
    {
        $this->tpAmb = $tpAmb;
        $identificador = '[4] <ide> - ';
        $ide = $this->dom->createElement("ide");
        $this->zAddChild(
            $ide,
            "cUF",
            $cUF,
            true,
            $identificador . "Código da UF do emitente do Documento Fiscal"
        );
        $this->zAddChild(
            $ide,
            "tpAmb",
            $tpAmb,
            true,
            $identificador . "Identificação do Ambiente"
        );
        $this->zAddChild(
            $ide,
            "tpEmit",
            $tpEmit,
            true,
            $identificador . "Indicador da tipo de emitente"
        );
        $this->zAddChild(
            $ide,
            "tpTransp",
            $tpTransp,
            false,
            $identificador . "Tipo do Transportador"
        );
        $this->zAddChild(
            $ide,
            "mod",
            $mod,
            true,
            $identificador . "Código do Modelo do Documento Fiscal"
        );
        $this->zAddChild(
            $ide,
            "serie",
            $serie,
            true,
            $identificador . "Série do Documento Fiscal"
        );
        $this->zAddChild(
            $ide,
            "nMDF",
            $nMDF,
            true,
            $identificador . "Número do Documento Fiscal"
        );
        $this->zAddChild(
            $ide,
            "cMDF",
            $cMDF,
            true,
            $identificador . "Código do numérico do MDF"
        );
        $this->zAddChild(
            $ide,
            "cDV",
            $cDV,
            true,
            $identificador . "Dígito Verificador da Chave de Acesso da NF-e"
        );
        $this->modal = $modal;
        $this->zAddChild(
            $ide,
            "modal",
            $modal,
            true,
            $identificador . "Modalidade de transporte"
        );
        $this->zAddChild(
            $ide,
            "dhEmi",
            $dhEmi,
            true,
            $identificador . "Data e hora de emissão do Documento Fiscal"
        );
        $this->zAddChild(
            $ide,
            "tpEmis",
            $tpEmis,
            true,
            $identificador . "Tipo de Emissão do Documento Fiscal"
        );
        $this->zAddChild(
            $ide,
            "procEmi",
            $procEmi,
            true,
            $identificador . "Processo de emissão"
        );
        $this->zAddChild(
            $ide,
            "verProc",
            $verProc,
            true,
            $identificador . "Versão do Processo de emissão"
        );
        $this->zAddChild(
            $ide,
            "UFIni",
            $ufIni,
            true,
            $identificador . "Sigla da UF do Carregamento"
        );
        $this->zAddChild(
            $ide,
            "UFFim",
            $ufFim,
            true,
            $identificador . "Sigla da UF do Descarregamento"
        );
        $this->mod = $mod;
        $this->ide = $ide;
        return $ide;
    }

    /**
     * tagInfMunCarrega
     *
     * tag MDFe/infMDFe/ide/infMunCarrega
     *
     * @param string $cMunCarrega
     * @param string $xMunCarrega
     * @return DOMElement
     */
    public function tagInfMunCarrega(
        $cMunCarrega = '',
        $xMunCarrega = ''
    )
    {
        $infMunCarrega = $this->dom->createElement("infMunCarrega");
        $this->zAddChild(
            $infMunCarrega,
            "cMunCarrega",
            $cMunCarrega,
            true,
            "Código do Município de Carregamento"
        );
        $this->zAddChild(
            $infMunCarrega,
            "xMunCarrega",
            $xMunCarrega,
            true,
            "Nome do Município de Carregamento"
        );
        $this->aInfMunCarrega[] = $infMunCarrega;
        return $infMunCarrega;
    }

    /**
     * tagInfPercurso
     *
     * tag MDFe/infMDFe/ide/infPercurso
     *
     * @param string $ufPer
     * @param string $dhIniViagem
     * @return DOMElement
     */
    public function tagInfPercurso(
        $ufPer = '',
        $dhIniViagem = ''
    )
    {
        $infPercurso = $this->dom->createElement("infPercurso");
        $this->zAddChild(
            $infPercurso,
            "UFPer",
            $ufPer,
            true,
            "Sigla das Unidades da Federação do percurso"
        );
        $this->zAddChild(
            $infPercurso,
            "dhIniViagem",
            $dhIniViagem,
            false,
            "Data e hora previstos de inicio da viagem"
        );
        $this->aInfPercurso[] = $infPercurso;
        return $infPercurso;
    }

    /**
     * tagemit
     * Identificação do emitente da MDFe [25] pai 1
     * tag MDFe/infMDFe/emit
     *
     * @param string $cnpj
     * @param string $numIE
     * @param string $xNome
     * @param string $xFant
     * @return DOMElement
     */
    public function tagemit(
        $cnpj = '',
        $numIE = '',
        $xNome = '',
        $xFant = ''
    )
    {
        $identificador = '[25] <emit> - ';
        $this->emit = $this->dom->createElement("emit");
        $this->zAddChild($this->emit, "CNPJ", $cnpj, true, $identificador . "CNPJ do emitente");
        $this->zAddChild($this->emit, "IE", $numIE, true, $identificador . "Inscrição Estadual do emitente");
        $this->zAddChild($this->emit, "xNome", $xNome, true, $identificador . "Razão Social ou Nome do emitente");
        $this->zAddChild($this->emit, "xFant", $xFant, false, $identificador . "Nome fantasia do emitente");
        return $this->emit;
    }

    /**
     * tagenderEmit
     * Endereço do emitente [30] pai [25]
     * tag MDFe/infMDFe/emit/endEmit
     *
     * @param string $xLgr
     * @param string $nro
     * @param string $xCpl
     * @param string $xBairro
     * @param string $cMun
     * @param string $xMun
     * @param string $cep
     * @param string $siglaUF
     * @param string $fone
     * @param string $email
     * @return DOMElement
     */
    public function tagenderEmit(
        $xLgr = '',
        $nro = '',
        $xCpl = '',
        $xBairro = '',
        $cMun = '',
        $xMun = '',
        $cep = '',
        $siglaUF = '',
        $fone = '',
        $email = ''
    )
    {
        $identificador = '[30] <enderEmit> - ';
        $this->enderEmit = $this->dom->createElement("enderEmit");
        $this->zAddChild(
            $this->enderEmit,
            "xLgr",
            $xLgr,
            true,
            $identificador . "Logradouro do Endereço do emitente"
        );
        $this->zAddChild(
            $this->enderEmit,
            "nro",
            $nro,
            true,
            $identificador . "Número do Endereço do emitente"
        );
        $this->zAddChild(
            $this->enderEmit,
            "xCpl",
            $xCpl,
            false,
            $identificador . "Complemento do Endereço do emitente"
        );
        $this->zAddChild(
            $this->enderEmit,
            "xBairro",
            $xBairro,
            true,
            $identificador . "Bairro do Endereço do emitente"
        );
        $this->zAddChild(
            $this->enderEmit,
            "cMun",
            $cMun,
            true,
            $identificador . "Código do município do Endereço do emitente"
        );
        $this->zAddChild(
            $this->enderEmit,
            "xMun",
            $xMun,
            true,
            $identificador . "Nome do município do Endereço do emitente"
        );
        $this->zAddChild(
            $this->enderEmit,
            "CEP",
            $cep,
            true,
            $identificador . "Código do CEP do Endereço do emitente"
        );
        $this->zAddChild(
            $this->enderEmit,
            "UF",
            $siglaUF,
            true,
            $identificador . "Sigla da UF do Endereço do emitente"
        );
        $this->zAddChild(
            $this->enderEmit,
            "fone",
            $fone,
            false,
            $identificador . "Número de telefone do emitente"
        );
        $this->zAddChild(
            $this->enderEmit,
            "email",
            $email,
            false,
            $identificador . "Endereço de email do emitente"
        );
        return $this->enderEmit;
    }

    /**
     * tagInfMunDescarga
     * tag MDFe/infMDFe/infDoc/infMunDescarga
     *
     * @param integer $nItem
     * @param string $cMunDescarga
     * @param string $xMunDescarga
     * @return DOMElement
     */
    public function tagInfMunDescarga(
        $nItem = 0,
        $cMunDescarga = '',
        $xMunDescarga = ''
    )
    {
        $infMunDescarga = $this->dom->createElement("infMunDescarga");
        $this->zAddChild(
            $infMunDescarga,
            "cMunDescarga",
            $cMunDescarga,
            true,
            "Código do Município de Descarga"
        );
        $this->zAddChild(
            $infMunDescarga,
            "xMunDescarga",
            $xMunDescarga,
            true,
            "Nome do Município de Descarga"
        );
        $this->aInfMunDescarga[$nItem] = $infMunDescarga;
        return $infMunDescarga;
    }

    /**
     * tagInfCTe
     * tag MDFe/infMDFe/infDoc/infMunDescarga/infCTe
     *
     * @param integer $nItem
     * @param string $chCTe
     * @param string $segCodBarra
     * @return DOMElement
     */
    public function tagInfCTe(
        $nItem = 0,
        $chCTe = '',
        $segCodBarra = ''
    )
    {
        $infCTe = $this->dom->createElement("infCTe");
        $this->zAddChild(
            $infCTe,
            "chCTe",
            $chCTe,
            true,
            "Chave de Acesso CTe"
        );
        $this->zAddChild(
            $infCTe,
            "SegCodBarra",
            $segCodBarra,
            false,
            "Segundo código de barras do CTe"
        );
        $this->aInfCTe[$nItem][] = $infCTe;
        return $infCTe;
    }

    /**
     * tagInfNFe
     * tag MDFe/infMDFe/infDoc/infMunDescarga/infNFe
     *
     * @param integer $nItem
     * @param string $chNFe
     * @param string $segCodBarra
     * @return DOMElement
     */
    public function tagInfNFe(
        $nItem = 0,
        $chNFe = '',
        $segCodBarra = ''
    )
    {
        $infNFe = $this->dom->createElement("infNFe");
        $this->zAddChild(
            $infNFe,
            "chNFe",
            $chNFe,
            true,
            "Chave de Acesso da NFe"
        );
        $this->zAddChild(
            $infNFe,
            "SegCodBarra",
            $segCodBarra,
            false,
            "Segundo código de barras da NFe"
        );
        $this->aInfNFe[$nItem][] = $infNFe;
        return $infNFe;
    }

    /**
     * tagTot
     * tag MDFe/infMDFe/tot
     *
     * @param string $qCTe
     * @param string $qNFe
     * @param string $qMDFe
     * @param string $vCarga
     * @param string $cUnid
     * @param string $qCarga
     * @return DOMElement
     */
    public function tagTot(
        $qCTe = '',
        $qNFe = '',
        $qMDFe = '',
        $vCarga = '',
        $cUnid = '',
        $qCarga = ''
    )
    {
        $tot = $this->dom->createElement("tot");
        $this->zAddChild(
            $tot,
            "qCTe",
            $qCTe,
            false,
            "Quantidade total de CT-e relacionados no Manifesto"
        );
        $this->zAddChild(
            $tot,
            "qNFe",
            $qNFe,
            false,
            "Quantidade total de NF-e relacionados no Manifesto"
        );
        $this->zAddChild(
            $tot,
            "qMDFe",
            $qMDFe,
            false,
            "Quantidade total de MDF-e relacionados no Manifesto Aquaviário"
        );
        $this->zAddChild(
            $tot,
            "vCarga",
            $vCarga,
            true,
            "Valor total da mercadoria/carga transportada"
        );
        $this->zAddChild(
            $tot,
            "cUnid",
            $cUnid,
            true,
            "Código da unidade de medida do Peso Bruto da Carga / Mercadoria Transportada"
        );
        $this->zAddChild(
            $tot,
            "qCarga",
            $qCarga,
            true,
            "Peso Bruto Total da Carga / Mercadoria Transportada"
        );
        $this->tot = $tot;
        return $tot;
    }

    /**
     * tagLacres
     * tag MDFe/infMDFe/lacres
     *
     * @param string $nLacre
     * @return DOMElement
     */
    public function tagLacres(
        $nLacre = ''
    )
    {
        $lacres = $this->dom->createElement("lacres");
        $this->zAddChild(
            $lacres,
            "nLacre",
            $nLacre,
            false,
            "Número do lacre"
        );
        $this->aLacres[] = $lacres;
        return $lacres;
    }

    /**
     * taginfAdic
     * Grupo de Informações Adicionais Z01 pai A01
     * tag MDFe/infMDFe/infAdic (opcional)
     *
     * @param string $infAdFisco
     * @param string $infCpl
     * @return DOMElement
     */
    public function taginfAdic(
        $infAdFisco = '',
        $infCpl = ''
    )
    {
        $infAdic = $this->dom->createElement("infAdic");
        $this->zAddChild(
            $infAdic,
            "infAdFisco",
            $infAdFisco,
            false,
            "Informações Adicionais de Interesse do Fisco"
        );
        $this->zAddChild(
            $infAdic,
            "infCpl",
            $infCpl,
            false,
            "Informações Complementares de interesse do Contribuinte"
        );
        $this->infAdic = $infAdic;
        return $infAdic;
    }

    /**
     * tagInfModal
     * tag MDFe/infMDFe/infModal
     *
     * @param  $versaoModal
     * @return DOMElement
     */
    public function tagInfModal($versaoModal = '')
    {
        $this->infModal = $this->dom->createElement("infModal");
//        $this->zAddChild(
//            $infModal,
//            "versaoModal",
//            $versaoModal,
//            false,
//            "Versão do leiaute específico para o Modal"
//        );
        $this->infModal->setAttribute("versaoModal", $versaoModal);
        return $this->infModal;
    }

    /**
     * tagAereo
     * tag MDFe/infMDFe/infModal/aereo
     *
     * @param string $nac
     * @param string $matr
     * @param string $nVoo
     * @param string $cAerEmb
     * @param string $cAerDes
     * @param string $dVoo
     * @return DOMElement
     */
    public function tagAereo(
        $nac = '',
        $matr = '',
        $nVoo = '',
        $cAerEmb = '',
        $cAerDes = '',
        $dVoo = ''
    )
    {
        $aereo = $this->dom->createElement("aereo");
        $this->zAddChild(
            $aereo,
            "nac",
            $nac,
            true,
            "Marca da Nacionalidade da aeronave"
        );
        $this->zAddChild(
            $aereo,
            "matr",
            $matr,
            true,
            "Marca de Matrícula da aeronave"
        );
        $this->zAddChild(
            $aereo,
            "nVoo",
            $nVoo,
            true,
            "Número do Vôo"
        );
        $this->zAddChild(
            $aereo,
            "cAerEmb",
            $cAerEmb,
            true,
            "Aeródromo de Embarque - Código IATA"
        );
        $this->zAddChild(
            $aereo,
            "cAerDes",
            $cAerDes,
            true,
            "Aeródromo de Destino - Código IATA"
        );
        $this->zAddChild(
            $aereo,
            "dVoo",
            $dVoo,
            true,
            "Data do Vôo"
        );
        $this->aereo = $aereo;
        return $aereo;
    }

    /**
     * tagTrem
     * tag MDFe/infMDFe/infModal/ferrov/trem
     *
     * @param string $xPref
     * @param string $dhTrem
     * @param string $xOri
     * @param string $xDest
     * @param string $qVag
     * @return DOMElement
     */
    public function tagTrem(
        $xPref = '',
        $dhTrem = '',
        $xOri = '',
        $xDest = '',
        $qVag = ''
    )
    {
        $trem = $this->dom->createElement("trem");
        $this->zAddChild(
            $trem,
            "xPref",
            $xPref,
            true,
            "Prefixo do Trem"
        );
        $this->zAddChild(
            $trem,
            "dhTrem",
            $dhTrem,
            false,
            "Data e hora de liberação do trem na origem"
        );
        $this->zAddChild(
            $trem,
            "xOri",
            $xOri,
            true,
            "Origem do Trem"
        );
        $this->zAddChild(
            $trem,
            "xDest",
            $xDest,
            true,
            "Destino do Trem"
        );
        $this->zAddChild(
            $trem,
            "qVag",
            $qVag,
            true,
            "Quantidade de vagões"
        );
        $this->trem = $trem;
        return $trem;
    }

    /**
     * tagVag
     * tag MDFe/infMDFe/infModal/ferrov/trem/vag
     *
     * @param string $serie
     * @param string $nVag
     * @param string $nSeq
     * @param string $tonUtil
     * @return DOMElement
     */
    public function tagVag(
        $serie = '',
        $nVag = '',
        $nSeq = '',
        $tonUtil = ''
    )
    {
        $vag = $this->dom->createElement("vag");
        $this->zAddChild(
            $vag,
            "serie",
            $serie,
            true,
            "Série de Identificação do vagão"
        );
        $this->zAddChild(
            $vag,
            "nVag",
            $nVag,
            true,
            "Número de Identificação do vagão"
        );
        $this->zAddChild(
            $vag,
            "nSeq",
            $nSeq,
            false,
            "Sequência do vagão na composição"
        );
        $this->zAddChild(
            $vag,
            "TU",
            $tonUtil,
            true,
            "Tonelada Útil"
        );
        $this->aVag[] = $vag;
        return $vag;
    }

    /**
     * tagAqua
     * tag MDFe/infMDFe/infModal/Aqua
     *
     * @param string $cnpjAgeNav
     * @param string $tpEmb
     * @param string $cEmbar
     * @param string $nViagem
     * @param string $cPrtEmb
     * @param string $cPrtDest
     * @return DOMElement
     */
    public function tagAqua(
        $cnpjAgeNav = '',
        $tpEmb = '',
        $cEmbar = '',
        $nViagem = '',
        $cPrtEmb = '',
        $cPrtDest = ''
    )
    {
        $aqua = $this->dom->createElement("Aqua");
        $this->zAddChild(
            $aqua,
            "CNPJAgeNav",
            $cnpjAgeNav,
            true,
            "CNPJ da Agência de Navegação"
        );
        $this->zAddChild(
            $aqua,
            "tpEmb",
            $tpEmb,
            true,
            "Código do tipo de embarcação"
        );
        $this->zAddChild(
            $aqua,
            "cEmbar",
            $cEmbar,
            true,
            "Código da Embarcação"
        );
        $this->zAddChild(
            $aqua,
            "nViagem",
            $nViagem,
            true,
            "Número da Viagem"
        );
        $this->zAddChild(
            $aqua,
            "cPrtEmb",
            $cPrtEmb,
            true,
            "Código do Porto de Embarque"
        );
        $this->zAddChild(
            $aqua,
            "cPrtDest",
            $cPrtDest,
            true,
            "Código do Porto de Destino"
        );
        $this->aqua = $aqua;
        return $aqua;
    }

    /**
     * tagInfTermCarreg
     * tag MDFe/infMDFe/infModal/Aqua/infTermCarreg
     *
     * @param string $cTermCarreg
     * @return DOMElement
     */
    public function tagInfTermCarreg(
        $cTermCarreg = ''
    )
    {
        $infTermCarreg = $this->dom->createElement("infTermCarreg");
        $this->zAddChild(
            $infTermCarreg,
            "cTermCarreg",
            $cTermCarreg,
            true,
            "Código do Terminal de Carregamento"
        );
        $this->aInfTermCarreg[] = $infTermCarreg;
        return $infTermCarreg;
    }

    /**
     * tagInfTermDescarreg
     * tag MDFe/infMDFe/infModal/Aqua/infTermDescarreg
     *
     * @param string $cTermDescarreg
     * @return DOMElement
     */
    public function tagInfTermDescarreg(
        $cTermDescarreg = ''
    )
    {
        $infTermDescarreg = $this->dom->createElement("infTermDescarreg");
        $this->zAddChild(
            $infTermDescarreg,
            "cTermCarreg",
            $cTermDescarreg,
            true,
            "Código do Terminal de Descarregamento"
        );
        $this->aInfTermDescarreg[] = $infTermDescarreg;
        return $infTermDescarreg;
    }

    /**
     * tagInfEmbComb
     * tag MDFe/infMDFe/infModal/Aqua/infEmbComb
     *
     * @param string $cEmbComb
     * @return DOMElement
     */
    public function tagInfEmbComb(
        $cEmbComb = ''
    )
    {
        $infEmbComb = $this->dom->createElement("infEmbComb");
        $this->zAddChild(
            $infEmbComb,
            "cEmbComb",
            $cEmbComb,
            true,
            "Código da embarcação do comboio"
        );
        $this->aInfEmbComb[] = $infEmbComb;
        return $infEmbComb;
    }

    /**
     * infANTT
     * tag MDFe/infMDFe/infModal/infANTT
     *
     * @param string $rntrc
     * @return DOMElement
     */
    public function tagANTT(
        $rntrc = ''
    )
    {
        $this->infANTT = $this->dom->createElement("infANTT");
        $this->zAddChild(
            $this->infANTT,
            "RNTRC",
            $rntrc,
            false,
            "Registro Nacional de Transportadores Rodoviários de Carga"
        );
        return $this->infANTT;
    }

    /**
     * tagCIOT
     * tag MDFe/infMDFe/infModal/infANTT/infCIOT
     *
     * @param string $CIOT
     * @param string $CPF
     * @param string $CNPJ
     * @return DOMElement
     */
    public function tagCIOT(
        $CIOT = '',
        $CPF = '',
        $CNPJ = ''
    )
    {
        $infCIOT = $this->dom->createElement("infCIOT");
        $this->zAddChild(
            $infCIOT,
            "CIOT",
            $CIOT,
            true,
            "Código Identificador da Operação de Transporte"
        );
        if ($CPF != '') {
            $this->zAddChild(
                $infCIOT,
                "CPF",
                $CPF,
                true,
                "Número do CPF responsável pela geração do CIOT"
            );
        } else {
            $this->zAddChild(
                $infCIOT,
                "CNPJ",
                $CNPJ,
                true,
                "Número do CNPJ responsável pela geração do CIOT"
            );
        }
        $this->aCIOT[] = $infCIOT;
        return $infCIOT;
    }

    /**
     * tagVeicTracao
     * tag MDFe/infMDFe/infModal/rodo/veicTracao
     *
     * @param string $cInt
     * @param string $placa
     * @param string $renavam
     * @param string $tara
     * @param string $capKG
     * @param string $capM3
     * @param string $CPF
     * @param string $CNPJ
     * @param string $propRNTRC
     * @param string $xNome
     * @param string $IE
     * @param string $UFprop
     * @param string $tpProp
     * @param string $tpRod
     * @param string $tpCar
     * @param string $UF
     * @return DOMElement
     */
    public function tagVeicTracao(
        $cInt = '',
        $placa = '',
        $renavam = '',
        $tara = '',
        $capKG = '',
        $capM3 = '',
        $CPF = '',
        $CNPJ = '',
        $propRNTRC = '',
        $xNome = '',
        $IE = '',
        $UFprop = '',
        $tpProp = '',
        $tpRod = '',
        $tpCar = '',
        $UF = ''
    )
    {
        $veicPrincipal = $this->zTagVeiculo(
            'veicTracao',
            $cInt,
            $placa,
            $renavam,
            $tara,
            $capKG,
            $capM3,
            $CPF,
            $CNPJ,
            $propRNTRC,
            $xNome,
            $IE,
            $UFprop,
            $tpProp,
            $tpRod,
            $tpCar,
            $UF
        );
        $this->veicPrincipal = $veicPrincipal;
        return $veicPrincipal;
    }

    /**
     * tagCondutor
     * tag MDFe/infMDFe/infModal/rodo/veicPrincipal/condutor
     *
     * @param string $xNome
     * @param string $cpf
     * @return DOMElement
     */
    public function tagCondutor(
        $xNome = '',
        $cpf = ''
    )
    {
        $condutor = $this->dom->createElement("condutor");
        $this->zAddChild(
            $condutor,
            "xNome",
            $xNome,
            true,
            "Nome do condutor"
        );
        $this->zAddChild(
            $condutor,
            "CPF",
            $cpf,
            true,
            "CPF do condutor"
        );
        $this->aCondutor[] = $condutor;
        return $condutor;
    }

    /**
     * tagVeicReboque
     * tag MDFe/infMDFe/infModal/rodo/reboque
     *
     * @param string $cInt
     * @param string $placa
     * @param string $renavam
     * @param string $tara
     * @param string $capKG
     * @param string $capM3
     * @param string $CPF
     * @param string $CNPJ
     * @param string $propRNTRC
     * @param string $xNome
     * @param string $IE
     * @param string $UFprop
     * @param string $tpProp
     * @param string $tpCar
     * @param string $UF
     * @return DOMElement
     */
    public function tagVeicReboque(
        $cInt = '',
        $placa = '',
        $renavam = '',
        $tara = '',
        $capKG = '',
        $capM3 = '',
        $CPF = '',
        $CNPJ = '',
        $propRNTRC = '',
        $xNome = '',
        $IE = '',
        $UFprop = '',
        $tpProp = '',
        $tpCar = '',
        $UF = ''
    )
    {
        $reboque = $this->zTagVeiculo(
            'veicReboque',
            $cInt,
            $placa,
            $renavam,
            $tara,
            $capKG,
            $capM3,
            $CPF,
            $CNPJ,
            $propRNTRC,
            $xNome,
            $IE,
            $UFprop,
            $tpProp,
            '',
            $tpCar,
            $UF
        );
        $this->aReboque[] = $reboque;
        return $reboque;
    }

    /**
     * tagValePed
     * tag MDFe/infMDFe/infModal/rodo/infANTT/valePed
     *
     * @param  $CNPJForn
     * @param  $CNPJPg
     * @param  $CPFPg
     * @param  $nCompra
     * @param  $vValePed
     * @return DOMElement
     */
    public function tagValePed(
        $CNPJForn = '',
        $CNPJPg = '',
        $CPFPg = '',
        $nCompra = '',
        $vValePed = ''
    )
    {
        $disp = $this->dom->createElement('disp');
        $this->zAddChild(
            $disp,
            "CNPJForn",
            $CNPJForn,
            true,
            "CNPJ da empresa fornecedora do Vale-Pedágio"
        );
        if ($CNPJPg != '') {
            $this->zAddChild(
                $disp,
                "CNPJPg",
                $CNPJPg,
                false,
                "CNPJ do responsável pelo pagamento do Vale-Pedágio"
            );
        }
        if ($CPFPg != '') {
            $this->zAddChild(
                $disp,
                "CPFPg",
                $CPFPg,
                false,
                "CF do responsável pelo pagamento do Vale-Pedágio"
            );
        }
        $this->zAddChild(
            $disp,
            "nCompra",
            $nCompra,
            true,
            "Número do comprovante de compra"
        );
        $this->zAddChild(
            $disp,
            "vValePed",
            $vValePed,
            true,
            "Valor do Vale-Pedagio"
        );
        $this->aDisp[] = $disp;
        return $disp;
    }

    /**
     * tagContratante
     * tag MDFe/infMDFe/infModal/rodo/infANTT/infContratante
     *
     * @param  $CNPJP
     * @param  $CNPJ
     * @return DOMElement
     */
    public function tagContratante(
        $CPF = '',
        $CNPJ = ''
    )
    {
        $infContratante = $this->dom->createElement('infContratante');
        $this->zAddChild(
            $infContratante,
            "CPF",
            $CPF,
            false,
            "Número do CPF do contratente do serviço"
        );
        $this->zAddChild(
            $infContratante,
            "CNPJ",
            $CNPJ,
            false,
            "Número do CNPJ do contratante do serviço"
        );
        $this->aContratante[] = $infContratante;
        return $infContratante;
    }

    /**
     * zTagVeiculo
     *
     * @param string $tag
     * @param string $cInt
     * @param string $placa
     * @param string $renavam
     * @param string $tara
     * @param string $capKG
     * @param string $capM3
     * @param string $propRNTRC
     * @param string $tpRod
     * @param string $tpCar
     * @param string $UF
     * @return DOMElement
     */
    protected function zTagVeiculo(
        $tag = '',
        $cInt = '',
        $placa = '',
        $renavam = '',
        $tara = '',
        $capKG = '',
        $capM3 = '',
        $CPF = '',
        $CNPJ = '',
        $propRNTRC = '',
        $xNome = '',
        $IE = '',
        $UFprop = '',
        $tpProp = '',
        $tpRod = '',
        $tpCar = '',
        $UF = ''
    )
    {
        $node = $this->dom->createElement($tag);
        $this->zAddChild(
            $node,
            "cInt",
            $cInt,
            false,
            "Código interno do veículo"
        );
        $this->zAddChild(
            $node,
            "placa",
            $placa,
            true,
            "Placa do veículo"
        );
        $this->zAddChild(
            $node,
            "RENAVAM",
            $renavam,
            false,
            "RENAVAM do veículo"
        );
        $this->zAddChild(
            $node,
            "tara",
            $tara,
            true,
            "Tara em KG"
        );
        if (floatval($capKG) > 0) {
            $this->zAddChild(
                $node,
                "capKG",
                $capKG,
                false,
                "Capacidade em KG"
            );
        }
        if (floatval($capM3) > 0) {
            $this->zAddChild(
                $node,
                "capM3",
                $capM3,
                false,
                "Capacidade em M3"
            );
        }
        if ($propRNTRC != '') {
            $prop = $this->dom->createElement("prop");
            if ($CPF != '') {
                $this->zAddChild(
                    $prop,
                    "CPF",
                    $CPF,
                    true,
                    "Numero do CPF"
                );
            } else {
                $this->zAddChild(
                    $prop,
                    "CNPJ",
                    $CNPJ,
                    true,
                    "Numero do CNPJ"
                );
            }
            $this->zAddChild(
                $prop,
                "RNTRC",
                $propRNTRC,
                true,
                "Registro Nacional dos Transportadores Rodoviários de Carga"
            );
            $this->zAddChild(
                $prop,
                "xNome",
                $xNome,
                true,
                "Razão Social ou Nome do Proprietário"
            );
            $this->zAddChild(
                $prop,
                "IE",
                $IE,
                false,
                "Inscrição Estadual"
            );
            $this->zAddChild(
                $prop,
                "UF",
                $UFprop,
                true,
                "UF"
            );
            $this->zAddChild(
                $prop,
                "tpProp",
                $tpProp,
                true,
                "Tipo Proprietário"
            );
            $this->zAppChild($node, $prop, '');
        }
        $this->zAddChild(
            $node,
            "tpRod",
            $tpRod,
            false,
            "Tipo de Rodado"
        );
        $this->zAddChild(
            $node,
            "tpCar",
            $tpCar,
            false,
            "Tipo de Carroceria"
        );
        $this->zAddChild(
            $node,
            "UF",
            $UF,
            false,
            "UF em que veículo está licenciado"
        );
        return $node;
    }

    /**
     * zTagMDFe
     * Tag raiz da MDFe
     * tag MDFe DOMNode
     * Função chamada pelo método [ monta ]
     *
     * @return DOMElement
     */
    protected function zTagMDFe()
    {
        if (empty($this->MDFe)) {
            $this->MDFe = $this->dom->createElement("MDFe");
            $this->MDFe->setAttribute("xmlns", "http://www.portalfiscal.inf.br/mdfe");
        }
        return $this->MDFe;
    }

    /**
     * Adiciona as tags
     * infMunCarrega e infPercurso
     * a tag ide
     */
    protected function zTagIde()
    {
        $this->zAddArrayChild($this->ide, $this->aInfMunCarrega);
        $this->zAddArrayChild($this->ide, $this->aInfPercurso);
    }

    /**
     * Processa lacres
     */
    protected function zTagLacres()
    {
        $this->zAddArrayChild($this->infMDFe, $this->aLacres);
    }

    /**
     * Proecessa documentos fiscais
     */
    protected function zTagInfDoc()
    {
        $this->aCountDoc = array('CTe' => 0, 'CT' => 0, 'NFe' => 0, 'NF' => 0);
        if (!empty($this->aInfMunDescarga)) {
            $infDoc = $this->dom->createElement("infDoc");
            foreach ($this->aInfMunDescarga as $nItem => $node) {
                $this->aCountDoc['CTe'] = $this->zAddArrayChild($node, $this->aInfCTe[$nItem]);
                $this->aCountDoc['CT'] = $this->zAddArrayChild($node, $this->aInfCT[$nItem]);
                $this->aCountDoc['NFe'] = $this->zAddArrayChild($node, $this->aInfNFe[$nItem]);
                $this->aCountDoc['NF'] = $this->zAddArrayChild($node, $this->aInfNF[$nItem]);
                $this->zAppChild($infDoc, $node, '');
            }
            $this->zAppChild($this->infMDFe, $infDoc, 'Falta tag "infModal"');
        }
    }

    /**
     * Processa modal rodoviario
     */
    protected function zTagRodo()
    {

        $this->rodo = $this->dom->createElement('rodo');
        $this->rodo->setAttribute("xmlns", 'http://www.portalfiscal.inf.br/mdfe');
        if (!empty($this->infANTT)) {
            $this->zAddArrayChild($this->infANTT, $this->aCIOT);
            if (!empty($this->aDisp)) {
                $valePed = $this->dom->createElement("valePed");
                foreach ($this->aDisp as $node) {
                    $this->zAppChild($valePed, $node);
                }
                $this->zAppChild($this->infANTT, $valePed, 'Falta tag "infANTT"');
            }
            $this->zAddArrayChild($this->infANTT, $this->aContratante);
            $this->zAppChild($this->rodo, $this->infANTT, 'Falta tag "rodo"');
        }
        foreach ($this->aCondutor as $child) {
            $this->zAppChildBefore($this->veicPrincipal, $child, 'tpRod');
        }
        $this->zAppChild($this->rodo, $this->veicPrincipal, 'Falta tag "rodo"');
        $this->zAddArrayChild($this->rodo, $this->aReboque);
        $this->zAppChild($this->infModal, $this->rodo, 'Falta tag "infModal"');
    }

    /**
     * Proecessa modal ferroviario
     */
    protected function zTagFerrov()
    {
        if (!empty($this->trem)) {
            $this->zAddArrayChild($this->trem, $this->aVag);
            $ferrov = $this->dom->createElement("ferrov");
            $this->zAppChild($ferrov, $this->trem);
            $this->zAppChild($this->infModal, $ferrov, 'Falta tag "infModal"');
        }
    }

    public function tagSeg(
        $respSeg = '',
        $CNPJ = '',
        $CPF = '',
        $xSeg = '',
        $CNPJSeg = '',
        $nApol = '',
        $nAver = ''
    )
    {
        $seg = $this->dom->createElement('seg');
        $identificador = 'infResp - ';
        $infResp = $this->dom->createElement("infResp");
        $this->zAddChild($infResp, "respSeg", $respSeg, true, $identificador . "Responsável pelo seguro");
        if ($respSeg == '2') {
            if ($CNPJ != "") {
                $this->zAddChild($infResp, "CNPJ", $CNPJ, true, $identificador . "Número do CNPJ do responsável pelo seguro");
            } else {
                $this->zAddChild($infResp, "CPF", $CPF, true, $identificador . "Número do CPF do responsável pelo seguro");
            }
        }
        $this->zAppChild($seg, $infResp);
        if ($xSeg != '') {
            $identificador = 'infSeg - ';
            $infSeg = $this->dom->createElement("infSeg");
            $this->zAddChild($infSeg, "xSeg", $xSeg, true, $identificador . "Nome da Seguradora");
            $this->zAddChild($infSeg, "CNPJ", $CNPJSeg, true, $identificador . "Número do CNPJ da seguradora");
            $this->zAppChild($seg, $infSeg);
        }
        $this->zAddChild($seg, "nApol", $nApol, false, $identificador . "Número da Apólice");
        $this->zAddChild($seg, "nAver", $nAver, false, $identificador . "Número da Averbação");
        $this->aSeg[] = $seg;
    }

    /**
     * Processa modal aereo
     */
    protected function zTagAereo()
    {
        if (!empty($this->aereo)) {
            $this->zAppChild($this->infModal, $this->aereo, 'Falta tag "infModal"');
        }
    }

    /**
     * Processa modal aquaviário
     */
    protected function zTagAqua()
    {
        if (!empty($this->aqua)) {
            $this->zAddArrayChild($this->aqua, $this->aInfTermCarreg);
            $this->zAddArrayChild($this->aqua, $this->aInfTermDescarreg);
            $this->zAddArrayChild($this->aqua, $this->aInfEmbComb);
            $this->zAppChild($this->infModal, $this->aqua, 'Falta tag "infModal"');
        }
    }

    private function zAddChild(&$parent, $name, $content = '', $obrigatorio = false, $descricao = "", $force = false)
    {
        if ($obrigatorio && $content === '' && !$force) {
            $this->erros[] = array(
                "tag" => $name,
                "desc" => $descricao,
                "erro" => "Preenchimento Obrigatório!"
            );
        }
        if ($obrigatorio || $content !== '') {
            $content = trim($content);
            $temp = $this->dom->createElement($name, $content);
            $parent->appendChild($temp);
        }
    }

    private function zAppChild(&$parent, $child, $mensagem = '')
    {
        if (empty($parent)) {
            throw new \Exception($mensagem);
        }
        if (!empty($child)) {
            $parent->appendChild($child);
        }
    }

    public function zAppChildBefore(&$parent, $child, $before, $msg = '')
    {
        if (empty($parent)) {
            throw new \InvalidArgumentException($msg);
        }
        $bnode = $parent->getElementsByTagName($before)->item(0);
        if (!empty($child) && !empty($bnode)) {
            $parent->insertBefore($child, $bnode);
        }
    }

    public function zAddArrayChild(&$parent, $arr)
    {
        $num = 0;
        if (!empty($arr) && !empty($parent)) {
            foreach ($arr as $node) {
                $this->zAppChild($parent, $node, '');
                $num++;
            }
        }
        return $num;
    }

}