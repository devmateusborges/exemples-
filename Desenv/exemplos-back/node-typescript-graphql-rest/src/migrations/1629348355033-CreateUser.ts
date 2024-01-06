import { MigrationInterface, QueryRunner } from 'typeorm'

export class CreateUser1629348355033 implements MigrationInterface {
  name = 'CreateUser1629348355033'

  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(
      `CREATE TABLE "users" ("id" uuid NOT NULL DEFAULT uuid_generate_v4(), "firstname" character varying(50) NOT NULL, "lastname" character varying(50) NOT NULL, "username" character varying(255) NOT NULL, "email" text NOT NULL, "password" text NOT NULL, "log_user_ins" character varying, "log_date_ins" TIMESTAMP NOT NULL DEFAULT now(), "log_user_upd" character varying, "log_date_upd" TIMESTAMP NOT NULL DEFAULT now(), CONSTRAINT "UQ_fe0bb3f6520ee0469504521e710" UNIQUE ("username"), CONSTRAINT "UQ_97672ac88f789774dd47f7c8be3" UNIQUE ("email"), CONSTRAINT "PK_a3ffb1c0c8416b9fc6f907b7433" PRIMARY KEY ("id")); COMMENT ON COLUMN "users"."id" IS 'ID Users'; COMMENT ON COLUMN "users"."firstname" IS 'Firt Name'; COMMENT ON COLUMN "users"."lastname" IS 'Last Name'; COMMENT ON COLUMN "users"."username" IS 'User Name'; COMMENT ON COLUMN "users"."email" IS 'Email'; COMMENT ON COLUMN "users"."log_user_ins" IS 'Log User Insert'; COMMENT ON COLUMN "users"."log_date_ins" IS 'Log Date Insert'; COMMENT ON COLUMN "users"."log_user_upd" IS 'Log User Update'; COMMENT ON COLUMN "users"."log_date_upd" IS 'Log Date Update'`
    )
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(`DROP TABLE "users"`)
  }
}
