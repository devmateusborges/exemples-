from alembic import op
import sqlalchemy as sa

revision = '202206151339038'
down_revision = '202206151339037'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
update sys_program set controller  = replace(controller,'/system','/sys');

UPDATE sys_module SET ICON = REPLACE(ICON,'fas','fa-solid ');

UPDATE sys_module SET ICON = 'fa-solid fa-vial'
where id='23497bdc-ea73-459d-804e-88682e474c51';

delete FROM sys_module where id in('479e64bc-f2ca-43ec-9ead-f0491b78e74e');

update sys_user set active='S';
update sys_group set active='S';

delete from sys_user_group where sys_user_id='062dddad-4ca3-4956-aa75-6f6cf368b05b';
INSERT INTO sys_user_group(id, sys_user_id, sys_group_id, log_user_ins, log_date_ins, log_user_upd, log_date_upd) VALUES ('60e4ff9c-8aeb-4bf2-b4b1-84fc77c25f4a', '062dddad-4ca3-4956-aa75-6f6cf368b05b', '0256e515-51a4-49a2-a8b8-adc36470cd51', 'admin', '2022-09-18 22:44:28', NULL, NULL);


UPDATE sys_module SET ICON = 'mdi mdi-cow' where id = '60e4ff9c-8aeb-4bf2-b4b1-84fc77c25f4a';--	  Pecuária
UPDATE sys_module SET ICON = 'mdi mdi-test-tube' where id = '23497bdc-ea73-459d-804e-88682e474c51';--		Testes
UPDATE sys_module SET ICON = 'mdi mdi-dolly' where id = 'a022d3d5-2ccf-4060-986f-bdd075b4e0ee';--		Movimento
UPDATE sys_module SET ICON = 'mdi mdi-chart-box-outline' where id = '82b4125d-0018-4d2e-8cc4-7f7ef7e52a08';--		Indicador
UPDATE sys_module SET ICON = 'mdi mdi-cellphone-wireless' where id = 'bf0a3b02-f67f-47a2-9f8f-3974c0138113';--		Mobilidade
UPDATE sys_module SET ICON = 'mdi mdi-cash' where id = 'cf4efc32-f1fc-4631-9189-5a71be403477';--		Financeiro
UPDATE sys_module SET ICON = 'mdi mdi-clock-time-three-outline' where id = 'cdf80950-068f-4343-a86f-d993eee9865f';--		Ponto
UPDATE sys_module SET ICON = 'mdi mdi-map-search-outline' where id = 'c2f71978-6ac0-4d80-b874-988a6b8a136b';--		Bordo
UPDATE sys_module SET ICON = 'mdi mdi-table-large' where id = '0a4e3058-b04f-4ec2-a791-cf98ecb27da7';--		Geral
UPDATE sys_module SET ICON = 'mdi mdi-tractor-variant' where id = '851f3230-70e7-44ea-a4aa-4c3c23f1052c';--		Operação
UPDATE sys_module SET ICON = 'mdi mdi-flashlight' where id = 'f33008f2-6d83-444f-ac76-5f4eb1d47e2c';--		Fiscal
UPDATE sys_module SET ICON = 'mdi mdi-cash-register' where id = '5f99ec23-e7f7-4199-801c-50cb92a4edad';--		Contabilidade
UPDATE sys_module SET ICON = 'mdi mdi-weight-lifter' where id = 'da48f325-87ee-4ba4-9142-d54bf625793c';--		Recurso Humano
UPDATE sys_module SET ICON = 'mdi mdi-database-lock' where id = 'ca29f487-243f-4c94-8a39-7c3faca63e90';--		Sistema
UPDATE sys_module SET ICON = 'mdi mdi-file-document' where id = '77bf2e96-5f9c-41be-9b2f-455e6bc756ae';--		Documentos
UPDATE sys_module SET ICON = 'mdi mdi-phone-incoming-outgoing' where id = '985d6d6e-6c10-42a7-952e-03f2c67be29d';--		Atendimento
UPDATE sys_module SET ICON = 'mdi mdi-database-lock' where id = '7be0ed16-b34a-4d67-9588-07efe47d5340';--		Sistema(M)
UPDATE sys_module SET ICON = 'mdi mdi-cash' where id = '145cdd4d-37a1-4156-bc3c-5b1f1067b5c5';--		Financeiro(M)
UPDATE sys_module SET ICON = 'mdi mdi-sitemap-outline' where id = 'da3e1191-75d2-46ac-9464-379bc5176201';--		Blog



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

""")


def downgrade():
    pass
