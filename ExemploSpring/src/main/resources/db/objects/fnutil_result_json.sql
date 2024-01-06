Drop FUNCTION IF EXISTS fnutil_result_Json;
CREATE OR REPLACE FUNCTION fnutil_result_Json(pJson json)
  RETURNS table(status varchar, data varchar, message varchar) AS $BODY$
BEGIN
  RETURN QUERY
		SELECT * from json_to_record($1) as x(status varchar, data varchar, message varchar);
END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100