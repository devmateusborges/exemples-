<?php

const C_RECORD_FIELD   = [['f1','=','fc1'],['f2','like','fc2']]; //[Campo Banco,Operador,Campo Form,Label,Largura,Coluna]
 
$VRECORD_FIELD = C_RECORD_FIELD;
foreach ($VRECORD_FIELD as $item) {
var_dump($item[1]);
}