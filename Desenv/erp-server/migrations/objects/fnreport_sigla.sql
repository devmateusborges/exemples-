Drop FUNCTION IF EXISTS fnreport_sigla;
create or replace function fnreport_sigla(pParUnitId varchar, pTabela varchar, pCampoSigla varchar, pCampoWhere varchar, pValorWhere varchar)
returns varchar as
$$
declare
    vSql varchar;
		vRet varchar;
		vExistUnitId integer := 0;
begin
	
		select count(1)
			into 	vExistUnitId
			from information_schema.columns  where upper(table_name) = upper(pTabela)  and upper(column_name) = 'UNIT_ID';

	    vSql := 'select STRING_AGG(t1.'||pCampoSigla||', '' ; '' ORDER BY t1.'||pCampoSigla||') AS grp
			           from '||pTabela||' t1
			          where '||pCampoWhere||' in('||pValorWhere||')';
			
			
			if (vExistUnitId > 0) and (pParUnitId != null) then
		   	vSql := vSql || ' and unit_id = '''||pParUnitId||'''' ;
			end if;
		
		 --raise notice 'fnreport_sigla Sql:%', vSql;

    execute vSql into vRet;

    return vRet;

end;
$$
language plpgsql;


