
<?php

class CadDispositivoList extends TStandardList
{
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
        parent::setActiveRecord('BorDispositivo');   // defines the active record
        parent::setDefaultOrder('id', 'asc');         // defines the default order
        // parent::setCriteria($criteria) // define a standard filter

        parent::addFilterField('id', '=', 'id'); // filterField, operator, formField
        parent::addFilterField('nome', 'like', 'nome'); // filterField, operator, formField
        parent::addFilterField('numero_serie', 'like', 'numero_serie'); // filterField, operator, formField
        
        // creates the form
        $this->form = new BootstrapFormBuilder('form_search_SystemProgram');
        $this->form->setFormTitle(('Dispositivos'));
        

        // create the form fields
        $nome = new TEntry('nome');
        $numero_serie = new TEntry('numero_serie');

        // add the fields
        $this->form->addFields( [new TLabel(('Nome'))], [$nome] );
        $this->form->addFields( [new TLabel(('Número de série'))], [$numero_serie] );
        $nome->setSize('70%');
        $numero_serie->setSize('70%');
        
        // keep the form filled during navigation with session data
        $this->form->setData( TSession::getValue('SystemProgram_filter_data') );
        
        // add the search form actions
        $btn = $this->form->addAction(_t('Find'), new TAction(array($this, 'onSearch')), 'fa:search');
        $btn->class = 'btn btn-sm btn-primary';
        $this->form->addAction(_t('New'),  new TAction(array('CadDispositivoForm', 'onEdit')), 'bs:plus-sign green');
        
        // creates a DataGrid
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->datatable = 'false';
        $this->datagrid->style = 'width: 100%';
        $this->datagrid->setHeight(320);
        
        // creates the datagrid columns
        $column_id = new TDataGridColumn('id', 'Id', 'center', 50);
        $column_numero_serie = new TDataGridColumn('numero_serie', 'Número de série', 'left');
        $column_nome = new TDataGridColumn('nome', 'Nome', 'left');
        
        /*$column_menu->setTransformer( function($value, $object, $row) {
            $menuparser = new TMenuParser('menu.xml');
            $paths = $menuparser->getPath($value);
            
            if ($paths)
            {
                return implode(' &raquo; ', $paths);
            }
        });*/

        // add the columns to the DataGrid
        $this->datagrid->addColumn($column_id);
        $this->datagrid->addColumn($column_numero_serie);
        $this->datagrid->addColumn($column_nome);


        // creates the datagrid column actions
        $order_id = new TAction(array($this, 'onReload'));
        $order_id->setParameter('order', 'id');
        $column_id->setAction($order_id);
        
        $order_nome = new TAction(array($this, 'onReload'));
        $order_nome->setParameter('order', 'nome');
        $column_nome->setAction($order_nome);
        
        $order_numero_serie = new TAction(array($this, 'onReload'));
        $order_numero_serie->setParameter('order', 'numero_serie');
        $column_numero_serie->setAction($order_numero_serie);
        
        // create EDIT action
        $action_edit = new TDataGridAction(array('SystemProgramForm', 'onEdit'));
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
        
        // create EXECUTE action
        $action_ope = new TDataGridAction(array($this, 'onOpen'));
        $action_ope->setButtonClass('btn btn-default');
        $action_ope->setLabel(_t('Open'));
        $action_ope->setImage('fa:folder-open-o green fa-lg');
        $action_ope->setField('numero_serie');
        $this->datagrid->addAction($action_ope);

        // create ADD MENU action
        $action_add_menu = new TDataGridAction(array($this, 'onAddMenu'));
        $action_add_menu->setDisplayCondition( array($this, 'displayAddMenu') );
        $action_add_menu->setButtonClass('btn btn-default');
        $action_add_menu->setLabel(_t('Add to menu'));
        $action_add_menu->setImage('fa:plus green fa-lg');
        $action_add_menu->setFields(['numero_serie', 'nome']);
        
