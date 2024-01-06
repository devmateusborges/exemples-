from alembic import op
import sqlalchemy as sa

revision = '202206151339040'
down_revision = '202206151339039'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""

ALTER TABLE public.sys_user_unit RENAME COLUMN unit_id TO sys_unit_id;

INSERT INTO sys_user_unit (id,sys_user_id,sys_unit_id,"owner")
	VALUES ('eb69f32e-b57b-4d06-9f1c-b28efa381b31','062dddad-4ca3-4956-aa75-6f6cf368b05b','f3996813-838e-49af-9649-8dc44e24bc75','S');


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
