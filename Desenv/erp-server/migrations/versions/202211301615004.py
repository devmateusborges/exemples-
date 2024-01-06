from alembic import op


revision = "202211301615004"
down_revision = "202211301615003"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
update ind_rel set ind_cjd_id=null where id='c9b0c767-55de-4eaf-af26-14c76c731547';
update ind_prm set tipo_entrada='CF', busca_campo_id='id' where id='984b7aaf-dd3f-4a5f-856c-521d1dec0815';
update ind_prm set tipo_entrada='CF' where busca_campo_nome <> '';
update ind_prm set obrigatorio='N' where obrigatorio is null;
update ind_prm set visivel='S' where visivel is null;
update ind_prm set tipo_entrada='CS' where busca_valores <> '';

COMMENT ON COLUMN ind_prm.tipo_entrada IS 'Tipo Entrada: IS-Input Simple, CS-Combo Simple, CF-Combo Field/Table, SP-Separador, VL-Variável, CT-Combo Types/Description, CD-Combo Fonte Dados';

alter table ind_prm add ind_ftd_id varchar(36);
alter table ind_prm add CONSTRAINT fk_ind_prm_ind_ftd FOREIGN KEY (ind_ftd_id) REFERENCES ind_ftd (id) ON DELETE NO ACTION ON UPDATE NO ACTION;

alter table ind_vr_ano add atributo1 varchar(100) null;
alter table ind_vr_ano add atributo2 varchar(100) null;
alter table ind_vr_ano add atributo3 varchar(100) null;
alter table ind_vr_ano add atributo4 varchar(100) null;
alter table ind_vr_ano add atributo5 varchar(100) null;
alter table ind_vr_ano add atributo_nivel int4;


alter table ind_vr_meta add atributo1 varchar(100) null;
alter table ind_vr_meta add atributo2 varchar(100) null;
alter table ind_vr_meta add atributo3 varchar(100) null;
alter table ind_vr_meta add atributo4 varchar(100) null;
alter table ind_vr_meta add atributo5 varchar(100) null;
alter table ind_vr_meta add atributo_nivel int4;

alter table ind_vr_bimestre add atributo1 varchar(100) null;
alter table ind_vr_bimestre add atributo2 varchar(100) null;
alter table ind_vr_bimestre add atributo3 varchar(100) null;
alter table ind_vr_bimestre add atributo4 varchar(100) null;
alter table ind_vr_bimestre add atributo5 varchar(100) null;
alter table ind_vr_bimestre add atributo_nivel int4;

alter table ind_vr_dia add atributo1 varchar(100) null;
alter table ind_vr_dia add atributo2 varchar(100) null;
alter table ind_vr_dia add atributo3 varchar(100) null;
alter table ind_vr_dia add atributo4 varchar(100) null;
alter table ind_vr_dia add atributo5 varchar(100) null;
alter table ind_vr_dia add atributo_nivel int4;

alter table ind_vr_mes add atributo1 varchar(100) null;
alter table ind_vr_mes add atributo2 varchar(100) null;
alter table ind_vr_mes add atributo3 varchar(100) null;
alter table ind_vr_mes add atributo4 varchar(100) null;
alter table ind_vr_mes add atributo5 varchar(100) null;
alter table ind_vr_mes add atributo_nivel int4;

alter table ind_vr_quadrimestre add atributo1 varchar(100) null;
alter table ind_vr_quadrimestre add atributo2 varchar(100) null;
alter table ind_vr_quadrimestre add atributo3 varchar(100) null;
alter table ind_vr_quadrimestre add atributo4 varchar(100) null;
alter table ind_vr_quadrimestre add atributo5 varchar(100) null;
alter table ind_vr_quadrimestre add atributo_nivel int4;

alter table ind_vr_quinzena add atributo1 varchar(100) null;
alter table ind_vr_quinzena add atributo2 varchar(100) null;
alter table ind_vr_quinzena add atributo3 varchar(100) null;
alter table ind_vr_quinzena add atributo4 varchar(100) null;
alter table ind_vr_quinzena add atributo5 varchar(100) null;
alter table ind_vr_quinzena add atributo_nivel int4;

