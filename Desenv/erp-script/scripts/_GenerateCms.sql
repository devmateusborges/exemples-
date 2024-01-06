--====================================================================================
--Gera
--====================================================================================

DO $$
DECLARE 
vI INTEGER;
vIdPost VARCHAR(36);
seq INTEGER := 1;

BEGIN
	FOR vI IN 1..100 loop
		SELECT uuid_generate_v4() INTO vIdPost;
		

	    INSERT INTO cms_post (unit_id,sys_user_id,id,titulo,corpo,status,favorito,util_blog,util_depoimento,util_treinamento,util_help,tipo_render,log_user_ins)
		VALUES ('f3996813-838e-49af-9649-8dc44e24bc75','062dddad-4ca3-4956-aa75-6f6cf368b05b',vIdPost ,'TESTE'||cast(seq as varchar),cast(seq as varchar)||'-Generate Lorem Ipsum placeholder text for use in your graphic, print and web layouts, and discover plugins for your favorite writing, design and blogging tools. Generate Lorem Ipsum placeholder text for use in your graphic, print and web layouts, and discover plugins for your favorite writing, design and blogging tools. Generate Lorem Ipsum placeholder text for use in your graphic, print and web layouts, and discover plugins for your favorite writing, design and blogging tools. Generate Lorem Ipsum placeholder text for use in your graphic, print and web layouts, and discover plugins for your favorite writing, design and blogging tools. Generate Lorem Ipsum placeholder text for use in your graphic, print and web layouts, and discover plugins for your favorite writing, design and blogging tools. Generate Lorem Ipsum placeholder text for use in your graphic, print and web layouts, and discover plugins for your favorite writing, design and blogging tools. Generate Lorem Ipsum placeholder text for use in your graphic, print and web layouts, and discover plugins for your favorite writing, design and blogging tools. Generate Lorem Ipsum placeholder text for use in your graphic, print and web layouts, and discover plugins for your favorite writing, design and blogging tools. Generate Lorem Ipsum placeholder text for use in your graphic, print and web layouts, and discover plugins for your favorite writing, design and blogging tools. Generate Lorem Ipsum placeholder text for use in your graphic, print and web layouts, and discover plugins for your favorite writing, design and blogging tools.','C','S','S','S','S','S','M','admin');

	

	INSERT INTO cms_post_grupo (cms_post_id,cms_grupo_id)
				VALUES (vIdPost,'7205374c-2be6-4b24-a13a-1bbec18ef728');

			

				INSERT into cms_post_tag  (cms_post_id,cms_tag_id)
				VALUES (vIdPost,'567aa2bc-60c3-4da6-8996-7cf450b0ed2e');

			
		seq := seq+1;
		
	END LOOP;
END$$;	


--====================================================================================
--Limpeza geral do teste
--====================================================================================
delete from cms_post suu where unit_id = 'f3996813-838e-49af-9649-8dc44e24bc75';


select count(1) from cms_post
select * from sys_user