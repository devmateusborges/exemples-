<?php

class LoginForm extends TPage
{
    protected $form; // form
    
    /**
     * Class constructor
     * Creates the page and the registration form
     */
    function __construct($param)
    {
        parent::__construct();
        
        $ini  = AdiantiApplicationConfig::get();
        
        $this->style = 'clear:both';
        // creates the form
        $this->form = new BootstrapFormBuilder('form_login');
        $this->form->setFormTitle( _t('Log in'));
        
		$BtnTour = new TButton('btntuor');
        $BtnTour->setLabel('Help');
		$BtnTour->class = 'btn bg-pink';
        $BtnTour->setImage('fa:question-circle');
		$BtnTour->addFunction("LoginFormTour()");
		
		
        // create the form fields
        $login = new TEntry('login');
        $login->class = 'slogin';
        $password = new TPassword('password');
        $password->class = 'spassword';
        
        // define the sizes
        $login->setSize('70%', 40);
        $password->setSize('70%', 40);

        $login->style = 'height:35px; font-size:14px;float:left;border-bottom-left-radius: 0;border-top-left-radius: 0;';
        $password->style = 'height:35px;font-size:14px;float:left;border-bottom-left-radius: 0;border-top-left-radius: 0;';
        
        $login->placeholder = _t('User');
        $password->placeholder = _t('Password');
        
        $login->autofocus = 'autofocus';

        $user = '<span style="float:left;margin-left:44px;height:35px;" class="login-avatar"><span class="glyphicon glyphicon-user"></span></span>';
        $locker = '<span style="float:left;margin-left:44px;height:35px;" class="login-avatar"><span class="glyphicon glyphicon-lock"></span></span>';
        $unit = '<span style="float:left;margin-left:44px;height:35px;" class="login-avatar"><span class="fa fa-university"></span></span>';
        
        $this->form->addFields( [$user, $login,] );
        $this->form->addFields( [$locker, $password] );
        
        if (!empty($ini['general']['multiunit']) and $ini['general']['multiunit'] == '1')
        {
            $unit_id = new TCombo('unit_id');
            $unit_id->class = 'sunit_id';
            $unit_id->setSize('70%');
            $unit_id->style = 'height:35px;font-size:14px;float:left;border-bottom-left-radius: 0;border-top-left-radius: 0;';
            $this->form->addFields( [$unit, $unit_id] );
            $login->setExitAction(new TAction( [$this, 'onExitUser'] ) );
        }
        
        
		$btn = $this->form->addAction(_t('Log in'), new TAction(array($this, 'onLogin')), '');
        $btn->class = 'sBtnLogin btn btn-primary';
        $btn->style = 'height: 40px;width: 90%;display: block;margin: 20px;font-size:17px;';
        
        $btn1 = $this->form->addAction('Criar Usuário', new TAction(array($this, 'onCadUsu')), '');
		$btn1->class = 'sBtnCadUsu btn btn-default';
        $btn1->style = 'height: 40px;width: 90%;display: block;margin: 20px;font-size:17px;padding-top:10px !important;';
        
        $btn2 = $this->form->addAction('Recuperar Senha', new TAction(array($this, 'onRecSenha')), '');
        $btn2->class = 'sBtnRecSenha btn btn-default';
        $btn2->style = 'height: 40px;width: 90%;display: block;margin: 20px;font-size:17px;padding-top:10px !important;';
        		
		
        $wrapper = new TElement('div');
        $wrapper->style = 'margin:auto; margin-top:100px;max-width:460px;';
        $wrapper->id    = 'login-wrapper';
        $wrapper->add($this->form);
		$wrapper->add($BtnTour);
        
		// add the form to the page
        parent::add($wrapper);

		if (!empty($param['jwt'])) {
            self::onActiveUserWelcome($param);
        }				 
		
    }
    
    /**
     * user exit action
     * Populate unit combo
     */
    public static function onExitUser($param)
    {
        try
        {
            TTransaction::open(TSession::getValue('pConn'));
            
            $user = SystemUser::newFromLogin( $param['login'] );
            if ($user instanceof SystemUser)
            {
                
                $units = $user->getSystemUserUnits();
                $options = [];
                
                if ($units)
                {
                    foreach ($units as $unit)
                    {
                        $options[$unit->id] = $unit->name;
                    }
                }
                TCombo::reload('form_login', 'unit_id', $options);
            } 
            
            TTransaction::close();
        }
        catch (Exception $e)
        {
            new TMessage('error',$e->getMessage());
            TTransaction::rollback();
        }
    }
    