alter table ind_vr_semana add atributo1 varchar(100) null;
alter table ind_vr_semana add atributo2 varchar(100) null;
alter table ind_vr_semana add atributo3 varchar(100) null;
alter table ind_vr_semana add atributo4 varchar(100) null;
alter table ind_vr_semana add atributo5 varchar(100) null;
alter table ind_vr_semana add atributo_nivel int4;

alter table ind_vr_semestre add atributo1 varchar(100) null;
alter table ind_vr_semestre add atributo2 varchar(100) null;
alter table ind_vr_semestre add atributo3 varchar(100) null;
alter table ind_vr_semestre add atributo4 varchar(100) null;
alter table ind_vr_semestre add atributo5 varchar(100) null;
alter table ind_vr_semestre add atributo_nivel int4;

alter table ind_vr_trimestre add atributo1 varchar(100) null;
alter table ind_vr_trimestre add atributo2 varchar(100) null;
alter table ind_vr_trimestre add atributo3 varchar(100) null;
alter table ind_vr_trimestre add atributo4 varchar(100) null;
alter table ind_vr_trimestre add atributo5 varchar(100) null;
alter table ind_vr_trimestre add atributo_nivel int4;



alter table ind_cjd_relac_ftd rename to ind_cjd_ftd;
alter table ind_cjd_ftd rename CONSTRAINT  fk_ind_cjd_relac_ftd_ind_cjd to fk_ind_cjd_ftd_ind_cjd_id;
alter table ind_cjd_ftd rename CONSTRAINT fk_ind_cjd_relac_ftd_ind_ftd to fk_ind_cjd_ftd_ind_ftd_id;
alter table ind_cjd_ftd rename CONSTRAINT pk_ind_cjd_relac_ftd to pk_ind_cjd_ftd;


alter table ind_ftd_relac_prm rename to ind_ftd_prm;
alter table ind_ftd_prm rename CONSTRAINT fk_ind_ftd_ind_ftd to fk_ind_ftd_prm_ind_ftd_id;
alter table ind_ftd_prm rename CONSTRAINT fk_ind_ftd_ind_param to fk_ind_ftd_prm_ind_prm_id;
alter table ind_ftd_prm rename CONSTRAINT pk_ind_ftd_relac_prm to pk_ind_ftd_prm;


alter table ind_grupo_relac_sub rename to ind_grupo_subgrupo;
alter table ind_grupo_subgrupo rename CONSTRAINT fk_ind_gupo_realc_sub_ind_grupo to fk_ind_grupo_subgrupo_ind_grupo_id;
alter table ind_grupo_subgrupo rename CONSTRAINT fk_ind_gupo_realc_sub_ind_subgrupo to fk_ind_grupo_subgrupo_ind_subgrupo_id;
alter table ind_grupo_subgrupo rename CONSTRAINT fk_ind_gupo_realc_sub_unit_id to  fk_ind_grupo_subgrupo_unit_id;
alter table ind_grupo_subgrupo rename CONSTRAINT pk_ind_grupo_relac_sub to pk_ind_grupo_subgrupo;


alter table ind_pnl_relac_rel rename to ind_pnl_rel;
alter table ind_pnl_rel rename CONSTRAINT fk_ind_pnl_relac_rel_ind_pnl_id to fk_ind_pnl_rel_ind_pnl_id;
alter table ind_pnl_rel rename CONSTRAINT fk_ind_pnl_relac_rel_ind_rel_id to fk_ind_pnl_rel_ind_rel_id;
alter table ind_pnl_rel rename CONSTRAINT pk_ind_pnl_relac_rel to pk_ind_pnl_rel;


alter table ind_rel_relac_prm rename to ind_rel_prm;
alter table ind_rel_prm rename CONSTRAINT fk_ind_rel_relac_prm_ind_prm_id to fk_ind_rel_prm_ind_prm_id;
alter table ind_rel_prm rename CONSTRAINT fk_ind_rel_relac_prm_ind_rel_id to fk_ind_rel_prm_ind_rel_id;
alter table ind_rel_prm rename CONSTRAINT pk_ind_rel_relac_prm to pk_ind_rel_prm;


alter table ind rename to ind_indic;
alter table ind_indic rename CONSTRAINT fk_ind_ger_umedida_id to fk_ind_indic_ger_umedida_id;
alter table ind_indic rename CONSTRAINT fk_ind_unit_id to fk_ind_indic_unit_id;
alter table ind_indic rename CONSTRAINT pk_ind to pk_ind_indic;
alter table ind_indic drop constraint fk_ind_ind_ponderado;
alter table ind_indic rename column ind_id_ponderacao to ind_indic_id_pond;


