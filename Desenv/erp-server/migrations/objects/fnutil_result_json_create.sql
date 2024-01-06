Drop FUNCTION IF EXISTS fnutil_result_json_create;
CREATE OR REPLACE FUNCTION fnutil_result_json_create(pncode numeric, pvdata json, pvname varchar, pvmsg varchar)
  RETURNS varchar AS $BODY$
declare
		vResult json;
begin
		select json_build_object(
						 'code',pncode,
						 'data', pvdata,
						 'name',pvname,
						 'msg', pvmsg) INTO vResult;
						 return vResult;
end;
$BODY$
  language plpgsql volatile
  cost 100