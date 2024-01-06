import { Column, Entity, Index } from 'typeorm';

import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_access_log', ['id'], { unique: true })
@Entity('system_access_log', { schema: 'public' })
export class SystemAccessLog extends BaseEntity {
  @Column('text', {
    name: 'sessionid',
    nullable: false,
  })
  sessionid: string;

  @Column('text', {
    name: 'login',
    nullable: false,
  })
  login: string;

  @Column('varchar', {
    name: 'access_ip',
    nullable: true,
    length: 45,
  })
  access_ip: string;

  @Column('timestamp without time zone', { name: 'login_time', nullable: true })
  login_time: Date;

  @Column('varchar', {
    name: 'login_year',
    nullable: true,
    length: 4,
  })
  login_year: string;

  @Column('varchar', {
    name: 'login_month',
    nullable: true,
    length: 2,
  })
  login_month: string;

  @Column('varchar', {
    name: 'login_day',
    nullable: true,
    length: 2,
  })
  login_day: string;

  @Column('char', {
    name: 'impersonated',
    length: 1,
  })
  impersonated: string;
}