alter table ind_relac rename to ind_indic_indic;
alter table ind_indic_indic rename CONSTRAINT fk_ind_relac_unit_id to fk_ind_indic_indic_unit_id;
alter table ind_indic_indic rename CONSTRAINT pk_ind_relac to pk_ind_indic_indic;
alter table ind_indic_indic  drop constraint fk_ind_relac_ind_id;
alter table ind_indic_indic  drop constraint fk_ind_relac_ind_id_relac;
alter table ind_indic_indic rename column ind_id to ind_indic_id;
alter table ind_indic_indic rename column ind_id_relac to ind_indic_id_relac;
alter table ind_indic_indic add constraint fk_ind_indic_indic_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id) ON DELETE CASCADE;
alter table ind_indic_indic add constraint fk_ind_indic_indic_ind_indic_id_relac FOREIGN key  (ind_indic_id_relac) references ind_indic(id);


alter table ope_atividade_relac_prod rename to ope_atividade_prod;
alter table ope_atividade_prod rename CONSTRAINT fk_ope_atividade_relac_prod_ope_atividade_id to fk_ope_atividade_prod_ope_atividade_id;
alter table ope_atividade_prod rename CONSTRAINT fk_ope_atividade_relac_prod_ope_atividade_id_prod to fk_ope_atividade_prod_ope_atividade_id_prod;
alter table ope_atividade_prod rename CONSTRAINT fk_ope_atividade_relac_prod_unit_id to fk_ope_atividade_prod_unit_id;


alter table ind_vr_dia rename column ind_id to ind_indic_id;
alter table ind_vr_dia add constraint fk_ind_vr_dia_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id);
alter table ind_vr_ano rename column ind_id to ind_indic_id;
alter table ind_vr_ano add constraint fk_ind_vr_ano_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id);
alter table ind_vr_bimestre rename column ind_id to ind_indic_id;
alter table ind_vr_bimestre add constraint fk_ind_vr_bimestre_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id);
alter table ind_vr_mes rename column ind_id to ind_indic_id;
alter table ind_vr_mes add constraint fk_ind_vr_mes_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id);
alter table ind_vr_meta rename column ind_id to ind_indic_id;
alter table ind_vr_meta add constraint fk_ind_vr_meta_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id);
alter table ind_vr_quadrimestre rename column ind_id to ind_indic_id;
alter table ind_vr_quadrimestre add constraint fk_ind_vr_quadrimestre_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id);
alter table ind_vr_quinzena rename column ind_id to ind_indic_id;
alter table ind_vr_quinzena add constraint fk_ind_vr_quinzena_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id);
alter table ind_vr_semana rename column ind_id to ind_indic_id;
alter table ind_vr_semana add constraint fk_ind_vr_semana_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id);
alter table ind_vr_semestre rename column ind_id to ind_indic_id;
alter table ind_vr_semestre add constraint fk_ind_vr_semestre_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id);
alter table ind_vr_trimestre rename column ind_id to ind_indic_id;
alter table ind_vr_trimestre add constraint fk_ind_vr_trimestre_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id);


alter table ind_grupo_subgrupo rename column ind_id_grupo to ind_grupo_id;
alter table ind_grupo_subgrupo rename column ind_id_subgrupo to ind_subgrupo_id;

alter table ind_indic_indic drop constraint fk_ind_indic_indic_ind_indic_id;
alter table ind_indic_indic add constraint fk_ind_indic_indic_ind_indic_id FOREIGN key  (ind_indic_id) references ind_indic(id) ON DELETE CASCADE;

alter table ind_ftd_prm drop constraint fk_ind_ftd_prm_ind_ftd_id;
alter table ind_ftd_prm add constraint fk_ind_ftd_prm_ind_ftd_id FOREIGN key  (ind_prm_id) references ind_prm(id) ON DELETE CASCADE;

