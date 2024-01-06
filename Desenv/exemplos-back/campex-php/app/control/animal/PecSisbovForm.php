<?php

class PecSisbovForm extends TPage
{
    protected $form;
    private $formFields = [];
    private static $database = 'padrao';
    private static $activeRecord = 'PecSisbov';
    private static $primaryKey = 'id';
    private static $formName = 'form_PecSisbovForm';

    /**
     * Form constructor
     * @param $param Request
     */
    public function __construct( $param )
    {
        parent::__construct();

        if(!empty($param['target_container']))
        {
            $this->adianti_target_container = $param['target_container'];
        }

        // creates the form
        $this->form = new BootstrapFormBuilder(self::$formName);
        // define the form title
        $this->form->setFormTitle("SISBOV");


        $codigo = new TEntry('codigo');
        $codigo_mae = new TEntry('codigo_mae');
        $codigo_pai = new TEntry('codigo_pai');
        $aptidao = new TEntry('aptidao');
        $nirf_nascimento = new TEntry('nirf_nascimento');
        $nirf_atual = new TEntry('nirf_atual');
        $observacoes = new TEntry('observacoes');

        $codigo->addValidation("Código", new TRequiredValidator()); 

        $codigo->setMaxLength(50);
        $aptidao->setMaxLength(100);
        $codigo_mae->setMaxLength(50);
        $codigo_pai->setMaxLength(50);
        $nirf_atual->setMaxLength(50);
        $nirf_nascimento->setMaxLength(50);

        $codigo->setSize('100%');
        $aptidao->setSize('100%');
        $codigo_mae->setSize('100%');
        $codigo_pai->setSize('100%');
        $nirf_atual->setSize('100%');
        $observacoes->setSize('100%');
        $nirf_nascimento->setSize('100%');

        $row1 = $this->form->addFields([new TLabel("Código:", '#ff0000', '14px', null, '100%'),$codigo],[new TLabel("Código Mãe:", null, '14px', null, '100%'),$codigo_mae]);
        $row1->layout = ['col-sm-6','col-sm-6'];

        $row2 = $this->form->addFields([new TLabel("Código Pai:", null, '14px', null, '100%'),$codigo_pai],[new TLabel("Aptidão:", null, '14px', null, '100%'),$aptidao]);
        $row2->layout = ['col-sm-6','col-sm-6'];

        $row3 = $this->form->addFields([new TLabel("NIRF Nascimento:", null, '14px', null, '100%'),$nirf_nascimento],[new TLabel("NIRF Atual:", null, '14px', null, '100%'),$nirf_atual]);
        $row3->layout = ['col-sm-6','col-sm-6'];

        $row4 = $this->form->addFields([new TLabel("Observações:", null, '14px', null, '100%'),$observacoes],[]);
        $row4->layout = ['col-sm-6','col-sm-6'];

        // create the form actions
        $btn_onsave = $this->form->addAction("Salvar", new TAction([$this, 'onSave']), 'fas:save #ffffff');
        $this->btn_onsave = $btn_onsave;
        $btn_onsave->addStyleClass('btn-primary'); 

        $btn_onclear = $this->form->addAction("Limpar formulário", new TAction([$this, 'onClear']), 'fas:eraser #dd5a43');
        $this->btn_onclear = $btn_onclear;

        $btn_onshow = $this->form->addAction("Voltar", new TAction(['PecSisbovHeaderList', 'onShow']), 'fas:arrow-left #000000');
        $this->btn_onshow = $btn_onshow;

        parent::setTargetContainer('adianti_right_panel');

        $btnClose = new TButton('closeCurtain');
        $btnClose->class = 'btn btn-sm btn-default';
        $btnClose->style = 'margin-right:10px;';
        $btnClose->onClick = "Template.closeRightPanel();";
        $btnClose->setLabel("Fechar");
        $btnClose->setImage('fas:times');

        $this->form->addHeaderWidget($btnClose);

        parent::add($this->form);

    }

    public function onSave($param = null) 
    {
        try
        {
            TTransaction::open(self::$database); // open a transaction

            $messageAction = null;

            $this->form->validate(); // validate form data

            $object = new PecSisbov(); // create an empty object 

            $data = $this->form->getData(); // get form data as array
            $object->fromArray( (array) $data); // load the object with data

            $object->system_unit_id = TSession::getValue('userunitid');

            $object->store(); // save the object 

            $loadPageParam = [];

            if(!empty($param['target_container']))
            {
                $loadPageParam['target_container'] = $param['target_container'];
            }

            // get the generated {PRIMARY_KEY}
            $data->id = $object->id; 

            $this->form->setData($data); // fill form data
            TTransaction::close(); // close the transaction

            TToast::show('success', "Registro salvo", 'topRight', 'far:check-circle');
            TApplication::loadPage('PecSisbovHeaderList', 'onShow', $loadPageParam); 

                        TScript::create("Template.closeRightPanel();"); 

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
                TTransaction::open(self::$database); // open a transaction

                $object = new PecSisbov($key); // instantiates the Active Record 

                if ($object->system_unit_id <> TSession::getValue('userunitid')) {
                    new TMessage('erro', "Sem Permissão na Unidade");
                    return false;
                }

                $this->form->setData($object); // fill the form 

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

    }

    public function onShow($param = null)
    {

    } 

}

