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


