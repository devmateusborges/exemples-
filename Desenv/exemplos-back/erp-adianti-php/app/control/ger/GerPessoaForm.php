<?php

class GerPessoaForm extends TPage
{
    protected $form;
    private $formFields = [];
    private static $activeRecord = 'GerPessoa';
    private static $primaryKey = 'id';
    private static $formName = 'form_GerPessoa';

    use Adianti\Base\AdiantiMasterDetailTrait;

    /**
     * Form constructor
     * @param $param Request
     */
    public function __construct( $param )
    {
        parent::__construct();

        // creates the form
        $this->form = new BootstrapFormBuilder(self::$formName);
        // define the form title
        $this->form->setFormTitle("GerPessoaForm");


        $id = new TEntry('id');
        $nome = new TEntry('nome');
        $razao_social = new TEntry('razao_social');
        $ativo = new TCombo('ativo');
        $data_abertura = new TDate('data_abertura');
        $contato_1 = new TEntry('contato_1');
        $fone_1 = new TEntry('fone_1');
        $contato_2 = new TEntry('contato_2');
        $fone_2 = new TEntry('fone_2');
        $contato_3 = new TEntry('contato_3');
        $fone_3 = new TEntry('fone_3');
        $ger_pessoa_endereco_ger_pessoa_ativo = new TCombo('ger_pessoa_endereco_ger_pessoa_ativo');
        $ger_pessoa_endereco_ger_pessoa_tipo = new TCombo('ger_pessoa_endereco_ger_pessoa_tipo');
        $ger_pessoa_endereco_ger_pessoa_padrao = new TCombo('ger_pessoa_endereco_ger_pessoa_padrao');
        $ger_pessoa_endereco_ger_pessoa_end_logradouro = new TEntry('ger_pessoa_endereco_ger_pessoa_end_logradouro');
        $ger_pessoa_endereco_ger_pessoa_end_logradouro_nr = new TEntry('ger_pessoa_endereco_ger_pessoa_end_logradouro_nr');
        $ger_pessoa_endereco_ger_pessoa_end_bairro = new TEntry('ger_pessoa_endereco_ger_pessoa_end_bairro');
        $ger_pessoa_endereco_ger_pessoa_end_complemento = new TEntry('ger_pessoa_endereco_ger_pessoa_end_complemento');
        $ger_pessoa_endereco_ger_pessoa_end_cep = new TEntry('ger_pessoa_endereco_ger_pessoa_end_cep');
        $ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id = new TDBCombo('ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id', TSession::getValue('pConn'), 'GerCidade', 'id', '{id}','id asc'  );
        $ger_pessoa_endereco_ger_pessoa_email = new TEntry('ger_pessoa_endereco_ger_pessoa_email');
        $ger_pessoa_endereco_ger_pessoa_contato = new TEntry('ger_pessoa_endereco_ger_pessoa_contato');
        $ger_pessoa_endereco_ger_pessoa_fone = new TEntry('ger_pessoa_endereco_ger_pessoa_fone');
        $ger_pessoa_conta_banco_ger_pessoa_fin_banco_id = new TDBCombo('ger_pessoa_conta_banco_ger_pessoa_fin_banco_id', TSession::getValue('pConn'), 'FinBanco', 'id', '{id}','id asc'  );
        $ger_pessoa_conta_banco_ger_pessoa_agencia = new TEntry('ger_pessoa_conta_banco_ger_pessoa_agencia');
        $ger_pessoa_conta_banco_ger_pessoa_conta = new TEntry('ger_pessoa_conta_banco_ger_pessoa_conta');
        $ger_pessoa_conta_banco_ger_pessoa_observacao = new TEntry('ger_pessoa_conta_banco_ger_pessoa_observacao');
        $doc_cpf = new TEntry('doc_cpf');
        $doc_cnpj = new TEntry('doc_cnpj');
        $doc_im = new TEntry('doc_im');
        $doc_ie = new TEntry('doc_ie');
        $nr_rntrc = new TEntry('nr_rntrc');
        $doc_junta = new TEntry('doc_junta');
        $doc_rg = new TEntry('doc_rg');
        $doc_rg_org_exp = new TEntry('doc_rg_org_exp');
        $doc_crc = new TEntry('doc_crc');
        $doc_crc_seq = new TEntry('doc_crc_seq');
        $doc_crc_org_exp = new TEntry('doc_crc_org_exp');
        $doc_cnae = new TEntry('doc_cnae');
        $fis_regime = new TEntry('fis_regime');
        $contrib_icms = new TEntry('contrib_icms');
        $ger_pessoa_endereco_ger_pessoa_id = new THidden('ger_pessoa_endereco_ger_pessoa_id');
        $ger_pessoa_conta_banco_ger_pessoa_id = new THidden('ger_pessoa_conta_banco_ger_pessoa_id');

        $nome->addValidation("Nome", new TRequiredValidator()); 
        $razao_social->addValidation("Razão Socialdddd", new TRequiredValidator()); 
        $ativo->addValidation("Ativo", new TRequiredValidator()); 
        $data_abertura->addValidation("Data abertura", new TRequiredValidator()); 
        $contrib_icms->addValidation("Contrib icms", new TRequiredValidator()); 

        $id->setEditable(false);
        $ativo->setDefaultOption(false);
        $data_abertura->setMask('dd/mm/yyyy');
        $data_abertura->setDatabaseMask('yyyy-mm-dd');

        $ativo->autofocus = 'autofocus';
        $ger_pessoa_endereco_ger_pessoa_ativo->autofocus = 'autofocus';

        $ativo->addItems(['S'=>'Sim','N'=>'Não']);
        $ger_pessoa_endereco_ger_pessoa_ativo->addItems(['S'=>'Sim','N'=>'Não']);
        $ger_pessoa_endereco_ger_pessoa_padrao->addItems(['S'=>'Sim','N'=>'Não']);
        $ger_pessoa_endereco_ger_pessoa_tipo->addItems(['F'=>'Fiscal','C'=>'Cobrança','E'=>'Entrega']);

        $ativo->setValue('S');
        $ger_pessoa_endereco_ger_pessoa_tipo->setValue('C');
        $ger_pessoa_endereco_ger_pessoa_ativo->setValue('S');
        $ger_pessoa_endereco_ger_pessoa_padrao->setValue('N');

        $ativo->enableSearch();
        $ger_pessoa_endereco_ger_pessoa_tipo->enableSearch();
        $ger_pessoa_endereco_ger_pessoa_ativo->enableSearch();
        $ger_pessoa_endereco_ger_pessoa_padrao->enableSearch();

        $id->setSize(100);
        $nome->setSize('70%');
        $ativo->setSize('70%');
        $fone_2->setSize('70%');
        $doc_im->setSize('70%');
        $doc_ie->setSize('70%');
        $doc_rg->setSize('70%');
        $fone_3->setSize('70%');
        $fone_1->setSize('70%');
        $doc_crc->setSize('70%');
        $doc_cpf->setSize('70%');
        $nr_rntrc->setSize('70%');
        $doc_cnae->setSize('70%');
        $doc_cnpj->setSize('70%');
        $contato_2->setSize('70%');
        $contato_3->setSize('70%');
        $contato_1->setSize('70%');
        $doc_junta->setSize('70%');
        $fis_regime->setSize('70%');
        $doc_crc_seq->setSize('20%');
        $contrib_icms->setSize('70%');
        $razao_social->setSize('70%');
        $data_abertura->setSize('37%');
        $doc_rg_org_exp->setSize('70%');
        $doc_crc_org_exp->setSize('70%');
        $ger_pessoa_endereco_ger_pessoa_fone->setSize('70%');
        $ger_pessoa_endereco_ger_pessoa_tipo->setSize('70%');
        $ger_pessoa_endereco_ger_pessoa_email->setSize('70%');
        $ger_pessoa_endereco_ger_pessoa_ativo->setSize('70%');
        $ger_pessoa_endereco_ger_pessoa_padrao->setSize('70%');
        $ger_pessoa_endereco_ger_pessoa_contato->setSize('70%');
        $ger_pessoa_endereco_ger_pessoa_end_cep->setSize('70%');
        $ger_pessoa_conta_banco_ger_pessoa_conta->setSize('70%');
        $ger_pessoa_endereco_ger_pessoa_end_bairro->setSize('70%');
        $ger_pessoa_conta_banco_ger_pessoa_agencia->setSize('70%');
        $ger_pessoa_endereco_ger_pessoa_end_logradouro->setSize('70%');
        $ger_pessoa_conta_banco_ger_pessoa_observacao->setSize('100%');
        $ger_pessoa_endereco_ger_pessoa_end_complemento->setSize('70%');
        $ger_pessoa_conta_banco_ger_pessoa_fin_banco_id->setSize('70%');
        $ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id->setSize('70%');
        $ger_pessoa_endereco_ger_pessoa_end_logradouro_nr->setSize('70%');

        $this->form->appendPage("Geral");

        $this->form->addFields([new THidden('current_tab_this->form')]);
        $this->form->setTabFunction("$('[name=current_tab_this->form]').val($(this).attr('data-current_page'));");

        $row1 = $this->form->addFields([new TLabel("ID")],[$id],[new TLabel("Nome")],[$nome]);
        $row2 = $this->form->addFields([new TLabel("Razão Social")],[$razao_social],[new TLabel("Ativo")],[$ativo]);
        $row3 = $this->form->addFields([new TLabel("Data abertura")],[$data_abertura],[],[]);
        $row4 = $this->form->addContent([new TFormSeparator("Contatos", '#333333', '18', '#428bca')]);
        $row5 = $this->form->addFields([new TLabel("Contato 1")],[$contato_1],[new TLabel("Fone 1")],[$fone_1]);
        $row6 = $this->form->addFields([new TLabel("Contato 2")],[$contato_2],[new TLabel("Fone 2")],[$fone_2]);
        $row7 = $this->form->addFields([new TLabel("Contato 3")],[$contato_3],[new TLabel("Fone 3")],[$fone_3]);

        $tbdet = new BootstrapFormBuilder('tbdet');
        $this->tbdet = $tbdet;
        $tbdet->setProperty('style', 'border:none; box-shadow:none;');

        $tbdet->appendPage("Aba 1");

        $tbdet->addFields([new THidden('current_tab_tbdet')]);
        $tbdet->setTabFunction("$('[name=current_tab_tbdet]').val($(this).attr('data-current_page'));");

        $row8 = $tbdet->addFields([new TLabel("Ativo")],[$ger_pessoa_endereco_ger_pessoa_ativo],[new TLabel("Tipo")],[$ger_pessoa_endereco_ger_pessoa_tipo]);
        $row9 = $tbdet->addFields([new TLabel("Padrão")],[$ger_pessoa_endereco_ger_pessoa_padrao],[],[]);
        $row10 = $tbdet->addFields([new TLabel("Logradouro")],[$ger_pessoa_endereco_ger_pessoa_end_logradouro],[new TLabel("Número")],[$ger_pessoa_endereco_ger_pessoa_end_logradouro_nr]);
        $row11 = $tbdet->addFields([new TLabel("Bairro")],[$ger_pessoa_endereco_ger_pessoa_end_bairro],[new TLabel("Complemento")],[$ger_pessoa_endereco_ger_pessoa_end_complemento]);
        $row12 = $tbdet->addFields([new TLabel("Cep")],[$ger_pessoa_endereco_ger_pessoa_end_cep],[new TLabel("Cidade")],[$ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id]);
        $row13 = $tbdet->addFields([new TLabel("Email")],[$ger_pessoa_endereco_ger_pessoa_email]);
        $row14 = $tbdet->addFields([new TLabel("Contato")],[$ger_pessoa_endereco_ger_pessoa_contato],[new TLabel("Fone")],[$ger_pessoa_endereco_ger_pessoa_fone]);
        $row15 = $tbdet->addFields([$ger_pessoa_endereco_ger_pessoa_id]);         
        $add_ger_pessoa_endereco_ger_pessoa = new TButton('add_ger_pessoa_endereco_ger_pessoa');

        $action_ger_pessoa_endereco_ger_pessoa = new TAction(array($this, 'onAddGerPessoaEnderecoGerPessoa'));

        $add_ger_pessoa_endereco_ger_pessoa->setAction($action_ger_pessoa_endereco_ger_pessoa, "Adicionar");
        $add_ger_pessoa_endereco_ger_pessoa->setImage('fa:plus #000000');

        $tbdet->addFields([$add_ger_pessoa_endereco_ger_pessoa]);

        $this->ger_pessoa_endereco_ger_pessoa_list = new BootstrapDatagridWrapper(new TQuickGrid);
        $this->ger_pessoa_endereco_ger_pessoa_list->style = 'width:100%';
        $this->ger_pessoa_endereco_ger_pessoa_list->class .= ' table-bordered';
        $this->ger_pessoa_endereco_ger_pessoa_list->disableDefaultClick();
        $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn('', 'edit', 'left', 50);
        $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn('', 'delete', 'left', 50);

        $column_ger_pessoa_endereco_ger_pessoa_ativo = $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn("Ativo", 'ger_pessoa_endereco_ger_pessoa_ativo', 'left');
        $column_ger_pessoa_endereco_ger_pessoa_tipo = $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn("Tipo", 'ger_pessoa_endereco_ger_pessoa_tipo', 'left');
        $column_ger_pessoa_endereco_ger_pessoa_padrao = $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn("Padrao", 'ger_pessoa_endereco_ger_pessoa_padrao', 'left');
        $column_ger_pessoa_endereco_ger_pessoa_end_logradouro = $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn("Logradouro", 'ger_pessoa_endereco_ger_pessoa_end_logradouro', 'left');
        $column_ger_pessoa_endereco_ger_pessoa_end_logradouro_nr = $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn("Número", 'ger_pessoa_endereco_ger_pessoa_end_logradouro_nr', 'left');
        $column_ger_pessoa_endereco_ger_pessoa_end_bairro = $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn("Bairro", 'ger_pessoa_endereco_ger_pessoa_end_bairro', 'left');
        $column_ger_pessoa_endereco_ger_pessoa_end_complemento = $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn("Complemento", 'ger_pessoa_endereco_ger_pessoa_end_complemento', 'left');
        $column_ger_pessoa_endereco_ger_pessoa_end_cep = $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn("Cep", 'ger_pessoa_endereco_ger_pessoa_end_cep', 'left');
        $column_ger_pessoa_endereco_ger_pessoa_fone = $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn("Fone", 'ger_pessoa_endereco_ger_pessoa_fone', 'left');
        $column_ger_pessoa_endereco_ger_pessoa_email = $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn("Email", 'ger_pessoa_endereco_ger_pessoa_email', 'left');
        $column_ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id = $this->ger_pessoa_endereco_ger_pessoa_list->addQuickColumn("Cidade", 'ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id', 'left');

        $this->ger_pessoa_endereco_ger_pessoa_list->createModel();
        $this->ger_pessoa_endereco_panel = new TPanelGroup();
        $this->ger_pessoa_endereco_panel->{'class'} = '';
        $this->ger_pessoa_endereco_panel->add($this->ger_pessoa_endereco_ger_pessoa_list);
        $this->ger_pessoa_endereco_panel->getBody()->style = "overflow-x:auto;";
        $tbdet->addContent([$this->ger_pessoa_endereco_panel]);

        $tbdet->appendPage("Aba 2");
        $row16 = $tbdet->addFields([new TLabel("Banco")],[$ger_pessoa_conta_banco_ger_pessoa_fin_banco_id]);
        $row17 = $tbdet->addFields([new TLabel("Agencia")],[$ger_pessoa_conta_banco_ger_pessoa_agencia],[new TLabel("Conta")],[$ger_pessoa_conta_banco_ger_pessoa_conta]);
        $row18 = $tbdet->addFields([new TLabel("Observacao")],[$ger_pessoa_conta_banco_ger_pessoa_observacao]);
        $row19 = $tbdet->addFields([$ger_pessoa_conta_banco_ger_pessoa_id]);         
        $add_ger_pessoa_conta_banco_ger_pessoa = new TButton('add_ger_pessoa_conta_banco_ger_pessoa');

        $action_ger_pessoa_conta_banco_ger_pessoa = new TAction(array($this, 'onAddGerPessoaContaBancoGerPessoa'));

        $add_ger_pessoa_conta_banco_ger_pessoa->setAction($action_ger_pessoa_conta_banco_ger_pessoa, "Adicionar");
        $add_ger_pessoa_conta_banco_ger_pessoa->setImage('fa:plus #000000');

        $tbdet->addFields([$add_ger_pessoa_conta_banco_ger_pessoa]);

        $this->ger_pessoa_conta_banco_ger_pessoa_list = new BootstrapDatagridWrapper(new TQuickGrid);
        $this->ger_pessoa_conta_banco_ger_pessoa_list->style = 'width:100%';
        $this->ger_pessoa_conta_banco_ger_pessoa_list->class .= ' table-bordered';
        $this->ger_pessoa_conta_banco_ger_pessoa_list->disableDefaultClick();
        $this->ger_pessoa_conta_banco_ger_pessoa_list->addQuickColumn('', 'edit', 'left', 50);
        $this->ger_pessoa_conta_banco_ger_pessoa_list->addQuickColumn('', 'delete', 'left', 50);

        $column_ger_pessoa_conta_banco_ger_pessoa_fin_banco_id = $this->ger_pessoa_conta_banco_ger_pessoa_list->addQuickColumn("Banco", 'ger_pessoa_conta_banco_ger_pessoa_fin_banco_id', 'left');
        $column_ger_pessoa_conta_banco_ger_pessoa_agencia = $this->ger_pessoa_conta_banco_ger_pessoa_list->addQuickColumn("Agencia", 'ger_pessoa_conta_banco_ger_pessoa_agencia', 'left');
        $column_ger_pessoa_conta_banco_ger_pessoa_conta = $this->ger_pessoa_conta_banco_ger_pessoa_list->addQuickColumn("Conta", 'ger_pessoa_conta_banco_ger_pessoa_conta', 'left');
        $column_ger_pessoa_conta_banco_ger_pessoa_observacao = $this->ger_pessoa_conta_banco_ger_pessoa_list->addQuickColumn("Observacao", 'ger_pessoa_conta_banco_ger_pessoa_observacao', 'left');
        
        $this->ger_pessoa_conta_banco_ger_pessoa_list->createModel();
        $this->ger_pessoa_conta_banco_panel = new TPanelGroup();
        $this->ger_pessoa_conta_banco_panel->{'class'} = '';
        $this->ger_pessoa_conta_banco_panel->add($this->ger_pessoa_conta_banco_ger_pessoa_list);
        $this->ger_pessoa_conta_banco_panel->getBody()->style = "overflow-x:auto;";
        $tbdet->addContent([$this->ger_pessoa_conta_banco_panel]);

        $row20 = $this->form->addFields([$tbdet]);
        $row20->layout = [' col-sm-12'];
        
        $this->form->appendPage("Documentos");
        $row21 = $this->form->addFields([new TLabel("Doc. Cpf")],[$doc_cpf],[new TLabel("Doc. Cnpj")],[$doc_cnpj]);
        $row22 = $this->form->addFields([new TLabel("Doc. Insc. Municipal")],[$doc_im],[new TLabel("Doc Insc. Estadual")],[$doc_ie]);
        $row23 = $this->form->addFields([new TLabel("Nr. Rntrc")],[$nr_rntrc],[new TLabel("Doc. Junta")],[$doc_junta]);
        $row24 = $this->form->addFields([new TLabel("Doc. Rg")],[$doc_rg],[new TLabel("Doc. Orgão Exp.")],[$doc_rg_org_exp]);
        $row25 = $this->form->addFields([new TLabel("Doc. Crc")],[$doc_crc,$doc_crc_seq],[new TLabel("Doc. Crc Orgão Exp.")],[$doc_crc_org_exp]);
        $row26 = $this->form->addFields([new TLabel("Doc. Cnae")],[$doc_cnae],[],[]);

        $this->form->appendPage("Fiscal");
        $row27 = $this->form->addFields([new TLabel("Regime")],[$fis_regime],[new TLabel("Contrib. Icms")],[$contrib_icms]);

        $this->form->addFields([new THidden('current_tab')]);
        $this->form->setTabFunction("$('[name=current_tab]').val($(this).attr('data-current_page'));");

        // create the form actions
        $btn_onsave = $this->form->addAction("Salvar", new TAction([$this, 'onSave']), 'fa:floppy-o #ffffff');
        $btn_onsave->addStyleClass('btn-primary'); 

        $btn_onclear = $this->form->addAction("Limpar", new TAction([$this, 'onClear']), 'fa:eraser #dd5a43');
        $btn_onback = $this->form->addAction('Voltar',new TAction(array('SystemGroupList','onReload')),'fa:arrow-circle-o-left blue');
        // vertical box container
        $container = new TVBox;
        $container->style = 'width: 100%';
        $container->class = 'form-container';
        $container->add(TBreadCrumb::create([TSession::getValue('pConn'),'GerPessoaForm']));
        $container->add($this->form);

        parent::add($container);

    }

