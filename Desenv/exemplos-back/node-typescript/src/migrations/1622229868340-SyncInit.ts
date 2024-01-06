import {MigrationInterface, QueryRunner} from "typeorm";

export class SyncInit1622229868340 implements MigrationInterface {
    name = 'SyncInit1622229868340'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`CREATE TABLE "tenant" ("id" uuid NOT NULL DEFAULT uuid_generate_v4(), "name" character varying(50) NOT NULL, "active" character varying(1) NOT NULL, "log_user_ins" character varying, "log_date_ins" TIMESTAMP NOT NULL DEFAULT current_timestamp, "log_user_upd" character varying, "log_date_upd" TIMESTAMP NOT NULL DEFAULT current_timestamp, CONSTRAINT "PK_da8c6efd67bb301e810e56ac139" PRIMARY KEY ("id")); COMMENT ON COLUMN "tenant"."id" IS 'ID Tenant'; COMMENT ON COLUMN "tenant"."name" IS 'Name'; COMMENT ON COLUMN "tenant"."active" IS 'Active'; COMMENT ON COLUMN "tenant"."log_user_ins" IS 'Log User Insert'; COMMENT ON COLUMN "tenant"."log_date_ins" IS 'Log Date Insert'; COMMENT ON COLUMN "tenant"."log_user_upd" IS 'Log User Update'; COMMENT ON COLUMN "tenant"."log_date_upd" IS 'Log Date Update'`);
        await queryRunner.query(`CREATE TABLE "user" ("id" uuid NOT NULL DEFAULT uuid_generate_v4(), "firstname" character varying(50) NOT NULL, "lastname" character varying(50) NOT NULL, "username" character varying(255) NOT NULL, "email" text NOT NULL, "password" text NOT NULL, "role" character varying(50) NOT NULL DEFAULT 'user', "tenant_id" uuid, "log_user_ins" character varying, "log_date_ins" TIMESTAMP NOT NULL DEFAULT current_timestamp, "log_user_upd" character varying, "log_date_upd" TIMESTAMP NOT NULL DEFAULT current_timestamp, CONSTRAINT "UQ_78a916df40e02a9deb1c4b75edb" UNIQUE ("username"), CONSTRAINT "UQ_e12875dfb3b1d92d7d7c5377e22" UNIQUE ("email"), CONSTRAINT "PK_cace4a159ff9f2512dd42373760" PRIMARY KEY ("id")); COMMENT ON COLUMN "user"."id" IS 'ID Users'; COMMENT ON COLUMN "user"."firstname" IS 'Firt Name'; COMMENT ON COLUMN "user"."lastname" IS 'Last Name'; COMMENT ON COLUMN "user"."username" IS 'User Name'; COMMENT ON COLUMN "user"."email" IS 'Email'; COMMENT ON COLUMN "user"."role" IS 'Role'; COMMENT ON COLUMN "user"."tenant_id" IS 'ID Tenant'; COMMENT ON COLUMN "user"."log_user_ins" IS 'Log User Insert'; COMMENT ON COLUMN "user"."log_date_ins" IS 'Log Date Insert'; COMMENT ON COLUMN "user"."log_user_upd" IS 'Log User Update'; COMMENT ON COLUMN "user"."log_date_upd" IS 'Log Date Update'`);
        await queryRunner.query(`ALTER TABLE "user" ADD CONSTRAINT "fk_user_tenant_id" FOREIGN KEY ("tenant_id") REFERENCES "tenant"("id") ON DELETE NO ACTION ON UPDATE NO ACTION`);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`ALTER TABLE "user" DROP CONSTRAINT "fk_user_tenant_id"`);
        await queryRunner.query(`DROP TABLE "user"`);
        await queryRunner.query(`DROP TABLE "tenant"`);
    }

}
