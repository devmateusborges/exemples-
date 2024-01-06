from alembic import op


revision = "202210310755000"
down_revision = "202206151339048"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
drop  table sys_group_program_feature;
drop  table sys_user_program_feature;
drop  table sys_program_feature;

CREATE TABLE sys_action (
  id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
  name varchar(100) ,
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  active varchar(1) ,
  CONSTRAINT pk_sys_action PRIMARY KEY (id)
);
COMMENT ON COLUMN sys_action.id IS 'ID da Ação';
COMMENT ON COLUMN sys_action.name IS 'Nome';
COMMENT ON COLUMN sys_action.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_action.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_action.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_action.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN sys_action.active IS 'Ativo: S-Sim, N-Não';
COMMENT ON TABLE sys_action IS 'System-Ação';

INSERT INTO sys_action(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active) VALUES ('bc0b4deb-3564-453b-acd6-d91f38d20759', 'Edit', 'admin', '2022-10-28 14:34:23', NULL, NULL, 'S');
INSERT INTO sys_action(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active) VALUES ('17e78824-cfd5-4e79-81e5-412cfa86cc59', 'Delete', 'admin', '2022-10-28 14:34:33', NULL, NULL, 'S');
INSERT INTO sys_action(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active) VALUES ('9218ba8e-2383-4a8a-bffc-f3a4484c13cd', 'Save', 'admin', '2022-10-28 14:34:44', NULL, NULL, 'S');


alter table sys_action add code varchar(50);
COMMENT ON COLUMN sys_action.code IS 'Código da Ação';
alter table sys_action add CONSTRAINT idx_unq_sys_action_code UNIQUE (code) WITH (fillfactor=90);

update sys_action set code ='EDIT' where id='bc0b4deb-3564-453b-acd6-d91f38d20759';
update sys_action set code ='DELETE' where id='17e78824-cfd5-4e79-81e5-412cfa86cc59';
update sys_action set code ='SAVE' where id='9218ba8e-2383-4a8a-bffc-f3a4484c13cd';
	
alter table 	sys_action alter column code set not null;

INSERT INTO sys_action(id, name, code,log_user_ins, log_date_ins, log_user_upd, log_date_upd, active) VALUES ('96e61c78-98ad-4b5a-b747-4bde9f8aa6cd', 'View Extra','VIEW_EXTRA' ,'admin', '2022-10-28 14:34:44', NULL, NULL, 'S');



CREATE TABLE sys_program_action (
  id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
  sys_program_id varchar(36)  NOT NULL,
	sys_action_id varchar(36)  NOT NULL, 
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  CONSTRAINT pk_sys_program_action PRIMARY KEY (id),
	CONSTRAINT fk_sys_program_action_sys_program_id FOREIGN KEY (sys_program_id) REFERENCES sys_program (id) ON DELETE CASCADE ON UPDATE NO ACTION,
	CONSTRAINT fk_sys_program_action_sys_action_id FOREIGN KEY (sys_action_id) REFERENCES sys_action (id) ON DELETE CASCADE ON UPDATE NO ACTION,
	CONSTRAINT idx_unq_sys_program_action UNIQUE (sys_program_id,sys_action_id) WITH (fillfactor=90)
);
COMMENT ON COLUMN sys_program_action.id IS 'ID do Programa x Ação';
COMMENT ON COLUMN sys_program_action.sys_program_id IS 'ID do Programa';
COMMENT ON COLUMN sys_program_action.sys_action_id IS 'ID da Ação';
COMMENT ON COLUMN sys_program_action.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_program_action.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_program_action.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_program_action.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON TABLE sys_program_action IS 'System-Programa x Ação';




INSERT INTO sys_program_action(id, sys_program_id, sys_action_id, log_user_ins, log_date_ins, log_user_upd, log_date_upd) VALUES ('125708c7-2b5d-4cad-83ab-ce1a4b5fd1de','9409eb65-56a3-4ffa-a53c-68122d440d9b','bc0b4deb-3564-453b-acd6-d91f38d20759', 'admin', '2022-10-28 14:34:23', NULL, NULL);
INSERT INTO sys_program_action(id, sys_program_id, sys_action_id, log_user_ins, log_date_ins, log_user_upd, log_date_upd) VALUES ('1b25baf1-0433-4cfd-8c21-aef96551eee5','9409eb65-56a3-4ffa-a53c-68122d440d9b','17e78824-cfd5-4e79-81e5-412cfa86cc59', 'admin', '2022-10-28 14:34:33', NULL, NULL);
INSERT INTO sys_program_action(id, sys_program_id, sys_action_id, log_user_ins, log_date_ins, log_user_upd, log_date_upd) VALUES ('1c9d513d-d390-4ec8-8317-c77cd49b17d2','9409eb65-56a3-4ffa-a53c-68122d440d9b','9218ba8e-2383-4a8a-bffc-f3a4484c13cd', 'admin', '2022-10-28 14:34:44', NULL, NULL);
INSERT INTO sys_program_action(id, sys_program_id, sys_action_id, log_user_ins, log_date_ins, log_user_upd, log_date_upd) VALUES ('9f5dec1d-c595-4d2d-a304-82c61cd830ef','9409eb65-56a3-4ffa-a53c-68122d440d9b','96e61c78-98ad-4b5a-b747-4bde9f8aa6cd', 'admin', '2022-10-28 14:34:44', NULL, NULL);




