import { Column, Entity, Index } from 'typeorm';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_preference', ['id'], { unique: true })
@Entity('system_preference', { schema: 'public' })
export class SystemPreference extends BaseEntity {
  @Column('text', { name: 'value', nullable: true })
  value: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;
}