COMMENT ON COLUMN ind_indic.totalizador_atributo IS 'Totalizador do atributo: 1-Nenhum, 2-Soma, 3-Média';
COMMENT ON COLUMN ind_indic.ind_indic_id_pond IS 'ID do Indicador para Ponderação';
alter table ind_indic add tipo_meta varchar(1);
COMMENT ON COLUMN ind_indic.tipo_meta IS 'Tipo Meta: 1-Menor Melhor, 2-Maior Melhor';

alter table ind_indic add ativo varchar(1);
COMMENT ON COLUMN ind_indic.ativo IS 'Ativo: S-Sim, N-Não';

update sys_type_description set table_name = 'ind_indic' where table_name = 'ind';

INSERT INTO sys_type_description(id, table_name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, field_name, value_type, description_type) VALUES ('f4a590e3-c071-4134-affd-d3ada430a391', 'ind_indic', 'admin', '2023-01-07 20:06:58', NULL, NULL, 'tipo_meta', '1', 'IN18MENORMELHOR');
INSERT INTO sys_type_description(id, table_name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, field_name, value_type, description_type) VALUES ('12ac08af-31f2-4fbf-8e27-617ee820d970', 'ind_indic', 'admin', '2023-01-07 20:06:58', NULL, NULL, 'tipo_meta', '2', 'IN18MAIORMELHOR');

alter table ger_empresa add ger_per_tipo_id varchar(36);
COMMENT ON COLUMN ger_empresa.ger_per_tipo_id IS 'ID do Tipo Periodo';
alter table ger_empresa add constraint fk_ger_empresa_ger_per_tipo_id FOREIGN key  (ger_per_tipo_id) references ger_per_tipo(id);

COMMENT ON COLUMN ind_indic.campo_ordenacao IS 'Campo Ordenação: 1-Ordem Linha, 2 Ordem Atributo';

INSERT INTO sys_type_description(id, table_name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, field_name, value_type, description_type) VALUES ('8dfefafa-b760-4625-be43-de2e2e3acc2c', 'ind_indic', 'admin', '2023-01-07 20:06:58', NULL, NULL, 'campo_ordenacao', '1', 'IN18ORDEMLINHA');
INSERT INTO sys_type_description(id, table_name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, field_name, value_type, description_type) VALUES ('bb322f50-a69c-46fd-ab29-e27a9873ee1b', 'ind_indic', 'admin', '2023-01-07 20:06:58', NULL, NULL, 'campo_ordenacao', '2', 'IN18ORDEMATRIBUTO');

