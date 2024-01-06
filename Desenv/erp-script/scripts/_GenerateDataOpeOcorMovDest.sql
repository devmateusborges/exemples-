do $$ declare
pParIdGenerate varchar;
pParOpeOcorMovId varchar;
pParCentro2Id varchar;
begin
	
 for i in 1..20 loop
			
			select uuid_generate_v4() into pParIdGenerate;
			
			select 
				id into pParOpeOcorMovId 
			from ope_ocor_mov where 
				unit_id in('f3996813-838e-49af-9649-8dc44e24bc75') 
				order by random() limit 1;
			
			select 
				id into pParCentro2Id 
			from ope_centro2 
				where unit_id in('f3996813-838e-49af-9649-8dc44e24bc75') 
				order by random() limit 1;
				
			
		INSERT INTO ope_ocor_mov_dest("unit_id", "id", "ope_ocor_mov_id", "ope_centro2_id", "ope_compart_id", "observacao", "log_user_ins", "log_date_ins", "log_user_upd", "log_date_upd") VALUES ('f3996813-838e-49af-9649-8dc44e24bc75', pParIdGenerate, pParOpeOcorMovId, pParCentro2Id, NULL, 'obs', 'admin', now(), NULL, NULL);

	end loop;
end $$;

-- select * from ope_ocor_mov_dest