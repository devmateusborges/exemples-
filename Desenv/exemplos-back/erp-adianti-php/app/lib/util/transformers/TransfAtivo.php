<?php
class TransfAtivo
{
    public static function t($value, $object, $row)
    {
        if ($value == "S") {
            return "<span style='color:Green'>Sim</span>";
        } else {
            return "<span style='color:red'>Não</span>";
        }
    }
}