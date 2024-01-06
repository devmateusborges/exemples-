from alembic import op


revision = "202211301615006"
down_revision = "202211301615005"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
ALTER TABLE cms_post RENAME COLUMN util_blob TO util_blog;

ALTER TABLE cms_grupo add COLUMN color varchar(100);
ALTER TABLE cms_tag add  COLUMN color varchar(100);
COMMENT ON COLUMN cms_grupo.color IS 'Cor';
COMMENT ON COLUMN cms_tag.color IS 'Cor';


CREATE TABLE cms_post_grupo (
	id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
	cms_post_id varchar(36) NOT NULL,
    cms_grupo_id varchar(36) not null,
	log_user_ins varchar(100) NULL,
	log_date_ins timestamp(0) NULL DEFAULT now(),
	log_user_upd varchar(100) NULL,
	log_date_upd timestamp(0) NULL,
	CONSTRAINT pk_cms_post_grupo PRIMARY KEY (id),
	CONSTRAINT fk_cms_post_grupo_cms_post_id FOREIGN KEY (cms_post_id) REFERENCES public.cms_post(id) ON DELETE cascade,
	CONSTRAINT fk_cms_post_grupo_cms_grupo_id FOREIGN KEY (cms_grupo_id) REFERENCES public.cms_grupo(id) ON DELETE CASCADE
);

COMMENT ON COLUMN cms_post_grupo.id IS 'ID cms_post_grupo';
COMMENT ON COLUMN cms_post_grupo.cms_post_id IS 'ID do cms_post ';
COMMENT ON COLUMN cms_post_grupo.cms_grupo_id IS 'ID do cms_grupo';
COMMENT ON COLUMN cms_post_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN cms_post_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN cms_post_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN cms_post_grupo.log_date_upd IS 'Log - Data de Alteração';




CREATE TABLE cms_post_tag (
	id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
	cms_post_id varchar(36) NOT NULL,
	cms_tag_id varchar(36) not null,
	log_user_ins varchar(100) NULL,
	log_date_ins timestamp(0) NULL DEFAULT now(),
	log_user_upd varchar(100) NULL,
	log_date_upd timestamp(0) NULL,
	CONSTRAINT pk_cms_post_tag PRIMARY KEY (id),
	CONSTRAINT fk_cms_post_tag_cms_post_id FOREIGN KEY (cms_post_id) REFERENCES public.cms_post(id) ON DELETE cascade,
    CONSTRAINT fk_cms_post_grupo_cms_tag_id FOREIGN KEY (cms_tag_id) REFERENCES public.cms_tag(id) ON DELETE CASCADE
);

COMMENT ON COLUMN cms_post_tag.id IS 'ID cms_post_tag';
COMMENT ON COLUMN cms_post_tag.cms_post_id IS 'ID do cms_post';
COMMENT ON COLUMN cms_post_tag.cms_tag_id IS 'ID do cms_tag';
COMMENT ON COLUMN cms_post_tag.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN cms_post_tag.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN cms_post_tag.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN cms_post_tag.log_date_upd IS 'Log - Data de Alteração';


ALTER TABLE public.cms_post ALTER COLUMN corpo TYPE text USING corpo::text;
ALTER TABLE public.cms_post ADD img_url text NULL;


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