CREATE TABLE sys_group_program_action (
  id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
  sys_group_id varchar(36)  NOT NULL,
	sys_program_action_id varchar(36)  NOT NULL, 
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  CONSTRAINT pk_sys_group_program_action PRIMARY KEY (id),
	CONSTRAINT fk_sys_group_program_action_sys_group_id FOREIGN KEY (sys_group_id) REFERENCES sys_group (id) ON DELETE CASCADE ON UPDATE NO ACTION,
	CONSTRAINT fk_sys_group_program_action_sys_program_action_id FOREIGN KEY (sys_program_action_id) REFERENCES sys_program_action (id) ON DELETE CASCADE ON UPDATE NO ACTION,
	CONSTRAINT idx_unq_sys_group_program_action UNIQUE (sys_group_id,sys_program_action_id) WITH (fillfactor=90)
);
COMMENT ON COLUMN sys_group_program_action.id IS 'ID do Grupo x Programa x Ação';
COMMENT ON COLUMN sys_group_program_action.sys_group_id IS 'ID do Grupo';
COMMENT ON COLUMN sys_group_program_action.sys_program_action_id IS 'ID da Programa x Ação';
COMMENT ON COLUMN sys_group_program_action.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_group_program_action.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_group_program_action.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_group_program_action.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON TABLE sys_group_program_action IS 'System-Grupo x Programa x Ação';



CREATE TABLE sys_user_program_action (
  id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
  sys_user_id varchar(36)  NOT NULL,
	sys_program_action_id varchar(36)  NOT NULL,
	exclude_action varchar(1) NOT NULL,
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  CONSTRAINT pk_sys_user_program_action_action PRIMARY KEY (id),
	CONSTRAINT fk_sys_user_program_action_action_sys_user_id FOREIGN KEY (sys_user_id) REFERENCES sys_user (id) ON DELETE CASCADE ON UPDATE NO ACTION,
	CONSTRAINT fk_sys_user_program_action_action_sys_program_action_id FOREIGN KEY (sys_program_action_id) REFERENCES sys_program_action (id) ON DELETE CASCADE ON UPDATE NO ACTION,
	CONSTRAINT idx_unq_sys_user_program_action UNIQUE (sys_user_id,sys_program_action_id) WITH (fillfactor=90)
);
COMMENT ON COLUMN sys_user_program_action.id IS 'ID do Grupo x Programa x Ação';
COMMENT ON COLUMN sys_user_program_action.sys_user_id IS 'ID do Grupo';
COMMENT ON COLUMN sys_user_program_action.sys_program_action_id IS 'ID da Programa x Ação';
COMMENT ON COLUMN sys_user_program_action.exclude_action IS 'Excluir Ação: S-Sim,N-Não';
COMMENT ON COLUMN sys_user_program_action.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_user_program_action.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_user_program_action.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_user_program_action.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON TABLE sys_user_program_action IS 'System-Grupo x Programa x Ação';



CREATE OR REPLACE FUNCTION fnsys_program_action_acesso(pvsysid varchar, pvuserlogin varchar, pvsysprogramid varchar)
  RETURNS TABLE(sys_action_id varchar, 
	              sys_action_name varchar, 
								sys_action_code varchar, 
								sys_program_id varchar, 
								sys_program_name varchar, 
								sys_program_controller varchar
								) AS $BODY$
