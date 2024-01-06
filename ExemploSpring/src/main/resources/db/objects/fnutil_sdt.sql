Drop FUNCTION IF EXISTS fnutil_sdt;
CREATE OR REPLACE FUNCTION public.fnutil_sdt(pTp varchar)
  RETURNs TIMESTAMP AS $BODY$
DECLARE
    vResult TIMESTAMP;	
BEGIN
 
 if pTp = 'I' then
   SELECT TO_TIMESTAMP('1900-01-01 12:00:00', 'YYYY-MM-DD HH24:MI:SS') into vResult;
	 
 end if;
 
 if pTp = 'F' then
	 SELECT TO_TIMESTAMP('2999-12-31 12:00:00', 'YYYY-MM-DD HH24:MI:SS') into vResult;
	 
 end if;
 

RETURN vResult;
		
END;
$BODY$
  LANGUAGE plpgsql VOLATILE
  