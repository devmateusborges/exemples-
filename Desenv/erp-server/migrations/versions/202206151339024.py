from alembic import op
import sqlalchemy as sa

revision = '202206151339024'
down_revision = '202206151339023'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""

ALTER TABLE crm_resposta RENAME COLUMN descritivo TO nome;

ALTER TABLE crm_tag RENAME COLUMN descritivo TO nome;

ALTER TABLE crm_aviso RENAME COLUMN descritivo TO nome;

DROP TABLE sys_change_log;

ALTER TABLE sys_user
DROP COLUMN frontpage_id;

alter table sys_document
add column cms_post_id varchar(36)
default NULL;

CREATE TABLE cms_post_hist (
    
    unit_id varchar(36) NOT NULL,
    id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
    data_hist timestamp(0),
    cms_post_id varchar(36) NOT NULL,
    descricao TEXT NOT NULL,
    tipo_hist varchar(1) NOT NULL,

    log_user_ins varchar(100),
    log_date_ins timestamp(0) DEFAULT now(),
    log_user_upd varchar(100),
    log_date_upd timestamp(0),
    CONSTRAINT pk_cms_post_hist PRIMARY KEY (id)
);


COMMENT ON COLUMN cms_post_hist.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN cms_post_hist.id IS 'ID do cms_post_hist ';
COMMENT ON COLUMN cms_post_hist.data_hist IS 'Data historico';
COMMENT ON COLUMN cms_post_hist.cms_post_id IS 'FK CMS ID';
COMMENT ON COLUMN cms_post_hist.descricao IS 'F-Fixo, V-Variável';
COMMENT ON COLUMN cms_post_hist.tipo_hist IS 'V-Visualização,A-Alteração,S-Status';

COMMENT ON COLUMN cms_post_hist.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN cms_post_hist.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN cms_post_hist.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN cms_post_hist.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE cms_post_hist OWNER TO postgres;


	
CREATE TABLE cms_post(
        
    unit_id varchar(36) NOT NULL,
    id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
    sys_user_id varchar(36) NOT NULL,
    titulo varchar(50) NOT NULL,
    corpo  varchar(50) NOT NULL,
    status varchar(1) NOT NULL,
    favorito varchar(1) NOT NULL,
    util_blob  varchar(1) NOT NULL,
    util_depoimento varchar(1) NOT NULL,
    util_treinamento varchar(1) NOT NULL,
    util_help varchar(1) NOT NULL,
    tipo_render varchar(1) NOT NULL,
    log_user_ins varchar(100),
    log_date_ins timestamp(0) DEFAULT now(),
    log_user_upd varchar(100),
    log_date_upd timestamp(0),
    CONSTRAINT pk_cms_post PRIMARY KEY (id)

);


COMMENT ON COLUMN cms_post.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN cms_post.id IS 'ID do cms_post ';
COMMENT ON COLUMN cms_post.sys_user_id IS 'ID User';
COMMENT ON COLUMN cms_post.titulo IS 'Titulo';
COMMENT ON COLUMN cms_post.corpo IS 'Corpo';
COMMENT ON COLUMN cms_post.status IS 'C-Criação,P-Publicado,D-Desativado';
COMMENT ON COLUMN cms_post.favorito IS 'favorito: S-Sim, N-Não';
COMMENT ON COLUMN cms_post.util_blob IS 'Blog: S-Sim, N-Não';
COMMENT ON COLUMN cms_post.util_depoimento IS 'Depoimento: S-Sim, N-Não';
COMMENT ON COLUMN cms_post.util_treinamento IS 'Treinamento: S-Sim, N-Não';
COMMENT ON COLUMN cms_post.util_help IS 'Help: S-Sim, N-Não';
COMMENT ON COLUMN cms_post.tipo_render IS 'Tipo Render: M-Markdown,H-Html';

COMMENT ON COLUMN cms_post.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN cms_post.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN cms_post.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN cms_post.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE cms_post OWNER TO postgres;



CREATE TABLE cms_grupo (
        
    unit_id varchar(36) NOT NULL,
    id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
    nome varchar(50) NOT NULL,
    ativo varchar(1) NOT NULL,
    sigla_grupo varchar(50) NOT NULL,
    publico varchar(1) NOT NULL,
    log_user_ins varchar(100),
    log_date_ins timestamp(0) DEFAULT now(),
    log_user_upd varchar(100),
    log_date_upd timestamp(0),
    CONSTRAINT pk_cms_grupo PRIMARY KEY (id)
	
);

