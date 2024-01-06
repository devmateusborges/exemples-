from alembic import op
import sqlalchemy as sa

revision = '202205111728018'
down_revision = '202205111728017'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
   create table test1_fk (
        id varchar(36) not null,
        log_date_ins timestamp,
        log_date_upd timestamp,
        log_user_ins varchar(100),
        log_user_upd varchar(100),
        codigo varchar(50) not null,
        descricao varchar(100) not null,
        constraint pk_test1_fk primary key (id)
    );

--================================================================
--Liberar acesso para todos usuários
--================================================================
--admin interno
delete from sys_group_program a where system_group_id='4218d8f1-8595-4052-aace-ba36f772623e';
insert into sys_group_program(id,system_group_id,system_program_id)
select uuid_generate_v4(),'4218d8f1-8595-4052-aace-ba36f772623e', b.id
from sys_program b;
--admin unit
delete from sys_group_program a where system_group_id='0256e515-51a4-49a2-a8b8-adc36470cd51';
insert into sys_group_program(id,system_group_id,system_program_id)
select uuid_generate_v4(),'0256e515-51a4-49a2-a8b8-adc36470cd51', b.id
from sys_program b where b.admin='N';
commit;
               """)


def downgrade():
    pass
