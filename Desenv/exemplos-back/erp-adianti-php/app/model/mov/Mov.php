<?php

class Mov extends GenericRecord
{

    const LOG_USER  = true;
    const LOG_TAB  = true;
    const UNITFIELD = 'unit_id';
 
    const TABLENAME = 'mov';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // {max, serial}

    private $ger_empresa;
    private $ger_pessoa;
    private $ger_pessoa_endereco_fiscal;
    private $ger_pessoa_endereco_entrega;
    private $mov_operacao;
    private $mov_tipo;
    private $mov_status;
    private $mov_itemserv;
    private $fis_doc;
    private $fis_doc_tipo;
    private $mov_ciot;
    private $mov_condutor;
    private $mov_entrega;
    private $mov_entrega_doc;
    private $mov_entrega_doc_ant;
    private $mov_lacre;
    private $mov_reboque;
    private $mov_seguradora;
    private $mov_tomador;
    private $mov_pedagio;
    private $ger_cidade_carreg;
    private $ger_cidade_descarreg;
    private $mov_percurso;
    private $ger_pessoa_endereco_reme;
    private $ger_pessoa_endereco_dest;
    private $ger_pessoa_endereco_rece;
    private $ger_pessoa_endereco_expe;
    private $mov_comp;
    private $mov_medida;
    private $mov_frete;
    private $fin_pagrec_origem;

    public function __construct($id = NULL, $callObjectLoad = TRUE)
    {
        parent::__construct($id, $callObjectLoad);
        parent::addAttribute('unit_id');
        parent::addAttribute('ger_empresa_id');
        parent::addAttribute('nr_externo');
        parent::addAttribute('ger_pessoa_id');
        parent::addAttribute('ger_pessoa_endereco_id_fiscal');
        parent::addAttribute('mov_operacao_id');
        parent::addAttribute('fin_cond_pagrec_id');
        parent::addAttribute('data_mov');
        parent::addAttribute('numero_mov');
        parent::addAttribute('data_emissao');
        parent::addAttribute('mov_tipo_id');
        parent::addAttribute('fis_doc_tipo_id');
        parent::addAttribute('serie_mov');
        parent::addAttribute('mov_status_id');
        parent::addAttribute('valor_total');
        parent::addAttribute('observacao');
        parent::addAttribute('tipo_frete');
        parent::addAttribute('data_entrega');
        parent::addAttribute('data_entrada_saida');
        parent::addAttribute('ger_pessoa_endereco_id_entrega');
        parent::addAttribute('ger_cidade_id_carreg');
        parent::addAttribute('ger_cidade_id_descarreg');
        parent::addAttribute('tipo_emissao_carga');
        parent::addAttribute('tipo_modal_carga');
        parent::addAttribute('tipo_transportador_carga');
        parent::addAttribute('valor_carga');
        parent::addAttribute('tipo_umedida_carga');
        parent::addAttribute('qnt_carga');
        parent::addAttribute('ger_pessoa_endereco_id_reme');
        parent::addAttribute('ger_pessoa_endereco_id_dest');
        parent::addAttribute('ger_pessoa_endereco_id_rece');
        parent::addAttribute('ger_pessoa_endereco_id_expe');
        parent::addAttribute('observacao_transp');
        parent::addAttribute('observacao_serv');
        parent::addAttribute('tipo_fretamento');
        parent::addAttribute('tipo_serv_frete');
        parent::addAttribute('tipo_tomador_serv_frete');
        parent::addAttribute('taf');
        parent::addAttribute('data_anulacao');
        parent::addAttribute('observacao_item');
        parent::addAttribute('valor_financeiro_total');
        parent::addAttribute('valor_item_frete_total');
    }

    public function get_ger_empresa()
    {
        if (empty($this->ger_empresa)) {
            $this->ger_empresa = new GerEmpresa($this->ger_empresa_id);
        }
        return $this->ger_empresa;
    }

