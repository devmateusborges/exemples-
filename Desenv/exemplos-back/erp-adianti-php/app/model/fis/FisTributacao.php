<?php

class FisTributacao extends GenericRecord
{

    const LOG_USER = true;
    const LOG_TAB = true;
    const UNITFIELD = 'unit_id';

    const TABLENAME = 'fis_tributacao';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $fis_tributo;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('fis_tributo_id');
        parent::addAttribute('mov_id');
        parent::addAttribute('mov_itemserv_id');
        parent::addAttribute('cst');
        parent::addAttribute('modalidade_base_calc');
        parent::addAttribute('valor_base_calc');
        parent::addAttribute('perc_aliquota');
        parent::addAttribute('valor_imposto');
        parent::addAttribute('valor_base_calc_isento');
        parent::addAttribute('perc_aliquota_isento');
        parent::addAttribute('valor_imposto_insento');
        parent::addAttribute('valor_base_calc_st');
        parent::addAttribute('margem_agregada_st');
        parent::addAttribute('perc_aliquota_st');
        parent::addAttribute('valor_imposto_st');
        parent::addAttribute('perc_reducao_base_calc');
        parent::addAttribute('observacao');
        parent::addAttribute('valor_imposto_operacao');
        parent::addAttribute('valor_imposto_diferido');
        parent::addAttribute('perc_credito_sn');
        parent::addAttribute('valor_credito_sn');
        parent::addAttribute('valor_base_calc_fcp');
        parent::addAttribute('perc_aliquota_fcp');
        parent::addAttribute('valor_imposto_fcp');
        parent::addAttribute('valor_base_calc_fcp_st');
        parent::addAttribute('perc_aliquota_fcp_st');
        parent::addAttribute('valor_imposto_fcp_st');

