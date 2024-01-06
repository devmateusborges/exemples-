from alembic import op


revision = "202211301615002"
down_revision = "202211220919001"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('cbf2cce9-ddce-4a83-9bf3-4c0680a7e0b3',(select id from sys_program where controller like '%/opecentroversao'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('2f83820b-7aba-415d-846d-a5f75c9b0669',(select id from sys_program where controller like '%/opecentroversao'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('649de997-da57-4265-9f42-1e12c621bd05',(select id from sys_program where controller like '%/opecentroversao'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('b5fbda4d-4376-4aaf-8581-3dd3faa44024',(select id from sys_program where controller like '%/opecentroversao'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentroversao') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentroversao') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentroversao') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentroversao') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

alter table sys_process_log add column error varchar(1) default 'N';
comment on column sys_process_log.error is 'Erro';

alter table sys_process_log add column message_process text;
comment on column sys_process_log.message_process is 'Mensagem';

alter table sys_process_log add column code_process text;
comment on column sys_process_log.code_process is 'Código do processo';

alter table ger_per add column sys_process_log_id varchar(36);
alter table ger_per add constraint fk_sys_process_log_id foreign key (sys_process_log_id) references sys_process_log;
comment on column ger_per.sys_process_log_id is 'ID do System-Log de Processo';

insert into sys_type_description (id, table_name, field_name, value_type, description_type) values ('b4ad245e-2efd-4907-bc3a-e83636df8dcf','sys_process_log','type_process','GER_PER_GENERATE', 'Geração de periodo');

insert into sys_action (id, name, active, code) values ('8b38240c-2e80-46ee-85a5-be192d3d6957', 'Revoke', 'S', 'REVOKE');
insert into sys_action (id, name, active, code) values ('d83f5825-0b58-4980-98e5-085e47f11b9e', 'Process', 'S', 'PROCESS');

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('e4a3f2be-6de5-4e0f-b4cd-745080c1af24',(select id from sys_program where controller like '%/gerpergerar'),(select id from sys_action sa  where code = 'REVOKE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('7491792b-bc0a-4cc7-81cc-1d18f14d09fc',(select id from sys_program where controller like '%/gerpergerar'),(select id from sys_action sa  where code = 'PROCESS'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/gerpergerar') and sys_action_id = (select id from sys_action sa  where code = 'REVOKE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/gerpergerar') and sys_action_id = (select id from sys_action sa  where code = 'PROCESS')));

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
