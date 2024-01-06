import { MigrationInterface, QueryRunner } from 'typeorm';

export class m1638990763873 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`
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
        ALTER TABLE system_email_log OWNER TO postgres;
    `);
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(``);
  }
}
