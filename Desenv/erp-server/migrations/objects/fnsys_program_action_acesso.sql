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
  ROWS 1000