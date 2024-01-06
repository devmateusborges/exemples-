from alembic import op
import sqlalchemy as sa

revision = '202206151339031'
down_revision = '202206151339030'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
 
ALTER TABLE ger_empresa_param DROP CONSTRAINT fk_ger_empresa_param_ger_empresa_id;
ALTER TABLE ger_empresa_param ADD CONSTRAINT fk_ger_empresa_param_ger_empresa_id FOREIGN KEY (ger_empresa_id) REFERENCES ger_empresa(id) ON DELETE CASCADE;
ALTER TABLE ger_empresa_pessoa DROP CONSTRAINT fk_ger_empresa_pessoa_ger_empresa_id;
ALTER TABLE ger_empresa_pessoa ADD CONSTRAINT fk_ger_empresa_pessoa_ger_empresa_id FOREIGN KEY (ger_empresa_id) REFERENCES ger_empresa(id) ON DELETE CASCADE;
ALTER TABLE ger_itemserv_subgrupo DROP CONSTRAINT fk_ger_itemserv_subgrupo_ger_itemserv_grupo_id;
ALTER TABLE ger_itemserv_subgrupo ADD CONSTRAINT fk_ger_itemserv_subgrupo_ger_itemserv_grupo_id FOREIGN KEY (ger_itemserv_grupo_id) REFERENCES ger_itemserv_grupo(id) ON DELETE CASCADE;
ALTER TABLE ger_itemserv_barra DROP CONSTRAINT fk_ger_itemserv_barra_ger_itemserv_id;
ALTER TABLE ger_itemserv_barra ADD CONSTRAINT fk_ger_itemserv_barra_ger_itemserv_id FOREIGN KEY (ger_itemserv_id) REFERENCES ger_itemserv(id) ON DELETE CASCADE;
ALTER TABLE ger_itemserv_local DROP CONSTRAINT fk_ger_itemserv_local_ger_itemserv_id;
ALTER TABLE ger_itemserv_local ADD CONSTRAINT fk_ger_itemserv_local_ger_itemserv_id FOREIGN KEY (ger_itemserv_id) REFERENCES ger_itemserv(id) ON DELETE CASCADE;
ALTER TABLE ger_itemserv_pessoa DROP CONSTRAINT fk_geritemserv_pessoa_ger_itemserv_id;
ALTER TABLE ger_itemserv_pessoa ADD CONSTRAINT fk_geritemserv_pessoa_ger_itemserv_id FOREIGN KEY (ger_itemserv_id) REFERENCES ger_itemserv(id) ON DELETE CASCADE;
ALTER TABLE ger_uf DROP CONSTRAINT fk_ger_uf_ger_pais_id;
ALTER TABLE ger_uf ADD CONSTRAINT fk_ger_uf_ger_pais_id FOREIGN KEY (ger_pais_id) REFERENCES ger_pais(id) ON DELETE CASCADE;
ALTER TABLE ger_pessoa_conta_banco DROP CONSTRAINT fk_ger_pessoa_conta_banco_ger_pessoa_id;
ALTER TABLE ger_pessoa_conta_banco ADD CONSTRAINT fk_ger_pessoa_conta_banco_ger_pessoa_id FOREIGN KEY (ger_pessoa_id) REFERENCES ger_pessoa(id) ON DELETE CASCADE;
ALTER TABLE ger_pessoa_endereco DROP CONSTRAINT fk_ger_pessoa_endereco_ger_pessoa_id;
ALTER TABLE ger_pessoa_endereco ADD CONSTRAINT fk_ger_pessoa_endereco_ger_pessoa_id FOREIGN KEY (ger_pessoa_id) REFERENCES ger_pessoa(id) ON DELETE CASCADE;
ALTER TABLE ger_processo_bloq_user DROP CONSTRAINT fk_ger_processo_bloq_user_ger_processo_bloq_id;
ALTER TABLE ger_processo_bloq_user ADD CONSTRAINT fk_ger_processo_bloq_user_ger_processo_bloq_id FOREIGN KEY (ger_processo_bloq_id) REFERENCES ger_processo_bloq(id) ON DELETE CASCADE;
ALTER TABLE ger_umedida_conv DROP CONSTRAINT fk_ger_umedida_conv_ger_umedida_id_de;
ALTER TABLE ger_umedida_conv ADD CONSTRAINT fk_ger_umedida_conv_ger_umedida_id_de FOREIGN KEY (ger_umedida_id_de) REFERENCES ger_umedida(id) ON DELETE CASCADE;
ALTER TABLE ger_device_param ALTER COLUMN ger_device_id DROP NOT NULL;
ALTER TABLE crm_status_prox DROP CONSTRAINT fk_crm_status_prox_crm_status_id;
ALTER TABLE crm_status_prox ADD CONSTRAINT fk_crm_status_prox_crm_status_id FOREIGN KEY (crm_status_id) REFERENCES crm_status(id) ON DELETE CASCADE;
ALTER TABLE crm_class_subgrupo DROP CONSTRAINT fk_crm_class_subgrupo_crm_class_grupo_id;
ALTER TABLE crm_class_subgrupo ADD CONSTRAINT fk_crm_class_subgrupo_crm_class_grupo_id FOREIGN KEY (crm_class_grupo_id) REFERENCES crm_class_grupo(id) ON DELETE CASCADE;
ALTER TABLE crm_status_prox ALTER COLUMN crm_status_id DROP NOT NULL;
ALTER TABLE fin_pagrec_parc DROP CONSTRAINT fk_fin_pagrec_parc_fin_pagrec_id;
ALTER TABLE fin_pagrec_parc ADD CONSTRAINT fk_fin_pagrec_parc_fin_pagrec_id FOREIGN KEY (fin_pagrec_id) REFERENCES fin_pagrec(id) ON DELETE CASCADE;
ALTER TABLE fin_pagrec_parc_var DROP CONSTRAINT fk_fin_pagrec_parc_var_fin_pagrec_parc_id;
ALTER TABLE fin_pagrec_parc_var ADD CONSTRAINT fk_fin_pagrec_parc_var_fin_pagrec_parc_id FOREIGN KEY (fin_pagrec_parc_id) REFERENCES fin_pagrec_parc(id) ON DELETE CASCADE;
ALTER TABLE fin_pagrec_baixa_var DROP CONSTRAINT fk_fin_pagrec_baixa_var_fin_pagrec_baixa_id;
ALTER TABLE fin_pagrec_baixa_var ADD CONSTRAINT fk_fin_pagrec_baixa_var_fin_pagrec_baixa_id FOREIGN KEY (fin_pagrec_baixa_id) REFERENCES fin_pagrec_baixa(id) ON DELETE CASCADE;
ALTER TABLE fin_class_agrup_grupo DROP CONSTRAINT fk_fin_class_agrup_grupo_fin_class_agrup;
ALTER TABLE fin_class_agrup_grupo ADD CONSTRAINT fk_fin_class_agrup_grupo_fin_class_agrup FOREIGN KEY (fin_class_agrup_id) REFERENCES fin_class_agrup(id) ON DELETE CASCADE;
ALTER TABLE fis_doc_evento DROP CONSTRAINT fk_fis_doc_evento_fis_doc_id;
ALTER TABLE fis_doc_evento ADD CONSTRAINT fk_fis_doc_evento_fis_doc_id FOREIGN KEY (fis_doc_id) REFERENCES fis_doc(id) ON DELETE CASCADE;
ALTER TABLE fis_cest_ncm DROP CONSTRAINT fk_fis_cest_ncm_fis_cest_id;
ALTER TABLE fis_cest_ncm ADD CONSTRAINT fk_fis_cest_ncm_fis_cest_id FOREIGN KEY (fis_cest_id) REFERENCES fis_cest(id) ON DELETE CASCADE;
ALTER TABLE mov_entrega_doc DROP CONSTRAINT fk_mov_entrega_doc_mov_entrega_id;
ALTER TABLE mov_entrega_doc ADD CONSTRAINT fk_mov_entrega_doc_mov_entrega_id FOREIGN KEY (mov_entrega_id) REFERENCES mov_entrega(id) ON DELETE CASCADE;
ALTER TABLE mov_operacao_status DROP CONSTRAINT fk_mov_operacao_status_mov_operacao_id;
ALTER TABLE mov_operacao_status ADD CONSTRAINT fk_mov_operacao_status_mov_operacao_id FOREIGN KEY (mov_operacao_id) REFERENCES mov_operacao(id) ON DELETE CASCADE;
ALTER TABLE ope_centro2_ord_ativ DROP CONSTRAINT fk_ope_centro2_ord_ativ_ope_centro2_ord_id;
ALTER TABLE ope_centro2_ord_ativ ADD CONSTRAINT fk_ope_centro2_ord_ativ_ope_centro2_ord_id FOREIGN KEY (ope_centro2_ord_id) REFERENCES ope_centro2_ord(id) ON DELETE CASCADE;
ALTER TABLE ope_centro2_ord_dest DROP CONSTRAINT fk_ope_centro2_ord_dest_ope_centro2_ord_id;
ALTER TABLE ope_centro2_ord_dest ADD CONSTRAINT fk_ope_centro2_ord_dest_ope_centro2_ord_id FOREIGN KEY (ope_centro2_ord_id) REFERENCES ope_centro2_ord(id) ON DELETE CASCADE;
ALTER TABLE ope_ocor_compart_mov_det DROP CONSTRAINT fk_ope_ocor_compart_mov_det_ope_compart_mov_id;
ALTER TABLE ope_ocor_compart_mov_det ADD CONSTRAINT fk_ope_ocor_compart_mov_det_ope_compart_mov_id FOREIGN KEY (ope_compart_mov_id) REFERENCES ope_ocor_compart_mov(id) ON DELETE CASCADE;
ALTER TABLE ope_centro_rat_periodo DROP CONSTRAINT fk_ope_centro_rat_periodo_ope_centro_rat_tipo_id;
ALTER TABLE ope_centro_rat_periodo ADD CONSTRAINT fk_ope_centro_rat_periodo_ope_centro_rat_tipo_id FOREIGN KEY (ope_centro_rat_tipo_id) REFERENCES ope_centro_rat_tipo(id) ON DELETE CASCADE;
ALTER TABLE ope_centro_rat_fator DROP CONSTRAINT fk_ope_centro2_rat_fator_ope_centro_rat_periodo_id;
ALTER TABLE ope_centro_rat_fator ADD CONSTRAINT fk_ope_centro2_rat_fator_ope_centro_rat_periodo_id FOREIGN KEY (ope_centro_rat_periodo_id) REFERENCES ope_centro_rat_periodo(id) ON DELETE CASCADE;
ALTER TABLE sys_group_program DROP CONSTRAINT fk_sys_group_program_sys_group_id;
ALTER TABLE sys_group_program ADD CONSTRAINT fk_sys_group_program_sys_group_id FOREIGN KEY (sys_group_id) REFERENCES sys_group(id) ON DELETE CASCADE;
ALTER TABLE sys_user_program RENAME CONSTRAINT fk_sys_user_program_system_user_id TO fk_sys_user_program_sys_user_id;
ALTER TABLE crm_class DROP CONSTRAINT fk_crm_class_crm_class_subgrupo_id;
ALTER TABLE crm_class ADD CONSTRAINT fk_crm_class_crm_class_subgrupo_id FOREIGN KEY (crm_class_subgrupo_id) REFERENCES crm_class_subgrupo(id) ON DELETE CASCADE;
ALTER TABLE crm_mov DROP CONSTRAINT fk_crm_mov_crm_status_id;
ALTER TABLE crm_mov ADD CONSTRAINT fk_crm_mov_crm_status_id FOREIGN KEY (crm_status_id) REFERENCES crm_status(id) ON DELETE CASCADE;



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
