from alembic import op


revision = "202211301615003"
down_revision = "202211301615002"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('c3ce6551-a59f-4512-a3da-52172b0d68d3','crm_status_prox','admin','tipo_status_ant','AB','Aberto');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6bf59434-5b15-479f-a5b6-c67852c05553','crm_status_prox','admin','tipo_status_ant','PE','DescPendente');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('312dcadf-8cec-46a6-9574-ac4186be4598','crm_status_prox','admin','tipo_status_ant','AI','AbatiAndamento');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('08de962c-ea91-4bad-ab5b-0fe61d20d968','crm_status_prox','admin','tipo_status_ant','AT','Andamento Transf');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('cf3907e0-d71a-492d-86d4-f007ae83a467','crm_status_prox','admin','tipo_status_ant','FM','Finalizado');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9e35b4e2-e535-4a17-b197-b8de48135fdf','crm_status_prox','admin','tipo_status_ant','CA','Cancelado');

ALTER TABLE ope_atividade_relac_prod DROP CONSTRAINT fk_ope_atividade_relac_prod_ope_atividade_id;
ALTER TABLE ope_atividade_relac_prod ADD CONSTRAINT fk_ope_atividade_relac_prod_ope_atividade_id FOREIGN KEY (ope_atividade_id) REFERENCES ope_atividade(id) ON DELETE CASCADE ON UPDATE CASCADE;


ALTER TABLE ope_atividade_relac_prod DROP CONSTRAINT fk_ope_atividade_relac_prod_ope_atividade_id_prod;
ALTER TABLE ope_atividade_relac_prod ADD CONSTRAINT fk_ope_atividade_relac_prod_ope_atividade_id_prod FOREIGN KEY (ope_atividade_id_prod) REFERENCES ope_atividade(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE sys_licence ALTER COLUMN log_date_ins DROP NOT NULL;

--== permisão para grupos o restante 
INSERT INTO sys_user_group
(id, sys_user_id, sys_group_id, log_user_ins, log_date_ins, log_user_upd, log_date_upd)
VALUES('4218d8f1-c757-4488-92ef-ba36f772623e', '062dddad-4ca3-4956-aa75-6f6cf368b05b', '4218d8f1-8595-4052-aace-ba36f772623e', NULL, '2022-12-15 08:53:00.000', NULL, NULL);


ALTER TABLE sys_module ALTER COLUMN color DROP NOT NULL;

-- Auto-generated SQL script #202212161353
UPDATE sys_type_description
	SET description_type='Saída'
	WHERE id='21f35e75-5bd8-457b-b98f-b700b61d4a65';

ALTER TABLE crm_class ALTER COLUMN crm_class_subgrupo_id DROP NOT NULL;

COMMENT ON COLUMN crm_org.ger_visual_user IS 'Gerente visualiza atendimento de outros usuários: S-Sim, N-Não';
COMMENT ON COLUMN crm_org.user_visual_user IS 'Usuário visualiza atendimento de outros usuários: S-Sim, N-Não';

COMMENT ON COLUMN ctb_conta_versao.versao_atual IS 'Versão Atual: S-Sim, N-Não';

-- Auto-generated SQL script #202212260750
UPDATE sys_restriction
	SET active='S'
	WHERE id='c7924fb8-b0f5-49ae-9d17-311cf96f545e';
UPDATE sys_restriction
	SET active='S'
	WHERE id='31da7d22-1925-4f32-85cc-d578834aad3a';
UPDATE sys_restriction
	SET active='S'
	WHERE id='a95523e8-eaf6-49c4-b6e6-dbf871571e2f';
UPDATE sys_restriction
	SET active='S'
	WHERE id='99d94b26-e2e9-4734-bb33-dd2819bd6f7b';
UPDATE sys_restriction
	SET active='S'
	WHERE id='fd554963-84a1-4ff5-be38-1ca59d191170';
UPDATE sys_restriction
	SET active='S'
	WHERE id='9f42d6b8-dfab-4f6a-a5b5-345b5c34f490';
UPDATE sys_restriction
	SET active='S'
	WHERE id='c4cf4f41-c997-4978-8429-a4814c2c120f';
UPDATE sys_restriction
	SET active='S'
	WHERE id='63f44e43-8012-4ab6-bec7-f8053b46e3f2';
UPDATE sys_restriction
	SET active='S'
	WHERE id='63b952a4-970e-4df9-892e-2a771613d36d';
UPDATE sys_restriction
	SET active='S'
	WHERE id='77184dfc-4ca5-4a3d-b44e-342cee684e34';
UPDATE sys_restriction
	SET active='S'
	WHERE id='c0b8eb6a-ea68-4de1-b779-97af7ffd9245';
UPDATE sys_restriction
	SET active='S'
	WHERE id='699c1cc5-a71d-403a-a7fc-1b0e52252762';
UPDATE sys_restriction
	SET active='S'
	WHERE id='5549653e-5d11-4a83-b644-3309f2c3fcd6';
UPDATE sys_restriction
	SET active='S'
	WHERE id='c1764231-869d-428b-a67b-4319271281e3';
UPDATE sys_restriction
	SET active='S'
	WHERE id='8e44b028-d418-4712-8738-0461e48d76af';
UPDATE sys_restriction
	SET active='S'
	WHERE id='3e76241d-1a7f-459e-96cd-b15ea9db8fa2';
UPDATE sys_restriction
	SET active='S'
	WHERE id='423a9d75-f2bb-48b1-9cd3-6273fc632f53';
UPDATE sys_restriction
	SET active='S'
	WHERE id='cfc30725-0b30-4f68-a482-cf10a48681ef';
UPDATE sys_restriction
	SET active='S'
	WHERE id='c6365950-680d-42ca-b5e0-c86ca9f7183c';
UPDATE sys_restriction
	SET active='S'
	WHERE id='6f411fd2-8499-4400-b1d1-7677b4ebbaf8';



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
