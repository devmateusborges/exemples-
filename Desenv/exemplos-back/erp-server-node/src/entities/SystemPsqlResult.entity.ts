import { Column, Entity, Index } from 'typeorm';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('system_psql_result_pkey', ['id'], { unique: true })
@Entity('system_psql_result', { schema: 'public' })
export class SystemPsqlResult extends BaseEntity {
  @Column('varchar', { name: 'system_user_id', length: 36 })
  systemUserId: string;

  @Column('timestamp without time zone', {
    name: 'dt_hr',
    default: () => 'now()',
  })
  dtHr: Date;

  @Column('varchar', {
    name: 'status',
    length: 1,
    default: () => "'S'",
  })
  status: string;

  @Column('text', { name: 'resultado', nullable: true })
  resultado: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;
}
