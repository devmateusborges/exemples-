import { BeforeInsert, Column, Entity, Index } from 'typeorm';

import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_email_log', ['id'], { unique: true })
@Entity('system_email_log', { schema: 'public' })
export class SystemEmailLog extends BaseEntity {
  @Column('varchar', {
    name: 'unit_id',
    nullable: true,
    length: 36,
  })
  unitId: string;

  @Column('varchar', {
    name: 'type_in_out',
    nullable: false,
    length: 2,
  })
  typeInOut: string;

  @Column('timestamp without time zone', { name: 'date_log' })
  dateLog: Date;

  @Column('text', {
    name: 'email_from',
    nullable: false,
  })
  emailFrom: string;

  @Column('text', {
    name: 'subject',
    nullable: false,
  })
  subject: string;

  @Column('text', {
    name: 'body',
    nullable: true,
  })
  body: string;

  @Column('text', {
    name: 'error_message',
    nullable: true,
  })
  errorMessage: string;

  @Column('text', {
    name: 'email_to',
    nullable: false,
  })
  emailTo: string;

  @Column('varchar', {
    name: 'login',
    nullable: true,
    length: 50,
  })
  login: string;

  @Column('timestamp without time zone', { name: 'date_send' })
  dateSend: Date;

  @Column('varchar', {
    name: 'body_type',
    nullable: true,
    length: 50,
  })
  bodyType: string;

}
