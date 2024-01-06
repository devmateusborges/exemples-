from alembic import op


revision = "202206151339047"
down_revision = "202206151339046"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
	CREATE TABLE sys_translate_lang (
  id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
  code varchar(50) ,
  name varchar(100) ,
  active varchar(1) ,
  default_lang varchar(1) ,
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  CONSTRAINT pk_sys_translate_lang PRIMARY KEY (id)
);


COMMENT ON COLUMN sys_translate_lang.id IS 'ID da Liguagem de Tradução';
COMMENT ON COLUMN sys_translate_lang.code IS 'Código da Liguagem de Tradução';
COMMENT ON COLUMN sys_translate_lang.name IS 'Nome';
COMMENT ON COLUMN sys_translate_lang.active IS 'Ativo: S-Sim, N-Não';
COMMENT ON COLUMN sys_translate_lang.default_lang IS 'Padrão: S-Sim, N-Não';
COMMENT ON COLUMN sys_translate_lang.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_translate_lang.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_translate_lang.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_translate_lang.log_date_upd IS 'Log - Data de Alteração';

insert into sys_translate_lang(code,name,active, default_lang) values('pt-BR','Português','S','S');
insert into sys_translate_lang(code,name,active, default_lang) values('en-US','English','S','N');
insert into sys_translate_lang(code,name,active, default_lang) values('es','Español','S','N');

CREATE TABLE sys_translate (
  id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
  sys_translate_lang_id varchar(36) ,
  term_group varchar(50) ,
  term_orig varchar(500) ,
  term_translate varchar(500),
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
	CONSTRAINT pk_sys_translate PRIMARY KEY (id),
	CONSTRAINT idx_unq_sys_translate UNIQUE (sys_translate_lang_id,term_group,term_orig) WITH (fillfactor=90),
	CONSTRAINT fk_sys_translate_sys_translate_lang_id FOREIGN KEY (sys_translate_lang_id) REFERENCES sys_translate_lang (id) ON DELETE NO ACTION ON UPDATE NO ACTION
);


COMMENT ON TABLE sys_translate IS 'System-Liguagem de Tradução';
COMMENT ON COLUMN sys_translate.sys_translate_lang_id IS 'ID da Liguagem de Tradução';
COMMENT ON COLUMN sys_translate.term_group IS 'Grupo de termo';
COMMENT ON COLUMN sys_translate.term_orig IS 'Termo origem';
COMMENT ON COLUMN sys_translate.term_translate IS 'Termo traduzido';
COMMENT ON COLUMN sys_translate.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_translate.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_translate.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_translate.log_date_upd IS 'Log - Data de Alteração';
  
alter table sys_user add sys_tran_lang_id_default varchar(36);
alter table sys_user add gtm_default varchar(50);
alter table sys_user add CONSTRAINT fk_sys_user_sys_tran_lang_id_default FOREIGN KEY (sys_tran_lang_id_default) REFERENCES sys_translate_lang (id) ON DELETE NO ACTION ON UPDATE NO ACTION;

alter table test1 drop column dt_nascimento;
alter table test1 add dt_nascimento Date;
alter table test1 add dthr_nascimento timestamp(6);
alter table test1 add hr_nascimento Date;
alter table test1 add radio varchar(50);
alter table test1 add cpfcnpj varchar(50);

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
