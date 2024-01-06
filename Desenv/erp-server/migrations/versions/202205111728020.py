from alembic import op
import sqlalchemy as sa

revision = '202205111728020'
down_revision = '202205111728019'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""

 
comment on column bor_msg.qualidade_posi is 'Qualida Da Posição OK-Boa,BAD-Ruim)';
comment on column fin_pagrec.tipo_es is 'Tipo: E-Entrada, S-Saída';
comment on column fin_pagrec_baixa.tipo is 'Tipo de Baixa: N-Normal, A-Agrupamento, E-Encontro';
comment on column fin_pagrec_prev.tipo_es is 'Tipo: E-Entrada, S-Saída';
comment on column fin_tipo_variacao.tipo is 'Tipo de Baixa: J-Juros, D-Descontos, A-Abatimento, M-Multa';
comment on column fis_doc.tipo_emissao is 'Tipo de Emissao (1 - Normal, 2 - SCAN, 9 - Off-Line)';
comment on column fis_doc_evento.tipo_evento is '1 - Autorizacao, 2 - Cancelamento, 3 - Inutilizacao, 4 - Carta de Correcao';
comment on column ger_itemserv.tipo is 'Tipo (I-Item, S-Serviço)';
comment on column ger_pessoa_endereco.padrao is 'Padrão (S-Sim, N-Não)';
comment on column ger_pessoa_endereco.tipo is 'Tipo (F-Fiscal, C-Cobrança, E-Entrega)';
comment on column ind.grafico_tipo_ind is 'Tipo de Gráfico para Indicador: 1-Coluna, 2-Pizza';
comment on column ind.grafico_tipo_atributo is 'Tipo de Grafico para Atributos: 1-Coluna, 2-Linha, 3-Area';
comment on column ind.tipo_acumulo is 'Tipo de Acumulo: 1-Manual, 2-Soma, 3-Média, 4-Media Ponderada, 5-Ultimo, 6-Maior, 7-Menor';
comment on column ind.totalizador_atributo is '1-Nenhum, 2-Soma, 3-Média';
comment on column mov.tipo_frete is 'Tipo de Frete (0 - Por conta do emitente, 1 - Por conta do destinatário/remetente, 2 - Por conta de terceiros, 9 - Sem frete)';
comment on column mov.tipo_emissao_carga is 'Tipo de Emissao da Carga (1 - Prestador de serviço de transporte, 2 - Transportador de Carga Própria)';
comment on column mov.tipo_umedida_carga is 'Tipo de Unidade Medida da Carga (01-KG, 02-TON)';
comment on column mov_status.tipo_status is 'Tipo do Status (F - Finalizado, P - Pendente, C - Cancelado, E-Erro)';
comment on column ope_centro2_equip.tipo_carroceria is 'Tipo do Carroceria (00 - Não Aplicável, 01 - Aberta, 02 - Fechada/Baú, 03 - Graneleira, 04 - Porta Container, 05 - Siber)';
comment on column ope_centro2_equip.tipo_rodado is 'Tipo do Rodado (00 - Não Aplicável, 01 - Truck, 02 - Toco, 03 - Cavalo Mecânico, 04 - Van, 05 - Utilitário, 06 - Outros)';
comment on column ope_centro2_equip.tipo_transp_auto_carga is 'Tipo Transp. Automo Carga 1-Agreg, 2-Indenp, 3-Outros';
comment on column ope_centro2_ord_status.tipo_status is 'Tipo do Status (L - Liquidada, F - Finalizado, P - Pendente, C - Cancelado, A-Andamento)';
comment on column sys_email_log.body_type is 'Tipo do Corpo: text,html';

--================================================================
--Liberar acesso para todos usuários
--================================================================
--admin interno
delete from sys_group_program a where system_group_id='4218d8f1-8595-4052-aace-ba36f772623e';
insert into sys_group_program(id,system_group_id,system_program_id)
select uuid_generate_v4(),'4218d8f1-8595-4052-aace-ba36f772623e', b.id
from sys_program b;
--admin unit
delete from sys_group_program a where system_group_id='0256e515-51a4-49a2-a8b8-adc36470cd51';
insert into sys_group_program(id,system_group_id,system_program_id)
select uuid_generate_v4(),'0256e515-51a4-49a2-a8b8-adc36470cd51', b.id
from sys_program b where b.admin='N';
commit;
               """)


def downgrade():
    pass
