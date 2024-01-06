<?php

class GerMarcaList extends GenericStandartList
{

    const C_RECORD_CLASS   = 'GerMarca';
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
}
]';
    const C_FORM_TITLE   = 'Listagem de Marca';
    const C_FORM_CLASS_EDIT   = 'GerMarcaForm';
    const C_FORM_EDIT_ROW   = true;
    const C_FORM_DEL_ROW   = true;
    const C_FORM_NEW_ROW   = true;

    public function __construct()
    {
        parent::__construct();
    }
}
