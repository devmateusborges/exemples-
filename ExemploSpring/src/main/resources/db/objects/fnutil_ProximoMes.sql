Drop FUNCTION IF EXISTS fnutil_ProximoMes;
CREATE OR REPLACE FUNCTION fnutil_ProximoMes(pData varchar, pFormato integer)
  RETURNS varchar AS $BODY$ DECLARE
	vPrimeiroDia varchar;
	vUltimoDia varchar;
	vAno integer;
	vMes integer;	
BEGIN
	
	vPrimeiroDia := '01';
	SELECT EXTRACT(MONTH FROM	(pData) :: DATE) INTO vMes;
	SELECT EXTRACT(YEAR FROM	(pData) :: DATE) INTO vAno;
	
	/*1 - Próximo mês com ultimo dia*/
	if pFormato = 1 then
		vUltimoDia := fnutil_ultimo_dia(vMes, vAno, 2);		
		SELECT EXTRACT(MONTH FROM vUltimoDia :: date) into vMes;		
		vUltimoDia := fnutil_ultimo_dia(vMes + 1, vAno, 1);	
			RETURN vUltimoDia;
	/*2 - Próximo mês com Primeiro dia*/
	elsif pFormato = 2 then
		vPrimeiroDia := fnutil_primeiro_dia(pData::date,2);
		SELECT EXTRACT(MONTH FROM vPrimeiroDia :: date) into vMes;
		vPrimeiroDia := concat(vAno,'/',vMes+1,'/01');
		vPrimeiroDia := fnutil_primeiro_dia(vPrimeiroDia :: date, 1);
			RETURN vPrimeiroDia;
	end if;	
	
	RETURN '01/01/1900';

END; $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100