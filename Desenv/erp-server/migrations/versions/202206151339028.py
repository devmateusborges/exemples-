from alembic import op
import sqlalchemy as sa

revision = '202206151339028'
down_revision = '202206151339027'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""

alter table fis_tributacao drop constraint chk_mov_id_mov_itemserv_id; 
alter table mov_entrega_doc drop constraint chk_mov_id_mov_entrega_id;	

alter table ger_itemserv_subgrupo rename column ger_grupo_id to ger_itemserv_grupo_id;

update sys_module set active = 'S';
INSERT INTO sys_module (id,"name",log_user_ins,log_date_ins,log_user_upd,log_date_upd,sigla_module,sys_id,icon,color,active) VALUES
 ('da3e1191-75d2-46ac-9464-379bc5176201','Blog','admin','2020-08-11 20:19:17.000',NULL,NULL,'CMS','e8329d00-443f-4c03-8e73-c161f0d4f37d','fas fa-blog','green','S');
update sys_program set active = 'S';
INSERT INTO sys_program (id,"name",controller,log_user_ins,log_date_ins,log_user_upd,log_date_upd,menu,type_program,sys_module_id,icon,"admin",active) VALUES
 ('50ed2ac6-fe43-41eb-bdd0-cb4e6f92add3','Tag de Post','/crm/cmstag',NULL,'2021-06-15 12:08:06.000',NULL,NULL,'S','T','da3e1191-75d2-46ac-9464-379bc5176201','fas fa-table','S','S');
INSERT INTO sys_program (id,"name",controller,log_user_ins,log_date_ins,log_user_upd,log_date_upd,menu,type_program,sys_module_id,icon,"admin",active) VALUES
 ('9e3738c3-2008-45a9-96de-8570740f5e69','Post','/crm/cmspost',NULL,'2021-06-15 12:08:06.000',NULL,NULL,'S','T','da3e1191-75d2-46ac-9464-379bc5176201','fas fa-table','S','S');
INSERT INTO sys_program (id,"name",controller,log_user_ins,log_date_ins,log_user_upd,log_date_upd,menu,type_program,sys_module_id,icon,"admin",active) VALUES
 ('843a6d45-7e74-4bfa-8728-860db645675b','Grupo de Post','/crm/cmsgrupo',NULL,'2021-06-15 12:08:06.000',NULL,NULL,'S','T','da3e1191-75d2-46ac-9464-379bc5176201','fas fa-table','S','S');


        
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
