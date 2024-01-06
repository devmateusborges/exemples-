from alembic import op
import sqlalchemy as sa

revision = '202206151339004'
down_revision = '202206151339003'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""




ALTER TABLE sys_group 
ADD active VARCHAR(1) NULL ;

ALTER TABLE sys_restriction 
ADD active VARCHAR(1) NULL ;

ALTER TABLE sys 
ADD active VARCHAR(1) NULL ;

ALTER TABLE sys_module 
ADD active VARCHAR(1) NULL ;

ALTER TABLE sys_plan 
ADD active VARCHAR(1) NULL ;

ALTER TABLE sys_program 
ADD active VARCHAR(1) NULL ;

ALTER TABLE sys_change_log 
DROP COLUMN php_sapi;

ALTER TABLE sys_change_log
DROP COLUMN log_year;

ALTER TABLE sys_change_log
DROP COLUMN log_month;

ALTER TABLE sys_change_log
DROP COLUMN log_day;

comment on column sys_group.active is 'aceita entrada: S-Sim, N-Não';
comment on column sys_restriction.active is 'aceita entrada: S-Sim, N-Não';
comment on column sys.active is 'aceita entrada: S-Sim, N-Não';
comment on column sys_module.active is 'aceita entrada: S-Sim, N-Não';
comment on column sys_plan.active is 'aceita entrada: S-Sim, N-Não';
comment on column sys_program.active is 'aceita entrada: S-Sim, N-Não';
comment on column sys_licence.tipo_doc is 'Tipo documento : RG, CPF, OUTRO...';

--Ger

ALTER TABLE ger_pessoa_conta_banco 
ADD active VARCHAR(1);

ALTER TABLE ger_itemserv_local 
ADD active VARCHAR(1);

ALTER TABLE ger_itemserv_pessoa 
ADD active VARCHAR(1);

ALTER TABLE ger_marca
ADD sigla_ger_marca VARCHAR(100);

ALTER TABLE ger_itemserv_compos_tipo
ADD sigla_ger_itemserv_compos_tipo VARCHAR(100);

ALTER TABLE ger_itemserv_subgrupo
ADD sigla_ger_itemserv_subgrupo VARCHAR(100);

ALTER TABLE ger_empresa_grupo
ADD sigla_ger_empresa_grupo VARCHAR(100);

ALTER TABLE ger_est_nivel
ADD sigla_ger_est_nivel VARCHAR(100);

ALTER TABLE ger_itemserv_grupo
ADD sigla_ger_itemserv_grupo VARCHAR(100);

ALTER TABLE ger_itemserv_lote
ADD sigla_ger_marca_modelo VARCHAR(100);

ALTER TABLE ger_numeracao
ADD sigla_ger_numeracao VARCHAR(100);


ALTER TABLE ger_empresa_param
DROP COLUMN sigla_param;

ALTER TABLE ger_empresa_param
DROP COLUMN valor_tx;

ALTER TABLE ger_empresa_param
DROP COLUMN valor_dt;

ALTER TABLE ger_empresa_param
DROP COLUMN valor_nm;


ALTER TABLE ger_empresa_param 
ADD dt_valid_inicial VARCHAR(1);


comment on column ger_pessoa_conta_banco.active is 'aceita entrada: S-Sim, N-Não';
comment on column ger_itemserv_local.active is 'aceita entrada: S-Sim, N-Não';
comment on column ger_itemserv_pessoa.active is 'aceita entrada: S-Sim, N-Não';

--Fin

ALTER TABLE fin_pagrec_tipo
ADD sigla_fin_pagrec_tipo VARCHAR(100);

ALTER TABLE fin_recibo_tipo
ADD sigla_fin_recibo_tipo VARCHAR(100);

ALTER TABLE fin_tipo_variacao
ADD sigla_fin_tipo_variacao VARCHAR(100);

ALTER TABLE fin_doc_tipo
ADD sigla_fin_doc_tipo VARCHAR(100);

ALTER TABLE fin_lote
ADD sigla_fin_doc_tipo VARCHAR(100);

ALTER TABLE fin_doc_tipo
DROP COLUMN nr_doc;

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