DECLARE
vSql varchar;
r record;
begin
	
			vSql = 'select distinct 
									 s1.sys_action_id,
									 s1.sys_action_name,
									 s1.sys_action_code,
									 s1.sys_program_id,
									 s1.sys_program_name,
									 s1.sys_program_controller
						from (

						select a.id sys_action_id,
									 a.name as sys_action_name,
									 a.code as sys_action_code,
									 p.id as sys_program_id,
									 p.name as sys_program_name,
									 p.controller as sys_program_controller
							from sys_group_program_action gpa
							join sys_program_action pa on(gpa.sys_program_action_id = pa.id)
							join sys_action a on(pa.sys_action_id = a.id)
							join sys_program p on(pa.sys_program_id = p.id)
							join sys_module m on(p.sys_module_id = m.id)
						where	a.active = ''S''
							and p.active = ''S''
							and m.sys_id = '''||pvSysId||'''
							and p.id =  '''||pvsysprogramid||'''
							and (exists (select 1 
														from sys_group_program s1,
																 sys_user_group s2,
																 sys_user s3,
																 sys_group s4
														where s1.sys_group_id = s2.sys_group_id
															and s2.sys_user_id = s3.id
															and s2.sys_group_id = s4.id
															and s1.sys_program_id = p.id
															and s3.active= ''S''
															and s4.active = ''S''
															and s3.login = '''||pvUserLogin||''') 
								or exists 	(select 1 
															 from sys_user_program x1,
																		sys_user x2
														 where x1.sys_program_id = p.id
															 and x1.sys_user_id = x2.id
															 and x2.active = ''S''
															 and x2.login = '''||pvUserLogin||'''))
						 and 	not exists (
									select 1
									 from sys_user_program_action supa
									where supa.exclude_action = ''S''
									 and supa.sys_program_action_id = pa.id)
															 
						union all							 
															 
						select a.id sys_action_id,
									 a.name as sys_action_name,
									 a.code as sys_action_code,
									 p.id as sys_program_id,
									 p.name as sys_program_name,
									 p.controller as sys_program_controller
							from sys_user_program_action upa
							join sys_program_action pa on(upa.sys_program_action_id = pa.id)
							join sys_action a on(pa.sys_action_id = a.id)
							join sys_program p on(pa.sys_program_id = p.id)
							join sys_module m on(p.sys_module_id = m.id)
						where	a.active = ''S''
							and p.active = ''S''
							and m.sys_id = '''||pvSysId||'''
							and p.id = '''||pvsysprogramid||'''
							and upa.exclude_action = ''N''	
							and (exists (select 1 
														from sys_group_program s1,
																 sys_user_group s2,
																 sys_user s3,
																 sys_group s4
														where s1.sys_group_id = s2.sys_group_id
															and s2.sys_user_id = s3.id
															and s2.sys_group_id = s4.id
															and s1.sys_program_id = p.id
															and s3.active= ''S''
															and s4.active = ''S''
															and s3.login = '''||pvUserLogin||''') 
								or exists 	(select 1 
															 from sys_user_program x1,
																		sys_user x2
														 where x1.sys_program_id = p.id
															 and x1.sys_user_id = x2.id
															 and x2.active = ''S''
															 and x2.login = '''||pvUserLogin||'''))
							) s1 ';
   
	FOR r IN EXECUTE vSql loop
	    sys_action_id := r.sys_action_id;
			sys_action_name := r.sys_action_name;
			sys_action_code := r.sys_action_code;
			sys_program_id := r.sys_program_id;
			sys_program_name := r.sys_program_name;
			sys_program_controller := r.sys_program_controller;
	RETURN NEXT;
	
	END loop;



end;
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100
  ROWS 1000;




--================================================================
--Liberar acesso para todos usuários
--================================================================
--admin interno
delete from sys_group_program a where sys_group_id='4218d8f1-8595-4052-aace-ba36f772623e';
insert into sys_group_program(id,sys_group_id,sys_program_id)
select uuid_generate_v4(),'4218d8f1-8595-4052-aace-ba36f772623e', b.id
from sys_program b;
--admin unit
delete from sys_group_program a where sys_group_id='0256e515-51a4-49a2-a8b8-adc36470cd51';
insert into sys_group_program(id,sys_group_id,sys_program_id)
select uuid_generate_v4(),'0256e515-51a4-49a2-a8b8-adc36470cd51', b.id
from sys_program b where b.admin='N';
commit;
--actions
delete from sys_group_program_action a where sys_group_id in('4218d8f1-8595-4052-aace-ba36f772623e','0256e515-51a4-49a2-a8b8-adc36470cd51');
--actions - interno
insert into sys_group_program_action(id,sys_group_id,sys_program_action_id)
select uuid_generate_v4(),'4218d8f1-8595-4052-aace-ba36f772623e', c.id
from sys_program b 
join sys_program_action c on(b.id = c.sys_program_id);
commit;
--actions - unit
insert into sys_group_program_action(id,sys_group_id,sys_program_action_id)
select uuid_generate_v4(),'0256e515-51a4-49a2-a8b8-adc36470cd51', c.id
from sys_program b 
join sys_program_action c on(b.id = c.sys_program_id) where b.admin='N';
commit;
"""
    )


def downgrade():
    pass
