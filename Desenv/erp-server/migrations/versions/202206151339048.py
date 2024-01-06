from alembic import op


revision = "202206151339048"
down_revision = "202206151339047"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
COMMENT ON COLUMN fin_recibo_tipo.padrao IS 'Padrão: S-Sim, N-Não';
COMMENT ON COLUMN fin_class_agrup.padrao IS 'Padrão: S-Sim, N-Não';
COMMENT ON COLUMN crm_mov.envia_email_ext IS 'Envia Email Externo: S-Sim, N-Não';
COMMENT ON COLUMN ger_empresa.fis_incent_fiscal_nfs IS 'Possue incentivo fiscal da NFS: S-Sim, N-Não';
COMMENT ON COLUMN ind.ind_id_ponderacao IS 'ID do Indicador para Ponderação: S-Sim, N-Não';
COMMENT ON COLUMN ind.acumular_ano IS 'Acumular Valores na Ano:  S-Sim, N-Não';
COMMENT ON COLUMN ind.acumular_semestre IS 'Acumular Valores na Semestre: S-Sim, N-Não';
COMMENT ON COLUMN ind.acumular_quadrimestre IS 'Acumular Valores na Quadrimestre: S-Sim, N-Não';
COMMENT ON COLUMN ind.acumular_trimestre IS 'Acumular Valores na Trimestre: S-Sim, N-Não';
COMMENT ON COLUMN ind.acumular_bimestre IS 'Acumular Valores na Bimestre: S-Sim, N-Não';
COMMENT ON COLUMN ind.acumular_mes IS 'Acumular Valores na Mês: S-Sim, N-Não';
COMMENT ON COLUMN ind.acumular_quinzena IS 'Acumular Valores na Quinzena: S-Sim, N-Não';
COMMENT ON COLUMN ind.acumular_semana IS 'Acumular Valores na Semana: S-Sim, N-Não';
COMMENT ON COLUMN ind.exibir_ano IS 'Exibir Ano: S-Sim, N-Não';
COMMENT ON COLUMN ind.exibir_semestre IS 'Exibir Semestre: S-Sim, N-Não';
COMMENT ON COLUMN ind.exibir_quadrimestre IS 'Exibir Quadrimestre: S-Sim, N-Não';
COMMENT ON COLUMN ind.exibir_trimestre IS 'Exibir Trimestre: S-Sim, N-Não';
COMMENT ON COLUMN ind.exibir_bimestre IS 'Exibir Bimestre: S-Sim, N-Não';
COMMENT ON COLUMN ind.exibir_mes IS 'Exibir Mês: S-Sim, N-Não';
COMMENT ON COLUMN ind.exibir_quinzena IS 'Exibir Quinzena: S-Sim, N-Não';
COMMENT ON COLUMN ind.exibir_semana IS 'Exibir Semana: S-Sim, N-Não';
COMMENT ON COLUMN ind.exibir_media_meta IS 'Exibir Media do Valor Meta: S-Sim, N-Não';
COMMENT ON COLUMN ind.exibir_media_real IS 'Exibir Media do Valor Real: S-Sim, N-Não';
COMMENT ON COLUMN ind.exibir_dia IS 'Exibir Dia: S-Sim, N-Não';
COMMENT ON COLUMN sys_user.email_verified IS 'Codigo do provider autenticado: S-Sim, N-Não';

---------- TYPE


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('17ebdb3b-e17a-478a-8c48-9387db5c990f','ope_centro_versao','admin','tipo_per','D','Diário');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('65841532-0864-4cc8-a602-33286462252c','ope_centro_versao','admin','tipo_per','M','Mensal');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('dafba307-4f35-4c88-908b-e78643d4c591','ope_centro_versao','admin','tipo_per','A','Anual');



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