    public function onSave($param = null) 
    {
        try
        {
            TTransaction::open(TSession::getValue('pConn')); // open a transaction

            $messageAction = null;

            $this->form->validate(); // validate form data

            $object = new GerPessoa(); // create an empty object 

            $data = $this->form->getData(); // get form data as array
            $object->fromArray( (array) $data); // load the object with data

            $object->store(); // save the object 

            $ger_pessoa_conta_banco_ger_pessoa_items = $this->storeItems('GerPessoaContaBanco', 'ger_pessoa_id', $object, 'ger_pessoa_conta_banco_ger_pessoa', function($masterObject, $detailObject){ 

                //code here

            }); 

            $ger_pessoa_endereco_ger_pessoa_items = $this->storeItems('GerPessoaEndereco', 'ger_pessoa_id', $object, 'ger_pessoa_endereco_ger_pessoa', function($masterObject, $detailObject){ 

                //code here

            }); 

            // get the generated {PRIMARY_KEY}
            $data->id = $object->id; 

            $this->form->setData($data); // fill form data
            TTransaction::close(); // close the transaction

            /**
            // To define an action to be executed on the message close event:
            $messageAction = new TAction(['className', 'methodName']);
            **/

            new TMessage('info', AdiantiCoreTranslator::translate('Record saved'), $messageAction);

        }
        catch (Exception $e) // in case of exception
        {
            //</catchAutoCode> 

            new TMessage('error', $e->getMessage()); // shows the exception error message
            $this->form->setData( $this->form->getData() ); // keep form data
            TTransaction::rollback(); // undo all pending operations
        }
    }

