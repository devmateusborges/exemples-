from alembic import op


revision = "202211100921002"
down_revision = "202211100921001"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """

------translate DETS

INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('10751432-bf3b-41f1-941a-2c53da56867c','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18GERALVARIACAODOITEM/SERVICOSIGLA','geral-variação do item/serviço - sigla','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('9d38f82e-5bbf-4de1-8086-28acca35f8ba','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18GERALVARIACAODOITEM/SERVICOSIGLA','general item/service variation - acronym','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('13b7de9b-663d-451e-a22c-61634cd8b41f','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18GERALVARIACAODOITEM/SERVICOSIGLA','Artículo general/variación de servicio - acrónimo','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('52bd5b63-9660-469d-be63-df6768f4eaed','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18CICLODAVARIEDADESIGLA','ciclo da variedade - sigla','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('057c9a40-9788-4e9f-902e-f6b8bf04652b','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18CICLODAVARIEDADESIGLA','variety cycle - acronym','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('27d7a5a9-8867-4f20-afed-f892453e46d7','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18CICLODAVARIEDADESIGLA','Ciclo de variedades - acrónimo','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('23b21087-3250-4d76-bbfe-52d6398bde5b','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18CICLODAVARIEDADENOME','ciclo da variedade - nome','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('4e9a91e0-4633-4d37-8ecb-cad376ee0590','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18CICLODAVARIEDADENOME','variety cycle - name','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('db13f40b-d2da-4a14-81fc-4d30b9924d3d','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18CICLODAVARIEDADENOME','Ciclo de variedades - Nombre','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('0488d6be-7cac-4a33-8964-6f384cae7ebf','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18SYSTEMUNIDADESIGLA','system-unidade - sigla','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('1ea8e01c-c579-4846-979a-3d7405f50432','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18SYSTEMUNIDADESIGLA','system -unit - acronym','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('0801afc7-ac38-4a1b-bff8-67d134e6000e','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18SYSTEMUNIDADESIGLA','Sistema -unidad - acrónimo','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('036c6563-814c-45bd-a487-248bd7f6fd46','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18GRUPODECONTASIGLA','grupo de conta - sigla','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('b3b8f979-ff23-48dd-a504-488f094385e0','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18GRUPODECONTASIGLA','account group - acronym','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('da70a11a-7579-4a0f-b44a-51143bdd195c','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18GRUPODECONTASIGLA','Grupo de cuentas - acrónimo','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('2c909234-2634-4614-966f-0caf0a353004','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18PERIODOSIGLA','Periodo - Sigla','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('2f7d65b3-6a93-464e-8ad6-73e8f34803c6','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18PERIODOSIGLA','period - acronym','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('a768a1a8-ae9d-41bc-80d4-5c1127024149','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18PERIODOSIGLA','Período - acrónimo','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('afdaf971-5984-4635-ab07-0c2f4c88eec2','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18RESTRICAODESISTEMASIGLA','restrição de sistema - sigla','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('081ef07a-9efe-4dae-9929-b5b757305128','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18RESTRICAODESISTEMASIGLA','system restriction - acronym','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('d290dd4f-c3de-4d2a-aab0-2e21c1d85fc7','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18RESTRICAODESISTEMASIGLA','Restricción del sistema - acrónimo','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('e72b4171-9f76-41ac-9539-2d26ab3ba656','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18RESTRICAODESISTEMANOME','restrição de sistema - nome','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('f1f97da9-7732-4d98-bcc2-880b66a6fc87','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18RESTRICAODESISTEMANOME','system restriction - name','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('6e155e3b-781f-4c3d-a881-83b166c0a29e','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18RESTRICAODESISTEMANOME','Restricción del sistema - Nombre','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('262979aa-0e1d-49c7-bf6c-10cb069886e1','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18PLANOSIGLA','plano - sigla','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('cfd84700-9a65-4937-9f0e-9dce471a80d8','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18PLANOSIGLA','plan - acronym','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('c5dfff81-60d3-4658-a29d-2ffd44d8aeef','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18PLANOSIGLA','Plan - acrónimo','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('00e7c024-4d8b-449c-86e0-b3a42d92b7cf','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18TIPOPLANO','tipo plano','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('e82e2989-df44-41f1-9ca1-e9e5dc5d0dbf','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18TIPOPLANO','plane','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('fcda1256-7ea1-484e-89cb-6ee31ae82805','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18TIPOPLANO','plano','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('2ce1ae45-43b5-4d93-9e34-bdf9693ffc68','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18INDICADO','indicado','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('91945ded-d5f4-473e-bffe-5c2b8cdd31f8','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18INDICADO','indicated','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('c14c88bb-f480-4aac-afdd-18748a19b2d2','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18INDICADO','indicado','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('b603909c-e53f-4209-be66-832748537418','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18SISTEMASIGLA','sistema - sigla','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('99048e58-bdae-42e6-ba91-5ffdf4d84daf','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18SISTEMASIGLA','system - acronym','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('62c194c0-24f5-4769-8eb7-feaf6ab597d7','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18SISTEMASIGLA','Sistema - acrónimo','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('e91ae462-238c-4c5d-9b33-3b5dda08e6dc','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18SISTEMANOME','sistema - nome','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('0d9a7b36-43bd-4bd8-9d50-6226f988b51c','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18SISTEMANOME','system - name','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('b2726537-6bb9-4b6d-afda-92800468a116','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18SISTEMANOME','Nombre del sistema','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('8bb256d8-8ae5-4ace-8a44-5916a9c363b2','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18GRUPOSIGLA','grupo - sigla','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('6c0dbe1f-4d75-44f1-bdc2-0d79af107db3','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18GRUPOSIGLA','group - acronym','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('13f081d4-7af4-4f50-8bdc-8bb457f301b2','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18GRUPOSIGLA','Grupo - acrónimo','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('17e9a65f-5944-4ee7-bb44-19ae5d993b8d','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18DIASPARABLOQUEIO','dias para bloqueio','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('518cfe7a-c488-4d97-80c4-2d94d86a7898','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18DIASPARABLOQUEIO','block days','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('5aa37739-338d-4311-a0b0-e8777ae1d92d','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18DIASPARABLOQUEIO','Días de bloque','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('3928df7a-c2de-4f47-b8ad-d5d5c37c6629','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18PROGAMASIGLA','progama - sigla','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('20abca2e-c442-4c6e-b080-6fd716f81c59','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18PROGAMASIGLA','progama - acronym','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('16b68c11-c183-4e30-944a-4086afa0ee80','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18PROGAMASIGLA','Progama - acrónimo','admin');
INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('bb923ff4-8ee4-4a0a-bb4d-d9776a087e8e','d696d2ba-3744-4103-b9d1-94200b71b11e','DEFAULT','IN18LICENCASIGLA','licença - sigla','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('3849420f-252e-468d-874b-c77710d711c2','dafeb827-969e-461e-8a00-24aaa34839e4','DEFAULT','IN18LICENCASIGLA','license - acronym','admin');
	INSERT INTO sys_translate (id,sys_translate_lang_id,term_group,term_orig,term_translate,log_user_ins) VALUES ('d1b5283c-baf4-4850-9bb2-bdcea8d5679c','941d2fca-5250-4da1-a536-da395e306fad','DEFAULT','IN18LICENCASIGLA','Licencia - acrónimo','admin');


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
