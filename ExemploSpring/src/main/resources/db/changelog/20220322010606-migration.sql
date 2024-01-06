
            
DROP TABLE system_notification;;
DROP TABLE system_request_log;;
DROP TABLE system_access_log;;
DROP TABLE system_change_log;;
DROP TABLE system_email_log;;
DROP TABLE system_sql_log;;

CREATE TABLE crm_org_system_user (
id varchar(36) COLLATE pg_catalog.default NOT NULL);

alter table crm_mov ADD column titulo varchar(200);
COMMENT ON COLUMN crm_mov.titulo IS 'Título da movimentação';


CREATE TABLE system_access_log (
        id varchar(36) NOT NULL,
        sessionid text ,
        login text ,
        login_time timestamp(6),
        login_year varchar(4) ,
        login_month varchar(2) ,
        login_day varchar(2) ,
        logout_time timestamp(6),
        impersonated char(1) ,
        access_ip varchar(45) ,
        CONSTRAINT pk_system_access_log PRIMARY KEY (id) 
        )
        WITHOUT OIDS;
        COMMENT ON TABLE system_access_log IS 'System-Log de Acesso';
        COMMENT ON COLUMN system_access_log.id IS 'ID do Log da Sessão';
        COMMENT ON COLUMN system_access_log.sessionid IS 'ID da Sessão';
        COMMENT ON COLUMN system_access_log.login IS 'Login';
        COMMENT ON COLUMN system_access_log.login_time IS 'Hora de Login';
        COMMENT ON COLUMN system_access_log.login_year IS 'Ano de Login';
        COMMENT ON COLUMN system_access_log.login_month IS 'Mês de Login';
        COMMENT ON COLUMN system_access_log.login_day IS 'Dia de Login';
        COMMENT ON COLUMN system_access_log.logout_time IS 'Hora Logout';
        COMMENT ON COLUMN system_access_log.impersonated IS 'Personificado';
        COMMENT ON COLUMN system_access_log.access_ip IS 'IP de Acesso';
        ALTER TABLE system_access_log OWNER TO postgres;;


    CREATE TABLE system_change_log (
    id varchar(36) NOT NULL,
    logdate timestamp(6),
    login text ,
    tablename text ,
    primarykey text ,
    pkvalue text ,
    operation text ,
    columnname text ,
    oldvalue text ,
    newvalue text ,
    access_ip text ,
    transaction_id text ,
    log_trace text ,
    session_id text ,
    class_name text ,
    php_sapi text ,
    log_year varchar(4) ,
    log_month varchar(2) ,
    log_day varchar(2) ,
    CONSTRAINT pk_system_change_log PRIMARY KEY (id) 
    )
    WITHOUT OIDS;
    COMMENT ON TABLE system_change_log IS 'System-Log de Alterações';
    COMMENT ON COLUMN system_change_log.id IS 'ID do Log de Alterações';
    COMMENT ON COLUMN system_change_log.logdate IS 'Data do Log';
    COMMENT ON COLUMN system_change_log.login IS 'Login';
    COMMENT ON COLUMN system_change_log.tablename IS 'Nome da Tabela';
    COMMENT ON COLUMN system_change_log.primarykey IS 'Chave Primária';
    COMMENT ON COLUMN system_change_log.pkvalue IS 'Valor da Chave';
    COMMENT ON COLUMN system_change_log.operation IS 'Operação';
    COMMENT ON COLUMN system_change_log.columnname IS 'Nome da Coluna';
    COMMENT ON COLUMN system_change_log.oldvalue IS 'Valor Antigo';
    COMMENT ON COLUMN system_change_log.newvalue IS 'Valor Novo';
    COMMENT ON COLUMN system_change_log.access_ip IS 'IP do Acesso';
    COMMENT ON COLUMN system_change_log.transaction_id IS 'ID da Transação';
    COMMENT ON COLUMN system_change_log.log_trace IS 'Log do Trace';
    COMMENT ON COLUMN system_change_log.session_id IS 'ID da Sessão';
    COMMENT ON COLUMN system_change_log.class_name IS 'Nome da Classe';
    COMMENT ON COLUMN system_change_log.php_sapi IS 'PHP Sapi';
    COMMENT ON COLUMN system_change_log.log_year IS 'Ano do Log';
    COMMENT ON COLUMN system_change_log.log_month IS 'Mês do Log';
    COMMENT ON COLUMN system_change_log.log_day IS 'Dia do Log';
    ALTER TABLE system_change_log OWNER TO postgres;;

    CREATE TABLE system_email_log (
    unit_id varchar(36),
    id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
    type_in_out varchar(2) NOT NULL,
    date_log timestamp(6) NOT NULL DEFAULT now(),
    email_from text NOT NULL,
    subject text NOT NULL,
    body text,
    error_message text,
    email_to text NOT NULL,
    login varchar(50),
    date_send timestamp(6),
    body_type varchar(50),
    log_user_ins varchar(100),
    log_date_ins timestamp(0) DEFAULT now(),
    log_user_upd varchar(100),
    log_date_upd timestamp(0),
    CONSTRAINT pk_system_email_log PRIMARY KEY (id) 
    )
    WITHOUT OIDS;
    COMMENT ON TABLE system_email_log IS 'System-Log de envio de Email';
    COMMENT ON COLUMN system_email_log.unit_id IS 'ID da Unidade';
    COMMENT ON COLUMN system_email_log.id IS 'ID do Log de envio de Email';
    COMMENT ON COLUMN system_email_log.type_in_out IS 'Tipo Entrada ou Saída';
    COMMENT ON COLUMN system_email_log.date_log IS 'Data/Hora do Log';
    COMMENT ON COLUMN system_email_log.email_from IS 'Email - De';
    COMMENT ON COLUMN system_email_log.subject IS 'Assunto';
    COMMENT ON COLUMN system_email_log.body IS 'Corpo';
    COMMENT ON COLUMN system_email_log.error_message IS 'Mensagem de Erro';
    COMMENT ON COLUMN system_email_log.email_to IS 'Email - Para';
    COMMENT ON COLUMN system_email_log.login IS 'Login';
    COMMENT ON COLUMN system_email_log.date_send IS 'Data/Hora de Envio';
    COMMENT ON COLUMN system_email_log.body_type IS 'Tipo do Corpo: text;html';
    COMMENT ON COLUMN system_email_log.log_user_ins IS 'Log - Usuário de Inserção';
    COMMENT ON COLUMN system_email_log.log_date_ins IS 'Log - Data de Inserção';
    COMMENT ON COLUMN system_email_log.log_user_upd IS 'Log - Usuário de Alteração';
    COMMENT ON COLUMN system_email_log.log_date_upd IS 'Log - Data de Alteração';
    ALTER TABLE system_email_log OWNER TO postgres;;


    CREATE TABLE system_sql_log (
    id varchar(36) NOT NULL,
    logdate timestamp(6),
    login text ,
    database_name text ,
    sql_command text ,
    statement_type text ,
    access_ip varchar(45) ,
    transaction_id text ,
    log_trace text ,
    session_id text ,
    class_name text ,
    php_sapi text ,
    request_id text ,
    log_year varchar(4) ,
    log_month varchar(2) ,
    log_day varchar(2) ,
    CONSTRAINT pk_system_sql_log PRIMARY KEY (id) 
    )
    WITHOUT OIDS;
    COMMENT ON TABLE system_sql_log IS 'System-Log de SQL';
    COMMENT ON COLUMN system_sql_log.id IS 'ID do Log de SQL';
    COMMENT ON COLUMN system_sql_log.logdate IS 'Data do Log';
    COMMENT ON COLUMN system_sql_log.login IS 'Login';
    COMMENT ON COLUMN system_sql_log.database_name IS 'Nome do Banco de Dados';
    COMMENT ON COLUMN system_sql_log.sql_command IS 'Comando SQL';
    COMMENT ON COLUMN system_sql_log.statement_type IS 'Comando Tipo';
    COMMENT ON COLUMN system_sql_log.access_ip IS 'IP de Acesso';
    COMMENT ON COLUMN system_sql_log.transaction_id IS 'ID da Transação';
    COMMENT ON COLUMN system_sql_log.log_trace IS 'Log do Trace';
    COMMENT ON COLUMN system_sql_log.session_id IS 'ID da Sessão';
    COMMENT ON COLUMN system_sql_log.class_name IS 'Nome da Classe';
    COMMENT ON COLUMN system_sql_log.php_sapi IS 'PHP Sapi';
    COMMENT ON COLUMN system_sql_log.request_id IS 'ID da Request';
    COMMENT ON COLUMN system_sql_log.log_year IS 'Ano do Log';
    COMMENT ON COLUMN system_sql_log.log_month IS 'Mês do Log';
    COMMENT ON COLUMN system_sql_log.log_day IS 'Dia do Log';
    ALTER TABLE system_sql_log OWNER TO postgres;;

    alter table system_access_log alter column id set default uuid_generate_v4();
    alter table system_change_log alter column id set default uuid_generate_v4();
    alter table system_sql_log alter column id set default uuid_generate_v4();

    ALTER TABLE system_access_log DROP COLUMN logout_time;

            alter table system_access_log drop column login;
    alter table system_access_log drop column sessionid;
    alter table system_access_log drop column impersonated;
    alter table system_access_log drop column login_year;
    alter table system_access_log drop column login_month;
    alter table system_access_log drop column login_day;

            ALTER TABLE system_access_log ADD system_user_id varchar(36) NOT NULL;
    ALTER TABLE system_access_log ADD unit_id varchar(36) NOT NULL;
    ALTER TABLE system_access_log ADD system_id varchar(36) NOT NULL;

            ALTER TABLE system_access_log add CONSTRAINT fk_system_access_log_system_user_id FOREIGN KEY (system_user_id) REFERENCES system_user(id);
    ALTER TABLE system_access_log add CONSTRAINT fk_system_access_log_unit_id FOREIGN KEY (unit_id) REFERENCES system_unit(id);
    ALTER TABLE system_access_log add CONSTRAINT fk_system_access_log_system_id FOREIGN KEY (system_id) REFERENCES system(id);

            ALTER TABLE system_access_log ALTER column login_time type timestamp(0);
    ALTER TABLE system_access_log ALTER column login_time set DEFAULT now();


    drop table crm_org_system_user;
