do $$ declare
pParIdGenerate varchar;
vDataMov date;
pParNumber integer;
pParGerEmpresaId varchar;
pParEnderecoExecId varchar;
pParOcorTipoId varchar;
begin

for i in 1..20 loop

	select uuid_generate_v4() into pParIdGenerate;
	
-- 	select * from ope_ocor_mov;
	
	select CAST (now() - random() * INTERVAL '5 days' as date)
			into  vDataMov;
	
	select ROW_NUMBER() over() +i into pParNumber;
	
	select id into pParGerEmpresaId from ger_empresa where unit_id in('f3996813-838e-49af-9649-8dc44e24bc75') order by random() limit 1;
	
	select id into pParEnderecoExecId from ger_pessoa_endereco where unit_id in('f3996813-838e-49af-9649-8dc44e24bc75') order by random() limit 1;
	

-- 	select id into pParOcorTipoId from ope_ocor_tipo where unit_id in('f3996813-838e-49af-9649-8dc44e24bc75') order by random() limit 1;
	
	pParOcorTipoId =	'759d87de-e9bb-4052-b8b0-7bbeabcbd5c8';
	
	INSERT INTO "public"."ope_ocor_mov"("unit_id", "id", "log_user_ins", "log_date_ins", "log_user_upd", "log_date_upd", "observacao", "data_mov", "numero", "ger_empresa_id", "ger_pessoa_endereco_id_exec", "ope_ocor_tipo_id") VALUES ('f3996813-838e-49af-9649-8dc44e24bc75', pParIdGenerate, 'admin', now(), NULL, NULL, 'obs',vDataMov, pParNumber, pParGerEmpresaId, pParEnderecoExecId, pParOcorTipoId);
	
	
end loop;

end $$;

-- select * from ope_ocor_mov