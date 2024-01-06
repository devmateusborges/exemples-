from alembic import op
import sqlalchemy as sa

revision = '202206151339041'
down_revision = '202206151339040'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
update sys_program set icon = 'mdi mdi-table' where icon='fas fa-table';
update sys_program set icon = 'mdi mdi-tools' where icon='fas fa-tools';
update sys_program set icon = 'mdi mdi-file-arrow-up-down' where icon='fas fa-tasks';
update sys_program set controller = '/private'||controller where controller  not like '/private%';

alter table sys_module add order_visual int2;
COMMENT ON COLUMN sys_module.order_visual IS 'Ordem de visualizacao';

update sys_module set order_visual=10 where id='0a4e3058-b04f-4ec2-a791-cf98ecb27da7';
update sys_module set order_visual=20 where id='cf4efc32-f1fc-4631-9189-5a71be403477';
update sys_module set order_visual=20 where id='145cdd4d-37a1-4156-bc3c-5b1f1067b5c5';
update sys_module set order_visual=30 where id='a022d3d5-2ccf-4060-986f-bdd075b4e0ee';
update sys_module set order_visual=40 where id='851f3230-70e7-44ea-a4aa-4c3c23f1052c';
update sys_module set order_visual=50 where id='82b4125d-0018-4d2e-8cc4-7f7ef7e52a08';
update sys_module set order_visual=60 where id='bf0a3b02-f67f-47a2-9f8f-3974c0138113';
update sys_module set order_visual=70 where id='5f99ec23-e7f7-4199-801c-50cb92a4edad';
update sys_module set order_visual=80 where id='f33008f2-6d83-444f-ac76-5f4eb1d47e2c';
update sys_module set order_visual=90 where id='60e4ff9c-8aeb-4bf2-b4b1-84fc77c25f4a';
update sys_module set order_visual=100 where id='da48f325-87ee-4ba4-9142-d54bf625793c';
update sys_module set order_visual=110 where id='cdf80950-068f-4343-a86f-d993eee9865f';
update sys_module set order_visual=120 where id='c2f71978-6ac0-4d80-b874-988a6b8a136b';
update sys_module set order_visual=130 where id='77bf2e96-5f9c-41be-9b2f-455e6bc756ae';
update sys_module set order_visual=140 where id='985d6d6e-6c10-42a7-952e-03f2c67be29d';
update sys_module set order_visual=150 where id='da3e1191-75d2-46ac-9464-379bc5176201';
update sys_module set order_visual=900 where id='ca29f487-243f-4c94-8a39-7c3faca63e90';
update sys_module set order_visual=900 where id='7be0ed16-b34a-4d67-9588-07efe47d5340';
update sys_module set order_visual=901 where id='23497bdc-ea73-459d-804e-88682e474c51';

Drop FUNCTION IF EXISTS fnsys_program_acesso;
CREATE OR REPLACE FUNCTION fnsys_program_acesso(
pvSysId varchar,
pvUserLogin varchar, 
pvSysProgramAdmin varchar, 
pvSysProgramMenu varchar,
pvSysProgramFavorite varchar
)
RETURNS TABLE(
sys_program_id varchar,
sys_program_name varchar,
sys_program_controller varchar,
sys_program_type_program varchar,
sys_program_icon varchar,
sys_module_id varchar,
sys_module_name varchar,
sys_module_icon varchar,
sys_module_sigla_module varchar,
sys_module_sigla_module_desc varchar,
sys_module_color varchar,
sys_module_order_visual numeric
) AS $BODY$
DECLARE
vSql varchar;
r record;
begin
	
			vSql = 'select distinct
								t1.id as sys_program_id,
								t1.name as sys_program_name,
								t1.controller as sys_program_controller,
								t1.type_program as sys_program_type_program,
								t1.icon as sys_program_icon,
								t1.sys_module_id,
								t2.name as sys_module_name,
								t2.icon as sys_module_icon,
								t2.sigla_module as sys_module_sigla_module,
								t2.sigla_module||''-''||t2.name as sys_module_sigla_module_desc,
								t2.color as sys_module_color,
								t2.order_visual as sys_module_order_visual
								from sys_program t1, 
										 sys_module  T2
								where t1.sys_module_id = t2.id
									and t1.menu = '''||pvSysProgramMenu||'''
									and t1.admin = '''||pvSysProgramAdmin||'''
									and t2.active = ''S''
									and t2.sys_id = '''||pvSysId||'''
									and (exists (select 1 
																from sys_group_program s1,
																		 sys_user_group s2,
																		 sys_user s3,
																		 sys_group s4
																where s1.sys_group_id = s2.sys_group_id
																	and s2.sys_user_id = s3.id
																	and s2.sys_group_id = s4.id
																	and s1.sys_program_id = t1.id
																	and s3.active= ''S''
																	and s4.active = ''S''
																	and s3.login = '''||pvUserLogin||'''	) 
											or exists 	(select 1 
																		 from sys_user_program x1,
																					sys_user x2
																	 where x1.sys_program_id = t1.id
																		 and x1.sys_user_id = x2.id
																		 and x2.active = ''S''
																		 and x2.login = '''||pvUserLogin||'''))';
																		 
								if pvSysProgramFavorite = 'S' then
                   vSql = vSql || 'and exists (select 1 
																		             from sys_program_favorite x1,
																					            sys_user x2
																								 where x1.sys_program_id = t1.id
																									 and x1.sys_user_id = x2.id
																									 and x2.active = ''S''
																									 and x2.login = '''||pvUserLogin||''')';
               end if;																		 
																		 
								vSql = vSql || 'order by t2.order_visual desc, t1.type_program, t1.name';
   
	FOR r IN EXECUTE vSql loop
		sys_program_id               := r.sys_program_id;
		sys_program_name             := r.sys_program_name;
		sys_program_controller       := r.sys_program_controller;
		sys_program_type_program     := r.sys_program_type_program;
		sys_program_icon             := r.sys_program_icon;
		sys_module_id                := r.sys_module_id;
		sys_module_name              := r.sys_module_name;
		sys_module_icon              := r.sys_module_icon;
		sys_module_sigla_module      := r.sys_module_sigla_module;
		sys_module_sigla_module_desc := r.sys_module_sigla_module_desc;
		sys_module_color             := r.sys_module_color;
		sys_module_order_visual      := r.sys_module_order_visual;
	RETURN NEXT;
	
	END loop;



end;
$BODY$
LANGUAGE plpgsql VOLATILE;
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