        // create DEL MENU action
        $action_del_menu = new TDataGridAction(array($this, 'onDelMenu'));
        $action_del_menu->setDisplayCondition( array($this, 'displayDelMenu') );
        $action_del_menu->setButtonClass('btn btn-default');
        $action_del_menu->setLabel(_t('Remove from menu'));
        $action_del_menu->setImage('fa:times red fa-lg');
        $action_del_menu->setField('numero_serie');
        
        $action_group = new TDataGridActionGroup('', 'fa:list');
        $action_group->addHeader('Menu');
        $action_group->addAction($action_add_menu);
        $action_group->addAction($action_del_menu);
        
        // add the actions to the datagrid
        $this->datagrid->addActionGroup($action_group);
        
        $ini = AdiantiApplicationConfig::get();
        
        if ((TSession::getValue('login') == 'admin') && isset($ini['general']['token']))
        {
            $action_edit_page = new TDataGridAction(array('SystemPageService', 'editPage'));
            $action_edit_page->setButtonClass('btn btn-default');
            $action_edit_page->setLabel(_t('Edit page'));
            $action_edit_page->setImage('fa:external-link green fa-lg');
            $action_edit_page->setField('numero_serie');
            $action_edit_page->setDisplayCondition( array($this, 'displayBuilderActions') );
            $this->datagrid->addAction($action_edit_page);
        }
        
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
    
    /**
     * Display condition for add to menu option
     */
    public function displayAddMenu($object)
    {
        $menuparser = new TMenuParser('menu.xml');
        return count((array) $menuparser->getPath($object->controller)) == 0;
    }
    
    /**
     * Display condition for del from menu option
     */
    public function displayDelMenu($object)
    {
        $menuparser = new TMenuParser('menu.xml');
        return count((array) $menuparser->getPath($object->controller)) > 0;
    }
    
    /**
     * Open controller
     */
    public function onOpen($param)
    {
        AdiantiCoreApplication::loadPage($param['controller']);
    }
    
    /**
     * Add item on menu
     */
    public function onAddMenu($param)
    {
        try
        {
            TTransaction::open(TSession::getValue('pConn'));
            
            $modules = (new TMenuParser('menu.xml'))->getModules();
            
            $form = new TQuickForm('input_form');
            $form->class = 'input_form';
            $form->style = 'padding:20px';
            
            $module = new TCombo('module');
            $module->addItems($modules);
            $module->enableSearch();
            
            $name = new TEntry('name');
            
            $icon = new TIcon('icon');
            $icon->setValue('fa-circle-o');
            
            $form->addQuickField(_t('Module'), $module);
            $form->addQuickField(_t('Name'), $name);
            $form->addQuickField(_t('Icon'), $icon);
            
            $module->setSize('70%');
            $icon->setSize('70%');
            $name->setSize('70%');
            
            $name->setValue($param['name']);
            
            $action = new TAction(array($this, 'addItemMenu'));
            $action->setParameters($param);
            
            $form->addQuickAction(_t('Add'), $action, 'fa:save green');
            new TInputDialog(_t('Add to menu'), $form);
            
            TTransaction::close();
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
    
    /**
     * Add item at menu
     */
    public function addItemMenu($param)
    {
        try
        {
            TTransaction::open(TSession::getValue('pConn'));
            
            $menu = new TMenuParser('menu.xml');
            $menu->appendPage( $param['module'], $param['name'], $param['controller'], str_replace('fa-', 'fa:', $param['icon'] . ' fa-fw'));
            
            $posaction = new TAction([$this, 'onReload']);
            new TMessage('info', _t('Item added to menu'), $posaction);
            TTransaction::close();
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
    
    /**
     * Remove item from menu
     */
    public function onDelMenu($param)
    {
        try
        {
            TTransaction::open(TSession::getValue('pConn'));
            
            $menu = new TMenuParser('menu.xml');
            $menu->removePage($param['controller']);
            
            $posaction = new TAction([$this, 'onReload']);
            new TMessage('info', _t('Item removed from menu'), $posaction);
            TTransaction::close();
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
    
    /**
     * Display condition
     */
    public function displayBuilderActions($object)
    {
        return ( (strpos($object->controller, 'System') === false) and !in_array($object->controller, ['CommonPage', 'WelcomeView']));
    }
}
