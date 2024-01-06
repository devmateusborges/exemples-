<?php

class GerMarcaForm extends GenericStandartForm
{

    const C_RECORD_CLASS   = 'GerMarca';
    const C_PERM_SYSTEM   = true;
    const C_RECORD_FIELD   = 
'[ 
{
"CampoForm":"id",
"Label":"Id",
"Largura":"30%",
"Obrigatorio":false,
"NumCaracterMinimo":0,
"NumCaracterMaximo":0,
"Dica":"Preencha campo para Cadastrar",
"Comp" :{"TipoComp":"TEntry"}
},
{
"CampoForm":"nome",
"Label":"Nome",
"Largura":"70%",
"Obrigatorio":true,
"NumCaracterMinimo":10,
"NumCaracterMaximo":0,
"Dica":"Preencha campo para Cadastrar",
"Comp":{"TipoComp":"TEntry"}
},
{
"CampoForm":"ativo",
"Label":"Ativo",
"Largura":"30%",
"Obrigatorio":true,
"NumCaracterMinimo":0,
"NumCaracterMaximo":0,
"Dica":"Preencha campo para Cadastrar",
"Comp":{"TipoComp":"TCombo",
        "ComboItens":{"S":"Sim","N":"Não"}
       }
}
]';
    const C_FORM_LIST   = 'GerMarcaList';
    const C_FORM_TITLE   = 'Cadastro de Marca';
    const C_FORM_SAVE   = true;
    const C_FORM_BACK   = true;

    function __construct()
    {
        parent::__construct();
     
    }
}
