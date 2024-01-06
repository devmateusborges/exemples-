<?php

class SystemUnitForm extends GenericStandartForm
{

    const C_RECORD_CLASS   = "SystemUnit";
    const C_PERM_SYSTEM   = true;
    const C_RECORD_FIELD   = 
'[ {"CampoForm":"id",
        "Label":"Id",
        "Largura":"30%",
        "Comp" :{"TipoComp":"TEntry"}
        },
{"CampoForm":"name",
       "Label":"Nome",
       "Largura":"70%",
       "Comp":{"TipoComp":"TEntry"}
      }
]';

    const C_FORM_LIST   = "SystemUnitList";
    const C_FORM_TITLE   = "Cadastro de Unidade";
    const C_FORM_SAVE   = true;
    const C_FORM_BACK   = true;

    function __construct()
    {
        parent::__construct();
     
    }
}
