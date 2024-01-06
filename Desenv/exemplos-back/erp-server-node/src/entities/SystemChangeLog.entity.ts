import { Column, Entity, Index } from 'typeorm';

import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_change_log', ['id'], { unique: true })
@Entity('system_change_log', { schema: 'public' })
export class SystemChangeLog extends BaseEntity {
  @Column('timestamp without time zone', { name: 'logdate' })
  logdate: Date;

  @Column('text', {
    name: 'login',
    nullable: true,
  })
  login: string;

  @Column('text', {
    name: 'tablename',
    nullable: true,
  })
  tablename: string;

  @Column('text', {
    name: 'primarykey',
    nullable: true,
  })
  primarykey: string;

  @Column('text', {
    name: 'pkvalue',
    nullable: true,
  })
  pkvalue: string;

  @Column('text', {
    name: 'operation',
    nullable: true,
  })
  operation: string;

  @Column('text', {
    name: 'columnname',
    nullable: true,
  })
  columnname: string;

  @Column('text', {
    name: 'oldvalue',
    nullable: true,
  })
  oldvalue: string;

  @Column('text', {
    name: 'newvalue',
    nullable: true,
  })
  newvalue: string;

  @Column('text', {
    name: 'access_ip',
    nullable: true,
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
