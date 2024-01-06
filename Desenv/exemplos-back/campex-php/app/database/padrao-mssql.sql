CREATE TABLE adm_ccusto( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
      status varchar  (1)   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE pec_animal( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
      dt_entrada date   , 
      status varchar  (1)   , 
      dt_nascimento date   , 
      observacao nvarchar(max)   , 
      pec_raca_id varchar  (36)   NOT NULL  , 
      pec_pelagem_id varchar  (36)   NOT NULL  , 
      pec_categoria_id varchar  (36)   NOT NULL  , 
      pec_brinco_id varchar  (36)   NOT NULL  , 
      pec_sisbov_id varchar  (36)   NOT NULL  , 
      pec_animal_id_pai varchar  (36)   , 
      pec_animal_id_mae varchar  (36)   , 
      pec_lote_id varchar  (36)   NOT NULL  , 
      pec_origem_id varchar  (36)   NOT NULL  , 
      rgn varchar  (50)   , 
      rgd varchar  (50)   , 
      dt_desmama date   , 
      vr_custo_entrada float   , 
      vr_custo_kg float   , 
      vr_custos_extra float   , 
      codigo_rastreio varchar  (50)   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE pec_brinco( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE pec_categoria( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
      pec_especie_id varchar  (36)   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE pec_especie( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
      observacao nvarchar(max)   , 
      tempo_gestacao int   , 
      primeira_cobertura int   , 
      diagnostico_apos_cobertura int   , 
      proximo_cruzamento int   , 
      tempo_lactacao int   , 
      idade_desmama int   , 
      nomenclatura_filhote int   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE pec_finalidade( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE pec_lote( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   NOT NULL  , 
      max_animais int   NOT NULL  , 
      pec_finalidade_id varchar  (36)   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE pec_origem( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE pec_pelagem( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE pec_raca( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
      pec_especie_id varchar  (36)   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE pec_sisbov( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      codigo_mae varchar  (50)   , 
      codigo_pai varchar  (50)   , 
      aptidao varchar  (100)   , 
      nirf_nascimento varchar  (50)   , 
      nirf_atual varchar  (50)   , 
      observacoes nvarchar(max)   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_document( 
      id int   NOT NULL  , 
      category_id int   NOT NULL  , 
      system_user_id int   , 
      title nvarchar(max)   NOT NULL  , 
      description nvarchar(max)   , 
      submission_date date   , 
      archive_date date   , 
      filename nvarchar(max)   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_document_category( 
      id int   NOT NULL  , 
      name nvarchar(max)   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_document_group( 
      id int   NOT NULL  , 
      document_id int   NOT NULL  , 
      system_group_id int   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_document_user( 
      id int   NOT NULL  , 
      document_id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_group( 
      id int   NOT NULL  , 
      name nvarchar(max)   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_group_program( 
      id int   NOT NULL  , 
      system_group_id int   NOT NULL  , 
      system_program_id int   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_message( 
      id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
      system_user_to_id int   NOT NULL  , 
      subject nvarchar(max)   NOT NULL  , 
      message nvarchar(max)   , 
      dt_message datetime2   , 
      checked char  (1)   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_notification( 
      id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
      system_user_to_id int   NOT NULL  , 
      subject nvarchar(max)   , 
      message nvarchar(max)   , 
      dt_message datetime2   , 
      action_url nvarchar(max)   , 
      action_label nvarchar(max)   , 
      icon nvarchar(max)   , 
      checked char  (1)   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_preference( 
      id varchar  (255)   NOT NULL  , 
      preference nvarchar(max)   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_program( 
      id int   NOT NULL  , 
      name nvarchar(max)   NOT NULL  , 
      controller nvarchar(max)   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_unit( 
      id int   NOT NULL  , 
      name nvarchar(max)   NOT NULL  , 
      connection_name nvarchar(max)   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_user_group( 
      id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
      system_group_id int   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_user_program( 
      id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
      system_program_id int   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_users( 
      id int   NOT NULL  , 
      name nvarchar(max)   NOT NULL  , 
      login nvarchar(max)   NOT NULL  , 
      password nvarchar(max)   NOT NULL  , 
      email nvarchar(max)   , 
      frontpage_id int   , 
      system_unit_id int   , 
      active char  (1)   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_user_unit( 
      id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
 PRIMARY KEY (id)) ; 

 
  
 ALTER TABLE adm_ccusto ADD CONSTRAINT fk_adm_ccusto_unit FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE pec_animal ADD CONSTRAINT fk_pec_animal_pec_raca FOREIGN KEY (pec_raca_id) references pec_raca(id); 
ALTER TABLE pec_animal ADD CONSTRAINT fk_pec_animal_pec_pelagem FOREIGN KEY (pec_pelagem_id) references pec_pelagem(id); 
ALTER TABLE pec_animal ADD CONSTRAINT fk_pec_animal_unit FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE pec_animal ADD CONSTRAINT fk_pec_animal_pec_categoria FOREIGN KEY (pec_categoria_id) references pec_categoria(id); 
ALTER TABLE pec_animal ADD CONSTRAINT fk_pec_animal_pec_brinco FOREIGN KEY (pec_brinco_id) references pec_brinco(id); 
ALTER TABLE pec_animal ADD CONSTRAINT fk_pec_animal_pec_sisbov FOREIGN KEY (pec_sisbov_id) references pec_sisbov(id); 
ALTER TABLE pec_animal ADD CONSTRAINT fk_pec_animal_pec_lote FOREIGN KEY (pec_lote_id) references pec_lote(id); 
ALTER TABLE pec_animal ADD CONSTRAINT fk_pec_animal_pec_origem FOREIGN KEY (pec_origem_id) references pec_origem(id); 
ALTER TABLE pec_brinco ADD CONSTRAINT fk_pec_brinco_unit FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE pec_categoria ADD CONSTRAINT fk_pec_categoria_pec_especie FOREIGN KEY (pec_especie_id) references pec_especie(id); 
ALTER TABLE pec_categoria ADD CONSTRAINT fk_pec_categoria_unit FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE pec_especie ADD CONSTRAINT fk_pec_especie_unit FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE pec_finalidade ADD CONSTRAINT fk_pec_finalidade_unit FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE pec_lote ADD CONSTRAINT fk_pec_lote_unit FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE pec_lote ADD CONSTRAINT fk_pec_lote_pec_finalidade FOREIGN KEY (pec_finalidade_id) references pec_finalidade(id); 
ALTER TABLE pec_origem ADD CONSTRAINT fk_pec_origem_unit FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE pec_pelagem ADD CONSTRAINT fk_pec_pelagem_unit FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE pec_raca ADD CONSTRAINT fk_pec_raca_pec_especie FOREIGN KEY (pec_especie_id) references pec_especie(id); 
ALTER TABLE pec_raca ADD CONSTRAINT fk_pec_raca_unit FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE pec_sisbov ADD CONSTRAINT fk_pec_sisbov_unit FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE system_document ADD CONSTRAINT fk_system_document_2 FOREIGN KEY (category_id) references system_document_category(id); 
ALTER TABLE system_document ADD CONSTRAINT fk_system_document_1 FOREIGN KEY (system_user_id) references system_users(id); 
ALTER TABLE system_document_group ADD CONSTRAINT fk_system_document_group_2 FOREIGN KEY (document_id) references system_document(id); 
ALTER TABLE system_document_group ADD CONSTRAINT fk_system_document_group_1 FOREIGN KEY (system_group_id) references system_group(id); 
ALTER TABLE system_document_user ADD CONSTRAINT fk_system_document_user_2 FOREIGN KEY (document_id) references system_document(id); 
ALTER TABLE system_document_user ADD CONSTRAINT fk_system_document_user_1 FOREIGN KEY (system_user_id) references system_users(id); 
ALTER TABLE system_group_program ADD CONSTRAINT fk_system_group_program_1 FOREIGN KEY (system_program_id) references system_program(id); 
ALTER TABLE system_group_program ADD CONSTRAINT fk_system_group_program_2 FOREIGN KEY (system_group_id) references system_group(id); 
ALTER TABLE system_message ADD CONSTRAINT fk_system_message_1 FOREIGN KEY (system_user_id) references system_users(id); 
ALTER TABLE system_message ADD CONSTRAINT fk_system_message_2 FOREIGN KEY (system_user_to_id) references system_users(id); 
ALTER TABLE system_notification ADD CONSTRAINT fk_system_notification_1 FOREIGN KEY (system_user_id) references system_users(id); 
ALTER TABLE system_notification ADD CONSTRAINT fk_system_notification_2 FOREIGN KEY (system_user_to_id) references system_users(id); 
ALTER TABLE system_user_group ADD CONSTRAINT fk_system_user_group_1 FOREIGN KEY (system_group_id) references system_group(id); 
ALTER TABLE system_user_group ADD CONSTRAINT fk_system_user_group_2 FOREIGN KEY (system_user_id) references system_users(id); 
ALTER TABLE system_user_program ADD CONSTRAINT fk_system_user_program_2 FOREIGN KEY (system_user_id) references system_users(id); 
ALTER TABLE system_user_program ADD CONSTRAINT fk_system_user_program_1 FOREIGN KEY (system_program_id) references system_program(id); 
ALTER TABLE system_users ADD CONSTRAINT fk_system_user_1 FOREIGN KEY (system_unit_id) references system_unit(id); 
ALTER TABLE system_users ADD CONSTRAINT fk_system_user_2 FOREIGN KEY (frontpage_id) references system_program(id); 
ALTER TABLE system_user_unit ADD CONSTRAINT fk_system_user_unit_1 FOREIGN KEY (system_user_id) references system_users(id); 
ALTER TABLE system_user_unit ADD CONSTRAINT fk_system_user_unit_2 FOREIGN KEY (system_unit_id) references system_unit(id); 

  
