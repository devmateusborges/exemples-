create or replace function fnutil_formatcpfcnpj(pgerPessoaId varchar,pFormatado boolean)
  RETURNS varchar as $BODY$
declare
 Vsql varchar;
begin
		IF pFormatado = TRUE THEN		
				select
				 (CASE 
					WHEN p1.doc_cnpj is null THEN regexp_replace(
					LPAD(p1.doc_cpf, 11),
					'([0-9]{3})([0-9]{3})([0-9]{3})','\1.\2.\3-')
					WHEN p1.doc_cpf is null THEN regexp_replace(
					LPAD(p1.doc_cnpj, 14),'([0-9]{2})([0-9]{3})([0-9]{3})([0-9]{4})','\1.\2.\3/\4-')
					WHEN p1.doc_cnpj is not null and p1.doc_cpf is not null THEN regexp_replace(
					LPAD(p1.doc_cnpj, 14),'([0-9]{2})([0-9]{3})([0-9]{3})([0-9]{4})','\1.\2.\3/\4-')||
					' || '||regexp_replace(LPAD(p1.doc_cpf, 11),'([0-9]{3})([0-9]{3})([0-9]{3})','\1.\2.\3-')
					ELSE '' END) into Vsql 
			from ger_pessoa p1 where p1.id = pgerPessoaId;
		
		ELSE
				select 
					 	(CASE 
							WHEN p1.doc_cnpj is null THEN p1.doc_cpf
							WHEN p1.doc_cpf is null THEN p1.doc_cnpj
							WHEN p1.doc_cnpj is not null and p1.doc_cpf is not null THEN p1.doc_cnpj||' || '||p1.doc_cpf
							ELSE ''
							END
						) into vSql
				 from ger_pessoa p1 where p1.id = pgerPessoaId;
		end if;	
	  
		return Vsql;
end;
$BODY$
LANGUAGE plpgsql VOLATILE;