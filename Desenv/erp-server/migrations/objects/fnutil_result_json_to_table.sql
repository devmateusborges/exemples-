Drop FUNCTION IF EXISTS fnutil_result_json_to_table;
CREATE OR REPLACE FUNCTION fnutil_result_json_to_table(pJson json)
  RETURNS table(code varchar, data varchar, name varchar, msg varchar) AS $BODY$
BEGIN
  RETURN QUERY
		SELECT * from json_to_record($1) as x(code varchar, data varchar, name varchar, msg varchar);
END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100