    public function get_ger_pessoa()
    {
        if (empty($this->ger_pessoa)) {
            $this->ger_pessoa = new GerPessoa($this->ger_pessoa_id);
        }
        return $this->ger_pessoa;
    }

    public function get_ger_pessoa_endereco_fiscal()
    {
        if (empty($this->ger_pessoa_endereco_fiscal)) {
            $this->ger_pessoa_endereco_fiscal = new GerPessoaEndereco($this->ger_pessoa_endereco_id_fiscal);
        }
        return $this->ger_pessoa_endereco_fiscal;
    }

    public function get_ger_pessoa_endereco_entrega()
    {
        if (empty($this->ger_pessoa_endereco_entrega)) {
            $this->ger_pessoa_endereco_entrega = new GerPessoaEndereco($this->ger_pessoa_endereco_id_entrega);
        }
        return $this->ger_pessoa_endereco_entrega;
    }

    public function get_mov_operacao()
    {
        if (empty($this->mov_operacao)) {
            $this->mov_operacao = new MovOperacao($this->mov_operacao_id);
        }
        return $this->mov_operacao;
    }

    public function get_mov_tipo()
    {
        if (empty($this->mov_tipo)) {
            $this->mov_tipo = new MovTipo($this->mov_tipo_id);
        }
        return $this->mov_tipo;
    }

    public function get_mov_status()
    {
        if (empty($this->mov_status)) {
            $this->mov_status = new MovStatus($this->mov_status_id);
        }
        return $this->mov_status;
    }

    public function get_mov_itemserv()
    {
        if (empty($this->mov_itemserv)) {
            $this->mov_itemserv = Mov::find($this->id)->hasMany('MovItemServ');
        }
        return $this->mov_itemserv;
    }

    public function get_fis_doc()
    {
        if (empty($this->fis_doc)) {
            $fisDoc = FisDoc::where('mov_id', '=', $this->id);
            if ($fisDoc->count() > 0) {
                $this->fis_doc = $fisDoc->first();
            }
        }
        return $this->fis_doc;
    }

    public function get_fis_doc_tipo()
    {
        if (empty($this->fis_doc_tipo)) {
            $this->fis_doc_tipo = new FisDocTipo($this->fis_doc_tipo_id);
        }
        return $this->fis_doc_tipo;
    }

    public function get_mov_origem()
    {
        $criteria = new TCriteria;
        $criteria->add(new TFilter('mov_id', '=', $this->id));
        $repository = new TRepository('MovOrigem');
        $origem = $repository->load($criteria);
        return $origem[0];
    }

    public function get_mov_ciot()
    {
        if (empty($this->mov_ciot)) {
            $this->mov_ciot = Mov::find($this->id)->hasMany('MovCiot');
        }
        return $this->mov_ciot;
    }

    public function get_mov_condutor()
    {
        if (empty($this->mov_condutor)) {
            $this->mov_condutor = Mov::find($this->id)->hasMany('MovCondutor');
        }
        return $this->mov_condutor;
    }

    public function get_mov_entrega()
    {
        if (empty($this->mov_entrega)) {
            $this->mov_entrega = Mov::find($this->id)->hasMany('MovEntrega');
        }
        return $this->mov_entrega;
    }

    public function get_mov_entrega_doc()
    {
        if (empty($this->mov_entrega_doc)) {
            $this->mov_entrega_doc = Mov::find($this->id)->hasMany('MovEntregaDoc');
        }
        return $this->mov_entrega_doc;
    }

    public function get_mov_entrega_doc_ant()
    {
        if (empty($this->mov_entrega_doc_ant)) {
            $criteria = new TCriteria;
            $criteria->add(new TFilter('mov_id', '=', $this->id));
            $criteria->add(new TFilter('modelo_documento', '=', '57'));
            $repository = new TRepository('MovEntregaDoc');
            $this->mov_entrega_doc_ant = $repository->load($criteria);
        }
        return $this->mov_entrega_doc_ant;
    }

