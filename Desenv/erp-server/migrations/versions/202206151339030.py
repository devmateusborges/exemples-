from alembic import op
import sqlalchemy as sa

revision = '202206151339030'
down_revision = '202206151339029'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
 
ALTER TABLE ind_relac DROP CONSTRAINT fk_ind_relac_ind_id;
ALTER TABLE ind_relac ADD CONSTRAINT fk_ind_relac_ind_id FOREIGN KEY (ind_id) REFERENCES ind(id) ON DELETE CASCADE;
ALTER TABLE test1_child DROP CONSTRAINT fk_test1_child_test1_id;
ALTER TABLE test1_child ADD CONSTRAINT fk_test1_child_test1_id FOREIGN KEY (test1_id) REFERENCES test1(id) ON DELETE CASCADE;

ALTER TABLE ind_cjd_relac_ftd DROP CONSTRAINT fk_ind_cjd_relac_ftd_ind_cjd;
ALTER TABLE ind_cjd_relac_ftd ADD CONSTRAINT fk_ind_cjd_relac_ftd_ind_cjd FOREIGN KEY (ind_cjd_id) REFERENCES ind_cjd(id) ON DELETE CASCADE;

ALTER TABLE ind_grupo_relac_sub DROP CONSTRAINT fk_ind_gupo_realc_sub_ind_grupo;
ALTER TABLE ind_grupo_relac_sub ADD CONSTRAINT fk_ind_gupo_realc_sub_ind_grupo FOREIGN KEY (ind_id_grupo) REFERENCES ind_grupo(id) ON DELETE CASCADE;
ALTER TABLE ind_rel_relac_prm DROP CONSTRAINT fk_ind_rel_relac_prm_ind_rel_id;
ALTER TABLE ind_rel_relac_prm ADD CONSTRAINT fk_ind_rel_relac_prm_ind_rel_id FOREIGN KEY (ind_rel_id) REFERENCES ind_rel(id) ON DELETE CASCADE;

ALTER TABLE ind_rel_var DROP CONSTRAINT fk_ind_rel_var_ind_rel_id;
ALTER TABLE ind_rel_var ADD CONSTRAINT fk_ind_rel_var_ind_rel_id FOREIGN KEY (ind_rel_id) REFERENCES ind_rel(id) ON DELETE CASCADE;
ALTER TABLE ind_pnl_relac_rel DROP CONSTRAINT fk_ind_pnl_relac_rel_ind_pnl_id;
ALTER TABLE ind_pnl_relac_rel ADD CONSTRAINT fk_ind_pnl_relac_rel_ind_pnl_id FOREIGN KEY (ind_pnl_id) REFERENCES ind_pnl(id) ON DELETE CASCADE;



ALTER TABLE test1_child RENAME CONSTRAINT test1_child_unit_id_fkey TO fk_test1_child_unit_id;
ALTER TABLE test1 RENAME CONSTRAINT test1_unit_id_fkey TO fk_test1_unit_id;
ALTER TABLE test1_FK RENAME CONSTRAINT test1_fk_unit_id_fkey TO fk_test1_FK_unit_id;

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