CREATE TABLE ind_indic_subgrupo (
  unit_id varchar(36)  NOT NULL,
  id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
  ind_indic_id varchar(36)  NOT NULL,
  ind_subgrupo_id varchar(36)  NOT NULL,
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  CONSTRAINT pk_ind_indic_subgrupo PRIMARY KEY (id),
  CONSTRAINT fk_ind_indic_subgrupo_ind_indic_id FOREIGN KEY (ind_indic_id) REFERENCES ind_indic (id) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT fk_ind_indic_subgrupo_ind_subgrupo_id FOREIGN KEY (ind_subgrupo_id) REFERENCES ind_subgrupo (id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT fk_ind_indic_subgrupo_unit_id FOREIGN KEY (unit_id) REFERENCES sys_unit (id) ON DELETE NO ACTION ON UPDATE NO ACTION
);
ALTER TABLE ind_indic_subgrupo OWNER TO postgres;
COMMENT ON COLUMN public.ind_indic_subgrupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN public.ind_indic_subgrupo.id IS 'ID do Relacionamento de Grupo x Sub-Grupo de Indicadores';
COMMENT ON COLUMN public.ind_indic_subgrupo.ind_indic_id IS 'ID do Indicador';
COMMENT ON COLUMN public.ind_indic_subgrupo.ind_subgrupo_id IS 'ID do Sub-Grupo de Indicador';
COMMENT ON COLUMN public.ind_indic_subgrupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN public.ind_indic_subgrupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN public.ind_indic_subgrupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN public.ind_indic_subgrupo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON TABLE public.ind_indic_subgrupo IS 'Indicador-Relacionamento de Indicador x Sub-Grupo de Indicadores';

CREATE TABLE sys_user_ind_subgrupo (
  id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
  sys_user_id varchar(36) ,
  ind_subgrupo_id varchar(36) ,
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  CONSTRAINT pk_sys_user_ind_subgrupo PRIMARY KEY (id),
  CONSTRAINT fk_sys_user_id FOREIGN KEY (sys_user_id) REFERENCES sys_user (id) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT fk_sys_user_ind_subgrupo_id FOREIGN KEY (ind_subgrupo_id) REFERENCES ind_subgrupo (id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

ALTER TABLE sys_user_ind_subgrupo   OWNER TO postgres;

CREATE INDEX idx_sys_user_ind_subgrupo_subgrupo ON sys_user_ind_subgrupo USING btree (  ind_subgrupo_id  pg_catalog.text_ops ASC NULLS LAST) WITH (FILLFACTOR = 90);
CREATE INDEX idx_sys_user_ind_subgrupo_user ON sys_user_ind_subgrupo USING btree (  sys_user_id  pg_catalog.text_ops ASC NULLS LAST) WITH (FILLFACTOR = 90);
COMMENT ON COLUMN sys_user_ind_subgrupo.id IS 'ID do Grupo x Usuário';
COMMENT ON COLUMN sys_user_ind_subgrupo.sys_user_id IS 'ID do Usuário';
COMMENT ON COLUMN sys_user_ind_subgrupo.ind_subgrupo_id IS 'ID do Subgrupo do Indicador';
COMMENT ON COLUMN sys_user_ind_subgrupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_user_ind_subgrupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_user_ind_subgrupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_user_ind_subgrupo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON TABLE sys_user_ind_pnl IS 'System-Usuário x Subgrupo do Indicador';


alter table ind_indic add exibir_dia_ant int4;
alter table ind_indic add exibir_dia_pos int4;
COMMENT ON COLUMN ind_indic.exibir_dia_ant IS 'Exibição Dia - Anterior';
COMMENT ON COLUMN ind_indic.exibir_dia_pos IS 'Exibição Dia - Posterior';
alter table ind_indic add exibir_semana_ant int4;
alter table ind_indic add exibir_semana_pos int4;
COMMENT ON COLUMN ind_indic.exibir_semana_ant IS 'Exibição Semana - Anterior';
COMMENT ON COLUMN ind_indic.exibir_semana_pos IS 'Exibição Semana - Posterior';
alter table ind_indic add exibir_quinzena_ant int4;
alter table ind_indic add exibir_quinzena_pos int4;
COMMENT ON COLUMN ind_indic.exibir_quinzena_ant IS 'Exibição Quinzena - Anterior';
COMMENT ON COLUMN ind_indic.exibir_quinzena_pos IS 'Exibição Quinzena - Posterior';
alter table ind_indic add exibir_mes_ant int4;
alter table ind_indic add exibir_mes_pos int4;
COMMENT ON COLUMN ind_indic.exibir_mes_ant IS 'Exibição Mes - Anterior';
COMMENT ON COLUMN ind_indic.exibir_mes_pos IS 'Exibição Mes - Posterior';
alter table ind_indic add exibir_bimestre_ant int4;
alter table ind_indic add exibir_bimestre_pos int4;
COMMENT ON COLUMN ind_indic.exibir_bimestre_ant IS 'Exibição Bimestre - Anterior';
COMMENT ON COLUMN ind_indic.exibir_bimestre_pos IS 'Exibição Bimestre - Posterior';
alter table ind_indic add exibir_trimestre_ant int4;
alter table ind_indic add exibir_trimestre_pos int4;
COMMENT ON COLUMN ind_indic.exibir_trimestre_ant IS 'Exibição Trimestre - Anterior';
COMMENT ON COLUMN ind_indic.exibir_trimestre_pos IS 'Exibição Trimestre - Posterior';
alter table ind_indic add exibir_quadrimestre_ant int4;
alter table ind_indic add exibir_quadrimestre_pos int4;
COMMENT ON COLUMN ind_indic.exibir_quadrimestre_ant IS 'Exibição Quadrimeste - Anterior';
COMMENT ON COLUMN ind_indic.exibir_quadrimestre_pos IS 'Exibição Quadrimeste - Posterior';
alter table ind_indic add exibir_semestre_ant int4;
alter table ind_indic add exibir_semestre_pos int4;
COMMENT ON COLUMN ind_indic.exibir_semestre_ant IS 'Exibição Semestre - Anterior';
COMMENT ON COLUMN ind_indic.exibir_semestre_pos IS 'Exibição Semestre - Posterior';
alter table ind_indic add exibir_ano_ant int4;
alter table ind_indic add exibir_ano_pos int4;
COMMENT ON COLUMN ind_indic.exibir_ano_ant IS 'Exibição Ano - Anterior';
COMMENT ON COLUMN ind_indic.exibir_ano_pos IS 'Exibição Ano - Posterior';


CREATE TABLE ind_legenda (
  id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
  nome varchar(100)  NOT NULL,
  ativo varchar(1)  NOT NULL,
  sigla_ind_legenda varchar(50)  NOT NULL,
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  CONSTRAINT pk_ind_legenda PRIMARY KEY (id)
);
ALTER TABLE ind_legenda   OWNER TO postgres;
COMMENT ON COLUMN ind_legenda.id IS 'ID da Legenda';
COMMENT ON COLUMN ind_legenda.nome IS 'Nome';
COMMENT ON COLUMN ind_legenda.ativo IS 'Ativo: S-Sim, N-Não';
COMMENT ON COLUMN ind_legenda.sigla_ind_legenda IS 'Sigla da Legenda do Indicador';
COMMENT ON COLUMN ind_legenda.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_legenda.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_legenda.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_legenda.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON TABLE ind_legenda IS 'Indicador-Legenda';


CREATE TABLE ind_legenda_config (
  unit_id varchar(36)  NOT NULL,
  id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
  ind_legenda_id varchar(36) NOT NULL,
  qnt_de numeric(18,6) NOT NULL,
  qnt_ate numeric(18,6) NOT NULL,
  cor varchar(50),
  icon varchar(50),
  observacao varchar(250),
  log_user_ins varchar(100) ,
  log_date_ins timestamp(0) DEFAULT now(),
  log_user_upd varchar(100) ,
  log_date_upd timestamp(0),
  CONSTRAINT pk_ind_legenda_config PRIMARY KEY (id),
  CONSTRAINT fk_ind_legenda_config_ind_legenda_id FOREIGN KEY (ind_legenda_id) REFERENCES ind_legenda (id) ON DELETE CASCADE,
  CONSTRAINT fk_ind_legenda_config_unit_id FOREIGN KEY (unit_id) REFERENCES sys_unit (id)
);

ALTER TABLE ind_legenda_config  OWNER TO postgres;
COMMENT ON COLUMN ind_legenda_config.unit_id IS 'ID de Unidade';
COMMENT ON COLUMN ind_legenda_config.id IS 'ID da Legenda - Config';
COMMENT ON COLUMN ind_legenda_config.ind_legenda_id IS 'ID da Legenda';
COMMENT ON COLUMN ind_legenda_config.qnt_de IS 'Quantidade - De';
COMMENT ON COLUMN ind_legenda_config.qnt_ate IS 'Quantidade - Ate';
COMMENT ON COLUMN ind_legenda_config.cor IS 'Cor';
COMMENT ON COLUMN ind_legenda_config.icon IS 'Icone';
COMMENT ON COLUMN ind_legenda_config.observacao IS 'Observação';
COMMENT ON COLUMN ind_legenda_config.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_legenda_config.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_legenda_config.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_legenda_config.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON TABLE ind_legenda_config IS 'Indicador-Legenda - Config';

alter table ind_indic add ind_legenda_id varchar(36);
COMMENT ON COLUMN ind_indic.ind_legenda_id IS 'ID da Legenda';

alter table ind_legenda add unit_id varchar(36); 
alter table ind_legenda add CONSTRAINT fk_ind_legenda_unit_id FOREIGN KEY (unit_id) REFERENCES sys_unit (id);
COMMENT ON COLUMN ind_legenda.unit_id IS 'ID de Unidade';


alter table ind_indic add tipo_meta_var varchar(1);
COMMENT ON COLUMN ind_indic.tipo_meta_var IS 'Tipo variação da meta: 1-Variação de quantidade, 2-Variação de Percentual';
INSERT INTO sys_type_description(id, table_name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, field_name, value_type, description_type) VALUES ('2d4f4a7b-4d95-40d7-a8c4-735aefe5f688', 'ind_indic', 'admin', '2023-01-07 20:06:58', NULL, NULL, 'tipo_meta_var', '1', 'IN18VARQUANTIDADE');
INSERT INTO sys_type_description(id, table_name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, field_name, value_type, description_type) VALUES ('1acc5e5d-882c-4c89-aa08-5af9ccfc75d6', 'ind_indic', 'admin', '2023-01-07 20:06:58', NULL, NULL, 'tipo_meta_var', '2', 'IN18VARPERCENTUAL');

delete from ind_rel_prm 
where ind_prm_id='059d6581-8fc9-4d44-84ae-01729457c247'
and ind_rel_id='da7751b9-a905-4e89-8392-7490c66c5a93';

UPDATE ind_ftd SET config_ftd = '{"query":"select /*FIELDS*/  from fin_doc_tipo where unit_id = ${pParUnitId} and id like ${pParFinDocTipoId} and nome like ${pParFinDocTipoNome} and ativo like ${pParFinDocTipoAtivo} and coalesce(log_user_ins,'''') like ${pParLogUserIns} and coalesce(log_user_upd,'''') like ${pParLogUserUpd} and COALESCE (log_date_ins, fnutil_sdt(''I''))  >= fnutil_nvl_sdt(${pParLogDateInsIni},''%'',''I'') AND COALESCE (log_date_ins, fnutil_sdt(''F'') )  <= fnutil_nvl_sdt(${pParLogDateInsFin},''%'',''F'') AND COALESCE (log_date_upd, fnutil_sdt(''I'') )  >= fnutil_nvl_sdt(${pParLogDateUpdIni},''%'',''I'') AND COALESCE (log_date_upd, fnutil_sdt(''F'') )  <= fnutil_nvl_sdt(${pParLogDateUpdFin},''%'',''F'')"}'
WHERE "id" = 'd6a5f6b9-60d8-49e0-b5af-14e1ed09c5a3';

update ind_prm set nome_tecnico='pVars01' where id='e6c8a4f2-8f66-447a-baaf-0946302c9ff3';
update ind_prm set nome_tecnico='pVars02' where id='36d96e27-310b-42ec-b09c-310ee0983048';	
update ind_prm set nome_tecnico='pVars03' where id='42ca64d1-d223-41bc-a82b-9db9f5bc9d60';	
update ind_prm set nome_tecnico='pVars04' where id='7bd77247-3c34-4f55-80ee-e96e450d7a22';	
update ind_prm set nome_tecnico='pVars05' where id='b6edf292-fc3e-4bbc-9134-415adc70e697';


alter table sys_notification_log rename CONSTRAINT fk_user_user_id to fk_sys_notification_log_sys_user_id;

COMMENT ON COLUMN sys_module.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_notification_log.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_notification_log.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_notification_log.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_notification_log.log_date_upd IS 'Log - Data de Alteração';

CREATE TABLE sys_notification_token (
  id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
  unit_id varchar(36),
	sys_user_id varchar(36),
	token text,
	data_token text,
	expired varchar(1),
  log_user_ins varchar(100),
  log_date_ins timestamp(6),
  log_user_upd varchar(100),
  log_date_upd timestamp(6),
  CONSTRAINT pk_sys_notification_token PRIMARY KEY (id),
  CONSTRAINT fk_sys_notification_token_sys_user_id FOREIGN KEY (sys_user_id) REFERENCES sys_user (id),
	CONSTRAINT fk_sys_notification_token_unit_id FOREIGN KEY (unit_id) REFERENCES sys_unit (id)
);

COMMENT ON TABLE sys_notification_token IS 'Systtem-Notificações-Token';
COMMENT ON COLUMN sys_notification_token.id IS 'ID da Notificação - Token';
COMMENT ON COLUMN sys_notification_token.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN sys_notification_token.sys_user_id IS 'ID do Usuário';
COMMENT ON COLUMN sys_notification_token.token IS 'Token';
COMMENT ON COLUMN sys_notification_token.data_token IS 'Dados do Token';
COMMENT ON COLUMN sys_notification_token.expired IS 'Expirado: S-Sim,N-Não';
COMMENT ON COLUMN sys_notification_token.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN sys_notification_token.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN sys_notification_token.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN sys_notification_token.log_date_upd IS 'Log - Data de Alteração';

CREATE UNIQUE INDEX idx_sys_notification_token_token ON sys_notification_token USING btree (token ASC NULLS LAST) WITH (fillfactor = 90);

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
