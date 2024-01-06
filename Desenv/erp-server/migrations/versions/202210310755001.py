from alembic import op


revision = "202210310755001"
down_revision = "202210310755000"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
ALTER TABLE ope_atividade_sistema RENAME COLUMN sigla_atividade_grupo TO sigla_atividade_sistema;

ALTER TABLE ind_cnd ADD sigla_ind_cnd varchar(50) NULL;
COMMENT ON COLUMN ind_cnd.sigla_ind_cnd IS 'Sigla - Ind Cnd';

ALTER TABLE ope_centro_subtipo ADD sigla_centro_subtipo varchar(50) NULL;

ALTER TABLE sys ADD sigla_sys varchar(50) NULL;
COMMENT ON COLUMN sys.sigla_sys IS 'Sigla Sistema';


--UPGRADE
-- Auto-generated SQL script #202211011245
UPDATE sys_program
	SET controller='/private/ger/geritemserv'
	WHERE id='1f50f139-382c-4cfd-a0fa-659e086d94b5';
-- Auto-generated SQL script #202211011246
UPDATE sys_program
	SET "name"='NCM'
	WHERE id='fe95af96-70d4-428b-a913-99bb6c0e597c';

-- Auto-generated SQL script #202211011437
UPDATE sys
	SET sigla_sys='WEB'
	WHERE id='e8329d00-443f-4c03-8e73-c161f0d4f37d';
UPDATE sys
	SET sigla_sys='DESKTOP'
	WHERE id='c8a70a60-73b5-4ba4-a97d-d754499ddb3c';
UPDATE sys
	SET sigla_sys='MOBILE'
	WHERE id='16afb315-e210-42e4-9b15-ece23f5808c6';
UPDATE sys
	SET sigla_sys='TST1'
	WHERE id='5faa8a21-05e2-4475-88a7-ec474ae1d459';


---DELETE
-- Auto-generated SQL script #202211011247
DELETE FROM sys_program
	WHERE id='13253c34-5407-44bb-998a-5d56b7ed89d7';

-- Auto-generated SQL script #202211011247
DELETE FROM sys_program
	WHERE id='8ad6ba2d-e546-4ab7-9cba-73a58531bf94';

-- Auto-generated SQL script #202211011247
DELETE FROM sys_program
	WHERE id='36cee55e-95a5-45ca-9cd6-a3b0a14dbec2';

--type


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('12bfdce3-111e-40d6-9a09-e2f8c83ff20f','fin_recibo','admin','status','PD','Pendente');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('ef532c0f-e12f-4dbc-9216-dfdc97e049e2','fin_recibo','admin','status','AS','Assinado');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('60d6928b-c2fb-4f60-81f2-ab11e1bef0a9','fin_recibo','admin','status','EA','Enviado para Assinatura');

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
