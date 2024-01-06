<?php

class CadDispositivoForm extends TStandardForm
{
    protected $form; // form
    
    /**
     * Class constructor
     * Creates the page and the registration form
     */
    function __construct($param)
    {
        parent::__construct();
                
        if (TSession::getValue('usersystem') !== 'Y') {
            new TMessage('error', _t('Permission denied').' - System');
            die();
        }
        
        $this->form = new BootstrapFormBuilder('form_CadDispositivo');
        $this->form->setFormTitle(('Dispositivos'));
        
        // defines the database
        parent::setDatabase(TSession::getValue('pConn'));
        
        // defines the active record
        parent::setActiveRecord('BorDispositivo');
        
        // create the form fields
        $id            = new TEntry('id');
        $numero_serie    = new TEntry('numero_serie');
        $nome          = new TEntry('nome');
        $unit_id          = 1;
        $ativo          = 'S';
        // add the fields
        $this->form->addFields( [new TLabel('ID')], [$id] );
        $this->form->addFields( [new TLabel('Número de série')], [$numero_serie] );
        $this->form->addFields( [new TLabel('Nome')], [$nome] );
        $this->form->addFields( [new TLabel('Nome')], [$unit_id] );
        $this->form->addFields( [new TLabel('Nome')], [$ativo] );
        
        
        $id->setSize('30%');
        $nome->setSize('70%');
        $numero_serie->setSize('70%');
        
        // validations
        $nome->addValidation(_t('Nome'), new TRequiredValidator);
        $numero_serie->addValidation(('Número de série'), new TRequiredValidator);

        // add form actions
        $btn = $this->form->addAction(_t('Save'), new TAction(array($this, 'onSave')), 'fa:floppy-o');
        $btn->class = 'btn btn-sm btn-primary';
        
        $this->form->addAction(_t('Clear'), new TAction(array($this, 'onEdit')), 'fa:eraser red');
        $this->form->addAction(_t('Back'),new TAction(array('CadDispositivoList','onReload')),'fa:arrow-circle-o-left blue');

        $container = new TVBox;
        $container->style = 'width: 99%';
        //$container->add(new TXMLBreadCrumb('menu.xml','SystemProgramList'));
        $container->add($this->form);
        
        
        // add the container to the page
        parent::add($container);
    }
    
    /**
     * Change controller, generate name
     */
    public static function onChangeController($param)
    {
        if (!empty($param['controller']) AND empty($param['name']))
        {
            $obj = new stdClass;
            $obj->name = preg_replace('/([a-z])([A-Z])/', '$1 $2', $param['controller']);
            TForm::sendData('form_SystemProgram', $obj);
        }
    }
    
    /**
     * Return all the programs under app/control
     */
    public function getPrograms( $just_new_programs = false )
    {
        try
        {
            TTransaction::open(TSession::getValue('pConn'));
            $registered_programs = SystemProgram::getIndexedArray('id', 'controller');
            TTransaction::close();
            
            $entries = array();
            $iterator = new AppendIterator();
            $iterator->append(new RecursiveIteratorIterator(new RecursiveDirectoryIterator('app/control'), RecursiveIteratorIterator::CHILD_FIRST));
            $iterator->append(new RecursiveIteratorIterator(new RecursiveDirectoryIterator('app/view'),    RecursiveIteratorIterator::CHILD_FIRST));
            
            foreach ($iterator as $arquivo)
            {
                if (substr($arquivo, -4) == '.php')
                {
                    $name = $arquivo->getFileName();
                    $pieces = explode('.', $name);
                    $class = (string) $pieces[0];
                    
                    if ($just_new_programs)
                    {
                        if (!in_array($class, $registered_programs) AND !in_array($class, array_keys(TApplication::getDefaultPermissions())) AND substr($class,0,6) !== 'System')
                        {
                            $entries[$class] = $class;
                        } 
                    }
                    else
                    {
                        $entries[$class] = $class;
                    }
                }
            }
            
            ksort($entries);
            return $entries;
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
    
    /**
     * method onEdit()
     * Executed whenever the user clicks at the edit button da datagrid
     * @param  $param An array containing the GET ($_GET) parameters
     */
    public function onEdit($param)
    {
        try
        {
            if (isset($param['key']))
            {
                $key=$param['key'];
                
                TTransaction::open($this->database);
                $class = $this->activeRecord;
                $object = new $class($key);
                
                $groups = array();
                
                if( $groups_db = $object->getSystemGroups() )
                {
                    foreach( $groups_db as $group )
                    {
                        $groups[] = $group->id;
                    }
                }
                $object->groups = $groups;
                $this->form->setData($object);
                
                TTransaction::close();
                
                return $object;
            }
            else
            {
                $this->form->clear();
            }
        }
        catch (Exception $e) // in case of exception
        {
            new TMessage('error', $e->getMessage());
            TTransaction::rollback();
        }
    }
    
    /**
     * method onSave()
     * Executed whenever the user clicks at the save button
     */
    public function onSave()
    {
        try
        {
            TTransaction::open($this->database);
            
            $data = $this->form->getData();
            
            $object = new BorDispositivo;
            $object->id = $data->id;
            $object->nome = $data->nome;
            $object->numero_serie = $data->numero_serie;
            $object->ativo = 'S';
            $object->unit_id = 1;
            
            $this->form->validate();
            $object->store();
            $data->id = $object->id;
            $this->form->setData($data);
            
            $object->clearParts();

            
            TTransaction::close();
            
            new TMessage('info', AdiantiCoreTranslator::translate('Record saved'));
            
            return $object;
        }
        catch (Exception $e) // in case of exception
        {
            // get the form data
            $object = $this->form->getData($this->activeRecord);
            $this->form->setData($object);
            new TMessage('error', $e->getMessage());
            TTransaction::rollback();
        }
    }
}
