from alembic import op
import sqlalchemy as sa

revision = '202206151339016'
down_revision = '202206151339015'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""

alter table sys_plan_restriction add value_restriction_blocked int4;
alter table sys_restriction_licence add value_restriction_blocked int4;
COMMENT ON COLUMN sys_plan_restriction.value_restriction_blocked IS 'Valor da Restricao - Bloqueada';
COMMENT ON COLUMN sys_restriction_licence.value_restriction_blocked IS 'Valor da Restricao - Bloqueada';

alter table sys_plan_restriction add days_blocked int4;
alter table sys_restriction_licence add days_blocked  int4;
COMMENT ON COLUMN sys_plan_restriction.days_blocked  IS 'Dias para Bloqueio';
COMMENT ON COLUMN sys_restriction_licence.days_blocked  IS 'Dias para Bloqueio';

alter table sys_plan_restriction add days_blocked_extra int4;
alter table sys_restriction_licence add days_blocked_extra  int4;
COMMENT ON COLUMN sys_plan_restriction.days_blocked_extra  IS 'Dias para Bloqueio - Extra';
COMMENT ON COLUMN sys_restriction_licence.days_blocked_extra  IS 'Dias para Bloqueio - Extra';


alter table sys_restriction add type_value varchar(1);
COMMENT ON COLUMN sys_restriction.type_value IS 'Tipo: Q-Quantitativo, L-Logico';
update sys_restriction set type_value='Q';

comment on column sys_plan.type_plan IS 'Tipo: FR-Free, TR-Trial, PG-Pago, PU-Pagamento Ãºnico';

alter table sys_plan add indicated varchar(1);
COMMENT ON COLUMN sys_plan.indicated IS 'Indicado';
update sys_plan set indicated='N';


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
