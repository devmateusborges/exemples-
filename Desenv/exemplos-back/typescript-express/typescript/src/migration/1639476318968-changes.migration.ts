import { MigrationInterface, QueryRunner } from 'typeorm';

export class m1639476318968 implements MigrationInterface {
  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`
        ALTER TABLE "system_access_log" DROP COLUMN logout_time;
    `);
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(``);
  }
}
