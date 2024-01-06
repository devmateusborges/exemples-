import { MigrationInterface, QueryRunner } from 'typeorm';

export class m1638990775691 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`
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
        ALTER TABLE system_sql_log OWNER TO postgres;
    `);
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(``);
  }
}
