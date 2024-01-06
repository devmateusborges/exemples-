import { MigrationInterface, QueryRunner } from 'typeorm';

export class m1638990508395 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`
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
            ALTER TABLE system_access_log OWNER TO postgres;
    `);
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(``);
  }
}
