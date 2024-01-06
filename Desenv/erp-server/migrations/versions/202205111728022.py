from alembic import op
import sqlalchemy as sa

revision = '202205111728022'
down_revision = '202205111728021'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""

alter table sys_group_program RENAME column system_group_id to sys_group_id;
alter table sys_group_program RENAME column system_program_id to sys_program_id;
alter table sys_group_program RENAME constraint fk_sys_group_program_system_group_id to fk_sys_group_program_sys_group_id;
alter table sys_group_program RENAME constraint fk_sys_group_program_system_program_id to fk_sys_group_program_sys_program_id;

ALTER TABLE sys_document
ADD active VARCHAR(1) NULL;


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
