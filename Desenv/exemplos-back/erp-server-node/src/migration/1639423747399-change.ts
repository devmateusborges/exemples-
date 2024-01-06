import { MigrationInterface, QueryRunner } from 'typeorm';

export class change1639423747399 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`
        alter table "system_access_log" alter column id set default uuid_generate_v4();
        alter table "system_change_log" alter column id set default uuid_generate_v4();
        alter table "system_sql_log" alter column id set default uuid_generate_v4();
    `);
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(``);
  }
}
