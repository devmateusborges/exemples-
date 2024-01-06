<?php

class SystemGroupList extends TStandardList
{
    use GenericTrait;  
    
    protected $form;     // registration form
    protected $datagrid; // listing
    protected $pageNavigation;
    protected $formgrid;
    protected $deleteButton;
    protected $transformCallback;
    
    /**
     * Page constructor
     */
    public function __construct()
    {
        parent::__construct();
        
        if (TSession::getValue('usersystem') !== 'Y') {
            new TMessage('error', _t('Permission denied').' - System');
            die();
        }
        
        parent::setDatabase(TSession::getValue('pConn'));            // defines the database
        parent::setActiveRecord('SystemGroup');   // defines the active record
        parent::setDefaultOrder('id', 'asc');         // defines the default order
        parent::addFilterField('id', '=', 'id'); // filterField, operator, formField
        parent::addFilterField('name', 'like', 'name'); // filterField, operator, formField
        
        // creates the form
        $this->form = new BootstrapFormBuilder('form_search_SystemGroup');
        $this->form->setFormTitle( _t('Groups') );
        
        // create the form fields
        $id = new TEntry('id');
        $id->id = 'edid';
        $name = new TEntry('name');
        $name->id = 'edname';
        
        // add the fields
        $this->form->addFields( [new TLabel('Id')], [$id] );
        $this->form->addFields( [new TLabel(_t('Name'))], [$name] );

        $id->setSize('30%');
        $name->setSize('70%');
        
        // keep the form filled during navigation with session data
        $this->form->setData( TSession::getValue('SystemGroup_filter_data') );
        
        // add the search form actions
        $btn = $this->form->addAction(_t('Find'), new TAction(array($this, 'onSearch')), 'fa:search');
        $btn->class = 'btn btn-sm btn-primary';
        $this->form->addAction(_t('New'),  new TAction(array('SystemGroupForm', 'onEdit')), 'bs:plus-sign green');
        
        //Botão de Treinamento
        $this->BtnTour = $this->form->addHeaderAction('Help', new TAction(array('SystemGroupList', 'onNone')), 'fa:question-circle');
        $this->BtnTour->class = 'btn btn-sm bg-pink';
        $this->BtnTour->addFunction("SystemGroupListTour()");
        
        // creates a DataGrid
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->datatable = 'true';
        $this->datagrid->style = 'width: 100%';
        $this->datagrid->setHeight(320);
        
        // creates the datagrid columns
        $column_id = new TDataGridColumn('id', 'Id', 'center', 50);
        $column_name = new TDataGridColumn('name', _t('Name'), 'left');


        // add the columns to the DataGrid
        $this->datagrid->addColumn($column_id);
        $this->datagrid->addColumn($column_name);


        // creates the datagrid column actions
        $order_id = new TAction(array($this, 'onReload'));
        $order_id->setParameter('order', 'id');
        $column_id->setAction($order_id);
        
        $order_name = new TAction(array($this, 'onReload'));
        $order_name->setParameter('order', 'name');
        $column_name->setAction($order_name);
        
        // create EDIT action
        $action_edit = new TDataGridAction(array('SystemGroupForm', 'onEdit'));
        $action_edit->setButtonClass('btn btn-default');
        $action_edit->setLabel(_t('Edit'));
        $action_edit->setImage('fa:pencil-square-o blue fa-lg');
        $action_edit->setField('id');
        $this->datagrid->addAction($action_edit);
        
        // create DELETE action
        $action_del = new TDataGridAction(array($this, 'onDelete'));
        $action_del->setButtonClass('btn btn-default');
        $action_del->setLabel(_t('Delete'));
        $action_del->setImage('fa:trash-o red fa-lg');
        $action_del->setField('id');
        $this->datagrid->addAction($action_del);
        
        // create the datagrid model
        $this->datagrid->createModel();

        $this->list_panel = new TPanelGroup();
        $this->list_panel->add($this->datagrid);
        $this->list_panel->getBody()->style = "overflow-x:auto;";            
        
        // create the page navigation
        $this->pageNavigation = new TPageNavigation;
        $this->pageNavigation->enableCounters();
        $this->pageNavigation->setAction(new TAction(array($this, 'onReload')));
        $this->pageNavigation->setWidth($this->datagrid->getWidth());
        
        $this->list_panel->addFooter($this->pageNavigation);
        
        // vertical box container
        $container = new TVBox;
        $container->style = 'width: 99%';
        //$container->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $container->add($this->form);
        $container->add($this->list_panel);
        
        parent::add($container);
    }
}
?>
<script>
  <?php 
    $vController = 'SystemGroupList';
    echo SystemProgramComponentService::MontaJSTour($vController); 
    echo SystemProgramComponentService::MontaJSTooltip($vController);
    echo SystemProgramComponentService::MontaExecJSCarreg($vController); 
    ?> 
</script>	