from alembic import op


revision = "202210310755002"
down_revision = "202210310755001"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
COMMENT ON TABLE public.sys_migration IS 'Systema-Migração';
COMMENT ON COLUMN public.sys_migration.version_num IS 'Versão da Migação';
COMMENT ON COLUMN public.sys_user.gtm_default IS 'Predefinição Google Tag Manager';
COMMENT ON COLUMN public.sys_user.sys_tran_lang_id_default IS 'ID Predefinição Tadução de Idioma';
COMMENT ON TABLE public.cms_post IS 'Content Management System-Post';
COMMENT ON TABLE public.test1 IS 'test1-Teste 1';
COMMENT ON TABLE public.cms_post_hist IS 'Content Management System-Historico de Post';
COMMENT ON TABLE public.test1_child IS 'test1_child-Teste 1 Filho';
COMMENT ON TABLE public.test1_fk IS 'test1_fk-Teste 1 Chave Estrangeira';
COMMENT ON TABLE public.sys_translate_lang IS 'Systema-Traduzir idioma';
COMMENT ON TABLE public.sys_user_cms_grupo IS 'Systema-Content Management System-Grupo';
COMMENT ON TABLE public.cms_grupo IS 'Content Management System-Grupo';
COMMENT ON TABLE public.cms_tag IS 'Content Management System-Tag';
COMMENT ON COLUMN public.ger_empresa_param.dt_valid_inicial IS 'Data Validade inicial';
COMMENT ON COLUMN public.fin_doc_tipo.sigla_fin_doc_tipo IS 'Sigla - Tipo de documento';
COMMENT ON COLUMN public.ger_empresa_grupo.sigla_ger_empresa_grupo IS 'Sigla - Grupo da Empresa';
COMMENT ON COLUMN public.ger_itemserv_compos_tipo.sigla_ger_itemserv_compos_tipo IS 'Sigla - Tipo de Composição do Item/Serviço';
COMMENT ON COLUMN public.ger_est_nivel.sigla_ger_est_nivel IS 'Sigla - Nivel de Estoque';
COMMENT ON COLUMN public.ger_marca.sigla_ger_marca IS 'Sigla - Marca';
COMMENT ON COLUMN public.ger_itemserv_subgrupo.sigla_ger_itemserv_subgrupo IS 'Sigla - SubGrupo de Item/Serviço';
COMMENT ON COLUMN public.ger_itemserv_grupo.sigla_ger_itemserv_grupo IS 'Sigla - Grupo de Item/Serviço';
COMMENT ON COLUMN public.ger_numeracao.sigla_ger_numeracao IS 'Sigla - Númeração';
COMMENT ON COLUMN public.ger_marca_modelo.sigla_ger_marca_modelo IS 'Sigla - Marca x Modelo';
COMMENT ON COLUMN public.fis_doc_tipo.sigla_fis_doc_tipo IS 'Sigla - Tipo de Documento';
COMMENT ON COLUMN public.ger_itemserv_lote.ger_itemserv_id IS 'ID Geral Item/Serviço';
COMMENT ON COLUMN public.ope_centro_subtipo.sigla_centro_subtipo IS 'Sigla -';
COMMENT ON COLUMN public.fin_pagrec_tipo.sigla_fin_pagrec_tipo IS 'Silga - Tipo de Pag/Rec';
COMMENT ON COLUMN public.fin_tipo_variacao.sigla_fin_tipo_variacao IS 'Sigla - Tipo de Variação';
COMMENT ON COLUMN public.fin_lote.sigla_fin_lote IS 'Sigla - Lote';
COMMENT ON COLUMN public.fin_recibo_tipo.sigla_fin_recibo_tipo IS 'Sigla - Tipo de Recibo';
COMMENT ON COLUMN public.sys_access_log.sys_user_id IS 'ID Systema Úsuario';
COMMENT ON COLUMN public.sys_access_log.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN public.sys_access_log.sys_id IS 'ID do Systema';
COMMENT ON COLUMN public.sys_document.cms_post_id IS 'ID Sistema de Gerenciamento de Conteúdo-Post';
COMMENT ON COLUMN public.sys_group_program.id IS 'ID do Grupo de Acesso x Programa';
COMMENT ON COLUMN public.sys_group_program.sys_group_id IS 'ID Grupo de Systema';
COMMENT ON COLUMN public.sys_group_program.sys_program_id IS 'ID Programas  do Systema';
ALTER TABLE public.test1 ALTER COLUMN id DROP DEFAULT;
COMMENT ON COLUMN public.test1.id IS 'ID Teste 1';
ALTER TABLE public.test1 ALTER COLUMN log_date_ins DROP DEFAULT;
COMMENT ON COLUMN public.test1.log_date_ins IS 'Log - Usuário de Inserção';
ALTER TABLE public.test1 ALTER COLUMN log_date_upd DROP DEFAULT;
COMMENT ON COLUMN public.test1.log_date_upd IS 'Log - Data de Inserção';
ALTER TABLE public.test1 ALTER COLUMN log_user_ins DROP DEFAULT;
COMMENT ON COLUMN public.test1.log_user_ins IS 'Log - Usuário de Alteração';
ALTER TABLE public.test1 ALTER COLUMN log_user_upd DROP DEFAULT;
COMMENT ON COLUMN public.test1.log_user_upd IS 'Log - Data de Alteração';
ALTER TABLE public.test1 ALTER COLUMN codigo DROP DEFAULT;
COMMENT ON COLUMN public.test1.codigo IS 'Código Teste1';
ALTER TABLE public.test1 ALTER COLUMN descricao DROP DEFAULT;
COMMENT ON COLUMN public.test1.descricao IS 'Descrição';
ALTER TABLE public.test1 ALTER COLUMN test1_fk_id DROP DEFAULT;
COMMENT ON COLUMN public.test1.test1_fk_id IS 'ID do Test1_fk';
COMMENT ON COLUMN public.test1.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN public.test1.dt_nascimento IS 'Data de nacimento';
COMMENT ON COLUMN public.test1.dthr_nascimento IS 'Data e Hora do nacimento';
COMMENT ON COLUMN public.test1.hr_nascimento IS 'Hora do nacimento';
COMMENT ON COLUMN public.test1.radio IS 'Radio';
COMMENT ON COLUMN public.test1.cpfcnpj IS 'CPF ou CNPJ';
COMMENT ON COLUMN public.test1_child.id IS 'ID Teste 1 Filho';
COMMENT ON COLUMN public.test1_child.log_date_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN public.test1_child.log_date_upd IS 'Log - Data de Inserção';
COMMENT ON COLUMN public.test1_child.log_user_ins IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN public.test1_child.log_user_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN public.test1_child.codigo IS 'Código';
COMMENT ON COLUMN public.test1_child.quantidade IS 'Quantidade';
COMMENT ON COLUMN public.test1_child.valor_total IS 'Valor total';
COMMENT ON COLUMN public.test1_child.valor_unit IS 'Valor da unidade';
COMMENT ON COLUMN public.test1_child.test1_id IS 'ID do Test1';
COMMENT ON COLUMN public.test1_fk.id IS 'ID Log - Teste 1 Chave Estrangeira';
COMMENT ON COLUMN public.test1_fk.log_date_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN public.test1_fk.log_date_upd IS 'Log - Data de Inserção';
COMMENT ON COLUMN public.test1_fk.log_user_ins IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN public.test1_fk.log_user_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN public.test1_fk.codigo IS 'Código';
COMMENT ON COLUMN public.test1_fk.descricao IS 'Descrição';
COMMENT ON COLUMN public.test1_fk.tipo_test1 IS 'Tipo do test1';
COMMENT ON COLUMN public.sys_translate.id IS 'ID Liguagem de Tradução';

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
