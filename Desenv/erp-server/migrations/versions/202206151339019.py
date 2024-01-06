from alembic import op
import sqlalchemy as sa

revision = '202206151339019'
down_revision = '202206151339018'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""

alter table sys_access_log add log_date_ins timestamp(0);
alter table sys_access_log add log_date_upd timestamp(0);

alter table sys_access_log add log_user_ins varchar(100);
alter table sys_access_log add log_user_upd varchar(100);

COMMENT ON COLUMN sys_access_log.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_access_log.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN sys_access_log.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_access_log.log_user_upd IS 'Log - Usuário de Alteração';

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
