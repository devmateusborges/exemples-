from alembic import op

revision = "202210310755005"
down_revision = "202210310755004"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """

alter table fis_certificado  drop column nome_arq_certificado;
alter table sys_document  drop column fin_pagrec_id;
alter table sys_document  drop column ger_pessoa_id ;
alter table sys_document  drop column crm_mov_id ;
alter table sys_document  drop column mov_id ;
alter table sys_document  drop column ope_centro1_id ;
alter table sys_document  drop column ope_centro2_id ;
alter table sys_document  drop column ope_centro2_ord_id ;
alter table sys_document  drop column ope_compart_id ;
alter table sys_document  drop column ope_compart_ocor_id ;
alter table sys_document  drop column ope_ocor_id ;
alter table sys_document  drop column sys_user_id ;
alter table sys_document  drop column cms_post_id ;
alter table sys_document  add orig_type varchar(50);
alter table sys_document  add orig_id varchar(36);
COMMENT ON COLUMN sys_document.orig_type IS 'Tipo da Origem';
COMMENT ON COLUMN sys_document.orig_id IS 'ID da Origem';

Drop FUNCTION IF EXISTS fnsys_program_acesso;
CREATE OR REPLACE FUNCTION public.fnsys_program_acesso(pvsysid character varying, pvuserlogin character varying, pvsysprogramadmin character varying, pvsysprogrammenu character varying, pvsysprogramfavorite character varying, pvSysProgramId varchar)
 RETURNS TABLE(sys_program_id character varying, sys_program_name character varying, sys_program_controller character varying, sys_program_type_program character varying, sys_program_icon character varying, sys_module_id character varying, sys_module_name character varying, sys_module_icon character varying, sys_module_sigla_module character varying, sys_module_sigla_module_desc character varying, sys_module_color character varying, sys_module_order_visual numeric, sys_program_is_favorite character varying)
 LANGUAGE plpgsql
AS $function$
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
		sys_program_is_favorite      := r.sys_program_is_favorite;
	RETURN NEXT;
	
	END loop;



end;
$function$
;

CREATE TABLE sys_unit_manager (
  id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
  name varchar(100) ,
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  active varchar(1) ,
	subdomain_name varchar(100),
	subdomain_active varchar(1),
	color_primary varchar(100),
	color_secondary varchar(100),
	color_general_background varchar(100),
	color_menu_module_background varchar(100),
	color_menu_module_font varchar(100),
	icon_menu varchar(250),
	icon_login varchar(250),
	icon_general varchar(250),
	link_website varchar(250),
	link_policy_private varchar(250),
	link_term_of_use varchar(250),
  CONSTRAINT pk_sys_unit_manager PRIMARY KEY (id)
);
COMMENT ON TABLE sys_unit_manager IS 'System-Gestora de Unidade';
COMMENT ON COLUMN sys_unit_manager.id IS 'ID da Gestora de Unidade';
COMMENT ON COLUMN sys_unit_manager.name IS 'Nome';
COMMENT ON COLUMN sys_unit_manager.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_unit_manager.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_unit_manager.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_unit_manager.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN sys_unit_manager.active IS 'Ativo: S-Sim, N-Não';

COMMENT ON COLUMN sys_unit_manager.subdomain_name IS 'Subdominio';
COMMENT ON COLUMN sys_unit_manager.subdomain_active IS 'Subdominio - Ativo';
COMMENT ON COLUMN sys_unit_manager.color_primary IS 'Cor - Primária';
COMMENT ON COLUMN sys_unit_manager.color_secondary IS 'Cor - Secondária'; 
COMMENT ON COLUMN sys_unit_manager.color_general_background IS 'Cor - Fundo geral'; 
COMMENT ON COLUMN sys_unit_manager.color_menu_module_background IS 'Cor - Menu Module fundo'; 
COMMENT ON COLUMN sys_unit_manager.color_menu_module_font IS 'Cor - Menu Module Fonte';
COMMENT ON COLUMN sys_unit_manager.icon_menu IS 'Icone - Menu'; 
COMMENT ON COLUMN sys_unit_manager.icon_login IS 'Icone - Login';
COMMENT ON COLUMN sys_unit_manager.icon_general IS 'Icone - Geral';
COMMENT ON COLUMN sys_unit_manager.link_website IS 'Link - Website';
COMMENT ON COLUMN sys_unit_manager.link_policy_private IS 'Link - Politica de Privacidade'; 
COMMENT ON COLUMN sys_unit_manager.link_term_of_use IS 'Link - Termo de Uso'; 


INSERT INTO sys_unit_manager(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,
	subdomain_name,
	subdomain_active,
	color_primary,
	color_secondary,
	color_general_background,
	color_menu_module_background,
	color_menu_module_font,
	icon_menu,
	icon_login,
	icon_general,
	link_website,
	link_policy_private,
	link_term_of_use ) VALUES ('1338cde6-3e48-4ec1-873c-5dc237d77f9b', '', 'admin', '2022-10-28 14:34:23', NULL, NULL, 'S',
'resultfacil',
'S',
'#047cfc',
'#04ac3c',
'#fcfcfc',
'#047cfc',
'#ffffff',
'logo.png',
'logo.png',
'logo.png',
'www.resutfacil.com.br',
'www.resutfacil.com.br',
'www.resutfacil.com.br'
);


alter table sys_unit add sys_unit_manager_id varchar(36);
COMMENT ON COLUMN sys_unit.sys_unit_manager_id IS 'ID da Gestora de Unidade';
update sys_unit set sys_unit_manager_id='1338cde6-3e48-4ec1-873c-5dc237d77f9b';
alter table sys_unit alter column sys_unit_manager_id set not null;
alter table sys_unit  add CONSTRAINT fk_sys_unit_sys_unit_manager_id FOREIGN KEY (sys_unit_manager_id) REFERENCES sys_unit_manager (id) ON DELETE NO ACTION ON UPDATE NO ACTION;



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
