import { Column, Entity, Index } from 'typeorm';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('system_migrations_pkey', ['version'], { unique: true })
@Entity('system_migrations', { schema: 'public' })
export class SystemMigrations extends BaseEntity {
  @Column('bigint', { primary: true, name: 'version' })
  version: string;

  @Column('varchar', {
    name: 'migration_name',
    nullable: true,
    length: 100,
  })
  migrationName: string;

  @Column('timestamp without time zone', { name: 'start_time', nullable: true })
  startTime: Date | null;

  @Column('timestamp without time zone', { name: 'end_time', nullable: true })
  endTime: Date | null;

  @Column('boolean', { name: 'breakpoint', default: () => 'false' })
  breakpoint: boolean;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;
}
