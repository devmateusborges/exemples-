import { MigrationInterface, QueryRunner } from 'typeorm';

export class m1639502851176 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`
    CREATE TABLE bor_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_bor_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_bor_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE bor_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN bor_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN bor_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN bor_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN bor_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN bor_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN bor_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN bor_unit_param.log_date_upd IS 'Log - Data de Alteração';

  /**/

  CREATE TABLE ctb_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_ctb_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_ctb_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE ctb_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN ctb_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN ctb_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN ctb_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN ctb_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN ctb_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN ctb_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN ctb_unit_param.log_date_upd IS 'Log - Data de Alteração';

  /**/

  CREATE TABLE doc_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_doc_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_doc_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE doc_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN doc_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN doc_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN doc_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN doc_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN doc_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN doc_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN doc_unit_param.log_date_upd IS 'Log - Data de Alteração';

  /**/

  CREATE TABLE fin_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_fin_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_fin_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE fin_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN fin_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN fin_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN fin_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN fin_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN fin_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN fin_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN fin_unit_param.log_date_upd IS 'Log - Data de Alteração';

  /**/

  CREATE TABLE fis_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_fis_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_fis_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE fis_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN fis_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN fis_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN fis_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN fis_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN fis_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN fis_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN fis_unit_param.log_date_upd IS 'Log - Data de Alteração';


  /**/

  CREATE TABLE ger_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_ger_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_ger_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE ger_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN ger_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN ger_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN ger_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN ger_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN ger_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN ger_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN ger_unit_param.log_date_upd IS 'Log - Data de Alteração';

  /**/

  CREATE TABLE ind_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_ind_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_ind_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE ind_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN ind_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN ind_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN ind_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN ind_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN ind_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN ind_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN ind_unit_param.log_date_upd IS 'Log - Data de Alteração';

  /**/

  CREATE TABLE mob_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_mob_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_mob_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE mob_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN mob_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN mob_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN mob_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN mob_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN mob_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN mob_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN mob_unit_param.log_date_upd IS 'Log - Data de Alteração';

  /**/

  CREATE TABLE mov_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_mov_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_mov_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE mov_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN mov_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN mov_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN mov_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN mov_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN mov_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN mov_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN mov_unit_param.log_date_upd IS 'Log - Data de Alteração';

  /**/

  CREATE TABLE ope_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_ope_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_ope_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE ope_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN ope_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN ope_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN ope_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN ope_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN ope_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN ope_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN ope_unit_param.log_date_upd IS 'Log - Data de Alteração';

  /**/

  CREATE TABLE pto_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_pto_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_pto_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE pto_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN pto_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN pto_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN pto_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN pto_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN pto_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN pto_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN pto_unit_param.log_date_upd IS 'Log - Data de Alteração';

  /**/

  CREATE TABLE rhm_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_rhm_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_rhm_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE rhm_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN rhm_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN rhm_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN rhm_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN rhm_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN rhm_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN rhm_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN rhm_unit_param.log_date_upd IS 'Log - Data de Alteração';

  /**/

  CREATE TABLE sys_unit_param (
      id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
      unit_id varchar(36) NOT NULL,
      system_unit_id varchar(36) NOT NULL,
      log_user_ins varchar(100),
      log_date_ins timestamp(0) DEFAULT now(),
      log_user_upd varchar(100),
      log_date_upd timestamp(0),
      CONSTRAINT pk_sys_unit_param PRIMARY KEY (id),
      CONSTRAINT fk_sys_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE sys_unit_param IS 'Parâmetros da unidade' ;
  COMMENT ON COLUMN sys_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN sys_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN sys_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN sys_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN sys_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN sys_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN sys_unit_param.log_date_upd IS 'Log - Data de Alteração';

  CREATE TABLE bov_unit_param (
    id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
    unit_id varchar(36) NOT NULL,
    system_unit_id varchar(36) NOT NULL,
    log_user_ins varchar(100),
    log_date_ins timestamp(0) DEFAULT now(),
    log_user_upd varchar(100),
    log_date_upd timestamp(0),
    CONSTRAINT pk_bov_unit_param PRIMARY KEY (id),
    CONSTRAINT fk_bov_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE bov_unit_param IS 'Parâmetros da pecuaria' ;
  COMMENT ON COLUMN bov_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN bov_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN bov_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN bov_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN bov_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN bov_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN bov_unit_param.log_date_upd IS 'Log - Data de Alteração';

  CREATE TABLE crm_unit_param (
    id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
    unit_id varchar(36) NOT NULL,
    system_unit_id varchar(36) NOT NULL,
    log_user_ins varchar(100),
    log_date_ins timestamp(0) DEFAULT now(),
    log_user_upd varchar(100),
    log_date_upd timestamp(0),
    CONSTRAINT pk_crm_unit_param PRIMARY KEY (id),
    CONSTRAINT fk_crm_unit_param_system_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit (id)
  );
  COMMENT ON TABLE crm_unit_param IS 'Parâmetros da atendimento' ;
  COMMENT ON COLUMN crm_unit_param.ID IS 'ID de Parâmetros da unidade' ;
  COMMENT ON COLUMN crm_unit_param.unit_id IS 'ID de Unidade' ;
  COMMENT ON COLUMN crm_unit_param.system_unit_id IS 'ID da Unidade em que este registro se refere' ;
  COMMENT ON COLUMN crm_unit_param.log_user_ins IS 'Log - Usuário de Inserção' ;
  COMMENT ON COLUMN crm_unit_param.log_date_ins IS 'Log - Data de Inserção' ;
  COMMENT ON COLUMN crm_unit_param.log_user_upd IS 'Log - Usuário de Alteração';
  COMMENT ON COLUMN crm_unit_param.log_date_upd IS 'Log - Data de Alteração';

      ALTER TABLE system_document add column mov_id varchar(36);
      ALTER TABLE system_document add column fin_pagrec_id varchar(36);
      ALTER TABLE system_document add column ope_centro1_id varchar(36);
      ALTER TABLE system_document add column ope_centro2_id varchar(36);
      ALTER TABLE system_document add column ope_centro2_ord_id varchar(36);
      ALTER TABLE system_document add column ope_compart_id varchar(36);
      ALTER TABLE system_document add column ope_compart_ocor_id varchar(36);
      ALTER TABLE system_document add column ope_ocor_id varchar(36);
      ALTER TABLE system_document add column ger_pessoa_id varchar(36);
      ALTER TABLE system_document add column crm_mov_id varchar(36);

      comment on column system_document.mov_id is 'ID do Movimento';
      comment on column system_document.fin_pagrec_id is 'ID do Pag/Rec';
      comment on column system_document.ope_centro1_id is 'ID do Centro Nível 1 Entrada/Saída';
      comment on column system_document.ope_centro2_id is 'ID do Centro Nível 2 Entrada/Saída';
      comment on column system_document.ope_centro2_ord_id is 'ID da Operação-Ordem';
      comment on column system_document.ope_compart_id is 'ID do Compartamento';
      comment on column system_document.ope_compart_ocor_id is 'ID do Compartamento da Ocorrência';
      comment on column system_document.ope_ocor_id is 'ID da Ocorrência';
      comment on column system_document.ger_pessoa_id is 'ID da Pessoa';
      comment on column system_document.crm_mov_id is 'ID do Movimento - Atendimento';

      ALTER TABLE system_document add constraint fk_system_document_mov_id foreign key (mov_id) references mov;
      ALTER TABLE system_document add constraint fk_system_document_fin_pagrec_id foreign key (fin_pagrec_id) references fin_pagrec;
      ALTER TABLE system_document add constraint fk_system_document_ope_centro1_id foreign key (ope_centro1_id) references ope_centro1;
      ALTER TABLE system_document add constraint fk_system_document_ope_centro2_id foreign key (ope_centro2_id) references ope_centro2;
      ALTER TABLE system_document add constraint fk_system_document_ope_centro2_ord_id foreign key (ope_centro2_ord_id) references ope_centro2_ord;
      ALTER TABLE system_document add constraint fk_system_document_ope_compart_id foreign key (ope_compart_id) references ope_compart;
      ALTER TABLE system_document add constraint fk_system_document_ope_compart_ocor_id foreign key (ope_compart_ocor_id) references ope_compart_ocor;
      ALTER TABLE system_document add constraint fk_system_document_ope_ocor_id foreign key (ope_ocor_id) references ope_ocor;
      ALTER TABLE system_document add constraint fk_system_document_ger_pessoa_id foreign key (ger_pessoa_id) references ger_pessoa;
      ALTER TABLE system_document add constraint fk_system_document_crm_mov_id foreign key (crm_mov_id) references crm_mov;

      drop table crm_mov_anexo;

      CREATE TABLE system_user_chat_grupo (
        id varchar(36) COLLATE pg_catalog.default NOT NULL DEFAULT uuid_generate_v4(),
        system_user_id varchar(36) COLLATE pg_catalog.default NOT NULL,
        crm_chat_grupo_id varchar(36) COLLATE pg_catalog.default NOT NULL,
        CONSTRAINT pk_system_user_chat_grupo PRIMARY KEY (id),
        CONSTRAINT fk_system_user_chat_grupo_chat_grupo_id FOREIGN KEY (crm_chat_grupo_id) REFERENCES crm_chat_grupo (id) ON DELETE NO ACTION ON UPDATE NO ACTION,
        CONSTRAINT fk_system_user_chat_grupo_system_user_id FOREIGN KEY (system_user_id) REFERENCES system_user (id) ON DELETE NO ACTION ON UPDATE NO ACTION
      );

      ALTER TABLE system_user_chat_grupo  OWNER TO postgres;
      COMMENT ON COLUMN system_user_chat_grupo.id IS 'ID do Usuário x Grupo do Chat';
      COMMENT ON COLUMN system_user_chat_grupo.system_user_id IS 'ID do Usuário';
      COMMENT ON COLUMN system_user_chat_grupo.crm_chat_grupo_id IS 'ID da Grupo do Chat';
      COMMENT ON TABLE system_user_chat_grupo IS 'System- Usuário x Grupo do Chat';

      drop table crm_chat_grupo_usuario;


      delete from system_group_program where system_program_id in ('84259eed-72b7-4346-ae8e-89b99f739556');
      delete from system_program where id in ('84259eed-72b7-4346-ae8e-89b99f739556');

      delete from system_group_program where system_program_id in ('5527d216-7e00-4c14-b122-cc33007e1400');
      delete from system_program where id in ('5527d216-7e00-4c14-b122-cc33007e1400');

      delete from system_group_program where system_program_id in ('966cf636-e2e1-4a1a-8d74-dc3e694e23c1');
      delete from system_program where id in ('966cf636-e2e1-4a1a-8d74-dc3e694e23c1');

      update system_program set name ='Pag/Rec - Baixa' where id='30b50f75-b06c-4425-ac4b-88b50b8d90f4';

      delete from system_group_program where system_program_id in ('3a5deff2-b346-450f-8097-6ba5c168a17b');
      delete from system_program where id in ('3a5deff2-b346-450f-8097-6ba5c168a17b');

      update system_program set name ='IBPT' where id='fd0a714c-9a39-4822-8aa2-60097f69daa2';
      update system_program set name ='NBS' where id='fe95af96-70d4-428b-a913-99bb6c0e597c';

      update system_program set type_program='L' where id='6a9da848-b1db-4f10-aefe-8fb397267b35';

      delete from system_group_program where system_program_id in ('00bced69-fbd1-4bcb-8a7d-f3c07503b795');
      delete from system_program where id in ('00bced69-fbd1-4bcb-8a7d-f3c07503b795');

      update system_program set name ='Parâmetro de Relatório' where id='21d9a471-37f3-4484-8eed-0a7692b786dd';


      INSERT INTO system_program(id, name, controller, log_user_ins, log_date_ins, log_user_upd, log_date_upd, menu, type_program, module_id, icon, admin) VALUES ('b9242c73-ed57-47ad-9484-4c3d11d2e342', 'Previsão Financeira', '/fin/finprev', NULL, '2020-11-17 15:13:38', NULL, NULL, 'S', 'L', 'cf4efc32-f1fc-4631-9189-5a71be403477', 'fas fa-table', 'N');

      INSERT INTO system_program(id, name, controller, log_user_ins, log_date_ins, log_user_upd, log_date_upd, menu, type_program, module_id, icon, admin)
      VALUES ('88446255-3827-4abd-bb5b-f055050a47dd', 'Parâmetros', '/ind/indunitparam', NULL, '2020-11-17 15:13:38', NULL, NULL, 'S', 'T', '82b4125d-0018-4d2e-8cc4-7f7ef7e52a08', 'fas fa-table', 'N');

      update system_program set name ='Operação de Movimento' where id='61367e65-04ee-431c-9d6e-a1620203cf12';

      delete from system_group_program where system_program_id in ('1368aa3f-8520-4faf-8283-50d49b71bc59');
      delete from system_program where id in ('1368aa3f-8520-4faf-8283-50d49b71bc59');

      INSERT INTO system_program(id, name, controller, log_user_ins, log_date_ins, log_user_upd, log_date_upd, menu, type_program, module_id, icon, admin)
      VALUES ('cf855479-d0dd-4c63-b948-176ee9adb49a', 'Centro 2', '/ope/opecentro2', NULL, '2020-11-17 15:13:38', NULL, NULL, 'S', 'T', '851f3230-70e7-44ea-a4aa-4c3c23f1052c', 'fas fa-table', 'N');

      INSERT INTO system_program(id, name, controller, log_user_ins, log_date_ins, log_user_upd, log_date_upd, menu, type_program, module_id, icon, admin)
      VALUES ('7eb1a5e1-a366-4dbe-93c0-c86118aa3ae4', 'Estágio', '/ope/opeestagio', NULL, '2020-11-17 15:13:38', NULL, NULL, 'S', 'T', '851f3230-70e7-44ea-a4aa-4c3c23f1052c', 'fas fa-table', 'N');

      DROP TABLE system_message;

      INSERT INTO system_program(id, name, controller, log_user_ins, log_date_ins, log_user_upd, log_date_upd, menu, type_program, module_id, icon, admin)
      VALUES ('a2a03603-822b-47ae-a7a0-17a6c880341b', 'Log de Email', '/sys/systememaillogview', NULL, '2020-11-17 15:13:38', NULL, NULL, 'S', 'U', 'ca29f487-243f-4c94-8a39-7c3faca63e90', 'fas fa-table', 'N');

      update system_program set name ='Log de Processamento' where id='14bd9d36-67ea-4f47-b347-c81b05fd8f18';

      CREATE TABLE system_program_feature (
        id varchar(36) COLLATE pg_catalog.default NOT NULL,
        system_program_id varchar(36) COLLATE pg_catalog.default NOT NULL,
        identity varchar(200) COLLATE pg_catalog.default NOT NULL,
        descricao text COLLATE pg_catalog.default,
        log_user_ins varchar(100) COLLATE pg_catalog.default,
        log_user_upd varchar(100) COLLATE pg_catalog.default,
        log_date_ins timestamp(6),
        log_date_upd timestamp(6),
        CONSTRAINT system_program_feature_pkey PRIMARY KEY (id),
        CONSTRAINT fk_system_program_feature_system_program_id FOREIGN KEY (system_program_id) REFERENCES system_program (id) ON DELETE NO ACTION ON UPDATE NO ACTION
      );
      ALTER TABLE system_program_feature   OWNER TO postgres;
      COMMENT ON COLUMN system_program_feature.id IS 'ID do Sistema - Features do Programa';
      COMMENT ON COLUMN system_program_feature.system_program_id IS 'ID do Programa';
      COMMENT ON COLUMN system_program_feature.identity IS 'Identificador da feature';
      COMMENT ON COLUMN system_program_feature.descricao IS 'Descrição da feature';
      COMMENT ON COLUMN system_program_feature.log_user_ins IS 'Log - Usuário de Inserção';
      COMMENT ON COLUMN system_program_feature.log_user_upd IS 'Log - Usuário de Alteração';
      COMMENT ON COLUMN system_program_feature.log_date_ins IS 'Log - Data de Inserção';
      COMMENT ON COLUMN system_program_feature.log_date_upd IS 'Log - Data de Alteração';
      COMMENT ON TABLE system_program_feature IS 'Sistema - Features do Programa';
      CREATE TABLE system_user_program_feature (
        id varchar(36) COLLATE pg_catalog.default NOT NULL,
        system_program_id varchar(36) COLLATE pg_catalog.default NOT NULL,
        identity_feature varchar(200) COLLATE pg_catalog.default NOT NULL,
        system_user_id varchar(36) COLLATE pg_catalog.default NOT NULL,
        log_user_ins varchar(100) COLLATE pg_catalog.default,
        log_user_upd varchar(100) COLLATE pg_catalog.default,
        log_date_ins timestamp(6),
        log_date_upd timestamp(6),
        CONSTRAINT system_user_program_feature_pkey PRIMARY KEY (id),
        CONSTRAINT fk_system_user_program_feature_system_program_id FOREIGN KEY (system_program_id) REFERENCES system_program (id) ON DELETE NO ACTION ON UPDATE NO ACTION,
        CONSTRAINT fk_system_user_program_feature_system_user_id FOREIGN KEY (system_user_id) REFERENCES system_user (id) ON DELETE NO ACTION ON UPDATE NO ACTION
      );
      ALTER TABLE system_user_program_feature   OWNER TO postgres;
      COMMENT ON COLUMN system_user_program_feature.id IS 'ID do Sistema - Usuário - Features do Programa';
      COMMENT ON COLUMN system_user_program_feature.system_program_id IS 'ID do Programa';
      COMMENT ON COLUMN system_user_program_feature.identity_feature IS 'Identificador da feature';
      COMMENT ON COLUMN system_user_program_feature.system_user_id IS 'ID do Usuário';
      COMMENT ON COLUMN system_user_program_feature.log_user_ins IS 'Log - Usuário de Inserção';
      COMMENT ON COLUMN system_user_program_feature.log_user_upd IS 'Log - Usuário de Alteração';
      COMMENT ON COLUMN system_user_program_feature.log_date_ins IS 'Log - Data de Inserção';
      COMMENT ON COLUMN system_user_program_feature.log_date_upd IS 'Log - Data de Alteração';
      COMMENT ON TABLE system_user_program_feature IS 'Sistema - Usuário - Features do Programa';
      CREATE TABLE system_group_program_feature (
       id varchar(36) COLLATE pg_catalog.default NOT NULL,
       system_program_id varchar(36) COLLATE pg_catalog.default NOT NULL,
        identity_feature varchar(200) COLLATE pg_catalog.default NOT NULL,
        system_group_id varchar(36) COLLATE pg_catalog.default NOT NULL,
        log_user_ins varchar(100) COLLATE pg_catalog.default,
        log_user_upd varchar(100) COLLATE pg_catalog.default,
        log_date_ins timestamp(6),
        log_date_upd timestamp(6),
        CONSTRAINT system_group_program_feature_pkey PRIMARY KEY (id),
        CONSTRAINT fk_system_group_program_feature_system_group_id FOREIGN KEY (system_group_id) REFERENCES system_group (id) ON DELETE NO ACTION ON UPDATE NO ACTION,
        CONSTRAINT fk_system_group_program_feature_system_program_id FOREIGN KEY (system_program_id) REFERENCES system_program (id) ON DELETE NO ACTION ON UPDATE NO ACTION
      );
      ALTER TABLE system_group_program_feature   OWNER TO postgres;
      COMMENT ON COLUMN system_group_program_feature.id IS 'ID do Sistema - Grupo - Features do Programa';
      COMMENT ON COLUMN system_group_program_feature.system_program_id IS 'ID do Programa';
      COMMENT ON COLUMN system_group_program_feature.identity_feature IS 'Identificador da feature';
      COMMENT ON COLUMN system_group_program_feature.system_group_id IS 'ID do Grupo';
      COMMENT ON COLUMN system_group_program_feature.log_user_ins IS 'Log - Usuário de Inserção';
      COMMENT ON COLUMN system_group_program_feature.log_user_upd IS 'Log - Usuário de Alteração';
      COMMENT ON COLUMN system_group_program_feature.log_date_ins IS 'Log - Data de Inserção';
      COMMENT ON COLUMN system_group_program_feature.log_date_upd IS 'Log - Data de Alteração';
      COMMENT ON TABLE system_group_program_feature IS 'Sistema - Grupo - Features do Programa';

      update system_program set name ='Permissões para Funcionalidades', controller='/sys/systemfeaturepermission' where id='13253c34-5407-44bb-998a-5d56b7ed89d7';

      delete from system_group_program where system_program_id in ('2703daf4-5b5b-4666-bc16-aedb4e36c62e','0101ade6-fec8-407a-b44d-f74217e4744d');
      delete from system_program where id in ('2703daf4-5b5b-4666-bc16-aedb4e36c62e','0101ade6-fec8-407a-b44d-f74217e4744d');

      delete from system_group_program where system_program_id in ('c38231c1-6f57-43aa-800b-489a5b384d2c');
      delete from system_program where id in ('c38231c1-6f57-43aa-800b-489a5b384d2c');

      drop table doc_unit_param;


      alter table system_user_unit RENAME CONSTRAINT fk_system_user_unit_system_unit_id to fk_sys_user_unit_system_unit_id;
alter table system_user_unit RENAME CONSTRAINT fk_system_user_unit_system_user_id to fk_sys_user_unit_system_user_id;
alter table system_restriction_licence RENAME CONSTRAINT fk_system_restriction_licence_system_restriction_id to fk_sys_restriction_licence_system_restriction_id;
alter table system_restriction_licence RENAME CONSTRAINT fk_system_restriction_licence_system_licence_id to fk_sys_restriction_licence_system_licence_id;
alter table system_licence_device RENAME CONSTRAINT fk_system_licence_device_system_licence_id to fk_sys_licence_device_system_licence_id;
alter table system_user_ind_pnl RENAME CONSTRAINT fk_system_user_ind_pnl to fk_sys_user_ind_pnl;
alter table system_user_ind_pnl RENAME CONSTRAINT fk_system_user_id to fk_sys_user_id;
alter table system_plan RENAME CONSTRAINT fk_system_plan_system_id to fk_sys_plan_system_id;
alter table system_plan_restriction RENAME CONSTRAINT fk_system_plan_restriction_system_plan_id to fk_sys_plan_restriction_system_plan_id;
alter table system_plan_restriction RENAME CONSTRAINT fk_system_plan_restriction_system_restriction_id to fk_sys_plan_restriction_system_restriction_id;
alter table system_licence RENAME CONSTRAINT fk_system_licence_system_id to fk_sys_licence_system_id;
alter table system_licence RENAME CONSTRAINT fk_system_licence_system_plan_id to fk_sys_licence_system_plan_id;
alter table system_licence RENAME CONSTRAINT fk_system_licence_system_user_id to fk_sys_licence_system_user_id;
alter table system_document RENAME CONSTRAINT fk_system_document_category_id to fk_sys_document_category_id;
alter table system_document_group RENAME CONSTRAINT fk_system_document_group_document_id to fk_sys_document_group_document_id;
alter table system_document_user RENAME CONSTRAINT fk_system_document_user_document_id to fk_sys_document_user_document_id;
alter table system_group_program RENAME CONSTRAINT fk_system_group_program_system_group_id to fk_sys_group_program_system_group_id;
alter table system_group_program RENAME CONSTRAINT fk_system_group_program_system_program_id to fk_sys_group_program_system_program_id;
alter table system_user_group RENAME CONSTRAINT fk_system_user_group_system_group_id to fk_sys_user_group_system_group_id;
alter table system_user_group RENAME CONSTRAINT fk_system_user_group_system_user_id to fk_sys_user_group_system_user_id;
alter table system_user_program RENAME CONSTRAINT fk_system_user_program_system_program_id to fk_sys_user_program_system_program_id;
alter table system_user_program RENAME CONSTRAINT fk_system_user_program_system_user_id to fk_sys_user_program_system_user_id;
alter table system_document_group RENAME CONSTRAINT fk_system_document_group_group_id to fk_sys_document_group_group_id;
alter table system_document_user RENAME CONSTRAINT fk_system_document_user_system_user_id to fk_sys_document_user_system_user_id;
alter table system_document RENAME CONSTRAINT fk_system_document_system_user_id to fk_sys_document_system_user_id;
alter table system_process_log RENAME CONSTRAINT fk_system_process_log_unit_id to fk_sys_process_log_unit_id;
alter table system_process_log RENAME CONSTRAINT fk_system_process_log_system_user_id to fk_sys_process_log_system_user_id;
alter table system_user_preference RENAME CONSTRAINT fk_system_user_preference_system_user_id to fk_sys_user_preference_system_user_id;
alter table system_param RENAME CONSTRAINT fk_system_param_system_id to fk_sys_param_system_id;
alter table system_module RENAME CONSTRAINT fk_system_module_system_id to fk_sys_module_system_id;
alter table system_program RENAME CONSTRAINT fk_system_program_system_module_id to fk_sys_program_system_module_id;
alter table system_program_favorite RENAME CONSTRAINT fk_system_program_favorite_program_id to fk_sys_program_favorite_program_id;
alter table system_program_favorite RENAME CONSTRAINT fk_system_program_favorite_user_id to fk_sys_program_favorite_user_id;
alter table system_access_log RENAME CONSTRAINT fk_system_access_log_system_user_id to fk_sys_access_log_system_user_id;
alter table system_access_log RENAME CONSTRAINT fk_system_access_log_unit_id to fk_sys_access_log_unit_id;
alter table system_access_log RENAME CONSTRAINT fk_system_access_log_system_id to fk_sys_access_log_system_id;
alter table system_document RENAME CONSTRAINT fk_system_document_mov_id to fk_sys_document_mov_id;
alter table system_document RENAME CONSTRAINT fk_system_document_fin_pagrec_id to fk_sys_document_fin_pagrec_id;
alter table system_document RENAME CONSTRAINT fk_system_document_ope_centro1_id to fk_sys_document_ope_centro1_id;
alter table system_document RENAME CONSTRAINT fk_system_document_ope_centro2_id to fk_sys_document_ope_centro2_id;
alter table system_document RENAME CONSTRAINT fk_system_document_ope_centro2_ord_id to fk_sys_document_ope_centro2_ord_id;
alter table system_document RENAME CONSTRAINT fk_system_document_ope_compart_id to fk_sys_document_ope_compart_id;
alter table system_document RENAME CONSTRAINT fk_system_document_ope_compart_ocor_id to fk_sys_document_ope_compart_ocor_id;
alter table system_document RENAME CONSTRAINT fk_system_document_ope_ocor_id to fk_sys_document_ope_ocor_id;
alter table system_document RENAME CONSTRAINT fk_system_document_ger_pessoa_id to fk_sys_document_ger_pessoa_id;
alter table system_document RENAME CONSTRAINT fk_system_document_crm_mov_id to fk_sys_document_crm_mov_id;
alter table system_user_chat_grupo RENAME CONSTRAINT fk_system_user_chat_grupo_chat_grupo_id to fk_sys_user_chat_grupo_chat_grupo_id;
alter table system_user_chat_grupo RENAME CONSTRAINT fk_system_user_chat_grupo_system_user_id to fk_sys_user_chat_grupo_system_user_id;
alter table system_program_feature RENAME CONSTRAINT fk_system_program_feature_system_program_id to fk_sys_program_feature_system_program_id;
alter table system_user_program_feature RENAME CONSTRAINT fk_system_user_program_feature_system_program_id to fk_sys_user_program_feature_system_program_id;
alter table system_user_program_feature RENAME CONSTRAINT fk_system_user_program_feature_system_user_id to fk_sys_user_program_feature_system_user_id;
alter table system_group_program_feature RENAME CONSTRAINT fk_system_group_program_feature_system_group_id to fk_sys_group_program_feature_system_group_id;
alter table system_group_program_feature RENAME CONSTRAINT fk_system_group_program_feature_system_program_id to fk_sys_group_program_feature_system_program_id;


ALTER TABLE system_user RENAME CONSTRAINT pk_system_user TO pk_sys_user;
alter table system_unit RENAME CONSTRAINT pk_system_unit to pk_sys_unit;
alter table system_user_unit RENAME CONSTRAINT pk_system_user_unit to pk_sys_user_unit;
alter table system RENAME CONSTRAINT pk_system to pk_sys;
alter table system_licence RENAME CONSTRAINT pk_system_licence to pk_sys_licence;
alter table system_restriction RENAME CONSTRAINT pk_system_restriction to pk_sys_restriction;
alter table system_restriction_licence RENAME CONSTRAINT pk_system_restriction_licence to pk_sys_restriction_licence;
alter table system_licence_device RENAME CONSTRAINT pk_system_licence_device to pk_sys_licence_device;
alter table system_user_ind_pnl RENAME CONSTRAINT pk_system_user_ind_pnl to pk_sys_user_ind_pnl;
alter table system_plan RENAME CONSTRAINT pk_system_plan to pk_sys_plan;
alter table system_plan_restriction RENAME CONSTRAINT pk_system_plan_restriction to pk_sys_plan_restriction;
alter table system_token RENAME CONSTRAINT pk_system_token to pk_sys_token;
alter table system_type_description RENAME CONSTRAINT pk_system_type_description to pk_sys_type_description;
alter table system_document RENAME CONSTRAINT pk_system_document to pk_sys_document;
alter table system_document_category RENAME CONSTRAINT pk_system_document_category to pk_sys_document_category;
alter table system_document_group RENAME CONSTRAINT pk_system_document_group to pk_sys_document_group;
alter table system_document_user RENAME CONSTRAINT pk_system_document_user to pk_sys_document_user;
alter table system_group RENAME CONSTRAINT pk_system_group to pk_sys_group;
alter table system_preference RENAME CONSTRAINT pk_system_preference to pk_sys_preference;
alter table system_program RENAME CONSTRAINT pk_system_program to pk_sys_program;
alter table system_user_group RENAME CONSTRAINT pk_system_user_group to pk_sys_user_group;
alter table system_user_program RENAME CONSTRAINT pk_system_user_program to pk_sys_user_program;
alter table system_process_log RENAME CONSTRAINT pk_system_process_log to pk_sys_process_log;
alter table system_notification_log RENAME CONSTRAINT pk_system_notification_log to pk_sys_notification_log;
alter table system_user_preference RENAME CONSTRAINT pk_system_user_preference to pk_sys_user_preference;
alter table system_module RENAME CONSTRAINT pk_system_module to pk_sys_module;
alter table system_param RENAME CONSTRAINT pk_system_param to pk_sys_param;
alter table system_program_favorite RENAME CONSTRAINT pk_system_program_favorite to pk_sys_program_favorite;
alter table system_access_log RENAME CONSTRAINT pk_system_access_log to pk_sys_access_log;
alter table system_change_log RENAME CONSTRAINT pk_system_change_log to pk_sys_change_log;
alter table system_email_log RENAME CONSTRAINT pk_system_email_log to pk_sys_email_log;
alter table system_sql_log RENAME CONSTRAINT pk_system_sql_log to pk_sys_sql_log;
alter table system_user_chat_grupo RENAME CONSTRAINT pk_system_user_chat_grupo to pk_sys_user_chat_grupo;


alter table bor_unit_param RENAME column system_unit_id to sys_unit_id;
alter table system_user_unit RENAME column system_user_id to sys_user_id;
alter table system_user_unit RENAME column system_unit_id to sys_unit_id;
alter table ctb_unit_param RENAME column system_unit_id to sys_unit_id;
alter table fin_unit_param RENAME column system_unit_id to sys_unit_id;
alter table fis_unit_param RENAME column system_unit_id to sys_unit_id;
alter table ger_unit_param RENAME column system_unit_id to sys_unit_id;
alter table ind_unit_param RENAME column system_unit_id to sys_unit_id;
alter table mob_unit_param RENAME column system_unit_id to sys_unit_id;
alter table mov_unit_param RENAME column system_unit_id to sys_unit_id;
alter table ope_unit_param RENAME column system_unit_id to sys_unit_id;
alter table pto_unit_param RENAME column system_unit_id to sys_unit_id;
alter table rhm_unit_param RENAME column system_unit_id to sys_unit_id;
alter table sys_unit_param RENAME column system_unit_id to sys_unit_id;
alter table mov RENAME column system_user_id_resp to sys_user_id_resp;
alter table bov_unit_param RENAME column system_unit_id to sys_unit_id;
alter table crm_unit_param RENAME column system_unit_id to sys_unit_id;
alter table system_user_chat_grupo RENAME column system_user_id to sys_user_id;
alter table system_program_feature RENAME column system_program_id to sys_program_id;
alter table system_licence RENAME column system_plan_id to sys_plan_id;
alter table system_licence RENAME column system_id to sys_id;
alter table system_licence RENAME column system_user_id to sys_user_id;
alter table system_licence RENAME column system_version to sys_version;
alter table system_restriction_licence RENAME column system_restriction_id to sys_restriction_id;
alter table system_restriction_licence RENAME column system_licence_id to sys_licence_id;
alter table system_licence_device RENAME column system_licence_id to sys_licence_id;
alter table system_user_program_feature RENAME column system_program_id to sys_program_id;
alter table system_user_program_feature RENAME column system_user_id to sys_user_id;
alter table system_group_program_feature RENAME column system_program_id to sys_program_id;
alter table system_group_program_feature RENAME column system_group_id to sys_group_id;
alter table system_user_ind_pnl RENAME column system_user_id to sys_user_id;
alter table system_plan RENAME column system_id to sys_id;
alter table system_plan_restriction RENAME column system_plan_id to sys_plan_id;
alter table system_plan_restriction RENAME column system_restriction_id to sys_restriction_id;
alter table ger_processo_bloq_user RENAME column system_user_id to sys_user_id;
alter table crm_mov RENAME column system_user_id_solic to sys_user_id_solic;
alter table crm_mov RENAME column system_user_id_atend_atu to sys_user_id_atend_atu;
alter table crm_mov RENAME column system_user_id_atend_ant to sys_user_id_atend_ant;
alter table crm_mov_hist RENAME column system_user_id_hist to sys_user_id_hist;
alter table system_document RENAME column system_user_id to sys_user_id;
alter table system_document_group RENAME column system_group_id to sys_group_id;
alter table system_document_user RENAME column system_user_id to sys_user_id;
alter table system_user_group RENAME column system_user_id to sys_user_id;
alter table system_user_group RENAME column system_group_id to sys_group_id;
alter table system_group_program RENAME column system_program_id to sys_program_id;
alter table system_group_program RENAME column system_group_id to sys_group_id;

alter table system_user_program RENAME column system_user_id to sys_user_id;
alter table system_user_program RENAME column system_program_id to sys_program_id;
alter table system_process_log RENAME column system_user_id to sys_user_id;
alter table system_notification_log RENAME column system_user_id to sys_user_id;
alter table system_notification_log RENAME column system_user_to_id to sys_user_to_id;
alter table system_user_preference RENAME column system_user_id to sys_user_id;
alter table mov_cotacao RENAME column system_user_id_aprov to sys_user_id_aprov;
alter table mov_cotacao_anal RENAME column c01_system_user_id_aprov to c01_sys_user_id_aprov;
alter table mov_cotacao_anal RENAME column c02_system_user_id_aprov to c02_sys_user_id_aprov;
alter table mov_cotacao_anal RENAME column c03_system_user_id_aprov to c03_sys_user_id_aprov;
alter table mov_cotacao_anal RENAME column c04_system_user_id_aprov to c04_sys_user_id_aprov;
alter table mov_cotacao_anal RENAME column c05_system_user_id_aprov to c05_sys_user_id_aprov;
alter table mov_cotacao_anal RENAME column c06_system_user_id_aprov to c06_sys_user_id_aprov;
alter table mov_cotacao_anal RENAME column c07_system_user_id_aprov to c07_sys_user_id_aprov;
alter table mov_cotacao_anal RENAME column c08_system_user_id_aprov to c08_sys_user_id_aprov;
alter table mov_cotacao_anal RENAME column c09_system_user_id_aprov to c09_sys_user_id_aprov;
alter table mov_cotacao_anal RENAME column c10_system_user_id_aprov to c10_sys_user_id_aprov;
alter table system_module RENAME column system_id to sys_id;
alter table system_param RENAME column system_id to sys_id;
alter table system_program_favorite RENAME column system_user_id to sys_user_id;
alter table system_program_favorite RENAME column system_program_id to sys_program_id;
alter table crm_chat_grupo RENAME column system_user_id_orig to sys_user_id_orig;
alter table crm_chat_grupo RENAME column system_user_id_dest to sys_user_id_dest;
alter table crm_chat_msg RENAME column system_user_id_orig to sys_user_id_orig;


alter table system rename to sys;
alter table system_access_log rename to sys_access_log;
alter table system_change_log rename to sys_change_log;
alter table system_document rename to sys_document;
alter table system_document_category rename to sys_document_category;
alter table system_document_group rename to sys_document_group;
alter table system_document_user rename to sys_document_user;
alter table system_email_log rename to sys_email_log;
alter table system_group rename to sys_group;
alter table system_group_program rename to sys_group_program;
alter table system_group_program_feature rename to sys_group_program_feature;
alter table system_licence rename to sys_licence;
alter table system_licence_device rename to sys_licence_device;
alter table system_module rename to sys_module;
alter table system_notification_log rename to sys_notification_log;
alter table system_param rename to sys_param;
alter table system_plan rename to sys_plan;
alter table system_plan_restriction rename to sys_plan_restriction;
alter table system_preference rename to sys_preference;
alter table system_process_log rename to sys_process_log;
alter table system_program rename to sys_program;
alter table system_program_favorite rename to sys_program_favorite;
alter table system_program_feature rename to sys_program_feature;
alter table system_restriction rename to sys_restriction;
alter table system_restriction_licence rename to sys_restriction_licence;
alter table system_sql_log rename to sys_sql_log;
alter table system_token rename to sys_token;
alter table system_type_description rename to sys_type_description;
alter table system_unit rename to sys_unit;
alter table system_user rename to sys_user;
alter table system_user_chat_grupo rename to sys_user_chat_grupo;
alter table system_user_group rename to sys_user_group;
alter table system_user_ind_pnl rename to sys_user_ind_pnl;
alter table system_user_preference rename to sys_user_preference;
alter table system_user_program rename to sys_user_program;
alter table system_user_program_feature rename to sys_user_program_feature;
alter table system_user_unit rename to sys_user_unit;



alter table sys_user_unit RENAME column sys_unit_id to unit_id;


alter table bor_unit_param drop column sys_unit_id;
alter table bov_unit_param drop column sys_unit_id;
alter table crm_unit_param drop column sys_unit_id;
alter table ctb_unit_param drop column sys_unit_id;
alter table fin_unit_param drop column sys_unit_id;
alter table fis_unit_param drop column sys_unit_id;
alter table ger_unit_param drop column sys_unit_id;
alter table ind_unit_param drop column sys_unit_id;
alter table mob_unit_param drop column sys_unit_id;
alter table mov_unit_param drop column sys_unit_id;
alter table ope_unit_param drop column sys_unit_id;
alter table pto_unit_param drop column sys_unit_id;
alter table rhm_unit_param drop column sys_unit_id;
alter table sys_unit_param drop column sys_unit_id;

alter table sys_program_feature RENAME CONSTRAINT system_program_feature_pkey to pk_sys_program_feature;
alter table sys_user_program_feature RENAME CONSTRAINT system_user_program_feature_pkey to pk_sys_user_program_feature;
alter table sys_group_program_feature RENAME CONSTRAINT system_group_program_feature_pkey to pk_sys_group_program_feature;
alter table sys_group_program RENAME CONSTRAINT system_group_program_pkey to pk_sys_group_program;

alter index idx_system_user_ind_pnl_pnl rename to idx_sys_user_ind_pnl_pnl;
alter index idx_system_user_ind_pnl_user rename to idx_sys_user_ind_pnl_user;
alter index idx_system_token rename to idx_sys_token;
alter index idx_system_type_description rename to idx_sys_type_description;
alter index idx_system_group_program_group rename to idx_sys_group_program_group;
alter index idx_system_group_program_program rename to idx_sys_group_program_program;
alter index unq_system_param rename to unq_sys_param;
alter index idx_system_user_group_group rename to idx_sys_user_group_group;
alter index idx_system_user_group_user rename to idx_sys_user_group_user;
alter index idx_system_param rename to idx_sys_param;


drop table sys_preference;
drop table sys_sql_log;

alter TABLE sys_document add content_type varchar(50);
COMMENT ON COLUMN sys_document.content_type IS 'Tipo de Conteudo';

alter TABLE sys_document alter column id  set DEFAULT uuid_generate_v4();

alter table sys_user add image_url varchar(1000);
alter table sys_user add email_verified varchar(1);
alter table sys_user add provider varchar(50);
alter table sys_user add provider_code varchar(50);
comment on column sys_user.image_url IS 'Url da imagem do usuario';
comment on column sys_user.email_verified IS 'Email verificado';
comment on column sys_user.email_verified IS 'Provider de autenticacao';
comment on column sys_user.email_verified IS 'Codigo do provider autenticado';;

INSERT INTO sys_user(id, log_date_ins, log_date_upd, log_user_ins, log_user_upd, active, active_message, admin, chat, document, email, email_verified, frontpage_id, image_url, login, login_ext, name, origem, password, phone, provider, provider_code) VALUES ('062dddad-4ca3-4956-aa75-6f6cf368b05b', '2022-04-25 23:46:15', NULL, 'admin', NULL, 'S', NULL, 'S', 'S', NULL, 'admin@admin.com', 'S', NULL, NULL, 'admin', NULL, 'Admin', '1', 'SsVJ3oSyzjz0L+8oup+nIGiyJ0pbX/5O9phOUIOgvlo=', NULL, 'local', NULL);

create table test1 (
  id uuid not null,
   log_date_ins timestamp,
   log_date_upd timestamp,
   log_user_ins varchar(100),
   log_user_upd varchar(100),
   codigo varchar(50) not null,
   descricao varchar(50) not null,
   dt_nascimento timestamp not null,
   constraint pk_test1 primary key (id)
);

create table test1_child (
  id uuid not null,
   log_date_ins timestamp,
   log_date_upd timestamp,
   log_user_ins varchar(100),
   log_user_upd varchar(100),
   codigo varchar(50) not null,
   quantidade numeric(18, 6) not null,
   valor_total numeric(18, 2) not null,
   valor_unit numeric(18, 2) not null,
   test1_id uuid not null,
   constraint pk_test1_child primary key (id)
);

alter table test1_child
  add constraint fk_test1_child_test1_id
  foreign key (test1_id)
  references test1;

  drop table test1_child;
  drop table test1;
  create table test1 (
         id varchar(36) not null,
          log_date_ins timestamp,
          log_date_upd timestamp,
          log_user_ins varchar(100),
          log_user_upd varchar(100),
          codigo varchar(50) not null,
          descricao varchar(50) not null,
          dt_nascimento timestamp not null,
          constraint pk_test1 primary key (id)
      );

      create table test1_child (
          id varchar(36) not null,
          log_date_ins timestamp,
          log_date_upd timestamp,
          log_user_ins varchar(100),
          log_user_upd varchar(100),
          codigo varchar(50) not null,
          quantidade numeric(18, 6) not null,
          valor_total numeric(18, 2) not null,
          valor_unit numeric(18, 2) not null,
          test1_id varchar(36) not null,
          constraint pk_test1_child primary key (id)
      );

      alter table test1_child
         add constraint fk_test1_child_test1_id
         foreign key (test1_id)
         references test1;

         drop table test1_child;
drop table test1;
alter table sys_unit drop column connection_name;
alter table sys_unit drop column img_logo;

create table test1 (
  id varchar(36) not null,
   log_date_ins timestamp,
   log_date_upd timestamp,
   log_user_ins varchar(100),
   log_user_upd varchar(100),
   codigo varchar(50) not null,
   descricao varchar(50) not null,
   dt_nascimento timestamp not null,
   constraint pk_test1 primary key (id)
);

create table test1_child (
   id varchar(36) not null,
   log_date_ins timestamp,
   log_date_upd timestamp,
   log_user_ins varchar(100),
   log_user_upd varchar(100),
   codigo varchar(50) not null,
   quantidade numeric(18, 6) not null,
   valor_total numeric(18, 2) not null,
   valor_unit numeric(18, 2) not null,
   test1_id varchar(36) not null,
   constraint pk_test1_child primary key (id)
);

alter table test1_child
  add constraint fk_test1_child_test1_id
  foreign key (test1_id)
  references test1;


alter table sys_unit add active varchar(1);

alter table sys_document_category add active varchar(1);

alter table sys_group_program RENAME CONSTRAINT fk_sys_group_program_system_group_id to fk_sys_group_program_sys_group_id;
alter table sys_group_program RENAME CONSTRAINT fk_sys_group_program_system_program_id to fk_sys_group_program_sys_program_id;

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
        `);
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(``);
  }
}
