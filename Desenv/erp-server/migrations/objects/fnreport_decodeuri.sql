Drop FUNCTION IF EXISTS fnreport_decodeuri;
create or replace function fnreport_decodeuri(pUri varchar)
returns varchar as
$$
declare
		vReplace varchar;
begin
    vReplace = pUri;
		vReplace = REPLACE(vReplace,'%27',chr(39));
		vReplace = REPLACE(vReplace,'%20',chr(45));
		vReplace = REPLACE(vReplace,'%C3%AD',chr(237));		
		vReplace = REPLACE(vReplace,'%22',chr(34));
		if substr(vReplace,1,1) <> chr(39) then
		vReplace = chr(39)||vReplace||chr(39);
		end if;
		
		--raise notice 'Select replace %',vReplace;
		return vReplace;
end;
$$
language plpgsql;


