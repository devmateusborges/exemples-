<?php

class SystemRegistrationForm extends TPage
{
    protected $form; // form
    protected $program_list;
    
    /**
     * Class constructor
     * Creates the page and the registration form
     */
    function __construct()
    {
        parent::__construct();
        
        // creates the form
        $this->form = new BootstrapFormBuilder('form_registration');
        $this->form->setFormTitle( _t('User registration') );
        
        // create the form fields
        $login          = new TEntry('login');
        $login->style   = "text-transform: lowercase";
        $login->id      = "edlogin";
        $name           = new TEntry('name');
        $login->id      = "edname";
        $email          = new TEntry('email');
        $email->id      = "edemail";
        $email->style   = "text-transform: lowercase";
        $phone       = new TEntry('phone');
        $phone->id   = "edphone";
        $password       = new TPassword('password');
        $password->id   = "edpassword";
        $repassword     = new TPassword('repassword');
        $repassword->id = "edrepassword";
        
        $this->form->addAction( _t('Save'),  new TAction([$this, 'onSave']), 'fa:floppy-o')->{'class'} = 'btn btn-sm btn-primary';
        $this->form->addAction( _t('Clear'), new TAction([$this, 'onClear']), 'fa:eraser red' );
        $btn1 = $this->form->addAction(_t('Back'), new TAction(array($this, 'onBack')), 'fa:arrow-circle-o-left blue');
  		
        // define the sizes
        $name->setSize('100%');
        $login->setSize('100%');
        $password->setSize('100%');
        $repassword->setSize('100%');
        $email->setSize('100%');
        
        $this->form->addFields( [new TLabel(_t('Login'), 'red')],    [$login] );
        $this->form->addFields( [new TLabel(_t('Name'), 'red')],     [$name] );
        $this->form->addFields( [new TLabel(_t('Email'), 'red')],    [$email] );
        $this->form->addFields( [new TLabel(_t('Phone'), 'red')], [$phone] );
        $this->form->addFields( [new TLabel(_t('Password'), 'red')], [$password] );
        $this->form->addFields( [new TLabel(_t('Password confirmation'), 'red')], [$repassword] );
        
        // add the container to the page
        parent::add($this->form);
    }
    
    /**
     * Clear form
     */
    public function onClear()
    {
        $this->form->clear( true );
    }
    
    /**
     * method onSave()
     * Executed whenever the user clicks at the save button
     */
    public static function onSave($param)
    {

        $systemUserService = new SystemUserService();
        $vreturn = $systemUserService->Registration($param);
        if ($vreturn == 'OK') {
            $param['pConn']='conn';
            $pos_action = new TAction(['LoginForm', 'onLoad']);
            new TMessage('info', _t('Account created, email sent to account activation'), $pos_action);
        } else
        {
            new TMessage('erro',$vreturn);   
        }
   
    }
    
   public static function onBack($param)
    {
		AdiantiCoreApplication::loadPage('LoginForm');
	}			
}
