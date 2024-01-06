<?php

class SystemPermissionUpdate extends TPage
{
    /**
     * Constructor method
     */
    public function __construct()
    {
        parent::__construct();
        
        if (TSession::getValue('usersystem') !== 'Y') {
            new TMessage('error', _t('Permission denied').' - System');
            die();
        }
    }
    
    /**
     * Ask for Update menu
     */
    public function onAskUpdate()
    {
        try
        {
            if (!file_exists('menu-dist.xml'))
            {
                throw new Exception(_t('File not found') . ':<br> menu-dist.xml');
            }
            
            $action = new TAction(array($this, 'onUpdatePermissions'));
            new TQuestion(_t('Update permissions?'), $action);
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
    
    /**
     * Update menu
     */
    public static function onUpdatePermissions($param)
    {
        try
        {
            $permissions = SystemPageService::getPermissions();
            
            if ($permissions)
            {
                TTransaction::open(TSession::getValue('pConn'));
                
                foreach ($permissions as $group => $programs)
                {
                    $system_group = SystemGroup::where('name','=',$group)->first();
                    
                    if (empty($system_group))
                    {
                        $system_group = new SystemGroup;
                        $system_group->name = $group;
                        $system_group->store();
                    }
                    
                    if ($programs)
                    {
                        foreach ($programs as $controller => $name)
                        {
                            $system_program = SystemProgram::findByController($controller);
                            
                            if (empty($system_program))
                            {
                                $system_program = new SystemProgram;
                                $system_program->name = $name;
                                $system_program->controller = $class_name;
                                $system_program->store();
                            }
                            
                            $system_group->addSystemProgram($system_program);
                        }
                    }
                }
                TTransaction::close();
            }
            LoginForm::reloadPermissions();
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
}
