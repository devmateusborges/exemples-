from alembic import op
import sqlalchemy as sa

revision = '202206151339003'
down_revision = '202206151339002'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""

comment on column fin_pagrec_tipo.aceita_entrada is 'aceita entrada: S-Sim, N-Não';
comment on column fin_pagrec_tipo.aceita_saida is 'aceita entrada: S-Sim, N-Não';
comment on column fin_pagrec_versao.versao_atual is 'aceita entrada: S-Sim, N-Não';
comment on column fin_pagrec_versao.versao_atual is 'aceita entrada: S-Sim, N-Não';
    
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
