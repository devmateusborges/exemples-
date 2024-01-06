--====================================================================================
--Gera carga de mensagens
--====================================================================================

DO $$
DECLARE 
vI INTEGER;
vIdUser VARCHAR(100);
msg INTEGER;

BEGIN
	FOR vI IN 1..100 loop
	
		insert into system_user (name, login, password, email, active) values (('teste'||vI||'a'), ('testeChat'||vI||'a'), '123', ('testeChat'||vI||'a'), 'S') RETURNING id into vIdUser;
		
		insert into system_user_unit (system_user_id, system_unit_id, owner) values (vIdUser, 'f3996813-838e-49af-9649-8dc44e24bc75', 'N');
	
		insert into system_user_crm_chat_grupo (unit_id, system_user_id, crm_chat_grupo_id, admin) 
		values ('f3996813-838e-49af-9649-8dc44e24bc75',
			    vIdUser,
			    '72cbce1d-d939-4fdd-9de2-6498c13167a1',
			    'N');
			   
		FOR msg IN 1..3 loop
			insert into crm_chat_msg (corpo, unit_id, system_user_id_orig, crm_chat_grupo_id, origem_sistema,log_user_ins) values('teste','f3996813-838e-49af-9649-8dc44e24bc75',vIdUser,'72cbce1d-d939-4fdd-9de2-6498c13167a1','N',CONCAT('teste',vI,'a'));
		   
		END LOOP;
	
		insert into system_user (name, login, password, email, active) values (('teste'||vI||'b'), ('testeChat'||vI||'b'), '123', ('testeChat'||vI||'b'), 'S') RETURNING id into vIdUser;
		
		insert into system_user_unit (system_user_id, system_unit_id, owner) values (vIdUser, 'f3996813-838e-49af-9649-8dc44e24bc75', 'N');
	
		insert into system_user_crm_chat_grupo (unit_id, system_user_id, crm_chat_grupo_id, admin) 
		values ('f3996813-838e-49af-9649-8dc44e24bc75',
			    vIdUser,
			    '0a6b30ea-6dc5-4339-822d-4756cf8171f7',
			    'N');
			   
		FOR msg IN 1..3 loop
			insert into crm_chat_msg (corpo, unit_id, system_user_id_orig, crm_chat_grupo_id, origem_sistema,log_user_ins) values('teste','f3996813-838e-49af-9649-8dc44e24bc75',vIdUser,'0a6b30ea-6dc5-4339-822d-4756cf8171f7','N',CONCAT('teste',vI,'b'));
		   
		END LOOP;
			   
		insert into system_user (name, login, password, email, active) values (('teste'||vI||'d'), ('testeChat'||vI||'d'), '123', ('testeChat'||vI||'d'), 'S') RETURNING id into vIdUser;
		
		insert into system_user_unit (system_user_id,system_unit_id,owner) values (vIdUser, 'f3996813-838e-49af-9649-8dc44e24bc75', 'N');
	
		insert into system_user_crm_chat_grupo (unit_id, system_user_id, crm_chat_grupo_id, admin) 
		values ('f3996813-838e-49af-9649-8dc44e24bc75',
			    vIdUser,
			    '8b6355a9-0b2a-4727-8d0e-0c27fee8d21b',
			    'N');
	
		FOR msg IN 1..3 loop
			insert into crm_chat_msg (corpo, unit_id, system_user_id_orig, crm_chat_grupo_id, origem_sistema,log_user_ins) values('teste','f3996813-838e-49af-9649-8dc44e24bc75',vIdUser,'8b6355a9-0b2a-4727-8d0e-0c27fee8d21b','N',CONCAT('teste',vI,'d'));
		   
		END LOOP;
	
	
	END LOOP;
END$$;

--====================================================================================
--Limpeza geral do teste
--====================================================================================


do $$
DECLARE 
i INTEGER;

BEGIN
	FOR i IN 1..100 loop
		delete from system_user_unit suu where system_user_id = (select id from system_user where name = concat('teste',i,'a'));

	END LOOP;
END$$;
