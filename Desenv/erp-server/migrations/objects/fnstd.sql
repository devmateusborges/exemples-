CREATE OR REPLACE FUNCTION fnstd(ptablename text, pfieldname text, pvaluetype text)
  RETURNS varchar AS $BODY$
declare
vSql varchar;
BEGIN
	
	
	select 
		t1.description_type into vSql
  from sys_type_description t1
	where t1.table_name = pTableName
	and t1.field_name = pFieldName
	and t1.value_type = pValueType;
	
	return vSql;
	
END;
$BODY$
  LANGUAGE plpgsql VOLATILE;
	