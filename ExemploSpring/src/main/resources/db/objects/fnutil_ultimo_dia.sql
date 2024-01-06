Drop FUNCTION IF EXISTS fnutil_ultimo_dia;
CREATE OR REPLACE FUNCTION "public"."fnutil_ultimo_dia"("mes" int4, "ano" int4, "formato" int4)
  RETURNS "pg_catalog"."varchar" AS $BODY$ DECLARE
	UltimoDiaMes varchar;
	vMes integer;
BEGIN
	
	if (Mes + 1) > 12 then
		vMes := 0;
	else 
		vMes := Mes;
	end if;
	
	SELECT EXTRACT(DAY FROM	(( Ano || '/' ||( vMes + 1 ) || '/01' ) :: DATE - 1 )) INTO UltimoDiaMes;

	if vMes = 0 then
	  vMes := 12;			
	end if;

	if Formato = 1 then
		if CHAR_LENGTH(vMes::text) < 2 then			
			UltimoDiaMes := UltimoDiaMes ||'/0' || vMes || '/' || Ano;	
		else
			UltimoDiaMes := UltimoDiaMes ||'/' || vMes || '/' || Ano;	
		end if;		
		
	elsif Formato = 2 then
		
		if CHAR_LENGTH(vMes::text) < 2 then			
			UltimoDiaMes := Ano ||'/0' || vMes || '/' || UltimoDiaMes;
		else
			UltimoDiaMes := Ano ||'/' || vMes || '/' || UltimoDiaMes;
		end if;
		
	elsif Formato = 3 then
		return UltimoDiaMes;
	end if;
	
	RETURN UltimoDiaMes;

END; $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100