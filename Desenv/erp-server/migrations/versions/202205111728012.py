from alembic import op
import sqlalchemy as sa

revision = '202205111728012'
down_revision = '202205111728011'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
  INSERT INTO sys_user(id, log_date_ins, log_date_upd, log_user_ins, log_user_upd, active, active_message, admin, chat, document, email, email_verified, frontpage_id, image_url, login, login_ext, name, origem, password, phone, provider, provider_code) VALUES ('062dddad-4ca3-4956-aa75-6f6cf368b05b', '2022-04-25 23:46:15', NULL, 'admin', NULL, 'S', NULL, 'S', 'S', NULL, 'admin@admin.com', 'S', NULL, NULL, 'admin', NULL, 'Admin', '1', '$pbkdf2-sha256$29000$937v3XsPwTjHOCfEmDOGkA$U3pam0d7LYzHFI23rKwuaIELJw7sWurNItuGUidU7v4', NULL, 'local', NULL);

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