    public function onEdit( $param )
    {
        try
        {
            if (isset($param['key']))
            {
                $key = $param['key'];  // get the parameter $key
                TTransaction::open(TSession::getValue('pConn')); // open a transaction

                $object = new GerPessoa($key); // instantiates the Active Record 

                $ger_pessoa_conta_banco_ger_pessoa_items = $this->loadItems('GerPessoaContaBanco', 'ger_pessoa_id', $object, 'ger_pessoa_conta_banco_ger_pessoa', function($masterObject, $detailObject, $objectItems){ 

                    //code here

                }); 

                $ger_pessoa_endereco_ger_pessoa_items = $this->loadItems('GerPessoaEndereco', 'ger_pessoa_id', $object, 'ger_pessoa_endereco_ger_pessoa', function($masterObject, $detailObject, $objectItems){ 

                    //code here

                }); 

                $this->form->setData($object); // fill the form 

                    $this->onReload();

                TTransaction::close(); // close the transaction 
            }
            else
            {
                $this->form->clear();
            }
        }
        catch (Exception $e) // in case of exception
        {
            new TMessage('error', $e->getMessage()); // shows the exception error message
            TTransaction::rollback(); // undo all pending operations
        }
    }

    /**
     * Clear form data
     * @param $param Request
     */
    public function onClear( $param )
    {
        $this->form->clear(true);

        TSession::setValue('ger_pessoa_endereco_ger_pessoa_items', null);
        TSession::setValue('ger_pessoa_conta_banco_ger_pessoa_items', null);

        $this->onReload();
    }

