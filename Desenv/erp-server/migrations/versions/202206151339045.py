from alembic import op
import sqlalchemy as sa

revision = '202206151339045'
down_revision = '202206151339044'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
	
---fin_class

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d72b5b09-0df6-43a9-b269-ce519954c490','fin_class','admin','tipo_es','E','Entrada');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('479a20ad-d278-41e1-b977-0aa962c171ae','fin_class','admin','tipo_es','S','Saida');



---fin_recibo_tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f730fd9d-d17d-4440-834e-2d5852abee3a','fin_recibo_tipo','admin','padrao','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d2cac217-6d2f-45d6-bade-ad1c648a18d1','fin_recibo_tipo','admin','padrao','N','Não');

---fin_tipo_variacao


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('49f9d591-f260-4d25-adcc-5d4a740251dd','fin_tipo_variacao','admin','tipo','J','Juros');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('c4112178-b089-4da0-b155-672a7b3be01a','fin_tipo_variacao','admin','tipo','D','Descontos');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d0516c68-c1d9-4b3e-8c37-d5b5dc7b263c','fin_tipo_variacao','admin','tipo','A','Abatimento');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('657bb947-32c6-4d95-9e91-d8a257ecaa81','fin_tipo_variacao','admin','tipo','M','Multa');


---ger empresa

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('52e82e81-3a58-4e7d-8fdc-d3d1a9a2a14d','ger_empresa','admin','fis_incent_cultura','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b7844312-2849-4a89-8fea-b5074318a4bb','ger_empresa','admin','fis_incent_cultura','N','Não');


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('28541ac3-3d2a-4c2c-b03f-fcfd56908dab','ger_empresa','admin','fis_incent_fiscal_nfs_ob','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('bdf4d5b9-36e5-496b-846b-93ee90d90851','ger_empresa','admin','fis_incent_fiscal_nfs_ob','N','Não');

---ind_prm

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('718b36ed-16bf-44f9-b08e-7f6a7f839595','ind_prm','admin','internal','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('71041b5b-66af-4b67-9bb5-7620e2d54bf4','ind_prm','admin','internal','N','Não');

---ope_centro_tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('aeade5c4-17bb-4a26-9daa-193a51bd2fbd','ope_centro_tipo','admin','tipo_es','E','Entrada');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1635892a-32b3-405e-b7bc-3e563d3632ca','ope_centro_tipo','admin','tipo_es','S','Saida');


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
