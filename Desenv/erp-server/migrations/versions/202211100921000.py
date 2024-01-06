from alembic import op


revision = "202211100921000"
down_revision = "202210310755006"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """



UPDATE public.sys_program
	SET controller='/private/sys/sysdocumentcategory'
	WHERE id='d59bfc00-dcc5-429e-8cc0-0d920f21656b';

--======= Add Code in SYS
ALTER TABLE public.sys_licence ADD code_licence varchar(50) NULL;
COMMENT ON COLUMN public.sys_licence.code_licence IS 'Sigla Licenças';

ALTER TABLE public.sys_program ADD code_program varchar(50) NULL;
COMMENT ON COLUMN public.sys_program.code_program IS 'Sigla Programas';

ALTER TABLE public.sys_group ADD code_group varchar(50) NULL;
COMMENT ON COLUMN public.sys_group.code_group IS 'Sigla Grupo de Acesso';

ALTER TABLE sys_plan ADD code_plan varchar(100) NULL;
COMMENT ON COLUMN sys_plan.code_plan IS 'Sigla - Plano de Utilização do Sistema';

ALTER TABLE public.sys_restriction ADD code_restriction varchar(50) NULL;
COMMENT ON COLUMN public.sys_restriction.code_restriction IS 'Sigla - Restrição de Sistema';

ALTER TABLE public.sys_document_category ADD code_document_category varchar(50) NULL;
COMMENT ON COLUMN public.sys_document_category.code_document_category IS 'Sigla Categoria Documento';

ALTER TABLE public.sys_document ADD code_document varchar(50) NULL;
COMMENT ON COLUMN public.sys_document.code_document IS 'Sigla Documento';


ALTER TABLE public.sys_unit RENAME COLUMN sigla_unit TO code_unit;

ALTER TABLE public.sys_module RENAME COLUMN sigla_module TO code_module;
ALTER TABLE public.sys_module ALTER COLUMN code_module TYPE varchar(50) ;

ALTER TABLE public.sys RENAME COLUMN sigla_sys TO code_sys;
ALTER TABLE public.sys ALTER COLUMN code_sys TYPE varchar(50);


create sequence tmt_seq; 
update sys_licence  set code_licence  = to_char(nextval('tmt_seq') + 1000, '0000'); 
drop sequence tmt_seq;

ALTER TABLE public.sys_licence ALTER COLUMN code_licence SET NOT NULL;


create sequence tmt_seq; 
update sys_group set code_group  = to_char(nextval('tmt_seq') + 1000, '0000'); 
drop sequence tmt_seq;

ALTER TABLE public.sys_group ALTER COLUMN code_group SET NOT NULL;


create sequence tmt_seq; 
update sys_plan  set code_plan  = to_char(nextval('tmt_seq') + 1000, '0000'); 
drop sequence tmt_seq;

ALTER TABLE public.sys_plan ALTER COLUMN code_plan SET NOT NULL;


create sequence tmt_seq; 
update sys_restriction  set code_restriction = to_char(nextval('tmt_seq') + 1000, '0000'); 
drop sequence tmt_seq;

ALTER TABLE public.sys_restriction ALTER COLUMN code_restriction SET NOT NULL;

create sequence tmt_seq; 
update sys_document_category  set code_document_category  = to_char(nextval('tmt_seq') + 1000, '0000'); 
drop sequence tmt_seq;

ALTER TABLE public.sys_document_category ALTER COLUMN code_document_category SET NOT NULL;

create sequence tmt_seq; 
update sys_program  set code_program  = to_char(nextval('tmt_seq') + 1000, '0000'); 
drop sequence tmt_seq;

ALTER TABLE public.sys_program ALTER COLUMN code_program SET NOT NULL;

create sequence tmt_seq; 
update sys_document  set code_document  = to_char(nextval('tmt_seq') + 1000, '0000'); 
drop sequence tmt_seq;

ALTER TABLE public.sys_document ALTER COLUMN code_document SET NOT NULL;

create sequence tmt_seq; 
update sys_unit  set code_unit  = to_char(nextval('tmt_seq') + 1000, '0000'); 
drop sequence tmt_seq;

ALTER TABLE public.sys_unit ALTER COLUMN code_unit SET NOT NULL;

--============================================================================

Drop FUNCTION IF EXISTS fnsys_program_acesso;
CREATE OR REPLACE FUNCTION public.fnsys_program_acesso(pvsysid character varying, pvuserlogin character varying, pvsysprogramadmin character varying, pvsysprogrammenu character varying, pvsysprogramfavorite character varying, pvSysProgramId varchar)
 RETURNS TABLE(sys_program_id character varying, sys_program_name character varying, sys_program_code_program character varying, sys_program_code_program_desc character varying, sys_program_controller character varying, sys_program_type_program character varying, sys_program_icon character varying, sys_module_id character varying, sys_module_name character varying, sys_module_icon character varying, sys_module_code_module character varying, sys_module_code_module_desc character varying, sys_module_color character varying, sys_module_order_visual numeric, sys_program_is_favorite character varying)
 LANGUAGE plpgsql
AS $function$
DECLARE
vSql varchar;
r record;
begin
	
			vSql = 'select distinct
								t1.id as sys_program_id,
								t1.name as sys_program_name,
								t1.code_program as sys_program_code_program,
								t1.code_program||''-''||t1.name as sys_program_code_program_desc,
								t1.controller as sys_program_controller,
								t1.type_program as sys_program_type_program,
								t1.icon as sys_program_icon,
								t1.sys_module_id,
								t2.name as sys_module_name,
								t2.icon as sys_module_icon,
								t2.code_module as sys_module_code_module,
								t2.code_module||''-''||t2.name as sys_module_code_module_desc,
								t2.color as sys_module_color,
								t2.order_visual as sys_module_order_visual,
								case when (select count(1)
									 from sys_program_favorite x1,
												sys_user x2
									 where x1.sys_program_id = t1.id
										 and x1.sys_user_id = x2.id
										 and x2.active = ''S''
										 and x2.login = '''||pvUserLogin||''') > 0 then ''S'' else ''N'' end as sys_program_is_favorite
								from sys_program t1, 
										 sys_module  T2
								where t1.sys_module_id = t2.id
									and t1.menu = '''||pvSysProgramMenu||'''
									and t1.admin like '''||pvSysProgramAdmin||'''
									and t1.id like '''||pvSysProgramId||'''
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
	    sys_program_code_program     := r.sys_program_code_program;
		sys_program_code_program_desc := r.sys_program_code_program_desc;
		sys_program_controller       := r.sys_program_controller;
		sys_program_type_program     := r.sys_program_type_program;
		sys_program_icon             := r.sys_program_icon;
		sys_module_id                := r.sys_module_id;
		sys_module_name              := r.sys_module_name;
		sys_module_icon              := r.sys_module_icon;
		sys_module_code_module      := r.sys_module_code_module;
		sys_module_code_module_desc := r.sys_module_code_module_desc;
		sys_module_color             := r.sys_module_color;
		sys_module_order_visual      := r.sys_module_order_visual;
		sys_program_is_favorite      := r.sys_program_is_favorite;
	RETURN NEXT;
	
	END loop;


	
end;
$function$
;


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
