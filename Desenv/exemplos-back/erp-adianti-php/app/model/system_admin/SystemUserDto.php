<?php
/************************************************************************************************************
 Proprietario: AGROBOT
 Descrição...: Classe para DTO de Usuários
 Nome                 Data       Alteracao
 -------------------- ---------- ---------------------------------------------------------------------------
 EJ                   06/04/2019 Criacao
************************************************************************************************************/

class SystemUserDto extends TRecord
{
    const TABLENAME = 'system_user';
    const PRIMARYKEY= 'id';
    const IDPOLICY =  'max'; // {max, serial}

    
    public function __construct($id = NULL)
    {
        parent::__construct($id);
        parent::addAttribute('name');
        parent::addAttribute('login');
        parent::addAttribute('active');
    }

   
}
