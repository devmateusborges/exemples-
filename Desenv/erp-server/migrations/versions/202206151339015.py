from alembic import op
import sqlalchemy as sa

revision = '202206151339015'
down_revision = '202206151339014'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""



comment on column crm_aviso.ativo IS 'Ativo: S-Sim, N-Não';
comment on column bor_dispositivo.ativo IS 'Ativo: S-Sim, N-Não';
comment on column crm_chat_grupo.ativo IS 'Ativo: S-Sim, N-Não';
comment on column crm_chat_msg.ativo IS 'Ativo: S-Sim, N-Não';
comment on column crm_class.ativo IS 'Ativo: S-Sim, N-Não';
comment on column crm_class_grupo.ativo IS 'Ativo: S-Sim, N-Não';
comment on column crm_class_subgrupo.ativo IS 'Ativo: S-Sim, N-Não';
comment on column crm_etapa.ativo IS 'Ativo: S-Sim, N-Não';
comment on column crm_org.ativo IS 'Ativo: S-Sim, N-Não';
comment on column crm_prioridade.ativo IS 'Ativo: S-Sim, N-Não';
comment on column crm_resposta.ativo IS 'Ativo: S-Sim, N-Não';
comment on column crm_status.ativo IS 'Ativo: S-Sim, N-Não';
comment on column crm_tag.ativo IS 'Ativo: S-Sim, N-Não';
comment on column ctb_centro.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ctb_centro_grupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ctb_comp.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ctb_comp_grupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ctb_conta.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ctb_conta_grupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ctb_conta_versao.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ctb_historico.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ctb_lote.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ctb_tipo_saldo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ctb_versao.ativo IS 'Ativo: S-Sim, N-Não';

Comment on column fin_banco.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fin_class.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fin_class_agrup.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fin_class_grupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fin_cond_pagrec.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fin_doc_tipo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fin_pagrec_tipo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fin_pagrec_versao.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fin_recibo_tipo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fin_tipo_variacao.ativo IS 'Ativo: S-Sim, N-Não';

Comment on column fis_nbs.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fis_ncm.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fis_obs.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column fis_tributo.ativo IS 'Ativo: S-Sim, N-Não';

Comment on column ger_cidade.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_device.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_empresa.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_empresa_grupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_est_nivel.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_index.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_itemserv.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_itemserv_barra.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_itemserv_compos.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_itemserv_compos_tipo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_itemserv_grupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_itemserv_local.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_itemserv_lote.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_itemserv_pessoa.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_itemserv_subgrupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_itemserv_var.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_marca.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_marca_modelo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_numeracao.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_pais.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_pessoa.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_pessoa_conta_banco.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_pessoa_endereco.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_uf.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_umedida.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_umedida_conv.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_marca_modelo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_numeracao.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_pais.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_pessoa.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_pessoa_conta_banco.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_pessoa_endereco.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ger_uf.ativo IS 'Ativo: S-Sim, N-Não';


Comment on column ind_cjd.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ind_cnd.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ind_ftd.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ind_grupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ind_prm.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ind_rel.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ind_subgrupo.ativo IS 'Ativo: S-Sim, N-Não';

Comment on column mov_operacao.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column mov_status.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column mov_tipo.ativo IS 'Ativo: S-Sim, N-Não';

Comment on column ope_atividade.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_atividade_grupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_atividade_sistema.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_centro1.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_centro2.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_centro2_area.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_centro2_ord_status.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_centro2_ord_tipo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_centro_config.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_centro_grupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_centro_rat_tipo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_centro_rend.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_centro_subgrupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_centro_versao.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_compart.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_compart_grupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_compart_itemserv.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_compart_medida.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_compart_ocor.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_compart_posicao.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_compart_status.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_compart_subgrupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_compart_tipo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_espac.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_estagio.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_frente_trabalho.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_ocor.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_ocor_grupo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_ocor_status.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_ocor_tipo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_periodo.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_regiao.ativo IS 'Ativo: S-Sim, N-Não';
Comment on column ope_tipo_solo.ativo IS 'Ativo: S-Sim, N-Não';

Comment on column pto_medidor.ativo IS 'Ativo: S-Sim, N-Não';

Comment on column sys.active IS 'Ativo: S-Sim, N-Não';
Comment on column sys_document.active IS 'Ativo: S-Sim, N-Não';
Comment on column sys_document_category.active IS 'Ativo: S-Sim, N-Não';
Comment on column sys_group.active IS 'Ativo: S-Sim, N-Não';
Comment on column sys_licence.active IS 'Ativo: S-Sim, N-Não';
Comment on column sys_module.active IS 'Ativo: S-Sim, N-Não';
Comment on column sys_plan.active IS 'Ativo: S-Sim, N-Não';
Comment on column sys_program.active IS 'Ativo: S-Sim, N-Não';
Comment on column sys_restriction.active IS 'Ativo: S-Sim, N-Não';
Comment on column sys_unit.active IS 'Ativo: S-Sim, N-Não';
Comment on column sys_user.active IS 'Ativo: S-Sim, N-Não';

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
