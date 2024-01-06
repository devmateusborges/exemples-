<?php

class SystemUnitList extends GenericStandartList
{

    const C_RECORD_CLASS   = "SystemUnit";
    const C_PERM_SYSTEM   = true;
    const C_RECORD_FIELD_ORDER = '{"CampoBanco":"id", "Ordem":"asc"}';
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
  "Comp":{"TipoComp":"TEntry"}
  }, 
  {
  "CampoBanco":"name", 
  "Operador":"like", 
  "CampoForm":"name", 
  "Label":"Nome", 
  "Largura":"70%", 
  "ExibirColuna":true,
  "ColunaAlinhamento":"left",
  "ColunaLargura":0,
  "FuncaoSQL":"upper",
  "Comp":{"TipoComp":"TEntry"}
  }
  ]';
    const C_FORM_TITLE   = "Listagem de Unidade";
    const C_FORM_CLASS_EDIT   = "SystemUnitForm";
    const C_FORM_EDIT_ROW   = true;
    const C_FORM_DEL_ROW   = true;
    const C_FORM_NEW_ROW   = true;

    public function __construct()
    {
        parent::__construct();
    }
    
}
   