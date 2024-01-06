drop function if exists public.fnutil_ini_fim_semana;

CREATE OR REPLACE FUNCTION public.fnutil_ini_fim_semana(p_ger_empresa_id character varying, p_dt_ini date, p_dt_fin integer)
 RETURNS date
 LANGUAGE plpgsql
AS $function$
declare
    v_ini_semana integer;
    v_day_of_week integer;
    v_date date;
begin
-- Recuperando configuração de início da semana
    select coalesce(ini_semana,0)
    into v_ini_semana
    from ger_empresa t
    where t.id = p_ger_empresa_id;
    v_day_of_week := EXTRACT(DOW from p_dt_ini);

    -- data de início da semana
    if p_dt_fin = 0 then
    if (v_day_of_week >= v_ini_semana) then
        v_date := p_dt_ini - (v_day_of_week - v_ini_semana);
    else
        v_date := p_dt_ini - (v_day_of_week - v_ini_semana + 7);
    end if;
    end if;

    -- data de Fin da semana
    if p_dt_fin = 1 then
    if (v_ini_semana <= v_day_of_week) then
        v_date := p_dt_ini + (v_ini_semana - v_day_of_week + 6);
    else
        v_date := p_dt_ini + (v_ini_semana - v_day_of_week - 1);
    end if;
    end if;

    return v_date;
exception
    when others then
    Return 'fnutil_ini_fim_semana ERRO: ' || sqlerrm;
end;
$function$
;
