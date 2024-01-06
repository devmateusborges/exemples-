drop function if exists fnutil_table_id;

CREATE OR REPLACE FUNCTION fnutil_table_id(pids varchar, pidnull varchar)
RETURNS TABLE("id" varchar) AS $BODY$
declare
vSql varchar;
vIdNull varchar;
r record;
begin

	if pids != ''  or pids != null then
		vSql = 'select unnest(string_to_array('''|| pids ||''', '','')) as idaux ';
	else
		vSql = 'select unnest(string_to_array('''|| pidnull ||''', '','')) as idaux ';
	end if;
	
  for r in execute vSql
 	loop
		id = r.idaux;
		return next;
		raise notice 'teste :%', 1;
 	
 	end loop;	
return;
end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100
  ROWS 1000