<?php

class FinBancoList extends GenericStandartList
{

    const C_RECORD_CLASS   = 'FinBanco';
    const C_PERM_SYSTEM   = true;
    const C_RECORD_FIELD_ORDER  = '{"CampoBanco":"id", "Ordem":"asc"}';
    const C_RECORD_FIELD   = 
'[
{
"CampoBanco":"id", 
"Operador":"=", 
"CampoForm":"id", 
"Label":"Id", 
"Largura":"30%", 
"ExibirColuna":true,
"ColunaAlinhamento":"center",
"ColunaLargura":100,
"FuncaoSQL":"",
"Dica":"Preencha campo para Filtrar",
"Comp":{"TipoComp":"TEntry"}
}, 
{
"CampoBanco":"nome", 
"Operador":"like", 
"CampoForm":"nome", 
"Label":"Nome", 
"Largura":"70%", 
"ExibirColuna":true,
"ColunaAlinhamento":"left",
"ColunaLargura":0,
"FuncaoSQL":"upper",
"Dica":"Preencha campo para Filtrar",
"Comp":{"TipoComp":"TEntry"}
}, 
{
"CampoBanco":"ativo", 
"Operador":"like", 
"CampoForm":"ativo", 
"Label":"Ativo", 
"Largura":"30%", 
"ExibirColuna":true,
"ColunaAlinhamento":"center",
"ColunaLargura":100,
"FuncaoSQL":"",
"Dica":"Preencha campo para Filtrar",
"Comp":{"TipoComp":"TCombo",
        "ComboItens":{"S":"Sim","N":"Não"}
        },
"ColunaTransf":"TransfAtivo"
}, 
{
"CampoBanco":"nr_banco", 
"Operador":"like", 
"CampoForm":"nr_banco", 
"Label":"Nr. Banco", 
"Largura":"30%", 
"ExibirColuna":true,
"ColunaAlinhamento":"center",
"ColunaLargura":100,
"FuncaoSQL":"",
"Dica":"Preencha campo para Filtrar",
"Comp":{"TipoComp":"TEntry"},
"ColunaTransf":""
}
]';
    const C_FORM_TITLE   = 'Listagem de Banco';
    const C_FORM_CLASS_EDIT   = 'FinBancoForm';
    const C_FORM_EDIT_ROW   = true;
    const C_FORM_DEL_ROW   = true;
    const C_FORM_NEW_ROW   = true;

    public function __construct()
    {
        parent::__construct();
    }
    
}
