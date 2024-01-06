from alembic import op


revision = "202210310755006"
down_revision = "202210310755005"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
delete from sys_program where id = 'e2ccfe0e-ee43-4096-b4da-fc34d235fc65';
delete from sys_program where id = '94231246-2874-4a02-b660-4538891ccfc7';
delete from sys_program where id = '5f8dd187-a9ee-49d9-80b0-5556c2f7c4e7';
delete from sys_program where id = 'd89328ef-4e99-454d-88af-411bc6a771c8';
update sys_program set controller='/private/sys/sysnotificationlogview', name='Log de Notificação' where id='b1e889f9-d08c-43cc-946c-0460966eab8e';
delete from sys_program where id = '48bf245c-a091-4e2f-b9cf-e426b91794ff';
delete from sys_program where id = 'ef39d0dd-057f-4b09-a5d6-2ffcdc463fda';
update sys_program set controller='/private/sys/syspermissionaccess', name='Permissões de Acesso' where id='13253c34-5407-44bb-998a-5d56b7ed89d1';
delete from sys_program where id = 'c38b2a96-c488-4bcf-998d-8739b3f4757b';
update sys_program set controller='/private/sys/sysqueuelogview', name='Log de Processamento' where id='14bd9d36-67ea-4f47-b347-c81b05fd8f18';
update sys_program set controller='/private/sys/syspreferenceform', name='Configuração de Formulário' where id='443bd386-52f0-4d6b-b791-754fa66160a7';

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('335c29b4-69ad-4915-9ec7-490c42d7719a','sys_dic','admin','type_dic','10','Tabela');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('503c64ba-56a6-4c7e-8100-bed124b0b810','sys_dic','admin','type_dic','11','Coluna');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('88f0e301-369d-4735-a34c-f0ba8fe9fa37','sys_dic','admin','type_dic','12','Grid');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('261c4886-060b-4ec5-97cd-559fc46d9e84','sys_dic','admin','type_dic','13','Ação');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('5a43a2f9-4b0f-4a87-af3c-dc529e8e70c6','sys_dic','admin','type_dic','14','Função');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('36f82734-6639-44d5-a84a-333c40753844','sys_dic','admin','type_dic','15','View');

UPDATE public.sys_program
	SET controller='/private/sys/sysplan'
	WHERE id='12cc44eb-1861-4880-8cda-9b4f6847cb79';

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
