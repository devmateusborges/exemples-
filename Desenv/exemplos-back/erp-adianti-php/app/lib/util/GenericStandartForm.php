<?php
class GenericStandartForm extends TStandardForm
{
    const C_UNITID   = true;
    const C_RECORD_CLASS   = '';
    const C_PERM_SYSTEM   = false;
    const C_RECORD_FIELD   = ''; 
    /*0-CampoForm
      1-Label
      2-Largura
      3-Comp
         0-TipoComp
    */     
    const C_FORM_LIST   = '';
    const C_FORM_TITLE   = '';
    const C_FORM_SAVE   = true;
    const C_FORM_BACK   = true;
    
    protected $form;
  
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

        $this->form = new BootstrapFormBuilder('form_' . constant("{$class}::C_RECORD_CLASS"));
        $this->form->setFormTitle(constant("{$class}::C_FORM_TITLE"));
        $VRECORD_FIELD =  json_decode(constant("{$class}::C_RECORD_FIELD"),true);
   
        foreach ($VRECORD_FIELD as $key => $item ) {
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

            ${$item['CampoForm']}->setSize($item['Largura']);

            if ($item['Obrigatorio']) {
                ${$item['CampoForm']}->addValidation($item['Label'], new TRequiredValidator);  
            }
            if ($item['NumCaracterMinimo'] > 0) {
                ${$item['CampoForm']}->addValidation($item['Label'], new TMinLengthValidator, array($item['NumCaracterMinimo']));  
            }
            if ($item['NumCaracterMaximo'] > 0) {
                ${$item['CampoForm']}->addValidation($item['Label'], new TMaxValueValidator, array($item['NumCaracterMaximo']));  
            }   
            
            if (!empty($item['Dica'])) {
                ${$item['CampoForm']}->setTip($item['Dica']);
            }

            $this->form->addFields([new TLabel($item['Label'])], [${$item['CampoForm']}]);
        }

        
        if (constant("{$class}::C_FORM_SAVE")) {
            $btn = $this->form->addAction(_t('Save'), new TAction(array($this, 'onSave')), 'fa:floppy-o');
            $btn->class = 'btn btn-sm btn-primary';
            $this->form->addAction(_t('Clear'),  new TAction(array($this, 'onEdit')), 'fa:eraser red');
        }
        if (constant("{$class}::C_FORM_BACK")) {
        $this->form->addAction(_t('Back'),new TAction(array(constant("{$class}::C_FORM_LIST"),'onReload')),'fa:arrow-circle-o-left blue');
        }
        $container = new TVBox;
        $container->style = 'width: 99%';
        $container->add($this->form);

        parent::add($container);
    }
}