    public function onAddGerPessoaEnderecoGerPessoa( $param )
    {
        try
        {
            $data = $this->form->getData();
            
            if(!$data->ger_pessoa_endereco_ger_pessoa_ativo)
            {
                throw new Exception(AdiantiCoreTranslator::translate('The field ^1 is required', "Ativo"));
            }             
            if(!$data->ger_pessoa_endereco_ger_pessoa_tipo)
            {
                throw new Exception(AdiantiCoreTranslator::translate('The field ^1 is required', "Tipo"));
            }             
            if(!$data->ger_pessoa_endereco_ger_pessoa_padrao)
            {
                throw new Exception(AdiantiCoreTranslator::translate('The field ^1 is required', "Padrao"));
            }             
            if(!$data->ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id)
            {
                throw new Exception(AdiantiCoreTranslator::translate('The field ^1 is required', "End ger cidade id"));
            }             
            
            $ger_pessoa_endereco_ger_pessoa_items = TSession::getValue('ger_pessoa_endereco_ger_pessoa_items');
            $key = isset($data->ger_pessoa_endereco_ger_pessoa_id) && $data->ger_pessoa_endereco_ger_pessoa_id ? $data->ger_pessoa_endereco_ger_pessoa_id : uniqid();
            $fields = []; 

            $fields['ger_pessoa_endereco_ger_pessoa_ativo'] = $data->ger_pessoa_endereco_ger_pessoa_ativo;
            $fields['ger_pessoa_endereco_ger_pessoa_tipo'] = $data->ger_pessoa_endereco_ger_pessoa_tipo;
            $fields['ger_pessoa_endereco_ger_pessoa_padrao'] = $data->ger_pessoa_endereco_ger_pessoa_padrao;
            $fields['ger_pessoa_endereco_ger_pessoa_end_logradouro'] = $data->ger_pessoa_endereco_ger_pessoa_end_logradouro;
            $fields['ger_pessoa_endereco_ger_pessoa_end_logradouro_nr'] = $data->ger_pessoa_endereco_ger_pessoa_end_logradouro_nr;
            $fields['ger_pessoa_endereco_ger_pessoa_end_bairro'] = $data->ger_pessoa_endereco_ger_pessoa_end_bairro;
            $fields['ger_pessoa_endereco_ger_pessoa_end_complemento'] = $data->ger_pessoa_endereco_ger_pessoa_end_complemento;
            $fields['ger_pessoa_endereco_ger_pessoa_end_cep'] = $data->ger_pessoa_endereco_ger_pessoa_end_cep;
            $fields['ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id'] = $data->ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id;
            $fields['ger_pessoa_endereco_ger_pessoa_email'] = $data->ger_pessoa_endereco_ger_pessoa_email;
            $fields['ger_pessoa_endereco_ger_pessoa_contato'] = $data->ger_pessoa_endereco_ger_pessoa_contato;
            $fields['ger_pessoa_endereco_ger_pessoa_fone'] = $data->ger_pessoa_endereco_ger_pessoa_fone;
            $ger_pessoa_endereco_ger_pessoa_items[ $key ] = $fields;

            TSession::setValue('ger_pessoa_endereco_ger_pessoa_items', $ger_pessoa_endereco_ger_pessoa_items);

            $data->ger_pessoa_endereco_ger_pessoa_id = '';
            $data->ger_pessoa_endereco_ger_pessoa_ativo = '';
            $data->ger_pessoa_endereco_ger_pessoa_tipo = '';
            $data->ger_pessoa_endereco_ger_pessoa_padrao = '';
            $data->ger_pessoa_endereco_ger_pessoa_end_logradouro = '';
            $data->ger_pessoa_endereco_ger_pessoa_end_logradouro_nr = '';
            $data->ger_pessoa_endereco_ger_pessoa_end_bairro = '';
            $data->ger_pessoa_endereco_ger_pessoa_end_complemento = '';
            $data->ger_pessoa_endereco_ger_pessoa_end_cep = '';
            $data->ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id = '';
            $data->ger_pessoa_endereco_ger_pessoa_email = '';
            $data->ger_pessoa_endereco_ger_pessoa_contato = '';
            $data->ger_pessoa_endereco_ger_pessoa_fone = '';

            $this->form->setData($data);

            $this->onReload( $param );
        }
        catch (Exception $e)
        {
            $this->form->setData( $this->form->getData());

            new TMessage('error', $e->getMessage());
        }
    }

