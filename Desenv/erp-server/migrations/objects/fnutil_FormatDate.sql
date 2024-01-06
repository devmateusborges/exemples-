Drop FUNCTION IF EXISTS fnutil_FormatDate;
CREATE OR REPLACE FUNCTION fnutil_FormatDate(pDate DATE, pFormato integer)
  RETURNS varchar AS $BODY$ DECLARE
	vDia varchar;
	vMes varchar;
	vAno varchar;
	vDataFormat VARCHAR;
BEGIN
	
	SELECT EXTRACT(DAY FROM	((pDate) :: DATE)) INTO vDia;
	SELECT EXTRACT(MONTH FROM	((pDate) :: DATE)) INTO vMes;
	SELECT EXTRACT(YEAR FROM	((pDate) :: DATE)) INTO vAno;
	
	if CHAR_LENGTH(vDia) < 2 then
		vDia := '0'||vDia;
	end if;
	
	if CHAR_LENGTH(vMes) < 2 then
		vMes := '0'||vMes;
	end if;
	
	if pFormato = 1 then
		vDataFormat := vDia ||'/' || vMes || '/' || vAno;
	elsif pformato = 2 then
		vDataFormat := vMes || '/' || vAno;
	elsif pFormato = 3 then
		vDataFormat := vAno ||'/' || vMes || '/' || vDia;
	end if;
	
	RETURN vDataFormat;

END; $BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100