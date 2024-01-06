from alembic import op
import sqlalchemy as sa

revision = '202205111728016'
down_revision = '202205111728015'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
  create table test1 (
       id varchar(36) not null,
        log_date_ins timestamp,
        log_date_upd timestamp,
        log_user_ins varchar(100),
        log_user_upd varchar(100),
        codigo varchar(50) not null,
        descricao varchar(100) not null,
        dt_nascimento timestamp not null,
        constraint pk_test1 primary key (id)
    );

    create table test1_child (
        id varchar(36) not null,
        log_date_ins timestamp,
        log_date_upd timestamp,
        log_user_ins varchar(100),
        log_user_upd varchar(100),
        codigo varchar(50) not null,
        quantidade numeric(18, 6) not null,
        valor_total numeric(18, 2) not null,
        valor_unit numeric(18, 2) not null,
        test1_id varchar(36) not null,
        constraint pk_test1_child primary key (id)
    );

    alter table test1_child
       add constraint fk_test1_child_test1_id
       foreign key (test1_id)
       references test1;


alter table sys_unit add active varchar(1);

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

               """)
 

def downgrade():
    pass