    public function onEditGerPessoaEnderecoGerPessoa( $param )
    {
        $data = $this->form->getData();

        // read session items
        $items = TSession::getValue('ger_pessoa_endereco_ger_pessoa_items');

        // get the session item
        $item = $items[$param['ger_pessoa_endereco_ger_pessoa_id_row_id']];

        $data->ger_pessoa_endereco_ger_pessoa_ativo = $item['ger_pessoa_endereco_ger_pessoa_ativo'];
        $data->ger_pessoa_endereco_ger_pessoa_tipo = $item['ger_pessoa_endereco_ger_pessoa_tipo'];
        $data->ger_pessoa_endereco_ger_pessoa_padrao = $item['ger_pessoa_endereco_ger_pessoa_padrao'];
        $data->ger_pessoa_endereco_ger_pessoa_end_logradouro = $item['ger_pessoa_endereco_ger_pessoa_end_logradouro'];
        $data->ger_pessoa_endereco_ger_pessoa_end_logradouro_nr = $item['ger_pessoa_endereco_ger_pessoa_end_logradouro_nr'];
        $data->ger_pessoa_endereco_ger_pessoa_end_bairro = $item['ger_pessoa_endereco_ger_pessoa_end_bairro'];
        $data->ger_pessoa_endereco_ger_pessoa_end_complemento = $item['ger_pessoa_endereco_ger_pessoa_end_complemento'];
        $data->ger_pessoa_endereco_ger_pessoa_end_cep = $item['ger_pessoa_endereco_ger_pessoa_end_cep'];
        $data->ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id = $item['ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id'];
        $data->ger_pessoa_endereco_ger_pessoa_email = $item['ger_pessoa_endereco_ger_pessoa_email'];
        $data->ger_pessoa_endereco_ger_pessoa_contato = $item['ger_pessoa_endereco_ger_pessoa_contato'];
        $data->ger_pessoa_endereco_ger_pessoa_fone = $item['ger_pessoa_endereco_ger_pessoa_fone'];

        $data->ger_pessoa_endereco_ger_pessoa_id = $param['ger_pessoa_endereco_ger_pessoa_id_row_id'];

        // fill product fields
        $this->form->setData( $data );

        $this->onReload( $param );

    }

