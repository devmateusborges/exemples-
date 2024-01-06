<?php
class GenericStandartList extends TStandardList
{
    const C_UNITID = true;
    const C_RECORD_CLASS   = '';
    const C_PERM_SYSTEM   = false;
    const C_RECORD_FIELD_ORDER   = ''; 
    /*0-CampoBanco
      1-Order
    */
    const C_RECORD_FIELD   = ''; 
    /*0-CampoBanco
      1-Operador
      2-CampoForm
      3-Label
      4-Largura
      5-ExibirColuna
      6-ColunaAlinhamento
      7-ColunaLargura
      8-FuncaoSQL
      9-Compo
         0-TipoComp
    */     
    const C_FORM_TITLE   = '';
    const C_FORM_CLASS_EDIT   = '';
    const C_FORM_EDIT_ROW   = true;
    const C_FORM_DEL_ROW   = true;
    const C_FORM_NEW_ROW   = true;

    protected $form;
    protected $datagrid;
    protected $pageNavigation;
    protected $formgrid;
    protected $deleteButton;
    protected $transformCallback;

    public function __construct()
    {
        parent::__construct();

        $class = get_class($this);

        if (constant("{$class}::C_PERM_SYSTEM")) {
            if (TSession::getValue('usersystem') !== 'Y') {
                new TMessage('error', _t('Permission denied') . ' - System');
                die();
            }
        }

        parent::setDatabase(TSession::getValue('pConn'));
        parent::setActiveRecord(constant("{$class}::C_RECORD_CLASS"));

        $this->form = new BootstrapFormBuilder('form_search_' . constant("{$class}::C_RECORD_CLASS"));
        $this->form->setFormTitle(constant("{$class}::C_FORM_TITLE"));

        $VRECORD_FIELD_ORDER = json_decode(constant("{$class}::C_RECORD_FIELD_ORDER"),true);
        parent::setDefaultOrder($VRECORD_FIELD_ORDER['CampoBanco'], $VRECORD_FIELD_ORDER['Ordem']);

        $VRECORD_FIELD =  json_decode(constant("{$class}::C_RECORD_FIELD"),true);
        foreach ($VRECORD_FIELD as $key => $item) {
            //TODO Tratar mais tipos de campos
            if ($item['Comp']['TipoComp'] =='TEntry') {
                ${$item['CampoForm']} = new TEntry($item['CampoForm']);
            } else
            if ($item['Comp']['TipoComp'] =='TCombo') {
                ${$item['CampoForm']} = new TCombo($item['CampoForm']);
                $vComboItens = $item['Comp']['ComboItens'];
                ${$item['CampoForm']}->addItems($vComboItens);
            } else
            {
                throw new Exception('Tipo componente '.$item['Comp']['TipoComp'].' não definido');
            }

            if ($item['FuncaoSQL'] == 'upper') {
                parent::addFilterField('upper(' . $item['CampoBanco'] . ')', $item['Operador'], $item['CampoForm']);
                ${$item['CampoForm']}->forceUpperCase();
            } else {
                parent::addFilterField($item['CampoBanco'], $item['Operador'], $item['CampoForm']);
            }
            ${$item['CampoForm']}->setSize($item['Largura']);

            if (!empty($item['Dica'])) {
                ${$item['CampoForm']}->setTip($item['Dica']);
            }

            $this->form->addFields([new TLabel($item['Label'])], [${$item['CampoForm']}]);
        }

        $this->form->setData(TSession::getValue(constant("{$class}::C_RECORD_CLASS") . '_filter_data'));

        $btn = $this->form->addAction(_t('Find'), new TAction(array($this, 'onSearch')), 'fa:search');
        $btn->class = 'btn btn-sm btn-primary';
        if (constant("{$class}::C_FORM_NEW_ROW")) {
            $btn_onshow = $this->form->addAction(_t('New'), new TAction([constant("{$class}::C_FORM_CLASS_EDIT"), 'onEdit']), 'bs:plus-sign green');
        }

        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->datatable = 'false';
        $this->datagrid->style = 'width: 100%';
        $this->datagrid->setHeight(320);


        foreach ($VRECORD_FIELD as $key => $item) {
            ${'column_' . $item['CampoBanco']} = new TDataGridColumn($item['CampoBanco'], $item['Label'], $item['ColunaAlinhamento'], $item['ColunaLargura']);
            $this->datagrid->addColumn(${'column_' . $item['CampoBanco']});

            ${'order_' . $item['CampoBanco']} = new TAction(array($this, 'onReload'));
            ${'order_' . $item['CampoBanco']}->setParameter('order', $item['CampoBanco']);
            ${'column_' . $item['CampoBanco']}->setAction(${'order_' . $item['CampoBanco']});

            if (!empty($item['ColunaTransf'])) {
               ${'column_' . $item['CampoBanco']}->setTransformer(array($item['ColunaTransf'],'t'));
            }
        }

        if (constant("{$class}::C_FORM_EDIT_ROW")) {
            $action_edit = new TDataGridAction(array(constant("{$class}::C_FORM_CLASS_EDIT"), 'onEdit'));
            $action_edit->setButtonClass('btn btn-default');
            $action_edit->setLabel(_t('Edit'));
            $action_edit->setImage('fa:pencil-square-o blue fa-lg');
            $action_edit->setField('id');
            $this->datagrid->addAction($action_edit);
        }

        if (constant("{$class}::C_FORM_DEL_ROW")) {
            $action_del = new TDataGridAction(array($this, 'onDelete'));
            $action_del->setButtonClass('btn btn-default');
            $action_del->setLabel(_t('Delete'));
            $action_del->setImage('fa:trash-o red fa-lg');
            $action_del->setField('id');
            $this->datagrid->addAction($action_del);
        }

        $this->datagrid->createModel();

        $this->list_panel = new TPanelGroup();
        $this->list_panel->add($this->datagrid);
        $this->list_panel->getBody()->style = "overflow-x:auto;";

        $this->pageNavigation = new TPageNavigation;
        $this->pageNavigation->enableCounters();
        $this->pageNavigation->setAction(new TAction(array($this, 'onReload')));
        $this->pageNavigation->setWidth($this->datagrid->getWidth());

        $this->list_panel->addFooter($this->pageNavigation);

        $container = new TVBox;
        $container->style = 'width: 99%';
        $container->add($this->form);
        $container->add($this->list_panel);

        parent::add($container);
    }
}
