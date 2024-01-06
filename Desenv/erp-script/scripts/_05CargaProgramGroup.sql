INSERT INTO public.system_group(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd) VALUES ('0256e515-51a4-49a2-a8b8-adc36470cd51', 'Gestor', 'admin', '2020-06-10 08:52:32', NULL, NULL);
INSERT INTO public.system_user_group(id, system_user_id, system_group_id, log_user_ins, log_date_ins, log_user_upd, log_date_upd) VALUES ('9faa3bc9-02d4-4fb7-9f87-94109144d737', '7448e100-8b3c-4cc3-ba78-18b230339005', '4218d8f1-8595-4052-aace-ba36f772623e', 'admn', '2020-06-10 11:33:06', NULL, NULL);
INSERT INTO public.system_user_group(id, system_user_id, system_group_id, log_user_ins, log_date_ins, log_user_upd, log_date_upd) VALUES ('9faa3bc9-02d4-4fb7-9f87-94109144d737', '7448e100-8b3c-4cc3-ba78-18b230339005', '0256e515-51a4-49a2-a8b8-adc36470cd51', 'admn', '2020-06-10 11:33:06', NULL, NULL);


--================================================================
--Liberar acesso para todos usuários
--================================================================
delete from system_group_program a where system_group_id='4218d8f1-8595-4052-aace-ba36f772623e';
insert into system_group_program(id,system_group_id,system_program_id)
   select uuid_generate_v4(),'4218d8f1-8595-4052-aace-ba36f772623e', b.id
     from system_program b;


--================================================================
--Liberar acesso para todos usuários - user não admin
--================================================================
delete from system_group_program a where system_group_id='0256e515-51a4-49a2-a8b8-adc36470cd51';
insert into system_group_program(id,system_group_id,system_program_id)
   select uuid_generate_v4(),'0256e515-51a4-49a2-a8b8-adc36470cd51', b.id
     from system_program b
		  where b.admin='N';
			
		 
select uuid_generate_v4()

select * from system_group