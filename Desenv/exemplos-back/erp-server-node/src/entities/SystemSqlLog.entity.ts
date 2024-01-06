import { Column, Entity, Index } from 'typeorm';

import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_sql_log', ['id'], { unique: true })
@Entity('system_sql_log', { schema: 'public' })
export class SystemSqlLog extends BaseEntity {
  @Column('timestamp without time zone', { name: 'logdate' })
  logdate: Date;

  @Column('text', {
    name: 'login',
    nullable: true,
  })
  login: string;

  @Column('text', {
    name: 'database_name',
    nullable: true,
  })
  databaseName: string;

  @Column('text', {
    name: 'sql_command',
    nullable: true,
  })
  sqlCommand: string;

  @Column('text', {
    name: 'statement_type',
    nullable: true,
  })
  statementType: string;

  @Column('varchar', {
    name: 'access_ip',
    nullable: true,
    length: 45,
  })
  accessIp: string;

  @Column('text', {
    name: 'transaction_id',
    nullable: true,
  })
  transactionId: string;

  @Column('text', {
    name: 'log_trace',
    nullable: true,
  })
  logTrace: string;

  @Column('text', {
    name: 'session_id',
    nullable: true,
  })
  sessionId: string;

  @Column('text', {
    name: 'class_name',
    nullable: true,
  })
  className: string;

  @Column('text', {
    name: 'php_sapi',
    nullable: true,
  })
  phpSapi: string;

  @Column('text', {
    name: 'request_id',
    nullable: true,
  })
  requestId: string;

  @Column('varchar', {
    name: 'log_year',
    nullable: true,
    length: 4,
  })
  logYear: string;

  @Column('varchar', {
    name: 'log_month',
    nullable: true,
    length: 2,
  })
  logMonth: string;

  @Column('varchar', {
    name: 'log_day',
    nullable: true,
    length: 2,
  })
  logDay: string;
}
