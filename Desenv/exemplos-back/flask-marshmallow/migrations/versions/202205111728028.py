from alembic import op
import sqlalchemy as sa

revision = '202205111728028'
down_revision = '202205111728027'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""

ALTER TABLE sys_migration
DROP COLUMN  log_user_ins;

ALTER TABLE sys_migration
DROP COLUMN  log_date_ins;

ALTER TABLE sys_migration
DROP COLUMN  log_user_upd;

ALTER TABLE sys_migration
DROP COLUMN  log_date_upd; 

 
    
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

               """)
 

def downgrade():
    pass