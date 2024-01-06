Drop FUNCTION IF EXISTS fnreport_par_json;
create or replace FUNCTION fnreport_par_json(parNomeTec text,parValor text) 
Returns text 
AS $BODY$
declare
pValue varchar;
pValueTec varchar;
pRet varchar;
contador integer;

begin
  pValue := '{"params":[';
		
	for contador in 1 .. array_upper(parNomeTec, 1) loop
	
				if  contador = 1 then
				
						pValue := pValue||jsonb_build_object('parNomeTec',parNomeTec[contador], 'parValor',parValor[	contador]);	
						
				end if;
				
				if contador >= 2 then 
				
					pValue := pValue||' , '|| jsonb_build_object('parNomeTec',parNomeTec[contador], 'parValor',parValor[contador]);

				end if;
	
	end loop;
		raise notice '%:',pValue;
		pValue := pValue||']}';
		
		return pValue;

end;
$BODY$
  LANGUAGE plpgsql VOLATILE;