COMMENT ON COLUMN cms_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN cms_grupo.id IS 'ID do cms_grupo ';
COMMENT ON COLUMN cms_grupo.nome IS 'Nome';
COMMENT ON COLUMN cms_grupo.ativo IS 'Ativo: S-Sim, N-Não';
COMMENT ON COLUMN cms_grupo.sigla_grupo IS 'sigla_grupo';
COMMENT ON COLUMN cms_grupo.publico IS 'Publico: S-Sim, N-Não';
COMMENT ON COLUMN cms_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN cms_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN cms_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN cms_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE cms_grupo OWNER TO postgres;

CREATE TABLE cms_tag (
        
    unit_id varchar(36) NOT NULL,
    id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
    nome varchar(50) NOT NULL,
    ativo varchar(1) NOT NULL,
    sigla_tag varchar(50) NOT NULL,
    log_user_ins varchar(100),
    log_date_ins timestamp(0) DEFAULT now(),
    log_user_upd varchar(100),
    log_date_upd timestamp(0),
    CONSTRAINT pk_cms_tag PRIMARY KEY (id)
);

COMMENT ON COLUMN cms_tag.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN cms_tag.id IS 'ID do cms_tag ';
COMMENT ON COLUMN cms_tag.nome IS 'Nome';
COMMENT ON COLUMN cms_tag.ativo IS 'Ativo: S-Sim, N-Não';
COMMENT ON COLUMN cms_tag.sigla_tag IS 'sigla_tag';
COMMENT ON COLUMN cms_tag.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN cms_tag.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN cms_tag.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN cms_tag.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE cms_tag OWNER TO postgres;



CREATE TABLE sys_user_cms_grupo (
        
    id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
    sys_user_id varchar(36) NOT NULL,
    cms_grupo_id varchar(36) NOT NULL,
    log_user_ins varchar(100),
    log_date_ins timestamp(0) DEFAULT now(),
    log_user_upd varchar(100),
    log_date_upd timestamp(0),
    CONSTRAINT pk_sys_user_cms_grupo PRIMARY KEY (id)
);

 
COMMENT ON COLUMN sys_user_cms_grupo.id IS 'ID do sys_user_cms_grupo';
COMMENT ON COLUMN sys_user_cms_grupo.sys_user_id IS 'ID do user';
COMMENT ON COLUMN sys_user_cms_grupo.cms_grupo_id IS 'ID da Grupo ';

COMMENT ON COLUMN sys_user_cms_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_user_cms_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_user_cms_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_user_cms_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE sys_user_cms_grupo OWNER TO postgres;


	    ALTER TABLE sys_user_cms_grupo ADD CONSTRAINT fk_cms_sys_user_sys_user_id FOREIGN KEY (sys_user_id)
        REFERENCES sys_user (id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION;
		
		ALTER TABLE sys_user_cms_grupo ADD CONSTRAINT fk_cms_sys_user_cms_grupo_grupo_id FOREIGN KEY (cms_grupo_id)
        REFERENCES cms_grupo (id)
        ON DELETE CASCADE
        ON UPDATE NO ACTION;
		
		ALTER TABLE cms_tag ADD CONSTRAINT fk_cms_tag_sys_unit_id FOREIGN KEY (unit_id) REFERENCES sys_unit (id) 
		ON DELETE CASCADE ON UPDATE NO ACTION;
		
		ALTER TABLE cms_grupo ADD CONSTRAINT fk_cms_grupo_sys_unit_id FOREIGN KEY (unit_id) REFERENCES sys_unit (id) 
		ON DELETE CASCADE ON UPDATE NO ACTION;
		
		ALTER TABLE cms_post ADD CONSTRAINT fk_cms_post_sys_user_id FOREIGN KEY (sys_user_id) 
		REFERENCES sys_user (id) 
		ON DELETE CASCADE ON UPDATE NO ACTION;
		ALTER TABLE cms_post ADD CONSTRAINT fk_cms_post_sys_unit_id FOREIGN KEY (unit_id) REFERENCES sys_unit (id) 
		ON DELETE CASCADE ON UPDATE NO ACTION;
		
		ALTER TABLE cms_post_hist ADD CONSTRAINT fk_cms_post_hist_sys_unit_id FOREIGN KEY (unit_id) REFERENCES sys_unit (id) 
		ON DELETE CASCADE ON UPDATE NO ACTION;
		ALTER TABLE cms_post_hist ADD CONSTRAINT fk_cms_post_hist_cms_post_id FOREIGN KEY (cms_post_id) REFERENCES cms_post (id) 
		ON DELETE CASCADE ON UPDATE NO ACTION;

        
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
