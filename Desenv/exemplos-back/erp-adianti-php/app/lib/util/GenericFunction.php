<?php

function soLetrasNumeros($_prString)
{
    return str_replace(" ", "", preg_replace("/[^0-9a-zA-Z\s]/", "", $_prString));
}

function soLetras($_prString)
{
    return preg_replace("/[^a-zA-Z\s]/", "", $_prString);
}

function soNumeros($_prString)
{
    return str_replace(" ", "", preg_replace("/[^0-9\s]/", "", $_prString));
}