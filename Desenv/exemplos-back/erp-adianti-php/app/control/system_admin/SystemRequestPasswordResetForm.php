<?php


class SystemRequestPasswordResetForm extends TPage
{
    protected $form; // form
    
    /**
     * Class constructor
     * Creates the page and the registration form
     */
    function __construct($param)
    {
        parent::__construct();
        
        $this->style = 'clear:both';
        // creates the form
        $this->form = new BootstrapFormBuilder('form_login');
        $this->form->setFormTitle( _t('Reset password') );
        
        // create the form fields
        $login = new TEntry('login');
        
        // define the sizes
        $login->setSize('70%', 40);
        
        $login->style = 'text-transform: lowercase; height:35px; font-size:14px;float:left;border-bottom-left-radius: 0;border-top-left-radius: 0;';
        $login->placeholder = _t('User');
        $user = '<span style="float:left;margin-left:44px;height:35px;" class="login-avatar"><span class="glyphicon glyphicon-user"></span></span>';
        $this->form->addFields( [$user, $login] );
        
        $btn = $this->form->addAction(_t('Send'), new TAction(array($this, 'onRequest')), '');
        $btn->class = 'btn btn-primary';
        $btn->style = 'height: 40px;width: 90%;display: block;margin: 20px;font-size:17px;';
        
        $btn1 = $this->form->addAction(_t('Back'), new TAction(array($this, 'onBack')), '');
        $btn1->class = 'btn btn-default';
        $btn1->style = 'height: 40px;width: 90%;display: block;margin: 20px;font-size:17px;';
        		
     
		
		
        $wrapper = new TElement('div');
        $wrapper->style = 'margin:auto; margin-top:100px;max-width:460px;';
        $wrapper->id    = 'login-wrapper';
        $wrapper->add($this->form);
        
        // add the form to the page
        parent::add($wrapper);
    }
    

    /**
     * Authenticate the User
     */

    public static function onRequest($param)
    {

        $systemUserService = new SystemUserService();
        $vreturn = $systemUserService->RequestNewPassword($param);
        if ($vreturn == 'OK') {
            $param['pConn']='conn';
            $pos_action = new TAction(['LoginForm', 'onLoad']);
            new TMessage('info', _t('Email sent successfully'),$pos_action);
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
