from alembic import op
import sqlalchemy as sa

revision = '202206151339029'
down_revision = '202206151339028'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""

 alter table test1 add valor numeric(18,6);
 alter table test1 add quantidade numeric(18,6);
 alter table test1 add ativo varchar(1);
 
COMMENT ON COLUMN test1.valor IS 'Valor';
COMMENT ON COLUMN test1.quantidade IS 'Quantidade';
COMMENT ON COLUMN test1.ativo IS 'Ativo: S-Sim, N-Não';

alter table test1 add unit_id varchar(36);
 
ALTER TABLE test1
ADD FOREIGN KEY (unit_id) REFERENCES sys_unit(id);

alter table test1_child add unit_id varchar(36);
 
ALTER TABLE test1_child
ADD FOREIGN KEY (unit_id) REFERENCES sys_unit(id);

alter table test1_fk add unit_id varchar(36);
 
ALTER TABLE test1_fk
ADD FOREIGN KEY (unit_id) REFERENCES sys_unit(id);
        
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
