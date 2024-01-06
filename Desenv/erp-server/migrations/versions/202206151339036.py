from alembic import op
import sqlalchemy as sa

revision = '202206151339036'
down_revision = '202206151339035'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""

alter table sys_unit_param add data_valid_ini date;
alter table ger_unit_param add data_valid_ini date;
alter table fin_unit_param add data_valid_ini date;
alter table ctb_unit_param add data_valid_ini date;
alter table fis_unit_param add data_valid_ini date;
alter table bor_unit_param add data_valid_ini date;
alter table pto_unit_param add data_valid_ini date;
alter table rhm_unit_param add data_valid_ini date;
alter table crm_unit_param add data_valid_ini date;
alter table ope_unit_param add data_valid_ini date;
alter table bov_unit_param add data_valid_ini date;
alter table mov_unit_param add data_valid_ini date;
alter table mob_unit_param add data_valid_ini date;
alter table ind_unit_param add data_valid_ini date;

COMMENT ON COLUMN sys_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN ger_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN fin_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN ctb_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN fis_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN bor_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN pto_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN rhm_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN crm_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN ope_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN bov_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN mov_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN mob_unit_param.data_valid_ini IS 'Validar Data Inicio';
COMMENT ON COLUMN ind_unit_param.data_valid_ini IS 'Validar Data Inicio';

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
