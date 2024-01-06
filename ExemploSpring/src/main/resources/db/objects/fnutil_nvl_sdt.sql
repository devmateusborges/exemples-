drop function if EXISTS fnutil_nvl_sdt;
create or replace FUNCTION fnutil_nvl_sdt(
pParCampo varchar,
pParTypeOperation varchar,
pParEntrada varchar)
returns TIMESTAMP as 
$function$
declare
begin

	IF pParCampo = pParTypeOperation then		
			return fnutil_sdt(pParEntrada);
	else
			return pParCampo;
	end if;

end;
$function$
LANGUAGE plpgsql VOLATILE;

-- select * from fnutil_nvl_sdt('%','%','I')