    public function onDeleteGerPessoaEnderecoGerPessoa( $param )
    {
        $data = $this->form->getData();

        $data->ger_pessoa_endereco_ger_pessoa_ativo = '';
        $data->ger_pessoa_endereco_ger_pessoa_tipo = '';
        $data->ger_pessoa_endereco_ger_pessoa_padrao = '';
        $data->ger_pessoa_endereco_ger_pessoa_end_logradouro = '';
        $data->ger_pessoa_endereco_ger_pessoa_end_logradouro_nr = '';
        $data->ger_pessoa_endereco_ger_pessoa_end_bairro = '';
        $data->ger_pessoa_endereco_ger_pessoa_end_complemento = '';
        $data->ger_pessoa_endereco_ger_pessoa_end_cep = '';
        $data->ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id = '';
        $data->ger_pessoa_endereco_ger_pessoa_email = '';
        $data->ger_pessoa_endereco_ger_pessoa_contato = '';
        $data->ger_pessoa_endereco_ger_pessoa_fone = '';

        // clear form data
        $this->form->setData( $data );

        // read session items
        $items = TSession::getValue('ger_pessoa_endereco_ger_pessoa_items');

        // delete the item from session
        unset($items[$param['ger_pessoa_endereco_ger_pessoa_id_row_id']]);
        TSession::setValue('ger_pessoa_endereco_ger_pessoa_items', $items);

        // reload sale items
        $this->onReload( $param );

    }

    public function onReloadGerPessoaEnderecoGerPessoa( $param )
    {
        $items = TSession::getValue('ger_pessoa_endereco_ger_pessoa_items'); 

        $this->ger_pessoa_endereco_ger_pessoa_list->clear(); 

        if($items) 
        { 
            $cont = 1; 
            foreach ($items as $key => $item) 
            {
                $rowItem = new StdClass;

                $action_del = new TAction(array($this, 'onDeleteGerPessoaEnderecoGerPessoa')); 
                $action_del->setParameter('ger_pessoa_endereco_ger_pessoa_id_row_id', $key);
                $action_del->setParameter('row_data', base64_encode(serialize($item)));
                $action_del->setParameter('key', $key);

                $action_edi = new TAction(array($this, 'onEditGerPessoaEnderecoGerPessoa'));  
                $action_edi->setParameter('ger_pessoa_endereco_ger_pessoa_id_row_id', $key);  
                $action_edi->setParameter('row_data', base64_encode(serialize($item)));
                $action_edi->setParameter('key', $key);

                $button_del = new TButton('delete_ger_pessoa_endereco_ger_pessoa'.$cont);
                $button_del->setAction($action_del, '');
                $button_del->setFormName($this->form->getName());
                $button_del->class = 'btn btn-link btn-sm';
                $button_del->title = "Excluir";
                $button_del->setImage('fa:trash-o #dd5a43');

                $rowItem->delete = $button_del;

                $button_edi = new TButton('edit_ger_pessoa_endereco_ger_pessoa'.$cont);
                $button_edi->setAction($action_edi, '');
                $button_edi->setFormName($this->form->getName());
                $button_edi->class = 'btn btn-link btn-sm';
                $button_edi->title = "Editar";
                $button_edi->setImage('fa:pencil-square-o #478fca');

                $rowItem->edit = $button_edi;

                $rowItem->ger_pessoa_endereco_ger_pessoa_ativo = isset($item['ger_pessoa_endereco_ger_pessoa_ativo']) ? $item['ger_pessoa_endereco_ger_pessoa_ativo'] : '';
                $rowItem->ger_pessoa_endereco_ger_pessoa_tipo = isset($item['ger_pessoa_endereco_ger_pessoa_tipo']) ? $item['ger_pessoa_endereco_ger_pessoa_tipo'] : '';
                $rowItem->ger_pessoa_endereco_ger_pessoa_padrao = isset($item['ger_pessoa_endereco_ger_pessoa_padrao']) ? $item['ger_pessoa_endereco_ger_pessoa_padrao'] : '';
                $rowItem->ger_pessoa_endereco_ger_pessoa_end_logradouro = isset($item['ger_pessoa_endereco_ger_pessoa_end_logradouro']) ? $item['ger_pessoa_endereco_ger_pessoa_end_logradouro'] : '';
                $rowItem->ger_pessoa_endereco_ger_pessoa_end_logradouro_nr = isset($item['ger_pessoa_endereco_ger_pessoa_end_logradouro_nr']) ? $item['ger_pessoa_endereco_ger_pessoa_end_logradouro_nr'] : '';
                $rowItem->ger_pessoa_endereco_ger_pessoa_end_bairro = isset($item['ger_pessoa_endereco_ger_pessoa_end_bairro']) ? $item['ger_pessoa_endereco_ger_pessoa_end_bairro'] : '';
                $rowItem->ger_pessoa_endereco_ger_pessoa_end_complemento = isset($item['ger_pessoa_endereco_ger_pessoa_end_complemento']) ? $item['ger_pessoa_endereco_ger_pessoa_end_complemento'] : '';
                $rowItem->ger_pessoa_endereco_ger_pessoa_end_cep = isset($item['ger_pessoa_endereco_ger_pessoa_end_cep']) ? $item['ger_pessoa_endereco_ger_pessoa_end_cep'] : '';
                $rowItem->ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id = '';
                if(isset($item['ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id']) && $item['ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id'])
                {
                    TTransaction::open(TSession::getValue('pConn'));
                    $ger_cidade = GerCidade::find($item['ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id']);
                    if($ger_cidade)
                    {
                        $rowItem->ger_pessoa_endereco_ger_pessoa_end_ger_cidade_id = $ger_cidade->render('{id}');
                    }
                    TTransaction::close();
                }

                $rowItem->ger_pessoa_endereco_ger_pessoa_email = isset($item['ger_pessoa_endereco_ger_pessoa_email']) ? $item['ger_pessoa_endereco_ger_pessoa_email'] : '';
                $rowItem->ger_pessoa_endereco_ger_pessoa_contato = isset($item['ger_pessoa_endereco_ger_pessoa_contato']) ? $item['ger_pessoa_endereco_ger_pessoa_contato'] : '';
                $rowItem->ger_pessoa_endereco_ger_pessoa_fone = isset($item['ger_pessoa_endereco_ger_pessoa_fone']) ? $item['ger_pessoa_endereco_ger_pessoa_fone'] : '';

                $row = $this->ger_pessoa_endereco_ger_pessoa_list->addItem($rowItem);

                $cont++;
            } 
        } 
    } 