        parent::addAttribute('valor_icms_desonerado');
        parent::addAttribute('motivo_icms_desonerado');
        parent::addAttribute('mod_base_calc_st');
        parent::addAttribute('perc_red_base_calc');
        parent::addAttribute('perc_fundo_comb_pob');
        parent::addAttribute('valor_fundo_comb_pob');
        parent::addAttribute('valor_base_calc_fundo_comb_pob');
        parent::addAttribute('valor_base_calc_st_fundo_comb_pob');
        parent::addAttribute('perc_st_fundo_comb_pob');
        parent::addAttribute('valor_st_fundo_comb_pob');
        parent::addAttribute('valor_base_calc_st_ret');
        parent::addAttribute('perc_aliquota_st');
        parent::addAttribute('valor_icms_st_ret');
        parent::addAttribute('valor_base_calc_fundo_comb_pob_st_ret');
        parent::addAttribute('perc_aliquota_fundo_comb_pob_st_ret');
        parent::addAttribute('valor_fundo_comb_pob_st_ret');
        parent::addAttribute('perc_aliquota_red_base_calc_efetiva');
        parent::addAttribute('valor_base_calc_efetiva');
        parent::addAttribute('perc_aliquota_icms_efetiva');
        parent::addAttribute('valor_icms_efetiva');
        parent::addAttribute('valor_icms_substituto');
        parent::addAttribute('perc_aliquota_credito');
        parent::addAttribute('valor_credito_icms');
    }

    public function get_fis_tributo()
    {
        if (empty($this->fis_tributo)) {
            $this->fis_tributo = new FisTributo($this->fis_tributo_id);
        }
        return $this->fis_tributo;
    }

    public static function retornaImposto($impostos, $_prTributo)
    {
        foreach ($impostos as $imposto) {
            if (in_array($imposto->fis_tributo->nr_tributo, $_prTributo)) {
                return $imposto;
            }
        }
        return false;
    }

    public static function processaImpostos($_prImpostos, $_prNItem, $_prRegimeEmpresa)
    {
        $impostos = simplexml_load_string($_prImpostos);
        $origem = 0;
        $vICMS = 0;
        $vST = 0;
        $vFCPST = 0;
        $vIPI = 0;
        $ICMS = new stdClass();
        $ICMS->tributo = 1;
        $IPI = new stdClass();
        $IPI->tributo = 2;
        $PIS = new stdClass();
        $PIS->tributo = 9;
        $COFINS = new stdClass();
        $COFINS->tributo = 10;
        // IPI
        if (!empty($impostos->IPI->IPITrib)) {
            $IPI->CST = (string)$impostos->IPI->IPITrib->CST;
            $IPI->valorImposto = (float)$impostos->IPI->IPITrib->vIPI;
            $IPI->valorBaseCalculo = (float)$impostos->IPI->IPITrib->vBC;
            $IPI->percencualAliquota = (float)$impostos->IPI->IPITrib->pIPI;
            $vIPI = (float)$impostos->IPI->IPITrib->vIPI;
        } else if (!empty($impostos->IPI->IPINT)) {
            $IPI->CST = (string)$impostos->IPI->IPINT->CST;
            $IPI->valorImposto = 0;
            $IPI->valorBaseCalculo = 0;
            $IPI->percencualAliquota = 0;
        }
        // PIS
        if (!empty($impostos->PIS->PISAliq)) {
            $PIS->CST = (string)$impostos->PIS->PISAliq->CST;
            $PIS->valorImposto = (float)$impostos->PIS->PISAliq->vPIS;
            $PIS->valorBaseCalculo = (float)$impostos->PIS->PISAliq->vBC;
            $PIS->percencualAliquota = (float)$impostos->PIS->PISAliq->pPIS;
        } else if (!empty($impostos->PIS->PISQtde)) {
            $PIS->CST = (string)$impostos->PIS->PISQtde->CST;
            $PIS->valorImposto = (float)$impostos->PIS->PISQtde->vPIS;
            $PIS->percencualAliquota = (float)$impostos->PIS->PISQtde->vAliqProd;
        } else if (!empty($impostos->PIS->PISNT)) {
            $PIS->CST = (string)$impostos->PIS->PISNT->CST;
            $PIS->valorImposto = 0;
            $PIS->valorBaseCalculo = 0;
            $PIS->percencualAliquota = 0;
        } else if (!empty($impostos->PIS->PISOutr)) {
            $PIS->CST = (string)$impostos->PIS->PISOutr->CST;
            $PIS->valorImposto = (float)$impostos->PIS->PISOutr->vPIS;
            $PIS->valorBaseCalculo = (float)$impostos->PIS->PISOutr->vBC;
            $PIS->percencualAliquota = (float)$impostos->PIS->PISOutr->pPIS;
        }
        // COFINS
        if (!empty($impostos->COFINS->COFINSAliq)) {
            $COFINS->CST = (string)$impostos->COFINS->COFINSAliq->CST;
            $COFINS->valorImposto = (float)$impostos->COFINS->COFINSAliq->vCOFINS;
            $COFINS->valorBaseCalculo = (float)$impostos->COFINS->COFINSAliq->vBC;
            $COFINS->percencualAliquota = (float)$impostos->COFINS->COFINSAliq->pCOFINS;
        } else if (!empty($impostos->COFINS->COFINSQtde)) {
            $COFINS->CST = (string)$impostos->COFINS->COFINSQtde->CST;
            $COFINS->valorImposto = (float)$impostos->COFINS->COFINSQtde->vCOFINS;
            $COFINS->percencualAliquota = (float)$impostos->COFINS->COFINSQtde->vAliqProd;
        } else if (!empty($impostos->COFINS->COFINSNT)) {
            $COFINS->CST = (string)$impostos->COFINS->COFINSNT->CST;
        } else if (!empty($impostos->COFINS->COFINSOutr)) {
            $COFINS->CST = (string)$impostos->COFINS->COFINSOutr->CST;
            $COFINS->valorImposto = (float)$impostos->COFINS->COFINSOutr->vCOFINS;
            $COFINS->valorBaseCalculo = (float)$impostos->COFINS->COFINSOutr->vBC;
            $COFINS->percencualAliquota = (float)$impostos->COFINS->COFINSOutr->pCOFINS;
        }
        // ICMS
        if (!empty($impostos->ICMS->ICMS00)) {
            $origem = (int)$impostos->ICMS->ICMS00->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMS00->CST;
            $ICMS->valorImposto = (float)$impostos->ICMS->ICMS00->vICMS;
            $ICMS->valorBaseCalculo = (float)$impostos->ICMS->ICMS00->vBC;
            $ICMS->percencualAliquota = (float)$impostos->ICMS->ICMS00->pICMS;
            $vICMS = (float)$impostos->ICMS->ICMS00->vICMS;
        } else if (!empty($impostos->ICMS->ICMS10)) {
            $origem = (int)$impostos->ICMS->ICMS10->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMS10->CST;
            $ICMS->valorImposto = (float)$impostos->ICMS->ICMS10->vICMS;
            $ICMS->valorBaseCalculo = (float)$impostos->ICMS->ICMS10->vBC;
            $ICMS->percencualAliquota = (float)$impostos->ICMS->ICMS10->pICMS;
            $vICMS = (float)$impostos->ICMS->ICMS10->vICMS;
            if (!empty($impostos->ICMS->ICMS10->vICMSST)) {
                $ICMS->percentualMargemValorAgregado = (float)$impostos->ICMS->ICMS10->pMVAST;
                $ICMS->percentualReducaoBaseCalculo = (float)$impostos->ICMS->ICMS10->pRedBCST;
                $ICMS->valorReducaoBaseCalculo = (float)$impostos->ICMS->ICMS10->vBCST;
                $ICMS->percentualST = (float)$impostos->ICMS->ICMS10->pICMSST;
                $ICMS->valorST = (float)$impostos->ICMS->ICMS10->vICMSST;
                $vST = (float)$impostos->ICMS->ICMS10->vICMSST;
                $ICMS->tributo = 5;
            }
            if (!empty($impostos->ICMS->ICMS10->vFCPST)) {
                $ICMS->valorBaseCalculoFCPST = (float)$impostos->ICMS->ICMS10->vBCFCPST;
                $ICMS->percencualAliquotaFCPST = (float)$impostos->ICMS->ICMS10->pFCPST;
                $ICMS->valorFCPST = (float)$impostos->ICMS->ICMS10->vFCPST;
                $vFCPST = (float)$impostos->ICMS->ICMS10->vFCPST;
            }
        } else if (!empty($impostos->ICMS->ICMS20)) {
            $origem = (int)$impostos->ICMS->ICMS20->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMS20->CST;
            $ICMS->valorImposto = (float)$impostos->ICMS->ICMS20->vICMS;
            $ICMS->valorBaseCalculo = (float)$impostos->ICMS->ICMS20->vBC;
            $ICMS->percencualAliquota = (float)$impostos->ICMS->ICMS20->pICMS;
            $ICMS->percentualReducaoBaseCalculo = (float)$impostos->ICMS->ICMS20->pRedBCST;
            $vICMS = (float)$impostos->ICMS->ICMS20->vICMS;
        } else if (!empty($impostos->ICMS->ICMS30)) {
            $origem = (int)$impostos->ICMS->ICMS30->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMS30->CST;
            $ICMS->percentualMargemValorAgregado = (float)$impostos->ICMS->ICMS30->pMVAST;
            $ICMS->percentualReducaoBaseCalculo = (float)$impostos->ICMS->ICMS30->pRedBCST;
            $ICMS->valorReducaoBaseCalculo = (float)$impostos->ICMS->ICMS30->vBCST;
            $ICMS->percentualST = (float)$impostos->ICMS->ICMS30->pICMSST;
            $ICMS->valorST = (float)$impostos->ICMS->ICMS30->vICMSST;
            $vST = (float)$impostos->ICMS->ICMS30->vICMSST;
            $ICMS->tributo = 5;
            if (!empty($impostos->ICMS->ICMS30->vFCPST)) {
                $ICMS->valorBaseCalculoFCPST = (float)$impostos->ICMS->ICMS30->vBCFCPST;
                $ICMS->percencualAliquotaFCPST = (float)$impostos->ICMS->ICMS30->pFCPST;
                $ICMS->valorFCPST = (float)$impostos->ICMS->ICMS30->vFCPST;
                $vFCPST = (float)$impostos->ICMS->ICMS30->vFCPST;
            }
        } else if (!empty($impostos->ICMS->ICMS40)) {
            $origem = (int)$impostos->ICMS->ICMS40->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMS40->CST;
            $ICMS->valorImposto = (float)$impostos->ICMS->ICMS40->vICMSDeson;
        } else if (!empty($impostos->ICMS->ICMS51)) {
            $origem = (int)$impostos->ICMS->ICMS51->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMS51->CST;
            $ICMS->valorImposto = (float)$impostos->ICMS->ICMS51->vICMS;
            $ICMS->valorBaseCalculo = (float)$impostos->ICMS->ICMS51->vBC;
            $ICMS->percencualAliquota = (float)$impostos->ICMS->ICMS51->pICMS;
            $ICMS->percentualReducaoBaseCalculo = (float)$impostos->ICMS->ICMS51->pRedBC;
            $vICMS = (float)$impostos->ICMS->ICMS51->vICMS;
        } else if (!empty($impostos->ICMS->ICMS60)) {
            $origem = (int)$impostos->ICMS->ICMS60->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMS60->CST;
            $ICMS->valorReducaoBaseCalculo = (float)$impostos->ICMS->ICMS60->vBCSTRet;
            $ICMS->percentualST = (float)$impostos->ICMS->ICMS60->pST;
            $ICMS->valorST = (float)$impostos->ICMS->ICMS60->vICMSSTRet;
            $ICMS->valorImposto = (float)$impostos->ICMS->ICMS60->vICMSSubstituto;
            $ICMS->tributo = 5;
        } else if (!empty($impostos->ICMS->ICMS70)) {
            $origem = (int)$impostos->ICMS->ICMS70->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMS70->CST;
            $ICMS->valorImposto = (float)$impostos->ICMS->ICMS70->vICMS;
            $ICMS->valorBaseCalculo = (float)$impostos->ICMS->ICMS70->vBC;
            $ICMS->percencualAliquota = (float)$impostos->ICMS->ICMS70->pICMS;
            $vICMS = (float)$impostos->ICMS->ICMS70->vICMS;
            if (!empty($impostos->ICMS->ICMS70->vICMSST)) {
                $ICMS->percentualMargemValorAgregado = (float)$impostos->ICMS->ICMS70->pMVAST;
                $ICMS->percentualReducaoBaseCalculo = (float)$impostos->ICMS->ICMS70->pRedBCST;
                $ICMS->valorReducaoBaseCalculo = (float)$impostos->ICMS->ICMS70->vBCST;
                $ICMS->percentualST = (float)$impostos->ICMS->ICMS70->pICMSST;
                $ICMS->valorST = (float)$impostos->ICMS->ICMS70->vICMSST;
                $vST = (float)$impostos->ICMS->ICMS70->vICMSST;
                $ICMS->tributo = 5;
            }
            if (!empty($impostos->ICMS->ICMS70->vFCPST)) {
                $ICMS->valorBaseCalculoFCPST = (float)$impostos->ICMS->ICMS70->vBCFCPST;
                $ICMS->percencualAliquotaFCPST = (float)$impostos->ICMS->ICMS70->pFCPST;
                $ICMS->valorFCPST = (float)$impostos->ICMS->ICMS70->vFCPST;
                $vFCPST = (float)$impostos->ICMS->ICMS70->vFCPST;
            }
        } else if (!empty($impostos->ICMS->ICMS90)) {
            $origem = (int)$impostos->ICMS->ICMS90->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMS90->CST;
            $ICMS->valorImposto = (float)$impostos->ICMS->ICMS90->vICMS;
            $ICMS->valorBaseCalculo = (float)$impostos->ICMS->ICMS90->vBC;
            $ICMS->percencualAliquota = (float)$impostos->ICMS->ICMS90->pICMS;
            $vICMS = (float)$impostos->ICMS->ICMS90->vICMS;
            if (!empty($impostos->ICMS->ICMS90->vICMSST)) {
                $ICMS->percentualMargemValorAgregado = (float)$impostos->ICMS->ICMS90->pMVAST;
                $ICMS->percentualReducaoBaseCalculo = (float)$impostos->ICMS->ICMS90->pRedBCST;
                $ICMS->valorReducaoBaseCalculo = (float)$impostos->ICMS->ICMS90->vBCST;
                $ICMS->percentualST = (float)$impostos->ICMS->ICMS90->pICMSST;
                $ICMS->valorST = (float)$impostos->ICMS->ICMS90->vICMSST;
                $vST = (float)$impostos->ICMS->ICMS90->vICMSST;
            }
            if (!empty($impostos->ICMS->ICMS90->vFCPST)) {
                $ICMS->valorBaseCalculoFCPST = (float)$impostos->ICMS->ICMS90->vBCFCPST;
                $ICMS->percencualAliquotaFCPST = (float)$impostos->ICMS->ICMS90->pFCPST;
                $ICMS->valorFCPST = (float)$impostos->ICMS->ICMS90->vFCPST;
                $vFCPST = (float)$impostos->ICMS->ICMS90->vFCPST;
            }
        } else if (!empty($impostos->ICMS->ICMSSN101)) {
            $origem = (int)$impostos->ICMS->ICMSSN101->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMSSN101->CSOSN;
            $ICMS->valorImposto = (float)$impostos->ICMS->ICMSSN101->vCredICMSSN;
            $ICMS->percencualAliquota = (float)$impostos->ICMS->ICMSSN101->pCredSN;
            $vICMS = (float)$impostos->ICMS->ICMSSN101->vCredICMSSN;
        } else if (!empty($impostos->ICMS->ICMSSN102)) {
            $origem = (int)$impostos->ICMS->ICMSSN102->orig;
            $ICMS->CST = 90;
            $ICMS->valorImposto = 0;
            $ICMS->valorBaseCalculo = 0;
            $ICMS->percencualAliquota = 0;
        } else if (!empty($impostos->ICMS->ICMSSN201)) {
            $origem = (int)$impostos->ICMS->ICMSSN201->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMSSN201->CSOSN;
            $ICMS->percentualMargemValorAgregado = (float)$impostos->ICMS->ICMSSN201->pMVAST;
            $ICMS->valorReducaoBaseCalculo = (float)$impostos->ICMS->ICMSSN201->vBCST;
            $ICMS->percentualST = (float)$impostos->ICMS->ICMSSN201->pICMSST;
            $ICMS->valorST = (float)$impostos->ICMS->ICMSSN201->vICMSST;
            $vST = (float)$impostos->ICMS->ICMSSN201->vICMSST;
            if (!empty($impostos->ICMS->ICMSSN201->vFCPST)) {
                $ICMS->valorBaseCalculoFCPST = (float)$impostos->ICMS->ICMSSN201->vBCFCPST;
                $ICMS->percencualAliquotaFCPST = (float)$impostos->ICMS->ICMSSN201->pFCPST;
                $ICMS->valorFCPST = (float)$impostos->ICMS->ICMSSN201->vFCPST;
                $vFCPST = (float)$impostos->ICMS->ICMSSN201->vFCPST;
            }
        } else if (!empty($impostos->ICMS->ICMSSN202)) {
            $origem = (int)$impostos->ICMS->ICMSSN202->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMSSN202->CSOSN;
            $ICMS->percentualMargemValorAgregado = (float)$impostos->ICMS->ICMSSN202->pMVAST;
            $ICMS->valorReducaoBaseCalculo = (float)$impostos->ICMS->ICMSSN202->vBCST;
            $ICMS->percentualST = (float)$impostos->ICMS->ICMSSN202->pICMSST;
            $ICMS->valorST = (float)$impostos->ICMS->ICMSSN202->vICMSST;
            $vST = (float)$impostos->ICMS->ICMSSN202->vICMSST;
            if (!empty($impostos->ICMS->ICMSSN202->vFCPST)) {
                $ICMS->valorBaseCalculoFCPST = (float)$impostos->ICMS->ICMSSN202->vBCFCPST;
                $ICMS->percencualAliquotaFCPST = (float)$impostos->ICMS->ICMSSN202->pFCPST;
                $ICMS->valorFCPST = (float)$impostos->ICMS->ICMSSN202->vFCPST;
                $vFCPST = (float)$impostos->ICMS->ICMSSN202->vFCPST;
            }
        } else if (!empty($impostos->ICMS->ICMSSN500)) {
            $origem = (int)$impostos->ICMS->ICMSSN500->orig;
            $ICMS->CST = 90;
            $ICMS->valorReducaoBaseCalculo = (float)$impostos->ICMS->ICMSSN500->vBCSTRet;
            $ICMS->percentualST = (float)$impostos->ICMS->ICMSSN500->pST;
            $ICMS->valorST = (float)$impostos->ICMS->ICMSSN500->vICMSSTRet;
            $ICMS->valorImposto = (float)$impostos->ICMS->ICMSSN500->vICMSSubstituto;
        } else if (!empty($impostos->ICMS->ICMSSN900)) {
            $origem = (int)$impostos->ICMS->ICMSSN900->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMSSN900->CSOSN;
            $ICMS->percentualMargemValorAgregado = (float)$impostos->ICMS->ICMSSN900->pMVAST;
            $ICMS->percentualReducaoBaseCalculo = (float)$impostos->ICMS->ICMSSN900->pRedBCST;
            $ICMS->valorImposto = (float)$impostos->ICMS->ICMSSN900->vICMSST;
            $ICMS->valorBaseCalculo = (float)$impostos->ICMS->ICMSSN900->vBCST;
            $ICMS->percencualAliquota = (float)$impostos->ICMS->ICMSSN900->pICMSST;
            $vICMS = (float)$impostos->ICMS->ICMSSN900->vICMS;
            if (!empty($impostos->ICMS->ICMSSN900->vFCPST)) {
                $ICMS->valorFCPST = (float)$impostos->ICMS->ICMSSN900->vFCPST;
                $vFCPST = (float)$impostos->ICMS->ICMSSN900->vFCPST;
            }
        } else if (!empty($impostos->ICMS->ICMSST)) {
            $origem = (int)$impostos->ICMS->ICMSST->orig;
            $ICMS->CST = (string)$impostos->ICMS->ICMSST->CST;
        }
        // Converte o CST de Saida para Entrada
        $IPI->CSTOrig = $IPI->CST;
        $IPI->CST = self::converteCST($IPI->CST, 2, $_prRegimeEmpresa);
        $PIS->CSTOrig = $PIS->CST;
        $PIS->CST = self::converteCST($PIS->CST, 9, $_prRegimeEmpresa);
        $COFINS->CSTOrig = $COFINS->CST;
        $COFINS->CST = self::converteCST($COFINS->CST, 10, $_prRegimeEmpresa);
        $ICMS->CSTOrig = $ICMS->CST;
        $ICMS->CST = self::converteCST($ICMS->CST, 1, $_prRegimeEmpresa);
        if ($ICMS->CST == "") {
            throw new Exception(sprintf("Esse documento possui alguma exceção de ICMS que não foi implementado no item %s, entre em contato com o suporte.", $_prNItem));
        }
        return array(
            "valoripi" => $vIPI,
            "valorst" => $vST,
            "valorfcpst" => $vFCPST,
            "valoricms" => $vICMS,
            "origem" => $origem,
            "impostos" => array(
                "ICMS" => $ICMS,
                "IPI" => $IPI,
                "PIS" => $PIS,
                "COFINS" => $COFINS
            )
        );
    }

    private static function converteCST($_prCST, $_prTributo, $_prRegimeEmpresa)
    {
        if ($_prTributo == 2) {
            $cstIPI = array(
                "50" => "00",
                "51" => "01",
                "52" => "02",
                "53" => "03",
                "54" => "04",
                "55" => "05",
                "99" => "49"
            );
            return $cstIPI[$_prCST];
        } else if (in_array($_prTributo, array(9, 10))) {
            // CST saida para entrada
            $cstPISCOFINS = array(
                "01" => "50",
                "02" => "50",
                "03" => "50",
                "04" => "70",
                "05" => "75",
                "06" => "73",
                "07" => "71",
                "08" => "74",
                "09" => "72",
                "49" => "98"
            );
            return $cstPISCOFINS[$_prCST];
        } else if (in_array($_prTributo, array(1))) {
            $SN = (in_array(intval($_prRegimeEmpresa), array(1, 2)));
            if ($SN and intval($_prCST) < 100) {
                $cstICMSST = array(
                    "00" => "102",
                    "20" => "102",
                    "10" => "202",
                    "30" => "202",
                    "60" => "202",
                    "70" => "202",
                    "40" => "500",
                    "50" => "500",
                    "51" => "500",
                    "41" => "900",
                    "90" => "900"
                );
                return $cstICMSST[$_prCST];
            } else if (!$SN and intval($_prCST) > 100) {
                $cstICMSST = array(
                    "101" => "00",
                    "102" => "90",
                    "103" => "90",
                    "201" => "60",
                    "202" => "60",
                    "203" => "60",
                    "500" => "60",
                    "900" => "60"
                );
                return $cstICMSST[$_prCST];
            } else {
                return $_prCST;
            }
        }
        return $_prCST;
    }

}

?>