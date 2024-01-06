from alembic import op
import sqlalchemy as sa

revision = '202206151339044'
down_revision = '202206151339043'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
	
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e42e14e6-e171-478c-b36a-ebde5b285d30','ind_prm','admin','tipo_entrada','CD','Combo Fonte Tabela');

ALTER TABLE fin_lote
ADD ativo VARCHAR(1) NULL;

COMMENT ON COLUMN fin_lote.ativo IS 'Ativo: S-Sim, N-Não';

delete FROM sys_program where id='cda2dadb-e23c-47bc-9723-62952329e0c6';
update sys_program set controller='/private/tst/test1' where id= '9409eb65-56a3-4ffa-a53c-68122d440d9b';

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
