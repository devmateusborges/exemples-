import { MigrationInterface, QueryRunner } from 'typeorm';

export class systemChangeLog1638990744242 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`
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
        ALTER TABLE system_change_log OWNER TO postgres;
    `);
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(``);
  }
}