    public function onAddGerPessoaContaBancoGerPessoa( $param )
    {
        try
        {
            $data = $this->form->getData();

            if(!$data->ger_pessoa_conta_banco_ger_pessoa_fin_banco_id)
            {
                throw new Exception(AdiantiCoreTranslator::translate('The field ^1 is required', "Fin banco id"));
            }             
            if(!$data->ger_pessoa_conta_banco_ger_pessoa_agencia)
            {
                throw new Exception(AdiantiCoreTranslator::translate('The field ^1 is required', "Agencia"));
            }             
            if(!$data->ger_pessoa_conta_banco_ger_pessoa_conta)
            {
                throw new Exception(AdiantiCoreTranslator::translate('The field ^1 is required', "Conta"));
            }             
            if(!$data->ger_pessoa_conta_banco_ger_pessoa_observacao)
            {
                throw new Exception(AdiantiCoreTranslator::translate('The field ^1 is required', "Observacao"));
            }             

            $ger_pessoa_conta_banco_ger_pessoa_items = TSession::getValue('ger_pessoa_conta_banco_ger_pessoa_items');
            $key = isset($data->ger_pessoa_conta_banco_ger_pessoa_id) && $data->ger_pessoa_conta_banco_ger_pessoa_id ? $data->ger_pessoa_conta_banco_ger_pessoa_id : uniqid();
            $fields = []; 

            $fields['ger_pessoa_conta_banco_ger_pessoa_fin_banco_id'] = $data->ger_pessoa_conta_banco_ger_pessoa_fin_banco_id;
            $fields['ger_pessoa_conta_banco_ger_pessoa_agencia'] = $data->ger_pessoa_conta_banco_ger_pessoa_agencia;
            $fields['ger_pessoa_conta_banco_ger_pessoa_conta'] = $data->ger_pessoa_conta_banco_ger_pessoa_conta;
            $fields['ger_pessoa_conta_banco_ger_pessoa_observacao'] = $data->ger_pessoa_conta_banco_ger_pessoa_observacao;
            $ger_pessoa_conta_banco_ger_pessoa_items[ $key ] = $fields;

            TSession::setValue('ger_pessoa_conta_banco_ger_pessoa_items', $ger_pessoa_conta_banco_ger_pessoa_items);

            $data->ger_pessoa_conta_banco_ger_pessoa_id = '';
            $data->ger_pessoa_conta_banco_ger_pessoa_fin_banco_id = '';
            $data->ger_pessoa_conta_banco_ger_pessoa_agencia = '';
            $data->ger_pessoa_conta_banco_ger_pessoa_conta = '';
            $data->ger_pessoa_conta_banco_ger_pessoa_observacao = '';

            $this->form->setData($data);

            $this->onReload( $param );
        }
        catch (Exception $e)
        {
            $this->form->setData( $this->form->getData());

            new TMessage('error', $e->getMessage());
        }
    }

    public function onEditGerPessoaContaBancoGerPessoa( $param )
    {
        $data = $this->form->getData();

        // read session items
        $items = TSession::getValue('ger_pessoa_conta_banco_ger_pessoa_items');

        // get the session item
        $item = $items[$param['ger_pessoa_conta_banco_ger_pessoa_id_row_id']];

        $data->ger_pessoa_conta_banco_ger_pessoa_fin_banco_id = $item['ger_pessoa_conta_banco_ger_pessoa_fin_banco_id'];
        $data->ger_pessoa_conta_banco_ger_pessoa_agencia = $item['ger_pessoa_conta_banco_ger_pessoa_agencia'];
        $data->ger_pessoa_conta_banco_ger_pessoa_conta = $item['ger_pessoa_conta_banco_ger_pessoa_conta'];
        $data->ger_pessoa_conta_banco_ger_pessoa_observacao = $item['ger_pessoa_conta_banco_ger_pessoa_observacao'];

        $data->ger_pessoa_conta_banco_ger_pessoa_id = $param['ger_pessoa_conta_banco_ger_pessoa_id_row_id'];

        // fill product fields
        $this->form->setData( $data );

        $this->onReload( $param );

    }

