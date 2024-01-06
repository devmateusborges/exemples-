--====================================================================================
--Gera
--====================================================================================

DO $$
DECLARE 
vI INTEGER;
vIdUnit VARCHAR(36);
seq INTEGER := 1;

BEGIN
	FOR vI IN 1..1000 loop
		SELECT uuid_generate_v4() INTO vIdUnit;
		
    INSERT INTO sys_unit(id, name, sigla_unit, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active) VALUES (vIdUnit,  'Name'||trim(to_char(seq,'0000')), 'T'||trim(to_char(seq,'0000')), 'admin', NOW(), NULL, NULL, 'S');

		insert into sys_user_unit (sys_user_id, unit_id, owner) values ('062dddad-4ca3-4956-aa75-6f6cf368b05b', vIdUnit, 'N');
		
		seq := seq+1;
		
	END LOOP;
END$$;

--====================================================================================
--Limpeza geral do teste
--====================================================================================
delete from sys_user_unit suu where unit_id != 'f3996813-838e-49af-9649-8dc44e24bc75';
delete from sys_unit a where a.id != 'f3996813-838e-49af-9649-8dc44e24bc75';

select * from sys_unit

SELECT uuid_generate_v4()