    public function get_mov_lacre()
    {
        if (empty($this->mov_lacre)) {
            $this->mov_lacre = Mov::find($this->id)->hasMany('MovLacre');
        }
        return $this->mov_lacre;
    }

    public function get_mov_reboque()
    {
        if (empty($this->mov_reboque)) {
            $this->mov_reboque = Mov::find($this->id)->hasMany('MovReboque');
        }
        return $this->mov_reboque;
    }

    public function get_mov_seguradora()
    {
        if (empty($this->mov_seguradora)) {
            $this->mov_seguradora = Mov::find($this->id)->hasMany('MovSeguradora');
        }
        return $this->mov_seguradora;
    }

    public function get_mov_tomador()
    {
        if (empty($this->mov_tomador)) {
            $this->mov_tomador = Mov::find($this->id)->hasMany('MovTomador');
        }
        return $this->mov_tomador;
    }

    public function get_mov_pedagio()
    {
        if (empty($this->mov_pedagio)) {
            $this->mov_pedagio = Mov::find($this->id)->hasMany('MovPedagio');
        }
        return $this->mov_pedagio;
    }

    public function get_ger_cidade_carreg()
    {
        if (empty($this->ger_cidade_carreg)) {
            $this->ger_cidade_carreg = new GerCidade($this->ger_cidade_id_carreg);
        }
        return $this->ger_cidade_carreg;
    }

    public function get_ger_cidade_descarreg()
    {
        if (empty($this->ger_cidade_descarreg)) {
            $this->ger_cidade_descarreg = new GerCidade($this->ger_cidade_id_descarreg);
        }
        return $this->ger_cidade_descarreg;
    }

    public function get_mov_percurso()
    {
        if (empty($this->mov_percurso)) {
            $this->mov_percurso = Mov::find($this->id)->hasMany('MovPercurso');
        }
        return $this->mov_percurso;
    }

    public function get_ger_pessoa_endereco_reme()
    {
        if (empty($this->ger_pessoa_endereco_reme)) {
            $this->ger_pessoa_endereco_reme = new GerPessoaEndereco($this->ger_pessoa_endereco_id_reme);
        }
        return $this->ger_pessoa_endereco_reme;
    }

    public function get_ger_pessoa_endereco_dest()
    {
        if (empty($this->ger_pessoa_endereco_dest)) {
            $this->ger_pessoa_endereco_dest = new GerPessoaEndereco($this->ger_pessoa_endereco_id_dest);
        }
        return $this->ger_pessoa_endereco_dest;
    }

    public function get_ger_pessoa_endereco_rece()
    {
        if (empty($this->ger_pessoa_endereco_rece)) {
            $this->ger_pessoa_endereco_rece = new GerPessoaEndereco($this->ger_pessoa_endereco_id_rece);
        }
        return $this->ger_pessoa_endereco_rece;
    }

    public function get_ger_pessoa_endereco_expe()
    {
        if (empty($this->ger_pessoa_endereco_expe)) {
            $this->ger_pessoa_endereco_expe = new GerPessoaEndereco($this->ger_pessoa_endereco_id_expe);
        }
        return $this->ger_pessoa_endereco_expe;
    }

    public function get_mov_comp()
    {
        if (empty($this->mov_comp)) {
            $this->mov_comp = Mov::find($this->id)->hasMany('MovComp');
        }
        return $this->mov_comp;
    }

    public function get_mov_medida()
    {
        if (empty($this->mov_medida)) {
            $this->mov_medida = Mov::find($this->id)->hasMany('MovMedida');
        }
        return $this->mov_medida;
    }

    public function get_mov_frete()
    {
        if (empty($this->mov_frete)) {
            $this->mov_frete = Mov::find($this->id)->hasMany('MovFrete');
        }
        return $this->mov_frete;
    }

    public function get_fin_pagrec_origem()
    {
        if (empty($this->fin_pagrec_origem)) {
            $this->fin_pagrec_origem = Mov::find($this->id)->hasMany('FinPagRecOrigem');
        }
        return $this->fin_pagrec_origem;
    }

}

?>