    public function onDeleteGerPessoaContaBancoGerPessoa( $param )
    {
        $data = $this->form->getData();

        $data->ger_pessoa_conta_banco_ger_pessoa_fin_banco_id = '';
        $data->ger_pessoa_conta_banco_ger_pessoa_agencia = '';
        $data->ger_pessoa_conta_banco_ger_pessoa_conta = '';
        $data->ger_pessoa_conta_banco_ger_pessoa_observacao = '';

        // clear form data
        $this->form->setData( $data );

        // read session items
        $items = TSession::getValue('ger_pessoa_conta_banco_ger_pessoa_items');

        // delete the item from session
        unset($items[$param['ger_pessoa_conta_banco_ger_pessoa_id_row_id']]);
        TSession::setValue('ger_pessoa_conta_banco_ger_pessoa_items', $items);

        // reload sale items
        $this->onReload( $param );

    }

    public function onReloadGerPessoaContaBancoGerPessoa( $param )
    {
        $items = TSession::getValue('ger_pessoa_conta_banco_ger_pessoa_items'); 

        $this->ger_pessoa_conta_banco_ger_pessoa_list->clear(); 

        if($items) 
        { 
            $cont = 1; 
            foreach ($items as $key => $item) 
            {
                $rowItem = new StdClass;

                $action_del = new TAction(array($this, 'onDeleteGerPessoaContaBancoGerPessoa')); 
                $action_del->setParameter('ger_pessoa_conta_banco_ger_pessoa_id_row_id', $key);
                $action_del->setParameter('row_data', base64_encode(serialize($item)));
                $action_del->setParameter('key', $key);

                $action_edi = new TAction(array($this, 'onEditGerPessoaContaBancoGerPessoa'));  
                $action_edi->setParameter('ger_pessoa_conta_banco_ger_pessoa_id_row_id', $key);  
                $action_edi->setParameter('row_data', base64_encode(serialize($item)));
                $action_edi->setParameter('key', $key);

                $button_del = new TButton('delete_ger_pessoa_conta_banco_ger_pessoa'.$cont);
                $button_del->setAction($action_del, '');
                $button_del->setFormName($this->form->getName());
                $button_del->class = 'btn btn-link btn-sm';
                $button_del->title = "Excluir";
                $button_del->setImage('fa:trash-o #dd5a43');

                $rowItem->delete = $button_del;

                $button_edi = new TButton('edit_ger_pessoa_conta_banco_ger_pessoa'.$cont);
                $button_edi->setAction($action_edi, '');
                $button_edi->setFormName($this->form->getName());
                $button_edi->class = 'btn btn-link btn-sm';
                $button_edi->title = "Editar";
                $button_edi->setImage('fa:pencil-square-o #478fca');

                $rowItem->edit = $button_edi;

                $rowItem->ger_pessoa_conta_banco_ger_pessoa_fin_banco_id = '';
                if(isset($item['ger_pessoa_conta_banco_ger_pessoa_fin_banco_id']) && $item['ger_pessoa_conta_banco_ger_pessoa_fin_banco_id'])
                {
                    TTransaction::open(TSession::getValue('pConn'));
                    $fin_banco = FinBanco::find($item['ger_pessoa_conta_banco_ger_pessoa_fin_banco_id']);
                    if($fin_banco)
                    {
                        $rowItem->ger_pessoa_conta_banco_ger_pessoa_fin_banco_id = $fin_banco->render('{id}');
                    }
                    TTransaction::close();
                }

                $rowItem->ger_pessoa_conta_banco_ger_pessoa_agencia = isset($item['ger_pessoa_conta_banco_ger_pessoa_agencia']) ? $item['ger_pessoa_conta_banco_ger_pessoa_agencia'] : '';
                $rowItem->ger_pessoa_conta_banco_ger_pessoa_conta = isset($item['ger_pessoa_conta_banco_ger_pessoa_conta']) ? $item['ger_pessoa_conta_banco_ger_pessoa_conta'] : '';
                $rowItem->ger_pessoa_conta_banco_ger_pessoa_observacao = isset($item['ger_pessoa_conta_banco_ger_pessoa_observacao']) ? $item['ger_pessoa_conta_banco_ger_pessoa_observacao'] : '';

                $row = $this->ger_pessoa_conta_banco_ger_pessoa_list->addItem($rowItem);

                $cont++;
            } 
        } 
    } 

    public function onShow($param = null)
    {
        TSession::setValue('ger_pessoa_endereco_ger_pessoa_items', null);
        TSession::setValue('ger_pessoa_conta_banco_ger_pessoa_items', null);

        $this->onReload();

    } 

    public function onReload($params = null)
    {
        $this->loaded = TRUE;

        $this->onReloadGerPessoaEnderecoGerPessoa($params);
        $this->onReloadGerPessoaContaBancoGerPessoa($params);
    }

    public function show() 
    { 
        $param = func_get_arg(0);
        if(!empty($param['current_tab']))
        {
            $this->form->setCurrentPage($param['current_tab']);
        }

        if(!empty($param['current_tab_tbdet']))
        {
            $this->tbdet->setCurrentPage($param['current_tab_tbdet']);
        }

        if (!$this->loaded AND (!isset($_GET['method']) OR $_GET['method'] !== 'onReload') ) 
        { 
            $this->onReload( func_get_arg(0) );
        }
        parent::show();
    }

}

