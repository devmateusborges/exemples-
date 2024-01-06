CREATE OR REPLACE FUNCTION public.fnsystem_psql_result(pid character varying, psystem_user_id character varying, presultado character varying, pstatus character varying default '')
 RETURNS character varying
 LANGUAGE plpgsql
AS $function$
declare 
    vRetornoJson varchar;	
BEGIN
    --apaga as com mais de 24 horas de idade
    delete from system_psql_result where dt_hr <= NOW() - INTERVAL '24 HOUR';

    if (pstatus = '') then
        pstatus := 'S';
    END if;

    insert into system_psql_result(id, system_user_id, resultado, status) values (pid, psystem_user_id, presultado, pstatus);

    SELECT json_build_object('status','success', 'data','Sucesso') INTO vRetornoJson;
	return vRetornoJson;
    exception
        when others then
            begin
            SELECT json_build_object(
                'status', 'error',
                'message', sqlerrm) INTO vRetornoJson;
         return vRetornoJson;
        end;   
	
END;
$function$;
