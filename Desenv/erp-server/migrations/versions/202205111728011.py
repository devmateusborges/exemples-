from alembic import op
import sqlalchemy as sa

revision = '202205111728011'
down_revision = '202205111728010'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
  alter table sys_user add image_url varchar(1000);
alter table sys_user add email_verified varchar(1);
alter table sys_user add provider varchar(50);
alter table sys_user add provider_code varchar(50);
comment on column sys_user.image_url IS 'Url da imagem do usuario';
comment on column sys_user.email_verified IS 'Email verificado';
comment on column sys_user.email_verified IS 'Provider de autenticacao';
comment on column sys_user.email_verified IS 'Codigo do provider autenticado';


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
