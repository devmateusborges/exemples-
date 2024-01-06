from alembic import op
import sqlalchemy as sa

revision = '202206151339034'
down_revision = '202206151339033'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
ALTER TABLE sys_group_program DROP CONSTRAINT fk_sys_group_program_sys_program_id;
ALTER TABLE sys_group_program ADD CONSTRAINT fk_sys_group_program_sys_program_id FOREIGN KEY (sys_program_id) REFERENCES sys_program(id) ON DELETE CASCADE;

ALTER TABLE sys_plan_restriction DROP CONSTRAINT fk_sys_plan_restriction_system_plan_id;
ALTER TABLE sys_plan_restriction ADD CONSTRAINT fk_sys_plan_restriction_system_plan_id FOREIGN KEY (sys_plan_id) REFERENCES sys_plan(id) ON DELETE CASCADE;

ALTER TABLE sys_user_group DROP CONSTRAINT fk_sys_user_group_system_user_id;
ALTER TABLE sys_user_group ADD CONSTRAINT fk_sys_user_group_system_user_id FOREIGN KEY (sys_user_id) REFERENCES sys_user(id) ON DELETE CASCADE;

ALTER TABLE sys_user_program DROP CONSTRAINT fk_sys_user_program_sys_user_id;
ALTER TABLE sys_user_program ADD CONSTRAINT fk_sys_user_program_sys_user_id FOREIGN KEY (sys_user_id) REFERENCES sys_user(id) ON DELETE CASCADE;


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
