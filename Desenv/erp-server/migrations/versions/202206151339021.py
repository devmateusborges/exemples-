from alembic import op
import sqlalchemy as sa

revision = "202206151339021"
down_revision = "202206151339020"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """

CREATE TABLE ger_per_tipo (
  unit_id varchar(36) NOT NULL,
  id varchar(36)      NOT NULL DEFAULT uuid_generate_v4(),
  nome varchar(50)    NOT NULL,
  ativo varchar(1)    NOT NULL,
  sigla_per_tipo varchar(50)  NOT NULL,
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  CONSTRAINT pk_ger_per_tipo PRIMARY KEY (id)
);

alter table ger_per_tipo add ini_semana varchar(1);
alter table ger_per add data_dia_final date;
alter table ger_per add data_quinzena_final date;
alter table ger_per add data_semana_final date;
alter table ger_per add data_mes_final date;
alter table ger_per add data_bimestre_final date;
alter table ger_per add data_trimestre_final date;
alter table ger_per add data_quadrimestre_final date;
alter table ger_per add data_semestre_final date;
alter table ger_per add data_ano_final date;

alter table ger_per add dia_numero int4;
alter table ger_per add quinzena_numero int4;
alter table ger_per add semana_numero int4;
alter table ger_per add mes_numero int4;
alter table ger_per add bimestre_numero int4;
alter table ger_per add trimestre_numero int4;
alter table ger_per add quadrimestre_numero int4;
alter table ger_per add semestre_numero int4;
alter table ger_per add ano_numero int4;

alter table ger_per add dia_tipo varchar(1);
alter table ger_per add quinzena_tipo varchar(1);
alter table ger_per add semana_tipo varchar(1);
alter table ger_per add mes_tipo varchar(1);
alter table ger_per add bimestre_tipo varchar(1);
alter table ger_per add trimestre_tipo varchar(1);
alter table ger_per add quadrimestre_tipo varchar(1);
alter table ger_per add semestre_tipo varchar(1);
alter table ger_per add ano_tipo varchar(1);


COMMENT ON COLUMN ger_per_tipo.ini_semana IS 'Inicio Dia Semana';


alter table sys_user_chat_grupo add log_date_ins timestamp(0);
alter table sys_user_chat_grupo add log_date_upd timestamp(0);

alter table sys_user_chat_grupo add log_user_ins varchar(100);
alter table sys_user_chat_grupo add log_user_upd varchar(100);

COMMENT ON COLUMN sys_user_chat_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_user_chat_grupo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN sys_user_chat_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_user_chat_grupo.log_user_upd IS 'Log - Usuário de Alteração';

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
               """
    )


def downgrade():
    pass
