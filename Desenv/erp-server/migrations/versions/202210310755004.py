from alembic import op


revision = "202210310755004"
down_revision = "202210310755003"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """

alter table ger_pessoa drop column contrib_icms;
alter table ger_pessoa add column contrib_icms integer;
COMMENT ON COLUMN ger_pessoa.contrib_icms IS 'Tipo de Contribuinte ICMS';
alter table sys_notification_log alter column checked type varchar(1);
alter table ctb_tipo_saldo alter column mes_ini_fechamento type integer;
alter table ctb_tipo_saldo alter column mes_fin_fechamento type integer;
alter table sys_module alter column order_visual type integer;
alter table crm_status_prox alter column ordem type integer;
alter table crm_etapa_prox alter column ordem type integer;
alter table ope_compart_posicao alter column numero_eixo type integer;
--====================================================================
CREATE TABLE sys_dic (
  id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
  name varchar(250)  NOT NULL,
	name_item varchar(250)  NOT NULL,
	type_dic varchar(2)  NOT NULL,
  description varchar(500)  NOT NULL,
  description_help  varchar(500)  NOT NULL,
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  CONSTRAINT pk_sys_dic PRIMARY KEY (id)
);
COMMENT ON TABLE sys_dic IS 'System-Dicionário';
COMMENT ON COLUMN sys_dic.id IS 'ID do Dicionario';
COMMENT ON COLUMN sys_dic.name IS 'Nome';
COMMENT ON COLUMN sys_dic.name_item IS 'Nome do Item';
COMMENT ON COLUMN sys_dic.type_dic IS 'Tipo do Dicionario: 10-Tabela;11-Coluna;12-Grid,13-Ação;14-Função;15-View';
COMMENT ON COLUMN sys_dic.description IS 'Descrição';
COMMENT ON COLUMN sys_dic.description_help IS 'Descrição do Help';
COMMENT ON COLUMN sys_dic.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_dic.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_dic.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_dic.log_date_upd IS 'Log - Data de Alteração';
--====================================================================

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
--actions
delete from sys_group_program_action a where sys_group_id in('4218d8f1-8595-4052-aace-ba36f772623e','0256e515-51a4-49a2-a8b8-adc36470cd51');
--actions - interno
insert into sys_group_program_action(id,sys_group_id,sys_program_action_id)
select uuid_generate_v4(),'4218d8f1-8595-4052-aace-ba36f772623e', c.id
from sys_program b 
join sys_program_action c on(b.id = c.sys_program_id);
commit;
--actions - unit
insert into sys_group_program_action(id,sys_group_id,sys_program_action_id)
select uuid_generate_v4(),'0256e515-51a4-49a2-a8b8-adc36470cd51', c.id
from sys_program b 
join sys_program_action c on(b.id = c.sys_program_id) where b.admin='N';
commit;
"""
    )


def downgrade():
    pass
