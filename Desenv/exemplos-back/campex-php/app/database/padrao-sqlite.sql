PRAGMA foreign_keys=OFF; 

CREATE TABLE adm_ccusto( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
      status varchar  (1)   NOT NULL  , 
 PRIMARY KEY (id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id)) ; 

CREATE TABLE pec_animal( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
      dt_entrada date   , 
      status varchar  (1)   , 
      dt_nascimento date   , 
      observacao text   , 
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
      vr_custo_entrada double   , 
      vr_custo_kg double   , 
      vr_custos_extra double   , 
      codigo_rastreio varchar  (50)   , 
 PRIMARY KEY (id),
FOREIGN KEY(pec_raca_id) REFERENCES pec_raca(id),
FOREIGN KEY(pec_pelagem_id) REFERENCES pec_pelagem(id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id),
FOREIGN KEY(pec_categoria_id) REFERENCES pec_categoria(id),
FOREIGN KEY(pec_brinco_id) REFERENCES pec_brinco(id),
FOREIGN KEY(pec_sisbov_id) REFERENCES pec_sisbov(id),
FOREIGN KEY(pec_lote_id) REFERENCES pec_lote(id),
FOREIGN KEY(pec_origem_id) REFERENCES pec_origem(id)) ; 

CREATE TABLE pec_brinco( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
 PRIMARY KEY (id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id)) ; 

CREATE TABLE pec_categoria( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
      pec_especie_id varchar  (36)   NOT NULL  , 
 PRIMARY KEY (id),
FOREIGN KEY(pec_especie_id) REFERENCES pec_especie(id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id)) ; 

CREATE TABLE pec_especie( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
      observacao text   , 
      tempo_gestacao int   , 
      primeira_cobertura int   , 
      diagnostico_apos_cobertura int   , 
      proximo_cruzamento int   , 
      tempo_lactacao int   , 
      idade_desmama int   , 
      nomenclatura_filhote int   , 
 PRIMARY KEY (id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id)) ; 

CREATE TABLE pec_finalidade( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
 PRIMARY KEY (id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id)) ; 

CREATE TABLE pec_lote( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   NOT NULL  , 
      max_animais int   NOT NULL  , 
      pec_finalidade_id varchar  (36)   NOT NULL  , 
 PRIMARY KEY (id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id),
FOREIGN KEY(pec_finalidade_id) REFERENCES pec_finalidade(id)) ; 

CREATE TABLE pec_origem( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
 PRIMARY KEY (id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id)) ; 

CREATE TABLE pec_pelagem( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
 PRIMARY KEY (id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id)) ; 

CREATE TABLE pec_raca( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      descricao varchar  (100)   , 
      pec_especie_id varchar  (36)   NOT NULL  , 
 PRIMARY KEY (id),
FOREIGN KEY(pec_especie_id) REFERENCES pec_especie(id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id)) ; 

CREATE TABLE pec_sisbov( 
      id varchar  (36)   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
      codigo varchar  (50)   NOT NULL  , 
      codigo_mae varchar  (50)   , 
      codigo_pai varchar  (50)   , 
      aptidao varchar  (100)   , 
      nirf_nascimento varchar  (50)   , 
      nirf_atual varchar  (50)   , 
      observacoes text   , 
 PRIMARY KEY (id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id)) ; 

CREATE TABLE system_document( 
      id int   NOT NULL  , 
      category_id int   NOT NULL  , 
      system_user_id int   , 
      title text   NOT NULL  , 
      description text   , 
      submission_date date   , 
      archive_date date   , 
      filename text   , 
 PRIMARY KEY (id),
FOREIGN KEY(category_id) REFERENCES system_document_category(id),
FOREIGN KEY(system_user_id) REFERENCES system_users(id)) ; 

CREATE TABLE system_document_category( 
      id int   NOT NULL  , 
      name text   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_document_group( 
      id int   NOT NULL  , 
      document_id int   NOT NULL  , 
      system_group_id int   NOT NULL  , 
 PRIMARY KEY (id),
FOREIGN KEY(document_id) REFERENCES system_document(id),
FOREIGN KEY(system_group_id) REFERENCES system_group(id)) ; 

CREATE TABLE system_document_user( 
      id int   NOT NULL  , 
      document_id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
 PRIMARY KEY (id),
FOREIGN KEY(document_id) REFERENCES system_document(id),
FOREIGN KEY(system_user_id) REFERENCES system_users(id)) ; 

CREATE TABLE system_group( 
      id int   NOT NULL  , 
      name text   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_group_program( 
      id int   NOT NULL  , 
      system_group_id int   NOT NULL  , 
      system_program_id int   NOT NULL  , 
 PRIMARY KEY (id),
FOREIGN KEY(system_program_id) REFERENCES system_program(id),
FOREIGN KEY(system_group_id) REFERENCES system_group(id)) ; 

CREATE TABLE system_message( 
      id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
      system_user_to_id int   NOT NULL  , 
      subject text   NOT NULL  , 
      message text   , 
      dt_message datetime   , 
      checked char  (1)   , 
 PRIMARY KEY (id),
FOREIGN KEY(system_user_id) REFERENCES system_users(id),
FOREIGN KEY(system_user_to_id) REFERENCES system_users(id)) ; 

CREATE TABLE system_notification( 
      id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
      system_user_to_id int   NOT NULL  , 
      subject text   , 
      message text   , 
      dt_message datetime   , 
      action_url text   , 
      action_label text   , 
      icon text   , 
      checked char  (1)   , 
 PRIMARY KEY (id),
FOREIGN KEY(system_user_id) REFERENCES system_users(id),
FOREIGN KEY(system_user_to_id) REFERENCES system_users(id)) ; 

CREATE TABLE system_preference( 
      id varchar  (255)   NOT NULL  , 
      preference text   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_program( 
      id int   NOT NULL  , 
      name text   NOT NULL  , 
      controller text   NOT NULL  , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_unit( 
      id int   NOT NULL  , 
      name text   NOT NULL  , 
      connection_name text   , 
 PRIMARY KEY (id)) ; 

CREATE TABLE system_user_group( 
      id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
      system_group_id int   NOT NULL  , 
 PRIMARY KEY (id),
FOREIGN KEY(system_group_id) REFERENCES system_group(id),
FOREIGN KEY(system_user_id) REFERENCES system_users(id)) ; 

CREATE TABLE system_user_program( 
      id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
      system_program_id int   NOT NULL  , 
 PRIMARY KEY (id),
FOREIGN KEY(system_user_id) REFERENCES system_users(id),
FOREIGN KEY(system_program_id) REFERENCES system_program(id)) ; 

CREATE TABLE system_users( 
      id int   NOT NULL  , 
      name text   NOT NULL  , 
      login text   NOT NULL  , 
      password text   NOT NULL  , 
      email text   , 
      frontpage_id int   , 
      system_unit_id int   , 
      active char  (1)   , 
 PRIMARY KEY (id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id),
FOREIGN KEY(frontpage_id) REFERENCES system_program(id)) ; 

CREATE TABLE system_user_unit( 
      id int   NOT NULL  , 
      system_user_id int   NOT NULL  , 
      system_unit_id int   NOT NULL  , 
 PRIMARY KEY (id),
FOREIGN KEY(system_user_id) REFERENCES system_users(id),
FOREIGN KEY(system_unit_id) REFERENCES system_unit(id)) ; 

 
 
  
