drop function if exists fnutil_ini_fim_semana;

CREATE OR REPLACE FUNCTION fnutil_ini_fim_semana(pvGerPerTipo character varying, pDtIni date, pDtFin integer)
 RETURNS date
 LANGUAGE plpgsql
AS $function$
declare
    v_ini_semana integer;
    v_day_of_week integer;
    v_date date;
begin
-- Recuperando configuracao de inicio da semana
    select to_number(coalesce(ini_semana,'0'),'9')
    into v_ini_semana
    from ger_per_tipo t
    where t.id = pvGerPerTipo;
    v_day_of_week := EXTRACT(DOW from pDtIni);

    -- data de inicio da semana
    if pDtFin = 0 then
    if (v_day_of_week >= v_ini_semana) then
        v_date := pDtIni - (v_day_of_week - v_ini_semana);
    else
        v_date := pDtIni - (v_day_of_week - v_ini_semana + 7);
    end if;
    end if;

    -- data de Fin da semana
    if pDtFin = 1 then
    if (v_ini_semana <= v_day_of_week) then
        v_date := pDtIni + (v_ini_semana - v_day_of_week + 6);
    else
        v_date := pDtIni + (v_ini_semana - v_day_of_week - 1);
    end if;
    end if;

    return v_date;
exception
    when others then
    Return 'fnutil_ini_fim_semana ERRO: ' || sqlerrm;
end;
$function$
;
