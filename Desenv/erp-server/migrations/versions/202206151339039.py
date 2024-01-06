from alembic import op
import sqlalchemy as sa

revision = '202206151339039'
down_revision = '202206151339038'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
COMMENT ON COLUMN sys_user.provider IS 'Tipo do Provider: LOCAL, GOOGLE';
COMMENT ON COLUMN sys_user.provider_code IS 'Codigo do Provider';

alter table sys_token add dt_used timestamp;
COMMENT ON COLUMN sys_token.dt_used IS 'Data utilizacao';

alter table sys_token add data_token text;
COMMENT ON COLUMN sys_token.data_token IS 'Dados do token';


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
