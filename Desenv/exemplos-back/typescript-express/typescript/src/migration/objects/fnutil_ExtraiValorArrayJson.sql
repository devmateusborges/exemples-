Drop FUNCTION IF EXISTS fnutil_ExtraiValorArrayJson;
CREATE OR REPLACE FUNCTION fnutil_ExtraiValorArrayJson(pJson varchar, pValorExtraido varchar)
  RETURNS varchar AS $BODY$
declare 
	vMsg varchar := '';
	vAuxiliar varchar;
	vJson json;
	vRetornoJson varchar;	
BEGIN

	vAuxiliar := pJson;
	
	SELECT REPLACE(vAuxiliar,'data:','') into vAuxiliar;
	raise notice 'Json 1: %', vAuxiliar;
	
	SELECT REPLACE(vAuxiliar,'(','') into vAuxiliar;
	raise notice 'Json 2: %', vAuxiliar;
	
	SELECT REPLACE(vAuxiliar,')','') into vAuxiliar;
	raise notice 'Json 3: %', vAuxiliar;
	
	SELECT REPLACE(vAuxiliar,'[','') into vAuxiliar;
	raise notice 'Json 4: %', vAuxiliar;
	
	SELECT REPLACE(vAuxiliar,']','') into vAuxiliar;
	raise notice 'Json 5: %', vAuxiliar;
	
	vJson := vAuxiliar;
	
	select json_extract_path_text(vJson, pValorExtraido) into vAuxiliar;
	raise notice '%', vAuxiliar;
 
	return vAuxiliar;	
	
EXCEPTION WHEN others THEN
		SELECT json_build_object('status','error', 'data','', 'message', sqlerrm) into vRetornoJson;
    return vRetornoJson;
END;

$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100