    /**
     * Authenticate the User
     */
    public static function onLogin($param)
    {
        $ini  = AdiantiApplicationConfig::get();
        
        try
        {
            TTransaction::open(TSession::getValue('pConn'));
            $data = (object) $param;
            
            if (empty($data->login))
            {
                throw new Exception( AdiantiCoreTranslator::translate('The field ^1 is required', _t('Login')) );
            }
            
            if (empty($data->password))
            {
                throw new Exception( AdiantiCoreTranslator::translate('The field ^1 is required', _t('Password')) );
            }
            
            $user = SystemUser::validate( $data->login );

            if (!empty($ini['general']['multiunit']) and $ini['general']['multiunit'] == '1' and empty($data->unit_id))
            {    
                throw new Exception( AdiantiCoreTranslator::translate('The field ^1 is required', _t('Unit')) );
            }
            

            
            if ($user)
            {
                if (!empty($ini['permission']['auth_service']) and class_exists($ini['permission']['auth_service']))
                {
                    $service = $ini['permission']['auth_service'];
                    $service::authenticate( $data->login, $data->password );
                }
                else
                {
                    SystemUser::authenticate( $data->login, $data->password );
                }
                
                TSession::regenerate();
                $programs = $user->getPrograms();
                $programs['LoginForm'] = TRUE;
                
                TSession::setValue('logged', TRUE);
                TSession::setValue('login', $data->login);
                TSession::setValue('userid', $user->id);
                TSession::setValue('usersystem', $user->system);
                TSession::setValue('usergroupids', $user->getSystemUserGroupIds());
                TSession::setValue('userunitids', $user->getSystemUserUnitIds());
                TSession::setValue('username', $user->name);
                TSession::setValue('usermail', $user->email);
                TSession::setValue('frontpage', '');
                TSession::setValue('programs',$programs);
                
               
                if (!empty($ini['general']['multiunit']) and $ini['general']['multiunit'] == '1' and !empty($data->unit_id))
                {
                    TSession::setValue('userunitid', $data->unit_id );

                    $unitObj = new SystemUnit($data->unit_id);

                    TSession::setValue('unitname', $unitObj->name );

                }

                if (empty($data->unit_id))
                {
                    new TMessage('error', _t('Selecionar Unidade para Login'));
                    die();
                }
                
                $frontpage = $user->frontpage;
                
                SystemAccessLog::registerLogin();
                
                if ($frontpage instanceof SystemProgram and $frontpage->controller)
                {
                    AdiantiCoreApplication::gotoPage($frontpage->controller); // reload
                    TSession::setValue('frontpage', $frontpage->controller);
                }
                else
                {
                    AdiantiCoreApplication::gotoPage('EmptyPage'); // reload
                    TSession::setValue('frontpage', 'EmptyPage');
                }
            }
            TTransaction::close();
        }
        catch (Exception $e)
        {
            new TMessage('error',$e->getMessage());
            TSession::setValue('logged', FALSE);
            TTransaction::rollback();
        }
    }
    
    /** 
     * Reload permissions
     */
    public static function reloadPermissions()
    {
        try
        {
            TTransaction::open(TSession::getValue('pConn'));
            $user = SystemUser::newFromLogin( TSession::getValue('login') );
            
            if ($user)
            {
                $programs = $user->getPrograms();
                $programs['LoginForm'] = TRUE;
                TSession::setValue('programs', $programs);
                
                $frontpage = $user->frontpage;
                if ($frontpage instanceof SystemProgram AND $frontpage->controller)
                {
                    TApplication::gotoPage($frontpage->controller); // reload
                }
                else
                {
                    TApplication::gotoPage('EmptyPage'); // reload
                }
            }
            TTransaction::close();
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
    
    /**
     *
     */
    public function onLoad($param)
    {
		
    }
	
    
    /**
     * Logout
     */
    public  function onLogout()
    {
        SystemAccessLog::registerLogout();
        TSession::freeSession();
        $param['pConn']='conn';
        AdiantiCoreApplication::gotoPage('LoginForm', null, $param);
    }
	
    public  function onCadUsu($param)
    {
		AdiantiCoreApplication::loadPage('SystemRegistrationForm');
		
	}
    public  function onRecSenha($param)
    {
		AdiantiCoreApplication::loadPage('SystemRequestPasswordResetForm');
	}	
    
    public static function onActiveUserWelcome($param)
    {
        $systemUserService = new SystemUserService();
        $vreturn = $systemUserService->ActiveUserWelcome($param);
        if ($vreturn == 'OK') {
            $param['pConn']='conn';
            $pos_action = new TAction(['LoginForm', 'onLoad']);
            new TMessage('info', _t('User activated successfully'), $pos_action);
        } else
        {
            new TMessage('erro',$vreturn);   
        }        
   
    }    
}
?>
<script>
  <?php
   $vController = 'LoginForm';
   echo SystemProgramComponentService::MontaJSTour($vController);  
   echo SystemProgramComponentService::MontaJSTooltip($vController);
   echo SystemProgramComponentService::MontaExecJSCarreg($vController); 
  ?>
</script>	
	    