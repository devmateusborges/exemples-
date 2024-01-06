Drop FUNCTION IF EXISTS fnutil_primeiro_dia;
CREATE OR REPLACE FUNCTION "public"."fnutil_primeiro_dia"("pperiodo" date, "pformato" int4)
  RETURNS "pg_catalog"."varchar" AS $BODY$ DECLARE
	vPrimeiroDiaMes varchar;
	vMes varchar;
	vAno varchar;
BEGIN

	SELECT EXTRACT(MONTH FROM	((pPeriodo) :: DATE)) INTO vMes;
	
	if LENGTH(vMes) < 2 then
		vMes := '0' || vMes;
	end if;
	
	SELECT EXTRACT(YEAR FROM	((pPeriodo) :: DATE)) INTO vAno;
	vPrimeiroDiaMes := '01';
	
	if pFormato = 1 then
		vPrimeiroDiaMes := vPrimeiroDiaMes ||'/' || vMes || '/' || vAno;
	elsif pFormato = 2 then
		vPrimeiroDiaMes := vAno ||'/' || vMes || '/' || vPrimeiroDiaMes;
	end if;
	
	RETURN vPrimeiroDiaMes;

END; $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100