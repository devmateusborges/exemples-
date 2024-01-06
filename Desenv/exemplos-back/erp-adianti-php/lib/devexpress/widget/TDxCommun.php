<?php

class TDxCommun
{
    public static function DxProp($pVar,$pProp,$pAspas)
    {
        if ($pAspas) {
        return isset($pVar[$pProp]) ? ','.$pProp.': "' .$pVar[$pProp]. '"' : ' ';
    } else
    {
        return isset($pVar[$pProp]) ? ','.$pProp.':' .$pVar[$pProp] : ' '; 
    }
    }
}