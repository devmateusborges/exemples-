import { MigrationInterface, QueryRunner } from 'typeorm';

export class m1639502851174 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`
        alter table system_access_log drop column login;
        alter table system_access_log drop column sessionid;
        alter table system_access_log drop column impersonated;
        alter table system_access_log drop column login_year;
        alter table system_access_log drop column login_month;
        alter table system_access_log drop column login_day;
        `);

    await queryRunner.query(`
        ALTER TABLE "system_access_log" ADD system_user_id varchar(36) NOT NULL;
        ALTER TABLE "system_access_log" ADD unit_id varchar(36) NOT NULL;
        ALTER TABLE "system_access_log" ADD system_id varchar(36) NOT NULL;
        `);

    await queryRunner.query(`
        ALTER TABLE "system_access_log" add CONSTRAINT "fk_system_access_log_system_user_id" FOREIGN KEY (system_user_id) REFERENCES "system_user"(id);
        ALTER TABLE "system_access_log" add CONSTRAINT "fk_system_access_log_unit_id" FOREIGN KEY (unit_id) REFERENCES "system_unit"(id);
        ALTER TABLE "system_access_log" add CONSTRAINT "fk_system_access_log_system_id" FOREIGN KEY (system_id) REFERENCES "system"(id);
        `);

    await queryRunner.query(`
        ALTER TABLE "system_access_log" ALTER column login_time type timestamp(0);
        ALTER TABLE "system_access_log" ALTER column login_time set DEFAULT now();
    `);
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(``);
  }
}
